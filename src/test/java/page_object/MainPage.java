package page_object;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class MainPage {
    private WebDriver driver;
    //Выпадающих списки в разделе Вопросы о важном
    public By questionsFieldCost = By.id("accordion__heading-0");
    public By questionsFieldQuantity = By.id("accordion__heading-1");
    public By questionsFieldTime = By.id("accordion__heading-2");
    public By questionsFieldToday = By.id("accordion__heading-3");
    public By questionsFieldProlong = By.id("accordion__heading-4");
    public By questionsFieldCharger = By.id("accordion__heading-5");
    public By questionsFieldCancel = By.id("accordion__heading-6");
    public By questionsFieldOutMoscow = By.id("accordion__heading-7");
    //Тексты ответов выпадающих списков в разделе Вопросы о важном
    public By answerFieldCost = By.xpath(".//p[contains(text(),'400 рублей')]");
    public By answerFieldQuantity = By.xpath(".//p[contains(text(),'покататься с друзьями')]");
    public By answerFieldTime = By.xpath(".//p[contains(text(),'Отсчёт времени аренды')]");
    public By answerFieldToday = By.xpath(".//p[contains(text(),'с завтрашнего дня')]");
    public By answerFieldProlong = By.xpath(".//p[contains(text(),'если что-то срочное')]");
    public By answerFieldCharger = By.xpath(".//p[contains(text(),'с полной зарядкой')]");
    public By answerFieldCancel = By.xpath(".//p[contains(text(),'пока самокат не привезли')]");
    public By answerFieldOutMoscow = By.xpath(".//p[contains(text(),'Московской области')]");
    //Верхняя кнопка создать заказ
    public By orderButtonHeader = By.className("Button_Button__ra12g");

    public MainPage (WebDriver driver){
        this.driver = driver;
    }

    public void clickElement(By locator){
        driver.findElement(locator).click();
    }

    public void findElement(By locator){
        driver.findElement(locator);
    }

    public void scrollElement(By locator){
        WebElement element = driver.findElement(locator);
        ((JavascriptExecutor)driver).executeScript("arguments[0].scrollIntoView();", element);
    }

    public void clickOrderButtonHeader(){
        driver.findElement(orderButtonHeader).click();
    }
}
