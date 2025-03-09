package page_object;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class OrderPage {
    private WebDriver driver;
    //Поля имя, фамилия, адрес, станция метро, номер телефона
    public By firstNameField = By.xpath(".//input[contains(@placeholder,'* Имя')]");
    public By surnameField = By.xpath(".//input[contains(@placeholder,'* Фамилия')]");
    public By adressField = By.xpath(".//input[contains(@placeholder,'* Адрес')]");
    public By metroField = By.xpath(".//input[contains(@placeholder,'* Станция метро')]");
    public By phoneField = By.xpath(".//input[contains(@placeholder,'* Телефон')]");
    //Найденная станция метро
    public By metroDropDown = By.xpath(".//div[contains(@class,'select-search__select')]");
    //Кнопка далее
    public By nextButton = By.xpath(".//button[text()='Далее']");
    //Поле когда привезти самокат
    public By dateOrderField = By.xpath(".//input[contains(@placeholder,'* Когда привезти')]");
    //Выбранная дата
    public By dateOrderSelected = By.xpath(".//div[contains(@class,'datepicker__day--selected')]");
    //Выпадающий список со сроком аренды
    public By timeOrderField = By.xpath(".//div[text()='* Срок аренды']");
    //Кнопка со сроком аренды на один день
    public By timeOrderOneDay = By.xpath(".//div[text()='сутки']");
    //Кнопка заказать
    public By nextButtonPayPage = By.xpath(".//div[contains(@class,'1xGrp')]/button[text()='Заказать']");
    //Кнопка да
    public By yesButton = By.xpath(".//div[contains(@class,'1xGrp')]/button[text()='Да']");
    //Сообщение об успешном заказе
    public By successStatusField = By.xpath(".//div[text()='Заказ оформлен']");

    public OrderPage (WebDriver driver){
        this.driver = driver;
    }

    public void setFirstName(String text){
        driver.findElement(firstNameField).sendKeys(text);;
    }

    public void setSurnameField(String text){
        driver.findElement(surnameField).sendKeys(text);;
    }

    public void setAdressField(String text){
        driver.findElement(adressField).sendKeys(text);;
    }

    public void setMetroField(String text){
        driver.findElement(metroField).sendKeys(text);;
    }

    public void setPhoneField(String text){
        driver.findElement(phoneField).sendKeys(text);;
    }

    public void clickMetro(){
        driver.findElement(metroDropDown).click();;
    }

    public void clickNextButton(){
        driver.findElement(nextButton).click();;
    }

    public void stepOneOrder(String firstNameText, String surnameText, String adressText,
                            String metroText, String phoneText){
        setFirstName(firstNameText);
        setSurnameField(surnameText);
        setAdressField(adressText);
        setMetroField(metroText);
        clickMetro();
        setPhoneField(phoneText);
        clickNextButton();
    }

    public void setdateOrderField(String text){
        driver.findElement(dateOrderField).sendKeys(text);
    }

    public void clickDateOrder(){
        driver.findElement(dateOrderSelected).click();
    }

    public void clickTimeOrder(){
        driver.findElement(timeOrderField).click();
    }

    public void clickOneDay(){
        driver.findElement(timeOrderOneDay).click();
    }

    public void clickNextButtonPayPage(){
        driver.findElement(nextButtonPayPage).click();
    }

    public void stepTwoOrder(String dateOrderText){
        setdateOrderField(dateOrderText);
        clickDateOrder();
        clickTimeOrder();
        clickOneDay();
        clickNextButtonPayPage();
    }

    public void clickYesButton(){
        new WebDriverWait(driver, Duration.ofSeconds(5))
                .until(ExpectedConditions.visibilityOf(driver.findElement(yesButton)));
        driver.findElement(yesButton).sendKeys();
    }

    public void findSuccessField(){
        driver.findElement(successStatusField);
    }

}
