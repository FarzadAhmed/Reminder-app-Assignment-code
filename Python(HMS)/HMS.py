from tkinter import*
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox

class Hospital:

    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Care System")
        self.root.geometry("1600x900")
        self.root.configure(background='powder blue')


        cmbNameTablets=StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets=StringVar()
        Lot=StringVar()
        IssuedDate=StringVar()
        ExpDate=StringVar()
        DailyDose=StringVar()
        PossibleSideEffects=StringVar()
        FurtherInformation=StringVar()
        HowtoUseMedication=StringVar()
        DrivingUsingMachines=StringVar() 
        StorageAdvice=StringVar()
        PatientID=StringVar()
        PatientName=StringVar()
        DateofBirth=StringVar()
        PatientAddress=StringVar()
        Prescription=StringVar()
        NHSNumber=StringVar()
        #=================================Function Declaration================================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("Hospital Management System","Confirm if you want to Exit")
            if iExit >0:
                root.destroy()
                return

        def iPrescription():
            
            self.txtPrescription.insert(END,'Name of Tablets : \t\t\t' +cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(END,'Ref No : \t\t\t' +Ref.get() + "\n")
            self.txtPrescription.insert(END,'Dosage : \t\t\t' +Dose.get() + "\n")
            self.txtPrescription.insert(END,' NumberTablets: \t\t\t' +cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(END,' Lot No : \t\t\t' +Lot.get() + "\n")
            self.txtPrescription.insert(END,'IssuedDate : \t\t\t' +IssuedDate.get() + "\n")
            self.txtPrescription.insert(END,'  ExpDate : \t\t\t' + ExpDate.get() + "\n")
            self.txtPrescription.insert(END,' DailyDose \t\t\t' +DailyDose.get() + "\n")
            self.txtPrescription.insert(END,' PossibleSideEffects :\t\t\t' +PossibleSideEffects.get() + "\n")
            self.txtPrescription.insert(END,' FurtherInformation: \t\t\t' + FurtherInformation.get() + "\n")
            self.txtPrescription.insert(END,' HowtoUseMedication : \t\t\t' + HowtoUseMedication.get() + "\n")
            self.txtPrescription.insert(END,'DrivingUsingMachines: \t\t\t' + DrivingUsingMachines.get() + "\n")
            self.txtPrescription.insert(END,' StorageAdvice : \t\t\t' +StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END,' PatientID : \t\t\t' + PatientID.get() + "\n")
            self.txtPrescription.insert(END,' PatientName: \t\t\t' + PatientName.get() + "\n")
            self.txtPrescription.insert(END,' DateofBirth: \t\t\t' + DateofBirth.get() + "\n")
            self.txtPrescription.insert(END,' PatientAddress: \t\t\t' + PatientAddress.get() + "\n")
            self.txtPrescription.insert(END,' Prescription :\t\t\t' + Prescription.get() + "\n")
            self.txtPrescription.insert(END,' NHSNumber: \t\t\t' + NHSNumber.get() + "\n")
             
            return

        def iPrescriptionData():

        

            self.txtFrameDetail.insert(END,cmbNameTablets.get()+"\t\t"+ Ref.get()+"\t\t"+Dose.get()+"\t\t"
                                       +NumberTablets.get()+"\t\t"+ Lot.get()+"\t\t"+IssuedDate.get()+"\t\t"+ExpDate.get()+"\t\t"+DailyDose.get() +"\t\t"
                                       + StorageAdvice.get() +"\t\t"+NHSNumber.get() +"\t\t"+ PatientName.get() +"\t\t"+ DateofBirth.get() +"\t\t"
                                       +PatientAddress.get() + "\t\n")
        


            return

        def iDelete():

            cmbNameTablets.set('')
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            NumberTablets.set("")
            FurtherInformation.set("")
            HowtoUseMedication.set("")
            DrivingUsingMachines.set("") 
            StorageAdvice.set("")
            PatientID.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            NHSNumber.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)
           

            return

        def iReset():

            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            NumberTablets.set("")
            FurtherInformation.set("")
            HowtoUseMedication.set("")
            DrivingUsingMachines.set("") 
            StorageAdvice.set("")
            PatientID.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            NHSNumber.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return

        
        
        #=================================Frame================================================
         
        MainFrame =Frame(self.root)
        MainFrame.grid()


        TitleFrame = Frame(MainFrame, bd=20, width=1600, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,width=39 ,font=('arial', 40, 'bold'), text="\tHospital Care Systems\t",padx=2)
        self.lblTitle.grid()


        FrameDetail = Frame(MainFrame, bd=20, width=1600, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM )

        ButtonFrame = Frame(MainFrame, bd=20, width=1600, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM )

        DataFrame = Frame(MainFrame, bd=20, width=1600, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM )

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=950, height=300, padx=20, relief=RIDGE
                              ,font=('arial', 12, 'bold'), text=" Patient's Information:",)
        DataFrameLEFT.pack(side=LEFT )

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=500, height=300, padx=20, relief=RIDGE
                                   , font=('arial', 12, 'bold'), text=" Prescription",)
        DataFrameRIGHT.pack(side=RIGHT )
       #==========================================DtaFrameLEFT===========================================================
        self.lblNameTablet =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Name of Tablet:",padx=2,pady=2)
        self.lblNameTablet.grid(row =0, column=0)

        self.cboNameTablet=ttk.Combobox(DataFrameLEFT, textvariable= cmbNameTablets, state='readonly', font=('arial', 12, 'bold'), width=20)
        self.cboNameTablet['value']=('','paracetomol','Telsar 50mg','Gemer=1','Primacal AT','ME-12OD')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)


        self.lblFurtherInfo =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Further Information:",padx=2)
        self.lblFurtherInfo.grid(row =0, column=2)
        self.txtFurtherInfo=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = FurtherInformation)
        self.txtFurtherInfo.grid(row =0, column=3)

        self.lblRef =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Reference No:",padx=2,pady=2)
        self.lblRef.grid(row =1, column=0)
        self.txtRef=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =  Ref,width=25)
        self.txtRef.grid(row =1, column=1)

        self.lblStorage =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Storage Advice:",padx=2,pady=2)
        self.lblStorage.grid(row =1, column=2)
        self.txtStorage=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = StorageAdvice,width=25)
        self.txtStorage.grid(row =1, column=3)

        self.lblDose =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Dose :",padx=2,pady=4)
        self.lblDose.grid(row =2, column=0)
        self.txtDose=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = Dose,width=25)
        self.txtDose.grid(row =2, column=1)


        self.lblDUseMachine =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Driving Machine:",padx=2,pady=2)
        self.lblDUseMachine.grid(row =2, column=2)
        self.txtDUseMachine=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = DrivingUsingMachines ,width=25)
        self.txtDUseMachine.grid(row =2, column=3)

        self.lblNoOfTablets =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="No. of Tablets:",padx=2,pady=2)
        self.lblNoOfTablets.grid(row =3, column=0)
        self.txtNoOfTablets=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = NumberTablets ,width=25)
        self.txtNoOfTablets.grid(row =3, column=1)

        

        self.lblLot =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Lot:",padx=2,pady=2)
        self.lblLot .grid(row =4, column=0)
        self.txtLot =Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = Lot ,width=25)
        self.txtLot.grid(row =4, column=1)

        
        self.lblPatientID =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient ID:",padx=2,pady=2)
        self.lblPatientID .grid(row =4, column=2)
        self.txtPatientID =Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = PatientID ,width=25)
        self.txtPatientID.grid(row =4, column=3)

        self.lblIssuedDate =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Issued Date:",padx=2,pady=42)
        self.lblIssuedDate .grid(row =5, column=0)
        self.txtIssuedDate =Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = IssuedDate ,width=25)
        self.txtIssuedDate.grid(row =5, column=1)

        self.lblNHSNumber =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="NHS Number:",padx=2,pady=2)
        self.lblNHSNumber .grid(row =5, column=2)
        self.txtNHSNumber =Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = NHSNumber,width=25)
        self.txtNHSNumber.grid(row =5, column=3)

        self.lblNHSNumber =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="NHS Number:",padx=2,pady=2)
        self.lblNHSNumber .grid(row =5, column=2)
        self.txtNHSNumber =Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = NHSNumber,width=25)
        self.txtNHSNumber.grid(row =5, column=3)

        self.lblExpDate =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Exp Date:",padx=2,pady=2)
        self.lblExpDate .grid(row =6, column=0)
        self.txtExpDate =Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = ExpDate,width=25)
        self.txtExpDate.grid(row =6, column=1)

        self.lblPatientName =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Name:",padx=2,pady=2)
        self.lblPatientName.grid(row =6, column=2)
        self.txtPatientName =Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =PatientName,width=25)
        self.txtPatientName.grid(row =6, column=3)

        self.lblPatientName =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Name:",padx=2,pady=2)
        self.lblPatientName.grid(row =6, column=2)
        self.txtPatientName =Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =PatientName,width=25)
        self.txtPatientName.grid(row =6, column=3)

        self.lblDailyDose =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Daily Dose:",padx=2,pady=2)
        self.lblDailyDose.grid(row =7, column=0)
        self.txtDailyDose =Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =DailyDose,width=25)
        self.txtDailyDose.grid(row =7, column=1)

        self.lblDateofBirth =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Date of Birth:",padx=2,pady=2)
        self.lblDateofBirth.grid(row =7, column=2)
        self.txtDateofBirth=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = DateofBirth,width=25)
        self.txtDateofBirth.grid(row =7, column=3)

        self.lblSideEffects =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Side Effects:",padx=2,pady=2)
        self.lblSideEffects.grid(row =8, column=0)
        self.txtSideEffects=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = PossibleSideEffects,width=25)
        self.txtSideEffects.grid(row=8, column=1)

        self.lblPatientAddress =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Address:",padx=2,pady=2)
        self.lblPatientAddress.grid(row =8, column=2)
        self.txtPatientAddress=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =  PatientAddress,width=25)
        self.txtPatientAddress.grid(row=8, column=3)

        #==========================================DtaFrameRIGHT===========================================================

        self.txtPrescription=Text(DataFrameRIGHT, font=('arial', 12, 'bold'),width =43, height=14, padx=2,pady=4)
        self.txtPrescription.grid(row =0, column=0)

        #========================================== ButtonFrame===========================================================
        self.btnPrescription=Button(ButtonFrame, text='Prescription', font=('arial', 12, 'bold'),width =15,bd=4,
                                    command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)
        self.btnPrescriptionData=Button(ButtonFrame, text='Prescription Data', font=('arial', 12, 'bold'),width =24,bd=4,
                               command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0,column=1)
        self.btnDelete=Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'),width =15,bd=4,
                              command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        self.btnReset=Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'),width =15,bd=4,
                             command=iReset)
        self.btnReset.grid(row=0,column=3)
        self.btnExit=Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'),width =15,bd=4,
                            command=iExit)
        self.btnExit.grid(row=0,column=4)

        


        #========================================== FrameDetail===========================================================

        self.lblLabel=Label(FrameDetail,font=('arial', 10, 'bold'),pady=8,
        text="Name of Tablets\tReferece No.\t Doseage\t No. of Tablet\t Lot\t Issued Date\t Exp.Date\
\tDaily Dose\t Stoorage Adv.\t NHS Number\t Patients Name\t DOB\t Address")
        self.lblLabel.grid(row =0, column=0)

        self.txtFrameDetail=Text(FrameDetail, font=('arial', 12, 'bold'),width =141, height=5, padx=2,pady=4)
        self.txtFrameDetail.grid(row =1, column=0)

        

if __name__=='__main__':
    root = Tk()
    application = Hospital (root)
    root.mainloop()

    

 


    

    


        
        
        
        
