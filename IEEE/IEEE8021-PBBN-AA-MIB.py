# SNMP MIB module (IEEE8021-PBBN-AA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/IEEE/IEEE8021-PBBN-AA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:12:28 2025
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021PbbnAutoAttachMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 37)
)
if mibBuilder.loadTexts:
    ieee8021PbbnAutoAttachMib.setRevisions(
        ("2023-09-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021AaNotifications_ObjectIdentity = ObjectIdentity
ieee8021AaNotifications = _Ieee8021AaNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 37, 0)
)
_Ieee8021AaObjects_ObjectIdentity = ObjectIdentity
ieee8021AaObjects = _Ieee8021AaObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 37, 1)
)
_Ieee8021AaConfig_ObjectIdentity = ObjectIdentity
ieee8021AaConfig = _Ieee8021AaConfig_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1)
)


class _Ieee8021AaSystemEnable_Type(Integer32):
    """Custom type ieee8021AaSystemEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Ieee8021AaSystemEnable_Type.__name__ = "Integer32"
_Ieee8021AaSystemEnable_Object = MibScalar
ieee8021AaSystemEnable = _Ieee8021AaSystemEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 1),
    _Ieee8021AaSystemEnable_Type()
)
ieee8021AaSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AaSystemEnable.setStatus("current")


class _Ieee8021AaSystemType_Type(Integer32):
    """Custom type ieee8021AaSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aaBeb", 1),
          ("aaDeviceVlanAware", 2),
          ("aaDeviceVlanUnaware", 3))
    )


_Ieee8021AaSystemType_Type.__name__ = "Integer32"
_Ieee8021AaSystemType_Object = MibScalar
ieee8021AaSystemType = _Ieee8021AaSystemType_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 2),
    _Ieee8021AaSystemType_Type()
)
ieee8021AaSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaSystemType.setStatus("current")
_Ieee8021AaSystemMAC_Type = MacAddress
_Ieee8021AaSystemMAC_Object = MibScalar
ieee8021AaSystemMAC = _Ieee8021AaSystemMAC_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 3),
    _Ieee8021AaSystemMAC_Type()
)
ieee8021AaSystemMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaSystemMAC.setStatus("current")


class _Ieee8021AaSystemResetTime_Type(Integer32):
    """Custom type ieee8021AaSystemResetTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_Ieee8021AaSystemResetTime_Type.__name__ = "Integer32"
_Ieee8021AaSystemResetTime_Object = MibScalar
ieee8021AaSystemResetTime = _Ieee8021AaSystemResetTime_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 4),
    _Ieee8021AaSystemResetTime_Type()
)
ieee8021AaSystemResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AaSystemResetTime.setStatus("current")
_Ieee8021AaVidIsidAsgnsTable_Object = MibTable
ieee8021AaVidIsidAsgnsTable = _Ieee8021AaVidIsidAsgnsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021AaVidIsidAsgnsTable.setStatus("current")
_Ieee8021AaVidIsidAsgnsEntry_Object = MibTableRow
ieee8021AaVidIsidAsgnsEntry = _Ieee8021AaVidIsidAsgnsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 5, 1)
)
ieee8021AaVidIsidAsgnsEntry.setIndexNames(
    (0, "IEEE8021-PBBN-AA-MIB", "ieee8021AaVidIsidAsgnsIfIndex"),
    (0, "IEEE8021-PBBN-AA-MIB", "ieee8021AaVidIsidAsgnsIsid"),
    (0, "IEEE8021-PBBN-AA-MIB", "ieee8021AaVidIsidAsgnsVid"),
)
if mibBuilder.loadTexts:
    ieee8021AaVidIsidAsgnsEntry.setStatus("current")


class _Ieee8021AaVidIsidAsgnsIfIndex_Type(Integer32):
    """Custom type ieee8021AaVidIsidAsgnsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AaVidIsidAsgnsIfIndex_Type.__name__ = "Integer32"
_Ieee8021AaVidIsidAsgnsIfIndex_Object = MibTableColumn
ieee8021AaVidIsidAsgnsIfIndex = _Ieee8021AaVidIsidAsgnsIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 5, 1, 1),
    _Ieee8021AaVidIsidAsgnsIfIndex_Type()
)
ieee8021AaVidIsidAsgnsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AaVidIsidAsgnsIfIndex.setStatus("current")


class _Ieee8021AaVidIsidAsgnsIsid_Type(Integer32):
    """Custom type ieee8021AaVidIsidAsgnsIsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1256, 16777214),
    )


_Ieee8021AaVidIsidAsgnsIsid_Type.__name__ = "Integer32"
_Ieee8021AaVidIsidAsgnsIsid_Object = MibTableColumn
ieee8021AaVidIsidAsgnsIsid = _Ieee8021AaVidIsidAsgnsIsid_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 5, 1, 2),
    _Ieee8021AaVidIsidAsgnsIsid_Type()
)
ieee8021AaVidIsidAsgnsIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AaVidIsidAsgnsIsid.setStatus("current")


class _Ieee8021AaVidIsidAsgnsVid_Type(Integer32):
    """Custom type ieee8021AaVidIsidAsgnsVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Ieee8021AaVidIsidAsgnsVid_Type.__name__ = "Integer32"
_Ieee8021AaVidIsidAsgnsVid_Object = MibTableColumn
ieee8021AaVidIsidAsgnsVid = _Ieee8021AaVidIsidAsgnsVid_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 5, 1, 3),
    _Ieee8021AaVidIsidAsgnsVid_Type()
)
ieee8021AaVidIsidAsgnsVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AaVidIsidAsgnsVid.setStatus("current")


class _Ieee8021AaVidIsidAsgnsStatus_Type(Integer32):
    """Custom type ieee8021AaVidIsidAsgnsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("pending", 1),
          ("accepted", 2),
          ("rejected", 3),
          ("rejectedAutoAttachResourcesUnavailable", 4),
          ("rejectedInvalidVLANID", 5),
          ("rejectedVLANResourcesUnavailable", 6),
          ("rejectedInvalidISID", 7),
          ("rejectedISIDResourcesUnavailable", 8),
          ("rejectedApplicationInteractionIssue", 9),
          ("rejectedAssignmentNotAllowed", 10))
    )


_Ieee8021AaVidIsidAsgnsStatus_Type.__name__ = "Integer32"
_Ieee8021AaVidIsidAsgnsStatus_Object = MibTableColumn
ieee8021AaVidIsidAsgnsStatus = _Ieee8021AaVidIsidAsgnsStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 5, 1, 4),
    _Ieee8021AaVidIsidAsgnsStatus_Type()
)
ieee8021AaVidIsidAsgnsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaVidIsidAsgnsStatus.setStatus("current")
_Ieee8021AaVidIsidAsgnsRowStatus_Type = RowStatus
_Ieee8021AaVidIsidAsgnsRowStatus_Object = MibTableColumn
ieee8021AaVidIsidAsgnsRowStatus = _Ieee8021AaVidIsidAsgnsRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 5, 1, 5),
    _Ieee8021AaVidIsidAsgnsRowStatus_Type()
)
ieee8021AaVidIsidAsgnsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021AaVidIsidAsgnsRowStatus.setStatus("current")
_Ieee8021AaPortTable_Object = MibTable
ieee8021AaPortTable = _Ieee8021AaPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021AaPortTable.setStatus("current")
_Ieee8021AaPortEntry_Object = MibTableRow
ieee8021AaPortEntry = _Ieee8021AaPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 6, 1)
)
ieee8021AaPortEntry.setIndexNames(
    (0, "IEEE8021-PBBN-AA-MIB", "ieee8021AaPortIfIndex"),
    (0, "IEEE8021-PBBN-AA-MIB", "ieee8021AaPortNetId"),
)
if mibBuilder.loadTexts:
    ieee8021AaPortEntry.setStatus("current")


class _Ieee8021AaPortIfIndex_Type(Integer32):
    """Custom type ieee8021AaPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AaPortIfIndex_Type.__name__ = "Integer32"
_Ieee8021AaPortIfIndex_Object = MibTableColumn
ieee8021AaPortIfIndex = _Ieee8021AaPortIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 6, 1, 1),
    _Ieee8021AaPortIfIndex_Type()
)
ieee8021AaPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AaPortIfIndex.setStatus("current")


class _Ieee8021AaPortNetId_Type(OctetString):
    """Custom type ieee8021AaPortNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Ieee8021AaPortNetId_Type.__name__ = "OctetString"
_Ieee8021AaPortNetId_Object = MibTableColumn
ieee8021AaPortNetId = _Ieee8021AaPortNetId_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 6, 1, 2),
    _Ieee8021AaPortNetId_Type()
)
ieee8021AaPortNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaPortNetId.setStatus("current")


class _Ieee8021AaPortEnable_Type(Integer32):
    """Custom type ieee8021AaPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Ieee8021AaPortEnable_Type.__name__ = "Integer32"
_Ieee8021AaPortEnable_Object = MibTableColumn
ieee8021AaPortEnable = _Ieee8021AaPortEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 6, 1, 3),
    _Ieee8021AaPortEnable_Type()
)
ieee8021AaPortEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021AaPortEnable.setStatus("current")
_Ieee8021AaPortRowStatus_Type = RowStatus
_Ieee8021AaPortRowStatus_Object = MibTableColumn
ieee8021AaPortRowStatus = _Ieee8021AaPortRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 6, 1, 4),
    _Ieee8021AaPortRowStatus_Type()
)
ieee8021AaPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021AaPortRowStatus.setStatus("current")
_Ieee8021AaDiscSystemsTable_Object = MibTable
ieee8021AaDiscSystemsTable = _Ieee8021AaDiscSystemsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ieee8021AaDiscSystemsTable.setStatus("current")
_Ieee8021AaDiscSystemsEntry_Object = MibTableRow
ieee8021AaDiscSystemsEntry = _Ieee8021AaDiscSystemsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 7, 1)
)
ieee8021AaDiscSystemsEntry.setIndexNames(
    (0, "IEEE8021-PBBN-AA-MIB", "ieee8021AaDiscLocPortIfIndex"),
    (0, "IEEE8021-PBBN-AA-MIB", "ieee8021AaDiscRemPortNetId"),
)
if mibBuilder.loadTexts:
    ieee8021AaDiscSystemsEntry.setStatus("current")


class _Ieee8021AaDiscLocPortIfIndex_Type(Integer32):
    """Custom type ieee8021AaDiscLocPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AaDiscLocPortIfIndex_Type.__name__ = "Integer32"
_Ieee8021AaDiscLocPortIfIndex_Object = MibTableColumn
ieee8021AaDiscLocPortIfIndex = _Ieee8021AaDiscLocPortIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 7, 1, 1),
    _Ieee8021AaDiscLocPortIfIndex_Type()
)
ieee8021AaDiscLocPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AaDiscLocPortIfIndex.setStatus("current")


class _Ieee8021AaDiscRemSystemType_Type(Integer32):
    """Custom type ieee8021AaDiscRemSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aaBeb", 1),
          ("aaDeviceCVlanAware", 2),
          ("aaDeviceVlanUnaware", 3),
          ("aaDeviceSVlanAware", 4))
    )


_Ieee8021AaDiscRemSystemType_Type.__name__ = "Integer32"
_Ieee8021AaDiscRemSystemType_Object = MibTableColumn
ieee8021AaDiscRemSystemType = _Ieee8021AaDiscRemSystemType_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 7, 1, 2),
    _Ieee8021AaDiscRemSystemType_Type()
)
ieee8021AaDiscRemSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaDiscRemSystemType.setStatus("current")


class _Ieee8021AaDiscRemPortNetId_Type(OctetString):
    """Custom type ieee8021AaDiscRemPortNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Ieee8021AaDiscRemPortNetId_Type.__name__ = "OctetString"
_Ieee8021AaDiscRemPortNetId_Object = MibTableColumn
ieee8021AaDiscRemPortNetId = _Ieee8021AaDiscRemPortNetId_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 7, 1, 3),
    _Ieee8021AaDiscRemPortNetId_Type()
)
ieee8021AaDiscRemPortNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaDiscRemPortNetId.setStatus("current")


class _Ieee8021AaDiscRemPortTagging_Type(Bits):
    """Custom type ieee8021AaDiscRemPortTagging based on Bits"""
    namedValues = NamedValues(
        *(("trafficTagged", 0),
          ("trafficTaggedAndUntagged", 1),
          ("trafficUntaggedOnly", 2))
    )

_Ieee8021AaDiscRemPortTagging_Type.__name__ = "Bits"
_Ieee8021AaDiscRemPortTagging_Object = MibTableColumn
ieee8021AaDiscRemPortTagging = _Ieee8021AaDiscRemPortTagging_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 7, 1, 4),
    _Ieee8021AaDiscRemPortTagging_Type()
)
ieee8021AaDiscRemPortTagging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaDiscRemPortTagging.setStatus("current")


class _Ieee8021AaDiscRemPortAssocState_Type(Integer32):
    """Custom type ieee8021AaDiscRemPortAssocState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              18,
              19,
              34,
              35,
              50,
              66)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 0),
          ("readyToAssoc", 1),
          ("readyToAttach", 2),
          ("assocAttached", 3),
          ("assocFailTypes", 18),
          ("assocStandby", 19),
          ("assocFailTags", 34),
          ("assocInvalid", 35),
          ("assocFailTopo", 50),
          ("assocFailOther", 66))
    )


_Ieee8021AaDiscRemPortAssocState_Type.__name__ = "Integer32"
_Ieee8021AaDiscRemPortAssocState_Object = MibTableColumn
ieee8021AaDiscRemPortAssocState = _Ieee8021AaDiscRemPortAssocState_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 7, 1, 5),
    _Ieee8021AaDiscRemPortAssocState_Type()
)
ieee8021AaDiscRemPortAssocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaDiscRemPortAssocState.setStatus("current")


class _Ieee8021AaDiscLocPortAssocState_Type(Integer32):
    """Custom type ieee8021AaDiscLocPortAssocState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              18,
              19,
              34,
              35,
              50,
              66)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 0),
          ("readyToAssoc", 1),
          ("readyToAttach", 2),
          ("assocAttached", 3),
          ("assocFailTypes", 18),
          ("assocStandby", 19),
          ("assocFailTags", 34),
          ("assocInvalid", 35),
          ("assocFailTopo", 50),
          ("assocFailOther", 66))
    )


_Ieee8021AaDiscLocPortAssocState_Type.__name__ = "Integer32"
_Ieee8021AaDiscLocPortAssocState_Object = MibTableColumn
ieee8021AaDiscLocPortAssocState = _Ieee8021AaDiscLocPortAssocState_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 1, 7, 1, 6),
    _Ieee8021AaDiscLocPortAssocState_Type()
)
ieee8021AaDiscLocPortAssocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaDiscLocPortAssocState.setStatus("current")
_Ieee8021AaStats_ObjectIdentity = ObjectIdentity
ieee8021AaStats = _Ieee8021AaStats_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2)
)
_Ieee8021AaStatsTable_Object = MibTable
ieee8021AaStatsTable = _Ieee8021AaStatsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021AaStatsTable.setStatus("current")
_Ieee8021AaStatsEntry_Object = MibTableRow
ieee8021AaStatsEntry = _Ieee8021AaStatsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1, 1)
)
ieee8021AaStatsEntry.setIndexNames(
    (0, "IEEE8021-PBBN-AA-MIB", "ieee8021AaStatsPortIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021AaStatsEntry.setStatus("current")


class _Ieee8021AaStatsPortIfIndex_Type(Integer32):
    """Custom type ieee8021AaStatsPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021AaStatsPortIfIndex_Type.__name__ = "Integer32"
_Ieee8021AaStatsPortIfIndex_Object = MibTableColumn
ieee8021AaStatsPortIfIndex = _Ieee8021AaStatsPortIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1, 1, 1),
    _Ieee8021AaStatsPortIfIndex_Type()
)
ieee8021AaStatsPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021AaStatsPortIfIndex.setStatus("current")
_Ieee8021AaStatsAssocAttached_Type = Counter32
_Ieee8021AaStatsAssocAttached_Object = MibTableColumn
ieee8021AaStatsAssocAttached = _Ieee8021AaStatsAssocAttached_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1, 1, 2),
    _Ieee8021AaStatsAssocAttached_Type()
)
ieee8021AaStatsAssocAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaStatsAssocAttached.setStatus("current")
_Ieee8021AaStatsAsgnsRequested_Type = Counter32
_Ieee8021AaStatsAsgnsRequested_Object = MibTableColumn
ieee8021AaStatsAsgnsRequested = _Ieee8021AaStatsAsgnsRequested_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1, 1, 3),
    _Ieee8021AaStatsAsgnsRequested_Type()
)
ieee8021AaStatsAsgnsRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaStatsAsgnsRequested.setStatus("current")
_Ieee8021AaStatsAsgnsAccepted_Type = Counter32
_Ieee8021AaStatsAsgnsAccepted_Object = MibTableColumn
ieee8021AaStatsAsgnsAccepted = _Ieee8021AaStatsAsgnsAccepted_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1, 1, 4),
    _Ieee8021AaStatsAsgnsAccepted_Type()
)
ieee8021AaStatsAsgnsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaStatsAsgnsAccepted.setStatus("current")
_Ieee8021AaStatsAsgnRejected_Type = Counter32
_Ieee8021AaStatsAsgnRejected_Object = MibTableColumn
ieee8021AaStatsAsgnRejected = _Ieee8021AaStatsAsgnRejected_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1, 1, 5),
    _Ieee8021AaStatsAsgnRejected_Type()
)
ieee8021AaStatsAsgnRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaStatsAsgnRejected.setStatus("current")
_Ieee8021AaStatsAssocFailed_Type = Counter32
_Ieee8021AaStatsAssocFailed_Object = MibTableColumn
ieee8021AaStatsAssocFailed = _Ieee8021AaStatsAssocFailed_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1, 1, 6),
    _Ieee8021AaStatsAssocFailed_Type()
)
ieee8021AaStatsAssocFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaStatsAssocFailed.setStatus("current")
_Ieee8021AaStatsAsgnsWithdrawn_Type = Counter32
_Ieee8021AaStatsAsgnsWithdrawn_Object = MibTableColumn
ieee8021AaStatsAsgnsWithdrawn = _Ieee8021AaStatsAsgnsWithdrawn_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1, 1, 7),
    _Ieee8021AaStatsAsgnsWithdrawn_Type()
)
ieee8021AaStatsAsgnsWithdrawn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaStatsAsgnsWithdrawn.setStatus("current")
_Ieee8021AaStatsAssocReset_Type = Counter32
_Ieee8021AaStatsAssocReset_Object = MibTableColumn
ieee8021AaStatsAssocReset = _Ieee8021AaStatsAssocReset_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1, 1, 8),
    _Ieee8021AaStatsAssocReset_Type()
)
ieee8021AaStatsAssocReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaStatsAssocReset.setStatus("current")
_Ieee8021AaStatsAssocStandby_Type = Counter32
_Ieee8021AaStatsAssocStandby_Object = MibTableColumn
ieee8021AaStatsAssocStandby = _Ieee8021AaStatsAssocStandby_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 1, 2, 1, 1, 9),
    _Ieee8021AaStatsAssocStandby_Type()
)
ieee8021AaStatsAssocStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021AaStatsAssocStandby.setStatus("current")
_Ieee8021AaNotifyObjects_ObjectIdentity = ObjectIdentity
ieee8021AaNotifyObjects = _Ieee8021AaNotifyObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 37, 2)
)


class _Ieee8021AaDiscSystemsDescr_Type(SnmpAdminString):
    """Custom type ieee8021AaDiscSystemsDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ieee8021AaDiscSystemsDescr_Type.__name__ = "SnmpAdminString"
_Ieee8021AaDiscSystemsDescr_Object = MibScalar
ieee8021AaDiscSystemsDescr = _Ieee8021AaDiscSystemsDescr_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 2, 1),
    _Ieee8021AaDiscSystemsDescr_Type()
)
ieee8021AaDiscSystemsDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ieee8021AaDiscSystemsDescr.setStatus("current")
_Ieee8021AaDiscSystemsMgmtOid_Type = ObjectIdentifier
_Ieee8021AaDiscSystemsMgmtOid_Object = MibScalar
ieee8021AaDiscSystemsMgmtOid = _Ieee8021AaDiscSystemsMgmtOid_Object(
    (1, 3, 111, 2, 802, 1, 1, 37, 2, 2),
    _Ieee8021AaDiscSystemsMgmtOid_Type()
)
ieee8021AaDiscSystemsMgmtOid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ieee8021AaDiscSystemsMgmtOid.setStatus("current")
_Ieee8021AaConformance_ObjectIdentity = ObjectIdentity
ieee8021AaConformance = _Ieee8021AaConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 37, 4)
)
_Ieee8021AaCompliances_ObjectIdentity = ObjectIdentity
ieee8021AaCompliances = _Ieee8021AaCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 37, 4, 1)
)
_Ieee8021AaGroups_ObjectIdentity = ObjectIdentity
ieee8021AaGroups = _Ieee8021AaGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 37, 4, 2)
)

# Managed Objects groups

ieee8021AaGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 37, 4, 2, 1)
)
ieee8021AaGroup.setObjects(
      *(("IEEE8021-PBBN-AA-MIB", "ieee8021AaSystemEnable"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaSystemType"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaSystemMAC"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaVidIsidAsgnsStatus"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaVidIsidAsgnsRowStatus"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaPortNetId"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaPortEnable"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaDiscRemPortNetId"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaStatsAssocAttached"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaStatsAsgnsRequested"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaStatsAsgnsAccepted"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaStatsAsgnRejected"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaDiscSystemsDescr"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaDiscSystemsMgmtOid"))
)
if mibBuilder.loadTexts:
    ieee8021AaGroup.setStatus("current")


# Notification objects

ieee8021AaDiscoveredSystem = NotificationType(
    (1, 3, 111, 2, 802, 1, 1, 37, 0, 1)
)
ieee8021AaDiscoveredSystem.setObjects(
      *(("IEEE8021-PBBN-AA-MIB", "ieee8021AaDiscRemSystemType"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaDiscRemPortNetId"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaDiscSystemsDescr"),
        ("IEEE8021-PBBN-AA-MIB", "ieee8021AaDiscSystemsMgmtOid"))
)
if mibBuilder.loadTexts:
    ieee8021AaDiscoveredSystem.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021AaCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 37, 4, 1, 1)
)
ieee8021AaCompliance.setObjects(
    ("IEEE8021-PBBN-AA-MIB", "ieee8021AaGroup")
)
if mibBuilder.loadTexts:
    ieee8021AaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-PBBN-AA-MIB",
    **{"ieee8021PbbnAutoAttachMib": ieee8021PbbnAutoAttachMib,
       "ieee8021AaNotifications": ieee8021AaNotifications,
       "ieee8021AaDiscoveredSystem": ieee8021AaDiscoveredSystem,
       "ieee8021AaObjects": ieee8021AaObjects,
       "ieee8021AaConfig": ieee8021AaConfig,
       "ieee8021AaSystemEnable": ieee8021AaSystemEnable,
       "ieee8021AaSystemType": ieee8021AaSystemType,
       "ieee8021AaSystemMAC": ieee8021AaSystemMAC,
       "ieee8021AaSystemResetTime": ieee8021AaSystemResetTime,
       "ieee8021AaVidIsidAsgnsTable": ieee8021AaVidIsidAsgnsTable,
       "ieee8021AaVidIsidAsgnsEntry": ieee8021AaVidIsidAsgnsEntry,
       "ieee8021AaVidIsidAsgnsIfIndex": ieee8021AaVidIsidAsgnsIfIndex,
       "ieee8021AaVidIsidAsgnsIsid": ieee8021AaVidIsidAsgnsIsid,
       "ieee8021AaVidIsidAsgnsVid": ieee8021AaVidIsidAsgnsVid,
       "ieee8021AaVidIsidAsgnsStatus": ieee8021AaVidIsidAsgnsStatus,
       "ieee8021AaVidIsidAsgnsRowStatus": ieee8021AaVidIsidAsgnsRowStatus,
       "ieee8021AaPortTable": ieee8021AaPortTable,
       "ieee8021AaPortEntry": ieee8021AaPortEntry,
       "ieee8021AaPortIfIndex": ieee8021AaPortIfIndex,
       "ieee8021AaPortNetId": ieee8021AaPortNetId,
       "ieee8021AaPortEnable": ieee8021AaPortEnable,
       "ieee8021AaPortRowStatus": ieee8021AaPortRowStatus,
       "ieee8021AaDiscSystemsTable": ieee8021AaDiscSystemsTable,
       "ieee8021AaDiscSystemsEntry": ieee8021AaDiscSystemsEntry,
       "ieee8021AaDiscLocPortIfIndex": ieee8021AaDiscLocPortIfIndex,
       "ieee8021AaDiscRemSystemType": ieee8021AaDiscRemSystemType,
       "ieee8021AaDiscRemPortNetId": ieee8021AaDiscRemPortNetId,
       "ieee8021AaDiscRemPortTagging": ieee8021AaDiscRemPortTagging,
       "ieee8021AaDiscRemPortAssocState": ieee8021AaDiscRemPortAssocState,
       "ieee8021AaDiscLocPortAssocState": ieee8021AaDiscLocPortAssocState,
       "ieee8021AaStats": ieee8021AaStats,
       "ieee8021AaStatsTable": ieee8021AaStatsTable,
       "ieee8021AaStatsEntry": ieee8021AaStatsEntry,
       "ieee8021AaStatsPortIfIndex": ieee8021AaStatsPortIfIndex,
       "ieee8021AaStatsAssocAttached": ieee8021AaStatsAssocAttached,
       "ieee8021AaStatsAsgnsRequested": ieee8021AaStatsAsgnsRequested,
       "ieee8021AaStatsAsgnsAccepted": ieee8021AaStatsAsgnsAccepted,
       "ieee8021AaStatsAsgnRejected": ieee8021AaStatsAsgnRejected,
       "ieee8021AaStatsAssocFailed": ieee8021AaStatsAssocFailed,
       "ieee8021AaStatsAsgnsWithdrawn": ieee8021AaStatsAsgnsWithdrawn,
       "ieee8021AaStatsAssocReset": ieee8021AaStatsAssocReset,
       "ieee8021AaStatsAssocStandby": ieee8021AaStatsAssocStandby,
       "ieee8021AaNotifyObjects": ieee8021AaNotifyObjects,
       "ieee8021AaDiscSystemsDescr": ieee8021AaDiscSystemsDescr,
       "ieee8021AaDiscSystemsMgmtOid": ieee8021AaDiscSystemsMgmtOid,
       "ieee8021AaConformance": ieee8021AaConformance,
       "ieee8021AaCompliances": ieee8021AaCompliances,
       "ieee8021AaCompliance": ieee8021AaCompliance,
       "ieee8021AaGroups": ieee8021AaGroups,
       "ieee8021AaGroup": ieee8021AaGroup}
)
