package main

import (
    "fmt"
    "log"
    "os"
    "strings"
    "github.com/go-telegram-bot-api/telegram-bot-api"
)

func main() {
    // Get the bot token from the environment variable.
    token := os.Getenv("6159945847:AAHLiJuL75pEZJ1XtlmA214cUcPpMS455Mo")
    if token == "" {
        log.Fatal("Please set the TELEGRAM_BOT_TOKEN environment variable.")
    }

    // Create a new BotAPI instance.
    api := tgbotapi.NewBotAPI(token)

    // Register a handler for the /start command.
    api.HandleFunc("/start", func(ctx *tgbotapi.Update) {
        // Send a message to the user.
        api.SendMessage(ctx.Message.Chat.ID, "Hello, world!")
    })

    // Register a handler for the /send_to_channel command.
    api.HandleFunc("/send_to_channel", func(ctx *tgbotapi.Update) {
        // Get the channel ID from the message.
        channelID := ctx.Message.CommandArguments[0]

        // Get the lines from the URL.
        lines, err := readLinesFromURL(ctx.Message.CommandArguments[1])
        if err != nil {
            log.Fatal(err)
        }

        // Send 10 lines randomly to the channel.
        for i := 0; i < 10; i++ {
            line := lines[rand.Intn(len(lines))]
            api.SendMessage(channelID, line)
        }
    })

    // Start the bot.
    err := api.Start()
    if err != nil {
        log.Fatal(err)
    }

    // Wait for messages.
    select {
    case <-api.UpdatesChan:
    }
}

func readLinesFromURL(url string) ([]string, error) {
    // Create a new request.
    req, err := http.NewRequest("GET", url, nil)
    if err != nil {
        return nil, err
    }

    // Do the request.
    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, err
    }

    // Check the response code.
    if resp.StatusCode != http.StatusOK {
        return nil, fmt.Errorf("Error getting lines from URL: %d", resp.StatusCode)
    }

    // Read the lines from the response body.
    lines := []string{}
    scanner := bufio.NewScanner(resp.Body)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }

    // Close the response body.
    resp.Body.Close()

    // Return the lines.
    return lines, nil
}
