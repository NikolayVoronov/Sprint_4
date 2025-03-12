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
import data.Texts;

import static org.junit.Assert.*;

@RunWith(Parameterized.class)
public class DropdownList {
    private final By list;
    private final By textList;
    private final String textField;
    private static WebDriver driver;
    public DropdownList(By list, By textList, String textField) {
        this.list = list;
        this.textList = textList;
        this.textField = textField;
    }
    @Parameterized.Parameters
    public static Object[][] getTextData() {
        MainPage objMainpage = new MainPage(driver);
        Texts objTexts = new Texts();
        return new Object[][] {
                {objMainpage.questionsFieldCost, objMainpage.answerFieldCost, objTexts.textFieldCost},
                {objMainpage.questionsFieldQuantity, objMainpage.answerFieldQuantity, objTexts.textFieldQuantity},
                {objMainpage.questionsFieldTime, objMainpage.answerFieldTime, objTexts.textFieldTime},
                {objMainpage.questionsFieldToday, objMainpage.answerFieldToday, objTexts.textFieldToday},
                {objMainpage.questionsFieldProlong, objMainpage.answerFieldProlong, objTexts.textFieldProlong},
                {objMainpage.questionsFieldCharger, objMainpage.answerFieldCharger, objTexts.textFieldCharger},
                {objMainpage.questionsFieldCancel, objMainpage.answerFieldCancel, objTexts.textFieldCancel},
                {objMainpage.questionsFieldOutMoscow, objMainpage.answerFieldOutMoscow, objTexts.textFieldOutMoscow},
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
        boolean elementExists = objMainpage.isElementPresent(textList);
        String actualText = objMainpage.getText(textList);
        assertEquals(elementExists, true);
        assertEquals(actualText, textField);
    }


    @After
    public void teardown() {
        driver.quit();
    }
}
