# SNMP MIB module (TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:37:32 2025
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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TDirection,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TDirection",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxOperState")


# MODULE-IDENTITY

timetraRouteNextHopTemplateMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 90)
)
if mibBuilder.loadTexts:
    timetraRouteNextHopTemplateMIBModule.setRevisions(
        ("2014-01-01 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxRouteNHVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("admin", 0),
          ("oper", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxRouteNHConformance_ObjectIdentity = ObjectIdentity
tmnxRouteNHConformance = _TmnxRouteNHConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 90)
)
_TmnxRouteNHCompliances_ObjectIdentity = ObjectIdentity
tmnxRouteNHCompliances = _TmnxRouteNHCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 90, 1)
)
_TmnxRouteNHGroups_ObjectIdentity = ObjectIdentity
tmnxRouteNHGroups = _TmnxRouteNHGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 90, 2)
)
_TmnxRouteNHNotifGroups_ObjectIdentity = ObjectIdentity
tmnxRouteNHNotifGroups = _TmnxRouteNHNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 90, 3)
)
_TmnxRouteNextHop_ObjectIdentity = ObjectIdentity
tmnxRouteNextHop = _TmnxRouteNextHop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90)
)
_TmnxRouteNextHopObjs_ObjectIdentity = ObjectIdentity
tmnxRouteNextHopObjs = _TmnxRouteNextHopObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1)
)
_TmnxRouteNHAdminControl_ObjectIdentity = ObjectIdentity
tmnxRouteNHAdminControl = _TmnxRouteNHAdminControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 1)
)
_TmnxRouteNHAdminLastChangeTime_Type = TimeStamp
_TmnxRouteNHAdminLastChangeTime_Object = MibScalar
tmnxRouteNHAdminLastChangeTime = _TmnxRouteNHAdminLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 1, 1),
    _TmnxRouteNHAdminLastChangeTime_Type()
)
tmnxRouteNHAdminLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRouteNHAdminLastChangeTime.setStatus("current")


class _TmnxRouteNHAdminOwner_Type(TNamedItemOrEmpty):
    """Custom type tmnxRouteNHAdminOwner based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxRouteNHAdminOwner_Type.__name__ = "TNamedItemOrEmpty"
_TmnxRouteNHAdminOwner_Object = MibScalar
tmnxRouteNHAdminOwner = _TmnxRouteNHAdminOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 1, 2),
    _TmnxRouteNHAdminOwner_Type()
)
tmnxRouteNHAdminOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRouteNHAdminOwner.setStatus("current")


class _TmnxRouteNHAdminControlApply_Type(Integer32):
    """Custom type tmnxRouteNHAdminControlApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("initialize", 2),
          ("commit", 3))
    )


_TmnxRouteNHAdminControlApply_Type.__name__ = "Integer32"
_TmnxRouteNHAdminControlApply_Object = MibScalar
tmnxRouteNHAdminControlApply = _TmnxRouteNHAdminControlApply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 1, 3),
    _TmnxRouteNHAdminControlApply_Type()
)
tmnxRouteNHAdminControlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxRouteNHAdminControlApply.setStatus("current")
_TmnxRouteNHTemplateTblLastCh_Type = TimeStamp
_TmnxRouteNHTemplateTblLastCh_Object = MibScalar
tmnxRouteNHTemplateTblLastCh = _TmnxRouteNHTemplateTblLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 3),
    _TmnxRouteNHTemplateTblLastCh_Type()
)
tmnxRouteNHTemplateTblLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplateTblLastCh.setStatus("current")
_TmnxRouteNHTemplateTable_Object = MibTable
tmnxRouteNHTemplateTable = _TmnxRouteNHTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxRouteNHTemplateTable.setStatus("current")
_TmnxRouteNHTemplateEntry_Object = MibTableRow
tmnxRouteNHTemplateEntry = _TmnxRouteNHTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 4, 1)
)
tmnxRouteNHTemplateEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplateVersion"),
    (0, "TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplateName"),
)
if mibBuilder.loadTexts:
    tmnxRouteNHTemplateEntry.setStatus("current")
_TmnxRouteNHTemplateVersion_Type = TmnxRouteNHVersion
_TmnxRouteNHTemplateVersion_Object = MibTableColumn
tmnxRouteNHTemplateVersion = _TmnxRouteNHTemplateVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 4, 1, 1),
    _TmnxRouteNHTemplateVersion_Type()
)
tmnxRouteNHTemplateVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplateVersion.setStatus("current")
_TmnxRouteNHTemplateName_Type = TNamedItem
_TmnxRouteNHTemplateName_Object = MibTableColumn
tmnxRouteNHTemplateName = _TmnxRouteNHTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 4, 1, 2),
    _TmnxRouteNHTemplateName_Type()
)
tmnxRouteNHTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplateName.setStatus("current")
_TmnxRouteNHTemplateRowStatus_Type = RowStatus
_TmnxRouteNHTemplateRowStatus_Object = MibTableColumn
tmnxRouteNHTemplateRowStatus = _TmnxRouteNHTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 4, 1, 3),
    _TmnxRouteNHTemplateRowStatus_Type()
)
tmnxRouteNHTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplateRowStatus.setStatus("current")
_TmnxRouteNHTemplateRowLstChng_Type = TimeStamp
_TmnxRouteNHTemplateRowLstChng_Object = MibTableColumn
tmnxRouteNHTemplateRowLstChng = _TmnxRouteNHTemplateRowLstChng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 4, 1, 4),
    _TmnxRouteNHTemplateRowLstChng_Type()
)
tmnxRouteNHTemplateRowLstChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplateRowLstChng.setStatus("current")


class _TmnxRouteNHTemplateDescription_Type(TItemDescription):
    """Custom type tmnxRouteNHTemplateDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxRouteNHTemplateDescription_Type.__name__ = "TItemDescription"
_TmnxRouteNHTemplateDescription_Object = MibTableColumn
tmnxRouteNHTemplateDescription = _TmnxRouteNHTemplateDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 4, 1, 5),
    _TmnxRouteNHTemplateDescription_Type()
)
tmnxRouteNHTemplateDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplateDescription.setStatus("current")


class _TmnxRouteNHTemplateSrlgEnable_Type(TruthValue):
    """Custom type tmnxRouteNHTemplateSrlgEnable based on TruthValue"""
    defaultValue = 2


_TmnxRouteNHTemplateSrlgEnable_Type.__name__ = "TruthValue"
_TmnxRouteNHTemplateSrlgEnable_Object = MibTableColumn
tmnxRouteNHTemplateSrlgEnable = _TmnxRouteNHTemplateSrlgEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 4, 1, 6),
    _TmnxRouteNHTemplateSrlgEnable_Type()
)
tmnxRouteNHTemplateSrlgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplateSrlgEnable.setStatus("current")


class _TmnxRouteNHTemplProtectionType_Type(Integer32):
    """Custom type tmnxRouteNHTemplProtectionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("node", 2))
    )


_TmnxRouteNHTemplProtectionType_Type.__name__ = "Integer32"
_TmnxRouteNHTemplProtectionType_Object = MibTableColumn
tmnxRouteNHTemplProtectionType = _TmnxRouteNHTemplProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 4, 1, 7),
    _TmnxRouteNHTemplProtectionType_Type()
)
tmnxRouteNHTemplProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplProtectionType.setStatus("current")


class _TmnxRouteNHTemplateNextHopType_Type(Integer32):
    """Custom type tmnxRouteNHTemplateNextHopType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("tunnel", 2))
    )


_TmnxRouteNHTemplateNextHopType_Type.__name__ = "Integer32"
_TmnxRouteNHTemplateNextHopType_Object = MibTableColumn
tmnxRouteNHTemplateNextHopType = _TmnxRouteNHTemplateNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 4, 1, 8),
    _TmnxRouteNHTemplateNextHopType_Type()
)
tmnxRouteNHTemplateNextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplateNextHopType.setStatus("current")
_TmnxRouteNHTemplAdminGrpTblLstCh_Type = TimeStamp
_TmnxRouteNHTemplAdminGrpTblLstCh_Object = MibScalar
tmnxRouteNHTemplAdminGrpTblLstCh = _TmnxRouteNHTemplAdminGrpTblLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 5),
    _TmnxRouteNHTemplAdminGrpTblLstCh_Type()
)
tmnxRouteNHTemplAdminGrpTblLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplAdminGrpTblLstCh.setStatus("current")
_TmnxRouteNHTemplAdminGrpTable_Object = MibTable
tmnxRouteNHTemplAdminGrpTable = _TmnxRouteNHTemplAdminGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxRouteNHTemplAdminGrpTable.setStatus("current")
_TmnxRouteNHTemplAdminGrpEntry_Object = MibTableRow
tmnxRouteNHTemplAdminGrpEntry = _TmnxRouteNHTemplAdminGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 6, 1)
)
tmnxRouteNHTemplAdminGrpEntry.setIndexNames(
    (0, "TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplateVersion"),
    (0, "TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplateName"),
    (0, "TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplAdminGrpType"),
    (0, "TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplAdminGrpName"),
)
if mibBuilder.loadTexts:
    tmnxRouteNHTemplAdminGrpEntry.setStatus("current")


class _TmnxRouteNHTemplAdminGrpType_Type(Integer32):
    """Custom type tmnxRouteNHTemplAdminGrpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_TmnxRouteNHTemplAdminGrpType_Type.__name__ = "Integer32"
_TmnxRouteNHTemplAdminGrpType_Object = MibTableColumn
tmnxRouteNHTemplAdminGrpType = _TmnxRouteNHTemplAdminGrpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 6, 1, 1),
    _TmnxRouteNHTemplAdminGrpType_Type()
)
tmnxRouteNHTemplAdminGrpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplAdminGrpType.setStatus("current")
_TmnxRouteNHTemplAdminGrpName_Type = TNamedItem
_TmnxRouteNHTemplAdminGrpName_Object = MibTableColumn
tmnxRouteNHTemplAdminGrpName = _TmnxRouteNHTemplAdminGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 6, 1, 2),
    _TmnxRouteNHTemplAdminGrpName_Type()
)
tmnxRouteNHTemplAdminGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplAdminGrpName.setStatus("current")
_TmnxRouteNHTemplAdmGrpRowStatus_Type = RowStatus
_TmnxRouteNHTemplAdmGrpRowStatus_Object = MibTableColumn
tmnxRouteNHTemplAdmGrpRowStatus = _TmnxRouteNHTemplAdmGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 6, 1, 3),
    _TmnxRouteNHTemplAdmGrpRowStatus_Type()
)
tmnxRouteNHTemplAdmGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplAdmGrpRowStatus.setStatus("current")
_TmnxRouteNHTemplAdmGrpRowLstCh_Type = TimeStamp
_TmnxRouteNHTemplAdmGrpRowLstCh_Object = MibTableColumn
tmnxRouteNHTemplAdmGrpRowLstCh = _TmnxRouteNHTemplAdmGrpRowLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 6, 1, 4),
    _TmnxRouteNHTemplAdmGrpRowLstCh_Type()
)
tmnxRouteNHTemplAdmGrpRowLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplAdmGrpRowLstCh.setStatus("current")


class _TmnxRouteNHTemplAdminGrpPref_Type(Integer32):
    """Custom type tmnxRouteNHTemplAdminGrpPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxRouteNHTemplAdminGrpPref_Type.__name__ = "Integer32"
_TmnxRouteNHTemplAdminGrpPref_Object = MibTableColumn
tmnxRouteNHTemplAdminGrpPref = _TmnxRouteNHTemplAdminGrpPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 1, 6, 1, 5),
    _TmnxRouteNHTemplAdminGrpPref_Type()
)
tmnxRouteNHTemplAdminGrpPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxRouteNHTemplAdminGrpPref.setStatus("current")
_TmnxRouteNHNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxRouteNHNotificationObjs = _TmnxRouteNHNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 90, 2)
)
_TmnxRouteNHNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxRouteNHNotifyPrefix = _TmnxRouteNHNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 90)
)
_TmnxRouteNHNotifications_ObjectIdentity = ObjectIdentity
tmnxRouteNHNotifications = _TmnxRouteNHNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 90, 0)
)

# Managed Objects groups

tmnxRouteNextHopTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 90, 2, 1)
)
tmnxRouteNextHopTemplateGroup.setObjects(
      *(("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHAdminLastChangeTime"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHAdminOwner"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHAdminControlApply"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplateTblLastCh"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplateRowStatus"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplateRowLstChng"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplateDescription"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplateSrlgEnable"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplProtectionType"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplateNextHopType"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplAdminGrpTblLstCh"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplAdmGrpRowStatus"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplAdmGrpRowLstCh"),
        ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNHTemplAdminGrpPref"))
)
if mibBuilder.loadTexts:
    tmnxRouteNextHopTemplateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxRouteNextHopCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 90, 1, 1)
)
tmnxRouteNextHopCompliance.setObjects(
    ("TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB", "tmnxRouteNextHopTemplateGroup")
)
if mibBuilder.loadTexts:
    tmnxRouteNextHopCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-ROUTE-NEXT-HOP-TEMPLATE-MIB",
    **{"TmnxRouteNHVersion": TmnxRouteNHVersion,
       "timetraRouteNextHopTemplateMIBModule": timetraRouteNextHopTemplateMIBModule,
       "tmnxRouteNHConformance": tmnxRouteNHConformance,
       "tmnxRouteNHCompliances": tmnxRouteNHCompliances,
       "tmnxRouteNextHopCompliance": tmnxRouteNextHopCompliance,
       "tmnxRouteNHGroups": tmnxRouteNHGroups,
       "tmnxRouteNextHopTemplateGroup": tmnxRouteNextHopTemplateGroup,
       "tmnxRouteNHNotifGroups": tmnxRouteNHNotifGroups,
       "tmnxRouteNextHop": tmnxRouteNextHop,
       "tmnxRouteNextHopObjs": tmnxRouteNextHopObjs,
       "tmnxRouteNHAdminControl": tmnxRouteNHAdminControl,
       "tmnxRouteNHAdminLastChangeTime": tmnxRouteNHAdminLastChangeTime,
       "tmnxRouteNHAdminOwner": tmnxRouteNHAdminOwner,
       "tmnxRouteNHAdminControlApply": tmnxRouteNHAdminControlApply,
       "tmnxRouteNHTemplateTblLastCh": tmnxRouteNHTemplateTblLastCh,
       "tmnxRouteNHTemplateTable": tmnxRouteNHTemplateTable,
       "tmnxRouteNHTemplateEntry": tmnxRouteNHTemplateEntry,
       "tmnxRouteNHTemplateVersion": tmnxRouteNHTemplateVersion,
       "tmnxRouteNHTemplateName": tmnxRouteNHTemplateName,
       "tmnxRouteNHTemplateRowStatus": tmnxRouteNHTemplateRowStatus,
       "tmnxRouteNHTemplateRowLstChng": tmnxRouteNHTemplateRowLstChng,
       "tmnxRouteNHTemplateDescription": tmnxRouteNHTemplateDescription,
       "tmnxRouteNHTemplateSrlgEnable": tmnxRouteNHTemplateSrlgEnable,
       "tmnxRouteNHTemplProtectionType": tmnxRouteNHTemplProtectionType,
       "tmnxRouteNHTemplateNextHopType": tmnxRouteNHTemplateNextHopType,
       "tmnxRouteNHTemplAdminGrpTblLstCh": tmnxRouteNHTemplAdminGrpTblLstCh,
       "tmnxRouteNHTemplAdminGrpTable": tmnxRouteNHTemplAdminGrpTable,
       "tmnxRouteNHTemplAdminGrpEntry": tmnxRouteNHTemplAdminGrpEntry,
       "tmnxRouteNHTemplAdminGrpType": tmnxRouteNHTemplAdminGrpType,
       "tmnxRouteNHTemplAdminGrpName": tmnxRouteNHTemplAdminGrpName,
       "tmnxRouteNHTemplAdmGrpRowStatus": tmnxRouteNHTemplAdmGrpRowStatus,
       "tmnxRouteNHTemplAdmGrpRowLstCh": tmnxRouteNHTemplAdmGrpRowLstCh,
       "tmnxRouteNHTemplAdminGrpPref": tmnxRouteNHTemplAdminGrpPref,
       "tmnxRouteNHNotificationObjs": tmnxRouteNHNotificationObjs,
       "tmnxRouteNHNotifyPrefix": tmnxRouteNHNotifyPrefix,
       "tmnxRouteNHNotifications": tmnxRouteNHNotifications}
)
