# SNMP MIB module (DIGI-MOBILE-INFORMATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-MOBILE-INFORMATION-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
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

(digiMobileInfo,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiMobileInfo")

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

_MiNumber_Type = Integer32
_MiNumber_Object = MibScalar
miNumber = _MiNumber_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 1),
    _MiNumber_Type()
)
miNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miNumber.setStatus("mandatory")
_MiTable_Object = MibTable
miTable = _MiTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 2)
)
if mibBuilder.loadTexts:
    miTable.setStatus("mandatory")
_MiEntry_Object = MibTableRow
miEntry = _MiEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 2, 1)
)
miEntry.setIndexNames(
    (0, "DIGI-MOBILE-INFORMATION-MIB", "miIndex"),
)
if mibBuilder.loadTexts:
    miEntry.setStatus("mandatory")
_MiIndex_Type = Integer32
_MiIndex_Object = MibTableColumn
miIndex = _MiIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 2, 1, 1),
    _MiIndex_Type()
)
miIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miIndex.setStatus("mandatory")


class _MiNumFields_Type(Integer32):
    """Custom type miNumFields based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MiNumFields_Type.__name__ = "Integer32"
_MiNumFields_Object = MibTableColumn
miNumFields = _MiNumFields_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 2, 1, 2),
    _MiNumFields_Type()
)
miNumFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miNumFields.setStatus("mandatory")
_MiInfoTable_Object = MibTable
miInfoTable = _MiInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 3)
)
if mibBuilder.loadTexts:
    miInfoTable.setStatus("mandatory")
_MiInfoEntry_Object = MibTableRow
miInfoEntry = _MiInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 3, 1)
)
miInfoEntry.setIndexNames(
    (0, "DIGI-MOBILE-INFORMATION-MIB", "miInfoInterface"),
    (0, "DIGI-MOBILE-INFORMATION-MIB", "miInfoIndex"),
)
if mibBuilder.loadTexts:
    miInfoEntry.setStatus("mandatory")
_MiInfoInterface_Type = Integer32
_MiInfoInterface_Object = MibTableColumn
miInfoInterface = _MiInfoInterface_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 3, 1, 1),
    _MiInfoInterface_Type()
)
miInfoInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miInfoInterface.setStatus("mandatory")


class _MiInfoIndex_Type(Integer32):
    """Custom type miInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MiInfoIndex_Type.__name__ = "Integer32"
_MiInfoIndex_Object = MibTableColumn
miInfoIndex = _MiInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 3, 1, 2),
    _MiInfoIndex_Type()
)
miInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miInfoIndex.setStatus("mandatory")


class _MiInfoName_Type(OctetString):
    """Custom type miInfoName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MiInfoName_Type.__name__ = "OctetString"
_MiInfoName_Object = MibTableColumn
miInfoName = _MiInfoName_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 3, 1, 3),
    _MiInfoName_Type()
)
miInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miInfoName.setStatus("mandatory")


class _MiInfoValue_Type(OctetString):
    """Custom type miInfoValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_MiInfoValue_Type.__name__ = "OctetString"
_MiInfoValue_Object = MibTableColumn
miInfoValue = _MiInfoValue_Object(
    (1, 3, 6, 1, 4, 1, 332, 11, 6, 3, 3, 1, 4),
    _MiInfoValue_Type()
)
miInfoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miInfoValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-MOBILE-INFORMATION-MIB",
    **{"miNumber": miNumber,
       "miTable": miTable,
       "miEntry": miEntry,
       "miIndex": miIndex,
       "miNumFields": miNumFields,
       "miInfoTable": miInfoTable,
       "miInfoEntry": miInfoEntry,
       "miInfoInterface": miInfoInterface,
       "miInfoIndex": miInfoIndex,
       "miInfoName": miInfoName,
       "miInfoValue": miInfoValue}
)
