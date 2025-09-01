from doctest import OutputChecker
import os
import sys

TargetExePath = ''
InterMediateFilePath = ''
SourceFilePath = ''
OutPutFilePath = ''
OutPutFilePath2 = ''
OutPutFilePath3 = ''
OutPutFilePath4 = ''
OutPutFilePath5 = ''
OutPutFilePath6 = ''
OutPutFilePath7 = ''
OutPutFilePath8 = ''
OutPutFilePath9 = ''
OutPutFilePath10 = ''
OutPutFilePath11 = ''
OutPutFilePath12 = ''
OutputFilePath13 = ''
OutputFilePath14 = ''
OutputFilePath15 = ''
OutputFilePath16 = ''
OutputFilePath17 = ''
OutputFilePath18 = ''
OutPutPicNumConfigFilePath = ''
OutPutPicNumConfigFilePath2 = ''
Mod = ''
StartSourceFileNo = ''
StopSourceFileNo = ''
SourceFileType = 0

def Run2(SourceFileDirPath, TargetFileDirPath):
     print("123")
     for ipath in os.listdir(SourceFileDirPath):
        SourceFile = os.path.join(SourceFileDirPath, ipath)
        #print(fulldir)
        if os.path.isfile(SourceFile):
            STR = TargetExePath + ' ' + InterMediateFilePath + ' ' + SourceFile + ' ' + OutPutFilePath + ' ' + OutPutFilePath2 + ' ' + OutPutFilePath3 + ' ' + OutPutFilePath4 + ' ' + OutPutFilePath5 + ' ' + OutPutFilePath6 + ' ' + OutPutFilePath7 + ' ' + OutPutFilePath8 + ' ' + OutPutFilePath9 + ' ' + OutPutFilePath10 + ' ' + OutPutFilePath11 + ' ' + OutPutPicNumConfigFilePath + ' ' + OutPutPicNumConfigFilePath2 + ' ' + OutPutFilePath12 + ' ' + OutPutFilePath13 + ' ' + OutPutFilePath14 + ' ' + OutPutFilePath15 + ' ' + OutPutFilePath16 + ' ' + OutPutFilePath17 + ' ' + Mod + ' ' + TargetFileDirPath
            print(SourceFile)
            #print(STR)
            os.system(STR)

def Run():
    CSuffix = '.c'
    CPPSuffix = '.cpp'
    SourceFile = ''
    for i in range(int(StartSourceFileNo), int(StopSourceFileNo)):

        if SourceFileType == 1:
            SourceFile = SourceFilePath + str(i) + CSuffix
        elif SourceFileType == 2:
             SourceFile = SourceFilePath + str(i) + CPPSuffix
        
        STR = TargetExePath + ' ' + InterMediateFilePath + ' ' + SourceFile + ' ' + OutPutFilePath + ' ' + OutPutFilePath2 + ' ' + OutPutFilePath3 + ' ' + OutPutFilePath4 + ' ' + OutPutFilePath5 + ' ' + OutPutFilePath6 + ' ' + OutPutFilePath7 + ' ' + OutPutFilePath8 + ' ' + OutPutFilePath9 + ' ' + OutPutFilePath10 + ' ' + OutPutFilePath11 + ' ' + OutPutPicNumConfigFilePath + ' ' + OutPutPicNumConfigFilePath2 + ' ' + OutPutFilePath12 + ' ' + OutPutFilePath13 + ' ' + OutPutFilePath14 + ' ' + OutPutFilePath15 + ' ' + OutPutFilePath16 + ' ' + OutPutFilePath17 + ' ' + Mod + ' ' + OutPutFilePath18
        
        print(SourceFile)
        #print(STR)
        os.system(STR)

if __name__ == '__main__':
    print('Usage: python CodeScritpe.py TargetExePath InterMediateFilePath SourceFilePath OutPutFilePath(SourceCodeFilePath) OutPutFilePath2(IntermediateFilePath) OutPutFilePath3(TokenTableFilePath) OutPutFilePath4(TokenTableToValueFilePath) OutPutFilePath5(VecFilePath) OutPutFilePath6(DataDependence) OutPutFilePath7(ControlDependence) OutPutFilePath8(word2vec) OutPutFilePath9(OutputPicPath) OutPutFilePath10(OutputAllSourceFileIntermediatePath) OutPutFilePath11(OutputPicPath2) OutPutPicNumConfigFilePath OutPutPicNumConfigFilePath2 OutPutFilePath12(OutputUnCodeFragmentExtractStatisticsFilePath) OutputFilePath13(Vul) OutputFilePath14(No-Vul) OutputFilePath15(FuncNo) OutputFilePath16(DataDependenceTime) OutputFilePath17(ControlDependenceTime) Mod(Real Code File Or Not) OutputFilePath18(Real Code File Output Pic Path) StartSourceFileNo StopSourceFileNo SourceFileType(1 == C ; 2 == CPP)')
    if len(sys.argv) != 28:
        print('Command Fail')
        sys.exit(0)
    TargetExePath = sys.argv[1]
    InterMediateFilePath = sys.argv[2]
    SourceFilePath = sys.argv[3]
    OutPutFilePath = sys.argv[4]
    OutPutFilePath2 = sys.argv[5]
    OutPutFilePath3 = sys.argv[6]
    OutPutFilePath4 = sys.argv[7]
    OutPutFilePath5 = sys.argv[8]
    OutPutFilePath6 = sys.argv[9]
    OutPutFilePath7 = sys.argv[10]
    OutPutFilePath8 = sys.argv[11]
    OutPutFilePath9 = sys.argv[12]
    OutPutFilePath10 = sys.argv[13]
    OutPutFilePath11 = sys.argv[14]
    OutPutPicNumConfigFilePath = sys.argv[15]
    OutPutPicNumConfigFilePath2 = sys.argv[16]
    OutPutFilePath12 = sys.argv[17]
    OutPutFilePath13 = sys.argv[18]
    OutPutFilePath14 = sys.argv[19]
    OutPutFilePath15 = sys.argv[20]
    OutPutFilePath16 = sys.argv[21]
    OutPutFilePath17 = sys.argv[22]
    Mod = sys.argv[23]
    OutPutFilePath18 = sys.argv[24]
    StartSourceFileNo = sys.argv[25]
    StopSourceFileNo = sys.argv[26]
    SourceFileType = int(sys.argv[27])
    #Run()
    files = os.listdir(SourceFilePath)
    for file in files:
        file_path = os.path.join(SourceFilePath, file)
        if file_path != SourceFilePath:
            if os.path.isdir(file_path):
                TargetPath = OutPutFilePath18 + file
                #print(file)
                #print(TargetPath)
                if not os.path.exists(TargetPath):
                    #print("1")
                    os.makedirs(TargetPath)
                #print(TargetPath)
                TargetPath = TargetPath + "/"
                Run2(file_path, TargetPath)

    Run2(SourceFilePath, OutPutFilePath18)
    