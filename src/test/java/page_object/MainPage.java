package page_object;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

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
    public By answerFieldCost = By.xpath(".//div[@id='accordion__panel-0']/p");
    public By answerFieldQuantity = By.xpath(".//div[@id='accordion__panel-1']/p");
    public By answerFieldTime = By.xpath(".//div[@id='accordion__panel-2']/p");
    public By answerFieldToday = By.xpath(".//div[@id='accordion__panel-3']/p");
    public By answerFieldProlong = By.xpath(".//div[@id='accordion__panel-4']/p");
    public By answerFieldCharger = By.xpath(".//div[@id='accordion__panel-5']/p");
    public By answerFieldCancel = By.xpath(".//div[@id='accordion__panel-6']/p");
    public By answerFieldOutMoscow = By.xpath(".//div[@id='accordion__panel-7']/p");
    //Верхняя кнопка создать заказ
    public By orderButtonHeader = By.className("Button_Button__ra12g");
    //Нижняя кнопка создать заказ
    public By orderButtonBody = By.xpath(".//div[contains(@class,'Home_FinishButton__1_cWm')]/button");

    public MainPage (WebDriver driver){
        this.driver = driver;
    }

    public void start(){
        driver = new ChromeDriver();
        driver.get("https://qa-scooter.praktikum-services.ru/");
    }

    public void clickElement(By locator){
        new WebDriverWait(driver, Duration.ofSeconds(5))
                .until(ExpectedConditions.visibilityOf(driver.findElement(locator)));
        driver.findElement(locator).click();
    }

    public boolean isElementPresent(By locator){
        driver.findElement(locator);
        return true;
    }

    public String getText(By locator){
        return driver.findElement(locator).getText();
    }

    public void scrollElement(By locator){
        WebElement element = driver.findElement(locator);
        ((JavascriptExecutor)driver).executeScript("arguments[0].scrollIntoView();", element);
    }

}
