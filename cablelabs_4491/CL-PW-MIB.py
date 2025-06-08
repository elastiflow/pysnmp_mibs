# SNMP MIB module (CL-PW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CL-PW-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:37:34 2025
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

(TeaPwAttachmentIdentifierType,
 TeaPwCapabilities,
 TeaPwCwStatusTC,
 TeaPwFragSize,
 TeaPwFragStatus,
 TeaPwGroupID,
 TeaPwIDType,
 TeaPwIndexType,
 TeaPwOperStatusTC,
 TeaPwPsnTypeTC,
 TeaPwStatus,
 TeaPwTypeTC) = mibBuilder.importSymbols(
    "CL-PW-TC-MIB",
    "TeaPwAttachmentIdentifierType",
    "TeaPwCapabilities",
    "TeaPwCwStatusTC",
    "TeaPwFragSize",
    "TeaPwFragStatus",
    "TeaPwGroupID",
    "TeaPwIDType",
    "TeaPwIndexType",
    "TeaPwOperStatusTC",
    "TeaPwPsnTypeTC",
    "TeaPwStatus",
    "TeaPwTypeTC")

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfTimeElapsed,
 HCPerfValidIntervals) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfTimeElapsed",
    "HCPerfValidIntervals")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

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
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

teaPwMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15)
)
if mibBuilder.loadTexts:
    teaPwMIB.setRevisions(
        ("2008-02-15 00:00",
         "2006-02-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TeaPwNotifications_ObjectIdentity = ObjectIdentity
teaPwNotifications = _TeaPwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 0)
)
_TeaPwObjects_ObjectIdentity = ObjectIdentity
teaPwObjects = _TeaPwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1)
)
_TeaPwIndexNext_Type = Unsigned32
_TeaPwIndexNext_Object = MibScalar
teaPwIndexNext = _TeaPwIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 1),
    _TeaPwIndexNext_Type()
)
teaPwIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwIndexNext.setStatus("current")
_TeaPwTable_Object = MibTable
teaPwTable = _TeaPwTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    teaPwTable.setStatus("current")
_TeaPwEntry_Object = MibTableRow
teaPwEntry = _TeaPwEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1)
)
teaPwEntry.setIndexNames(
    (0, "CL-PW-MIB", "teaPwIndex"),
)
if mibBuilder.loadTexts:
    teaPwEntry.setStatus("current")
_TeaPwIndex_Type = TeaPwIndexType
_TeaPwIndex_Object = MibTableColumn
teaPwIndex = _TeaPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 1),
    _TeaPwIndex_Type()
)
teaPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwIndex.setStatus("current")
_TeaPwType_Type = TeaPwTypeTC
_TeaPwType_Object = MibTableColumn
teaPwType = _TeaPwType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 2),
    _TeaPwType_Type()
)
teaPwType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwType.setStatus("current")


class _TeaPwOwner_Type(Integer32):
    """Custom type teaPwOwner based on Integer32"""
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
        *(("manual", 1),
          ("pwIdFecSignaling", 2),
          ("genFecSignaling", 3),
          ("l2tpControlProtocol", 4),
          ("other", 5))
    )


_TeaPwOwner_Type.__name__ = "Integer32"
_TeaPwOwner_Object = MibTableColumn
teaPwOwner = _TeaPwOwner_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 3),
    _TeaPwOwner_Type()
)
teaPwOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwOwner.setStatus("current")
_TeaPwPsnType_Type = TeaPwPsnTypeTC
_TeaPwPsnType_Object = MibTableColumn
teaPwPsnType = _TeaPwPsnType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 4),
    _TeaPwPsnType_Type()
)
teaPwPsnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwPsnType.setStatus("current")


class _TeaPwSetUpPriority_Type(Integer32):
    """Custom type teaPwSetUpPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeaPwSetUpPriority_Type.__name__ = "Integer32"
_TeaPwSetUpPriority_Object = MibTableColumn
teaPwSetUpPriority = _TeaPwSetUpPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 5),
    _TeaPwSetUpPriority_Type()
)
teaPwSetUpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwSetUpPriority.setStatus("current")


class _TeaPwHoldingPriority_Type(Integer32):
    """Custom type teaPwHoldingPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeaPwHoldingPriority_Type.__name__ = "Integer32"
_TeaPwHoldingPriority_Object = MibTableColumn
teaPwHoldingPriority = _TeaPwHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 6),
    _TeaPwHoldingPriority_Type()
)
teaPwHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwHoldingPriority.setStatus("current")


class _TeaPwPeerAddrType_Type(InetAddressType):
    """Custom type teaPwPeerAddrType based on InetAddressType"""
    defaultValue = 1


_TeaPwPeerAddrType_Type.__name__ = "InetAddressType"
_TeaPwPeerAddrType_Object = MibTableColumn
teaPwPeerAddrType = _TeaPwPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 8),
    _TeaPwPeerAddrType_Type()
)
teaPwPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwPeerAddrType.setStatus("current")
_TeaPwPeerAddr_Type = InetAddress
_TeaPwPeerAddr_Object = MibTableColumn
teaPwPeerAddr = _TeaPwPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 9),
    _TeaPwPeerAddr_Type()
)
teaPwPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwPeerAddr.setStatus("current")


class _TeaPwAttachedPwIndex_Type(TeaPwIndexType):
    """Custom type teaPwAttachedPwIndex based on TeaPwIndexType"""
    defaultValue = 0


_TeaPwAttachedPwIndex_Type.__name__ = "TeaPwIndexType"
_TeaPwAttachedPwIndex_Object = MibTableColumn
teaPwAttachedPwIndex = _TeaPwAttachedPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 10),
    _TeaPwAttachedPwIndex_Type()
)
teaPwAttachedPwIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwAttachedPwIndex.setStatus("current")


class _TeaPwIfIndex_Type(InterfaceIndexOrZero):
    """Custom type teaPwIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TeaPwIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TeaPwIfIndex_Object = MibTableColumn
teaPwIfIndex = _TeaPwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 11),
    _TeaPwIfIndex_Type()
)
teaPwIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwIfIndex.setStatus("current")
_TeaPwID_Type = TeaPwIDType
_TeaPwID_Object = MibTableColumn
teaPwID = _TeaPwID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 12),
    _TeaPwID_Type()
)
teaPwID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwID.setStatus("current")
_TeaPwLocalGroupID_Type = TeaPwGroupID
_TeaPwLocalGroupID_Object = MibTableColumn
teaPwLocalGroupID = _TeaPwLocalGroupID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 13),
    _TeaPwLocalGroupID_Type()
)
teaPwLocalGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwLocalGroupID.setStatus("current")
_TeaPwGroupAttachmentID_Type = TeaPwAttachmentIdentifierType
_TeaPwGroupAttachmentID_Object = MibTableColumn
teaPwGroupAttachmentID = _TeaPwGroupAttachmentID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 14),
    _TeaPwGroupAttachmentID_Type()
)
teaPwGroupAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwGroupAttachmentID.setStatus("current")
_TeaPwLocalAttachmentID_Type = TeaPwAttachmentIdentifierType
_TeaPwLocalAttachmentID_Object = MibTableColumn
teaPwLocalAttachmentID = _TeaPwLocalAttachmentID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 15),
    _TeaPwLocalAttachmentID_Type()
)
teaPwLocalAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwLocalAttachmentID.setStatus("current")
_TeaPwPeerAttachmentID_Type = TeaPwAttachmentIdentifierType
_TeaPwPeerAttachmentID_Object = MibTableColumn
teaPwPeerAttachmentID = _TeaPwPeerAttachmentID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 16),
    _TeaPwPeerAttachmentID_Type()
)
teaPwPeerAttachmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwPeerAttachmentID.setStatus("current")


class _TeaPwCwPreference_Type(TruthValue):
    """Custom type teaPwCwPreference based on TruthValue"""
    defaultValue = 2


_TeaPwCwPreference_Type.__name__ = "TruthValue"
_TeaPwCwPreference_Object = MibTableColumn
teaPwCwPreference = _TeaPwCwPreference_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 17),
    _TeaPwCwPreference_Type()
)
teaPwCwPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwCwPreference.setStatus("current")


class _TeaPwLocalIfMtu_Type(Unsigned32):
    """Custom type teaPwLocalIfMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TeaPwLocalIfMtu_Type.__name__ = "Unsigned32"
_TeaPwLocalIfMtu_Object = MibTableColumn
teaPwLocalIfMtu = _TeaPwLocalIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 18),
    _TeaPwLocalIfMtu_Type()
)
teaPwLocalIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwLocalIfMtu.setStatus("current")


class _TeaPwLocalIfString_Type(TruthValue):
    """Custom type teaPwLocalIfString based on TruthValue"""
    defaultValue = 2


_TeaPwLocalIfString_Type.__name__ = "TruthValue"
_TeaPwLocalIfString_Object = MibTableColumn
teaPwLocalIfString = _TeaPwLocalIfString_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 19),
    _TeaPwLocalIfString_Type()
)
teaPwLocalIfString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwLocalIfString.setStatus("current")
_TeaPwLocalCapabAdvert_Type = TeaPwCapabilities
_TeaPwLocalCapabAdvert_Object = MibTableColumn
teaPwLocalCapabAdvert = _TeaPwLocalCapabAdvert_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 20),
    _TeaPwLocalCapabAdvert_Type()
)
teaPwLocalCapabAdvert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwLocalCapabAdvert.setStatus("current")
_TeaPwRemoteGroupID_Type = TeaPwGroupID
_TeaPwRemoteGroupID_Object = MibTableColumn
teaPwRemoteGroupID = _TeaPwRemoteGroupID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 21),
    _TeaPwRemoteGroupID_Type()
)
teaPwRemoteGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwRemoteGroupID.setStatus("current")
_TeaPwCwStatus_Type = TeaPwCwStatusTC
_TeaPwCwStatus_Object = MibTableColumn
teaPwCwStatus = _TeaPwCwStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 22),
    _TeaPwCwStatus_Type()
)
teaPwCwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwCwStatus.setStatus("current")
_TeaPwRemoteIfMtu_Type = Unsigned32
_TeaPwRemoteIfMtu_Object = MibTableColumn
teaPwRemoteIfMtu = _TeaPwRemoteIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 23),
    _TeaPwRemoteIfMtu_Type()
)
teaPwRemoteIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwRemoteIfMtu.setStatus("current")


class _TeaPwRemoteIfString_Type(SnmpAdminString):
    """Custom type teaPwRemoteIfString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TeaPwRemoteIfString_Type.__name__ = "SnmpAdminString"
_TeaPwRemoteIfString_Object = MibTableColumn
teaPwRemoteIfString = _TeaPwRemoteIfString_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 24),
    _TeaPwRemoteIfString_Type()
)
teaPwRemoteIfString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwRemoteIfString.setStatus("current")
_TeaPwRemoteCapabilities_Type = TeaPwCapabilities
_TeaPwRemoteCapabilities_Object = MibTableColumn
teaPwRemoteCapabilities = _TeaPwRemoteCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 25),
    _TeaPwRemoteCapabilities_Type()
)
teaPwRemoteCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwRemoteCapabilities.setStatus("current")


class _TeaPwFragmentCfgSize_Type(TeaPwFragSize):
    """Custom type teaPwFragmentCfgSize based on TeaPwFragSize"""
    defaultValue = 0


_TeaPwFragmentCfgSize_Type.__name__ = "TeaPwFragSize"
_TeaPwFragmentCfgSize_Object = MibTableColumn
teaPwFragmentCfgSize = _TeaPwFragmentCfgSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 26),
    _TeaPwFragmentCfgSize_Type()
)
teaPwFragmentCfgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwFragmentCfgSize.setStatus("current")
_TeaPwRmtFragCapability_Type = TeaPwFragStatus
_TeaPwRmtFragCapability_Object = MibTableColumn
teaPwRmtFragCapability = _TeaPwRmtFragCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 27),
    _TeaPwRmtFragCapability_Type()
)
teaPwRmtFragCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwRmtFragCapability.setStatus("current")


class _TeaPwFcsRetentioncfg_Type(Integer32):
    """Custom type teaPwFcsRetentioncfg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcsRetentionDisable", 1),
          ("fcsRetentionEnable", 2))
    )


_TeaPwFcsRetentioncfg_Type.__name__ = "Integer32"
_TeaPwFcsRetentioncfg_Object = MibTableColumn
teaPwFcsRetentioncfg = _TeaPwFcsRetentioncfg_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 28),
    _TeaPwFcsRetentioncfg_Type()
)
teaPwFcsRetentioncfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwFcsRetentioncfg.setStatus("current")


class _TeaPwFcsRetentionStatus_Type(Bits):
    """Custom type teaPwFcsRetentionStatus based on Bits"""
    namedValues = NamedValues(
        *(("remoteIndicationUnknown", 0),
          ("remoteRequestFcsRetention", 1),
          ("fcsRetentionEnabled", 2),
          ("fcsRetentionDisabled", 3),
          ("localFcsRetentionCfgErr", 4),
          ("fcsRetentionFcsSizeMismatch", 5))
    )

_TeaPwFcsRetentionStatus_Type.__name__ = "Bits"
_TeaPwFcsRetentionStatus_Object = MibTableColumn
teaPwFcsRetentionStatus = _TeaPwFcsRetentionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 29),
    _TeaPwFcsRetentionStatus_Type()
)
teaPwFcsRetentionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwFcsRetentionStatus.setStatus("current")
_TeaPwOutboundLabel_Type = Unsigned32
_TeaPwOutboundLabel_Object = MibTableColumn
teaPwOutboundLabel = _TeaPwOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 30),
    _TeaPwOutboundLabel_Type()
)
teaPwOutboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwOutboundLabel.setStatus("current")
_TeaPwInboundLabel_Type = Unsigned32
_TeaPwInboundLabel_Object = MibTableColumn
teaPwInboundLabel = _TeaPwInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 31),
    _TeaPwInboundLabel_Type()
)
teaPwInboundLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwInboundLabel.setStatus("current")
_TeaPwName_Type = SnmpAdminString
_TeaPwName_Object = MibTableColumn
teaPwName = _TeaPwName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 32),
    _TeaPwName_Type()
)
teaPwName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwName.setStatus("current")
_TeaPwDescr_Type = SnmpAdminString
_TeaPwDescr_Object = MibTableColumn
teaPwDescr = _TeaPwDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 33),
    _TeaPwDescr_Type()
)
teaPwDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwDescr.setStatus("current")
_TeaPwCreateTime_Type = TimeStamp
_TeaPwCreateTime_Object = MibTableColumn
teaPwCreateTime = _TeaPwCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 34),
    _TeaPwCreateTime_Type()
)
teaPwCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwCreateTime.setStatus("current")
_TeaPwUpTime_Type = TimeTicks
_TeaPwUpTime_Object = MibTableColumn
teaPwUpTime = _TeaPwUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 35),
    _TeaPwUpTime_Type()
)
teaPwUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwUpTime.setStatus("current")
_TeaPwLastChange_Type = TimeTicks
_TeaPwLastChange_Object = MibTableColumn
teaPwLastChange = _TeaPwLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 36),
    _TeaPwLastChange_Type()
)
teaPwLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwLastChange.setStatus("current")


class _TeaPwAdminStatus_Type(Integer32):
    """Custom type teaPwAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_TeaPwAdminStatus_Type.__name__ = "Integer32"
_TeaPwAdminStatus_Object = MibTableColumn
teaPwAdminStatus = _TeaPwAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 37),
    _TeaPwAdminStatus_Type()
)
teaPwAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwAdminStatus.setStatus("current")
_TeaPwOperStatus_Type = TeaPwOperStatusTC
_TeaPwOperStatus_Object = MibTableColumn
teaPwOperStatus = _TeaPwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 38),
    _TeaPwOperStatus_Type()
)
teaPwOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwOperStatus.setStatus("current")
_TeaPwLocalStatus_Type = TeaPwStatus
_TeaPwLocalStatus_Object = MibTableColumn
teaPwLocalStatus = _TeaPwLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 39),
    _TeaPwLocalStatus_Type()
)
teaPwLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwLocalStatus.setStatus("current")


class _TeaPwRemoteStatusCapable_Type(Integer32):
    """Custom type teaPwRemoteStatusCapable based on Integer32"""
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
        *(("notApplicable", 1),
          ("notYetKnown", 2),
          ("remoteCapable", 3),
          ("remoteNotCapable", 4))
    )


_TeaPwRemoteStatusCapable_Type.__name__ = "Integer32"
_TeaPwRemoteStatusCapable_Object = MibTableColumn
teaPwRemoteStatusCapable = _TeaPwRemoteStatusCapable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 40),
    _TeaPwRemoteStatusCapable_Type()
)
teaPwRemoteStatusCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwRemoteStatusCapable.setStatus("current")
_TeaPwRemoteStatus_Type = TeaPwStatus
_TeaPwRemoteStatus_Object = MibTableColumn
teaPwRemoteStatus = _TeaPwRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 41),
    _TeaPwRemoteStatus_Type()
)
teaPwRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwRemoteStatus.setStatus("current")
_TeaPwTimeElapsed_Type = HCPerfTimeElapsed
_TeaPwTimeElapsed_Object = MibTableColumn
teaPwTimeElapsed = _TeaPwTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 42),
    _TeaPwTimeElapsed_Type()
)
teaPwTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwTimeElapsed.setStatus("current")
_TeaPwValidIntervals_Type = HCPerfValidIntervals
_TeaPwValidIntervals_Object = MibTableColumn
teaPwValidIntervals = _TeaPwValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 43),
    _TeaPwValidIntervals_Type()
)
teaPwValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwValidIntervals.setStatus("current")
_TeaPwRowStatus_Type = RowStatus
_TeaPwRowStatus_Object = MibTableColumn
teaPwRowStatus = _TeaPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 44),
    _TeaPwRowStatus_Type()
)
teaPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwRowStatus.setStatus("current")
_TeaPwStorageType_Type = StorageType
_TeaPwStorageType_Object = MibTableColumn
teaPwStorageType = _TeaPwStorageType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 2, 1, 45),
    _TeaPwStorageType_Type()
)
teaPwStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    teaPwStorageType.setStatus("current")
_TeaPwPerfCurrentTable_Object = MibTable
teaPwPerfCurrentTable = _TeaPwPerfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 3)
)
if mibBuilder.loadTexts:
    teaPwPerfCurrentTable.setStatus("current")
_TeaPwPerfCurrentEntry_Object = MibTableRow
teaPwPerfCurrentEntry = _TeaPwPerfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 3, 1)
)
teaPwPerfCurrentEntry.setIndexNames(
    (0, "CL-PW-MIB", "teaPwIndex"),
)
if mibBuilder.loadTexts:
    teaPwPerfCurrentEntry.setStatus("current")
_TeaPwPerfCurrentInHCPackets_Type = HCPerfCurrentCount
_TeaPwPerfCurrentInHCPackets_Object = MibTableColumn
teaPwPerfCurrentInHCPackets = _TeaPwPerfCurrentInHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 3, 1, 1),
    _TeaPwPerfCurrentInHCPackets_Type()
)
teaPwPerfCurrentInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfCurrentInHCPackets.setStatus("current")
_TeaPwPerfCurrentInHCBytes_Type = HCPerfCurrentCount
_TeaPwPerfCurrentInHCBytes_Object = MibTableColumn
teaPwPerfCurrentInHCBytes = _TeaPwPerfCurrentInHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 3, 1, 2),
    _TeaPwPerfCurrentInHCBytes_Type()
)
teaPwPerfCurrentInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfCurrentInHCBytes.setStatus("current")
_TeaPwPerfCurrentOutHCPackets_Type = HCPerfCurrentCount
_TeaPwPerfCurrentOutHCPackets_Object = MibTableColumn
teaPwPerfCurrentOutHCPackets = _TeaPwPerfCurrentOutHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 3, 1, 3),
    _TeaPwPerfCurrentOutHCPackets_Type()
)
teaPwPerfCurrentOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfCurrentOutHCPackets.setStatus("current")
_TeaPwPerfCurrentOutHCBytes_Type = HCPerfCurrentCount
_TeaPwPerfCurrentOutHCBytes_Object = MibTableColumn
teaPwPerfCurrentOutHCBytes = _TeaPwPerfCurrentOutHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 3, 1, 4),
    _TeaPwPerfCurrentOutHCBytes_Type()
)
teaPwPerfCurrentOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfCurrentOutHCBytes.setStatus("current")
_TeaPwPerfCurrentInPackets_Type = PerfCurrentCount
_TeaPwPerfCurrentInPackets_Object = MibTableColumn
teaPwPerfCurrentInPackets = _TeaPwPerfCurrentInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 3, 1, 5),
    _TeaPwPerfCurrentInPackets_Type()
)
teaPwPerfCurrentInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfCurrentInPackets.setStatus("current")
_TeaPwPerfCurrentInBytes_Type = PerfCurrentCount
_TeaPwPerfCurrentInBytes_Object = MibTableColumn
teaPwPerfCurrentInBytes = _TeaPwPerfCurrentInBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 3, 1, 6),
    _TeaPwPerfCurrentInBytes_Type()
)
teaPwPerfCurrentInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfCurrentInBytes.setStatus("current")
_TeaPwPerfCurrentOutPackets_Type = PerfCurrentCount
_TeaPwPerfCurrentOutPackets_Object = MibTableColumn
teaPwPerfCurrentOutPackets = _TeaPwPerfCurrentOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 3, 1, 7),
    _TeaPwPerfCurrentOutPackets_Type()
)
teaPwPerfCurrentOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfCurrentOutPackets.setStatus("current")
_TeaPwPerfCurrentOutBytes_Type = PerfCurrentCount
_TeaPwPerfCurrentOutBytes_Object = MibTableColumn
teaPwPerfCurrentOutBytes = _TeaPwPerfCurrentOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 3, 1, 8),
    _TeaPwPerfCurrentOutBytes_Type()
)
teaPwPerfCurrentOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfCurrentOutBytes.setStatus("current")
_TeaPwPerfIntervalTable_Object = MibTable
teaPwPerfIntervalTable = _TeaPwPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4)
)
if mibBuilder.loadTexts:
    teaPwPerfIntervalTable.setStatus("current")
_TeaPwPerfIntervalEntry_Object = MibTableRow
teaPwPerfIntervalEntry = _TeaPwPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1)
)
teaPwPerfIntervalEntry.setIndexNames(
    (0, "CL-PW-MIB", "teaPwIndex"),
    (0, "CL-PW-MIB", "teaPwPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    teaPwPerfIntervalEntry.setStatus("current")


class _TeaPwPerfIntervalNumber_Type(Integer32):
    """Custom type teaPwPerfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TeaPwPerfIntervalNumber_Type.__name__ = "Integer32"
_TeaPwPerfIntervalNumber_Object = MibTableColumn
teaPwPerfIntervalNumber = _TeaPwPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 1),
    _TeaPwPerfIntervalNumber_Type()
)
teaPwPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwPerfIntervalNumber.setStatus("current")
_TeaPwPerfIntervalValidData_Type = TruthValue
_TeaPwPerfIntervalValidData_Object = MibTableColumn
teaPwPerfIntervalValidData = _TeaPwPerfIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 2),
    _TeaPwPerfIntervalValidData_Type()
)
teaPwPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfIntervalValidData.setStatus("current")
_TeaPwPerfIntervalTimeElapsed_Type = HCPerfTimeElapsed
_TeaPwPerfIntervalTimeElapsed_Object = MibTableColumn
teaPwPerfIntervalTimeElapsed = _TeaPwPerfIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 3),
    _TeaPwPerfIntervalTimeElapsed_Type()
)
teaPwPerfIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfIntervalTimeElapsed.setStatus("current")
_TeaPwPerfIntervalInHCPackets_Type = HCPerfIntervalCount
_TeaPwPerfIntervalInHCPackets_Object = MibTableColumn
teaPwPerfIntervalInHCPackets = _TeaPwPerfIntervalInHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 4),
    _TeaPwPerfIntervalInHCPackets_Type()
)
teaPwPerfIntervalInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfIntervalInHCPackets.setStatus("current")
_TeaPwPerfIntervalInHCBytes_Type = HCPerfIntervalCount
_TeaPwPerfIntervalInHCBytes_Object = MibTableColumn
teaPwPerfIntervalInHCBytes = _TeaPwPerfIntervalInHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 5),
    _TeaPwPerfIntervalInHCBytes_Type()
)
teaPwPerfIntervalInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfIntervalInHCBytes.setStatus("current")
_TeaPwPerfIntervalOutHCPackets_Type = HCPerfIntervalCount
_TeaPwPerfIntervalOutHCPackets_Object = MibTableColumn
teaPwPerfIntervalOutHCPackets = _TeaPwPerfIntervalOutHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 6),
    _TeaPwPerfIntervalOutHCPackets_Type()
)
teaPwPerfIntervalOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfIntervalOutHCPackets.setStatus("current")
_TeaPwPerfIntervalOutHCBytes_Type = HCPerfIntervalCount
_TeaPwPerfIntervalOutHCBytes_Object = MibTableColumn
teaPwPerfIntervalOutHCBytes = _TeaPwPerfIntervalOutHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 7),
    _TeaPwPerfIntervalOutHCBytes_Type()
)
teaPwPerfIntervalOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfIntervalOutHCBytes.setStatus("current")
_TeaPwPerfIntervalInPackets_Type = PerfIntervalCount
_TeaPwPerfIntervalInPackets_Object = MibTableColumn
teaPwPerfIntervalInPackets = _TeaPwPerfIntervalInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 8),
    _TeaPwPerfIntervalInPackets_Type()
)
teaPwPerfIntervalInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfIntervalInPackets.setStatus("current")
_TeaPwPerfIntervalInBytes_Type = PerfIntervalCount
_TeaPwPerfIntervalInBytes_Object = MibTableColumn
teaPwPerfIntervalInBytes = _TeaPwPerfIntervalInBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 9),
    _TeaPwPerfIntervalInBytes_Type()
)
teaPwPerfIntervalInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfIntervalInBytes.setStatus("current")
_TeaPwPerfIntervalOutPackets_Type = PerfIntervalCount
_TeaPwPerfIntervalOutPackets_Object = MibTableColumn
teaPwPerfIntervalOutPackets = _TeaPwPerfIntervalOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 10),
    _TeaPwPerfIntervalOutPackets_Type()
)
teaPwPerfIntervalOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfIntervalOutPackets.setStatus("current")
_TeaPwPerfIntervalOutBytes_Type = PerfIntervalCount
_TeaPwPerfIntervalOutBytes_Object = MibTableColumn
teaPwPerfIntervalOutBytes = _TeaPwPerfIntervalOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 4, 1, 11),
    _TeaPwPerfIntervalOutBytes_Type()
)
teaPwPerfIntervalOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfIntervalOutBytes.setStatus("current")
_TeaPwPerf1DayIntervalTable_Object = MibTable
teaPwPerf1DayIntervalTable = _TeaPwPerf1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 5)
)
if mibBuilder.loadTexts:
    teaPwPerf1DayIntervalTable.setStatus("current")
_TeaPwPerf1DayIntervalEntry_Object = MibTableRow
teaPwPerf1DayIntervalEntry = _TeaPwPerf1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 5, 1)
)
teaPwPerf1DayIntervalEntry.setIndexNames(
    (0, "CL-PW-MIB", "teaPwIndex"),
    (0, "CL-PW-MIB", "teaPwPerf1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    teaPwPerf1DayIntervalEntry.setStatus("current")


class _TeaPwPerf1DayIntervalNumber_Type(Unsigned32):
    """Custom type teaPwPerf1DayIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_TeaPwPerf1DayIntervalNumber_Type.__name__ = "Unsigned32"
_TeaPwPerf1DayIntervalNumber_Object = MibTableColumn
teaPwPerf1DayIntervalNumber = _TeaPwPerf1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 5, 1, 1),
    _TeaPwPerf1DayIntervalNumber_Type()
)
teaPwPerf1DayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwPerf1DayIntervalNumber.setStatus("current")
_TeaPwPerf1DayIntervalValidData_Type = TruthValue
_TeaPwPerf1DayIntervalValidData_Object = MibTableColumn
teaPwPerf1DayIntervalValidData = _TeaPwPerf1DayIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 5, 1, 2),
    _TeaPwPerf1DayIntervalValidData_Type()
)
teaPwPerf1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerf1DayIntervalValidData.setStatus("current")
_TeaPwPerf1DayIntervalMoniSecs_Type = HCPerfTimeElapsed
_TeaPwPerf1DayIntervalMoniSecs_Object = MibTableColumn
teaPwPerf1DayIntervalMoniSecs = _TeaPwPerf1DayIntervalMoniSecs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 5, 1, 3),
    _TeaPwPerf1DayIntervalMoniSecs_Type()
)
teaPwPerf1DayIntervalMoniSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerf1DayIntervalMoniSecs.setStatus("current")
if mibBuilder.loadTexts:
    teaPwPerf1DayIntervalMoniSecs.setUnits("seconds")
_TeaPwPerf1DayIntervalInHCPackets_Type = Counter64
_TeaPwPerf1DayIntervalInHCPackets_Object = MibTableColumn
teaPwPerf1DayIntervalInHCPackets = _TeaPwPerf1DayIntervalInHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 5, 1, 4),
    _TeaPwPerf1DayIntervalInHCPackets_Type()
)
teaPwPerf1DayIntervalInHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerf1DayIntervalInHCPackets.setStatus("current")
_TeaPwPerf1DayIntervalInHCBytes_Type = Counter64
_TeaPwPerf1DayIntervalInHCBytes_Object = MibTableColumn
teaPwPerf1DayIntervalInHCBytes = _TeaPwPerf1DayIntervalInHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 5, 1, 5),
    _TeaPwPerf1DayIntervalInHCBytes_Type()
)
teaPwPerf1DayIntervalInHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerf1DayIntervalInHCBytes.setStatus("current")
_TeaPwPerf1DayIntervalOutHCPackets_Type = Counter64
_TeaPwPerf1DayIntervalOutHCPackets_Object = MibTableColumn
teaPwPerf1DayIntervalOutHCPackets = _TeaPwPerf1DayIntervalOutHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 5, 1, 6),
    _TeaPwPerf1DayIntervalOutHCPackets_Type()
)
teaPwPerf1DayIntervalOutHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerf1DayIntervalOutHCPackets.setStatus("current")
_TeaPwPerf1DayIntervalOutHCBytes_Type = Counter64
_TeaPwPerf1DayIntervalOutHCBytes_Object = MibTableColumn
teaPwPerf1DayIntervalOutHCBytes = _TeaPwPerf1DayIntervalOutHCBytes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 5, 1, 7),
    _TeaPwPerf1DayIntervalOutHCBytes_Type()
)
teaPwPerf1DayIntervalOutHCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerf1DayIntervalOutHCBytes.setStatus("current")
_TeaPwPerfTotalErrorPackets_Type = Counter32
_TeaPwPerfTotalErrorPackets_Object = MibScalar
teaPwPerfTotalErrorPackets = _TeaPwPerfTotalErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 6),
    _TeaPwPerfTotalErrorPackets_Type()
)
teaPwPerfTotalErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPerfTotalErrorPackets.setStatus("current")
_TeaPwIndexMappingTable_Object = MibTable
teaPwIndexMappingTable = _TeaPwIndexMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 7)
)
if mibBuilder.loadTexts:
    teaPwIndexMappingTable.setStatus("current")
_TeaPwIndexMappingEntry_Object = MibTableRow
teaPwIndexMappingEntry = _TeaPwIndexMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 7, 1)
)
teaPwIndexMappingEntry.setIndexNames(
    (0, "CL-PW-MIB", "teaPwIndexMappingPwType"),
    (0, "CL-PW-MIB", "teaPwIndexMappingPwID"),
    (0, "CL-PW-MIB", "teaPwIndexMappingPeerAddrType"),
    (0, "CL-PW-MIB", "teaPwIndexMappingPeerAddr"),
)
if mibBuilder.loadTexts:
    teaPwIndexMappingEntry.setStatus("current")
_TeaPwIndexMappingPwType_Type = TeaPwTypeTC
_TeaPwIndexMappingPwType_Object = MibTableColumn
teaPwIndexMappingPwType = _TeaPwIndexMappingPwType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 7, 1, 1),
    _TeaPwIndexMappingPwType_Type()
)
teaPwIndexMappingPwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwIndexMappingPwType.setStatus("current")
_TeaPwIndexMappingPwID_Type = TeaPwIDType
_TeaPwIndexMappingPwID_Object = MibTableColumn
teaPwIndexMappingPwID = _TeaPwIndexMappingPwID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 7, 1, 2),
    _TeaPwIndexMappingPwID_Type()
)
teaPwIndexMappingPwID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwIndexMappingPwID.setStatus("current")
_TeaPwIndexMappingPeerAddrType_Type = InetAddressType
_TeaPwIndexMappingPeerAddrType_Object = MibTableColumn
teaPwIndexMappingPeerAddrType = _TeaPwIndexMappingPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 7, 1, 3),
    _TeaPwIndexMappingPeerAddrType_Type()
)
teaPwIndexMappingPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwIndexMappingPeerAddrType.setStatus("current")
_TeaPwIndexMappingPeerAddr_Type = InetAddress
_TeaPwIndexMappingPeerAddr_Object = MibTableColumn
teaPwIndexMappingPeerAddr = _TeaPwIndexMappingPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 7, 1, 4),
    _TeaPwIndexMappingPeerAddr_Type()
)
teaPwIndexMappingPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwIndexMappingPeerAddr.setStatus("current")
_TeaPwIndexMappingPwIndex_Type = TeaPwIndexType
_TeaPwIndexMappingPwIndex_Object = MibTableColumn
teaPwIndexMappingPwIndex = _TeaPwIndexMappingPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 7, 1, 5),
    _TeaPwIndexMappingPwIndex_Type()
)
teaPwIndexMappingPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwIndexMappingPwIndex.setStatus("current")
_TeaPwPeerMappingTable_Object = MibTable
teaPwPeerMappingTable = _TeaPwPeerMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 8)
)
if mibBuilder.loadTexts:
    teaPwPeerMappingTable.setStatus("current")
_TeaPwPeerMappingEntry_Object = MibTableRow
teaPwPeerMappingEntry = _TeaPwPeerMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 8, 1)
)
teaPwPeerMappingEntry.setIndexNames(
    (0, "CL-PW-MIB", "teaPwPeerMappingPeerAddrType"),
    (0, "CL-PW-MIB", "teaPwPeerMappingPeerAddr"),
    (0, "CL-PW-MIB", "teaPwPeerMappingPwType"),
    (0, "CL-PW-MIB", "teaPwPeerMappingPwID"),
)
if mibBuilder.loadTexts:
    teaPwPeerMappingEntry.setStatus("current")
_TeaPwPeerMappingPeerAddrType_Type = InetAddressType
_TeaPwPeerMappingPeerAddrType_Object = MibTableColumn
teaPwPeerMappingPeerAddrType = _TeaPwPeerMappingPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 8, 1, 1),
    _TeaPwPeerMappingPeerAddrType_Type()
)
teaPwPeerMappingPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwPeerMappingPeerAddrType.setStatus("current")
_TeaPwPeerMappingPeerAddr_Type = InetAddress
_TeaPwPeerMappingPeerAddr_Object = MibTableColumn
teaPwPeerMappingPeerAddr = _TeaPwPeerMappingPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 8, 1, 2),
    _TeaPwPeerMappingPeerAddr_Type()
)
teaPwPeerMappingPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwPeerMappingPeerAddr.setStatus("current")
_TeaPwPeerMappingPwType_Type = TeaPwTypeTC
_TeaPwPeerMappingPwType_Object = MibTableColumn
teaPwPeerMappingPwType = _TeaPwPeerMappingPwType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 8, 1, 3),
    _TeaPwPeerMappingPwType_Type()
)
teaPwPeerMappingPwType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwPeerMappingPwType.setStatus("current")
_TeaPwPeerMappingPwID_Type = TeaPwIDType
_TeaPwPeerMappingPwID_Object = MibTableColumn
teaPwPeerMappingPwID = _TeaPwPeerMappingPwID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 8, 1, 4),
    _TeaPwPeerMappingPwID_Type()
)
teaPwPeerMappingPwID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    teaPwPeerMappingPwID.setStatus("current")
_TeaPwPeerMappingPwIndex_Type = TeaPwIndexType
_TeaPwPeerMappingPwIndex_Object = MibTableColumn
teaPwPeerMappingPwIndex = _TeaPwPeerMappingPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 8, 1, 5),
    _TeaPwPeerMappingPwIndex_Type()
)
teaPwPeerMappingPwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teaPwPeerMappingPwIndex.setStatus("current")


class _TeaPwUpDownNotifEnable_Type(TruthValue):
    """Custom type teaPwUpDownNotifEnable based on TruthValue"""
    defaultValue = 2


_TeaPwUpDownNotifEnable_Type.__name__ = "TruthValue"
_TeaPwUpDownNotifEnable_Object = MibScalar
teaPwUpDownNotifEnable = _TeaPwUpDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 9),
    _TeaPwUpDownNotifEnable_Type()
)
teaPwUpDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teaPwUpDownNotifEnable.setStatus("current")


class _TeaPwDeletedNotifEnable_Type(TruthValue):
    """Custom type teaPwDeletedNotifEnable based on TruthValue"""
    defaultValue = 2


_TeaPwDeletedNotifEnable_Type.__name__ = "TruthValue"
_TeaPwDeletedNotifEnable_Object = MibScalar
teaPwDeletedNotifEnable = _TeaPwDeletedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 10),
    _TeaPwDeletedNotifEnable_Type()
)
teaPwDeletedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teaPwDeletedNotifEnable.setStatus("current")
_TeaPwNotifRate_Type = Unsigned32
_TeaPwNotifRate_Object = MibScalar
teaPwNotifRate = _TeaPwNotifRate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 1, 11),
    _TeaPwNotifRate_Type()
)
teaPwNotifRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teaPwNotifRate.setStatus("current")
_TeaPwConformance_ObjectIdentity = ObjectIdentity
teaPwConformance = _TeaPwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2)
)
_TeaPwGroups_ObjectIdentity = ObjectIdentity
teaPwGroups = _TeaPwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1)
)
_TeaPwCompliances_ObjectIdentity = ObjectIdentity
teaPwCompliances = _TeaPwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 2)
)

# Managed Objects groups

teaPwBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 1)
)
teaPwBasicGroup.setObjects(
      *(("CL-PW-MIB", "teaPwType"),
        ("CL-PW-MIB", "teaPwOwner"),
        ("CL-PW-MIB", "teaPwPsnType"),
        ("CL-PW-MIB", "teaPwPeerAddrType"),
        ("CL-PW-MIB", "teaPwPeerAddr"),
        ("CL-PW-MIB", "teaPwIfIndex"),
        ("CL-PW-MIB", "teaPwID"),
        ("CL-PW-MIB", "teaPwLocalGroupID"),
        ("CL-PW-MIB", "teaPwCwPreference"),
        ("CL-PW-MIB", "teaPwLocalIfMtu"),
        ("CL-PW-MIB", "teaPwLocalIfString"),
        ("CL-PW-MIB", "teaPwLocalCapabAdvert"),
        ("CL-PW-MIB", "teaPwRemoteGroupID"),
        ("CL-PW-MIB", "teaPwCwStatus"),
        ("CL-PW-MIB", "teaPwRemoteIfMtu"),
        ("CL-PW-MIB", "teaPwRemoteIfString"),
        ("CL-PW-MIB", "teaPwOutboundLabel"),
        ("CL-PW-MIB", "teaPwInboundLabel"),
        ("CL-PW-MIB", "teaPwName"),
        ("CL-PW-MIB", "teaPwDescr"),
        ("CL-PW-MIB", "teaPwCreateTime"),
        ("CL-PW-MIB", "teaPwUpTime"),
        ("CL-PW-MIB", "teaPwLastChange"),
        ("CL-PW-MIB", "teaPwAdminStatus"),
        ("CL-PW-MIB", "teaPwOperStatus"),
        ("CL-PW-MIB", "teaPwLocalStatus"),
        ("CL-PW-MIB", "teaPwRowStatus"),
        ("CL-PW-MIB", "teaPwStorageType"))
)
if mibBuilder.loadTexts:
    teaPwBasicGroup.setStatus("current")

teaPwPwIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 2)
)
teaPwPwIdGroup.setObjects(
    ("CL-PW-MIB", "teaPwID")
)
if mibBuilder.loadTexts:
    teaPwPwIdGroup.setStatus("current")

teaPwGeneralizedFecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 3)
)
teaPwGeneralizedFecGroup.setObjects(
      *(("CL-PW-MIB", "teaPwGroupAttachmentID"),
        ("CL-PW-MIB", "teaPwLocalAttachmentID"),
        ("CL-PW-MIB", "teaPwPeerAttachmentID"))
)
if mibBuilder.loadTexts:
    teaPwGeneralizedFecGroup.setStatus("current")

teaPwFcsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 4)
)
teaPwFcsGroup.setObjects(
      *(("CL-PW-MIB", "teaPwFcsRetentioncfg"),
        ("CL-PW-MIB", "teaPwFcsRetentionStatus"))
)
if mibBuilder.loadTexts:
    teaPwFcsGroup.setStatus("current")

teaPwFragGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 5)
)
teaPwFragGroup.setObjects(
      *(("CL-PW-MIB", "teaPwFragmentCfgSize"),
        ("CL-PW-MIB", "teaPwRmtFragCapability"))
)
if mibBuilder.loadTexts:
    teaPwFragGroup.setStatus("current")

teaPwPwStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 6)
)
teaPwPwStatusGroup.setObjects(
      *(("CL-PW-MIB", "teaPwRemoteCapabilities"),
        ("CL-PW-MIB", "teaPwRemoteStatusCapable"),
        ("CL-PW-MIB", "teaPwRemoteStatus"))
)
if mibBuilder.loadTexts:
    teaPwPwStatusGroup.setStatus("current")

teaPwGetNextGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 7)
)
teaPwGetNextGroup.setObjects(
    ("CL-PW-MIB", "teaPwIndexNext")
)
if mibBuilder.loadTexts:
    teaPwGetNextGroup.setStatus("current")

teaPwPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 8)
)
teaPwPriorityGroup.setObjects(
      *(("CL-PW-MIB", "teaPwSetUpPriority"),
        ("CL-PW-MIB", "teaPwHoldingPriority"))
)
if mibBuilder.loadTexts:
    teaPwPriorityGroup.setStatus("current")

teaPwAttachmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 9)
)
teaPwAttachmentGroup.setObjects(
    ("CL-PW-MIB", "teaPwAttachedPwIndex")
)
if mibBuilder.loadTexts:
    teaPwAttachmentGroup.setStatus("current")

teaPwPerformanceGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 10)
)
teaPwPerformanceGeneralGroup.setObjects(
    ("CL-PW-MIB", "teaPwPerfTotalErrorPackets")
)
if mibBuilder.loadTexts:
    teaPwPerformanceGeneralGroup.setStatus("current")

teaPwPeformance1DayIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 11)
)
teaPwPeformance1DayIntervalGroup.setObjects(
      *(("CL-PW-MIB", "teaPwPerf1DayIntervalValidData"),
        ("CL-PW-MIB", "teaPwPerf1DayIntervalMoniSecs"),
        ("CL-PW-MIB", "teaPwPerf1DayIntervalInHCPackets"),
        ("CL-PW-MIB", "teaPwPerf1DayIntervalInHCBytes"),
        ("CL-PW-MIB", "teaPwPerf1DayIntervalOutHCPackets"),
        ("CL-PW-MIB", "teaPwPerf1DayIntervalOutHCBytes"))
)
if mibBuilder.loadTexts:
    teaPwPeformance1DayIntervalGroup.setStatus("current")

teaPwPerformanceIntervalGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 12)
)
teaPwPerformanceIntervalGeneralGroup.setObjects(
      *(("CL-PW-MIB", "teaPwTimeElapsed"),
        ("CL-PW-MIB", "teaPwValidIntervals"),
        ("CL-PW-MIB", "teaPwPerfIntervalValidData"),
        ("CL-PW-MIB", "teaPwPerfIntervalTimeElapsed"))
)
if mibBuilder.loadTexts:
    teaPwPerformanceIntervalGeneralGroup.setStatus("current")

teaPwPeformanceIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 13)
)
teaPwPeformanceIntervalGroup.setObjects(
      *(("CL-PW-MIB", "teaPwPerfCurrentInPackets"),
        ("CL-PW-MIB", "teaPwPerfCurrentInBytes"),
        ("CL-PW-MIB", "teaPwPerfCurrentOutPackets"),
        ("CL-PW-MIB", "teaPwPerfCurrentOutBytes"),
        ("CL-PW-MIB", "teaPwPerfIntervalInPackets"),
        ("CL-PW-MIB", "teaPwPerfIntervalInBytes"),
        ("CL-PW-MIB", "teaPwPerfIntervalOutPackets"),
        ("CL-PW-MIB", "teaPwPerfIntervalOutBytes"))
)
if mibBuilder.loadTexts:
    teaPwPeformanceIntervalGroup.setStatus("current")

teaPwHCPeformanceIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 14)
)
teaPwHCPeformanceIntervalGroup.setObjects(
      *(("CL-PW-MIB", "teaPwPerfCurrentInHCPackets"),
        ("CL-PW-MIB", "teaPwPerfCurrentInHCBytes"),
        ("CL-PW-MIB", "teaPwPerfCurrentOutHCPackets"),
        ("CL-PW-MIB", "teaPwPerfCurrentOutHCBytes"),
        ("CL-PW-MIB", "teaPwPerfIntervalInHCPackets"),
        ("CL-PW-MIB", "teaPwPerfIntervalInHCBytes"),
        ("CL-PW-MIB", "teaPwPerfIntervalOutHCPackets"),
        ("CL-PW-MIB", "teaPwPerfIntervalOutHCBytes"))
)
if mibBuilder.loadTexts:
    teaPwHCPeformanceIntervalGroup.setStatus("current")

teaPwMappingTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 15)
)
teaPwMappingTablesGroup.setObjects(
      *(("CL-PW-MIB", "teaPwIndexMappingPwIndex"),
        ("CL-PW-MIB", "teaPwPeerMappingPwIndex"))
)
if mibBuilder.loadTexts:
    teaPwMappingTablesGroup.setStatus("current")

teaPwNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 16)
)
teaPwNotificationControlGroup.setObjects(
      *(("CL-PW-MIB", "teaPwUpDownNotifEnable"),
        ("CL-PW-MIB", "teaPwDeletedNotifEnable"),
        ("CL-PW-MIB", "teaPwNotifRate"))
)
if mibBuilder.loadTexts:
    teaPwNotificationControlGroup.setStatus("current")

bsodPwBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 18)
)
bsodPwBasicGroup.setObjects(
      *(("CL-PW-MIB", "teaPwType"),
        ("CL-PW-MIB", "teaPwPsnType"),
        ("CL-PW-MIB", "teaPwPeerAddrType"),
        ("CL-PW-MIB", "teaPwPeerAddr"),
        ("CL-PW-MIB", "teaPwIfIndex"),
        ("CL-PW-MIB", "teaPwOutboundLabel"),
        ("CL-PW-MIB", "teaPwInboundLabel"),
        ("CL-PW-MIB", "teaPwName"),
        ("CL-PW-MIB", "teaPwDescr"),
        ("CL-PW-MIB", "teaPwCreateTime"),
        ("CL-PW-MIB", "teaPwUpTime"),
        ("CL-PW-MIB", "teaPwLastChange"),
        ("CL-PW-MIB", "teaPwAdminStatus"),
        ("CL-PW-MIB", "teaPwOperStatus"),
        ("CL-PW-MIB", "teaPwLocalStatus"),
        ("CL-PW-MIB", "teaPwRowStatus"))
)
if mibBuilder.loadTexts:
    bsodPwBasicGroup.setStatus("current")


# Notification objects

teaPwDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 0, 1)
)
teaPwDown.setObjects(
      *(("CL-PW-MIB", "teaPwOperStatus"),
        ("CL-PW-MIB", "teaPwOperStatus"))
)
if mibBuilder.loadTexts:
    teaPwDown.setStatus(
        "current"
    )

teaPwUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 0, 2)
)
teaPwUp.setObjects(
      *(("CL-PW-MIB", "teaPwOperStatus"),
        ("CL-PW-MIB", "teaPwOperStatus"))
)
if mibBuilder.loadTexts:
    teaPwUp.setStatus(
        "current"
    )

teaPwDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 0, 3)
)
teaPwDeleted.setObjects(
      *(("CL-PW-MIB", "teaPwType"),
        ("CL-PW-MIB", "teaPwID"),
        ("CL-PW-MIB", "teaPwPeerAddrType"),
        ("CL-PW-MIB", "teaPwPeerAddr"))
)
if mibBuilder.loadTexts:
    teaPwDeleted.setStatus(
        "current"
    )


# Notifications groups

teaPwNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 1, 17)
)
teaPwNotificationGroup.setObjects(
      *(("CL-PW-MIB", "teaPwUp"),
        ("CL-PW-MIB", "teaPwDown"),
        ("CL-PW-MIB", "teaPwDeleted"))
)
if mibBuilder.loadTexts:
    teaPwNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pwModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 2, 1)
)
pwModuleFullCompliance.setObjects(
      *(("CL-PW-MIB", "teaPwBasicGroup"),
        ("CL-PW-MIB", "teaPwPerformanceGeneralGroup"))
)
if mibBuilder.loadTexts:
    pwModuleFullCompliance.setStatus(
        "current"
    )

bsodPwModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 2, 2)
)
bsodPwModuleFullCompliance.setObjects(
      *(("CL-PW-MIB", "bsodPwBasicGroup"),
        ("CL-PW-MIB", "teaPwPerformanceGeneralGroup"),
        ("CL-PW-MIB", "teaPwPeformanceIntervalGroup"),
        ("CL-PW-MIB", "teaPwNotificationGroup"),
        ("CL-PW-MIB", "teaPwPwIdGroup"),
        ("CL-PW-MIB", "teaPwGeneralizedFecGroup"),
        ("CL-PW-MIB", "teaPwFcsGroup"),
        ("CL-PW-MIB", "teaPwFragGroup"),
        ("CL-PW-MIB", "teaPwPwStatusGroup"),
        ("CL-PW-MIB", "teaPwGetNextGroup"),
        ("CL-PW-MIB", "teaPwPriorityGroup"),
        ("CL-PW-MIB", "teaPwAttachmentGroup"),
        ("CL-PW-MIB", "teaPwPeformance1DayIntervalGroup"),
        ("CL-PW-MIB", "teaPwPerformanceIntervalGeneralGroup"),
        ("CL-PW-MIB", "teaPwPeformanceIntervalGroup"),
        ("CL-PW-MIB", "teaPwHCPeformanceIntervalGroup"),
        ("CL-PW-MIB", "teaPwMappingTablesGroup"),
        ("CL-PW-MIB", "teaPwNotificationControlGroup"))
)
if mibBuilder.loadTexts:
    bsodPwModuleFullCompliance.setStatus(
        "current"
    )

teaPwModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 15, 2, 2, 3)
)
teaPwModuleReadOnlyCompliance.setObjects(
      *(("CL-PW-MIB", "teaPwBasicGroup"),
        ("CL-PW-MIB", "teaPwNotificationGroup"),
        ("CL-PW-MIB", "teaPwPwIdGroup"),
        ("CL-PW-MIB", "teaPwGeneralizedFecGroup"),
        ("CL-PW-MIB", "teaPwFcsGroup"),
        ("CL-PW-MIB", "teaPwFragGroup"),
        ("CL-PW-MIB", "teaPwPwStatusGroup"),
        ("CL-PW-MIB", "teaPwGetNextGroup"),
        ("CL-PW-MIB", "teaPwPriorityGroup"),
        ("CL-PW-MIB", "teaPwAttachmentGroup"),
        ("CL-PW-MIB", "teaPwPeformance1DayIntervalGroup"),
        ("CL-PW-MIB", "teaPwPerformanceIntervalGeneralGroup"),
        ("CL-PW-MIB", "teaPwPeformanceIntervalGroup"),
        ("CL-PW-MIB", "teaPwHCPeformanceIntervalGroup"),
        ("CL-PW-MIB", "teaPwMappingTablesGroup"),
        ("CL-PW-MIB", "teaPwNotificationControlGroup"))
)
if mibBuilder.loadTexts:
    teaPwModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PW-MIB",
    **{"teaPwMIB": teaPwMIB,
       "teaPwNotifications": teaPwNotifications,
       "teaPwDown": teaPwDown,
       "teaPwUp": teaPwUp,
       "teaPwDeleted": teaPwDeleted,
       "teaPwObjects": teaPwObjects,
       "teaPwIndexNext": teaPwIndexNext,
       "teaPwTable": teaPwTable,
       "teaPwEntry": teaPwEntry,
       "teaPwIndex": teaPwIndex,
       "teaPwType": teaPwType,
       "teaPwOwner": teaPwOwner,
       "teaPwPsnType": teaPwPsnType,
       "teaPwSetUpPriority": teaPwSetUpPriority,
       "teaPwHoldingPriority": teaPwHoldingPriority,
       "teaPwPeerAddrType": teaPwPeerAddrType,
       "teaPwPeerAddr": teaPwPeerAddr,
       "teaPwAttachedPwIndex": teaPwAttachedPwIndex,
       "teaPwIfIndex": teaPwIfIndex,
       "teaPwID": teaPwID,
       "teaPwLocalGroupID": teaPwLocalGroupID,
       "teaPwGroupAttachmentID": teaPwGroupAttachmentID,
       "teaPwLocalAttachmentID": teaPwLocalAttachmentID,
       "teaPwPeerAttachmentID": teaPwPeerAttachmentID,
       "teaPwCwPreference": teaPwCwPreference,
       "teaPwLocalIfMtu": teaPwLocalIfMtu,
       "teaPwLocalIfString": teaPwLocalIfString,
       "teaPwLocalCapabAdvert": teaPwLocalCapabAdvert,
       "teaPwRemoteGroupID": teaPwRemoteGroupID,
       "teaPwCwStatus": teaPwCwStatus,
       "teaPwRemoteIfMtu": teaPwRemoteIfMtu,
       "teaPwRemoteIfString": teaPwRemoteIfString,
       "teaPwRemoteCapabilities": teaPwRemoteCapabilities,
       "teaPwFragmentCfgSize": teaPwFragmentCfgSize,
       "teaPwRmtFragCapability": teaPwRmtFragCapability,
       "teaPwFcsRetentioncfg": teaPwFcsRetentioncfg,
       "teaPwFcsRetentionStatus": teaPwFcsRetentionStatus,
       "teaPwOutboundLabel": teaPwOutboundLabel,
       "teaPwInboundLabel": teaPwInboundLabel,
       "teaPwName": teaPwName,
       "teaPwDescr": teaPwDescr,
       "teaPwCreateTime": teaPwCreateTime,
       "teaPwUpTime": teaPwUpTime,
       "teaPwLastChange": teaPwLastChange,
       "teaPwAdminStatus": teaPwAdminStatus,
       "teaPwOperStatus": teaPwOperStatus,
       "teaPwLocalStatus": teaPwLocalStatus,
       "teaPwRemoteStatusCapable": teaPwRemoteStatusCapable,
       "teaPwRemoteStatus": teaPwRemoteStatus,
       "teaPwTimeElapsed": teaPwTimeElapsed,
       "teaPwValidIntervals": teaPwValidIntervals,
       "teaPwRowStatus": teaPwRowStatus,
       "teaPwStorageType": teaPwStorageType,
       "teaPwPerfCurrentTable": teaPwPerfCurrentTable,
       "teaPwPerfCurrentEntry": teaPwPerfCurrentEntry,
       "teaPwPerfCurrentInHCPackets": teaPwPerfCurrentInHCPackets,
       "teaPwPerfCurrentInHCBytes": teaPwPerfCurrentInHCBytes,
       "teaPwPerfCurrentOutHCPackets": teaPwPerfCurrentOutHCPackets,
       "teaPwPerfCurrentOutHCBytes": teaPwPerfCurrentOutHCBytes,
       "teaPwPerfCurrentInPackets": teaPwPerfCurrentInPackets,
       "teaPwPerfCurrentInBytes": teaPwPerfCurrentInBytes,
       "teaPwPerfCurrentOutPackets": teaPwPerfCurrentOutPackets,
       "teaPwPerfCurrentOutBytes": teaPwPerfCurrentOutBytes,
       "teaPwPerfIntervalTable": teaPwPerfIntervalTable,
       "teaPwPerfIntervalEntry": teaPwPerfIntervalEntry,
       "teaPwPerfIntervalNumber": teaPwPerfIntervalNumber,
       "teaPwPerfIntervalValidData": teaPwPerfIntervalValidData,
       "teaPwPerfIntervalTimeElapsed": teaPwPerfIntervalTimeElapsed,
       "teaPwPerfIntervalInHCPackets": teaPwPerfIntervalInHCPackets,
       "teaPwPerfIntervalInHCBytes": teaPwPerfIntervalInHCBytes,
       "teaPwPerfIntervalOutHCPackets": teaPwPerfIntervalOutHCPackets,
       "teaPwPerfIntervalOutHCBytes": teaPwPerfIntervalOutHCBytes,
       "teaPwPerfIntervalInPackets": teaPwPerfIntervalInPackets,
       "teaPwPerfIntervalInBytes": teaPwPerfIntervalInBytes,
       "teaPwPerfIntervalOutPackets": teaPwPerfIntervalOutPackets,
       "teaPwPerfIntervalOutBytes": teaPwPerfIntervalOutBytes,
       "teaPwPerf1DayIntervalTable": teaPwPerf1DayIntervalTable,
       "teaPwPerf1DayIntervalEntry": teaPwPerf1DayIntervalEntry,
       "teaPwPerf1DayIntervalNumber": teaPwPerf1DayIntervalNumber,
       "teaPwPerf1DayIntervalValidData": teaPwPerf1DayIntervalValidData,
       "teaPwPerf1DayIntervalMoniSecs": teaPwPerf1DayIntervalMoniSecs,
       "teaPwPerf1DayIntervalInHCPackets": teaPwPerf1DayIntervalInHCPackets,
       "teaPwPerf1DayIntervalInHCBytes": teaPwPerf1DayIntervalInHCBytes,
       "teaPwPerf1DayIntervalOutHCPackets": teaPwPerf1DayIntervalOutHCPackets,
       "teaPwPerf1DayIntervalOutHCBytes": teaPwPerf1DayIntervalOutHCBytes,
       "teaPwPerfTotalErrorPackets": teaPwPerfTotalErrorPackets,
       "teaPwIndexMappingTable": teaPwIndexMappingTable,
       "teaPwIndexMappingEntry": teaPwIndexMappingEntry,
       "teaPwIndexMappingPwType": teaPwIndexMappingPwType,
       "teaPwIndexMappingPwID": teaPwIndexMappingPwID,
       "teaPwIndexMappingPeerAddrType": teaPwIndexMappingPeerAddrType,
       "teaPwIndexMappingPeerAddr": teaPwIndexMappingPeerAddr,
       "teaPwIndexMappingPwIndex": teaPwIndexMappingPwIndex,
       "teaPwPeerMappingTable": teaPwPeerMappingTable,
       "teaPwPeerMappingEntry": teaPwPeerMappingEntry,
       "teaPwPeerMappingPeerAddrType": teaPwPeerMappingPeerAddrType,
       "teaPwPeerMappingPeerAddr": teaPwPeerMappingPeerAddr,
       "teaPwPeerMappingPwType": teaPwPeerMappingPwType,
       "teaPwPeerMappingPwID": teaPwPeerMappingPwID,
       "teaPwPeerMappingPwIndex": teaPwPeerMappingPwIndex,
       "teaPwUpDownNotifEnable": teaPwUpDownNotifEnable,
       "teaPwDeletedNotifEnable": teaPwDeletedNotifEnable,
       "teaPwNotifRate": teaPwNotifRate,
       "teaPwConformance": teaPwConformance,
       "teaPwGroups": teaPwGroups,
       "teaPwBasicGroup": teaPwBasicGroup,
       "teaPwPwIdGroup": teaPwPwIdGroup,
       "teaPwGeneralizedFecGroup": teaPwGeneralizedFecGroup,
       "teaPwFcsGroup": teaPwFcsGroup,
       "teaPwFragGroup": teaPwFragGroup,
       "teaPwPwStatusGroup": teaPwPwStatusGroup,
       "teaPwGetNextGroup": teaPwGetNextGroup,
       "teaPwPriorityGroup": teaPwPriorityGroup,
       "teaPwAttachmentGroup": teaPwAttachmentGroup,
       "teaPwPerformanceGeneralGroup": teaPwPerformanceGeneralGroup,
       "teaPwPeformance1DayIntervalGroup": teaPwPeformance1DayIntervalGroup,
       "teaPwPerformanceIntervalGeneralGroup": teaPwPerformanceIntervalGeneralGroup,
       "teaPwPeformanceIntervalGroup": teaPwPeformanceIntervalGroup,
       "teaPwHCPeformanceIntervalGroup": teaPwHCPeformanceIntervalGroup,
       "teaPwMappingTablesGroup": teaPwMappingTablesGroup,
       "teaPwNotificationControlGroup": teaPwNotificationControlGroup,
       "teaPwNotificationGroup": teaPwNotificationGroup,
       "bsodPwBasicGroup": bsodPwBasicGroup,
       "teaPwCompliances": teaPwCompliances,
       "pwModuleFullCompliance": pwModuleFullCompliance,
       "bsodPwModuleFullCompliance": bsodPwModuleFullCompliance,
       "teaPwModuleReadOnlyCompliance": teaPwModuleReadOnlyCompliance}
)
