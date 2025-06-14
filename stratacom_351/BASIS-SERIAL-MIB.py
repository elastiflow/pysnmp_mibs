# SNMP MIB module (BASIS-SERIAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/stratacom_351/BASIS-SERIAL-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:03:53 2025
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

(basisLines,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "basisLines")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

basisSerialMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 69)
)
if mibBuilder.loadTexts:
    basisSerialMIB.setRevisions(
        ("2003-05-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SerialInterface_ObjectIdentity = ObjectIdentity
serialInterface = _SerialInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 1)
)
_SerialInterfaceTable_Object = MibTable
serialInterfaceTable = _SerialInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1)
)
if mibBuilder.loadTexts:
    serialInterfaceTable.setStatus("current")
_SerialInterfaceEntry_Object = MibTableRow
serialInterfaceEntry = _SerialInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1)
)
serialInterfaceEntry.setIndexNames(
    (0, "BASIS-SERIAL-MIB", "serialPortNum"),
)
if mibBuilder.loadTexts:
    serialInterfaceEntry.setStatus("current")


class _SerialPortNum_Type(Integer32):
    """Custom type serialPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SerialPortNum_Type.__name__ = "Integer32"
_SerialPortNum_Object = MibTableColumn
serialPortNum = _SerialPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 1),
    _SerialPortNum_Type()
)
serialPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortNum.setStatus("current")


class _SerialPortType_Type(Integer32):
    """Custom type serialPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("debug", 2))
    )


_SerialPortType_Type.__name__ = "Integer32"
_SerialPortType_Object = MibTableColumn
serialPortType = _SerialPortType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 2),
    _SerialPortType_Type()
)
serialPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortType.setStatus("current")


class _SerialPortEnable_Type(Integer32):
    """Custom type serialPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SerialPortEnable_Type.__name__ = "Integer32"
_SerialPortEnable_Object = MibTableColumn
serialPortEnable = _SerialPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 3),
    _SerialPortEnable_Type()
)
serialPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortEnable.setStatus("current")


class _SerialPortbps_Type(Integer32):
    """Custom type serialPortbps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bps9600", 1),
          ("bps2400", 2),
          ("bps19200", 3))
    )


_SerialPortbps_Type.__name__ = "Integer32"
_SerialPortbps_Object = MibTableColumn
serialPortbps = _SerialPortbps_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 1, 1, 4),
    _SerialPortbps_Type()
)
serialPortbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPortbps.setStatus("current")


class _SerialPortNumOfValidEntries_Type(Integer32):
    """Custom type serialPortNumOfValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SerialPortNumOfValidEntries_Type.__name__ = "Integer32"
_SerialPortNumOfValidEntries_Object = MibScalar
serialPortNumOfValidEntries = _SerialPortNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 1, 2),
    _SerialPortNumOfValidEntries_Type()
)
serialPortNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialPortNumOfValidEntries.setStatus("current")
_BasisSerialMIBConformance_ObjectIdentity = ObjectIdentity
basisSerialMIBConformance = _BasisSerialMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 69, 2)
)
_BasisSerialMIBGroups_ObjectIdentity = ObjectIdentity
basisSerialMIBGroups = _BasisSerialMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 1)
)
_BasisSerialMIBCompliances_ObjectIdentity = ObjectIdentity
basisSerialMIBCompliances = _BasisSerialMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 2)
)

# Managed Objects groups

basisSerialConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 1, 1)
)
basisSerialConfGroup.setObjects(
      *(("BASIS-SERIAL-MIB", "serialPortNumOfValidEntries"),
        ("BASIS-SERIAL-MIB", "serialPortNum"),
        ("BASIS-SERIAL-MIB", "serialPortType"),
        ("BASIS-SERIAL-MIB", "serialPortEnable"),
        ("BASIS-SERIAL-MIB", "serialPortbps"))
)
if mibBuilder.loadTexts:
    basisSerialConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basisSerialCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 69, 2, 2, 1)
)
basisSerialCompliance.setObjects(
    ("BASIS-SERIAL-MIB", "basisSerialConfGroup")
)
if mibBuilder.loadTexts:
    basisSerialCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BASIS-SERIAL-MIB",
    **{"serialInterface": serialInterface,
       "serialInterfaceTable": serialInterfaceTable,
       "serialInterfaceEntry": serialInterfaceEntry,
       "serialPortNum": serialPortNum,
       "serialPortType": serialPortType,
       "serialPortEnable": serialPortEnable,
       "serialPortbps": serialPortbps,
       "serialPortNumOfValidEntries": serialPortNumOfValidEntries,
       "basisSerialMIB": basisSerialMIB,
       "basisSerialMIBConformance": basisSerialMIBConformance,
       "basisSerialMIBGroups": basisSerialMIBGroups,
       "basisSerialConfGroup": basisSerialConfGroup,
       "basisSerialMIBCompliances": basisSerialMIBCompliances,
       "basisSerialCompliance": basisSerialCompliance}
)
