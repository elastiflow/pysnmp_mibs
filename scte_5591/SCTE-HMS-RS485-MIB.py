# SNMP MIB module (SCTE-HMS-RS485-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-RS485-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:36:31 2025
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

(transponderInterfaceBusIdent,) = mibBuilder.importSymbols(
    "SCTE-HMS-ROOTS",
    "transponderInterfaceBusIdent")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rs485attachedDevices_Type = Integer32
_Rs485attachedDevices_Object = MibScalar
rs485attachedDevices = _Rs485attachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 1),
    _Rs485attachedDevices_Type()
)
rs485attachedDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs485attachedDevices.setStatus("mandatory")
_Rs485commStatus_Type = Integer32
_Rs485commStatus_Object = MibScalar
rs485commStatus = _Rs485commStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 2),
    _Rs485commStatus_Type()
)
rs485commStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs485commStatus.setStatus("mandatory")
_Rs485DevicesAddressedTable_Object = MibTable
rs485DevicesAddressedTable = _Rs485DevicesAddressedTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 3)
)
if mibBuilder.loadTexts:
    rs485DevicesAddressedTable.setStatus("mandatory")
_Rs485DevicesAddressedEntry_Object = MibTableRow
rs485DevicesAddressedEntry = _Rs485DevicesAddressedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1)
)
rs485DevicesAddressedEntry.setIndexNames(
    (0, "SCTE-HMS-RS485-MIB", "rs485DeviceAddress"),
)
if mibBuilder.loadTexts:
    rs485DevicesAddressedEntry.setStatus("mandatory")


class _Rs485DeviceAddress_Type(Integer32):
    """Custom type rs485DeviceAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Rs485DeviceAddress_Type.__name__ = "Integer32"
_Rs485DeviceAddress_Object = MibTableColumn
rs485DeviceAddress = _Rs485DeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1, 1),
    _Rs485DeviceAddress_Type()
)
rs485DeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs485DeviceAddress.setStatus("mandatory")
_Rs485DeviceIdentity_Type = ObjectIdentifier
_Rs485DeviceIdentity_Object = MibTableColumn
rs485DeviceIdentity = _Rs485DeviceIdentity_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1, 2),
    _Rs485DeviceIdentity_Type()
)
rs485DeviceIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs485DeviceIdentity.setStatus("mandatory")


class _Rs485controlMode_Type(Integer32):
    """Custom type rs485controlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remote", 1),
          ("local", 2),
          ("notCommunicating", 3))
    )


_Rs485controlMode_Type.__name__ = "Integer32"
_Rs485controlMode_Object = MibTableColumn
rs485controlMode = _Rs485controlMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1, 3),
    _Rs485controlMode_Type()
)
rs485controlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs485controlMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-RS485-MIB",
    **{"rs485attachedDevices": rs485attachedDevices,
       "rs485commStatus": rs485commStatus,
       "rs485DevicesAddressedTable": rs485DevicesAddressedTable,
       "rs485DevicesAddressedEntry": rs485DevicesAddressedEntry,
       "rs485DeviceAddress": rs485DeviceAddress,
       "rs485DeviceIdentity": rs485DeviceIdentity,
       "rs485controlMode": rs485controlMode}
)
