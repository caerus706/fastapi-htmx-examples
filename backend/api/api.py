from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import  HTMLResponse
from fastapi.templating import Jinja2Templates

from starlette import status

from .routes.click_to_edit import router as click_edit_router
from .routes.bulk_update import router as bulk_update_router
from .routes.click_to_load import router as click_to_load_router
from .routes.delete_row import router as delete_row_router
from .routes.edit_row import router as edit_row_router
from .routes.lazy_loading import router as lazy_loading_router
from .routes.inline_validation import router as inline_validation_router
from .routes.infinite_scroll import router as infinite_scroll_router
from .routes.active_search import router as active_search_router
from .routes.progress_bar import router as progress_bar_router
from .routes.value_select import router as value_select_router
from .routes.animations import router as animations_router
from .routes.file_upload import router as file_upload_router
from .routes.preserving_file_inputs import router as preserving_file_inputs_router
from .routes.dialogs_browser import router as dialogs_browser_router
from .routes.dialogs_uikit import router as dialogs_uikit_router
from .routes.dialogs_bootstrap import router as dialogs_bootstrap_router
from .routes.dialogs_custom import router as dialogs_custom_router
from .routes.tabs_hateoas import router as tabs_hateoas_router
from .routes.tabs_hyperscript import router as tabs_hyperscript_router
from .routes.keyboard_shortcuts import router as keyboard_shortcuts_router
from .routes.sortable import router as sortable_router
from .routes.updating_other_content import router as updating_other_content_router
from .routes.confirm import router as confirm_router

api_router = APIRouter()

# templates = Jinja2Templates(directory="templates")

# @api_router.get('/', response_class=HTMLResponse)
# def index(request: Request): #hx-request
#     context = {'request': request}
#     return templates.TemplateResponse("index.html", context)


@api_router.get('/confirmed', tags=['Confirm'])
def do_confirm():
    return True

api_router.include_router(click_edit_router, prefix="/click_to_edit", tags=["Click to Edit"])
api_router.include_router(bulk_update_router, prefix="/bulk_update", tags=["Bulk Update"])
api_router.include_router(click_to_load_router, prefix="/click_to_load", tags=["Bulk Update"])
api_router.include_router(delete_row_router, prefix="/delete_row", tags=["Delete Row"])
api_router.include_router(edit_row_router, prefix="/edit_row", tags=["Edit Row"])
api_router.include_router(lazy_loading_router, prefix="/lazy_loading", tags=["Lazy Loading"])
api_router.include_router(inline_validation_router, prefix="/inline_validation", tags=["Inline Validation"])
api_router.include_router(infinite_scroll_router, prefix="/infinite_scroll", tags=["Infinite Scroll"])
api_router.include_router(active_search_router, prefix="/active_search", tags=["Active Search"])
api_router.include_router(progress_bar_router, prefix="/progress_bar", tags=["Progress Bar"])
api_router.include_router(value_select_router, prefix="/value_select", tags=["Value Select"])
api_router.include_router(animations_router, prefix="/animations", tags=["Animations"])
api_router.include_router(file_upload_router, prefix="/file_upload", tags=["File Upload"])
api_router.include_router(preserving_file_inputs_router, prefix="/preserving_file_inputs", tags=["Preserving File Inputs"])
api_router.include_router(dialogs_browser_router, prefix="/dialogs_browser", tags=["Dialogs Browser"])
api_router.include_router(dialogs_uikit_router, prefix="/dialogs_uikit", tags=["Dialogs UIKit"])
api_router.include_router(dialogs_bootstrap_router, prefix="/dialogs_bootstrap", tags=["Dialogs Bootstrap"])
api_router.include_router(dialogs_custom_router, prefix="/dialogs_custom", tags=["Dialogs Custom"])
api_router.include_router(tabs_hateoas_router, prefix="/tabs_hateoas", tags=["Tabs Hateoas"])
api_router.include_router(tabs_hyperscript_router, prefix="/tabs_hyperscript", tags=["Tabs Hyperscript"])
api_router.include_router(keyboard_shortcuts_router, prefix="/keyboard_shortcuts", tags=["Keyboard Shortcuts"])
api_router.include_router(sortable_router, prefix="/sortable", tags=["Sortable"])
api_router.include_router(updating_other_content_router, prefix="/updating_other_content", tags=["Updating Other Content"])
api_router.include_router(confirm_router, prefix="/confirm", tags=["Confirm"])
