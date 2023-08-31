import base64
import streamlit as st
from streamlit_option_menu import option_menu
import time


def main():
    # 设置页面配置
    st.set_page_config(page_title="橙汁的网站", page_icon="⭐", layout="wide")



    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

    # 通过 css样式隐藏主菜单和页脚
    hide_menu = '''
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    '''
    st.markdown(hide_menu,unsafe_allow_html=True)
    # Play the birthday song as background music
    def autoplay_audio(file_path: str):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio controls autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(
                md,
                unsafe_allow_html=True,
            )

    st.write("# 点击听好听的生日快乐歌 !")

    autoplay_audio("./static/happy_birthday_song.mp3")
    st.write("# 点击听最好听的生日快乐歌 !")
    autoplay_audio("./static/me.m4a")




    st.write("🎉 Happy Birthday! 🎉 生日快乐 🎉")
    time.sleep(1)
    st.balloons()

    # 配置左侧菜单项
    with st.sidebar:
        choose = option_menu("橙汁的网站", ["介绍", "图片", "视频"],
                             icons=['house', 'book-half', 'boombox-fill'],
                             menu_icon="bullseye", default_index=0)


    if choose == "介绍":
        st.title("欢迎来到橙汁的网站")
        st.title("Welcome to Orange Juice's Website")
        st.write("🎉 Happy Birthday! 🎉 生日快乐 🎉")


    elif choose == "图片":
        # 创建单独的容器，图片放入此容器中
        with st.container():
            # 将布局分为四列
            cols = st.columns(5)
            # 在第一列中添加图片，设置图片说明，并设置缩放比例
            cols[0].image("./static/image_1.jpeg","漫画中的橙汁",use_column_width=True)
            cols[1].image("./static/image_2.jpeg","腻歪中的橙汁",use_column_width=True)
            cols[2].image("./static/image_3.jpeg","装可爱的橙汁",use_column_width=True)
            cols[3].image("./static/image_4.jpeg","被包裹的橙汁",use_column_width=True)
            cols[4].image("./static/image_5.jpeg","粉树下的橙汁",use_column_width=True)




    elif choose == "视频":

        st.video("./static/1.mp4","被主人召唤找回的橙汁")
        st.video("./static/2.mp4","被主人召唤找回的橙汁")





        # # Home Page
        # def home_page():
        #
        #     st.write("Hello! I'm excited to share with you.")
        #
        # # Video Gallery
        # def video_gallery():
        #     st.title("Video Gallery")
        #     videos = [ "https://www.youtube.com/watch?v=VIDEO_ID_1",
        #                "https://www.youtube.com/watch?v=VIDEO_ID_2",
        #     # Add more video URLs
        #     ]
        #     for video_link in videos:
        #         st.video(video_link)
        #    # Photo Gallery
        #     def photo_gallery():
        #         st.title("Photo Gallery")
        #         images = [ "image_1.jpg", "image_2.jpg", "image_3.jpg", "image_4.jpg", "image_5.jpg" # Add more image URLs
        #         ]
        #         for image_url in images:
        #             st.image(image_url, caption='Image Caption', use_column_width=True)
        #
        #         # Sidebar navigation
        #         st.sidebar.title("Navigation")
        #         selected_page = st.sidebar.selectbox("Go to", ["Home", "Video Gallery", "Photo Gallery"])
        #         # Page content
        #         if selected_page == "Home":
        #             happy_birthday_animation()
        #         # Add animation before going to the home page
        #             home_page()
        #         elif selected_page == "Video Gallery":
        #             video_gallery()
        #         elif selected_page == "Photo Gallery":
        #             photo_gallery()
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
