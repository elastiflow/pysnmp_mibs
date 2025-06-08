# SNMP MIB module (TIMETRA-SAS-VRTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-SAS-VRTR-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:35:22 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(TMplsLspExpProfMapID,
 TNetworkIngressMeterId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TMplsLspExpProfMapID",
    "TNetworkIngressMeterId")

(vRtrConfEntry,
 vRtrID,
 vRtrIfBfdSessExtLclDisc,
 vRtrIfEntry,
 vRtrIfIndex,
 vRtrMaxRoutesType,
 vRtrStatEntry) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrConfEntry",
    "vRtrID",
    "vRtrIfBfdSessExtLclDisc",
    "vRtrIfEntry",
    "vRtrIfIndex",
    "vRtrMaxRoutesType",
    "vRtrStatEntry")


# MODULE-IDENTITY

timetraSASVRtrMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    timetraSASVRtrMIBModule.setRevisions(
        ("1909-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSASVRtrGroups_ObjectIdentity = ObjectIdentity
tmnxSASVRtrGroups = _TmnxSASVRtrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 11)
)
_TSASVRtrObjects_ObjectIdentity = ObjectIdentity
tSASVRtrObjects = _TSASVRtrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7)
)
_VRtrIfExtnTable_Object = MibTable
vRtrIfExtnTable = _VRtrIfExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    vRtrIfExtnTable.setStatus("current")
_VRtrIfExtnEntry_Object = MibTableRow
vRtrIfExtnEntry = _VRtrIfExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrIfExtnEntry.setStatus("current")


class _VRtrIfAcctPolicyId_Type(Unsigned32):
    """Custom type vRtrIfAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_VRtrIfAcctPolicyId_Type.__name__ = "Unsigned32"
_VRtrIfAcctPolicyId_Object = MibTableColumn
vRtrIfAcctPolicyId = _VRtrIfAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 1, 1, 1),
    _VRtrIfAcctPolicyId_Type()
)
vRtrIfAcctPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfAcctPolicyId.setStatus("current")


class _VRtrIfCollectStats_Type(TruthValue):
    """Custom type vRtrIfCollectStats based on TruthValue"""
    defaultValue = 2


_VRtrIfCollectStats_Type.__name__ = "TruthValue"
_VRtrIfCollectStats_Object = MibTableColumn
vRtrIfCollectStats = _VRtrIfCollectStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 1, 1, 2),
    _VRtrIfCollectStats_Type()
)
vRtrIfCollectStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfCollectStats.setStatus("current")
_VRtrNetIfIngressStatsTable_Object = MibTable
vRtrNetIfIngressStatsTable = _VRtrNetIfIngressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 2)
)
if mibBuilder.loadTexts:
    vRtrNetIfIngressStatsTable.setStatus("current")
_VRtrNetIfIngressStatsEntry_Object = MibTableRow
vRtrNetIfIngressStatsEntry = _VRtrNetIfIngressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 2, 1)
)
vRtrNetIfIngressStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-SAS-VRTR-MIB", "vRtrNetIfIngressMeterIndex"),
)
if mibBuilder.loadTexts:
    vRtrNetIfIngressStatsEntry.setStatus("current")
_VRtrNetIfIngressMeterIndex_Type = TNetworkIngressMeterId
_VRtrNetIfIngressMeterIndex_Object = MibTableColumn
vRtrNetIfIngressMeterIndex = _VRtrNetIfIngressMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 2, 1, 1),
    _VRtrNetIfIngressMeterIndex_Type()
)
vRtrNetIfIngressMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrNetIfIngressMeterIndex.setStatus("current")
_VRtrNetIfIngressFwdInProfPkts_Type = Counter64
_VRtrNetIfIngressFwdInProfPkts_Object = MibTableColumn
vRtrNetIfIngressFwdInProfPkts = _VRtrNetIfIngressFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 2, 1, 2),
    _VRtrNetIfIngressFwdInProfPkts_Type()
)
vRtrNetIfIngressFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrNetIfIngressFwdInProfPkts.setStatus("current")
_VRtrNetIfIngressFwdOutProfPkts_Type = Counter64
_VRtrNetIfIngressFwdOutProfPkts_Object = MibTableColumn
vRtrNetIfIngressFwdOutProfPkts = _VRtrNetIfIngressFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 2, 1, 3),
    _VRtrNetIfIngressFwdOutProfPkts_Type()
)
vRtrNetIfIngressFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrNetIfIngressFwdOutProfPkts.setStatus("current")
_VRtrNetIfIngressFwdInProfOcts_Type = Counter64
_VRtrNetIfIngressFwdInProfOcts_Object = MibTableColumn
vRtrNetIfIngressFwdInProfOcts = _VRtrNetIfIngressFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 2, 1, 4),
    _VRtrNetIfIngressFwdInProfOcts_Type()
)
vRtrNetIfIngressFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrNetIfIngressFwdInProfOcts.setStatus("current")
_VRtrNetIfIngressFwdOutProfOcts_Type = Counter64
_VRtrNetIfIngressFwdOutProfOcts_Object = MibTableColumn
vRtrNetIfIngressFwdOutProfOcts = _VRtrNetIfIngressFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 2, 1, 5),
    _VRtrNetIfIngressFwdOutProfOcts_Type()
)
vRtrNetIfIngressFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrNetIfIngressFwdOutProfOcts.setStatus("current")
_VRtrConfExtnTable_Object = MibTable
vRtrConfExtnTable = _VRtrConfExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 4)
)
if mibBuilder.loadTexts:
    vRtrConfExtnTable.setStatus("current")
_VRtrConfExtnEntry_Object = MibTableRow
vRtrConfExtnEntry = _VRtrConfExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 4, 1)
)
if mibBuilder.loadTexts:
    vRtrConfExtnEntry.setStatus("current")


class _VRtrMaxNumRouteDests_Type(Integer32):
    """Custom type vRtrMaxNumRouteDests based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_VRtrMaxNumRouteDests_Type.__name__ = "Integer32"
_VRtrMaxNumRouteDests_Object = MibTableColumn
vRtrMaxNumRouteDests = _VRtrMaxNumRouteDests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 4, 1, 1),
    _VRtrMaxNumRouteDests_Type()
)
vRtrMaxNumRouteDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMaxNumRouteDests.setStatus("current")
_VRtrStatExtnTable_Object = MibTable
vRtrStatExtnTable = _VRtrStatExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 5)
)
if mibBuilder.loadTexts:
    vRtrStatExtnTable.setStatus("current")
_VRtrStatExtnEntry_Object = MibTableRow
vRtrStatExtnEntry = _VRtrStatExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 5, 1)
)
if mibBuilder.loadTexts:
    vRtrStatExtnEntry.setStatus("current")
_VRtrStatCurrNumRouteDests_Type = Gauge32
_VRtrStatCurrNumRouteDests_Object = MibTableColumn
vRtrStatCurrNumRouteDests = _VRtrStatCurrNumRouteDests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 5, 1, 1),
    _VRtrStatCurrNumRouteDests_Type()
)
vRtrStatCurrNumRouteDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatCurrNumRouteDests.setStatus("current")
_TmnxSASVRtrNotifications_ObjectIdentity = ObjectIdentity
tmnxSASVRtrNotifications = _TmnxSASVRtrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 20)
)
vRtrIfEntry.registerAugmentions(
    ("TIMETRA-SAS-VRTR-MIB",
     "vRtrIfExtnEntry")
)
vRtrIfExtnEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrConfEntry.registerAugmentions(
    ("TIMETRA-SAS-VRTR-MIB",
     "vRtrConfExtnEntry")
)
vRtrConfExtnEntry.setIndexNames(*vRtrConfEntry.getIndexNames())
vRtrStatEntry.registerAugmentions(
    ("TIMETRA-SAS-VRTR-MIB",
     "vRtrStatExtnEntry")
)
vRtrStatExtnEntry.setIndexNames(*vRtrStatEntry.getIndexNames())

# Managed Objects groups

tmnxSASVRtrV1v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 11, 1)
)
tmnxSASVRtrV1v0Group.setObjects(
      *(("TIMETRA-SAS-VRTR-MIB", "vRtrIfAcctPolicyId"),
        ("TIMETRA-SAS-VRTR-MIB", "vRtrIfCollectStats"),
        ("TIMETRA-SAS-VRTR-MIB", "vRtrNetIfIngressFwdInProfPkts"),
        ("TIMETRA-SAS-VRTR-MIB", "vRtrNetIfIngressFwdOutProfPkts"),
        ("TIMETRA-SAS-VRTR-MIB", "vRtrNetIfIngressFwdInProfOcts"),
        ("TIMETRA-SAS-VRTR-MIB", "vRtrNetIfIngressFwdOutProfOcts"),
        ("TIMETRA-SAS-VRTR-MIB", "vRtrMaxNumRouteDests"),
        ("TIMETRA-SAS-VRTR-MIB", "vRtrStatCurrNumRouteDests"))
)
if mibBuilder.loadTexts:
    tmnxSASVRtrV1v0Group.setStatus("current")


# Notification objects

tmnxVRtrMaxRouteDests = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 20, 1)
)
tmnxVRtrMaxRouteDests.setObjects(
      *(("TIMETRA-SAS-VRTR-MIB", "vRtrStatCurrNumRouteDests"),
        ("TIMETRA-SAS-VRTR-MIB", "vRtrMaxNumRouteDests"),
        ("TIMETRA-VRTR-MIB", "vRtrMaxRoutesType"))
)
if mibBuilder.loadTexts:
    tmnxVRtrMaxRouteDests.setStatus(
        "current"
    )

tmnxVRtrBfdNoBfdHashResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 20, 2)
)
tmnxVRtrBfdNoBfdHashResources.setObjects(
    ("TIMETRA-VRTR-MIB", "vRtrIfBfdSessExtLclDisc")
)
if mibBuilder.loadTexts:
    tmnxVRtrBfdNoBfdHashResources.setStatus(
        "current"
    )

tmnxVRtrBfdNoIomHwResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 7, 20, 3)
)
tmnxVRtrBfdNoIomHwResources.setObjects(
    ("TIMETRA-VRTR-MIB", "vRtrIfBfdSessExtLclDisc")
)
if mibBuilder.loadTexts:
    tmnxVRtrBfdNoIomHwResources.setStatus(
        "current"
    )


# Notifications groups

tmnxSASVrtrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 11, 2)
)
tmnxSASVrtrNotificationGroup.setObjects(
    ("TIMETRA-SAS-VRTR-MIB", "tmnxVRtrMaxRouteDests")
)
if mibBuilder.loadTexts:
    tmnxSASVrtrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-VRTR-MIB",
    **{"timetraSASVRtrMIBModule": timetraSASVRtrMIBModule,
       "tmnxSASVRtrGroups": tmnxSASVRtrGroups,
       "tmnxSASVRtrV1v0Group": tmnxSASVRtrV1v0Group,
       "tmnxSASVrtrNotificationGroup": tmnxSASVrtrNotificationGroup,
       "tSASVRtrObjects": tSASVRtrObjects,
       "vRtrIfExtnTable": vRtrIfExtnTable,
       "vRtrIfExtnEntry": vRtrIfExtnEntry,
       "vRtrIfAcctPolicyId": vRtrIfAcctPolicyId,
       "vRtrIfCollectStats": vRtrIfCollectStats,
       "vRtrNetIfIngressStatsTable": vRtrNetIfIngressStatsTable,
       "vRtrNetIfIngressStatsEntry": vRtrNetIfIngressStatsEntry,
       "vRtrNetIfIngressMeterIndex": vRtrNetIfIngressMeterIndex,
       "vRtrNetIfIngressFwdInProfPkts": vRtrNetIfIngressFwdInProfPkts,
       "vRtrNetIfIngressFwdOutProfPkts": vRtrNetIfIngressFwdOutProfPkts,
       "vRtrNetIfIngressFwdInProfOcts": vRtrNetIfIngressFwdInProfOcts,
       "vRtrNetIfIngressFwdOutProfOcts": vRtrNetIfIngressFwdOutProfOcts,
       "vRtrConfExtnTable": vRtrConfExtnTable,
       "vRtrConfExtnEntry": vRtrConfExtnEntry,
       "vRtrMaxNumRouteDests": vRtrMaxNumRouteDests,
       "vRtrStatExtnTable": vRtrStatExtnTable,
       "vRtrStatExtnEntry": vRtrStatExtnEntry,
       "vRtrStatCurrNumRouteDests": vRtrStatCurrNumRouteDests,
       "tmnxSASVRtrNotifications": tmnxSASVRtrNotifications,
       "tmnxVRtrMaxRouteDests": tmnxVRtrMaxRouteDests,
       "tmnxVRtrBfdNoBfdHashResources": tmnxVRtrBfdNoBfdHashResources,
       "tmnxVRtrBfdNoIomHwResources": tmnxVRtrBfdNoIomHwResources}
)
