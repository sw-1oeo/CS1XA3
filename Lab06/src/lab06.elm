import Browser
import Html exposing (Html, Attribute, div, input, text)
import Html.Attributes exposing (..)
import Html.Events exposing (onInput)



-- MAIN


main =
  Browser.sandbox { init = init, update = update, view = view }

-- MODEL


type alias Model =
  { content1 : String , content2 : String }


init : Model
init = { content1 = "", content2 = "" }



-- UPDATE


type Msg
  = Change1 String | Change2 String

update : Msg -> Model -> Model
update msg model = case msg of
                  Change1 newContent -> { model | content1 = newContent}
                  Change2 newContent -> { model | content2 = newContent}

-- VIEW


view : Model -> Html Msg
view model =
  div []
    [ input [ placeholder "String1", value model.content1, onInput Change1 ] []
    , input [ placeholder "String2", value model.content2, onInput Change2 ] []
    , div [] [ text (model.content1 ++ " : " ++ model.content2  )]
    ] 
