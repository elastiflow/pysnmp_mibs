# SNMP MIB module (SAPEX-ENTITIES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/prescom_28855/SAPEX-ENTITIES-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:58:11 2025
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

(netSnmp,) = mibBuilder.importSymbols(
    "NET-SNMP-MIB",
    "netSnmp")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

sapexEntities = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Prescom_ObjectIdentity = ObjectIdentity
prescom = _Prescom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1)
)
_Mxs_ObjectIdentity = ObjectIdentity
mxs = _Mxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 1)
)
_NewGvr_ObjectIdentity = ObjectIdentity
newGvr = _NewGvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2)
)
_EntityAsteriskNotification_ObjectIdentity = ObjectIdentity
entityAsteriskNotification = _EntityAsteriskNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 1)
)
_EntityAsteriskTable_Object = MibTable
entityAsteriskTable = _EntityAsteriskTable_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    entityAsteriskTable.setStatus("current")
_EntityAsteriskEntry_Object = MibTableRow
entityAsteriskEntry = _EntityAsteriskEntry_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 1, 1, 1)
)
entityAsteriskEntry.setIndexNames(
    (0, "SAPEX-ENTITIES-MIB", "entityAsteriskEntryType"),
)
if mibBuilder.loadTexts:
    entityAsteriskEntry.setStatus("current")


class _EntityAsteriskEntryType_Type(DisplayString):
    """Custom type entityAsteriskEntryType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EntityAsteriskEntryType_Type.__name__ = "DisplayString"
_EntityAsteriskEntryType_Object = MibTableColumn
entityAsteriskEntryType = _EntityAsteriskEntryType_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 1, 1, 1, 1),
    _EntityAsteriskEntryType_Type()
)
entityAsteriskEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityAsteriskEntryType.setStatus("current")


class _EntityAsteriskEntryName_Type(DisplayString):
    """Custom type entityAsteriskEntryName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityAsteriskEntryName_Type.__name__ = "DisplayString"
_EntityAsteriskEntryName_Object = MibTableColumn
entityAsteriskEntryName = _EntityAsteriskEntryName_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 1, 1, 1, 2),
    _EntityAsteriskEntryName_Type()
)
entityAsteriskEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityAsteriskEntryName.setStatus("current")


class _EntityAsteriskEntryVal_Type(DisplayString):
    """Custom type entityAsteriskEntryVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_EntityAsteriskEntryVal_Type.__name__ = "DisplayString"
_EntityAsteriskEntryVal_Object = MibTableColumn
entityAsteriskEntryVal = _EntityAsteriskEntryVal_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 1, 1, 1, 3),
    _EntityAsteriskEntryVal_Type()
)
entityAsteriskEntryVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityAsteriskEntryVal.setStatus("current")


class _EntityAsteriskEntryAddress_Type(DisplayString):
    """Custom type entityAsteriskEntryAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EntityAsteriskEntryAddress_Type.__name__ = "DisplayString"
_EntityAsteriskEntryAddress_Object = MibTableColumn
entityAsteriskEntryAddress = _EntityAsteriskEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 1, 1, 1, 4),
    _EntityAsteriskEntryAddress_Type()
)
entityAsteriskEntryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityAsteriskEntryAddress.setStatus("current")


class _EntityAsteriskEntryUptime_Type(DisplayString):
    """Custom type entityAsteriskEntryUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityAsteriskEntryUptime_Type.__name__ = "DisplayString"
_EntityAsteriskEntryUptime_Object = MibTableColumn
entityAsteriskEntryUptime = _EntityAsteriskEntryUptime_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 1, 1, 1, 5),
    _EntityAsteriskEntryUptime_Type()
)
entityAsteriskEntryUptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityAsteriskEntryUptime.setStatus("current")
_EntityGCMNotification_ObjectIdentity = ObjectIdentity
entityGCMNotification = _EntityGCMNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2)
)
_EntityGCMTable_Object = MibTable
entityGCMTable = _EntityGCMTable_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    entityGCMTable.setStatus("current")
_EntityGCMEntry_Object = MibTableRow
entityGCMEntry = _EntityGCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1, 1)
)
entityGCMEntry.setIndexNames(
    (0, "SAPEX-ENTITIES-MIB", "entityGCMEntryType"),
)
if mibBuilder.loadTexts:
    entityGCMEntry.setStatus("current")


class _EntityGCMEntryType_Type(DisplayString):
    """Custom type entityGCMEntryType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EntityGCMEntryType_Type.__name__ = "DisplayString"
_EntityGCMEntryType_Object = MibTableColumn
entityGCMEntryType = _EntityGCMEntryType_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1, 1, 1),
    _EntityGCMEntryType_Type()
)
entityGCMEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGCMEntryType.setStatus("current")


class _EntityGCMEntryName_Type(DisplayString):
    """Custom type entityGCMEntryName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityGCMEntryName_Type.__name__ = "DisplayString"
_EntityGCMEntryName_Object = MibTableColumn
entityGCMEntryName = _EntityGCMEntryName_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1, 1, 2),
    _EntityGCMEntryName_Type()
)
entityGCMEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGCMEntryName.setStatus("current")


class _EntityGCMEntryId_Type(DisplayString):
    """Custom type entityGCMEntryId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityGCMEntryId_Type.__name__ = "DisplayString"
_EntityGCMEntryId_Object = MibTableColumn
entityGCMEntryId = _EntityGCMEntryId_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1, 1, 3),
    _EntityGCMEntryId_Type()
)
entityGCMEntryId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGCMEntryId.setStatus("current")


class _EntityGCMEntryMajor_Type(DisplayString):
    """Custom type entityGCMEntryMajor based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGCMEntryMajor_Type.__name__ = "DisplayString"
_EntityGCMEntryMajor_Object = MibTableColumn
entityGCMEntryMajor = _EntityGCMEntryMajor_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1, 1, 4),
    _EntityGCMEntryMajor_Type()
)
entityGCMEntryMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGCMEntryMajor.setStatus("current")


class _EntityGCMEntryMinor_Type(DisplayString):
    """Custom type entityGCMEntryMinor based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGCMEntryMinor_Type.__name__ = "DisplayString"
_EntityGCMEntryMinor_Object = MibTableColumn
entityGCMEntryMinor = _EntityGCMEntryMinor_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1, 1, 5),
    _EntityGCMEntryMinor_Type()
)
entityGCMEntryMinor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGCMEntryMinor.setStatus("current")


class _EntityGCMEntryDelayed_Type(DisplayString):
    """Custom type entityGCMEntryDelayed based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGCMEntryDelayed_Type.__name__ = "DisplayString"
_EntityGCMEntryDelayed_Object = MibTableColumn
entityGCMEntryDelayed = _EntityGCMEntryDelayed_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1, 1, 6),
    _EntityGCMEntryDelayed_Type()
)
entityGCMEntryDelayed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGCMEntryDelayed.setStatus("current")


class _EntityGCMEntryGCAR_Type(DisplayString):
    """Custom type entityGCMEntryGCAR based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGCMEntryGCAR_Type.__name__ = "DisplayString"
_EntityGCMEntryGCAR_Object = MibTableColumn
entityGCMEntryGCAR = _EntityGCMEntryGCAR_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1, 1, 7),
    _EntityGCMEntryGCAR_Type()
)
entityGCMEntryGCAR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGCMEntryGCAR.setStatus("current")


class _EntityGCMEntryGCAA_Type(DisplayString):
    """Custom type entityGCMEntryGCAA based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGCMEntryGCAA_Type.__name__ = "DisplayString"
_EntityGCMEntryGCAA_Object = MibTableColumn
entityGCMEntryGCAA = _EntityGCMEntryGCAA_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1, 1, 8),
    _EntityGCMEntryGCAA_Type()
)
entityGCMEntryGCAA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGCMEntryGCAA.setStatus("current")


class _EntityGCMEntryUptime_Type(DisplayString):
    """Custom type entityGCMEntryUptime based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityGCMEntryUptime_Type.__name__ = "DisplayString"
_EntityGCMEntryUptime_Object = MibTableColumn
entityGCMEntryUptime = _EntityGCMEntryUptime_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 2, 1, 1, 9),
    _EntityGCMEntryUptime_Type()
)
entityGCMEntryUptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGCMEntryUptime.setStatus("current")
_EntityPENotification_ObjectIdentity = ObjectIdentity
entityPENotification = _EntityPENotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 3)
)
_EntityPETable_Object = MibTable
entityPETable = _EntityPETable_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    entityPETable.setStatus("current")
_EntityPEEntry_Object = MibTableRow
entityPEEntry = _EntityPEEntry_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 3, 1, 1)
)
entityPEEntry.setIndexNames(
    (0, "SAPEX-ENTITIES-MIB", "entityPEEntryType"),
)
if mibBuilder.loadTexts:
    entityPEEntry.setStatus("current")


class _EntityPEEntryType_Type(DisplayString):
    """Custom type entityPEEntryType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EntityPEEntryType_Type.__name__ = "DisplayString"
_EntityPEEntryType_Object = MibTableColumn
entityPEEntryType = _EntityPEEntryType_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 3, 1, 1, 1),
    _EntityPEEntryType_Type()
)
entityPEEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityPEEntryType.setStatus("current")


class _EntityPEEntryName_Type(DisplayString):
    """Custom type entityPEEntryName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityPEEntryName_Type.__name__ = "DisplayString"
_EntityPEEntryName_Object = MibTableColumn
entityPEEntryName = _EntityPEEntryName_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 3, 1, 1, 2),
    _EntityPEEntryName_Type()
)
entityPEEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityPEEntryName.setStatus("current")


class _EntityPEEntryId_Type(DisplayString):
    """Custom type entityPEEntryId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityPEEntryId_Type.__name__ = "DisplayString"
_EntityPEEntryId_Object = MibTableColumn
entityPEEntryId = _EntityPEEntryId_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 3, 1, 1, 3),
    _EntityPEEntryId_Type()
)
entityPEEntryId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityPEEntryId.setStatus("current")


class _EntityPEEntryED137_Type(DisplayString):
    """Custom type entityPEEntryED137 based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityPEEntryED137_Type.__name__ = "DisplayString"
_EntityPEEntryED137_Object = MibTableColumn
entityPEEntryED137 = _EntityPEEntryED137_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 3, 1, 1, 4),
    _EntityPEEntryED137_Type()
)
entityPEEntryED137.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityPEEntryED137.setStatus("current")


class _EntityPEEntrySIP_Type(DisplayString):
    """Custom type entityPEEntrySIP based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityPEEntrySIP_Type.__name__ = "DisplayString"
_EntityPEEntrySIP_Object = MibTableColumn
entityPEEntrySIP = _EntityPEEntrySIP_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 3, 1, 1, 5),
    _EntityPEEntrySIP_Type()
)
entityPEEntrySIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityPEEntrySIP.setStatus("current")


class _EntityPEEntryUptime_Type(DisplayString):
    """Custom type entityPEEntryUptime based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityPEEntryUptime_Type.__name__ = "DisplayString"
_EntityPEEntryUptime_Object = MibTableColumn
entityPEEntryUptime = _EntityPEEntryUptime_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 3, 1, 1, 6),
    _EntityPEEntryUptime_Type()
)
entityPEEntryUptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityPEEntryUptime.setStatus("current")
_EntityGatewayNotification_ObjectIdentity = ObjectIdentity
entityGatewayNotification = _EntityGatewayNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4)
)
_EntityGatewayTable_Object = MibTable
entityGatewayTable = _EntityGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    entityGatewayTable.setStatus("current")
_EntityGatewayEntry_Object = MibTableRow
entityGatewayEntry = _EntityGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1)
)
entityGatewayEntry.setIndexNames(
    (0, "SAPEX-ENTITIES-MIB", "entityGatewayEntryType"),
)
if mibBuilder.loadTexts:
    entityGatewayEntry.setStatus("current")


class _EntityGatewayEntryType_Type(DisplayString):
    """Custom type entityGatewayEntryType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EntityGatewayEntryType_Type.__name__ = "DisplayString"
_EntityGatewayEntryType_Object = MibTableColumn
entityGatewayEntryType = _EntityGatewayEntryType_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 1),
    _EntityGatewayEntryType_Type()
)
entityGatewayEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryType.setStatus("current")


class _EntityGatewayEntryName_Type(DisplayString):
    """Custom type entityGatewayEntryName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityGatewayEntryName_Type.__name__ = "DisplayString"
_EntityGatewayEntryName_Object = MibTableColumn
entityGatewayEntryName = _EntityGatewayEntryName_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 2),
    _EntityGatewayEntryName_Type()
)
entityGatewayEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryName.setStatus("current")


class _EntityGatewayEntryId_Type(DisplayString):
    """Custom type entityGatewayEntryId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityGatewayEntryId_Type.__name__ = "DisplayString"
_EntityGatewayEntryId_Object = MibTableColumn
entityGatewayEntryId = _EntityGatewayEntryId_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 3),
    _EntityGatewayEntryId_Type()
)
entityGatewayEntryId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryId.setStatus("current")


class _EntityGatewayEntryED137_Type(DisplayString):
    """Custom type entityGatewayEntryED137 based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryED137_Type.__name__ = "DisplayString"
_EntityGatewayEntryED137_Object = MibTableColumn
entityGatewayEntryED137 = _EntityGatewayEntryED137_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 4),
    _EntityGatewayEntryED137_Type()
)
entityGatewayEntryED137.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryED137.setStatus("current")


class _EntityGatewayEntrySIP_Type(DisplayString):
    """Custom type entityGatewayEntrySIP based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntrySIP_Type.__name__ = "DisplayString"
_EntityGatewayEntrySIP_Object = MibTableColumn
entityGatewayEntrySIP = _EntityGatewayEntrySIP_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 5),
    _EntityGatewayEntrySIP_Type()
)
entityGatewayEntrySIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntrySIP.setStatus("current")


class _EntityGatewayEntryIPB_Type(DisplayString):
    """Custom type entityGatewayEntryIPB based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryIPB_Type.__name__ = "DisplayString"
_EntityGatewayEntryIPB_Object = MibTableColumn
entityGatewayEntryIPB = _EntityGatewayEntryIPB_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 6),
    _EntityGatewayEntryIPB_Type()
)
entityGatewayEntryIPB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryIPB.setStatus("current")


class _EntityGatewayEntryIP_Type(DisplayString):
    """Custom type entityGatewayEntryIP based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryIP_Type.__name__ = "DisplayString"
_EntityGatewayEntryIP_Object = MibTableColumn
entityGatewayEntryIP = _EntityGatewayEntryIP_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 7),
    _EntityGatewayEntryIP_Type()
)
entityGatewayEntryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryIP.setStatus("current")


class _EntityGatewayEntryTEMP_Type(DisplayString):
    """Custom type entityGatewayEntryTEMP based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryTEMP_Type.__name__ = "DisplayString"
_EntityGatewayEntryTEMP_Object = MibTableColumn
entityGatewayEntryTEMP = _EntityGatewayEntryTEMP_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 8),
    _EntityGatewayEntryTEMP_Type()
)
entityGatewayEntryTEMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryTEMP.setStatus("current")


class _EntityGatewayEntryMPOW_Type(DisplayString):
    """Custom type entityGatewayEntryMPOW based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryMPOW_Type.__name__ = "DisplayString"
_EntityGatewayEntryMPOW_Object = MibTableColumn
entityGatewayEntryMPOW = _EntityGatewayEntryMPOW_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 9),
    _EntityGatewayEntryMPOW_Type()
)
entityGatewayEntryMPOW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryMPOW.setStatus("current")


class _EntityGatewayEntrySPOW_Type(DisplayString):
    """Custom type entityGatewayEntrySPOW based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntrySPOW_Type.__name__ = "DisplayString"
_EntityGatewayEntrySPOW_Object = MibTableColumn
entityGatewayEntrySPOW = _EntityGatewayEntrySPOW_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 10),
    _EntityGatewayEntrySPOW_Type()
)
entityGatewayEntrySPOW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntrySPOW.setStatus("current")


class _EntityGatewayEntryNGWENR_Type(DisplayString):
    """Custom type entityGatewayEntryNGWENR based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryNGWENR_Type.__name__ = "DisplayString"
_EntityGatewayEntryNGWENR_Object = MibTableColumn
entityGatewayEntryNGWENR = _EntityGatewayEntryNGWENR_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 11),
    _EntityGatewayEntryNGWENR_Type()
)
entityGatewayEntryNGWENR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryNGWENR.setStatus("current")


class _EntityGatewayEntryUART_Type(DisplayString):
    """Custom type entityGatewayEntryUART based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryUART_Type.__name__ = "DisplayString"
_EntityGatewayEntryUART_Object = MibTableColumn
entityGatewayEntryUART = _EntityGatewayEntryUART_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 12),
    _EntityGatewayEntryUART_Type()
)
entityGatewayEntryUART.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryUART.setStatus("current")


class _EntityGatewayEntryIPRESC_Type(DisplayString):
    """Custom type entityGatewayEntryIPRESC based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryIPRESC_Type.__name__ = "DisplayString"
_EntityGatewayEntryIPRESC_Object = MibTableColumn
entityGatewayEntryIPRESC = _EntityGatewayEntryIPRESC_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 13),
    _EntityGatewayEntryIPRESC_Type()
)
entityGatewayEntryIPRESC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryIPRESC.setStatus("current")


class _EntityGatewayEntryIPMAIN_Type(DisplayString):
    """Custom type entityGatewayEntryIPMAIN based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryIPMAIN_Type.__name__ = "DisplayString"
_EntityGatewayEntryIPMAIN_Object = MibTableColumn
entityGatewayEntryIPMAIN = _EntityGatewayEntryIPMAIN_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 14),
    _EntityGatewayEntryIPMAIN_Type()
)
entityGatewayEntryIPMAIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryIPMAIN.setStatus("current")


class _EntityGatewayEntryTALK_Type(DisplayString):
    """Custom type entityGatewayEntryTALK based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryTALK_Type.__name__ = "DisplayString"
_EntityGatewayEntryTALK_Object = MibTableColumn
entityGatewayEntryTALK = _EntityGatewayEntryTALK_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 15),
    _EntityGatewayEntryTALK_Type()
)
entityGatewayEntryTALK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryTALK.setStatus("current")


class _EntityGatewayEntryDSP_Type(DisplayString):
    """Custom type entityGatewayEntryDSP based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_EntityGatewayEntryDSP_Type.__name__ = "DisplayString"
_EntityGatewayEntryDSP_Object = MibTableColumn
entityGatewayEntryDSP = _EntityGatewayEntryDSP_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 16),
    _EntityGatewayEntryDSP_Type()
)
entityGatewayEntryDSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryDSP.setStatus("current")


class _EntityGatewayEntryUptime_Type(DisplayString):
    """Custom type entityGatewayEntryUptime based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EntityGatewayEntryUptime_Type.__name__ = "DisplayString"
_EntityGatewayEntryUptime_Object = MibTableColumn
entityGatewayEntryUptime = _EntityGatewayEntryUptime_Object(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 4, 1, 1, 17),
    _EntityGatewayEntryUptime_Type()
)
entityGatewayEntryUptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entityGatewayEntryUptime.setStatus("current")
_SapexEntitiesMIBConformance_ObjectIdentity = ObjectIdentity
sapexEntitiesMIBConformance = _SapexEntitiesMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 5)
)

# Managed Objects groups

sapexEntitiesMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 5, 2)
)
sapexEntitiesMIBGroup.setObjects(
      *(("SAPEX-ENTITIES-MIB", "entityAsteriskEntryType"),
        ("SAPEX-ENTITIES-MIB", "entityAsteriskEntryName"),
        ("SAPEX-ENTITIES-MIB", "entityAsteriskEntryVal"),
        ("SAPEX-ENTITIES-MIB", "entityAsteriskEntryAddress"),
        ("SAPEX-ENTITIES-MIB", "entityAsteriskEntryUptime"),
        ("SAPEX-ENTITIES-MIB", "entityGCMEntryType"),
        ("SAPEX-ENTITIES-MIB", "entityGCMEntryName"),
        ("SAPEX-ENTITIES-MIB", "entityGCMEntryId"),
        ("SAPEX-ENTITIES-MIB", "entityGCMEntryMajor"),
        ("SAPEX-ENTITIES-MIB", "entityGCMEntryMinor"),
        ("SAPEX-ENTITIES-MIB", "entityGCMEntryDelayed"),
        ("SAPEX-ENTITIES-MIB", "entityGCMEntryGCAR"),
        ("SAPEX-ENTITIES-MIB", "entityGCMEntryGCAA"),
        ("SAPEX-ENTITIES-MIB", "entityGCMEntryUptime"),
        ("SAPEX-ENTITIES-MIB", "entityPEEntryType"),
        ("SAPEX-ENTITIES-MIB", "entityPEEntryName"),
        ("SAPEX-ENTITIES-MIB", "entityPEEntryId"),
        ("SAPEX-ENTITIES-MIB", "entityPEEntryED137"),
        ("SAPEX-ENTITIES-MIB", "entityPEEntrySIP"),
        ("SAPEX-ENTITIES-MIB", "entityPEEntryUptime"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryType"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryName"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryId"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryED137"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntrySIP"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryIPB"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryIP"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryTEMP"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryMPOW"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntrySPOW"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryNGWENR"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryUART"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryIPRESC"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryIPMAIN"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryTALK"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryDSP"),
        ("SAPEX-ENTITIES-MIB", "entityGatewayEntryUptime"))
)
if mibBuilder.loadTexts:
    sapexEntitiesMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sapexEntitiesMIBCopliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28855, 1, 2, 1, 5, 1)
)
sapexEntitiesMIBCopliance.setObjects(
    ("SAPEX-ENTITIES-MIB", "sapexEntitiesMIBGroup")
)
if mibBuilder.loadTexts:
    sapexEntitiesMIBCopliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAPEX-ENTITIES-MIB",
    **{"prescom": prescom,
       "systems": systems,
       "mxs": mxs,
       "newGvr": newGvr,
       "sapexEntities": sapexEntities,
       "entityAsteriskNotification": entityAsteriskNotification,
       "entityAsteriskTable": entityAsteriskTable,
       "entityAsteriskEntry": entityAsteriskEntry,
       "entityAsteriskEntryType": entityAsteriskEntryType,
       "entityAsteriskEntryName": entityAsteriskEntryName,
       "entityAsteriskEntryVal": entityAsteriskEntryVal,
       "entityAsteriskEntryAddress": entityAsteriskEntryAddress,
       "entityAsteriskEntryUptime": entityAsteriskEntryUptime,
       "entityGCMNotification": entityGCMNotification,
       "entityGCMTable": entityGCMTable,
       "entityGCMEntry": entityGCMEntry,
       "entityGCMEntryType": entityGCMEntryType,
       "entityGCMEntryName": entityGCMEntryName,
       "entityGCMEntryId": entityGCMEntryId,
       "entityGCMEntryMajor": entityGCMEntryMajor,
       "entityGCMEntryMinor": entityGCMEntryMinor,
       "entityGCMEntryDelayed": entityGCMEntryDelayed,
       "entityGCMEntryGCAR": entityGCMEntryGCAR,
       "entityGCMEntryGCAA": entityGCMEntryGCAA,
       "entityGCMEntryUptime": entityGCMEntryUptime,
       "entityPENotification": entityPENotification,
       "entityPETable": entityPETable,
       "entityPEEntry": entityPEEntry,
       "entityPEEntryType": entityPEEntryType,
       "entityPEEntryName": entityPEEntryName,
       "entityPEEntryId": entityPEEntryId,
       "entityPEEntryED137": entityPEEntryED137,
       "entityPEEntrySIP": entityPEEntrySIP,
       "entityPEEntryUptime": entityPEEntryUptime,
       "entityGatewayNotification": entityGatewayNotification,
       "entityGatewayTable": entityGatewayTable,
       "entityGatewayEntry": entityGatewayEntry,
       "entityGatewayEntryType": entityGatewayEntryType,
       "entityGatewayEntryName": entityGatewayEntryName,
       "entityGatewayEntryId": entityGatewayEntryId,
       "entityGatewayEntryED137": entityGatewayEntryED137,
       "entityGatewayEntrySIP": entityGatewayEntrySIP,
       "entityGatewayEntryIPB": entityGatewayEntryIPB,
       "entityGatewayEntryIP": entityGatewayEntryIP,
       "entityGatewayEntryTEMP": entityGatewayEntryTEMP,
       "entityGatewayEntryMPOW": entityGatewayEntryMPOW,
       "entityGatewayEntrySPOW": entityGatewayEntrySPOW,
       "entityGatewayEntryNGWENR": entityGatewayEntryNGWENR,
       "entityGatewayEntryUART": entityGatewayEntryUART,
       "entityGatewayEntryIPRESC": entityGatewayEntryIPRESC,
       "entityGatewayEntryIPMAIN": entityGatewayEntryIPMAIN,
       "entityGatewayEntryTALK": entityGatewayEntryTALK,
       "entityGatewayEntryDSP": entityGatewayEntryDSP,
       "entityGatewayEntryUptime": entityGatewayEntryUptime,
       "sapexEntitiesMIBConformance": sapexEntitiesMIBConformance,
       "sapexEntitiesMIBCopliance": sapexEntitiesMIBCopliance,
       "sapexEntitiesMIBGroup": sapexEntitiesMIBGroup}
)
