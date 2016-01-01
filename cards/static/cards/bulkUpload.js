function bulkUpload(e) {
	console.log(e)
	form = document.createElement("form")
	form.setAttribute("method", "post")
	form.setAttribute("action", "/decks_template/")
	form.setAttribute("enctype", "multipart/form-data")
	input = document.createElement("input")
	input.setAttribute("type", "file")
	input.setAttribute("name","bulkupload")
	form.appendChild(input)
    input.click()
    form.onchange = function() {
    	form.submit()
    }

}