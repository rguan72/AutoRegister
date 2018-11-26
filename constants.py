from selenium import webdriver
from pytz import timezone
LOGIN_URL = "https://weblogin.umich.edu/cosign-bin/cosign.cgi"
driver = webdriver.Chrome("./chromedriver")
BACK_REG_ID = "DERIVED_SSS_SCR_SSS_LINK_ANCHOR3$span"
STUD_WOL = "https://csprod.dsc.umich.edu/services/student"
STUD_SS = "https://csprod.dsc.umich.edu/psc/csprodnonop_1/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?PortalActualURL=https%3a%2f%2fcsprod.dsc.umich.edu%2fpsc%2fcsprodnonop_1%2fEMPLOYEE%2fSA%2fc%2fSA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL&amp;PortalContentURL=https%3a%2f%2fcsprod.dsc.umich.edu%2fpsc%2fcsprodnonop_1%2fEMPLOYEE%2fSA%2fc%2fSA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL&amp;PortalContentProvider=SA&amp;PortalCRefLabel=Student%20Center&amp;PortalRegistryName=EMPLOYEE&amp;PortalServletURI=https%3a%2f%2fcsprod.dsc.umich.edu%2fpsp%2fcsprodnonop_1%2f&amp;PortalURI=https%3a%2f%2fcsprod.dsc.umich.edu%2fpsc%2fcsprodnonop_1%2f&amp;PortalHostNode=SA&amp;NoCrumbs=yes&amp;PortalKeyStruct=yes"
W19_ID = "SSR_DUMMY_RECV1$sels$0$$0" # ID might change with different yeared students
CONT_ID = "DERIVED_SSS_SCT_SSR_PB_GO"
P2_3 = "DERIVED_REGFRM1_LINK_ADD_ENRL$82$"
FIN_ID = "DERIVED_REGFRM1_SSR_PB_SUBMIT"
EST = timezone("US/Eastern")

# Testing purposes only
F19_ID = "SSR_DUMMY_RECV1$sels$1$$0"
