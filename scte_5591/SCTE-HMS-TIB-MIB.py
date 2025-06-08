# SNMP MIB module (SCTE-HMS-TIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-TIB-MIB.mib
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

_TibAttachedDevices_Type = Integer32
_TibAttachedDevices_Object = MibScalar
tibAttachedDevices = _TibAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 1),
    _TibAttachedDevices_Type()
)
tibAttachedDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tibAttachedDevices.setStatus("mandatory")
_TibCommStatus_Type = Integer32
_TibCommStatus_Object = MibScalar
tibCommStatus = _TibCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 2),
    _TibCommStatus_Type()
)
tibCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tibCommStatus.setStatus("mandatory")
_TibDevicesAddressedTable_Object = MibTable
tibDevicesAddressedTable = _TibDevicesAddressedTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 3)
)
if mibBuilder.loadTexts:
    tibDevicesAddressedTable.setStatus("mandatory")
_TibDevicesAddressedEntry_Object = MibTableRow
tibDevicesAddressedEntry = _TibDevicesAddressedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1)
)
tibDevicesAddressedEntry.setIndexNames(
    (0, "SCTE-HMS-TIB-MIB", "tibDeviceAddress"),
)
if mibBuilder.loadTexts:
    tibDevicesAddressedEntry.setStatus("mandatory")


class _TibDeviceAddress_Type(Integer32):
    """Custom type tibDeviceAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TibDeviceAddress_Type.__name__ = "Integer32"
_TibDeviceAddress_Object = MibTableColumn
tibDeviceAddress = _TibDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1, 1),
    _TibDeviceAddress_Type()
)
tibDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tibDeviceAddress.setStatus("mandatory")
_TibDeviceIdentity_Type = ObjectIdentifier
_TibDeviceIdentity_Object = MibTableColumn
tibDeviceIdentity = _TibDeviceIdentity_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1, 2),
    _TibDeviceIdentity_Type()
)
tibDeviceIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tibDeviceIdentity.setStatus("mandatory")


class _TibControlMode_Type(Integer32):
    """Custom type tibControlMode based on Integer32"""
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


_TibControlMode_Type.__name__ = "Integer32"
_TibControlMode_Object = MibTableColumn
tibControlMode = _TibControlMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 7, 3, 1, 3),
    _TibControlMode_Type()
)
tibControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tibControlMode.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-TIB-MIB",
    **{"tibAttachedDevices": tibAttachedDevices,
       "tibCommStatus": tibCommStatus,
       "tibDevicesAddressedTable": tibDevicesAddressedTable,
       "tibDevicesAddressedEntry": tibDevicesAddressedEntry,
       "tibDeviceAddress": tibDeviceAddress,
       "tibDeviceIdentity": tibDeviceIdentity,
       "tibControlMode": tibControlMode}
)
