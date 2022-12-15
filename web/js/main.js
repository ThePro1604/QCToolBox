document.getElementById("Duplicator_script").addEventListener("click", ()=>{eel.Duplicator_script()}, false);
document.getElementById("ExcelCells2Files_script").addEventListener("click", ()=>{eel.ExcelCells2Files_script()}, false);
document.getElementById("FileList_script").addEventListener("click", ()=>{eel.FileList_script()}, false);
document.getElementById("IDnJsonResults2Excel_script").addEventListener("click", ()=>{eel.IDnJsonResults2Excel_script()}, false);
document.getElementById("Jsons2Excel_script").addEventListener("click", ()=>{eel.Jsons2Excel_script()}, false);
document.getElementById("NameScrambler_script").addEventListener("click", ()=>{eel.NameScrambler_script()}, false);
document.getElementById("NameSwitcher_script").addEventListener("click", ()=>{eel.NameSwitcher_script()}, false);
document.getElementById("PDF2JPG_script").addEventListener("click", ()=>{eel.PDF2JPG_script()}, false);
//document.getElementById("PickleDictSearch_script").addEventListener("click", ()=>{eel.PickleDictSearch_script()}, false);
<<<<<<< HEAD
document.getElementById("POAnJsonResults2Excel_script").addEventListener("click", ()=>{eel.POAnJsonResults2Excel_script()}, false);
document.getElementById("SendMail_script").addEventListener("click", ()=>{eel.SendMail_script()}, false);
=======
document.getElementById("JsonAge2Excel_script").addEventListener("click", ()=>{eel.JsonAge2Excel_script()}, false);
document.getElementById("JsonFaceLiveness2Excel_script").addEventListener("click", ()=>{eel.JsonFaceLiveness2Excel_script()}, false);
document.getElementById("POAnJsonResults2Excel_script").addEventListener("click", ()=>{eel.POAnJsonResults2Excel_script()}, false);
document.getElementById("SendMail_script").addEventListener("click", ()=>{eel.SendMail_script()}, false);
document.getElementById("ImageCollector_script").addEventListener("click", ()=>{eel.ImageCollector_script()}, false);
document.getElementById("FileScrambler_script").addEventListener("click", ()=>{eel.FileScrambler_script()}, false);
document.getElementById("FormatClientDemoExcel_script").addEventListener("click", ()=>{eel.FormatClientDemoExcel_script()}, false);
document.getElementById("FilesToSubDirectories_script").addEventListener("click", ()=>{eel.FilesToSubDirectories_script()}, false);
document.getElementById("DoubleDisplay_script").addEventListener("click", ()=>{eel.DoubleDisplay_script()}, false);
>>>>>>> 84b359e (Initial commit)

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}
