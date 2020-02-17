from requests import *
import socket
import pyodbc
import random
from datetime import timedelta, date
import os
import shutil
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart

EndDate = date.today() + timedelta(days=10)
EndDate = EndDate.strftime("%m%d%Y")

currentdir = os.getcwd()

if (not os.path.isdir('\\umakant\\script\\Logs')):
    os.makedirs('\\umakant\\script\\Logs')

logfilename = ("LogFile_" + date.today().strftime("%Y_%m_%d%H%M%S") + "." + "txt")
vs_Log_File_Name = os.path.join("\\umakant\\script\\Logs" + logfilename)
print(vs_Log_File_Name)
vobf_Log_File_Obj = open(vs_Log_File_Name, "w+")


def fn_LogMsg(msg):
    print(msg)
    msg = msg + "\r\n"
    vobf_Log_File_Obj.write(msg)


# END fn_LogMsg

def postrequest(furl, fdata, ftag, ftagvalue):
    # For Any api

    fn_LogMsg('\n############################################################################################################\n')
    fn_LogMsg('Request----\n' + str(fdata))
    fcode = 0
    fStatus = ""

    PSTMSR = furl
    data = fdata
    Head = {"Accept": "application/json", "Content-Type": "application/json"}

    response = post(url=PSTMSR, data=data, headers=Head)

    if response.status_code == 200:

        fcode = 200
        print(response.json())
        fn_LogMsg(str(furl) + '----\n' + 'Response---\n' + str(response.json()))
        if response.json()[ftag] == ftagvalue:
            fStatus = "Pass"
        else:
            fn_LogMsg('Failed***************************************----\n' + 'Response---\n' + str(
                response.json()[ftag]) + '<>' + str(ftagvalue))
            fStatus = "Fail"
    else:
        fStatus = "Fail"
        fcode = response.status_code
    return fcode, fStatus


for i in range(5):
    # For api P_accountCreation-----
    ssn = str(random.randint(111111111, 999999999))
    P_accountCreationcode = 0
    P_accountCreationstatus = ""

    P_accountCreation = 'https:Link/AccountCreationReq/'
    data = """Request body"""
    Head = {"Accept": "application/json", "Content-Type": "application/json"}

    response = post(url=P_accountCreation, data=data, headers=Head)
    fn_LogMsg('Request----\n' + str(data))
    if response.status_code == 200:

        P_accountCreationcode = 200
        if response.json()["Object"] != None:
            a = str(response.json()["Object"]["CAppReqest"]["ERROR"]["MESSAGE"])
            fn_LogMsg(str(P_accountCreation) + ' \nResponse-' + str(a))

            fn_LogMsg( ' \nResponse-' + str(response.json()))
            print(a[0:8])
            if (a[0:8] == 'INFO : |' or a == "Auto Approve") and str(response.json()["Object"]["CAppReqest"]["ERROR"]["CODE"])=='AA' and str(response.json()["Object"]["PreQualCall"] != None) :

                P_accountCreationstatus = "Pass"
                break
            else:
                fn_LogMsg('Failed***************************************----\n' + 'Response---\n Message <>' + str(a))
                P_accountCreationstatus = "Fail"
        else:
            P_accountCreationstatus = "Fail"
    else:
        P_accountCreationstatus = "Fail"
        P_accountCreationcode = response.status_code

print(P_accountCreationcode, P_accountCreationstatus, P_accountCreation)

fn_LogMsg(' \n#############################################################################################################\n' )
# For api H_account creation


for i in range(5):

    ssn = str(random.randint(111111111, 999999999))
    H_accountCreationcode = 0
    H_accountCreationstatus = ""

    H_accountCreation = 'https:Link/AccountCreationReq/'
    data = """Body request"""
    Head = {"Accept": "application/json", "Content-Type": "application/json"}

    response = post(url=H_accountCreation, data=data, headers=Head)
    fn_LogMsg('Request----\n' + str(data))
    if response.status_code == 200:
        H_accountCreationcode = 200
        if response.json()["Object"] != None:
            a = str(response.json()["Object"]["CAppReqest"]["ERROR"]["MESSAGE"])
            print(a)
            fn_LogMsg(str(H_accountCreation) + 'hard pull Response-' + str(a))
            fn_LogMsg(' \nResponse-' + str(response.json()))
            if (a[0:8] == 'INFO : |' or a == "SUCCESSFUL"):

                H_accountCreationstatus = "Pass"
                break
            else:
                fn_LogMsg('Failed***************************************----\n' + 'Response---\n Message <>' + str(a))
                H_accountCreationstatus = "Fail"
        else:
            H_accountCreationstatus = "Fail"
    else:
        H_accountCreationstatus = "Fail"
        H_accountCreationcode = response.status_code

print(H_accountCreationcode, H_accountCreationstatus, H_accountCreation)

# For CreateMSR


CreateMSRcode = 0
CreateMSRStatus = ""

msr = str(random.randint(11111111, 99999999))

data = 'request Body'

CreateMSRcode, CreateMSRStatus = postrequest(
    'link', data, 'ErrorMessage','Request processed successfully')

print(CreateMSRcode, CreateMSRStatus, 'https:link/MSR')
# For PST

data = 'data""}'
PSTcode, PSTstatus = postrequest(
    'https://link/PostTransaction/', data,
    'ErrorMessage', 'Transaction posted successfully')

print(PSTcode, PSTstatus,
      'https:LinkPostSingleTransaction/')

# for account update
data = 'request""}'
accountupdatecode, accountupdatestatus = postrequest(
    'https://link/AccountUpdate/', data, 'Note',
    'Account Updated Successfully.')

print(accountupdatecode, accountupdatestatus,
      'https:link/AccountUpdate/')

# for BankAccountManagement
accountno = str(random.randint(11111111, 99999999))
data = 'data'

BankAccountManagementcode, BankAccountManagementstatus = postrequest(
    'https:LinkBankAccountManagement/', data,
    'ErrorMessage', 'Bank Account Management Added')

print(BankAccountManagementcode, BankAccountManagementstatus,
      'https:LinkBankAccountManagement/')

# For SearchBankAccountManagement
data = 'data'
BankAccountsearchcode, BankAccountsearchstatus = postrequest(
    'https:LinkSearchBankAccountManagement/', data,
    'ErrorMessage', 'Bank account details retrieved successfully')
print(BankAccountsearchcode, BankAccountsearchstatus,
      'https:LinkSearchBankAccountManagement/')

# For SearchPaymentSchedule
data = '{data'
SearchPaymentSchedulecode, SearchPaymentSchedulestatus = postrequest(
    'https:LinkSearchPaymentSchedule/', data,
    'ErrorMessage', 'Payment Schedules returned successfully')
print(SearchPaymentSchedulecode, SearchPaymentSchedulestatus,
      'https:LinkSearchPaymentSchedule/')

# For PaymentSchedule
data = 'data'
PaymentSchedulecode, PaymentSchedulestatus = postrequest(
    'https:LinkPaymentSchedule/', data, 'ErrorMessage',
    'Payment Schedule Added')
print(PaymentSchedulecode, PaymentSchedulestatus,
      'https:LinkPaymentSchedule/')

# html creation
Htmlcode = '''

<!DOCTYPE html>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Base</title>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  </head>
  <body>
    <div class="container">
<div class="container">
    <table class="table table-bordered" id="CreditTable">
	<h3>Post API Smoke Details -</h3>
          <thead>
               <th  style='border: 1px solid #ABABAB;' align="right"  scope="col">APILink</th>
                <th style='border: 1px solid #ABABAB;'  scope="col" align="center">Satuscode</th>
                <th  style='border: 1px solid #ABABAB;'  scope="col" align="center">Pass/Fail Satus</th>
            </thead>
              <tr class="table-info">
                <td style='border: 1px solid #ABABAB;' ><h4>Account creation Prequal</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(P_accountCreationcode) + '''</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(P_accountCreationstatus) + '''</h4></td>
                    </tr>
              <tr class="table-info">
                <td style='border: 1px solid #ABABAB;' ><h4>Account creation Hardpull</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(H_accountCreationcode) + '''</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(H_accountCreationstatus) + '''</h4></td>
                    </tr>
              <tr class="table-info">
                <td style='border: 1px solid #ABABAB;' ><h4>CreateMSR</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(CreateMSRcode) + '''</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(CreateMSRStatus) + '''</h4></td>
                    </tr>
  <tr class="table-info">
                <td style='border: 1px solid #ABABAB;' ><h4>PST</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(PSTcode) + '''</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(PSTstatus) + '''</h4></td>
                    </tr>
  <tr class="table-info">
                <td style='border: 1px solid #ABABAB;' ><h4>Account Update</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(accountupdatecode) + '''</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(accountupdatestatus) + '''</h4></td>
                    </tr>
  <tr class="table-info">
                <td style='border: 1px solid #ABABAB;' ><h4>BankAccountManagement</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(BankAccountManagementcode) + '''</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(BankAccountManagementstatus) + '''</h4></td>
                    </tr>
  <tr class="table-info">
                <td style=' border: 1px solid #ABABAB;' ><h4>SearchBankAccountManagement</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(BankAccountsearchcode) + '''</h4></td>
                <td style='border: 1px solid #ABABAB;' ><h4>''' + str(BankAccountsearchstatus) + '''</h4></td>
                    </tr>
  <tr class="table-info">
                <td style='border: 1px solid #ABABAB;' ><h4>SearchPaymentSchedule</h4></td>
                <td style='border: 1px solid #ABABAB;'  ><h4>''' + str(SearchPaymentSchedulecode) + '''</h4></td>
                <td style='border: 1px solid #ABABAB;'  ><h4>''' + str(SearchPaymentSchedulestatus) + '''</h4></td>
                    </tr>    
   <tr class="table-info">
                <td style='border: 1px solid #ABABAB;'  ><h4>PaymentSchedule</h4></td>
                <td style='border: 1px solid #ABABAB;'  ><h4>''' + str(PaymentSchedulecode) + '''</h4></td>
                <td style='border: 1px solid #ABABAB;'  ><h4>''' + str(PaymentSchedulestatus) + '''</h4></td>
                    </tr>             



        </table>
        </div>
        </div>
<div class="container">
    <div class="jumbotron">

</div></div>
    </div>
  </body>
</html>'''

Tolist = ['ssharma@gmail.com','aasati@gmail.com','umakant.yadav@gmail.com','nisaxena@gmail.com','rgupta@gmail.com','gmodak@gmail.com']


msg = MIMEMultipart()
msg['Subject'] = "Test Env Post API SMOKE"
msg['From'] = 'umakant.yadav@gmail.com'
msg['To'] = ', '.join(Tolist)

f = open(vs_Log_File_Name)
attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment', filename=logfilename)
msg.attach(attachment)

part2 = MIMEText(Htmlcode, 'html')

msg.attach(part2)
try:
    s = smtplib.SMTP("gmail-com.mail.protection.outlook.com")
    s.sendmail('umakant.yadav@gmail.com', Tolist, msg.as_string())
    s.quit()
    print("Mail Sent SuccessFully")
except:
    print("Error Occured")