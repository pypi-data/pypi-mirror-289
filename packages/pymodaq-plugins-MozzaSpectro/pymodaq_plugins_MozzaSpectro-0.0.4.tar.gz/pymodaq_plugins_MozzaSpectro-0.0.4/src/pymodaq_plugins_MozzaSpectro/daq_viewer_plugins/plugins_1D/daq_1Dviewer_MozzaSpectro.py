from qtpy import QtWidgets
from pymodaq.control_modules.viewer_utility_classes import DAQ_Viewer_base, comon_parameters, main
import numpy as np
from collections import OrderedDict
from pymodaq.utils.daq_utils import ThreadCommand, getLineInfo
from pymodaq.utils.data import DataFromPlugins, Axis, DataToExport
import sys
import time
from libmozza import mozza_defines as MD
from libmozza.mozza import MozzaUSB, MozzaError

class DAQ_1DViewer_Mozza(DAQ_Viewer_base):
    """PyMoDAQ plugin controlling Mozza spectrometers using the Mozza SDK"""

    params = comon_parameters + [
        {'title': 'Trigger Frequency (Hz):', 'name': 'trigger_freq', 'type': 'int', 'value': 10000},
        {'title': 'Wavenumber Start:', 'name': 'wavenumber_start', 'type': 'float', 'value': 2000},
        {'title': 'Wavenumber End:', 'name': 'wavenumber_end', 'type': 'float', 'value': 6000},
    ]

    def ini_attributes(self):
        self.controller = None
        self.serials = []

    def commit_settings(self, param):
        if param.name() in ['trigger_freq', 'wavenumber_start', 'wavenumber_end']:
            self.initialize_controller()

    def ini_detector(self, controller=None):
        if self.settings['controller_status'] == "Slave":
            if controller is None:
                raise Exception('No controller has been defined externally while this axe is a slave one')
            else:
                self.controller = controller
        else:  # Master stage
            self.initialize_controller()
            if self.controller is None:
                return '', False

        initialized = True
        info = 'Detector initialized successfully'
        return info, initialized

    def initialize_controller(self):
        try:
            self.controller = MozzaUSB()
            self.serials = self.controller.get_serials()
            if self.serials:
                self.controller.connect(serial=self.serials[0])
                wls_nm = (self.settings.child('wavenumber_start').value(), self.settings.child('wavenumber_end').value())
                wnums = np.arange(1e7 / wls_nm[1], 1e7 / wls_nm[0], 5)
                self.controller.set_wavenumber_array(wnums)
                self.controller.acquisition_params.trigger_source = MD.INTERNAL
                self.controller.acquisition_params.trigger_frequency_Hz = self.settings.child('trigger_freq').value()
                self.controller.set_auto_params()
                print('Connected to Mozza device')
            else:
                print('No Mozza device found')
                self.controller = None
        except MozzaError as e:
            print(f"Failed to connect to Mozza device: {e}")
            self.controller = None

    def get_xaxis(self, ind_spectro):
        try:
            return self.controller.acquisition_params.wavenumber_array
        except Exception as e:
            print(f"Failed to get wavenumber array: {e}")
            return np.array([])

    def close(self):
        if self.controller is not None:
            self.controller.end_acquisition()
            self.controller.disconnect()

    def grab_data(self, Naverage=1, **kwargs):
        dte = DataToExport('Mozza')

        if self.controller:
            try:
                bytes_to_read = self.controller.begin_acquisition()
                raw = self.controller.read_raw()
                signal, reference = self.controller.separate_sig_ref(raw)
                self.controller.end_acquisition()
                spectrum = self.controller.process_spectrum(sig_data=signal, ref_data=reference)

                wnums = self.get_xaxis(0)
                dte.append(DataFromPlugins(name='Mozza', data=[spectrum], dim='Data1D',
                                           axes=[Axis(data=wnums, label='Wavenumber', units='cm^-1')]))
                QtWidgets.QApplication.processEvents()
            except MozzaError as e:
                print(f"Failed to acquire data: {e}")

        self.dte_signal.emit(dte)

    def stop(self):
        # No specific stop function provided in example script, assuming end_acquisition is called
        if self.controller is not None:
            try:
                self.controller.end_acquisition()
            except MozzaError as e:
                print(f"Failed to stop acquisition: {e}")

if __name__ == '__main__':
    main(__file__)
