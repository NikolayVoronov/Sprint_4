package tests;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import page_object.MainPage;

@RunWith(Parameterized.class)
public class DropdownList {
    private final By list;
    private final By textList;
    private static WebDriver driver;
    public DropdownList(By list, By textList) {
        this.list = list;
        this.textList = textList;
    }
    @Parameterized.Parameters
    public static Object[][] getTextData() {
        MainPage objMainpage = new MainPage(driver);
        return new Object[][] {
                {objMainpage.questionsFieldCost, objMainpage.answerFieldCost},
                {objMainpage.questionsFieldQuantity, objMainpage.answerFieldQuantity},
                {objMainpage.questionsFieldTime, objMainpage.answerFieldTime},
                {objMainpage.questionsFieldToday, objMainpage.answerFieldToday},
                {objMainpage.questionsFieldProlong, objMainpage.answerFieldProlong},
                {objMainpage.questionsFieldCharger, objMainpage.answerFieldCharger},
                {objMainpage.questionsFieldCancel, objMainpage.answerFieldCancel},
                {objMainpage.questionsFieldOutMoscow, objMainpage.answerFieldOutMoscow},
        };
    }

    @Before
    public void start() {
        driver = new ChromeDriver();
        driver.get("https://qa-scooter.praktikum-services.ru/");
    }

    @Test
    public void checkDropdownList() {
        MainPage objMainpage = new MainPage(driver);
        objMainpage.scrollElement(list);
        objMainpage.clickElement(list);
        objMainpage.findElement(textList);
    }


    @After
    public void teardown() {
        driver.quit();
    }
}
