# SNMP MIB module (F3-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/F3-BFD-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:57 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(bfdSessEntry,
 bfdSessIndex) = mibBuilder.importSymbols(
    "BFD-STD-MIB",
    "bfdSessEntry",
    "bfdSessIndex")

(AdminState,
 OperationalState,
 SecondaryState,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "OperationalState",
    "SecondaryState",
    "VlanId",
    "VlanPriority")

(f3L3TrafficIPInterfaceEntry,) = mibBuilder.importSymbols(
    "F3-L3-MIB",
    "f3L3TrafficIPInterfaceEntry")

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
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3BfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38)
)
if mibBuilder.loadTexts:
    f3BfdMIB.setRevisions(
        ("2015-08-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BfdSessPerfAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("clearCtrlPkts", 1))
    )



# MIB Managed Objects in the order of their OIDs

_F3BfdConfigObjects_ObjectIdentity = ObjectIdentity
f3BfdConfigObjects = _F3BfdConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1)
)
_BfdSessExtTable_Object = MibTable
bfdSessExtTable = _BfdSessExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1)
)
if mibBuilder.loadTexts:
    bfdSessExtTable.setStatus("current")
_BfdSessExtEntry_Object = MibTableRow
bfdSessExtEntry = _BfdSessExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bfdSessExtEntry.setStatus("current")
_BfdSessExtInnerVlanControl_Type = TruthValue
_BfdSessExtInnerVlanControl_Object = MibTableColumn
bfdSessExtInnerVlanControl = _BfdSessExtInnerVlanControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 1),
    _BfdSessExtInnerVlanControl_Type()
)
bfdSessExtInnerVlanControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtInnerVlanControl.setStatus("current")
_BfdSessExtInnerVlanId_Type = VlanId
_BfdSessExtInnerVlanId_Object = MibTableColumn
bfdSessExtInnerVlanId = _BfdSessExtInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 2),
    _BfdSessExtInnerVlanId_Type()
)
bfdSessExtInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtInnerVlanId.setStatus("current")
_BfdSessExtInnerVlanPri_Type = VlanPriority
_BfdSessExtInnerVlanPri_Object = MibTableColumn
bfdSessExtInnerVlanPri = _BfdSessExtInnerVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 3),
    _BfdSessExtInnerVlanPri_Type()
)
bfdSessExtInnerVlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtInnerVlanPri.setStatus("current")
_BfdSessExtOuterVlanControl_Type = TruthValue
_BfdSessExtOuterVlanControl_Object = MibTableColumn
bfdSessExtOuterVlanControl = _BfdSessExtOuterVlanControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 4),
    _BfdSessExtOuterVlanControl_Type()
)
bfdSessExtOuterVlanControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtOuterVlanControl.setStatus("current")
_BfdSessExtOuterVlanId_Type = VlanId
_BfdSessExtOuterVlanId_Object = MibTableColumn
bfdSessExtOuterVlanId = _BfdSessExtOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 5),
    _BfdSessExtOuterVlanId_Type()
)
bfdSessExtOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtOuterVlanId.setStatus("current")
_BfdSessExtOuterVlanPri_Type = VlanPriority
_BfdSessExtOuterVlanPri_Object = MibTableColumn
bfdSessExtOuterVlanPri = _BfdSessExtOuterVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 6),
    _BfdSessExtOuterVlanPri_Type()
)
bfdSessExtOuterVlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtOuterVlanPri.setStatus("current")
_BfdSessExtIpPri_Type = Unsigned32
_BfdSessExtIpPri_Object = MibTableColumn
bfdSessExtIpPri = _BfdSessExtIpPri_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 7),
    _BfdSessExtIpPri_Type()
)
bfdSessExtIpPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtIpPri.setStatus("current")
_BfdSessExtIpGateway_Type = IpAddress
_BfdSessExtIpGateway_Object = MibTableColumn
bfdSessExtIpGateway = _BfdSessExtIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 8),
    _BfdSessExtIpGateway_Type()
)
bfdSessExtIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtIpGateway.setStatus("current")
_BfdSessExtAdminState_Type = AdminState
_BfdSessExtAdminState_Object = MibTableColumn
bfdSessExtAdminState = _BfdSessExtAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 9),
    _BfdSessExtAdminState_Type()
)
bfdSessExtAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtAdminState.setStatus("current")
_BfdSessExtOperationalState_Type = OperationalState
_BfdSessExtOperationalState_Object = MibTableColumn
bfdSessExtOperationalState = _BfdSessExtOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 10),
    _BfdSessExtOperationalState_Type()
)
bfdSessExtOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessExtOperationalState.setStatus("current")
_BfdSessExtSecondaryState_Type = SecondaryState
_BfdSessExtSecondaryState_Object = MibTableColumn
bfdSessExtSecondaryState = _BfdSessExtSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 11),
    _BfdSessExtSecondaryState_Type()
)
bfdSessExtSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessExtSecondaryState.setStatus("current")
_BfdSessExtNegRxInterval_Type = Unsigned32
_BfdSessExtNegRxInterval_Object = MibTableColumn
bfdSessExtNegRxInterval = _BfdSessExtNegRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 12),
    _BfdSessExtNegRxInterval_Type()
)
bfdSessExtNegRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdSessExtNegRxInterval.setStatus("current")
_BfdSessExtAlias_Type = DisplayString
_BfdSessExtAlias_Object = MibTableColumn
bfdSessExtAlias = _BfdSessExtAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 13),
    _BfdSessExtAlias_Type()
)
bfdSessExtAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtAlias.setStatus("current")
_BfdSessExtAction_Type = BfdSessPerfAction
_BfdSessExtAction_Object = MibTableColumn
bfdSessExtAction = _BfdSessExtAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 1, 1, 14),
    _BfdSessExtAction_Type()
)
bfdSessExtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bfdSessExtAction.setStatus("current")
_F3BfdIpIfMemberTable_Object = MibTable
f3BfdIpIfMemberTable = _F3BfdIpIfMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 2)
)
if mibBuilder.loadTexts:
    f3BfdIpIfMemberTable.setStatus("current")
_F3BfdIpIfMemberEntry_Object = MibTableRow
f3BfdIpIfMemberEntry = _F3BfdIpIfMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 2, 1)
)
f3BfdIpIfMemberEntry.setIndexNames(
    (0, "BFD-STD-MIB", "bfdSessIndex"),
    (0, "F3-BFD-MIB", "f3BfdIpIfMemberObject"),
)
if mibBuilder.loadTexts:
    f3BfdIpIfMemberEntry.setStatus("current")
_F3BfdIpIfMemberObject_Type = VariablePointer
_F3BfdIpIfMemberObject_Object = MibTableColumn
f3BfdIpIfMemberObject = _F3BfdIpIfMemberObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 2, 1, 1),
    _F3BfdIpIfMemberObject_Type()
)
f3BfdIpIfMemberObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3BfdIpIfMemberObject.setStatus("current")
_F3BfdIpIfMemberStorageType_Type = StorageType
_F3BfdIpIfMemberStorageType_Object = MibTableColumn
f3BfdIpIfMemberStorageType = _F3BfdIpIfMemberStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 2, 1, 2),
    _F3BfdIpIfMemberStorageType_Type()
)
f3BfdIpIfMemberStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3BfdIpIfMemberStorageType.setStatus("current")
_F3BfdIpIfMemberRowStatus_Type = RowStatus
_F3BfdIpIfMemberRowStatus_Object = MibTableColumn
f3BfdIpIfMemberRowStatus = _F3BfdIpIfMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 2, 1, 3),
    _F3BfdIpIfMemberRowStatus_Type()
)
f3BfdIpIfMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3BfdIpIfMemberRowStatus.setStatus("current")
_F3L3TrafficIPInterfaceExtBfdTable_Object = MibTable
f3L3TrafficIPInterfaceExtBfdTable = _F3L3TrafficIPInterfaceExtBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 3)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceExtBfdTable.setStatus("current")
_F3L3TrafficIPInterfaceExtBfdEntry_Object = MibTableRow
f3L3TrafficIPInterfaceExtBfdEntry = _F3L3TrafficIPInterfaceExtBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 3, 1)
)
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceExtBfdEntry.setStatus("current")
_F3L3TrafficIPInterfaceExtBfdObject_Type = VariablePointer
_F3L3TrafficIPInterfaceExtBfdObject_Object = MibTableColumn
f3L3TrafficIPInterfaceExtBfdObject = _F3L3TrafficIPInterfaceExtBfdObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 1, 3, 1, 1),
    _F3L3TrafficIPInterfaceExtBfdObject_Type()
)
f3L3TrafficIPInterfaceExtBfdObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3L3TrafficIPInterfaceExtBfdObject.setStatus("current")
_F3BfdConformance_ObjectIdentity = ObjectIdentity
f3BfdConformance = _F3BfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 2)
)
_F3BfdCompliances_ObjectIdentity = ObjectIdentity
f3BfdCompliances = _F3BfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 2, 1)
)
_F3BfdGroups_ObjectIdentity = ObjectIdentity
f3BfdGroups = _F3BfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 2, 2)
)
bfdSessEntry.registerAugmentions(
    ("F3-BFD-MIB",
     "bfdSessExtEntry")
)
bfdSessExtEntry.setIndexNames(*bfdSessEntry.getIndexNames())
f3L3TrafficIPInterfaceEntry.registerAugmentions(
    ("F3-BFD-MIB",
     "f3L3TrafficIPInterfaceExtBfdEntry")
)
f3L3TrafficIPInterfaceExtBfdEntry.setIndexNames(*f3L3TrafficIPInterfaceEntry.getIndexNames())

# Managed Objects groups

f3BfdConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 2, 2, 1)
)
f3BfdConfigGroup.setObjects(
      *(("F3-BFD-MIB", "bfdSessExtInnerVlanControl"),
        ("F3-BFD-MIB", "bfdSessExtInnerVlanId"),
        ("F3-BFD-MIB", "bfdSessExtInnerVlanPri"),
        ("F3-BFD-MIB", "bfdSessExtOuterVlanControl"),
        ("F3-BFD-MIB", "bfdSessExtOuterVlanId"),
        ("F3-BFD-MIB", "bfdSessExtOuterVlanPri"),
        ("F3-BFD-MIB", "bfdSessExtIpPri"),
        ("F3-BFD-MIB", "bfdSessExtIpGateway"),
        ("F3-BFD-MIB", "bfdSessExtAdminState"),
        ("F3-BFD-MIB", "bfdSessExtOperationalState"),
        ("F3-BFD-MIB", "bfdSessExtSecondaryState"),
        ("F3-BFD-MIB", "bfdSessExtNegRxInterval"),
        ("F3-BFD-MIB", "bfdSessExtAlias"),
        ("F3-BFD-MIB", "bfdSessExtAction"),
        ("F3-BFD-MIB", "f3BfdIpIfMemberObject"),
        ("F3-BFD-MIB", "f3BfdIpIfMemberStorageType"),
        ("F3-BFD-MIB", "f3BfdIpIfMemberRowStatus"),
        ("F3-BFD-MIB", "f3L3TrafficIPInterfaceExtBfdObject"))
)
if mibBuilder.loadTexts:
    f3BfdConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3BfdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 38, 2, 1, 1)
)
f3BfdCompliance.setObjects(
    ("F3-BFD-MIB", "f3BfdConfigGroup")
)
if mibBuilder.loadTexts:
    f3BfdCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-BFD-MIB",
    **{"BfdSessPerfAction": BfdSessPerfAction,
       "f3BfdMIB": f3BfdMIB,
       "f3BfdConfigObjects": f3BfdConfigObjects,
       "bfdSessExtTable": bfdSessExtTable,
       "bfdSessExtEntry": bfdSessExtEntry,
       "bfdSessExtInnerVlanControl": bfdSessExtInnerVlanControl,
       "bfdSessExtInnerVlanId": bfdSessExtInnerVlanId,
       "bfdSessExtInnerVlanPri": bfdSessExtInnerVlanPri,
       "bfdSessExtOuterVlanControl": bfdSessExtOuterVlanControl,
       "bfdSessExtOuterVlanId": bfdSessExtOuterVlanId,
       "bfdSessExtOuterVlanPri": bfdSessExtOuterVlanPri,
       "bfdSessExtIpPri": bfdSessExtIpPri,
       "bfdSessExtIpGateway": bfdSessExtIpGateway,
       "bfdSessExtAdminState": bfdSessExtAdminState,
       "bfdSessExtOperationalState": bfdSessExtOperationalState,
       "bfdSessExtSecondaryState": bfdSessExtSecondaryState,
       "bfdSessExtNegRxInterval": bfdSessExtNegRxInterval,
       "bfdSessExtAlias": bfdSessExtAlias,
       "bfdSessExtAction": bfdSessExtAction,
       "f3BfdIpIfMemberTable": f3BfdIpIfMemberTable,
       "f3BfdIpIfMemberEntry": f3BfdIpIfMemberEntry,
       "f3BfdIpIfMemberObject": f3BfdIpIfMemberObject,
       "f3BfdIpIfMemberStorageType": f3BfdIpIfMemberStorageType,
       "f3BfdIpIfMemberRowStatus": f3BfdIpIfMemberRowStatus,
       "f3L3TrafficIPInterfaceExtBfdTable": f3L3TrafficIPInterfaceExtBfdTable,
       "f3L3TrafficIPInterfaceExtBfdEntry": f3L3TrafficIPInterfaceExtBfdEntry,
       "f3L3TrafficIPInterfaceExtBfdObject": f3L3TrafficIPInterfaceExtBfdObject,
       "f3BfdConformance": f3BfdConformance,
       "f3BfdCompliances": f3BfdCompliances,
       "f3BfdCompliance": f3BfdCompliance,
       "f3BfdGroups": f3BfdGroups,
       "f3BfdConfigGroup": f3BfdConfigGroup}
)
