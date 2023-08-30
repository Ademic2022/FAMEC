document.addEventListener ('DOMContentLoaded', ()=>{
    function inputAutoFill(id, inputValue) {
        const element = document.getElementById(id);
        if (inputValue === 'country') {
            element.value = geoplugin_countryName();
        } else if (inputValue === 'state') {
            element.value = geoplugin_region();
        } else if (inputValue === 'city') {
            element.value = geoplugin_city();
        }
    }
    inputAutoFill('country', 'country');
    inputAutoFill('state', 'state');
})