import Browser
import Http
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (onInput, onClick)

-- MAIN


main =
  Browser.element { init = init, update = update, subscriptions = subscriptions, view = view }



-- MODEL


type alias Model =
  { name : String 
  , password : String
  , passwordAgain : String
  , output : String
  }


init : () -> (Model, Cmd Msg)
init _ =
  ({name = "",password = "",passwordAgain = "",output = ""}, Cmd.none)



-- UPDATE


type Msg
  = Name String
  | Password String
  | PasswordAgain String
  | GotText (Result Http.Error String)
  | ButtonFunction String String String

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    Name name ->
      ({ model | name = name }, Cmd.none)

    Password password ->
      ({ model | password = password }, Cmd.none)

    PasswordAgain passwordAgain ->
      ({ model | passwordAgain = passwordAgain }, Cmd.none)

    ButtonFunction name pass repass ->
      ({ model | name = name , password = pass, passwordAgain = repass}, testPost name pass repass)

    GotText result ->
            case result of
                Ok val ->
                  ( { model | output = val }, Cmd.none )

                Err error ->
                  ( handleError model error, Cmd.none )

handleError model error =
    case error of
        Http.BadUrl url ->
            { model | output = "bad url: " ++ url }
        Http.Timeout ->
            { model | output = "timeout" }
        Http.NetworkError ->
            { model | output = "network error" }
        Http.BadStatus i ->
            { model | output = "bad status " ++ String.fromInt i }
        Http.BadBody body ->
            { model | output = "bad body " ++ body }


-- VIEW


view : Model -> Html Msg
view model =
  div []
    [ viewInput "text" "Name" model.name Name
    , viewInput "password" "Password" model.password Password
    , viewInput "password" "Re-enter Password" model.passwordAgain PasswordAgain
    , viewValidation model
    , button [ onClick (ButtonFunction model.name model.password model.passwordAgain) ] [text "Log In"]
    , div [] [text model.output] 
    ]

testPost : String -> String -> String -> Cmd Msg
testPost user pass repass =
  Http.post
    { url = "https://mac1xa3.ca/e/sunwooj/lab7/"
    , body = Http.stringBody "application/x-www-form-urlencoded" ("username="++user++"&password="++pass++"&repassword="++repass)
    , expect = Http.expectString GotText
    }
 

viewInput : String -> String -> String -> (String -> msg) -> Html msg
viewInput t p v toMsg =
  input [ type_ t, placeholder p, value v, onInput toMsg ] []


viewValidation : Model -> Html msg
viewValidation model =
  if model.password == model.passwordAgain then
    div [ style "color" "green" ] [ text "OK" ]
  else
    div [ style "color" "red" ] [ text "Passwords do not match!" ]

subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none