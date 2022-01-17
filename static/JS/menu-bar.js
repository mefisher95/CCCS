function mobile_menu_button()
{
    console.log('button clicked');
    var x = document.getElementById("site-links");
    if (x.style.display === "block")
    {
        x.style.display = "none";
    }
    else
    {
        x.style.display = "block";
    }
}