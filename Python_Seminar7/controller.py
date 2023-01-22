import view
import process
import log


def button_click():
    rezhim = view.inp_mod()
    if rezhim.lower() == 'импорт':
        search = view.inp_import()
        result_search = process.search(search)
        if isinstance(result_search, str):
            view.view_import_no()
        else:
            view.view_import(result_search)
            log.log_import(result_search)
    elif rezhim.lower() == 'экспорт':
        result = view.inp_export()
        process.export(result)
        log.log_export(result)
