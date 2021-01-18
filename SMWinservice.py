import socket

import win32serviceutil

import servicemanager
import win32event
import win32service

        
class SMWinservice(win32serviceutil.ServiceFramework):
    

    _svc_name_ = 'OEOEOEOEOEOEOE'
    _svc_display_name_ = 'TEST Service'
    _svc_description_ = 'TEST Service Description'

    @classmethod
    def parse_command_line(cls):
        
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
       
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def start(self):
        '''
        Si on veut faire kekchose lors du démarrage (certainement le test micro)
        eg. running condition
        '''
        pass

    def stop(self):
        '''
        Si on veut faire kekchose lors de la fin (certainement l'envoi)
        eg. invalidating running condition
        '''
        pass

    def main(self):
        '''
        Main class to be ovverridden 
        '''
        pass


if __name__ == '__main__':
    SMWinservice.parse_command_line()