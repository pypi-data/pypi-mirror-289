""" Vision System interface - main
 
 
@author:    kais, misil.
@created:   2024-08-08
@version:   v0.0.2

vision_ip : camera IP
vision_port : camera Port

Functions:
JobChange() -- vision job change
CalibStart() -- 
CalibX() -- 
CalibEnd() -- 
ModelPos() -- 
ModelReg() -- 
Trigger() -- Trigger
                       
"""

import socket
import requests
import xhost
from typing import Optional

valueList: list = ['x', 'y', 'z', 'rx', 'ry', 'rz']
delimiter: str = ','



# global variables
raddr : tuple
sock : Optional[socket.socket] = None

vision_ip : str
vision_port : int
robot_ip : str
robot_port : int

class cmd:
    # VISOR Control
    TRR = "TRR"     # Trigger Robotics
    CJB = "CJB"     # Job Change
    
    # VISOR Job settings
    SPP = "SPP"     # Set Parameter
    
    # VISOR calibration
    CCD = "CCD"     # Initialization
    CAI = "CAI"     # Add image
    CRP = "CRP"     # Robotics multi-image
    
    PASS = "P"
    FAIL = "F"
    
    TRR_default: str = "TRR104Part"
    CAI_init_default: str = "CAI12000102"
    CAI_default: str = "CAI12000002"
    CRP_default: str = "CRP1140"
    SPP_default: str = "SPP001030000013"
    SPP_default_res: str = "SPP001035000480"

    
    
    @staticmethod
    def GetSPPT(key):
        # signed(정수), unsigned(음수)
        if key == "SI08":
            return "SignedInteger08"
        elif key == "UI08":
             return "UnsignedInteger08"
        elif key == "SI16":
            return "SignedInteger16"
        elif key == "UI16":
             return "UnsignedInteger16"
        elif key == "SI32":
            return "SignedInteger32"
        elif key == "UI32":
            return "UnsignedInteger32"
        elif key == "SI40":
            return "SignedInteger40"
        elif key == "UI40":
            return "UnsignedInteger40"
        elif key == "FLOT":
            return "Float"
        elif key == "DOBL":
            return "Double"
        elif key == "STRG":
            return "String"
        elif key == "BOOL":
            return "Boolean"
        elif key == "SP08":
            return "SpecialSigned8"
        elif key == "UDEF":
            return "Undefined"
        elif key == "IARR":
            return "IntegerArray"
        elif key == "ZERO":
            return "DefaultZeroParameter"

    
class log:
    VISION = "[vision]"
    ROBOT = "[robot]"
    ERROR = "[error]"
    SEND = "[send]"
    RECV = "[recv]"
    COLON = " : "
    
    FAIL_RETURN:str = "Fail"
    READY_RETURN: str = "CalibReady"
    NEXT_RETURN: str = "Next"
    COMPLETE_RETURN: str = "Complete"
    JOBCHANGE_RETURN: str = "JobChange Successful" 


def GetBase(type):
    if type == 0:
        return "\"robot\""  # "robot"
    elif type == 1:
        return "\"u1\""
    else:
        return "\"base\""

def GetQuery(type):
    if type == 0:
        return {'crd': 1,'mechinfo': 1}
    elif type == 1:
        return {'ucrd_no': 1,'mechinfo': 1}
    else:
        return {'crd': 0,'mechinfo': 1}

def GetPath():
    return '/project/robot/po_cur'

    
class socketFunc:
    def __init__(self):
        self.ip = vision_ip
        self.port = vision_port

    def open(self):
        global raddr, sock
        
        if sock is not None: 
            return False
        
        try:
            raddr = (self.ip, self.port)
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            sock.connect(raddr)
            return True

        except socket.error as e:
            logd("[vision][error] open failed")
            return False



    def is_close(self):
        if sock is not None:
            self.close()


    def close(self):
        global sock
        try:
            if sock is None: 
                return
            
            sock.close()
            sock = None
            return True
        
        except:
            logd("[vision][error] open failed")
            return False
        
    
    def send_msg(self, msg):
        if sock is None: 
            return -1
        
        try:
            logd(log.VISION + log.SEND + log.COLON + msg)
            bts = bytes(msg.encode())
            return sock.send(bts) 
        except Exception as e:
            logd(log.VISION + log.ERROR + log.COLON + str(e))
            return ""

    
    def recv_msg(self):
        if sock is None: 
            return ""
        try:
            recv_data = sock.recv(1024).decode()
            logd(log.VISION + log.RECV + log.COLON + recv_data)
            return recv_data
        
        except Exception as e:
            logd(log.VISION + log.ERROR + log.COLON + str(e))
            return ""


def Return(result):
    if result == cmd.PASS:
        return True
    elif result ==cmd.FAIL:
        return False 


def Set_CCD():
    msg = cmd.CCD
    return msg

def Get_CCD(recv_data):
    # CCDP
    recv = list(recv_data)
    recv, _ = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)
    return Return(result)

def Set_CJB(value):
    if value:
        msg = cmd.CJB + ZeroFill(value, 3)
        return msg
    else:
        return None


def Get_CJB(recv_data):
    recv = list(recv_data)
    recv, _ = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)
    
    if result == cmd.PASS:
        recv, trigger = Get_Data(recv, 0, 1)    # T:Triggered, F:Freerun
        recv, jobCrtNum = Get_Data(recv, 0, 3)
        # Job.jobCrtNum = jobCrtNum
        return  True
    elif result == cmd.FAIL:
        return False    


def Set_CAI(value, type):
    if type == 0:
        _cmd = cmd.CAI_init_default
    else: # type == 1
        _cmd = cmd.CAI_default
    result = Get_Value(value)
    return _cmd+result if result != None else None
    

def Get_CAI(recv_data):
    recv = list(recv_data)
    recv, _ = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)
    return Return(result)

def Set_CRP():
    #  CRP1140
    return cmd.CRP_default


def Get_CRP(recv_data):
    recv = list(recv_data)
    recv, _ = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)
    return Return(result)
    
    
def Set_TRR(value):
    _cmd = cmd.TRR_default
    result = Get_Value(value)
    return _cmd+result if result != None else None


def Get_TRR(recv_data):
    recv = list(recv_data)
    recv, _ = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)
    return Return(result)
    

def Shift(recv_data, type):
    recv = list(recv_data)
    recv, _ = Get_Data(recv, 0, 3)
    recv, result = Get_Data(recv, 0, 1)

    if result == cmd.PASS:
        recv, _ = Get_Data(recv, 0, 20)
        recv, positionData = Get_Data(recv, 0, len(recv)-1)
        
        result_str = "["
        values = ''.join(positionData).split(delimiter)
        for value in values:
                result_str += str(round(float(value)/1000, 3)) + ","
        result_str += GetBase(type)
        result_str += "]"             
        return result_str

    elif result == cmd.FAIL:
        return False
    

def Set_SPP():
    msg = cmd.SPP_default
    return msg


def Set_PoseSPP( value):
    _cmd = cmd.SPP_default_res
    result = Get_Value(value)
    return _cmd+result if result != None else None
    

def Get_SPP(recv_data):
    recv = list(recv_data)
    recv, _ = Get_Data(recv, 0, 2)
    recv, pt = Get_Data(recv, 0, 1) # permanent # Temporary
    recv, result = Get_Data(recv, 0, 1)

    if result == cmd.PASS:   
        recv, msg = Get_Data(recv, 0, 1)
        if msg == "U":
            return True
        elif msg == "S":
            return True
        else:
            return False

    elif result == cmd.FAIL:
        return False     

    
def Get_Value(value):
    if(value):
        try:
            if value.get('_type') == "Pose":
                vSendMsg :str = ""
                for values in valueList:
                    temp: float = value.get(values)
                    valInt = float(temp) * 1000
                    # valInt = int(temp * 1000)* 10 
                    vSendMsg += ('%08d' % valInt) 
                
                return vSendMsg
        except:
            return None    
    else:
        return None


def Get_Data(list, start, end):
    # temp = end
    # for i, str in enumerate(list):
    #     temp -= len(str.encode())
    #     if temp == 0:
    #         end = i + 1
    #         break
        
    data = ''.join(list[start: end])
    cut = list[end:]
    return cut, data
    
    
def VisionRecv(recv):
    status = False
    _cmd = ''.join(list(recv)[0:3])
    if recv is not None:
        
        if cmd.CCD == _cmd:
            status = Get_CCD(recv)
            if status:
                logd(log.VISION + " Calibration Initialization Successful")
            else:
                logd(log.VISION + " Calibration Initialization Failed")
        
        elif cmd.CJB == _cmd:
            status = Get_CJB(recv_data=recv)
            if status:
                logd(log.VISION + " Job Change Successful")
            else:
                logd(log.VISION + " Job Change Failed")
        
        elif cmd.CAI == _cmd:
            status = Get_CAI(recv_data=recv)
            if status:
                logd(log.VISION+ " Calibration CAI Successful")
            else:
                logd(log.VISION+ " Calibration CAI Failed")
                
        elif cmd.CRP == _cmd:
            status = Get_CRP(recv_data=recv)
            if status:
                logd(log.VISION+ " Calibration CPR Successful")
            else:
                logd(log.VISION+ " Calibration CPR Failed")  
                
        elif cmd.TRR == _cmd:
            status = Get_TRR(recv_data=recv)
            if status:
                logd(log.VISION+ " Trigger Robotics complete")
            else:
                logd(log.VISION+ " Trigger Robotics error")    
                
        elif cmd.SPP == _cmd:
            status = Get_SPP(recv_data=recv)
            if status:
                logd(log.VISION+ " Set Parameters Successful")
            else:
                logd(log.VISION+ " Set Parameters Failed")

    return status


def JobChange(num: int):
    if socketfunc_open(JobChange_func, num):
        return log.JOBCHANGE_RETURN
    else:
        logd(log.VISION + log.ERROR + " JobChange failed")
        return log.FAIL_RETURN

def JobChange_func(socketfunc, num):
    # visionSend : 'CCD' 전송
    visionMsg = Set_CJB(num)
    if not socketfunc.send_msg(visionMsg):
        logd(log.VISION + log.ERROR + " JobChange/send_msg failed")
        return False
    
    recv = socketfunc.recv_msg()
    if recv:
        if not VisionRecv(recv):
            logd(log.VISION + log.ERROR + " JobChange/recv_msg/VisionRecv failed")
            return False
    else:
        logd(log.VISION + log.ERROR + " JobChange/vision recv_msg failed")
        return False
    
    return True  
    

def CalibX_com(socketfunc, type):
    apiResult: dict = res_api(path=GetPath(), query=GetQuery(1))
    visionMsg = Set_CAI(apiResult, type)
    
    if visionMsg:
        if not socketfunc.send_msg(msg=visionMsg):
            return False
    else:
        logd(log.VISION + log.ERROR + " CalibX_func/send_msg failed")
        return False

    recv = socketfunc.recv_msg()
    if recv:
        if VisionRecv(recv):
            return True
        else:
            logd(log.VISION + log.ERROR + " CalibX_func/recv_msg/VisionRecv failed")
            return False     
    else:
        logd(log.VISION + log.ERROR + " CalibX_func/recv_msg failed")
        return False  


def socketfunc_open(func, mode=None):
    socketfunc = socketFunc()
    try:
        if not socketfunc.open():
            return False
        
        status = func(socketfunc, mode)
        socketfunc.is_close()
        if status:
            return True
        else:
            return False
    except:
        socketfunc.is_close()
        return False

        
        
    
def CalibStart():
    if socketfunc_open(CalibStart_func):
        return log.READY_RETURN
    else:
        logd(log.VISION + log.ERROR + " CalibStart failed")
        return log.FAIL_RETURN


def CalibStart_func(socketfunc, mode):
    # visionSend : 'CCD' 전송
    if not socketfunc.send_msg(cmd.CCD):
        logd(log.VISION + log.ERROR + " CalibStart/send_msg failed")
        return False
    
    # visionRecv : CCDP or CCDF 
    recv = socketfunc.recv_msg()
    if recv:
        if not VisionRecv(recv):
            logd(log.VISION + log.ERROR + " CalibStart/recv_msg/VisionRecv failed")
            return False
    else:
        logd(log.VISION + log.ERROR + " CalibStart/vision recv_msg failed")
        return False
    
    if CalibX_com(socketfunc, 0):
        return True 
    else:
        logd(log.VISION + log.ERROR + " CalibX_Com failed")
        return False
    

def CalibX():
    if socketfunc_open(CalibX_func):
        return log.NEXT_RETURN
    else:
        logd(log.VISION + log.ERROR + " CalibX failed")
        return log.FAIL_RETURN



def CalibX_func(socketfunc, _):
    if CalibX_com(socketfunc, 1):
        return True 
    else:
        logd(log.VISION + log.ERROR + " CalibX_func failed")
        return False


def CalibEnd():
        if socketfunc_open(CalibEnd_func):
            return log.COMPLETE_RETURN
        else:
            logd(log.VISION + log.ERROR + " CalibEnd failed")
            return log.FAIL_RETURN


def CalibEnd_func(socketfunc, _):
    if CalibX_com(socketfunc, 1):
        visionMsg = Set_CRP()
        if visionMsg:
            if not socketfunc.send_msg(visionMsg):
                return False
        else:
            logd(log.VISION + log.ERROR + " CalibEnd/send_msg failed")
            return False

        recv = socketfunc.recv_msg()
        if recv:
            if not VisionRecv(recv):
                logd(log.VISION + log.ERROR + " recv_msg/VisionRecv failed")
                return False    
        else:
            logd(log.VISION + log.ERROR + " recv_msg failed")
            return False
        return True  
    else:
        logd(log.VISION + log.ERROR + " CalibX failed")
        return False
    

def ModelPos():
    if socketfunc_open(ModelPos_func):
        return log.COMPLETE_RETURN
    else:
        logd(log.VISION + log.ERROR + " ModelPos failed")
        return log.FAIL_RETURN


def ModelPos_func(socketfunc, mode):
    apiResult: dict = res_api(path=GetPath(), query=GetQuery(1))
    visionMsg = Set_TRR(apiResult)
    
    if visionMsg:
        if not socketfunc.send_msg(visionMsg):
            return False
    else:
        logd(log.VISION + log.ERROR + " ModelPos_func/send_msg failed")
        return False

    recv = socketfunc.recv_msg()
    if recv:
        if VisionRecv(recv):
            return True
        else:
            logd(log.VISION + log.ERROR + " ModelPos_func/recv_msg/VisionRecv failed")   
            return False
    else:
        logd(log.VISION + log.ERROR + " ModelPos_func/recv_msg failed")
        return False



def ModelReg():
    if socketfunc_open(ModelReg_func):
        return log.COMPLETE_RETURN
    else:
        logd(log.VISION + log.ERROR + " ModelReg failed")
        return log.FAIL_RETURN


def ModelReg_func(socketfunc, mode):
    visionMsg = Set_SPP()
    if visionMsg:
        if not socketfunc.send_msg(visionMsg):
            return False
    else:
        logd(log.VISION + log.ERROR + " ModelReg_func/send_msg failed")
        return False
    
    recv = socketfunc.recv_msg()
    if recv:
        if not VisionRecv(recv):
            logd(log.VISION + log.ERROR + " ModelReg_func/recv_msg/VisionRecv failed")  
            return False  
    else:
        logd(log.VISION + log.ERROR + " ModelReg_func/recv_msg failed")
        return False
    
    apiResult: dict = res_api(path=GetPath(), query=GetQuery(1))
    visionMsg = Set_PoseSPP(apiResult)
    if visionMsg:
        if not socketfunc.send_msg(visionMsg):
            return False
    else:
        logd(log.VISION + log.ERROR + " ModelReg_func/send_msg failed")
        return False
    
    recv = socketfunc.recv_msg()
    if recv:
        if VisionRecv(recv):
            return True
        else:
            logd(log.VISION + log.ERROR + " ModelReg_func/recv_msg/VisionRecv failed")     
            return False
    else:
        logd(log.VISION + log.ERROR + " ModelReg_func/recv_msg failed")
        return False
    



def Trigger(mode : int):
    result = socketfunc_open(Trigger_func, mode)
    if result:
        return result
    else:
        logd(log.VISION + log.ERROR + " Trigger failed")
        return log.FAIL_RETURN


def Trigger_func(socketfunc, mode):
    result = []
    apiResult: dict = res_api(path=GetPath(), query=GetQuery(mode))
    visionMsg = Set_TRR(apiResult)
    if visionMsg:
        if not socketfunc.send_msg(visionMsg):
            return False
    else:
        logd(log.VISION + log.ERROR + " Trigger_func/send_msg failed")
        return False
    
    recv = socketfunc.recv_msg()
    if recv:
        if VisionRecv(recv):
            return Shift(recv, mode)
        else:
            logd(log.VISION + log.ERROR + " Trigger_func/recv_msg/VisionRecv failed")  
            return False   
    else:
        logd(log.VISION + log.ERROR + " Trigger_func/recv_msg failed")
        return False
    


def res_api(path: str, query: dict):
    base_url        = 'http://' + robot_ip + ':' + str(robot_port)
    path_parameter  = path
    query_parameter = query
    response = requests.get(url = base_url + path_parameter, params = query_parameter).json()
    return response


def logd(text: str):
    print(text)
    xhost.printh(text)

def ZeroFill(value, size):
    msg = str(value).zfill(int(size))
    return msg

robot_ip = "192.168.1.150"
robot_port = 8888


vision_ip = "192.168.1.104"
vision_port = 2006


# print(JobChange(1))
# print(CalibStart())
# print(CalibX())
# print(CalibEnd())
# print(ModelPos())

# print(ModelReg())
# print(Trigger(0))