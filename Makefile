NAME	=	bombyx

SRC	=	bombyx.py

$(NAME):
	cp $(SRC) $(NAME)
	chmod 755 $(NAME)

all:	$(NAME)
