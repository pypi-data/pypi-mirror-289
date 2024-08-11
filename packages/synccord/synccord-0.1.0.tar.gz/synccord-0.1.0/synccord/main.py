from pywinauto import Application
def Sync_Cords(train_model):
    pass

def Application_tit(app_title):
    app = Application(backend="uia").connect(title_re=app_title, found_index=0)
