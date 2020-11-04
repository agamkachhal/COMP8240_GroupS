{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "fasttextformat.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "GQ1R3uqOFX06"
      },
      "source": [
        "import pandas as pd"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8VkqBLiXF0D2"
      },
      "source": [
        "import csv"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MitGWdViF1uF",
        "outputId": "8207b794-e5a8-4dd8-9af2-cb95b7203cbe",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 419
        }
      },
      "source": [
        "photography = pd.read_csv(\"Photography.csv\", encoding=\"utf-8\")\n",
        "photography"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Questions</th>\n",
              "      <th>Labels</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>What caused these large white spots on my deve...</td>\n",
              "      <td>film artifacts spots development</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>How to coax 8-sec shutter on aperture prio fil...</td>\n",
              "      <td>film shutter-speed 35mm yashica</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>autofocus shown in viewfinder and captured on ...</td>\n",
              "      <td>autofocus portrait noise nikon-d7000 noise-red...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Godox AD200 is not triggering at some outdoor ...</td>\n",
              "      <td>godox</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Old-fashioned hot shoe flash does not fire on ...</td>\n",
              "      <td>flash hotshoe-flash</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6760</th>\n",
              "      <td>I'd like to create a Smart Collection to inclu...</td>\n",
              "      <td>smart-collections</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6761</th>\n",
              "      <td>External Flash triggered by camera's internal ...</td>\n",
              "      <td>flash camera-settings off-camera-flash camera-...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6762</th>\n",
              "      <td>Can I trigger the Yongnuo YN-600EX RT Il with ...</td>\n",
              "      <td>canon flash yongnuo studio-lighting wireless-f...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6763</th>\n",
              "      <td>Can I do “back conversion” of a B&amp;W JPEG to co...</td>\n",
              "      <td>color jpeg black-and-white file-format rgb</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6764</th>\n",
              "      <td>Damaged Nikon AF Nikkor 80-200 f2.8 ED</td>\n",
              "      <td>lens nikon repair</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>6765 rows × 2 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "                                              Questions                                             Labels\n",
              "0     What caused these large white spots on my deve...                   film artifacts spots development\n",
              "1     How to coax 8-sec shutter on aperture prio fil...                    film shutter-speed 35mm yashica\n",
              "2     autofocus shown in viewfinder and captured on ...  autofocus portrait noise nikon-d7000 noise-red...\n",
              "3     Godox AD200 is not triggering at some outdoor ...                                              godox\n",
              "4     Old-fashioned hot shoe flash does not fire on ...                                flash hotshoe-flash\n",
              "...                                                 ...                                                ...\n",
              "6760  I'd like to create a Smart Collection to inclu...                                  smart-collections\n",
              "6761  External Flash triggered by camera's internal ...  flash camera-settings off-camera-flash camera-...\n",
              "6762  Can I trigger the Yongnuo YN-600EX RT Il with ...  canon flash yongnuo studio-lighting wireless-f...\n",
              "6763  Can I do “back conversion” of a B&W JPEG to co...         color jpeg black-and-white file-format rgb\n",
              "6764             Damaged Nikon AF Nikkor 80-200 f2.8 ED                                  lens nikon repair\n",
              "\n",
              "[6765 rows x 2 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2cYoxOuKGA9h"
      },
      "source": [
        "# Converting to fasttext format\n",
        "photography['Labels']=['__label__'+s.replace(' ','__label__') for s in photography['Labels']]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yDMHAZk0GfEN",
        "outputId": "bd699bd3-7e12-45e0-c917-e5ef7e163920",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 119
        }
      },
      "source": [
        "photography['Labels'][:5]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    __label__film__label__artifacts__label__spots_...\n",
              "1    __label__film__label__shutter-speed__label__35...\n",
              "2    __label__autofocus__label__portrait__label__no...\n",
              "3                                       __label__godox\n",
              "4                 __label__flash__label__hotshoe-flash\n",
              "Name: Labels, dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CS-8-cN196K8",
        "outputId": "67cc7a2e-571b-41b0-cab1-0c2e5893cd67",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 359
        }
      },
      "source": [
        "photography[:10]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Questions</th>\n",
              "      <th>Labels</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>What caused these large white spots on my deve...</td>\n",
              "      <td>__label__film__label__artifacts__label__spots_...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>How to coax 8-sec shutter on aperture prio fil...</td>\n",
              "      <td>__label__film__label__shutter-speed__label__35...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>autofocus shown in viewfinder and captured on ...</td>\n",
              "      <td>__label__autofocus__label__portrait__label__no...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Godox AD200 is not triggering at some outdoor ...</td>\n",
              "      <td>__label__godox</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Old-fashioned hot shoe flash does not fire on ...</td>\n",
              "      <td>__label__flash__label__hotshoe-flash</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>What is this mount with notched tab on a Solig...</td>\n",
              "      <td>__label__lens-mount__label__old-lenses__label_...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Err 80 appears when I turn on my Canon EOS 5D ...</td>\n",
              "      <td>__label__troubleshooting__label__battery__labe...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>Battery is not communicating?</td>\n",
              "      <td>__label__canon__label__error__label__canon-70d</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>Canon FT QL Light Meter problem</td>\n",
              "      <td>__label__canon__label__repair__label__slr__lab...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>Continuous Video with No FPS [closed]</td>\n",
              "      <td>__label__video__label__camera__label__framerate</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                           Questions                                             Labels\n",
              "0  What caused these large white spots on my deve...  __label__film__label__artifacts__label__spots_...\n",
              "1  How to coax 8-sec shutter on aperture prio fil...  __label__film__label__shutter-speed__label__35...\n",
              "2  autofocus shown in viewfinder and captured on ...  __label__autofocus__label__portrait__label__no...\n",
              "3  Godox AD200 is not triggering at some outdoor ...                                     __label__godox\n",
              "4  Old-fashioned hot shoe flash does not fire on ...               __label__flash__label__hotshoe-flash\n",
              "5  What is this mount with notched tab on a Solig...  __label__lens-mount__label__old-lenses__label_...\n",
              "6  Err 80 appears when I turn on my Canon EOS 5D ...  __label__troubleshooting__label__battery__labe...\n",
              "7                      Battery is not communicating?     __label__canon__label__error__label__canon-70d\n",
              "8                    Canon FT QL Light Meter problem  __label__canon__label__repair__label__slr__lab...\n",
              "9              Continuous Video with No FPS [closed]    __label__video__label__camera__label__framerate"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "l0tKq0cXGh2D"
      },
      "source": [
        "# adding both the columns\n",
        "data_output = photography['Labels']+ ' ' + photography['Questions']"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "foEOXHx2G0c7",
        "outputId": "048a32c4-0f2f-457e-b3dd-ad061526ddec",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "data_output.head(10)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    __label__film__label__artifacts__label__spots_...\n",
              "1    __label__film__label__shutter-speed__label__35...\n",
              "2    __label__autofocus__label__portrait__label__no...\n",
              "3    __label__godox Godox AD200 is not triggering a...\n",
              "4    __label__flash__label__hotshoe-flash Old-fashi...\n",
              "5    __label__lens-mount__label__old-lenses__label_...\n",
              "6    __label__troubleshooting__label__battery__labe...\n",
              "7    __label__canon__label__error__label__canon-70d...\n",
              "8    __label__canon__label__repair__label__slr__lab...\n",
              "9    __label__video__label__camera__label__framerat...\n",
              "dtype: object"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hktFTE40G2jc"
      },
      "source": [
        "data_output.to_csv(r' photography.txt', index=False, sep=' ', header=False, quoting=csv.QUOTE_NONE, quotechar=\"\", escapechar=\" \")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ext4dPBtIU4d",
        "outputId": "c4417c71-eb58-4fc9-9773-0ed7dc208f04",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 289
        }
      },
      "source": [
        "photography[\"Labels\"].value_counts()\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "__label__flash__label__hotshoe-flash                                                                               451\n",
              "__label__autofocus__label__portrait__label__noise__label__nikon-d7000__label__noise-reduction                      451\n",
              "__label__flash__label__camera-settings__label__off-camera-flash__label__camera-basics__label__wireless-triggers    451\n",
              "__label__film__label__artifacts__label__spots__label__development                                                  451\n",
              "__label__canon__label__error__label__canon-70d                                                                     451\n",
              "__label__godox                                                                                                     451\n",
              "__label__video__label__camera__label__framerate                                                                    451\n",
              "__label__smart-collections                                                                                         451\n",
              "__label__troubleshooting__label__battery__label__canon-5d-mark-ii__label__error__label__power                      451\n",
              "__label__canon__label__repair__label__slr__label__light-meter                                                      451\n",
              "__label__lens-mount__label__old-lenses__label__soligor                                                             451\n",
              "__label__film__label__shutter-speed__label__35mm__label__yashica                                                   451\n",
              "__label__lens__label__nikon__label__repair                                                                         451\n",
              "__label__canon__label__flash__label__yongnuo__label__studio-lighting__label__wireless-flash                        451\n",
              "__label__color__label__jpeg__label__black-and-white__label__file-format__label__rgb                                451\n",
              "Name: Labels, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2dfTRe6VECf7"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}