# SNMP MIB module (NDS-DTH3-RS232DATA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-RS232DATA.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ndsDTH3Encoder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rs232Enc_ObjectIdentity = ObjectIdentity
rs232Enc = _Rs232Enc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8)
)


class _Rs232ModuleNumber_Type(Integer32):
    """Custom type rs232ModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Rs232ModuleNumber_Type.__name__ = "Integer32"
_Rs232ModuleNumber_Object = MibScalar
rs232ModuleNumber = _Rs232ModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 1),
    _Rs232ModuleNumber_Type()
)
rs232ModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232ModuleNumber.setStatus("current")
_Rs232ModuleTable_Object = MibTable
rs232ModuleTable = _Rs232ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 2)
)
if mibBuilder.loadTexts:
    rs232ModuleTable.setStatus("current")
_Rs232ModuleEntry_Object = MibTableRow
rs232ModuleEntry = _Rs232ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 2, 1)
)
rs232ModuleEntry.setIndexNames(
    (0, "NDS-DTH3-RS232DATA", "rs232ModIndex"),
)
if mibBuilder.loadTexts:
    rs232ModuleEntry.setStatus("current")


class _Rs232ModIndex_Type(Integer32):
    """Custom type rs232ModIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4),
          ("module5", 5),
          ("module6", 6),
          ("module7", 7))
    )


_Rs232ModIndex_Type.__name__ = "Integer32"
_Rs232ModIndex_Object = MibTableColumn
rs232ModIndex = _Rs232ModIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 2, 1, 1),
    _Rs232ModIndex_Type()
)
rs232ModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232ModIndex.setStatus("current")


class _Rs232HardwareRelease_Type(OctetString):
    """Custom type rs232HardwareRelease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Rs232HardwareRelease_Type.__name__ = "OctetString"
_Rs232HardwareRelease_Object = MibTableColumn
rs232HardwareRelease = _Rs232HardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 2, 1, 2),
    _Rs232HardwareRelease_Type()
)
rs232HardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232HardwareRelease.setStatus("current")


class _Rs232SoftwareRelease_Type(OctetString):
    """Custom type rs232SoftwareRelease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Rs232SoftwareRelease_Type.__name__ = "OctetString"
_Rs232SoftwareRelease_Object = MibTableColumn
rs232SoftwareRelease = _Rs232SoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 2, 1, 3),
    _Rs232SoftwareRelease_Type()
)
rs232SoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SoftwareRelease.setStatus("current")


class _Rs232FirmwareRelease_Type(OctetString):
    """Custom type rs232FirmwareRelease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Rs232FirmwareRelease_Type.__name__ = "OctetString"
_Rs232FirmwareRelease_Object = MibTableColumn
rs232FirmwareRelease = _Rs232FirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 2, 1, 4),
    _Rs232FirmwareRelease_Type()
)
rs232FirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232FirmwareRelease.setStatus("current")
_Rs232nextTimeDate_Type = OctetString
_Rs232nextTimeDate_Object = MibTableColumn
rs232nextTimeDate = _Rs232nextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 2, 1, 5),
    _Rs232nextTimeDate_Type()
)
rs232nextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232nextTimeDate.setStatus("current")
_Rs232Table_Object = MibTable
rs232Table = _Rs232Table_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3)
)
if mibBuilder.loadTexts:
    rs232Table.setStatus("current")
_Rs232Entry_Object = MibTableRow
rs232Entry = _Rs232Entry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1)
)
rs232Entry.setIndexNames(
    (0, "NDS-DTH3-RS232DATA", "rs232CurrentNextIndex"),
    (0, "NDS-DTH3-RS232DATA", "rs232ModuleIndex"),
)
if mibBuilder.loadTexts:
    rs232Entry.setStatus("current")


class _Rs232CurrentNextIndex_Type(Integer32):
    """Custom type rs232CurrentNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_Rs232CurrentNextIndex_Type.__name__ = "Integer32"
_Rs232CurrentNextIndex_Object = MibTableColumn
rs232CurrentNextIndex = _Rs232CurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1, 1),
    _Rs232CurrentNextIndex_Type()
)
rs232CurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232CurrentNextIndex.setStatus("current")


class _Rs232ModuleIndex_Type(Integer32):
    """Custom type rs232ModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("module1", 1),
          ("module2", 2),
          ("module3", 3),
          ("module4", 4),
          ("module5", 5),
          ("module6", 6),
          ("module7", 7))
    )


_Rs232ModuleIndex_Type.__name__ = "Integer32"
_Rs232ModuleIndex_Object = MibTableColumn
rs232ModuleIndex = _Rs232ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1, 2),
    _Rs232ModuleIndex_Type()
)
rs232ModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232ModuleIndex.setStatus("current")


class _Rs232Encode_Type(Integer32):
    """Custom type rs232Encode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on-TANDBERG", 1),
          ("on-DVB", 2))
    )


_Rs232Encode_Type.__name__ = "Integer32"
_Rs232Encode_Object = MibTableColumn
rs232Encode = _Rs232Encode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1, 3),
    _Rs232Encode_Type()
)
rs232Encode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232Encode.setStatus("current")


class _Rs232BaudRate_Type(Integer32):
    """Custom type rs232BaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rate-1200", 0),
          ("rate-2400", 1),
          ("rate-4800", 2),
          ("rate-9600", 3),
          ("rate-19200", 4),
          ("rate-38400", 5))
    )


_Rs232BaudRate_Type.__name__ = "Integer32"
_Rs232BaudRate_Object = MibTableColumn
rs232BaudRate = _Rs232BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1, 4),
    _Rs232BaudRate_Type()
)
rs232BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232BaudRate.setStatus("current")


class _Rs232TestPattern_Type(Integer32):
    """Custom type rs232TestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Rs232TestPattern_Type.__name__ = "Integer32"
_Rs232TestPattern_Object = MibTableColumn
rs232TestPattern = _Rs232TestPattern_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1, 5),
    _Rs232TestPattern_Type()
)
rs232TestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232TestPattern.setStatus("current")


class _Rs232DMode_Type(Integer32):
    """Custom type rs232DMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("internally-formatted", 0),
          ("externally-formatted", 1))
    )


_Rs232DMode_Type.__name__ = "Integer32"
_Rs232DMode_Object = MibTableColumn
rs232DMode = _Rs232DMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1, 6),
    _Rs232DMode_Type()
)
rs232DMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232DMode.setStatus("current")


class _Rs232Delay_Type(Integer32):
    """Custom type rs232Delay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Rs232Delay_Type.__name__ = "Integer32"
_Rs232Delay_Object = MibTableColumn
rs232Delay = _Rs232Delay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1, 7),
    _Rs232Delay_Type()
)
rs232Delay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232Delay.setStatus("current")


class _Rs232PID_Type(Integer32):
    """Custom type rs232PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_Rs232PID_Type.__name__ = "Integer32"
_Rs232PID_Object = MibTableColumn
rs232PID = _Rs232PID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1, 8),
    _Rs232PID_Type()
)
rs232PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PID.setStatus("current")


class _Rs232ComponentTag_Type(Integer32):
    """Custom type rs232ComponentTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Rs232ComponentTag_Type.__name__ = "Integer32"
_Rs232ComponentTag_Object = MibTableColumn
rs232ComponentTag = _Rs232ComponentTag_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1, 9),
    _Rs232ComponentTag_Type()
)
rs232ComponentTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232ComponentTag.setStatus("current")


class _Rs232BufferData_Type(Integer32):
    """Custom type rs232BufferData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("wait-1-second", 0),
          ("send-immediately", 1))
    )


_Rs232BufferData_Type.__name__ = "Integer32"
_Rs232BufferData_Object = MibTableColumn
rs232BufferData = _Rs232BufferData_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 8, 3, 1, 10),
    _Rs232BufferData_Type()
)
rs232BufferData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232BufferData.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-RS232DATA",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "rs232Enc": rs232Enc,
       "rs232ModuleNumber": rs232ModuleNumber,
       "rs232ModuleTable": rs232ModuleTable,
       "rs232ModuleEntry": rs232ModuleEntry,
       "rs232ModIndex": rs232ModIndex,
       "rs232HardwareRelease": rs232HardwareRelease,
       "rs232SoftwareRelease": rs232SoftwareRelease,
       "rs232FirmwareRelease": rs232FirmwareRelease,
       "rs232nextTimeDate": rs232nextTimeDate,
       "rs232Table": rs232Table,
       "rs232Entry": rs232Entry,
       "rs232CurrentNextIndex": rs232CurrentNextIndex,
       "rs232ModuleIndex": rs232ModuleIndex,
       "rs232Encode": rs232Encode,
       "rs232BaudRate": rs232BaudRate,
       "rs232TestPattern": rs232TestPattern,
       "rs232DMode": rs232DMode,
       "rs232Delay": rs232Delay,
       "rs232PID": rs232PID,
       "rs232ComponentTag": rs232ComponentTag,
       "rs232BufferData": rs232BufferData}
)
