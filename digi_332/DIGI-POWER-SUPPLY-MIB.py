# SNMP MIB module (DIGI-POWER-SUPPLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-POWER-SUPPLY-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:31 2025
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

(digiPowerSupply,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiPowerSupply")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 12, 11)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("mandatory")
_PowerSupplyEntry_Object = MibTableRow
powerSupplyEntry = _PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 12, 11, 1)
)
powerSupplyEntry.setIndexNames(
    (0, "DIGI-POWER-SUPPLY-MIB", "powerSupplyIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyEntry.setStatus("mandatory")
_PowerSupplyIndex_Type = Integer32
_PowerSupplyIndex_Object = MibTableColumn
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 12, 11, 1, 11),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("mandatory")
_PowerSupplyDescription_Type = DisplayString
_PowerSupplyDescription_Object = MibTableColumn
powerSupplyDescription = _PowerSupplyDescription_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 12, 11, 1, 12),
    _PowerSupplyDescription_Type()
)
powerSupplyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyDescription.setStatus("mandatory")


class _PowerSupplyType_Type(Integer32):
    """Custom type powerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("internal", 3),
          ("external", 4),
          ("powered-Ethernet", 5),
          ("serialPowerRI", 6))
    )


_PowerSupplyType_Type.__name__ = "Integer32"
_PowerSupplyType_Object = MibTableColumn
powerSupplyType = _PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 12, 11, 1, 13),
    _PowerSupplyType_Type()
)
powerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyType.setStatus("mandatory")


class _PowerSupplyStatus_Type(Integer32):
    """Custom type powerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("malfunction", 2),
          ("disabled", 3),
          ("redundant", 4),
          ("engaged", 5))
    )


_PowerSupplyStatus_Type.__name__ = "Integer32"
_PowerSupplyStatus_Object = MibTableColumn
powerSupplyStatus = _PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 13, 12, 11, 1, 14),
    _PowerSupplyStatus_Type()
)
powerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-POWER-SUPPLY-MIB",
    **{"DisplayString": DisplayString,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyEntry": powerSupplyEntry,
       "powerSupplyIndex": powerSupplyIndex,
       "powerSupplyDescription": powerSupplyDescription,
       "powerSupplyType": powerSupplyType,
       "powerSupplyStatus": powerSupplyStatus}
)
