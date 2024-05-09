function cmbShapeType_SelectedIndexChanged(sender, eventArgs) {
    var item = eventArgs.get_item().get_index();
    var NumTxtLength = $find("ctl00_ContentPlaceHolder1_NumTxtLength");
    var NumTxtWidth = $find("ctl00_ContentPlaceHolder1_NumTxtWidth");
    const divDrawingPad = document.getElementById('ContentPlaceHolder1_divDrawingPad');
    const divSetup = document.getElementById('ContentPlaceHolder1_divSetup');
    const divButton = document.getElementById('ContentPlaceHolder1_divButton');
    if (item == 2 || item == 4 || item == 5 || item == 6) {
        NumTxtWidth.set_value(NumTxtLength._text);
        NumTxtWidth.disable();
    }
    else if (item == 7) {
        divDrawingPad.style.display = "flex";
        divSetup.style.display = "none";
        divButton.style.display = "none";
    }
    else {
        NumTxtWidth.set_value(NumTxtLength._text);
        NumTxtWidth.enable();
    }
}
function cmbType_SelectedIndexChanged(sender, eventArgs) {
    var item = eventArgs.get_item().get_index();
    const cmbShapeType = $find("ctl00_ContentPlaceHolder1_cmbShapeType");
    const NumTxtQuantity = $find("ctl00_ContentPlaceHolder1_NumTxtQuantity");
    if (item == 2) {
        cmbShapeType.get_items().getItem(1).select();
        NumTxtQuantity.set_value(1);
        cmbShapeType.disable();
        NumTxtQuantity.disable();
    }
    else {
        cmbShapeType.clearSelection();
        cmbShapeType.enable();
        NumTxtQuantity.set_value(null);
        NumTxtQuantity.enable();
    }
}
function NumTxtLength_TextChanged(sender, eventArgs) {
    const cmbShapeType = $find("ctl00_ContentPlaceHolder1_cmbShapeType");
    var NumTxtWidth = $find("ctl00_ContentPlaceHolder1_NumTxtWidth");
    var NumTxtLength = $find("ctl00_ContentPlaceHolder1_NumTxtLength");
    if (cmbShapeType._selectedIndex == 2 || cmbShapeType._selectedIndex == 4 || cmbShapeType._selectedIndex == 5 || cmbShapeType._selectedIndex == 6) {
        NumTxtWidth.set_value(NumTxtLength._text);
    }
}
function btnDone_Click() {
    const divDrawingPad = document.getElementById('ContentPlaceHolder1_divDrawingPad');
    const divSetup = document.getElementById('ContentPlaceHolder1_divSetup');
    const divButton = document.getElementById('ContentPlaceHolder1_divButton');
    divDrawingPad.style.display = "none";
    divSetup.style.display = "contents";
    divButton.style.display = "contents";
}
function trapezoidToRectangle(cmbShapeType, width, height) {
    var NumTxtWidth = $find("ctl00_ContentPlaceHolder1_NumTxtWidth");
    var NumTxtLength = $find("ctl00_ContentPlaceHolder1_NumTxtLength");
    cmbShapeType.get_items().getItem(1).select();
    NumTxtWidth.set_value(width);
    NumTxtLength.set_value(height);
}
function circleToSquare(cmbShapeType, width) {
    var NumTxtWidth = $find("ctl00_ContentPlaceHolder1_NumTxtWidth");
    var NumTxtLength = $find("ctl00_ContentPlaceHolder1_NumTxtLength");
    cmbShapeType.get_items().getItem(2).select();
    NumTxtWidth.set_value(width);
    NumTxtLength.set_value(width);
}
function semiCircleToTrianlge(cmbShapeType, width) {
    var NumTxtWidth = $find("ctl00_ContentPlaceHolder1_NumTxtWidth");
    var NumTxtLength = $find("ctl00_ContentPlaceHolder1_NumTxtLength");
    cmbShapeType.get_items().getItem(5).select();
    NumTxtLength.set_value(width);
}
function cmbShapeType_grid_SelectedIndexChanged(sender, eventArgs) {
    var item = eventArgs.get_item().get_index();
    var NumTxtLength = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtLength_grid");
    var NumTxtWidth = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtWidth_grid");
    const divDrawingPad = document.getElementById('ContentPlaceHolder1_divDrawingPad');
    const divSetup = document.getElementById('ContentPlaceHolder1_divSetup');
    const divButton = document.getElementById('ContentPlaceHolder1_divButton');
    if (item == 2 || item == 4 || item == 5 || item == 6) {
        NumTxtWidth.set_value(NumTxtLength._text);
        NumTxtWidth.disable();
    }
    else if (item == 7) {
        divDrawingPad.style.display = "flex";
        divSetup.style.display = "none";
        divButton.style.display = "none";
    }
    else {
        NumTxtWidth.set_value(NumTxtLength._text);
        NumTxtWidth.enable();
    }
}
function cmbType_grid_SelectedIndexChanged(sender, eventArgs) {
    var item = eventArgs.get_item().get_index();
    const cmbShapeType = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_cmbShapeType_grid");
    const NumTxtQuantity = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtQuantity_grid");
    if (item == 2) {
        cmbShapeType.get_items().getItem(1).select();
        NumTxtQuantity.set_value(1);
        cmbShapeType.disable();
        NumTxtQuantity.disable();
    }
    else {
        cmbShapeType.clearSelection();
        cmbShapeType.enable();
        NumTxtQuantity.set_value(null);
        NumTxtQuantity.enable();
    }
}


function NumTxtLength_grid_TextChanged(sender, eventArgs) {
    const cmbShapeType = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_cmbShapeType_grid");
    var NumTxtWidth = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtWidth_grid");
    var NumTxtLength = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtLength_grid");
    var NumTxtActLength = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtActLength_grid");
    var NumTxtActWidth = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtActWidth_grid");
    if (cmbShapeType._selectedIndex == 1 || cmbShapeType._selectedIndex == 2) {
        if (cmbShapeType._selectedIndex == 1 || cmbShapeType._selectedIndex == 2) {
            NumTxtWidth.set_value(NumTxtLength._text);
        }
        NumTxtActLength.set_value(NumTxtLength._text);
        NumTxtActWidth.set_value(NumTxtWidth._text);
    }
    else if (cmbShapeType._selectedIndex == 3) {
        NumTxtActLength.set_value(NumTxtLength._text + NumTxtWidth._text - 1);
        NumTxtActWidth.set_value(NumTxtWidth._text);
    }
    else if (cmbShapeType._selectedIndex == 4) {
        NumTxtWidth.set_value(NumTxtLength._text);
        NumTxtActWidth.set_value(NumTxtWidth._text * 2 - 1);
        NumTxtActLength.set_value(NumTxtActWidth._text);
    }
    else if (cmbShapeType._selectedIndex == 5) {
        NumTxtWidth.set_value(NumTxtLength._text);
        NumTxtActWidth.set_value(NumTxtWidth._text);
        NumTxtActLength.set_value(NumTxtActWidth._text * 2 - 1);
    }
    else if (cmbShapeType._selectedIndex == 6) {
        NumTxtWidth.set_value(NumTxtLength._text);
        NumTxtActWidth.set_value(NumTxtWidth._text * 3 - 2);
        NumTxtActLength.set_value(NumTxtActWidth._text * 2 - 1);
    }    
}

function NumTxtWidth_grid_TextChanged(sender, eventArgs) {
    const cmbShapeType = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_cmbShapeType_grid");
    var NumTxtWidth = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtWidth_grid");
    var NumTxtLength = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtLength_grid");
    var NumTxtActLength = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtActLength_grid");
    var NumTxtActWidth = $find("ctl00_ContentPlaceHolder1_TgridObjects_ctl00_ctl04_NumTxtActWidth_grid");
    if (cmbShapeType._selectedIndex == 1 || cmbShapeType._selectedIndex == 2) {
        NumTxtActLength.set_value(NumTxtLength._text);
        NumTxtActWidth.set_value(NumTxtWidth._text);
    }
    else if (cmbShapeType._selectedIndex == 3) {
        NumTxtActLength.set_value(NumTxtLength._text + NumTxtWidth._text - 1);
        NumTxtActWidth.set_value(NumTxtWidth._text);
    }
    else if (cmbShapeType._selectedIndex == 4) {
        NumTxtActWidth.set_value(NumTxtWidth._text * 2 - 1);
        NumTxtActLength.set_value(NumTxtActWidth._text);
    }
    else if (cmbShapeType._selectedIndex == 5) {
        NumTxtActWidth.set_value(NumTxtWidth._text);
        NumTxtActLength.set_value(NumTxtActWidth._text * 2 - 1);
    }
    else if (cmbShapeType._selectedIndex == 6) {
        NumTxtActWidth.set_value(NumTxtWidth._text * 3 - 2);
        NumTxtActLength.set_value(NumTxtActWidth._text * 2 - 1);
    }
}
