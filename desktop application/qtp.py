import win32com, win32com.client
import time
import os

for i in range(1,10000):
    qtp = win32com.client.Dispatch("QuickTest.Application")
    # starts up QTP
    qtp.Launch()
    # make the QTP window visible
    qtp.Visible = True
    # Open a test, replace the path
    qtp.Open("D:\\script\\test2")
    # to open a QTP test in Quality Center
    # qtp.Open(r"[QualityCenter] Subject\FolderName\QTPScript")
    # create a RunResultsOptions object
    qtResultsOpt = win32com.client.Dispatch("QuickTest.RunResultsOptions")
    # set the location to where the results will be save
    qtResultsOpt.ResultsLocation = "C:\\Test\\testFlight\\Res1"
    qtp.Test.Run(qtResultsOpt)
    print "Test has %s" %qtp.Test.LastRunResults.Status
    # close the Test
    qtp.Test.Close()
    # quit QTP
    qtp.Quit()

