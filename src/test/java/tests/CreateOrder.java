package tests;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import page_object.MainPage;
import page_object.OrderPage;

@RunWith(Parameterized.class)
public class CreateOrder {
    private final String firstNameText;
    private final String surnameText;
    private final String adressText;
    private final String metroText;
    private final String phoneText;
    private final String dateOrderText;
    private static WebDriver driver;
    public CreateOrder(String firstNameText, String surnameText, String adressText,
                       String metroText, String phoneText, String dateOrderText) {
        this.firstNameText = firstNameText;
        this.surnameText = surnameText;
        this.adressText = adressText;
        this.metroText = metroText;
        this.phoneText = phoneText;
        this.dateOrderText = dateOrderText;
    }
    @Parameterized.Parameters
    public static Object[][] getTextData() {
        return new Object[][] {
                {"Жан жак", "Тестировалль", "Вымышленный адрес",
                        "Аэропорт", "+79999999999", "20.03.2025"},
                {"Агент", "Смит", "г. Зеон, ул. Машинная, д.5, корп.7",
                        "Автозаводская", "+77776665544", "01.05.2025"},
        };
    }

    @Before
    public void start() {
        driver = new ChromeDriver();
        driver.get("https://qa-scooter.praktikum-services.ru/");
    }

    @Test
    public void checkCreateOrder() {
        MainPage objMainpage = new MainPage(driver);
        objMainpage.clickOrderButtonHeader();
        OrderPage objOrderPage = new OrderPage(driver);
        objOrderPage.stepOneOrder(firstNameText, surnameText, adressText, metroText, phoneText);
        objOrderPage.stepTwoOrder(dateOrderText);
        objOrderPage.clickYesButton();
        objOrderPage.findSuccessField();
    }


    @After
    public void teardown() {
        driver.quit();
    }
}