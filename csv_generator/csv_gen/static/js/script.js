CURRENT_COLUMN_INDEX = 1;
CURRENT_ORDER=1;
function add(){
    console.log('ээээээээээээээээээээээээээээээээээээээ')
    var column = document.getElementById('column_template').children[0]
    var columnsContainer = document.getElementById('columns_container')

    //columnsContainer.innerHTML += column

    columnsContainer.appendChild(column.cloneNode(true))

    var quantity = CURRENT_COLUMN_INDEX


    var columnContainer = columnsContainer.lastElementChild;
    columnContainer.querySelector('input[name=column_name]').setAttribute("name", `column_name_${quantity}`)
    /*var setAttrColumnName = columnsContainer.lastElementChild.firstElementChild.children[1].setAttribute("name", `column_name_${quantity}`)*/
    var setAttrType = columnsContainer.lastElementChild.firstElementChild.nextElementSibling.children[0].setAttribute("name", `type_${quantity}`)

    var setAttrTypeOptionFrom = columnsContainer.lastElementChild.firstElementChild.nextElementSibling.nextElementSibling.children[0].setAttribute("name", `option_from_${quantity}`)
    var setAttrTypeOptionTo = columnsContainer.lastElementChild.firstElementChild.nextElementSibling.nextElementSibling.children[1].setAttribute("name", `option_to_${quantity}`)

    var setAttrOrder = columnsContainer.lastElementChild.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.children[1].setAttribute("name", `order_${quantity}`)
    var setOrder = columnsContainer.lastElementChild.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.children[1].value = CURRENT_ORDER
    console.log(setOrder)
    var setValueAttrHidden = columnContainer.querySelector('input[name="column_numbers[]"]').setAttribute("value", quantity)













    CURRENT_COLUMN_INDEX++;
    CURRENT_ORDER++;
}


function remove(item){
    var columnsContainer = document.getElementById('columns_container')
    /*var currentItem = document.querySelector('.schema_column_container')*/
    /*var columnsContainer = document.getElementById('schema_column_container')*/
    var currentItem = item.parentElement
    currentItem.remove()
    /*console.log(currentItem )
    console.log(columnsContainer)*/
    console.log(currentItem)
    console.log(columnsContainer)
}


function select(element){
    debugger;
    var value = element.value

    var targetElement = element.parentElement.nextElementSibling
    console.log(targetElement)

    if (value === 'integer') {
        console.log('показать')
        targetElement.classList.remove("hidden")
        //показать
    }
    else {
        console.log("скрыть")
        targetElement.classList.add("hidden")
        //скрыть
    }
}