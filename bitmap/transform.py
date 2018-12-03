import cmd
import sys
import bitmap


class BitmapManipulator(cmd.Cmd):
    intro = 'Welcome to the bitmap manipulator.   Type help or ? to list commands.\n'
    prompt = '> '

    @staticmethod
    def do_get_headers(source):
        """
        To use this type 'get_headers' followed by the file location's source.

        get_headers <source>

        Returns a line-item response of the file's header data.
        """
        try:
            read_headers = bitmap.Bitmap.read_file(source)
            print(read_headers.get_headers())

        except:
            print('Invalid input.  Type "help get_headers" for more information.')

    def do_transform(self, arg):
        """
        To use this type in 'transform' followed by
        the original file location and the new file location
        and the type of change you would like to do.

        transform <original> <new> <transform>

        Creates a new file at 'new' location with the provided 'transform' applied to the new file.
        """
        arg_split = arg.split()
        try:
            check_args = bitmap.Bitmap.read_file(arg_split[0])
            if arg_split[2] == 'invert':
                check_args.invert('invert')
            if arg_split[2] == 'red':
                check_args.red('red')
            if arg_split[2] == 'blue':
                check_args.blue('blue')
            if arg_split[2] == 'random_color':
                check_args.random_color('random_color')

            check_args.write_file(arg_split[1])

        except:
            print('Invalid input.  Type "help transform" for more information.')

    @staticmethod
    def do_exit(args):
        """To use this type in 'exit' and the CLI tool will cleanly exit the running application."""
        sys.exit()


if __name__ == '__main__':
    try:
        BitmapManipulator().cmdloop()
    except KeyboardInterrupt:
        print('Goodbye!')
