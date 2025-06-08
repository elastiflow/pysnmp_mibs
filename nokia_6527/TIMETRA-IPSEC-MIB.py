# SNMP MIB module (TIMETRA-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-IPSEC-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:24 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(TmnxHwIndexOrZero,
 tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxHwIndexOrZero",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(TEntryId,) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TEntryId")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TTcpUdpPort,
 TmnxAdminState,
 TmnxBfdSessOperState,
 TmnxIPsecTunnelTemplateId,
 TmnxIPsecTunnelTemplateIdOrZero,
 TmnxIkePolicyAuthMethod,
 TmnxIkePolicyAutoEapMethod,
 TmnxIkePolicyAutoEapOwnMethod,
 TmnxIkePolicyOwnAuthMethod,
 TmnxOperState,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TmnxAdminState",
    "TmnxBfdSessOperState",
    "TmnxIPsecTunnelTemplateId",
    "TmnxIPsecTunnelTemplateIdOrZero",
    "TmnxIkePolicyAuthMethod",
    "TmnxIkePolicyAutoEapMethod",
    "TmnxIkePolicyAutoEapOwnMethod",
    "TmnxIkePolicyOwnAuthMethod",
    "TmnxOperState",
    "TmnxServId")


# MODULE-IDENTITY

timetraIPsecMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 48)
)
if mibBuilder.loadTexts:
    timetraIPsecMIBModule.setRevisions(
        ("2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxIPsecTransformId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )



class TmnxIPsecTransformIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )



class TmnxAuthAlgorithm(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("md5", 2),
          ("sha1", 3),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6),
          ("aesXcbc", 7))
    )



class TmnxEncrAlgorithm(TextualConvention, Integer32):
    status = "current"
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
        *(("null", 1),
          ("des", 2),
          ("des3", 3),
          ("aes128", 4),
          ("aes192", 5),
          ("aes256", 6))
    )



class TmnxIkePolicyId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )



class TmnxIkePolicyIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )



class TmnxIkeVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )



class TmnxIkePolicyIkeMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("aggressive", 2))
    )



class TmnxIkePolicyDHGroup(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("group1", 1),
          ("group2", 2),
          ("group5", 5),
          ("group14", 14),
          ("group15", 15))
    )



class TmnxIkePolicyDHGroupOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("group1", 1),
          ("group2", 2),
          ("group5", 5),
          ("group14", 14),
          ("group15", 15))
    )



class TmnxIPsecPolicyId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )



class TmnxIPsecPolicyIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )



class TmnxIPsecKeyingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("manual", 1),
          ("dynamic", 2))
    )



class TmnxIPsecDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



class TmnxIPsecDirection2(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2),
          ("bidirectional", 3))
    )



class TmnxIPsecProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ah", 1),
          ("esp", 2))
    )



class TmnxIPsecLocalIdType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ipv4", 1),
          ("fqdn", 2),
          ("dn", 3))
    )



class TmnxCertRevStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crl", 1),
          ("ocsp", 2))
    )



class TmnxCertRevStatusOrNone(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("crl", 1),
          ("ocsp", 2))
    )



class TmnxIkePolicyRelayUnSolCfgAttr(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("reserved1", 0),
          ("internalIp4Netmask", 1),
          ("internalIp4Dns", 2),
          ("reserved2", 3),
          ("internalIp6Dns", 4))
    )


class TmnxIpsecTrafficSelSide(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxIPsecConformance_ObjectIdentity = ObjectIdentity
tmnxIPsecConformance = _TmnxIPsecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48)
)
_TmnxIPsecCompliances_ObjectIdentity = ObjectIdentity
tmnxIPsecCompliances = _TmnxIPsecCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1)
)
_TmnxIPsecGroups_ObjectIdentity = ObjectIdentity
tmnxIPsecGroups = _TmnxIPsecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2)
)
_TmnxIPsecNotifGroups_ObjectIdentity = ObjectIdentity
tmnxIPsecNotifGroups = _TmnxIPsecNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3)
)
_TmnxIPsecObjects_ObjectIdentity = ObjectIdentity
tmnxIPsecObjects = _TmnxIPsecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48)
)
_TmnxIPsecTransformTblLastChanged_Type = TimeStamp
_TmnxIPsecTransformTblLastChanged_Object = MibScalar
tmnxIPsecTransformTblLastChanged = _TmnxIPsecTransformTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 1),
    _TmnxIPsecTransformTblLastChanged_Type()
)
tmnxIPsecTransformTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTransformTblLastChanged.setStatus("current")
_TmnxIPsecTransformTable_Object = MibTable
tmnxIPsecTransformTable = _TmnxIPsecTransformTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2)
)
if mibBuilder.loadTexts:
    tmnxIPsecTransformTable.setStatus("current")
_TmnxIPsecTransformEntry_Object = MibTableRow
tmnxIPsecTransformEntry = _TmnxIPsecTransformEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1)
)
tmnxIPsecTransformEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTransformId"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTransformEntry.setStatus("current")
_TmnxIPsecTransformId_Type = TmnxIPsecTransformId
_TmnxIPsecTransformId_Object = MibTableColumn
tmnxIPsecTransformId = _TmnxIPsecTransformId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 1),
    _TmnxIPsecTransformId_Type()
)
tmnxIPsecTransformId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTransformId.setStatus("current")
_TmnxIPsecTransformRowStatus_Type = RowStatus
_TmnxIPsecTransformRowStatus_Object = MibTableColumn
tmnxIPsecTransformRowStatus = _TmnxIPsecTransformRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 2),
    _TmnxIPsecTransformRowStatus_Type()
)
tmnxIPsecTransformRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTransformRowStatus.setStatus("current")
_TmnxIPsecTransformLastChanged_Type = TimeStamp
_TmnxIPsecTransformLastChanged_Object = MibTableColumn
tmnxIPsecTransformLastChanged = _TmnxIPsecTransformLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 3),
    _TmnxIPsecTransformLastChanged_Type()
)
tmnxIPsecTransformLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTransformLastChanged.setStatus("current")


class _TmnxIPsecTransformAuthAlgorithm_Type(TmnxAuthAlgorithm):
    """Custom type tmnxIPsecTransformAuthAlgorithm based on TmnxAuthAlgorithm"""
    defaultValue = 3


_TmnxIPsecTransformAuthAlgorithm_Type.__name__ = "TmnxAuthAlgorithm"
_TmnxIPsecTransformAuthAlgorithm_Object = MibTableColumn
tmnxIPsecTransformAuthAlgorithm = _TmnxIPsecTransformAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 4),
    _TmnxIPsecTransformAuthAlgorithm_Type()
)
tmnxIPsecTransformAuthAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTransformAuthAlgorithm.setStatus("current")


class _TmnxIPsecTransformEncrAlgorithm_Type(TmnxEncrAlgorithm):
    """Custom type tmnxIPsecTransformEncrAlgorithm based on TmnxEncrAlgorithm"""
    defaultValue = 4


_TmnxIPsecTransformEncrAlgorithm_Type.__name__ = "TmnxEncrAlgorithm"
_TmnxIPsecTransformEncrAlgorithm_Object = MibTableColumn
tmnxIPsecTransformEncrAlgorithm = _TmnxIPsecTransformEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 2, 1, 5),
    _TmnxIPsecTransformEncrAlgorithm_Type()
)
tmnxIPsecTransformEncrAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTransformEncrAlgorithm.setStatus("current")
_TmnxIkePolicyTableLastChanged_Type = TimeStamp
_TmnxIkePolicyTableLastChanged_Object = MibScalar
tmnxIkePolicyTableLastChanged = _TmnxIkePolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 3),
    _TmnxIkePolicyTableLastChanged_Type()
)
tmnxIkePolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIkePolicyTableLastChanged.setStatus("current")
_TmnxIkePolicyTable_Object = MibTable
tmnxIkePolicyTable = _TmnxIkePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4)
)
if mibBuilder.loadTexts:
    tmnxIkePolicyTable.setStatus("current")
_TmnxIkePolicyEntry_Object = MibTableRow
tmnxIkePolicyEntry = _TmnxIkePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1)
)
tmnxIkePolicyEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tmnxIkePolicyId"),
)
if mibBuilder.loadTexts:
    tmnxIkePolicyEntry.setStatus("current")
_TmnxIkePolicyId_Type = TmnxIkePolicyId
_TmnxIkePolicyId_Object = MibTableColumn
tmnxIkePolicyId = _TmnxIkePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 1),
    _TmnxIkePolicyId_Type()
)
tmnxIkePolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIkePolicyId.setStatus("current")
_TmnxIkePolicyRowStatus_Type = RowStatus
_TmnxIkePolicyRowStatus_Object = MibTableColumn
tmnxIkePolicyRowStatus = _TmnxIkePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 2),
    _TmnxIkePolicyRowStatus_Type()
)
tmnxIkePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyRowStatus.setStatus("current")
_TmnxIkePolicyLastChanged_Type = TimeStamp
_TmnxIkePolicyLastChanged_Object = MibTableColumn
tmnxIkePolicyLastChanged = _TmnxIkePolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 3),
    _TmnxIkePolicyLastChanged_Type()
)
tmnxIkePolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIkePolicyLastChanged.setStatus("current")


class _TmnxIkePolicyDescription_Type(TItemDescription):
    """Custom type tmnxIkePolicyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxIkePolicyDescription_Type.__name__ = "TItemDescription"
_TmnxIkePolicyDescription_Object = MibTableColumn
tmnxIkePolicyDescription = _TmnxIkePolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 4),
    _TmnxIkePolicyDescription_Type()
)
tmnxIkePolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyDescription.setStatus("current")


class _TmnxIkePolicyIkeMode_Type(TmnxIkePolicyIkeMode):
    """Custom type tmnxIkePolicyIkeMode based on TmnxIkePolicyIkeMode"""
    defaultValue = 1


_TmnxIkePolicyIkeMode_Type.__name__ = "TmnxIkePolicyIkeMode"
_TmnxIkePolicyIkeMode_Object = MibTableColumn
tmnxIkePolicyIkeMode = _TmnxIkePolicyIkeMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 5),
    _TmnxIkePolicyIkeMode_Type()
)
tmnxIkePolicyIkeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyIkeMode.setStatus("current")


class _TmnxIkePolicyDHGroup_Type(TmnxIkePolicyDHGroup):
    """Custom type tmnxIkePolicyDHGroup based on TmnxIkePolicyDHGroup"""
    defaultValue = 2


_TmnxIkePolicyDHGroup_Type.__name__ = "TmnxIkePolicyDHGroup"
_TmnxIkePolicyDHGroup_Object = MibTableColumn
tmnxIkePolicyDHGroup = _TmnxIkePolicyDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 6),
    _TmnxIkePolicyDHGroup_Type()
)
tmnxIkePolicyDHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyDHGroup.setStatus("current")


class _TmnxIkePolicyPFSEnabled_Type(TruthValue):
    """Custom type tmnxIkePolicyPFSEnabled based on TruthValue"""
    defaultValue = 2


_TmnxIkePolicyPFSEnabled_Type.__name__ = "TruthValue"
_TmnxIkePolicyPFSEnabled_Object = MibTableColumn
tmnxIkePolicyPFSEnabled = _TmnxIkePolicyPFSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 7),
    _TmnxIkePolicyPFSEnabled_Type()
)
tmnxIkePolicyPFSEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyPFSEnabled.setStatus("current")


class _TmnxIkePolicyPFSDHGroup_Type(TmnxIkePolicyDHGroup):
    """Custom type tmnxIkePolicyPFSDHGroup based on TmnxIkePolicyDHGroup"""
    defaultValue = 2


_TmnxIkePolicyPFSDHGroup_Type.__name__ = "TmnxIkePolicyDHGroup"
_TmnxIkePolicyPFSDHGroup_Object = MibTableColumn
tmnxIkePolicyPFSDHGroup = _TmnxIkePolicyPFSDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 8),
    _TmnxIkePolicyPFSDHGroup_Type()
)
tmnxIkePolicyPFSDHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyPFSDHGroup.setStatus("current")


class _TmnxIkePolicyAuthAlgorithm_Type(TmnxAuthAlgorithm):
    """Custom type tmnxIkePolicyAuthAlgorithm based on TmnxAuthAlgorithm"""
    defaultValue = 3


_TmnxIkePolicyAuthAlgorithm_Type.__name__ = "TmnxAuthAlgorithm"
_TmnxIkePolicyAuthAlgorithm_Object = MibTableColumn
tmnxIkePolicyAuthAlgorithm = _TmnxIkePolicyAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 9),
    _TmnxIkePolicyAuthAlgorithm_Type()
)
tmnxIkePolicyAuthAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyAuthAlgorithm.setStatus("current")


class _TmnxIkePolicyEncrAlgorithm_Type(TmnxEncrAlgorithm):
    """Custom type tmnxIkePolicyEncrAlgorithm based on TmnxEncrAlgorithm"""
    defaultValue = 4


_TmnxIkePolicyEncrAlgorithm_Type.__name__ = "TmnxEncrAlgorithm"
_TmnxIkePolicyEncrAlgorithm_Object = MibTableColumn
tmnxIkePolicyEncrAlgorithm = _TmnxIkePolicyEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 10),
    _TmnxIkePolicyEncrAlgorithm_Type()
)
tmnxIkePolicyEncrAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyEncrAlgorithm.setStatus("current")


class _TmnxIkePolicyIsakmpLifeTime_Type(Unsigned32):
    """Custom type tmnxIkePolicyIsakmpLifeTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 172800),
    )


_TmnxIkePolicyIsakmpLifeTime_Type.__name__ = "Unsigned32"
_TmnxIkePolicyIsakmpLifeTime_Object = MibTableColumn
tmnxIkePolicyIsakmpLifeTime = _TmnxIkePolicyIsakmpLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 11),
    _TmnxIkePolicyIsakmpLifeTime_Type()
)
tmnxIkePolicyIsakmpLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyIsakmpLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyIsakmpLifeTime.setUnits("seconds")


class _TmnxIkePolicyIPsecLifeTime_Type(Unsigned32):
    """Custom type tmnxIkePolicyIPsecLifeTime based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 172800),
    )


_TmnxIkePolicyIPsecLifeTime_Type.__name__ = "Unsigned32"
_TmnxIkePolicyIPsecLifeTime_Object = MibTableColumn
tmnxIkePolicyIPsecLifeTime = _TmnxIkePolicyIPsecLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 12),
    _TmnxIkePolicyIPsecLifeTime_Type()
)
tmnxIkePolicyIPsecLifeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyIPsecLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyIPsecLifeTime.setUnits("seconds")


class _TmnxIkePolicyNatTraversal_Type(Integer32):
    """Custom type tmnxIkePolicyNatTraversal based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("force", 3))
    )


_TmnxIkePolicyNatTraversal_Type.__name__ = "Integer32"
_TmnxIkePolicyNatTraversal_Object = MibTableColumn
tmnxIkePolicyNatTraversal = _TmnxIkePolicyNatTraversal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 13),
    _TmnxIkePolicyNatTraversal_Type()
)
tmnxIkePolicyNatTraversal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyNatTraversal.setStatus("current")


class _TmnxIkePolicyNatTKeepAliveIntvl_Type(Unsigned32):
    """Custom type tmnxIkePolicyNatTKeepAliveIntvl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 600),
    )


_TmnxIkePolicyNatTKeepAliveIntvl_Type.__name__ = "Unsigned32"
_TmnxIkePolicyNatTKeepAliveIntvl_Object = MibTableColumn
tmnxIkePolicyNatTKeepAliveIntvl = _TmnxIkePolicyNatTKeepAliveIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 14),
    _TmnxIkePolicyNatTKeepAliveIntvl_Type()
)
tmnxIkePolicyNatTKeepAliveIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyNatTKeepAliveIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyNatTKeepAliveIntvl.setUnits("seconds")


class _TmnxIkePolicyNatTBehindNatOnly_Type(TruthValue):
    """Custom type tmnxIkePolicyNatTBehindNatOnly based on TruthValue"""
    defaultValue = 1


_TmnxIkePolicyNatTBehindNatOnly_Type.__name__ = "TruthValue"
_TmnxIkePolicyNatTBehindNatOnly_Object = MibTableColumn
tmnxIkePolicyNatTBehindNatOnly = _TmnxIkePolicyNatTBehindNatOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 15),
    _TmnxIkePolicyNatTBehindNatOnly_Type()
)
tmnxIkePolicyNatTBehindNatOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyNatTBehindNatOnly.setStatus("current")


class _TmnxIkePolicyDpd_Type(Integer32):
    """Custom type tmnxIkePolicyDpd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("replyOnly", 3))
    )


_TmnxIkePolicyDpd_Type.__name__ = "Integer32"
_TmnxIkePolicyDpd_Object = MibTableColumn
tmnxIkePolicyDpd = _TmnxIkePolicyDpd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 16),
    _TmnxIkePolicyDpd_Type()
)
tmnxIkePolicyDpd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyDpd.setStatus("current")


class _TmnxIkePolicyDpdInterval_Type(Unsigned32):
    """Custom type tmnxIkePolicyDpdInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_TmnxIkePolicyDpdInterval_Type.__name__ = "Unsigned32"
_TmnxIkePolicyDpdInterval_Object = MibTableColumn
tmnxIkePolicyDpdInterval = _TmnxIkePolicyDpdInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 17),
    _TmnxIkePolicyDpdInterval_Type()
)
tmnxIkePolicyDpdInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyDpdInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIkePolicyDpdInterval.setUnits("seconds")


class _TmnxIkePolicyDpdMaxRetries_Type(Unsigned32):
    """Custom type tmnxIkePolicyDpdMaxRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_TmnxIkePolicyDpdMaxRetries_Type.__name__ = "Unsigned32"
_TmnxIkePolicyDpdMaxRetries_Object = MibTableColumn
tmnxIkePolicyDpdMaxRetries = _TmnxIkePolicyDpdMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 18),
    _TmnxIkePolicyDpdMaxRetries_Type()
)
tmnxIkePolicyDpdMaxRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyDpdMaxRetries.setStatus("current")


class _TmnxIkePolicyAuthMethod_Type(TmnxIkePolicyAuthMethod):
    """Custom type tmnxIkePolicyAuthMethod based on TmnxIkePolicyAuthMethod"""
    defaultValue = 1


_TmnxIkePolicyAuthMethod_Type.__name__ = "TmnxIkePolicyAuthMethod"
_TmnxIkePolicyAuthMethod_Object = MibTableColumn
tmnxIkePolicyAuthMethod = _TmnxIkePolicyAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 19),
    _TmnxIkePolicyAuthMethod_Type()
)
tmnxIkePolicyAuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyAuthMethod.setStatus("current")


class _TmnxIkePolicyIkeVersion_Type(TmnxIkeVersion):
    """Custom type tmnxIkePolicyIkeVersion based on TmnxIkeVersion"""
    defaultValue = 1


_TmnxIkePolicyIkeVersion_Type.__name__ = "TmnxIkeVersion"
_TmnxIkePolicyIkeVersion_Object = MibTableColumn
tmnxIkePolicyIkeVersion = _TmnxIkePolicyIkeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 20),
    _TmnxIkePolicyIkeVersion_Type()
)
tmnxIkePolicyIkeVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyIkeVersion.setStatus("current")


class _TmnxIkePolicyOwnAuthMethod_Type(TmnxIkePolicyOwnAuthMethod):
    """Custom type tmnxIkePolicyOwnAuthMethod based on TmnxIkePolicyOwnAuthMethod"""
    defaultValue = 0


_TmnxIkePolicyOwnAuthMethod_Type.__name__ = "TmnxIkePolicyOwnAuthMethod"
_TmnxIkePolicyOwnAuthMethod_Object = MibTableColumn
tmnxIkePolicyOwnAuthMethod = _TmnxIkePolicyOwnAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 21),
    _TmnxIkePolicyOwnAuthMethod_Type()
)
tmnxIkePolicyOwnAuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyOwnAuthMethod.setStatus("current")


class _TmnxIkePolicyMatchPeerToCert_Type(TruthValue):
    """Custom type tmnxIkePolicyMatchPeerToCert based on TruthValue"""
    defaultValue = 2


_TmnxIkePolicyMatchPeerToCert_Type.__name__ = "TruthValue"
_TmnxIkePolicyMatchPeerToCert_Object = MibTableColumn
tmnxIkePolicyMatchPeerToCert = _TmnxIkePolicyMatchPeerToCert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 22),
    _TmnxIkePolicyMatchPeerToCert_Type()
)
tmnxIkePolicyMatchPeerToCert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyMatchPeerToCert.setStatus("current")


class _TmnxIkePolicyRelayUnSolCfgAttr_Type(TmnxIkePolicyRelayUnSolCfgAttr):
    """Custom type tmnxIkePolicyRelayUnSolCfgAttr based on TmnxIkePolicyRelayUnSolCfgAttr"""
    defaultBinValue = "0"


_TmnxIkePolicyRelayUnSolCfgAttr_Type.__name__ = "TmnxIkePolicyRelayUnSolCfgAttr"
_TmnxIkePolicyRelayUnSolCfgAttr_Object = MibTableColumn
tmnxIkePolicyRelayUnSolCfgAttr = _TmnxIkePolicyRelayUnSolCfgAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 23),
    _TmnxIkePolicyRelayUnSolCfgAttr_Type()
)
tmnxIkePolicyRelayUnSolCfgAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyRelayUnSolCfgAttr.setStatus("current")


class _TmnxIkePolicyAutoEapMethod_Type(TmnxIkePolicyAutoEapMethod):
    """Custom type tmnxIkePolicyAutoEapMethod based on TmnxIkePolicyAutoEapMethod"""
    defaultValue = 2


_TmnxIkePolicyAutoEapMethod_Type.__name__ = "TmnxIkePolicyAutoEapMethod"
_TmnxIkePolicyAutoEapMethod_Object = MibTableColumn
tmnxIkePolicyAutoEapMethod = _TmnxIkePolicyAutoEapMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 24),
    _TmnxIkePolicyAutoEapMethod_Type()
)
tmnxIkePolicyAutoEapMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyAutoEapMethod.setStatus("current")


class _TmnxIkePolicyAutoEapOwnMethod_Type(TmnxIkePolicyAutoEapOwnMethod):
    """Custom type tmnxIkePolicyAutoEapOwnMethod based on TmnxIkePolicyAutoEapOwnMethod"""
    defaultValue = 2


_TmnxIkePolicyAutoEapOwnMethod_Type.__name__ = "TmnxIkePolicyAutoEapOwnMethod"
_TmnxIkePolicyAutoEapOwnMethod_Object = MibTableColumn
tmnxIkePolicyAutoEapOwnMethod = _TmnxIkePolicyAutoEapOwnMethod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 4, 1, 25),
    _TmnxIkePolicyAutoEapOwnMethod_Type()
)
tmnxIkePolicyAutoEapOwnMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIkePolicyAutoEapOwnMethod.setStatus("current")
_TmnxIPsecTunnelTableLastChanged_Type = TimeStamp
_TmnxIPsecTunnelTableLastChanged_Object = MibScalar
tmnxIPsecTunnelTableLastChanged = _TmnxIPsecTunnelTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 5),
    _TmnxIPsecTunnelTableLastChanged_Type()
)
tmnxIPsecTunnelTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelTableLastChanged.setStatus("current")
_TmnxIPsecTunnelTable_Object = MibTable
tmnxIPsecTunnelTable = _TmnxIPsecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6)
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelTable.setStatus("current")
_TmnxIPsecTunnelEntry_Object = MibTableRow
tmnxIPsecTunnelEntry = _TmnxIPsecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1)
)
tmnxIPsecTunnelEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelEntry.setStatus("current")
_TmnxIPsecTunnelName_Type = TNamedItem
_TmnxIPsecTunnelName_Object = MibTableColumn
tmnxIPsecTunnelName = _TmnxIPsecTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 1),
    _TmnxIPsecTunnelName_Type()
)
tmnxIPsecTunnelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelName.setStatus("current")
_TmnxIPsecTunnelRowStatus_Type = RowStatus
_TmnxIPsecTunnelRowStatus_Object = MibTableColumn
tmnxIPsecTunnelRowStatus = _TmnxIPsecTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 2),
    _TmnxIPsecTunnelRowStatus_Type()
)
tmnxIPsecTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelRowStatus.setStatus("current")
_TmnxIPsecTunnelLastChanged_Type = TimeStamp
_TmnxIPsecTunnelLastChanged_Object = MibTableColumn
tmnxIPsecTunnelLastChanged = _TmnxIPsecTunnelLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 3),
    _TmnxIPsecTunnelLastChanged_Type()
)
tmnxIPsecTunnelLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelLastChanged.setStatus("current")


class _TmnxIPsecTunnelDescription_Type(TItemDescription):
    """Custom type tmnxIPsecTunnelDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxIPsecTunnelDescription_Type.__name__ = "TItemDescription"
_TmnxIPsecTunnelDescription_Object = MibTableColumn
tmnxIPsecTunnelDescription = _TmnxIPsecTunnelDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 4),
    _TmnxIPsecTunnelDescription_Type()
)
tmnxIPsecTunnelDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelDescription.setStatus("current")


class _TmnxIPsecTunnelLclGwAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecTunnelLclGwAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecTunnelLclGwAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecTunnelLclGwAddrType_Object = MibTableColumn
tmnxIPsecTunnelLclGwAddrType = _TmnxIPsecTunnelLclGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 5),
    _TmnxIPsecTunnelLclGwAddrType_Type()
)
tmnxIPsecTunnelLclGwAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelLclGwAddrType.setStatus("current")


class _TmnxIPsecTunnelLclGwAddr_Type(InetAddress):
    """Custom type tmnxIPsecTunnelLclGwAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTunnelLclGwAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTunnelLclGwAddr_Object = MibTableColumn
tmnxIPsecTunnelLclGwAddr = _TmnxIPsecTunnelLclGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 6),
    _TmnxIPsecTunnelLclGwAddr_Type()
)
tmnxIPsecTunnelLclGwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelLclGwAddr.setStatus("current")


class _TmnxIPsecTunnelRemGwAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecTunnelRemGwAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecTunnelRemGwAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecTunnelRemGwAddrType_Object = MibTableColumn
tmnxIPsecTunnelRemGwAddrType = _TmnxIPsecTunnelRemGwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 7),
    _TmnxIPsecTunnelRemGwAddrType_Type()
)
tmnxIPsecTunnelRemGwAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelRemGwAddrType.setStatus("current")


class _TmnxIPsecTunnelRemGwAddr_Type(InetAddress):
    """Custom type tmnxIPsecTunnelRemGwAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTunnelRemGwAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTunnelRemGwAddr_Object = MibTableColumn
tmnxIPsecTunnelRemGwAddr = _TmnxIPsecTunnelRemGwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 8),
    _TmnxIPsecTunnelRemGwAddr_Type()
)
tmnxIPsecTunnelRemGwAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelRemGwAddr.setStatus("current")


class _TmnxIPsecTunnelPublicSvcId_Type(TmnxServId):
    """Custom type tmnxIPsecTunnelPublicSvcId based on TmnxServId"""
    defaultValue = 0


_TmnxIPsecTunnelPublicSvcId_Type.__name__ = "TmnxServId"
_TmnxIPsecTunnelPublicSvcId_Object = MibTableColumn
tmnxIPsecTunnelPublicSvcId = _TmnxIPsecTunnelPublicSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 9),
    _TmnxIPsecTunnelPublicSvcId_Type()
)
tmnxIPsecTunnelPublicSvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelPublicSvcId.setStatus("current")


class _TmnxIPsecTunnelSecurityPolicyId_Type(TmnxIPsecPolicyIdOrZero):
    """Custom type tmnxIPsecTunnelSecurityPolicyId based on TmnxIPsecPolicyIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelSecurityPolicyId_Type.__name__ = "TmnxIPsecPolicyIdOrZero"
_TmnxIPsecTunnelSecurityPolicyId_Object = MibTableColumn
tmnxIPsecTunnelSecurityPolicyId = _TmnxIPsecTunnelSecurityPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 10),
    _TmnxIPsecTunnelSecurityPolicyId_Type()
)
tmnxIPsecTunnelSecurityPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelSecurityPolicyId.setStatus("current")


class _TmnxIPsecTunnelKeyingType_Type(TmnxIPsecKeyingType):
    """Custom type tmnxIPsecTunnelKeyingType based on TmnxIPsecKeyingType"""
    defaultValue = 0


_TmnxIPsecTunnelKeyingType_Type.__name__ = "TmnxIPsecKeyingType"
_TmnxIPsecTunnelKeyingType_Object = MibTableColumn
tmnxIPsecTunnelKeyingType = _TmnxIPsecTunnelKeyingType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 11),
    _TmnxIPsecTunnelKeyingType_Type()
)
tmnxIPsecTunnelKeyingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelKeyingType.setStatus("current")


class _TmnxIPsecTunnelDynTransformId1_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxIPsecTunnelDynTransformId1 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelDynTransformId1_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxIPsecTunnelDynTransformId1_Object = MibTableColumn
tmnxIPsecTunnelDynTransformId1 = _TmnxIPsecTunnelDynTransformId1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 12),
    _TmnxIPsecTunnelDynTransformId1_Type()
)
tmnxIPsecTunnelDynTransformId1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelDynTransformId1.setStatus("current")


class _TmnxIPsecTunnelDynTransformId2_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxIPsecTunnelDynTransformId2 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelDynTransformId2_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxIPsecTunnelDynTransformId2_Object = MibTableColumn
tmnxIPsecTunnelDynTransformId2 = _TmnxIPsecTunnelDynTransformId2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 13),
    _TmnxIPsecTunnelDynTransformId2_Type()
)
tmnxIPsecTunnelDynTransformId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelDynTransformId2.setStatus("current")


class _TmnxIPsecTunnelDynTransformId3_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxIPsecTunnelDynTransformId3 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelDynTransformId3_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxIPsecTunnelDynTransformId3_Object = MibTableColumn
tmnxIPsecTunnelDynTransformId3 = _TmnxIPsecTunnelDynTransformId3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 14),
    _TmnxIPsecTunnelDynTransformId3_Type()
)
tmnxIPsecTunnelDynTransformId3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelDynTransformId3.setStatus("current")


class _TmnxIPsecTunnelDynTransformId4_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tmnxIPsecTunnelDynTransformId4 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelDynTransformId4_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TmnxIPsecTunnelDynTransformId4_Object = MibTableColumn
tmnxIPsecTunnelDynTransformId4 = _TmnxIPsecTunnelDynTransformId4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 15),
    _TmnxIPsecTunnelDynTransformId4_Type()
)
tmnxIPsecTunnelDynTransformId4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelDynTransformId4.setStatus("current")


class _TmnxIPsecTunnelIkePolicyId_Type(TmnxIkePolicyIdOrZero):
    """Custom type tmnxIPsecTunnelIkePolicyId based on TmnxIkePolicyIdOrZero"""
    defaultValue = 0


_TmnxIPsecTunnelIkePolicyId_Type.__name__ = "TmnxIkePolicyIdOrZero"
_TmnxIPsecTunnelIkePolicyId_Object = MibTableColumn
tmnxIPsecTunnelIkePolicyId = _TmnxIPsecTunnelIkePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 16),
    _TmnxIPsecTunnelIkePolicyId_Type()
)
tmnxIPsecTunnelIkePolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIkePolicyId.setStatus("current")


class _TmnxIPsecTunnelIkePreSharedKey_Type(OctetString):
    """Custom type tmnxIPsecTunnelIkePreSharedKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxIPsecTunnelIkePreSharedKey_Type.__name__ = "OctetString"
_TmnxIPsecTunnelIkePreSharedKey_Object = MibTableColumn
tmnxIPsecTunnelIkePreSharedKey = _TmnxIPsecTunnelIkePreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 17),
    _TmnxIPsecTunnelIkePreSharedKey_Type()
)
tmnxIPsecTunnelIkePreSharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIkePreSharedKey.setStatus("current")


class _TmnxIPsecTunnelAdminState_Type(TmnxAdminState):
    """Custom type tmnxIPsecTunnelAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIPsecTunnelAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIPsecTunnelAdminState_Object = MibTableColumn
tmnxIPsecTunnelAdminState = _TmnxIPsecTunnelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 18),
    _TmnxIPsecTunnelAdminState_Type()
)
tmnxIPsecTunnelAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelAdminState.setStatus("current")
_TmnxIPsecTunnelOperState_Type = TmnxOperState
_TmnxIPsecTunnelOperState_Object = MibTableColumn
tmnxIPsecTunnelOperState = _TmnxIPsecTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 19),
    _TmnxIPsecTunnelOperState_Type()
)
tmnxIPsecTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelOperState.setStatus("current")


class _TmnxIPsecTunnelOperFlags_Type(Bits):
    """Custom type tmnxIPsecTunnelOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("unresolvedLocalIp", 0),
          ("tunnelAdminDown", 1),
          ("sapDown", 2),
          ("unresolvedPublicSvc", 3),
          ("bfdSessionDown", 4),
          ("reserved1", 5),
          ("unresolvedDstIp", 6),
          ("invalidCertFile", 7),
          ("invalidKeyFile", 8),
          ("trustAnchorsDown", 9),
          ("certProfileDown", 10),
          ("invalidCertKeyCombo", 11))
    )

_TmnxIPsecTunnelOperFlags_Type.__name__ = "Bits"
_TmnxIPsecTunnelOperFlags_Object = MibTableColumn
tmnxIPsecTunnelOperFlags = _TmnxIPsecTunnelOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 20),
    _TmnxIPsecTunnelOperFlags_Type()
)
tmnxIPsecTunnelOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelOperFlags.setStatus("current")


class _TmnxIPsecTunnelReplayWindow_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelReplayWindow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
    )


_TmnxIPsecTunnelReplayWindow_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelReplayWindow_Object = MibTableColumn
tmnxIPsecTunnelReplayWindow = _TmnxIPsecTunnelReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 21),
    _TmnxIPsecTunnelReplayWindow_Type()
)
tmnxIPsecTunnelReplayWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelReplayWindow.setStatus("current")


class _TmnxIPsecTunnelAutoEstablish_Type(TruthValue):
    """Custom type tmnxIPsecTunnelAutoEstablish based on TruthValue"""
    defaultValue = 2


_TmnxIPsecTunnelAutoEstablish_Type.__name__ = "TruthValue"
_TmnxIPsecTunnelAutoEstablish_Object = MibTableColumn
tmnxIPsecTunnelAutoEstablish = _TmnxIPsecTunnelAutoEstablish_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 22),
    _TmnxIPsecTunnelAutoEstablish_Type()
)
tmnxIPsecTunnelAutoEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelAutoEstablish.setStatus("current")


class _TmnxIPsecTunnelBfdDesignate_Type(TruthValue):
    """Custom type tmnxIPsecTunnelBfdDesignate based on TruthValue"""
    defaultValue = 2


_TmnxIPsecTunnelBfdDesignate_Type.__name__ = "TruthValue"
_TmnxIPsecTunnelBfdDesignate_Object = MibTableColumn
tmnxIPsecTunnelBfdDesignate = _TmnxIPsecTunnelBfdDesignate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 23),
    _TmnxIPsecTunnelBfdDesignate_Type()
)
tmnxIPsecTunnelBfdDesignate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdDesignate.setStatus("current")


class _TmnxIPsecTunnelCertTrustAnchor_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecTunnelCertTrustAnchor based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecTunnelCertTrustAnchor_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecTunnelCertTrustAnchor_Object = MibTableColumn
tmnxIPsecTunnelCertTrustAnchor = _TmnxIPsecTunnelCertTrustAnchor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 24),
    _TmnxIPsecTunnelCertTrustAnchor_Type()
)
tmnxIPsecTunnelCertTrustAnchor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCertTrustAnchor.setStatus("current")


class _TmnxIPsecTunnelCertFile_Type(DisplayString):
    """Custom type tmnxIPsecTunnelCertFile based on DisplayString"""
    defaultHexValue = ""


_TmnxIPsecTunnelCertFile_Type.__name__ = "DisplayString"
_TmnxIPsecTunnelCertFile_Object = MibTableColumn
tmnxIPsecTunnelCertFile = _TmnxIPsecTunnelCertFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 25),
    _TmnxIPsecTunnelCertFile_Type()
)
tmnxIPsecTunnelCertFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCertFile.setStatus("current")


class _TmnxIPsecTunnelKeyFile_Type(DisplayString):
    """Custom type tmnxIPsecTunnelKeyFile based on DisplayString"""
    defaultHexValue = ""


_TmnxIPsecTunnelKeyFile_Type.__name__ = "DisplayString"
_TmnxIPsecTunnelKeyFile_Object = MibTableColumn
tmnxIPsecTunnelKeyFile = _TmnxIPsecTunnelKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 26),
    _TmnxIPsecTunnelKeyFile_Type()
)
tmnxIPsecTunnelKeyFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelKeyFile.setStatus("current")


class _TmnxIPsecTunnelLocalIdType_Type(TmnxIPsecLocalIdType):
    """Custom type tmnxIPsecTunnelLocalIdType based on TmnxIPsecLocalIdType"""
    defaultValue = 0


_TmnxIPsecTunnelLocalIdType_Type.__name__ = "TmnxIPsecLocalIdType"
_TmnxIPsecTunnelLocalIdType_Object = MibTableColumn
tmnxIPsecTunnelLocalIdType = _TmnxIPsecTunnelLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 27),
    _TmnxIPsecTunnelLocalIdType_Type()
)
tmnxIPsecTunnelLocalIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelLocalIdType.setStatus("current")


class _TmnxIPsecTunnelLocalIdValue_Type(DisplayString):
    """Custom type tmnxIPsecTunnelLocalIdValue based on DisplayString"""
    defaultHexValue = ""


_TmnxIPsecTunnelLocalIdValue_Type.__name__ = "DisplayString"
_TmnxIPsecTunnelLocalIdValue_Object = MibTableColumn
tmnxIPsecTunnelLocalIdValue = _TmnxIPsecTunnelLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 28),
    _TmnxIPsecTunnelLocalIdValue_Type()
)
tmnxIPsecTunnelLocalIdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelLocalIdValue.setStatus("current")


class _TmnxIPsecTunnelClearDfBit_Type(TruthValue):
    """Custom type tmnxIPsecTunnelClearDfBit based on TruthValue"""
    defaultValue = 2


_TmnxIPsecTunnelClearDfBit_Type.__name__ = "TruthValue"
_TmnxIPsecTunnelClearDfBit_Object = MibTableColumn
tmnxIPsecTunnelClearDfBit = _TmnxIPsecTunnelClearDfBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 29),
    _TmnxIPsecTunnelClearDfBit_Type()
)
tmnxIPsecTunnelClearDfBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelClearDfBit.setStatus("current")


class _TmnxIPsecTunnelIpMtu_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxIPsecTunnelIpMtu_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelIpMtu_Object = MibTableColumn
tmnxIPsecTunnelIpMtu = _TmnxIPsecTunnelIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 30),
    _TmnxIPsecTunnelIpMtu_Type()
)
tmnxIPsecTunnelIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIpMtu.setStatus("current")
_TmnxIPsecTunnelHostISA_Type = TmnxHwIndexOrZero
_TmnxIPsecTunnelHostISA_Object = MibTableColumn
tmnxIPsecTunnelHostISA = _TmnxIPsecTunnelHostISA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 31),
    _TmnxIPsecTunnelHostISA_Type()
)
tmnxIPsecTunnelHostISA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelHostISA.setStatus("current")


class _TmnxIPsecTunnelCSVPrimary_Type(TmnxCertRevStatus):
    """Custom type tmnxIPsecTunnelCSVPrimary based on TmnxCertRevStatus"""
    defaultValue = 1


_TmnxIPsecTunnelCSVPrimary_Type.__name__ = "TmnxCertRevStatus"
_TmnxIPsecTunnelCSVPrimary_Object = MibTableColumn
tmnxIPsecTunnelCSVPrimary = _TmnxIPsecTunnelCSVPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 32),
    _TmnxIPsecTunnelCSVPrimary_Type()
)
tmnxIPsecTunnelCSVPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCSVPrimary.setStatus("current")


class _TmnxIPsecTunnelCSVSecondary_Type(TmnxCertRevStatusOrNone):
    """Custom type tmnxIPsecTunnelCSVSecondary based on TmnxCertRevStatusOrNone"""
    defaultValue = 0


_TmnxIPsecTunnelCSVSecondary_Type.__name__ = "TmnxCertRevStatusOrNone"
_TmnxIPsecTunnelCSVSecondary_Object = MibTableColumn
tmnxIPsecTunnelCSVSecondary = _TmnxIPsecTunnelCSVSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 33),
    _TmnxIPsecTunnelCSVSecondary_Type()
)
tmnxIPsecTunnelCSVSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCSVSecondary.setStatus("current")


class _TmnxIPsecTunnelCSVDefResult_Type(Integer32):
    """Custom type tmnxIPsecTunnelCSVDefResult based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("revoked", 0),
          ("good", 1))
    )


_TmnxIPsecTunnelCSVDefResult_Type.__name__ = "Integer32"
_TmnxIPsecTunnelCSVDefResult_Object = MibTableColumn
tmnxIPsecTunnelCSVDefResult = _TmnxIPsecTunnelCSVDefResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 34),
    _TmnxIPsecTunnelCSVDefResult_Type()
)
tmnxIPsecTunnelCSVDefResult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCSVDefResult.setStatus("current")


class _TmnxIPsecTunnelCertProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecTunnelCertProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecTunnelCertProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecTunnelCertProfile_Object = MibTableColumn
tmnxIPsecTunnelCertProfile = _TmnxIPsecTunnelCertProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 35),
    _TmnxIPsecTunnelCertProfile_Type()
)
tmnxIPsecTunnelCertProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCertProfile.setStatus("current")
_TmnxIPsecTunnelMatchTrustAnchor_Type = TNamedItemOrEmpty
_TmnxIPsecTunnelMatchTrustAnchor_Object = MibTableColumn
tmnxIPsecTunnelMatchTrustAnchor = _TmnxIPsecTunnelMatchTrustAnchor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 36),
    _TmnxIPsecTunnelMatchTrustAnchor_Type()
)
tmnxIPsecTunnelMatchTrustAnchor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelMatchTrustAnchor.setStatus("current")


class _TmnxIPsecTunnelCertTrstAnchrProf_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecTunnelCertTrstAnchrProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecTunnelCertTrstAnchrProf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecTunnelCertTrstAnchrProf_Object = MibTableColumn
tmnxIPsecTunnelCertTrstAnchrProf = _TmnxIPsecTunnelCertTrstAnchrProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 37),
    _TmnxIPsecTunnelCertTrstAnchrProf_Type()
)
tmnxIPsecTunnelCertTrstAnchrProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCertTrstAnchrProf.setStatus("current")


class _TmnxIPsecTunnelEncapIpMtu_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelEncapIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxIPsecTunnelEncapIpMtu_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelEncapIpMtu_Object = MibTableColumn
tmnxIPsecTunnelEncapIpMtu = _TmnxIPsecTunnelEncapIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 38),
    _TmnxIPsecTunnelEncapIpMtu_Type()
)
tmnxIPsecTunnelEncapIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelEncapIpMtu.setStatus("current")


class _TmnxIPsecTunnelIcmp6Pkt2Big_Type(TruthValue):
    """Custom type tmnxIPsecTunnelIcmp6Pkt2Big based on TruthValue"""
    defaultValue = 1


_TmnxIPsecTunnelIcmp6Pkt2Big_Type.__name__ = "TruthValue"
_TmnxIPsecTunnelIcmp6Pkt2Big_Object = MibTableColumn
tmnxIPsecTunnelIcmp6Pkt2Big = _TmnxIPsecTunnelIcmp6Pkt2Big_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 40),
    _TmnxIPsecTunnelIcmp6Pkt2Big_Type()
)
tmnxIPsecTunnelIcmp6Pkt2Big.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIcmp6Pkt2Big.setStatus("current")


class _TmnxIPsecTunnelIcmp6NumPkt2Big_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelIcmp6NumPkt2Big based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TmnxIPsecTunnelIcmp6NumPkt2Big_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelIcmp6NumPkt2Big_Object = MibTableColumn
tmnxIPsecTunnelIcmp6NumPkt2Big = _TmnxIPsecTunnelIcmp6NumPkt2Big_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 41),
    _TmnxIPsecTunnelIcmp6NumPkt2Big_Type()
)
tmnxIPsecTunnelIcmp6NumPkt2Big.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIcmp6NumPkt2Big.setStatus("current")


class _TmnxIPsecTunnelIcmp6Pkt2BigTime_Type(Unsigned32):
    """Custom type tmnxIPsecTunnelIcmp6Pkt2BigTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TmnxIPsecTunnelIcmp6Pkt2BigTime_Type.__name__ = "Unsigned32"
_TmnxIPsecTunnelIcmp6Pkt2BigTime_Object = MibTableColumn
tmnxIPsecTunnelIcmp6Pkt2BigTime = _TmnxIPsecTunnelIcmp6Pkt2BigTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 42),
    _TmnxIPsecTunnelIcmp6Pkt2BigTime_Type()
)
tmnxIPsecTunnelIcmp6Pkt2BigTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIcmp6Pkt2BigTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIcmp6Pkt2BigTime.setUnits("seconds")
_TmnxIPsecTunnelOperChanged_Type = TimeStamp
_TmnxIPsecTunnelOperChanged_Object = MibTableColumn
tmnxIPsecTunnelOperChanged = _TmnxIPsecTunnelOperChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 6, 1, 43),
    _TmnxIPsecTunnelOperChanged_Type()
)
tmnxIPsecTunnelOperChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelOperChanged.setStatus("current")
_TmnxIPsecTunnelStatsTable_Object = MibTable
tmnxIPsecTunnelStatsTable = _TmnxIPsecTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7)
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelStatsTable.setStatus("current")
_TmnxIPsecTunnelStatsEntry_Object = MibTableRow
tmnxIPsecTunnelStatsEntry = _TmnxIPsecTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1)
)
tmnxIPsecTunnelStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelStatsEntry.setStatus("current")


class _TmnxIPsecTunnelIsakmpState_Type(Integer32):
    """Custom type tmnxIPsecTunnelIsakmpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxIPsecTunnelIsakmpState_Type.__name__ = "Integer32"
_TmnxIPsecTunnelIsakmpState_Object = MibTableColumn
tmnxIPsecTunnelIsakmpState = _TmnxIPsecTunnelIsakmpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 1),
    _TmnxIPsecTunnelIsakmpState_Type()
)
tmnxIPsecTunnelIsakmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIsakmpState.setStatus("current")
_TmnxIPsecTunnelIsakmpEstabTime_Type = TimeStamp
_TmnxIPsecTunnelIsakmpEstabTime_Object = MibTableColumn
tmnxIPsecTunnelIsakmpEstabTime = _TmnxIPsecTunnelIsakmpEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 2),
    _TmnxIPsecTunnelIsakmpEstabTime_Type()
)
tmnxIPsecTunnelIsakmpEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIsakmpEstabTime.setStatus("current")
_TmnxIPsecTunnelIsakmpNegLifeTime_Type = Unsigned32
_TmnxIPsecTunnelIsakmpNegLifeTime_Object = MibTableColumn
tmnxIPsecTunnelIsakmpNegLifeTime = _TmnxIPsecTunnelIsakmpNegLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 3),
    _TmnxIPsecTunnelIsakmpNegLifeTime_Type()
)
tmnxIPsecTunnelIsakmpNegLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelIsakmpNegLifeTime.setStatus("current")
_TmnxIPsecTunnelNumDpdTx_Type = Counter32
_TmnxIPsecTunnelNumDpdTx_Object = MibTableColumn
tmnxIPsecTunnelNumDpdTx = _TmnxIPsecTunnelNumDpdTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 4),
    _TmnxIPsecTunnelNumDpdTx_Type()
)
tmnxIPsecTunnelNumDpdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumDpdTx.setStatus("current")
_TmnxIPsecTunnelNumDpdRx_Type = Counter32
_TmnxIPsecTunnelNumDpdRx_Object = MibTableColumn
tmnxIPsecTunnelNumDpdRx = _TmnxIPsecTunnelNumDpdRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 5),
    _TmnxIPsecTunnelNumDpdRx_Type()
)
tmnxIPsecTunnelNumDpdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumDpdRx.setStatus("current")
_TmnxIPsecTunnelNumDpdAckTx_Type = Counter32
_TmnxIPsecTunnelNumDpdAckTx_Object = MibTableColumn
tmnxIPsecTunnelNumDpdAckTx = _TmnxIPsecTunnelNumDpdAckTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 6),
    _TmnxIPsecTunnelNumDpdAckTx_Type()
)
tmnxIPsecTunnelNumDpdAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumDpdAckTx.setStatus("current")
_TmnxIPsecTunnelNumDpdAckRx_Type = Counter32
_TmnxIPsecTunnelNumDpdAckRx_Object = MibTableColumn
tmnxIPsecTunnelNumDpdAckRx = _TmnxIPsecTunnelNumDpdAckRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 7),
    _TmnxIPsecTunnelNumDpdAckRx_Type()
)
tmnxIPsecTunnelNumDpdAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumDpdAckRx.setStatus("current")
_TmnxIPsecTunnelNumExpRx_Type = Counter32
_TmnxIPsecTunnelNumExpRx_Object = MibTableColumn
tmnxIPsecTunnelNumExpRx = _TmnxIPsecTunnelNumExpRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 8),
    _TmnxIPsecTunnelNumExpRx_Type()
)
tmnxIPsecTunnelNumExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumExpRx.setStatus("current")
_TmnxIPsecTunnelNumInvalidDpdRx_Type = Counter32
_TmnxIPsecTunnelNumInvalidDpdRx_Object = MibTableColumn
tmnxIPsecTunnelNumInvalidDpdRx = _TmnxIPsecTunnelNumInvalidDpdRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 9),
    _TmnxIPsecTunnelNumInvalidDpdRx_Type()
)
tmnxIPsecTunnelNumInvalidDpdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumInvalidDpdRx.setStatus("current")
_TmnxIPsecTunnelNumCtrlPktsTx_Type = Counter32
_TmnxIPsecTunnelNumCtrlPktsTx_Object = MibTableColumn
tmnxIPsecTunnelNumCtrlPktsTx = _TmnxIPsecTunnelNumCtrlPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 10),
    _TmnxIPsecTunnelNumCtrlPktsTx_Type()
)
tmnxIPsecTunnelNumCtrlPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumCtrlPktsTx.setStatus("current")
_TmnxIPsecTunnelNumCtrlPktsRx_Type = Counter32
_TmnxIPsecTunnelNumCtrlPktsRx_Object = MibTableColumn
tmnxIPsecTunnelNumCtrlPktsRx = _TmnxIPsecTunnelNumCtrlPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 11),
    _TmnxIPsecTunnelNumCtrlPktsRx_Type()
)
tmnxIPsecTunnelNumCtrlPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumCtrlPktsRx.setStatus("current")
_TmnxIPsecTunnelNumCtrlTxErrors_Type = Counter32
_TmnxIPsecTunnelNumCtrlTxErrors_Object = MibTableColumn
tmnxIPsecTunnelNumCtrlTxErrors = _TmnxIPsecTunnelNumCtrlTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 12),
    _TmnxIPsecTunnelNumCtrlTxErrors_Type()
)
tmnxIPsecTunnelNumCtrlTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumCtrlTxErrors.setStatus("current")
_TmnxIPsecTunnelNumCtrlRxErrors_Type = Counter32
_TmnxIPsecTunnelNumCtrlRxErrors_Object = MibTableColumn
tmnxIPsecTunnelNumCtrlRxErrors = _TmnxIPsecTunnelNumCtrlRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 13),
    _TmnxIPsecTunnelNumCtrlRxErrors_Type()
)
tmnxIPsecTunnelNumCtrlRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelNumCtrlRxErrors.setStatus("current")
_TmnxIPsecTunnelMatCertEntryId_Type = Integer32
_TmnxIPsecTunnelMatCertEntryId_Object = MibTableColumn
tmnxIPsecTunnelMatCertEntryId = _TmnxIPsecTunnelMatCertEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 14),
    _TmnxIPsecTunnelMatCertEntryId_Type()
)
tmnxIPsecTunnelMatCertEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelMatCertEntryId.setStatus("current")
_TmnxIPsecTunnelCertProfName_Type = TNamedItemOrEmpty
_TmnxIPsecTunnelCertProfName_Object = MibTableColumn
tmnxIPsecTunnelCertProfName = _TmnxIPsecTunnelCertProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 7, 1, 15),
    _TmnxIPsecTunnelCertProfName_Type()
)
tmnxIPsecTunnelCertProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelCertProfName.setStatus("current")
_TmnxIPsecPolicyTableLastChanged_Type = TimeStamp
_TmnxIPsecPolicyTableLastChanged_Object = MibScalar
tmnxIPsecPolicyTableLastChanged = _TmnxIPsecPolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 8),
    _TmnxIPsecPolicyTableLastChanged_Type()
)
tmnxIPsecPolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyTableLastChanged.setStatus("current")
_TmnxIPsecPolicyTable_Object = MibTable
tmnxIPsecPolicyTable = _TmnxIPsecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 9)
)
if mibBuilder.loadTexts:
    tmnxIPsecPolicyTable.setStatus("current")
_TmnxIPsecPolicyEntry_Object = MibTableRow
tmnxIPsecPolicyEntry = _TmnxIPsecPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 9, 1)
)
tmnxIPsecPolicyEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyId"),
)
if mibBuilder.loadTexts:
    tmnxIPsecPolicyEntry.setStatus("current")
_TmnxIPsecPolicyId_Type = TmnxIPsecPolicyId
_TmnxIPsecPolicyId_Object = MibTableColumn
tmnxIPsecPolicyId = _TmnxIPsecPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 9, 1, 1),
    _TmnxIPsecPolicyId_Type()
)
tmnxIPsecPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyId.setStatus("current")
_TmnxIPsecPolicyRowStatus_Type = RowStatus
_TmnxIPsecPolicyRowStatus_Object = MibTableColumn
tmnxIPsecPolicyRowStatus = _TmnxIPsecPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 9, 1, 2),
    _TmnxIPsecPolicyRowStatus_Type()
)
tmnxIPsecPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyRowStatus.setStatus("current")
_TmnxIPsecPolicyLastChanged_Type = TimeStamp
_TmnxIPsecPolicyLastChanged_Object = MibTableColumn
tmnxIPsecPolicyLastChanged = _TmnxIPsecPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 9, 1, 3),
    _TmnxIPsecPolicyLastChanged_Type()
)
tmnxIPsecPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyLastChanged.setStatus("current")
_TmnxIPsecPlcyParamsTblLastChangd_Type = TimeStamp
_TmnxIPsecPlcyParamsTblLastChangd_Object = MibScalar
tmnxIPsecPlcyParamsTblLastChangd = _TmnxIPsecPlcyParamsTblLastChangd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 10),
    _TmnxIPsecPlcyParamsTblLastChangd_Type()
)
tmnxIPsecPlcyParamsTblLastChangd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsTblLastChangd.setStatus("current")
_TmnxIPsecPolicyParamsTable_Object = MibTable
tmnxIPsecPolicyParamsTable = _TmnxIPsecPolicyParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11)
)
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsTable.setStatus("current")
_TmnxIPsecPolicyParamsEntry_Object = MibTableRow
tmnxIPsecPolicyParamsEntry = _TmnxIPsecPolicyParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1)
)
tmnxIPsecPolicyParamsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsId"),
)
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsEntry.setStatus("current")


class _TmnxIPsecPolicyParamsId_Type(Unsigned32):
    """Custom type tmnxIPsecPolicyParamsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxIPsecPolicyParamsId_Type.__name__ = "Unsigned32"
_TmnxIPsecPolicyParamsId_Object = MibTableColumn
tmnxIPsecPolicyParamsId = _TmnxIPsecPolicyParamsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 1),
    _TmnxIPsecPolicyParamsId_Type()
)
tmnxIPsecPolicyParamsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsId.setStatus("current")
_TmnxIPsecPolicyParamsRowStatus_Type = RowStatus
_TmnxIPsecPolicyParamsRowStatus_Object = MibTableColumn
tmnxIPsecPolicyParamsRowStatus = _TmnxIPsecPolicyParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 2),
    _TmnxIPsecPolicyParamsRowStatus_Type()
)
tmnxIPsecPolicyParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsRowStatus.setStatus("current")
_TmnxIPsecPolicyParamsLastChanged_Type = TimeStamp
_TmnxIPsecPolicyParamsLastChanged_Object = MibTableColumn
tmnxIPsecPolicyParamsLastChanged = _TmnxIPsecPolicyParamsLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 3),
    _TmnxIPsecPolicyParamsLastChanged_Type()
)
tmnxIPsecPolicyParamsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsLastChanged.setStatus("current")


class _TmnxIPsecPolicyParamsLclAddrAny_Type(TruthValue):
    """Custom type tmnxIPsecPolicyParamsLclAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxIPsecPolicyParamsLclAddrAny_Type.__name__ = "TruthValue"
_TmnxIPsecPolicyParamsLclAddrAny_Object = MibTableColumn
tmnxIPsecPolicyParamsLclAddrAny = _TmnxIPsecPolicyParamsLclAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 4),
    _TmnxIPsecPolicyParamsLclAddrAny_Type()
)
tmnxIPsecPolicyParamsLclAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsLclAddrAny.setStatus("current")


class _TmnxIPsecPolicyParamsLclAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecPolicyParamsLclAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecPolicyParamsLclAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecPolicyParamsLclAddrType_Object = MibTableColumn
tmnxIPsecPolicyParamsLclAddrType = _TmnxIPsecPolicyParamsLclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 5),
    _TmnxIPsecPolicyParamsLclAddrType_Type()
)
tmnxIPsecPolicyParamsLclAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsLclAddrType.setStatus("current")


class _TmnxIPsecPolicyParamsLclAddr_Type(InetAddress):
    """Custom type tmnxIPsecPolicyParamsLclAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecPolicyParamsLclAddr_Type.__name__ = "InetAddress"
_TmnxIPsecPolicyParamsLclAddr_Object = MibTableColumn
tmnxIPsecPolicyParamsLclAddr = _TmnxIPsecPolicyParamsLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 6),
    _TmnxIPsecPolicyParamsLclAddr_Type()
)
tmnxIPsecPolicyParamsLclAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsLclAddr.setStatus("current")


class _TmnxIPsecPolicyParamsLclAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxIPsecPolicyParamsLclAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxIPsecPolicyParamsLclAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxIPsecPolicyParamsLclAPrefLen_Object = MibTableColumn
tmnxIPsecPolicyParamsLclAPrefLen = _TmnxIPsecPolicyParamsLclAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 7),
    _TmnxIPsecPolicyParamsLclAPrefLen_Type()
)
tmnxIPsecPolicyParamsLclAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsLclAPrefLen.setStatus("current")


class _TmnxIPsecPolicyParamsRemAddrAny_Type(TruthValue):
    """Custom type tmnxIPsecPolicyParamsRemAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxIPsecPolicyParamsRemAddrAny_Type.__name__ = "TruthValue"
_TmnxIPsecPolicyParamsRemAddrAny_Object = MibTableColumn
tmnxIPsecPolicyParamsRemAddrAny = _TmnxIPsecPolicyParamsRemAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 8),
    _TmnxIPsecPolicyParamsRemAddrAny_Type()
)
tmnxIPsecPolicyParamsRemAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsRemAddrAny.setStatus("current")


class _TmnxIPsecPolicyParamsRemAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecPolicyParamsRemAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecPolicyParamsRemAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecPolicyParamsRemAddrType_Object = MibTableColumn
tmnxIPsecPolicyParamsRemAddrType = _TmnxIPsecPolicyParamsRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 9),
    _TmnxIPsecPolicyParamsRemAddrType_Type()
)
tmnxIPsecPolicyParamsRemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsRemAddrType.setStatus("current")


class _TmnxIPsecPolicyParamsRemAddr_Type(InetAddress):
    """Custom type tmnxIPsecPolicyParamsRemAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecPolicyParamsRemAddr_Type.__name__ = "InetAddress"
_TmnxIPsecPolicyParamsRemAddr_Object = MibTableColumn
tmnxIPsecPolicyParamsRemAddr = _TmnxIPsecPolicyParamsRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 10),
    _TmnxIPsecPolicyParamsRemAddr_Type()
)
tmnxIPsecPolicyParamsRemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsRemAddr.setStatus("current")


class _TmnxIPsecPolicyParamsRemAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxIPsecPolicyParamsRemAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TmnxIPsecPolicyParamsRemAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxIPsecPolicyParamsRemAPrefLen_Object = MibTableColumn
tmnxIPsecPolicyParamsRemAPrefLen = _TmnxIPsecPolicyParamsRemAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 11),
    _TmnxIPsecPolicyParamsRemAPrefLen_Type()
)
tmnxIPsecPolicyParamsRemAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPolicyParamsRemAPrefLen.setStatus("current")


class _TmnxIPsecPlcyParamsV6LclAddrAny_Type(TruthValue):
    """Custom type tmnxIPsecPlcyParamsV6LclAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxIPsecPlcyParamsV6LclAddrAny_Type.__name__ = "TruthValue"
_TmnxIPsecPlcyParamsV6LclAddrAny_Object = MibTableColumn
tmnxIPsecPlcyParamsV6LclAddrAny = _TmnxIPsecPlcyParamsV6LclAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 12),
    _TmnxIPsecPlcyParamsV6LclAddrAny_Type()
)
tmnxIPsecPlcyParamsV6LclAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6LclAddrAny.setStatus("current")


class _TmnxIPsecPlcyParamsV6LclAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecPlcyParamsV6LclAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecPlcyParamsV6LclAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecPlcyParamsV6LclAddrType_Object = MibTableColumn
tmnxIPsecPlcyParamsV6LclAddrType = _TmnxIPsecPlcyParamsV6LclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 13),
    _TmnxIPsecPlcyParamsV6LclAddrType_Type()
)
tmnxIPsecPlcyParamsV6LclAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6LclAddrType.setStatus("current")


class _TmnxIPsecPlcyParamsV6LclAddr_Type(InetAddress):
    """Custom type tmnxIPsecPlcyParamsV6LclAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecPlcyParamsV6LclAddr_Type.__name__ = "InetAddress"
_TmnxIPsecPlcyParamsV6LclAddr_Object = MibTableColumn
tmnxIPsecPlcyParamsV6LclAddr = _TmnxIPsecPlcyParamsV6LclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 14),
    _TmnxIPsecPlcyParamsV6LclAddr_Type()
)
tmnxIPsecPlcyParamsV6LclAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6LclAddr.setStatus("current")


class _TmnxIPsecPlcyParamsV6LclAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxIPsecPlcyParamsV6LclAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )


_TmnxIPsecPlcyParamsV6LclAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxIPsecPlcyParamsV6LclAPrefLen_Object = MibTableColumn
tmnxIPsecPlcyParamsV6LclAPrefLen = _TmnxIPsecPlcyParamsV6LclAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 15),
    _TmnxIPsecPlcyParamsV6LclAPrefLen_Type()
)
tmnxIPsecPlcyParamsV6LclAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6LclAPrefLen.setStatus("current")


class _TmnxIPsecPlcyParamsV6RemAddrAny_Type(TruthValue):
    """Custom type tmnxIPsecPlcyParamsV6RemAddrAny based on TruthValue"""
    defaultValue = 2


_TmnxIPsecPlcyParamsV6RemAddrAny_Type.__name__ = "TruthValue"
_TmnxIPsecPlcyParamsV6RemAddrAny_Object = MibTableColumn
tmnxIPsecPlcyParamsV6RemAddrAny = _TmnxIPsecPlcyParamsV6RemAddrAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 16),
    _TmnxIPsecPlcyParamsV6RemAddrAny_Type()
)
tmnxIPsecPlcyParamsV6RemAddrAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6RemAddrAny.setStatus("current")


class _TmnxIPsecPlcyParamsV6RemAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecPlcyParamsV6RemAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecPlcyParamsV6RemAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecPlcyParamsV6RemAddrType_Object = MibTableColumn
tmnxIPsecPlcyParamsV6RemAddrType = _TmnxIPsecPlcyParamsV6RemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 17),
    _TmnxIPsecPlcyParamsV6RemAddrType_Type()
)
tmnxIPsecPlcyParamsV6RemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6RemAddrType.setStatus("current")


class _TmnxIPsecPlcyParamsV6RemAddr_Type(InetAddress):
    """Custom type tmnxIPsecPlcyParamsV6RemAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxIPsecPlcyParamsV6RemAddr_Type.__name__ = "InetAddress"
_TmnxIPsecPlcyParamsV6RemAddr_Object = MibTableColumn
tmnxIPsecPlcyParamsV6RemAddr = _TmnxIPsecPlcyParamsV6RemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 18),
    _TmnxIPsecPlcyParamsV6RemAddr_Type()
)
tmnxIPsecPlcyParamsV6RemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6RemAddr.setStatus("current")


class _TmnxIPsecPlcyParamsV6RemAPrefLen_Type(InetAddressPrefixLength):
    """Custom type tmnxIPsecPlcyParamsV6RemAPrefLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )


_TmnxIPsecPlcyParamsV6RemAPrefLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxIPsecPlcyParamsV6RemAPrefLen_Object = MibTableColumn
tmnxIPsecPlcyParamsV6RemAPrefLen = _TmnxIPsecPlcyParamsV6RemAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 11, 1, 19),
    _TmnxIPsecPlcyParamsV6RemAPrefLen_Type()
)
tmnxIPsecPlcyParamsV6RemAPrefLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecPlcyParamsV6RemAPrefLen.setStatus("current")
_TmnxIPsecSATableLastChanged_Type = TimeStamp
_TmnxIPsecSATableLastChanged_Object = MibScalar
tmnxIPsecSATableLastChanged = _TmnxIPsecSATableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 12),
    _TmnxIPsecSATableLastChanged_Type()
)
tmnxIPsecSATableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSATableLastChanged.setStatus("current")
_TmnxIPsecSATable_Object = MibTable
tmnxIPsecSATable = _TmnxIPsecSATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13)
)
if mibBuilder.loadTexts:
    tmnxIPsecSATable.setStatus("current")
_TmnxIPsecSAEntry_Object = MibTableRow
tmnxIPsecSAEntry = _TmnxIPsecSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1)
)
tmnxIPsecSAEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSAIndex"),
)
if mibBuilder.loadTexts:
    tmnxIPsecSAEntry.setStatus("current")


class _TmnxIPsecSAId_Type(Unsigned32):
    """Custom type tmnxIPsecSAId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxIPsecSAId_Type.__name__ = "Unsigned32"
_TmnxIPsecSAId_Object = MibTableColumn
tmnxIPsecSAId = _TmnxIPsecSAId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 1),
    _TmnxIPsecSAId_Type()
)
tmnxIPsecSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecSAId.setStatus("current")


class _TmnxIPsecSAIndex_Type(Unsigned32):
    """Custom type tmnxIPsecSAIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxIPsecSAIndex_Type.__name__ = "Unsigned32"
_TmnxIPsecSAIndex_Object = MibTableColumn
tmnxIPsecSAIndex = _TmnxIPsecSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 2),
    _TmnxIPsecSAIndex_Type()
)
tmnxIPsecSAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecSAIndex.setStatus("current")
_TmnxIPsecSADirection_Type = TmnxIPsecDirection
_TmnxIPsecSADirection_Object = MibTableColumn
tmnxIPsecSADirection = _TmnxIPsecSADirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 3),
    _TmnxIPsecSADirection_Type()
)
tmnxIPsecSADirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecSADirection.setStatus("current")
_TmnxIPsecSARowStatus_Type = RowStatus
_TmnxIPsecSARowStatus_Object = MibTableColumn
tmnxIPsecSARowStatus = _TmnxIPsecSARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 4),
    _TmnxIPsecSARowStatus_Type()
)
tmnxIPsecSARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSARowStatus.setStatus("current")
_TmnxIPsecSALastChanged_Type = TimeStamp
_TmnxIPsecSALastChanged_Object = MibTableColumn
tmnxIPsecSALastChanged = _TmnxIPsecSALastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 5),
    _TmnxIPsecSALastChanged_Type()
)
tmnxIPsecSALastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSALastChanged.setStatus("current")
_TmnxIPsecSAType_Type = TmnxIPsecKeyingType
_TmnxIPsecSAType_Object = MibTableColumn
tmnxIPsecSAType = _TmnxIPsecSAType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 6),
    _TmnxIPsecSAType_Type()
)
tmnxIPsecSAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAType.setStatus("current")


class _TmnxIPsecSAEncryptionKey_Type(OctetString):
    """Custom type tmnxIPsecSAEncryptionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxIPsecSAEncryptionKey_Type.__name__ = "OctetString"
_TmnxIPsecSAEncryptionKey_Object = MibTableColumn
tmnxIPsecSAEncryptionKey = _TmnxIPsecSAEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 7),
    _TmnxIPsecSAEncryptionKey_Type()
)
tmnxIPsecSAEncryptionKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSAEncryptionKey.setStatus("current")


class _TmnxIPsecSAAuthenticationKey_Type(OctetString):
    """Custom type tmnxIPsecSAAuthenticationKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxIPsecSAAuthenticationKey_Type.__name__ = "OctetString"
_TmnxIPsecSAAuthenticationKey_Object = MibTableColumn
tmnxIPsecSAAuthenticationKey = _TmnxIPsecSAAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 8),
    _TmnxIPsecSAAuthenticationKey_Type()
)
tmnxIPsecSAAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSAAuthenticationKey.setStatus("current")


class _TmnxIPsecSASpi_Type(Unsigned32):
    """Custom type tmnxIPsecSASpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16383),
    )


_TmnxIPsecSASpi_Type.__name__ = "Unsigned32"
_TmnxIPsecSASpi_Object = MibTableColumn
tmnxIPsecSASpi = _TmnxIPsecSASpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 9),
    _TmnxIPsecSASpi_Type()
)
tmnxIPsecSASpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSASpi.setStatus("current")
_TmnxIPsecSAManualTransformId_Type = TmnxIPsecTransformIdOrZero
_TmnxIPsecSAManualTransformId_Object = MibTableColumn
tmnxIPsecSAManualTransformId = _TmnxIPsecSAManualTransformId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 10),
    _TmnxIPsecSAManualTransformId_Type()
)
tmnxIPsecSAManualTransformId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecSAManualTransformId.setStatus("current")
_TmnxIPsecSAAuthAlgorithm_Type = TmnxAuthAlgorithm
_TmnxIPsecSAAuthAlgorithm_Object = MibTableColumn
tmnxIPsecSAAuthAlgorithm = _TmnxIPsecSAAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 11),
    _TmnxIPsecSAAuthAlgorithm_Type()
)
tmnxIPsecSAAuthAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAAuthAlgorithm.setStatus("current")
_TmnxIPsecSAEncrAlgorithm_Type = TmnxEncrAlgorithm
_TmnxIPsecSAEncrAlgorithm_Object = MibTableColumn
tmnxIPsecSAEncrAlgorithm = _TmnxIPsecSAEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 12),
    _TmnxIPsecSAEncrAlgorithm_Type()
)
tmnxIPsecSAEncrAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAEncrAlgorithm.setStatus("current")
_TmnxIPsecSAStorageType_Type = StorageType
_TmnxIPsecSAStorageType_Object = MibTableColumn
tmnxIPsecSAStorageType = _TmnxIPsecSAStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 13),
    _TmnxIPsecSAStorageType_Type()
)
tmnxIPsecSAStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStorageType.setStatus("current")
_TmnxIPsecSAEstablishedTime_Type = TimeStamp
_TmnxIPsecSAEstablishedTime_Object = MibTableColumn
tmnxIPsecSAEstablishedTime = _TmnxIPsecSAEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 14),
    _TmnxIPsecSAEstablishedTime_Type()
)
tmnxIPsecSAEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAEstablishedTime.setStatus("current")
_TmnxIPsecSANegotiatedLifeTime_Type = Unsigned32
_TmnxIPsecSANegotiatedLifeTime_Object = MibTableColumn
tmnxIPsecSANegotiatedLifeTime = _TmnxIPsecSANegotiatedLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 13, 1, 15),
    _TmnxIPsecSANegotiatedLifeTime_Type()
)
tmnxIPsecSANegotiatedLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSANegotiatedLifeTime.setStatus("current")
_TmnxIPsecSAStatsTable_Object = MibTable
tmnxIPsecSAStatsTable = _TmnxIPsecSAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14)
)
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsTable.setStatus("current")
_TmnxIPsecSAStatsEntry_Object = MibTableRow
tmnxIPsecSAStatsEntry = _TmnxIPsecSAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1)
)
tmnxIPsecSAStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecSAIndex"),
)
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsEntry.setStatus("current")
_TmnxIPsecSAStatsBytesProcessed_Type = Counter64
_TmnxIPsecSAStatsBytesProcessed_Object = MibTableColumn
tmnxIPsecSAStatsBytesProcessed = _TmnxIPsecSAStatsBytesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 1),
    _TmnxIPsecSAStatsBytesProcessed_Type()
)
tmnxIPsecSAStatsBytesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsBytesProcessed.setStatus("current")
_TmnxIPsecSAStatsBytesProcLow32_Type = Counter32
_TmnxIPsecSAStatsBytesProcLow32_Object = MibTableColumn
tmnxIPsecSAStatsBytesProcLow32 = _TmnxIPsecSAStatsBytesProcLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 2),
    _TmnxIPsecSAStatsBytesProcLow32_Type()
)
tmnxIPsecSAStatsBytesProcLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsBytesProcLow32.setStatus("current")
_TmnxIPsecSAStatsBytesProcHigh32_Type = Counter32
_TmnxIPsecSAStatsBytesProcHigh32_Object = MibTableColumn
tmnxIPsecSAStatsBytesProcHigh32 = _TmnxIPsecSAStatsBytesProcHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 3),
    _TmnxIPsecSAStatsBytesProcHigh32_Type()
)
tmnxIPsecSAStatsBytesProcHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsBytesProcHigh32.setStatus("current")
_TmnxIPsecSAStatsPktsProcessed_Type = Counter64
_TmnxIPsecSAStatsPktsProcessed_Object = MibTableColumn
tmnxIPsecSAStatsPktsProcessed = _TmnxIPsecSAStatsPktsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 4),
    _TmnxIPsecSAStatsPktsProcessed_Type()
)
tmnxIPsecSAStatsPktsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPktsProcessed.setStatus("current")
_TmnxIPsecSAStatsPktsProcLow32_Type = Counter32
_TmnxIPsecSAStatsPktsProcLow32_Object = MibTableColumn
tmnxIPsecSAStatsPktsProcLow32 = _TmnxIPsecSAStatsPktsProcLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 5),
    _TmnxIPsecSAStatsPktsProcLow32_Type()
)
tmnxIPsecSAStatsPktsProcLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPktsProcLow32.setStatus("current")
_TmnxIPsecSAStatsPktsProcHigh32_Type = Counter32
_TmnxIPsecSAStatsPktsProcHigh32_Object = MibTableColumn
tmnxIPsecSAStatsPktsProcHigh32 = _TmnxIPsecSAStatsPktsProcHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 6),
    _TmnxIPsecSAStatsPktsProcHigh32_Type()
)
tmnxIPsecSAStatsPktsProcHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPktsProcHigh32.setStatus("current")
_TmnxIPsecSAStatsCryptoErrors_Type = Counter32
_TmnxIPsecSAStatsCryptoErrors_Object = MibTableColumn
tmnxIPsecSAStatsCryptoErrors = _TmnxIPsecSAStatsCryptoErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 7),
    _TmnxIPsecSAStatsCryptoErrors_Type()
)
tmnxIPsecSAStatsCryptoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsCryptoErrors.setStatus("current")
_TmnxIPsecSAStatsReplayErrors_Type = Counter32
_TmnxIPsecSAStatsReplayErrors_Object = MibTableColumn
tmnxIPsecSAStatsReplayErrors = _TmnxIPsecSAStatsReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 8),
    _TmnxIPsecSAStatsReplayErrors_Type()
)
tmnxIPsecSAStatsReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsReplayErrors.setStatus("current")
_TmnxIPsecSAStatsSAErrors_Type = Counter32
_TmnxIPsecSAStatsSAErrors_Object = MibTableColumn
tmnxIPsecSAStatsSAErrors = _TmnxIPsecSAStatsSAErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 9),
    _TmnxIPsecSAStatsSAErrors_Type()
)
tmnxIPsecSAStatsSAErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsSAErrors.setStatus("current")
_TmnxIPsecSAStatsPolicyErrors_Type = Counter32
_TmnxIPsecSAStatsPolicyErrors_Object = MibTableColumn
tmnxIPsecSAStatsPolicyErrors = _TmnxIPsecSAStatsPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 10),
    _TmnxIPsecSAStatsPolicyErrors_Type()
)
tmnxIPsecSAStatsPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPolicyErrors.setStatus("current")
_TmnxIPsecSAStatsEncapOverhead_Type = Counter32
_TmnxIPsecSAStatsEncapOverhead_Object = MibTableColumn
tmnxIPsecSAStatsEncapOverhead = _TmnxIPsecSAStatsEncapOverhead_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 11),
    _TmnxIPsecSAStatsEncapOverhead_Type()
)
tmnxIPsecSAStatsEncapOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsEncapOverhead.setStatus("current")
_TmnxIPsecSAStatsPreEncapFragCnt_Type = Counter64
_TmnxIPsecSAStatsPreEncapFragCnt_Object = MibTableColumn
tmnxIPsecSAStatsPreEncapFragCnt = _TmnxIPsecSAStatsPreEncapFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 12),
    _TmnxIPsecSAStatsPreEncapFragCnt_Type()
)
tmnxIPsecSAStatsPreEncapFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPreEncapFragCnt.setStatus("current")
_TmnxIPsecSAStatsPreEncapFragLtSz_Type = Unsigned32
_TmnxIPsecSAStatsPreEncapFragLtSz_Object = MibTableColumn
tmnxIPsecSAStatsPreEncapFragLtSz = _TmnxIPsecSAStatsPreEncapFragLtSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 13),
    _TmnxIPsecSAStatsPreEncapFragLtSz_Type()
)
tmnxIPsecSAStatsPreEncapFragLtSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPreEncapFragLtSz.setStatus("current")
_TmnxIPsecSAStatsPstEncapFragCnt_Type = Counter64
_TmnxIPsecSAStatsPstEncapFragCnt_Object = MibTableColumn
tmnxIPsecSAStatsPstEncapFragCnt = _TmnxIPsecSAStatsPstEncapFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 14),
    _TmnxIPsecSAStatsPstEncapFragCnt_Type()
)
tmnxIPsecSAStatsPstEncapFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPstEncapFragCnt.setStatus("current")
_TmnxIPsecSAStatsPstEncapFragLtSz_Type = Unsigned32
_TmnxIPsecSAStatsPstEncapFragLtSz_Object = MibTableColumn
tmnxIPsecSAStatsPstEncapFragLtSz = _TmnxIPsecSAStatsPstEncapFragLtSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 14, 1, 15),
    _TmnxIPsecSAStatsPstEncapFragLtSz_Type()
)
tmnxIPsecSAStatsPstEncapFragLtSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsPstEncapFragLtSz.setStatus("current")
_TmnxIPsecMdaDpStatsTable_Object = MibTable
tmnxIPsecMdaDpStatsTable = _TmnxIPsecMdaDpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15)
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsTable.setStatus("current")
_TmnxIPsecMdaDpStatsEntry_Object = MibTableRow
tmnxIPsecMdaDpStatsEntry = _TmnxIPsecMdaDpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1)
)
tmnxIPsecMdaDpStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEntry.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptPkts_Type = Counter64
_TmnxIPsecMdaDpStatsEncryptPkts_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptPkts = _TmnxIPsecMdaDpStatsEncryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 1),
    _TmnxIPsecMdaDpStatsEncryptPkts_Type()
)
tmnxIPsecMdaDpStatsEncryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptPkts.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptPktsLow32_Type = Counter32
_TmnxIPsecMdaDpStatsEncryptPktsLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptPktsLow32 = _TmnxIPsecMdaDpStatsEncryptPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 2),
    _TmnxIPsecMdaDpStatsEncryptPktsLow32_Type()
)
tmnxIPsecMdaDpStatsEncryptPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptPktsLow32.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptPktsHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsEncryptPktsHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptPktsHigh32 = _TmnxIPsecMdaDpStatsEncryptPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 3),
    _TmnxIPsecMdaDpStatsEncryptPktsHigh32_Type()
)
tmnxIPsecMdaDpStatsEncryptPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptPktsHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptBytes_Type = Counter64
_TmnxIPsecMdaDpStatsEncryptBytes_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptBytes = _TmnxIPsecMdaDpStatsEncryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 4),
    _TmnxIPsecMdaDpStatsEncryptBytes_Type()
)
tmnxIPsecMdaDpStatsEncryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptBytes.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptBytesLow32_Type = Counter32
_TmnxIPsecMdaDpStatsEncryptBytesLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptBytesLow32 = _TmnxIPsecMdaDpStatsEncryptBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 5),
    _TmnxIPsecMdaDpStatsEncryptBytesLow32_Type()
)
tmnxIPsecMdaDpStatsEncryptBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptBytesLow32.setStatus("current")
_TmnxIPsecMdaDpStatsEncryptBytesHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsEncryptBytesHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsEncryptBytesHigh32 = _TmnxIPsecMdaDpStatsEncryptBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 6),
    _TmnxIPsecMdaDpStatsEncryptBytesHigh32_Type()
)
tmnxIPsecMdaDpStatsEncryptBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsEncryptBytesHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptPkts_Type = Counter64
_TmnxIPsecMdaDpStatsDecryptPkts_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptPkts = _TmnxIPsecMdaDpStatsDecryptPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 7),
    _TmnxIPsecMdaDpStatsDecryptPkts_Type()
)
tmnxIPsecMdaDpStatsDecryptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptPkts.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptPktsLow32_Type = Counter32
_TmnxIPsecMdaDpStatsDecryptPktsLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptPktsLow32 = _TmnxIPsecMdaDpStatsDecryptPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 8),
    _TmnxIPsecMdaDpStatsDecryptPktsLow32_Type()
)
tmnxIPsecMdaDpStatsDecryptPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptPktsLow32.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptPktsHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsDecryptPktsHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptPktsHigh32 = _TmnxIPsecMdaDpStatsDecryptPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 9),
    _TmnxIPsecMdaDpStatsDecryptPktsHigh32_Type()
)
tmnxIPsecMdaDpStatsDecryptPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptPktsHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptBytes_Type = Counter64
_TmnxIPsecMdaDpStatsDecryptBytes_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptBytes = _TmnxIPsecMdaDpStatsDecryptBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 10),
    _TmnxIPsecMdaDpStatsDecryptBytes_Type()
)
tmnxIPsecMdaDpStatsDecryptBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptBytes.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptBytesLow32_Type = Counter32
_TmnxIPsecMdaDpStatsDecryptBytesLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptBytesLow32 = _TmnxIPsecMdaDpStatsDecryptBytesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 11),
    _TmnxIPsecMdaDpStatsDecryptBytesLow32_Type()
)
tmnxIPsecMdaDpStatsDecryptBytesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptBytesLow32.setStatus("current")
_TmnxIPsecMdaDpStatsDecryptBytesHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsDecryptBytesHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsDecryptBytesHigh32 = _TmnxIPsecMdaDpStatsDecryptBytesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 12),
    _TmnxIPsecMdaDpStatsDecryptBytesHigh32_Type()
)
tmnxIPsecMdaDpStatsDecryptBytesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsDecryptBytesHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsTxPktErrs_Type = Counter32
_TmnxIPsecMdaDpStatsTxPktErrs_Object = MibTableColumn
tmnxIPsecMdaDpStatsTxPktErrs = _TmnxIPsecMdaDpStatsTxPktErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 13),
    _TmnxIPsecMdaDpStatsTxPktErrs_Type()
)
tmnxIPsecMdaDpStatsTxPktErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsTxPktErrs.setStatus("current")
_TmnxIPsecMdaDpStatsOutBDropPkts_Type = Counter64
_TmnxIPsecMdaDpStatsOutBDropPkts_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBDropPkts = _TmnxIPsecMdaDpStatsOutBDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 14),
    _TmnxIPsecMdaDpStatsOutBDropPkts_Type()
)
tmnxIPsecMdaDpStatsOutBDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBDropPkts.setStatus("current")
_TmnxIPsecMdaDpStatsOutBDropPktsLow32_Type = Counter32
_TmnxIPsecMdaDpStatsOutBDropPktsLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBDropPktsLow32 = _TmnxIPsecMdaDpStatsOutBDropPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 15),
    _TmnxIPsecMdaDpStatsOutBDropPktsLow32_Type()
)
tmnxIPsecMdaDpStatsOutBDropPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBDropPktsLow32.setStatus("current")
_TmnxIPsecMdaDpStatsOutBDropPktsHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsOutBDropPktsHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBDropPktsHigh32 = _TmnxIPsecMdaDpStatsOutBDropPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 16),
    _TmnxIPsecMdaDpStatsOutBDropPktsHigh32_Type()
)
tmnxIPsecMdaDpStatsOutBDropPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBDropPktsHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsOutBSAMisses_Type = Counter64
_TmnxIPsecMdaDpStatsOutBSAMisses_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBSAMisses = _TmnxIPsecMdaDpStatsOutBSAMisses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 17),
    _TmnxIPsecMdaDpStatsOutBSAMisses_Type()
)
tmnxIPsecMdaDpStatsOutBSAMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBSAMisses.setStatus("current")
_TmnxIPsecMdaDpStatsOutBSAMissesLow32_Type = Counter32
_TmnxIPsecMdaDpStatsOutBSAMissesLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBSAMissesLow32 = _TmnxIPsecMdaDpStatsOutBSAMissesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 18),
    _TmnxIPsecMdaDpStatsOutBSAMissesLow32_Type()
)
tmnxIPsecMdaDpStatsOutBSAMissesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBSAMissesLow32.setStatus("current")
_TmnxIPsecMdaDpStatsOutBSAMissesHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsOutBSAMissesHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBSAMissesHigh32 = _TmnxIPsecMdaDpStatsOutBSAMissesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 19),
    _TmnxIPsecMdaDpStatsOutBSAMissesHigh32_Type()
)
tmnxIPsecMdaDpStatsOutBSAMissesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBSAMissesHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsOutBPolicyEntryMisses_Type = Counter32
_TmnxIPsecMdaDpStatsOutBPolicyEntryMisses_Object = MibTableColumn
tmnxIPsecMdaDpStatsOutBPolicyEntryMisses = _TmnxIPsecMdaDpStatsOutBPolicyEntryMisses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 20),
    _TmnxIPsecMdaDpStatsOutBPolicyEntryMisses_Type()
)
tmnxIPsecMdaDpStatsOutBPolicyEntryMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsOutBPolicyEntryMisses.setStatus("current")
_TmnxIPsecMdaDpStatsInBDropPkts_Type = Counter64
_TmnxIPsecMdaDpStatsInBDropPkts_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBDropPkts = _TmnxIPsecMdaDpStatsInBDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 21),
    _TmnxIPsecMdaDpStatsInBDropPkts_Type()
)
tmnxIPsecMdaDpStatsInBDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBDropPkts.setStatus("current")
_TmnxIPsecMdaDpStatsInBDropPktsLow32_Type = Counter32
_TmnxIPsecMdaDpStatsInBDropPktsLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBDropPktsLow32 = _TmnxIPsecMdaDpStatsInBDropPktsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 22),
    _TmnxIPsecMdaDpStatsInBDropPktsLow32_Type()
)
tmnxIPsecMdaDpStatsInBDropPktsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBDropPktsLow32.setStatus("current")
_TmnxIPsecMdaDpStatsInBDropPktsHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsInBDropPktsHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBDropPktsHigh32 = _TmnxIPsecMdaDpStatsInBDropPktsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 23),
    _TmnxIPsecMdaDpStatsInBDropPktsHigh32_Type()
)
tmnxIPsecMdaDpStatsInBDropPktsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBDropPktsHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsInBSAMisses_Type = Counter64
_TmnxIPsecMdaDpStatsInBSAMisses_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBSAMisses = _TmnxIPsecMdaDpStatsInBSAMisses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 24),
    _TmnxIPsecMdaDpStatsInBSAMisses_Type()
)
tmnxIPsecMdaDpStatsInBSAMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBSAMisses.setStatus("current")
_TmnxIPsecMdaDpStatsInBSAMissesLow32_Type = Counter32
_TmnxIPsecMdaDpStatsInBSAMissesLow32_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBSAMissesLow32 = _TmnxIPsecMdaDpStatsInBSAMissesLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 25),
    _TmnxIPsecMdaDpStatsInBSAMissesLow32_Type()
)
tmnxIPsecMdaDpStatsInBSAMissesLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBSAMissesLow32.setStatus("current")
_TmnxIPsecMdaDpStatsInBSAMissesHigh32_Type = Counter32
_TmnxIPsecMdaDpStatsInBSAMissesHigh32_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBSAMissesHigh32 = _TmnxIPsecMdaDpStatsInBSAMissesHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 26),
    _TmnxIPsecMdaDpStatsInBSAMissesHigh32_Type()
)
tmnxIPsecMdaDpStatsInBSAMissesHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBSAMissesHigh32.setStatus("current")
_TmnxIPsecMdaDpStatsInBIPDstSrcMismatches_Type = Counter32
_TmnxIPsecMdaDpStatsInBIPDstSrcMismatches_Object = MibTableColumn
tmnxIPsecMdaDpStatsInBIPDstSrcMismatches = _TmnxIPsecMdaDpStatsInBIPDstSrcMismatches_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 27),
    _TmnxIPsecMdaDpStatsInBIPDstSrcMismatches_Type()
)
tmnxIPsecMdaDpStatsInBIPDstSrcMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsInBIPDstSrcMismatches.setStatus("current")
_TmnxIPsecMdaDpInFragments_Type = Counter64
_TmnxIPsecMdaDpInFragments_Object = MibTableColumn
tmnxIPsecMdaDpInFragments = _TmnxIPsecMdaDpInFragments_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 28),
    _TmnxIPsecMdaDpInFragments_Type()
)
tmnxIPsecMdaDpInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpInFragments.setStatus("current")
_TmnxIPsecMdaDpInFragmentsLow32_Type = Counter32
_TmnxIPsecMdaDpInFragmentsLow32_Object = MibTableColumn
tmnxIPsecMdaDpInFragmentsLow32 = _TmnxIPsecMdaDpInFragmentsLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 29),
    _TmnxIPsecMdaDpInFragmentsLow32_Type()
)
tmnxIPsecMdaDpInFragmentsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpInFragmentsLow32.setStatus("current")
_TmnxIPsecMdaDpInFragmentsHigh32_Type = Counter32
_TmnxIPsecMdaDpInFragmentsHigh32_Object = MibTableColumn
tmnxIPsecMdaDpInFragmentsHigh32 = _TmnxIPsecMdaDpInFragmentsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 30),
    _TmnxIPsecMdaDpInFragmentsHigh32_Type()
)
tmnxIPsecMdaDpInFragmentsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpInFragmentsHigh32.setStatus("current")
_TmnxIPsecMdaDpPktsReassem_Type = Counter64
_TmnxIPsecMdaDpPktsReassem_Object = MibTableColumn
tmnxIPsecMdaDpPktsReassem = _TmnxIPsecMdaDpPktsReassem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 31),
    _TmnxIPsecMdaDpPktsReassem_Type()
)
tmnxIPsecMdaDpPktsReassem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsReassem.setStatus("current")
_TmnxIPsecMdaDpPktsReassemLow32_Type = Counter32
_TmnxIPsecMdaDpPktsReassemLow32_Object = MibTableColumn
tmnxIPsecMdaDpPktsReassemLow32 = _TmnxIPsecMdaDpPktsReassemLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 32),
    _TmnxIPsecMdaDpPktsReassemLow32_Type()
)
tmnxIPsecMdaDpPktsReassemLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsReassemLow32.setStatus("current")
_TmnxIPsecMdaDpPktsReassemHigh32_Type = Counter32
_TmnxIPsecMdaDpPktsReassemHigh32_Object = MibTableColumn
tmnxIPsecMdaDpPktsReassemHigh32 = _TmnxIPsecMdaDpPktsReassemHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 33),
    _TmnxIPsecMdaDpPktsReassemHigh32_Type()
)
tmnxIPsecMdaDpPktsReassemHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsReassemHigh32.setStatus("current")
_TmnxIPsecMdaDpFragDropTime_Type = Counter64
_TmnxIPsecMdaDpFragDropTime_Object = MibTableColumn
tmnxIPsecMdaDpFragDropTime = _TmnxIPsecMdaDpFragDropTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 34),
    _TmnxIPsecMdaDpFragDropTime_Type()
)
tmnxIPsecMdaDpFragDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDropTime.setStatus("current")
_TmnxIPsecMdaDpFragDropTimeLow32_Type = Counter32
_TmnxIPsecMdaDpFragDropTimeLow32_Object = MibTableColumn
tmnxIPsecMdaDpFragDropTimeLow32 = _TmnxIPsecMdaDpFragDropTimeLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 35),
    _TmnxIPsecMdaDpFragDropTimeLow32_Type()
)
tmnxIPsecMdaDpFragDropTimeLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDropTimeLow32.setStatus("current")
_TmnxIPsecMdaDpFragDropTimeHigh32_Type = Counter32
_TmnxIPsecMdaDpFragDropTimeHigh32_Object = MibTableColumn
tmnxIPsecMdaDpFragDropTimeHigh32 = _TmnxIPsecMdaDpFragDropTimeHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 36),
    _TmnxIPsecMdaDpFragDropTimeHigh32_Type()
)
tmnxIPsecMdaDpFragDropTimeHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDropTimeHigh32.setStatus("current")
_TmnxIPsecMdaDpFragDropped_Type = Counter64
_TmnxIPsecMdaDpFragDropped_Object = MibTableColumn
tmnxIPsecMdaDpFragDropped = _TmnxIPsecMdaDpFragDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 37),
    _TmnxIPsecMdaDpFragDropped_Type()
)
tmnxIPsecMdaDpFragDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDropped.setStatus("current")
_TmnxIPsecMdaDpFragDroppedLow32_Type = Counter32
_TmnxIPsecMdaDpFragDroppedLow32_Object = MibTableColumn
tmnxIPsecMdaDpFragDroppedLow32 = _TmnxIPsecMdaDpFragDroppedLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 38),
    _TmnxIPsecMdaDpFragDroppedLow32_Type()
)
tmnxIPsecMdaDpFragDroppedLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDroppedLow32.setStatus("current")
_TmnxIPsecMdaDpFragDroppedHigh32_Type = Counter32
_TmnxIPsecMdaDpFragDroppedHigh32_Object = MibTableColumn
tmnxIPsecMdaDpFragDroppedHigh32 = _TmnxIPsecMdaDpFragDroppedHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 39),
    _TmnxIPsecMdaDpFragDroppedHigh32_Type()
)
tmnxIPsecMdaDpFragDroppedHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpFragDroppedHigh32.setStatus("current")
_TmnxIPsecMdaDpGreTnlInPkts_Type = Counter64
_TmnxIPsecMdaDpGreTnlInPkts_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInPkts = _TmnxIPsecMdaDpGreTnlInPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 40),
    _TmnxIPsecMdaDpGreTnlInPkts_Type()
)
tmnxIPsecMdaDpGreTnlInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInPkts.setStatus("current")
_TmnxIPsecMdaDpGreTnlInPktsLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlInPktsLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInPktsLo = _TmnxIPsecMdaDpGreTnlInPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 41),
    _TmnxIPsecMdaDpGreTnlInPktsLo_Type()
)
tmnxIPsecMdaDpGreTnlInPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInPktsLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlInPktsHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlInPktsHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInPktsHi = _TmnxIPsecMdaDpGreTnlInPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 42),
    _TmnxIPsecMdaDpGreTnlInPktsHi_Type()
)
tmnxIPsecMdaDpGreTnlInPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInPktsHi.setStatus("current")
_TmnxIPsecMdaDpGreTnlInBytes_Type = Counter64
_TmnxIPsecMdaDpGreTnlInBytes_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInBytes = _TmnxIPsecMdaDpGreTnlInBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 43),
    _TmnxIPsecMdaDpGreTnlInBytes_Type()
)
tmnxIPsecMdaDpGreTnlInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInBytes.setStatus("current")
_TmnxIPsecMdaDpGreTnlInBytesLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlInBytesLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInBytesLo = _TmnxIPsecMdaDpGreTnlInBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 44),
    _TmnxIPsecMdaDpGreTnlInBytesLo_Type()
)
tmnxIPsecMdaDpGreTnlInBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInBytesLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlInBytesHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlInBytesHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInBytesHi = _TmnxIPsecMdaDpGreTnlInBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 45),
    _TmnxIPsecMdaDpGreTnlInBytesHi_Type()
)
tmnxIPsecMdaDpGreTnlInBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInBytesHi.setStatus("current")
_TmnxIPsecMdaDpGreTnlInErrs_Type = Counter64
_TmnxIPsecMdaDpGreTnlInErrs_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInErrs = _TmnxIPsecMdaDpGreTnlInErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 46),
    _TmnxIPsecMdaDpGreTnlInErrs_Type()
)
tmnxIPsecMdaDpGreTnlInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInErrs.setStatus("current")
_TmnxIPsecMdaDpGreTnlInErrsLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlInErrsLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInErrsLo = _TmnxIPsecMdaDpGreTnlInErrsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 47),
    _TmnxIPsecMdaDpGreTnlInErrsLo_Type()
)
tmnxIPsecMdaDpGreTnlInErrsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInErrsLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlInErrsHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlInErrsHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlInErrsHi = _TmnxIPsecMdaDpGreTnlInErrsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 48),
    _TmnxIPsecMdaDpGreTnlInErrsHi_Type()
)
tmnxIPsecMdaDpGreTnlInErrsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlInErrsHi.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutPkts_Type = Counter64
_TmnxIPsecMdaDpGreTnlOutPkts_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutPkts = _TmnxIPsecMdaDpGreTnlOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 49),
    _TmnxIPsecMdaDpGreTnlOutPkts_Type()
)
tmnxIPsecMdaDpGreTnlOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutPkts.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutPktsLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutPktsLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutPktsLo = _TmnxIPsecMdaDpGreTnlOutPktsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 50),
    _TmnxIPsecMdaDpGreTnlOutPktsLo_Type()
)
tmnxIPsecMdaDpGreTnlOutPktsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutPktsLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutPktsHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutPktsHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutPktsHi = _TmnxIPsecMdaDpGreTnlOutPktsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 51),
    _TmnxIPsecMdaDpGreTnlOutPktsHi_Type()
)
tmnxIPsecMdaDpGreTnlOutPktsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutPktsHi.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutBytes_Type = Counter64
_TmnxIPsecMdaDpGreTnlOutBytes_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutBytes = _TmnxIPsecMdaDpGreTnlOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 52),
    _TmnxIPsecMdaDpGreTnlOutBytes_Type()
)
tmnxIPsecMdaDpGreTnlOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutBytes.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutBytesLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutBytesLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutBytesLo = _TmnxIPsecMdaDpGreTnlOutBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 53),
    _TmnxIPsecMdaDpGreTnlOutBytesLo_Type()
)
tmnxIPsecMdaDpGreTnlOutBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutBytesLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutBytesHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutBytesHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutBytesHi = _TmnxIPsecMdaDpGreTnlOutBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 54),
    _TmnxIPsecMdaDpGreTnlOutBytesHi_Type()
)
tmnxIPsecMdaDpGreTnlOutBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutBytesHi.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutErrs_Type = Counter64
_TmnxIPsecMdaDpGreTnlOutErrs_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutErrs = _TmnxIPsecMdaDpGreTnlOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 55),
    _TmnxIPsecMdaDpGreTnlOutErrs_Type()
)
tmnxIPsecMdaDpGreTnlOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutErrs.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutErrsLo_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutErrsLo_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutErrsLo = _TmnxIPsecMdaDpGreTnlOutErrsLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 56),
    _TmnxIPsecMdaDpGreTnlOutErrsLo_Type()
)
tmnxIPsecMdaDpGreTnlOutErrsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutErrsLo.setStatus("current")
_TmnxIPsecMdaDpGreTnlOutErrsHi_Type = Counter32
_TmnxIPsecMdaDpGreTnlOutErrsHi_Object = MibTableColumn
tmnxIPsecMdaDpGreTnlOutErrsHi = _TmnxIPsecMdaDpGreTnlOutErrsHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 57),
    _TmnxIPsecMdaDpGreTnlOutErrsHi_Type()
)
tmnxIPsecMdaDpGreTnlOutErrsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGreTnlOutErrsHi.setStatus("current")
_TmnxIPsecMdaDpPktsDropDfSet_Type = Counter64
_TmnxIPsecMdaDpPktsDropDfSet_Object = MibTableColumn
tmnxIPsecMdaDpPktsDropDfSet = _TmnxIPsecMdaDpPktsDropDfSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 58),
    _TmnxIPsecMdaDpPktsDropDfSet_Type()
)
tmnxIPsecMdaDpPktsDropDfSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsDropDfSet.setStatus("current")
_TmnxIPsecMdaDpPktsDropDfSetLo_Type = Counter32
_TmnxIPsecMdaDpPktsDropDfSetLo_Object = MibTableColumn
tmnxIPsecMdaDpPktsDropDfSetLo = _TmnxIPsecMdaDpPktsDropDfSetLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 59),
    _TmnxIPsecMdaDpPktsDropDfSetLo_Type()
)
tmnxIPsecMdaDpPktsDropDfSetLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsDropDfSetLo.setStatus("current")
_TmnxIPsecMdaDpPktsDropDfSetHi_Type = Counter32
_TmnxIPsecMdaDpPktsDropDfSetHi_Object = MibTableColumn
tmnxIPsecMdaDpPktsDropDfSetHi = _TmnxIPsecMdaDpPktsDropDfSetHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 60),
    _TmnxIPsecMdaDpPktsDropDfSetHi_Type()
)
tmnxIPsecMdaDpPktsDropDfSetHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpPktsDropDfSetHi.setStatus("current")
_TmnxIPsecMdaDpStaticIPsecTnls_Type = Counter32
_TmnxIPsecMdaDpStaticIPsecTnls_Object = MibTableColumn
tmnxIPsecMdaDpStaticIPsecTnls = _TmnxIPsecMdaDpStaticIPsecTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 61),
    _TmnxIPsecMdaDpStaticIPsecTnls_Type()
)
tmnxIPsecMdaDpStaticIPsecTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStaticIPsecTnls.setStatus("current")
_TmnxIPsecMdaDpDynIPsecTnls_Type = Counter32
_TmnxIPsecMdaDpDynIPsecTnls_Object = MibTableColumn
tmnxIPsecMdaDpDynIPsecTnls = _TmnxIPsecMdaDpDynIPsecTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 62),
    _TmnxIPsecMdaDpDynIPsecTnls_Type()
)
tmnxIPsecMdaDpDynIPsecTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpDynIPsecTnls.setStatus("current")
_TmnxIPsecMdaDpIpGreTnls_Type = Counter32
_TmnxIPsecMdaDpIpGreTnls_Object = MibTableColumn
tmnxIPsecMdaDpIpGreTnls = _TmnxIPsecMdaDpIpGreTnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 63),
    _TmnxIPsecMdaDpIpGreTnls_Type()
)
tmnxIPsecMdaDpIpGreTnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpIpGreTnls.setStatus("current")
_TmnxIPsecMdaDpIpv4Tnls_Type = Counter32
_TmnxIPsecMdaDpIpv4Tnls_Object = MibTableColumn
tmnxIPsecMdaDpIpv4Tnls = _TmnxIPsecMdaDpIpv4Tnls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 15, 1, 64),
    _TmnxIPsecMdaDpIpv4Tnls_Type()
)
tmnxIPsecMdaDpIpv4Tnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpIpv4Tnls.setStatus("current")
_TIPsecTnlTempTblLastChanged_Type = TimeStamp
_TIPsecTnlTempTblLastChanged_Object = MibScalar
tIPsecTnlTempTblLastChanged = _TIPsecTnlTempTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 16),
    _TIPsecTnlTempTblLastChanged_Type()
)
tIPsecTnlTempTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTnlTempTblLastChanged.setStatus("current")
_TIPsecTnlTempTable_Object = MibTable
tIPsecTnlTempTable = _TIPsecTnlTempTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17)
)
if mibBuilder.loadTexts:
    tIPsecTnlTempTable.setStatus("current")
_TIPsecTnlTempEntry_Object = MibTableRow
tIPsecTnlTempEntry = _TIPsecTnlTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1)
)
tIPsecTnlTempEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTnlTempId"),
)
if mibBuilder.loadTexts:
    tIPsecTnlTempEntry.setStatus("current")
_TIPsecTnlTempId_Type = TmnxIPsecTunnelTemplateId
_TIPsecTnlTempId_Object = MibTableColumn
tIPsecTnlTempId = _TIPsecTnlTempId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 1),
    _TIPsecTnlTempId_Type()
)
tIPsecTnlTempId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTnlTempId.setStatus("current")
_TIPsecTnlTempRowStatus_Type = RowStatus
_TIPsecTnlTempRowStatus_Object = MibTableColumn
tIPsecTnlTempRowStatus = _TIPsecTnlTempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 2),
    _TIPsecTnlTempRowStatus_Type()
)
tIPsecTnlTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempRowStatus.setStatus("current")
_TIPsecTnlTempLastChanged_Type = TimeStamp
_TIPsecTnlTempLastChanged_Object = MibTableColumn
tIPsecTnlTempLastChanged = _TIPsecTnlTempLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 3),
    _TIPsecTnlTempLastChanged_Type()
)
tIPsecTnlTempLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTnlTempLastChanged.setStatus("current")


class _TIPsecTnlTempDescr_Type(TItemDescription):
    """Custom type tIPsecTnlTempDescr based on TItemDescription"""
    defaultValue = OctetString("")


_TIPsecTnlTempDescr_Type.__name__ = "TItemDescription"
_TIPsecTnlTempDescr_Object = MibTableColumn
tIPsecTnlTempDescr = _TIPsecTnlTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 4),
    _TIPsecTnlTempDescr_Type()
)
tIPsecTnlTempDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempDescr.setStatus("current")


class _TIPsecTnlTempReverseRoute_Type(Integer32):
    """Custom type tIPsecTnlTempReverseRoute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reverseRoute", 1),
          ("useSecurityPolicy", 2))
    )


_TIPsecTnlTempReverseRoute_Type.__name__ = "Integer32"
_TIPsecTnlTempReverseRoute_Object = MibTableColumn
tIPsecTnlTempReverseRoute = _TIPsecTnlTempReverseRoute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 5),
    _TIPsecTnlTempReverseRoute_Type()
)
tIPsecTnlTempReverseRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempReverseRoute.setStatus("current")


class _TIPsecTnlTempDynKeyTransformId1_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tIPsecTnlTempDynKeyTransformId1 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TIPsecTnlTempDynKeyTransformId1_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TIPsecTnlTempDynKeyTransformId1_Object = MibTableColumn
tIPsecTnlTempDynKeyTransformId1 = _TIPsecTnlTempDynKeyTransformId1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 6),
    _TIPsecTnlTempDynKeyTransformId1_Type()
)
tIPsecTnlTempDynKeyTransformId1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempDynKeyTransformId1.setStatus("current")


class _TIPsecTnlTempDynKeyTransformId2_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tIPsecTnlTempDynKeyTransformId2 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TIPsecTnlTempDynKeyTransformId2_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TIPsecTnlTempDynKeyTransformId2_Object = MibTableColumn
tIPsecTnlTempDynKeyTransformId2 = _TIPsecTnlTempDynKeyTransformId2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 7),
    _TIPsecTnlTempDynKeyTransformId2_Type()
)
tIPsecTnlTempDynKeyTransformId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempDynKeyTransformId2.setStatus("current")


class _TIPsecTnlTempDynKeyTransformId3_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tIPsecTnlTempDynKeyTransformId3 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TIPsecTnlTempDynKeyTransformId3_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TIPsecTnlTempDynKeyTransformId3_Object = MibTableColumn
tIPsecTnlTempDynKeyTransformId3 = _TIPsecTnlTempDynKeyTransformId3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 8),
    _TIPsecTnlTempDynKeyTransformId3_Type()
)
tIPsecTnlTempDynKeyTransformId3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempDynKeyTransformId3.setStatus("current")


class _TIPsecTnlTempDynKeyTransformId4_Type(TmnxIPsecTransformIdOrZero):
    """Custom type tIPsecTnlTempDynKeyTransformId4 based on TmnxIPsecTransformIdOrZero"""
    defaultValue = 0


_TIPsecTnlTempDynKeyTransformId4_Type.__name__ = "TmnxIPsecTransformIdOrZero"
_TIPsecTnlTempDynKeyTransformId4_Object = MibTableColumn
tIPsecTnlTempDynKeyTransformId4 = _TIPsecTnlTempDynKeyTransformId4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 9),
    _TIPsecTnlTempDynKeyTransformId4_Type()
)
tIPsecTnlTempDynKeyTransformId4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempDynKeyTransformId4.setStatus("current")


class _TIPsecTnlTempReplayWindow_Type(Unsigned32):
    """Custom type tIPsecTnlTempReplayWindow based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
    )


_TIPsecTnlTempReplayWindow_Type.__name__ = "Unsigned32"
_TIPsecTnlTempReplayWindow_Object = MibTableColumn
tIPsecTnlTempReplayWindow = _TIPsecTnlTempReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 10),
    _TIPsecTnlTempReplayWindow_Type()
)
tIPsecTnlTempReplayWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempReplayWindow.setStatus("current")


class _TIPsecTnlTempIpMtu_Type(Unsigned32):
    """Custom type tIPsecTnlTempIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TIPsecTnlTempIpMtu_Type.__name__ = "Unsigned32"
_TIPsecTnlTempIpMtu_Object = MibTableColumn
tIPsecTnlTempIpMtu = _TIPsecTnlTempIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 11),
    _TIPsecTnlTempIpMtu_Type()
)
tIPsecTnlTempIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempIpMtu.setStatus("current")


class _TIPsecTnlTempEncapIpMtu_Type(Unsigned32):
    """Custom type tIPsecTnlTempEncapIpMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TIPsecTnlTempEncapIpMtu_Type.__name__ = "Unsigned32"
_TIPsecTnlTempEncapIpMtu_Object = MibTableColumn
tIPsecTnlTempEncapIpMtu = _TIPsecTnlTempEncapIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 12),
    _TIPsecTnlTempEncapIpMtu_Type()
)
tIPsecTnlTempEncapIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempEncapIpMtu.setStatus("current")


class _TIPsecTnlTempIcmp6Pkt2Big_Type(TruthValue):
    """Custom type tIPsecTnlTempIcmp6Pkt2Big based on TruthValue"""
    defaultValue = 1


_TIPsecTnlTempIcmp6Pkt2Big_Type.__name__ = "TruthValue"
_TIPsecTnlTempIcmp6Pkt2Big_Object = MibTableColumn
tIPsecTnlTempIcmp6Pkt2Big = _TIPsecTnlTempIcmp6Pkt2Big_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 14),
    _TIPsecTnlTempIcmp6Pkt2Big_Type()
)
tIPsecTnlTempIcmp6Pkt2Big.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempIcmp6Pkt2Big.setStatus("current")


class _TIPsecTnlTempIcmp6NumPkt2Big_Type(Unsigned32):
    """Custom type tIPsecTnlTempIcmp6NumPkt2Big based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TIPsecTnlTempIcmp6NumPkt2Big_Type.__name__ = "Unsigned32"
_TIPsecTnlTempIcmp6NumPkt2Big_Object = MibTableColumn
tIPsecTnlTempIcmp6NumPkt2Big = _TIPsecTnlTempIcmp6NumPkt2Big_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 15),
    _TIPsecTnlTempIcmp6NumPkt2Big_Type()
)
tIPsecTnlTempIcmp6NumPkt2Big.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempIcmp6NumPkt2Big.setStatus("current")


class _TIPsecTnlTempIcmp6Pkt2BigTime_Type(Unsigned32):
    """Custom type tIPsecTnlTempIcmp6Pkt2BigTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TIPsecTnlTempIcmp6Pkt2BigTime_Type.__name__ = "Unsigned32"
_TIPsecTnlTempIcmp6Pkt2BigTime_Object = MibTableColumn
tIPsecTnlTempIcmp6Pkt2BigTime = _TIPsecTnlTempIcmp6Pkt2BigTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 16),
    _TIPsecTnlTempIcmp6Pkt2BigTime_Type()
)
tIPsecTnlTempIcmp6Pkt2BigTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempIcmp6Pkt2BigTime.setStatus("current")
if mibBuilder.loadTexts:
    tIPsecTnlTempIcmp6Pkt2BigTime.setUnits("seconds")


class _TIPsecTnlTempClearDfBit_Type(TruthValue):
    """Custom type tIPsecTnlTempClearDfBit based on TruthValue"""
    defaultValue = 2


_TIPsecTnlTempClearDfBit_Type.__name__ = "TruthValue"
_TIPsecTnlTempClearDfBit_Object = MibTableColumn
tIPsecTnlTempClearDfBit = _TIPsecTnlTempClearDfBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 17, 1, 17),
    _TIPsecTnlTempClearDfBit_Type()
)
tIPsecTnlTempClearDfBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTnlTempClearDfBit.setStatus("current")
_TmnxIPsecGWTblLastChgd_Type = TimeStamp
_TmnxIPsecGWTblLastChgd_Object = MibScalar
tmnxIPsecGWTblLastChgd = _TmnxIPsecGWTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 18),
    _TmnxIPsecGWTblLastChgd_Type()
)
tmnxIPsecGWTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWTblLastChgd.setStatus("current")
_TmnxIPsecGWTable_Object = MibTable
tmnxIPsecGWTable = _TmnxIPsecGWTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19)
)
if mibBuilder.loadTexts:
    tmnxIPsecGWTable.setStatus("current")
_TmnxIPsecGWEntry_Object = MibTableRow
tmnxIPsecGWEntry = _TmnxIPsecGWEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1)
)
tmnxIPsecGWEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    tmnxIPsecGWEntry.setStatus("current")
_TmnxIPsecGWRowStatus_Type = RowStatus
_TmnxIPsecGWRowStatus_Object = MibTableColumn
tmnxIPsecGWRowStatus = _TmnxIPsecGWRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 1),
    _TmnxIPsecGWRowStatus_Type()
)
tmnxIPsecGWRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWRowStatus.setStatus("current")
_TmnxIPsecGWLastMgmtChange_Type = TimeStamp
_TmnxIPsecGWLastMgmtChange_Object = MibTableColumn
tmnxIPsecGWLastMgmtChange = _TmnxIPsecGWLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 2),
    _TmnxIPsecGWLastMgmtChange_Type()
)
tmnxIPsecGWLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWLastMgmtChange.setStatus("current")


class _TmnxIPsecGWAdminState_Type(TmnxAdminState):
    """Custom type tmnxIPsecGWAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxIPsecGWAdminState_Type.__name__ = "TmnxAdminState"
_TmnxIPsecGWAdminState_Object = MibTableColumn
tmnxIPsecGWAdminState = _TmnxIPsecGWAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 3),
    _TmnxIPsecGWAdminState_Type()
)
tmnxIPsecGWAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWAdminState.setStatus("current")
_TmnxIPsecGWOperState_Type = TmnxOperState
_TmnxIPsecGWOperState_Object = MibTableColumn
tmnxIPsecGWOperState = _TmnxIPsecGWOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 4),
    _TmnxIPsecGWOperState_Type()
)
tmnxIPsecGWOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWOperState.setStatus("current")


class _TmnxIPsecGWTunnelPolicyTemp_Type(TmnxIPsecTunnelTemplateIdOrZero):
    """Custom type tmnxIPsecGWTunnelPolicyTemp based on TmnxIPsecTunnelTemplateIdOrZero"""
    defaultValue = 0


_TmnxIPsecGWTunnelPolicyTemp_Type.__name__ = "TmnxIPsecTunnelTemplateIdOrZero"
_TmnxIPsecGWTunnelPolicyTemp_Object = MibTableColumn
tmnxIPsecGWTunnelPolicyTemp = _TmnxIPsecGWTunnelPolicyTemp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 5),
    _TmnxIPsecGWTunnelPolicyTemp_Type()
)
tmnxIPsecGWTunnelPolicyTemp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWTunnelPolicyTemp.setStatus("current")


class _TmnxIPsecGWSecureService_Type(TmnxServId):
    """Custom type tmnxIPsecGWSecureService based on TmnxServId"""
    defaultValue = 0


_TmnxIPsecGWSecureService_Type.__name__ = "TmnxServId"
_TmnxIPsecGWSecureService_Object = MibTableColumn
tmnxIPsecGWSecureService = _TmnxIPsecGWSecureService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 6),
    _TmnxIPsecGWSecureService_Type()
)
tmnxIPsecGWSecureService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWSecureService.setStatus("current")


class _TmnxIPsecGWIfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWIfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWIfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWIfName_Object = MibTableColumn
tmnxIPsecGWIfName = _TmnxIPsecGWIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 7),
    _TmnxIPsecGWIfName_Type()
)
tmnxIPsecGWIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWIfName.setStatus("current")


class _TmnxIPsecGWInetAddrType_Type(InetAddressType):
    """Custom type tmnxIPsecGWInetAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxIPsecGWInetAddrType_Type.__name__ = "InetAddressType"
_TmnxIPsecGWInetAddrType_Object = MibTableColumn
tmnxIPsecGWInetAddrType = _TmnxIPsecGWInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 8),
    _TmnxIPsecGWInetAddrType_Type()
)
tmnxIPsecGWInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWInetAddrType.setStatus("current")


class _TmnxIPsecGWInetAddress_Type(InetAddress):
    """Custom type tmnxIPsecGWInetAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecGWInetAddress_Type.__name__ = "InetAddress"
_TmnxIPsecGWInetAddress_Object = MibTableColumn
tmnxIPsecGWInetAddress = _TmnxIPsecGWInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 9),
    _TmnxIPsecGWInetAddress_Type()
)
tmnxIPsecGWInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWInetAddress.setStatus("current")


class _TmnxIPsecGWIkePolicyId_Type(TmnxIkePolicyIdOrZero):
    """Custom type tmnxIPsecGWIkePolicyId based on TmnxIkePolicyIdOrZero"""
    defaultValue = 0


_TmnxIPsecGWIkePolicyId_Type.__name__ = "TmnxIkePolicyIdOrZero"
_TmnxIPsecGWIkePolicyId_Object = MibTableColumn
tmnxIPsecGWIkePolicyId = _TmnxIPsecGWIkePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 10),
    _TmnxIPsecGWIkePolicyId_Type()
)
tmnxIPsecGWIkePolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWIkePolicyId.setStatus("current")


class _TmnxIPsecGWIkePreShared_Type(OctetString):
    """Custom type tmnxIPsecGWIkePreShared based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TmnxIPsecGWIkePreShared_Type.__name__ = "OctetString"
_TmnxIPsecGWIkePreShared_Object = MibTableColumn
tmnxIPsecGWIkePreShared = _TmnxIPsecGWIkePreShared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 11),
    _TmnxIPsecGWIkePreShared_Type()
)
tmnxIPsecGWIkePreShared.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWIkePreShared.setStatus("current")


class _TmnxIPsecGWLclX509Cert_Type(DisplayString):
    """Custom type tmnxIPsecGWLclX509Cert based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxIPsecGWLclX509Cert_Type.__name__ = "DisplayString"
_TmnxIPsecGWLclX509Cert_Object = MibTableColumn
tmnxIPsecGWLclX509Cert = _TmnxIPsecGWLclX509Cert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 12),
    _TmnxIPsecGWLclX509Cert_Type()
)
tmnxIPsecGWLclX509Cert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWLclX509Cert.setStatus("current")


class _TmnxIPsecGWLclPrivateKey_Type(DisplayString):
    """Custom type tmnxIPsecGWLclPrivateKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxIPsecGWLclPrivateKey_Type.__name__ = "DisplayString"
_TmnxIPsecGWLclPrivateKey_Object = MibTableColumn
tmnxIPsecGWLclPrivateKey = _TmnxIPsecGWLclPrivateKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 13),
    _TmnxIPsecGWLclPrivateKey_Type()
)
tmnxIPsecGWLclPrivateKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWLclPrivateKey.setStatus("current")


class _TmnxIPsecGWOperFlags_Type(Bits):
    """Custom type tmnxIPsecGWOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("localIpUnreachable", 0),
          ("gatewayAdminDown", 1),
          ("x509CertUnavailable", 2),
          ("privateKeyUnavailable", 3),
          ("caCertUnavailable", 4),
          ("caCRLUnavailable", 5),
          ("trustAnchorsDown", 6),
          ("certProfileDown", 7),
          ("invalidCertKeyCombo", 8))
    )

_TmnxIPsecGWOperFlags_Type.__name__ = "Bits"
_TmnxIPsecGWOperFlags_Object = MibTableColumn
tmnxIPsecGWOperFlags = _TmnxIPsecGWOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 14),
    _TmnxIPsecGWOperFlags_Type()
)
tmnxIPsecGWOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWOperFlags.setStatus("current")


class _TmnxIPsecGWCACert_Type(DisplayString):
    """Custom type tmnxIPsecGWCACert based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxIPsecGWCACert_Type.__name__ = "DisplayString"
_TmnxIPsecGWCACert_Object = MibTableColumn
tmnxIPsecGWCACert = _TmnxIPsecGWCACert_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 15),
    _TmnxIPsecGWCACert_Type()
)
tmnxIPsecGWCACert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCACert.setStatus("obsolete")


class _TmnxIPsecGWCACertRevocList_Type(DisplayString):
    """Custom type tmnxIPsecGWCACertRevocList based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 180),
    )


_TmnxIPsecGWCACertRevocList_Type.__name__ = "DisplayString"
_TmnxIPsecGWCACertRevocList_Object = MibTableColumn
tmnxIPsecGWCACertRevocList = _TmnxIPsecGWCACertRevocList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 16),
    _TmnxIPsecGWCACertRevocList_Type()
)
tmnxIPsecGWCACertRevocList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCACertRevocList.setStatus("obsolete")
_TmnxIPsecGWName_Type = TNamedItem
_TmnxIPsecGWName_Object = MibTableColumn
tmnxIPsecGWName = _TmnxIPsecGWName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 17),
    _TmnxIPsecGWName_Type()
)
tmnxIPsecGWName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWName.setStatus("current")


class _TmnxIPsecGWCertTrustAnchor_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWCertTrustAnchor based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWCertTrustAnchor_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWCertTrustAnchor_Object = MibTableColumn
tmnxIPsecGWCertTrustAnchor = _TmnxIPsecGWCertTrustAnchor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 18),
    _TmnxIPsecGWCertTrustAnchor_Type()
)
tmnxIPsecGWCertTrustAnchor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCertTrustAnchor.setStatus("current")


class _TmnxIPsecGWLocalIdType_Type(TmnxIPsecLocalIdType):
    """Custom type tmnxIPsecGWLocalIdType based on TmnxIPsecLocalIdType"""
    defaultValue = 0


_TmnxIPsecGWLocalIdType_Type.__name__ = "TmnxIPsecLocalIdType"
_TmnxIPsecGWLocalIdType_Object = MibTableColumn
tmnxIPsecGWLocalIdType = _TmnxIPsecGWLocalIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 19),
    _TmnxIPsecGWLocalIdType_Type()
)
tmnxIPsecGWLocalIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWLocalIdType.setStatus("current")


class _TmnxIPsecGWLocalIdValue_Type(DisplayString):
    """Custom type tmnxIPsecGWLocalIdValue based on DisplayString"""
    defaultHexValue = ""


_TmnxIPsecGWLocalIdValue_Type.__name__ = "DisplayString"
_TmnxIPsecGWLocalIdValue_Object = MibTableColumn
tmnxIPsecGWLocalIdValue = _TmnxIPsecGWLocalIdValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 20),
    _TmnxIPsecGWLocalIdValue_Type()
)
tmnxIPsecGWLocalIdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWLocalIdValue.setStatus("current")


class _TmnxIPsecGWCSVPrimary_Type(TmnxCertRevStatus):
    """Custom type tmnxIPsecGWCSVPrimary based on TmnxCertRevStatus"""
    defaultValue = 1


_TmnxIPsecGWCSVPrimary_Type.__name__ = "TmnxCertRevStatus"
_TmnxIPsecGWCSVPrimary_Object = MibTableColumn
tmnxIPsecGWCSVPrimary = _TmnxIPsecGWCSVPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 21),
    _TmnxIPsecGWCSVPrimary_Type()
)
tmnxIPsecGWCSVPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCSVPrimary.setStatus("current")


class _TmnxIPsecGWCSVSecondary_Type(TmnxCertRevStatusOrNone):
    """Custom type tmnxIPsecGWCSVSecondary based on TmnxCertRevStatusOrNone"""
    defaultValue = 0


_TmnxIPsecGWCSVSecondary_Type.__name__ = "TmnxCertRevStatusOrNone"
_TmnxIPsecGWCSVSecondary_Object = MibTableColumn
tmnxIPsecGWCSVSecondary = _TmnxIPsecGWCSVSecondary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 22),
    _TmnxIPsecGWCSVSecondary_Type()
)
tmnxIPsecGWCSVSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCSVSecondary.setStatus("current")


class _TmnxIPsecGWCSVDefResult_Type(Integer32):
    """Custom type tmnxIPsecGWCSVDefResult based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("revoked", 0),
          ("good", 1))
    )


_TmnxIPsecGWCSVDefResult_Type.__name__ = "Integer32"
_TmnxIPsecGWCSVDefResult_Object = MibTableColumn
tmnxIPsecGWCSVDefResult = _TmnxIPsecGWCSVDefResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 23),
    _TmnxIPsecGWCSVDefResult_Type()
)
tmnxIPsecGWCSVDefResult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCSVDefResult.setStatus("current")


class _TmnxIPsecGWRadAcctgPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWRadAcctgPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWRadAcctgPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWRadAcctgPolicy_Object = MibTableColumn
tmnxIPsecGWRadAcctgPolicy = _TmnxIPsecGWRadAcctgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 24),
    _TmnxIPsecGWRadAcctgPolicy_Type()
)
tmnxIPsecGWRadAcctgPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWRadAcctgPolicy.setStatus("current")


class _TmnxIPsecGWRadAuthPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWRadAuthPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWRadAuthPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWRadAuthPolicy_Object = MibTableColumn
tmnxIPsecGWRadAuthPolicy = _TmnxIPsecGWRadAuthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 25),
    _TmnxIPsecGWRadAuthPolicy_Type()
)
tmnxIPsecGWRadAuthPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWRadAuthPolicy.setStatus("current")


class _TmnxIPsecGWCertProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWCertProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWCertProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWCertProfile_Object = MibTableColumn
tmnxIPsecGWCertProfile = _TmnxIPsecGWCertProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 26),
    _TmnxIPsecGWCertProfile_Type()
)
tmnxIPsecGWCertProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCertProfile.setStatus("current")


class _TmnxIPsecGWCertTrstAnchrProf_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecGWCertTrstAnchrProf based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxIPsecGWCertTrstAnchrProf_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecGWCertTrstAnchrProf_Object = MibTableColumn
tmnxIPsecGWCertTrstAnchrProf = _TmnxIPsecGWCertTrstAnchrProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 19, 1, 27),
    _TmnxIPsecGWCertTrstAnchrProf_Type()
)
tmnxIPsecGWCertTrstAnchrProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecGWCertTrstAnchrProf.setStatus("current")
_TIPsecRUTnlTable_Object = MibTable
tIPsecRUTnlTable = _TIPsecRUTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20)
)
if mibBuilder.loadTexts:
    tIPsecRUTnlTable.setStatus("current")
_TIPsecRUTnlEntry_Object = MibTableRow
tIPsecRUTnlEntry = _TIPsecRUTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1)
)
tIPsecRUTnlEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
)
if mibBuilder.loadTexts:
    tIPsecRUTnlEntry.setStatus("current")
_TIPsecRUTnlInetAddrType_Type = InetAddressType
_TIPsecRUTnlInetAddrType_Object = MibTableColumn
tIPsecRUTnlInetAddrType = _TIPsecRUTnlInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 1),
    _TIPsecRUTnlInetAddrType_Type()
)
tIPsecRUTnlInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUTnlInetAddrType.setStatus("current")


class _TIPsecRUTnlInetAddress_Type(InetAddress):
    """Custom type tIPsecRUTnlInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUTnlInetAddress_Type.__name__ = "InetAddress"
_TIPsecRUTnlInetAddress_Object = MibTableColumn
tIPsecRUTnlInetAddress = _TIPsecRUTnlInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 2),
    _TIPsecRUTnlInetAddress_Type()
)
tIPsecRUTnlInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUTnlInetAddress.setStatus("current")
_TIPsecRUTnlPort_Type = TTcpUdpPort
_TIPsecRUTnlPort_Object = MibTableColumn
tIPsecRUTnlPort = _TIPsecRUTnlPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 3),
    _TIPsecRUTnlPort_Type()
)
tIPsecRUTnlPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUTnlPort.setStatus("current")
_TIPsecRUTnlPrivateIpAddrType_Type = InetAddressType
_TIPsecRUTnlPrivateIpAddrType_Object = MibTableColumn
tIPsecRUTnlPrivateIpAddrType = _TIPsecRUTnlPrivateIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 4),
    _TIPsecRUTnlPrivateIpAddrType_Type()
)
tIPsecRUTnlPrivateIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIpAddrType.setStatus("current")


class _TIPsecRUTnlPrivateIpAddr_Type(InetAddress):
    """Custom type tIPsecRUTnlPrivateIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUTnlPrivateIpAddr_Type.__name__ = "InetAddress"
_TIPsecRUTnlPrivateIpAddr_Object = MibTableColumn
tIPsecRUTnlPrivateIpAddr = _TIPsecRUTnlPrivateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 5),
    _TIPsecRUTnlPrivateIpAddr_Type()
)
tIPsecRUTnlPrivateIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIpAddr.setStatus("current")
_TIPsecRUTnlPrivateIpPrefixLen_Type = InetAddressPrefixLength
_TIPsecRUTnlPrivateIpPrefixLen_Object = MibTableColumn
tIPsecRUTnlPrivateIpPrefixLen = _TIPsecRUTnlPrivateIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 6),
    _TIPsecRUTnlPrivateIpPrefixLen_Type()
)
tIPsecRUTnlPrivateIpPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIpPrefixLen.setStatus("current")
_TIPsecRUTnlTempId_Type = TmnxIPsecTunnelTemplateId
_TIPsecRUTnlTempId_Object = MibTableColumn
tIPsecRUTnlTempId = _TIPsecRUTnlTempId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 7),
    _TIPsecRUTnlTempId_Type()
)
tIPsecRUTnlTempId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlTempId.setStatus("current")


class _TIPsecRUTnlIPsecSALifeTime_Type(Unsigned32):
    """Custom type tIPsecRUTnlIPsecSALifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 172800),
    )


_TIPsecRUTnlIPsecSALifeTime_Type.__name__ = "Unsigned32"
_TIPsecRUTnlIPsecSALifeTime_Object = MibTableColumn
tIPsecRUTnlIPsecSALifeTime = _TIPsecRUTnlIPsecSALifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 8),
    _TIPsecRUTnlIPsecSALifeTime_Type()
)
tIPsecRUTnlIPsecSALifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlIPsecSALifeTime.setStatus("current")
if mibBuilder.loadTexts:
    tIPsecRUTnlIPsecSALifeTime.setUnits("seconds")
_TIPsecRUTnlPfsDHGroup_Type = TmnxIkePolicyDHGroupOrZero
_TIPsecRUTnlPfsDHGroup_Object = MibTableColumn
tIPsecRUTnlPfsDHGroup = _TIPsecRUTnlPfsDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 9),
    _TIPsecRUTnlPfsDHGroup_Type()
)
tIPsecRUTnlPfsDHGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPfsDHGroup.setStatus("current")


class _TIPsecRUTnlReplayWindow_Type(Unsigned32):
    """Custom type tIPsecRUTnlReplayWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
    )


_TIPsecRUTnlReplayWindow_Type.__name__ = "Unsigned32"
_TIPsecRUTnlReplayWindow_Object = MibTableColumn
tIPsecRUTnlReplayWindow = _TIPsecRUTnlReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 10),
    _TIPsecRUTnlReplayWindow_Type()
)
tIPsecRUTnlReplayWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlReplayWindow.setStatus("current")
_TIPsecRUTnlPrivateSvcId_Type = TmnxServId
_TIPsecRUTnlPrivateSvcId_Object = MibTableColumn
tIPsecRUTnlPrivateSvcId = _TIPsecRUTnlPrivateSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 11),
    _TIPsecRUTnlPrivateSvcId_Type()
)
tIPsecRUTnlPrivateSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateSvcId.setStatus("current")
_TIPsecRUTnlPrivateIfIndex_Type = InterfaceIndex
_TIPsecRUTnlPrivateIfIndex_Object = MibTableColumn
tIPsecRUTnlPrivateIfIndex = _TIPsecRUTnlPrivateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 12),
    _TIPsecRUTnlPrivateIfIndex_Type()
)
tIPsecRUTnlPrivateIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlPrivateIfIndex.setStatus("current")
_TIPsecRUTnlHasBiDirectionalSA_Type = TruthValue
_TIPsecRUTnlHasBiDirectionalSA_Object = MibTableColumn
tIPsecRUTnlHasBiDirectionalSA = _TIPsecRUTnlHasBiDirectionalSA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 13),
    _TIPsecRUTnlHasBiDirectionalSA_Type()
)
tIPsecRUTnlHasBiDirectionalSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlHasBiDirectionalSA.setStatus("current")
_TIPsecRUTnlHostISA_Type = TmnxHwIndexOrZero
_TIPsecRUTnlHostISA_Object = MibTableColumn
tIPsecRUTnlHostISA = _TIPsecRUTnlHostISA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 14),
    _TIPsecRUTnlHostISA_Type()
)
tIPsecRUTnlHostISA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlHostISA.setStatus("current")
_TIPsecRUTnlMatchTrustAnchor_Type = TNamedItemOrEmpty
_TIPsecRUTnlMatchTrustAnchor_Object = MibTableColumn
tIPsecRUTnlMatchTrustAnchor = _TIPsecRUTnlMatchTrustAnchor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 15),
    _TIPsecRUTnlMatchTrustAnchor_Type()
)
tIPsecRUTnlMatchTrustAnchor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlMatchTrustAnchor.setStatus("current")
_TIPsecRUTnlOperChanged_Type = TimeStamp
_TIPsecRUTnlOperChanged_Object = MibTableColumn
tIPsecRUTnlOperChanged = _TIPsecRUTnlOperChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 20, 1, 16),
    _TIPsecRUTnlOperChanged_Type()
)
tIPsecRUTnlOperChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlOperChanged.setStatus("current")
_TIPsecRUTnlStatsTable_Object = MibTable
tIPsecRUTnlStatsTable = _TIPsecRUTnlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21)
)
if mibBuilder.loadTexts:
    tIPsecRUTnlStatsTable.setStatus("current")
_TIPsecRUTnlStatsEntry_Object = MibTableRow
tIPsecRUTnlStatsEntry = _TIPsecRUTnlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1)
)
tIPsecRUTnlStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
)
if mibBuilder.loadTexts:
    tIPsecRUTnlStatsEntry.setStatus("current")


class _TIPsecRUTnlIsakmpState_Type(Integer32):
    """Custom type tIPsecRUTnlIsakmpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TIPsecRUTnlIsakmpState_Type.__name__ = "Integer32"
_TIPsecRUTnlIsakmpState_Object = MibTableColumn
tIPsecRUTnlIsakmpState = _TIPsecRUTnlIsakmpState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 1),
    _TIPsecRUTnlIsakmpState_Type()
)
tIPsecRUTnlIsakmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlIsakmpState.setStatus("current")
_TIPsecRUTnlIsakmpEstabTime_Type = TimeStamp
_TIPsecRUTnlIsakmpEstabTime_Object = MibTableColumn
tIPsecRUTnlIsakmpEstabTime = _TIPsecRUTnlIsakmpEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 2),
    _TIPsecRUTnlIsakmpEstabTime_Type()
)
tIPsecRUTnlIsakmpEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlIsakmpEstabTime.setStatus("current")
_TIPsecRUTnlIsakmpNegLifeTime_Type = Unsigned32
_TIPsecRUTnlIsakmpNegLifeTime_Object = MibTableColumn
tIPsecRUTnlIsakmpNegLifeTime = _TIPsecRUTnlIsakmpNegLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 3),
    _TIPsecRUTnlIsakmpNegLifeTime_Type()
)
tIPsecRUTnlIsakmpNegLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlIsakmpNegLifeTime.setStatus("current")
_TIPsecRUTnlNumDpdTx_Type = Counter32
_TIPsecRUTnlNumDpdTx_Object = MibTableColumn
tIPsecRUTnlNumDpdTx = _TIPsecRUTnlNumDpdTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 4),
    _TIPsecRUTnlNumDpdTx_Type()
)
tIPsecRUTnlNumDpdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumDpdTx.setStatus("current")
_TIPsecRUTnlNumDpdRx_Type = Counter32
_TIPsecRUTnlNumDpdRx_Object = MibTableColumn
tIPsecRUTnlNumDpdRx = _TIPsecRUTnlNumDpdRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 5),
    _TIPsecRUTnlNumDpdRx_Type()
)
tIPsecRUTnlNumDpdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumDpdRx.setStatus("current")
_TIPsecRUTnlNumDpdAckTx_Type = Counter32
_TIPsecRUTnlNumDpdAckTx_Object = MibTableColumn
tIPsecRUTnlNumDpdAckTx = _TIPsecRUTnlNumDpdAckTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 6),
    _TIPsecRUTnlNumDpdAckTx_Type()
)
tIPsecRUTnlNumDpdAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumDpdAckTx.setStatus("current")
_TIPsecRUTnlNumDpdAckRx_Type = Counter32
_TIPsecRUTnlNumDpdAckRx_Object = MibTableColumn
tIPsecRUTnlNumDpdAckRx = _TIPsecRUTnlNumDpdAckRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 7),
    _TIPsecRUTnlNumDpdAckRx_Type()
)
tIPsecRUTnlNumDpdAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumDpdAckRx.setStatus("current")
_TIPsecRUTnlNumExpRx_Type = Counter32
_TIPsecRUTnlNumExpRx_Object = MibTableColumn
tIPsecRUTnlNumExpRx = _TIPsecRUTnlNumExpRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 8),
    _TIPsecRUTnlNumExpRx_Type()
)
tIPsecRUTnlNumExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumExpRx.setStatus("current")
_TIPsecRUTnlNumInvalidDpdRx_Type = Counter32
_TIPsecRUTnlNumInvalidDpdRx_Object = MibTableColumn
tIPsecRUTnlNumInvalidDpdRx = _TIPsecRUTnlNumInvalidDpdRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 9),
    _TIPsecRUTnlNumInvalidDpdRx_Type()
)
tIPsecRUTnlNumInvalidDpdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumInvalidDpdRx.setStatus("current")
_TIPsecRUTnlNumCtrlPktsTx_Type = Counter32
_TIPsecRUTnlNumCtrlPktsTx_Object = MibTableColumn
tIPsecRUTnlNumCtrlPktsTx = _TIPsecRUTnlNumCtrlPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 10),
    _TIPsecRUTnlNumCtrlPktsTx_Type()
)
tIPsecRUTnlNumCtrlPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumCtrlPktsTx.setStatus("current")
_TIPsecRUTnlNumCtrlPktsRx_Type = Counter32
_TIPsecRUTnlNumCtrlPktsRx_Object = MibTableColumn
tIPsecRUTnlNumCtrlPktsRx = _TIPsecRUTnlNumCtrlPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 11),
    _TIPsecRUTnlNumCtrlPktsRx_Type()
)
tIPsecRUTnlNumCtrlPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumCtrlPktsRx.setStatus("current")
_TIPsecRUTnlNumCtrlTxErrors_Type = Counter32
_TIPsecRUTnlNumCtrlTxErrors_Object = MibTableColumn
tIPsecRUTnlNumCtrlTxErrors = _TIPsecRUTnlNumCtrlTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 12),
    _TIPsecRUTnlNumCtrlTxErrors_Type()
)
tIPsecRUTnlNumCtrlTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumCtrlTxErrors.setStatus("current")
_TIPsecRUTnlNumCtrlRxErrors_Type = Counter32
_TIPsecRUTnlNumCtrlRxErrors_Object = MibTableColumn
tIPsecRUTnlNumCtrlRxErrors = _TIPsecRUTnlNumCtrlRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 13),
    _TIPsecRUTnlNumCtrlRxErrors_Type()
)
tIPsecRUTnlNumCtrlRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlNumCtrlRxErrors.setStatus("current")
_TIPsecRUTnlMatCertEntryId_Type = Integer32
_TIPsecRUTnlMatCertEntryId_Object = MibTableColumn
tIPsecRUTnlMatCertEntryId = _TIPsecRUTnlMatCertEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 14),
    _TIPsecRUTnlMatCertEntryId_Type()
)
tIPsecRUTnlMatCertEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlMatCertEntryId.setStatus("current")
_TIPsecRUTnlCertProfName_Type = TNamedItemOrEmpty
_TIPsecRUTnlCertProfName_Object = MibTableColumn
tIPsecRUTnlCertProfName = _TIPsecRUTnlCertProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 21, 1, 15),
    _TIPsecRUTnlCertProfName_Type()
)
tIPsecRUTnlCertProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUTnlCertProfName.setStatus("current")
_TIPsecRUSATable_Object = MibTable
tIPsecRUSATable = _TIPsecRUSATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22)
)
if mibBuilder.loadTexts:
    tIPsecRUSATable.setStatus("current")
_TIPsecRUSAEntry_Object = MibTableRow
tIPsecRUSAEntry = _TIPsecRUSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1)
)
tIPsecRUSAEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAIndex"),
)
if mibBuilder.loadTexts:
    tIPsecRUSAEntry.setStatus("current")


class _TIPsecRUSAId_Type(Unsigned32):
    """Custom type tIPsecRUSAId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TIPsecRUSAId_Type.__name__ = "Unsigned32"
_TIPsecRUSAId_Object = MibTableColumn
tIPsecRUSAId = _TIPsecRUSAId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 1),
    _TIPsecRUSAId_Type()
)
tIPsecRUSAId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSAId.setStatus("current")


class _TIPsecRUSAIndex_Type(Unsigned32):
    """Custom type tIPsecRUSAIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TIPsecRUSAIndex_Type.__name__ = "Unsigned32"
_TIPsecRUSAIndex_Object = MibTableColumn
tIPsecRUSAIndex = _TIPsecRUSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 2),
    _TIPsecRUSAIndex_Type()
)
tIPsecRUSAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSAIndex.setStatus("current")
_TIPsecRUSADirection_Type = TmnxIPsecDirection
_TIPsecRUSADirection_Object = MibTableColumn
tIPsecRUSADirection = _TIPsecRUSADirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 3),
    _TIPsecRUSADirection_Type()
)
tIPsecRUSADirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSADirection.setStatus("current")


class _TIPsecRUSAEncryptionKey_Type(OctetString):
    """Custom type tIPsecRUSAEncryptionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TIPsecRUSAEncryptionKey_Type.__name__ = "OctetString"
_TIPsecRUSAEncryptionKey_Object = MibTableColumn
tIPsecRUSAEncryptionKey = _TIPsecRUSAEncryptionKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 4),
    _TIPsecRUSAEncryptionKey_Type()
)
tIPsecRUSAEncryptionKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAEncryptionKey.setStatus("current")


class _TIPsecRUSAAuthenticationKey_Type(OctetString):
    """Custom type tIPsecRUSAAuthenticationKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TIPsecRUSAAuthenticationKey_Type.__name__ = "OctetString"
_TIPsecRUSAAuthenticationKey_Object = MibTableColumn
tIPsecRUSAAuthenticationKey = _TIPsecRUSAAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 5),
    _TIPsecRUSAAuthenticationKey_Type()
)
tIPsecRUSAAuthenticationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAAuthenticationKey.setStatus("current")


class _TIPsecRUSASpi_Type(Unsigned32):
    """Custom type tIPsecRUSASpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16383),
    )


_TIPsecRUSASpi_Type.__name__ = "Unsigned32"
_TIPsecRUSASpi_Object = MibTableColumn
tIPsecRUSASpi = _TIPsecRUSASpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 6),
    _TIPsecRUSASpi_Type()
)
tIPsecRUSASpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSASpi.setStatus("current")
_TIPsecRUSAAuthAlgorithm_Type = TmnxAuthAlgorithm
_TIPsecRUSAAuthAlgorithm_Object = MibTableColumn
tIPsecRUSAAuthAlgorithm = _TIPsecRUSAAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 7),
    _TIPsecRUSAAuthAlgorithm_Type()
)
tIPsecRUSAAuthAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAAuthAlgorithm.setStatus("current")
_TIPsecRUSAEncrAlgorithm_Type = TmnxEncrAlgorithm
_TIPsecRUSAEncrAlgorithm_Object = MibTableColumn
tIPsecRUSAEncrAlgorithm = _TIPsecRUSAEncrAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 8),
    _TIPsecRUSAEncrAlgorithm_Type()
)
tIPsecRUSAEncrAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAEncrAlgorithm.setStatus("current")
_TIPsecRUSAEstablishedTime_Type = TimeStamp
_TIPsecRUSAEstablishedTime_Object = MibTableColumn
tIPsecRUSAEstablishedTime = _TIPsecRUSAEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 9),
    _TIPsecRUSAEstablishedTime_Type()
)
tIPsecRUSAEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAEstablishedTime.setStatus("current")
_TIPsecRUSANegotiatedLifeTime_Type = Unsigned32
_TIPsecRUSANegotiatedLifeTime_Object = MibTableColumn
tIPsecRUSANegotiatedLifeTime = _TIPsecRUSANegotiatedLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 10),
    _TIPsecRUSANegotiatedLifeTime_Type()
)
tIPsecRUSANegotiatedLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSANegotiatedLifeTime.setStatus("current")
_TIPsecRUSALclAddrType_Type = InetAddressType
_TIPsecRUSALclAddrType_Object = MibTableColumn
tIPsecRUSALclAddrType = _TIPsecRUSALclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 11),
    _TIPsecRUSALclAddrType_Type()
)
tIPsecRUSALclAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSALclAddrType.setStatus("obsolete")


class _TIPsecRUSALclAddr_Type(InetAddress):
    """Custom type tIPsecRUSALclAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUSALclAddr_Type.__name__ = "InetAddress"
_TIPsecRUSALclAddr_Object = MibTableColumn
tIPsecRUSALclAddr = _TIPsecRUSALclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 12),
    _TIPsecRUSALclAddr_Type()
)
tIPsecRUSALclAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSALclAddr.setStatus("obsolete")
_TIPsecRUSALclAPrefLen_Type = InetAddressPrefixLength
_TIPsecRUSALclAPrefLen_Object = MibTableColumn
tIPsecRUSALclAPrefLen = _TIPsecRUSALclAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 13),
    _TIPsecRUSALclAPrefLen_Type()
)
tIPsecRUSALclAPrefLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSALclAPrefLen.setStatus("obsolete")
_TIPsecRUSARemAddrType_Type = InetAddressType
_TIPsecRUSARemAddrType_Object = MibTableColumn
tIPsecRUSARemAddrType = _TIPsecRUSARemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 14),
    _TIPsecRUSARemAddrType_Type()
)
tIPsecRUSARemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSARemAddrType.setStatus("obsolete")


class _TIPsecRUSARemAddr_Type(InetAddress):
    """Custom type tIPsecRUSARemAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUSARemAddr_Type.__name__ = "InetAddress"
_TIPsecRUSARemAddr_Object = MibTableColumn
tIPsecRUSARemAddr = _TIPsecRUSARemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 15),
    _TIPsecRUSARemAddr_Type()
)
tIPsecRUSARemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSARemAddr.setStatus("obsolete")
_TIPsecRUSARemAPrefLen_Type = InetAddressPrefixLength
_TIPsecRUSARemAPrefLen_Object = MibTableColumn
tIPsecRUSARemAPrefLen = _TIPsecRUSARemAPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 22, 1, 16),
    _TIPsecRUSARemAPrefLen_Type()
)
tIPsecRUSARemAPrefLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSARemAPrefLen.setStatus("obsolete")
_TIPsecRUSAStatsTable_Object = MibTable
tIPsecRUSAStatsTable = _TIPsecRUSAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23)
)
if mibBuilder.loadTexts:
    tIPsecRUSAStatsTable.setStatus("current")
_TIPsecRUSAStatsEntry_Object = MibTableRow
tIPsecRUSAStatsEntry = _TIPsecRUSAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1)
)
tIPsecRUSAStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAIndex"),
)
if mibBuilder.loadTexts:
    tIPsecRUSAStatsEntry.setStatus("current")
_TIPsecRUSAStatsBytesProcessed_Type = Counter64
_TIPsecRUSAStatsBytesProcessed_Object = MibTableColumn
tIPsecRUSAStatsBytesProcessed = _TIPsecRUSAStatsBytesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 1),
    _TIPsecRUSAStatsBytesProcessed_Type()
)
tIPsecRUSAStatsBytesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsBytesProcessed.setStatus("current")
_TIPsecRUSAStatsBytesProcLow32_Type = Counter32
_TIPsecRUSAStatsBytesProcLow32_Object = MibTableColumn
tIPsecRUSAStatsBytesProcLow32 = _TIPsecRUSAStatsBytesProcLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 2),
    _TIPsecRUSAStatsBytesProcLow32_Type()
)
tIPsecRUSAStatsBytesProcLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsBytesProcLow32.setStatus("current")
_TIPsecRUSAStatsBytesProcHigh32_Type = Counter32
_TIPsecRUSAStatsBytesProcHigh32_Object = MibTableColumn
tIPsecRUSAStatsBytesProcHigh32 = _TIPsecRUSAStatsBytesProcHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 3),
    _TIPsecRUSAStatsBytesProcHigh32_Type()
)
tIPsecRUSAStatsBytesProcHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsBytesProcHigh32.setStatus("current")
_TIPsecRUSAStatsPktsProcessed_Type = Counter64
_TIPsecRUSAStatsPktsProcessed_Object = MibTableColumn
tIPsecRUSAStatsPktsProcessed = _TIPsecRUSAStatsPktsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 4),
    _TIPsecRUSAStatsPktsProcessed_Type()
)
tIPsecRUSAStatsPktsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPktsProcessed.setStatus("current")
_TIPsecRUSAStatsPktsProcLow32_Type = Counter32
_TIPsecRUSAStatsPktsProcLow32_Object = MibTableColumn
tIPsecRUSAStatsPktsProcLow32 = _TIPsecRUSAStatsPktsProcLow32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 5),
    _TIPsecRUSAStatsPktsProcLow32_Type()
)
tIPsecRUSAStatsPktsProcLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPktsProcLow32.setStatus("current")
_TIPsecRUSAStatsPktsProcHigh32_Type = Counter32
_TIPsecRUSAStatsPktsProcHigh32_Object = MibTableColumn
tIPsecRUSAStatsPktsProcHigh32 = _TIPsecRUSAStatsPktsProcHigh32_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 6),
    _TIPsecRUSAStatsPktsProcHigh32_Type()
)
tIPsecRUSAStatsPktsProcHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPktsProcHigh32.setStatus("current")
_TIPsecRUSAStatsCryptoErrors_Type = Counter32
_TIPsecRUSAStatsCryptoErrors_Object = MibTableColumn
tIPsecRUSAStatsCryptoErrors = _TIPsecRUSAStatsCryptoErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 7),
    _TIPsecRUSAStatsCryptoErrors_Type()
)
tIPsecRUSAStatsCryptoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsCryptoErrors.setStatus("current")
_TIPsecRUSAStatsReplayErrors_Type = Counter32
_TIPsecRUSAStatsReplayErrors_Object = MibTableColumn
tIPsecRUSAStatsReplayErrors = _TIPsecRUSAStatsReplayErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 8),
    _TIPsecRUSAStatsReplayErrors_Type()
)
tIPsecRUSAStatsReplayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsReplayErrors.setStatus("current")
_TIPsecRUSAStatsSAErrors_Type = Counter32
_TIPsecRUSAStatsSAErrors_Object = MibTableColumn
tIPsecRUSAStatsSAErrors = _TIPsecRUSAStatsSAErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 9),
    _TIPsecRUSAStatsSAErrors_Type()
)
tIPsecRUSAStatsSAErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsSAErrors.setStatus("current")
_TIPsecRUSAStatsPolicyErrors_Type = Counter32
_TIPsecRUSAStatsPolicyErrors_Object = MibTableColumn
tIPsecRUSAStatsPolicyErrors = _TIPsecRUSAStatsPolicyErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 10),
    _TIPsecRUSAStatsPolicyErrors_Type()
)
tIPsecRUSAStatsPolicyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPolicyErrors.setStatus("current")
_TIPsecRUSAStatsEncapOverhead_Type = Counter32
_TIPsecRUSAStatsEncapOverhead_Object = MibTableColumn
tIPsecRUSAStatsEncapOverhead = _TIPsecRUSAStatsEncapOverhead_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 11),
    _TIPsecRUSAStatsEncapOverhead_Type()
)
tIPsecRUSAStatsEncapOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsEncapOverhead.setStatus("current")
_TIPsecRUSAStatsPreEncapFragCnt_Type = Counter64
_TIPsecRUSAStatsPreEncapFragCnt_Object = MibTableColumn
tIPsecRUSAStatsPreEncapFragCnt = _TIPsecRUSAStatsPreEncapFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 12),
    _TIPsecRUSAStatsPreEncapFragCnt_Type()
)
tIPsecRUSAStatsPreEncapFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPreEncapFragCnt.setStatus("current")
_TIPsecRUSAStatsPreEncapFragLtSz_Type = Unsigned32
_TIPsecRUSAStatsPreEncapFragLtSz_Object = MibTableColumn
tIPsecRUSAStatsPreEncapFragLtSz = _TIPsecRUSAStatsPreEncapFragLtSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 13),
    _TIPsecRUSAStatsPreEncapFragLtSz_Type()
)
tIPsecRUSAStatsPreEncapFragLtSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPreEncapFragLtSz.setStatus("current")
_TIPsecRUSAStatsPostEncapFragCnt_Type = Counter64
_TIPsecRUSAStatsPostEncapFragCnt_Object = MibTableColumn
tIPsecRUSAStatsPostEncapFragCnt = _TIPsecRUSAStatsPostEncapFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 14),
    _TIPsecRUSAStatsPostEncapFragCnt_Type()
)
tIPsecRUSAStatsPostEncapFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPostEncapFragCnt.setStatus("current")
_TIPsecRUSAStatsPostEncapFragLtSz_Type = Unsigned32
_TIPsecRUSAStatsPostEncapFragLtSz_Object = MibTableColumn
tIPsecRUSAStatsPostEncapFragLtSz = _TIPsecRUSAStatsPostEncapFragLtSz_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 23, 1, 15),
    _TIPsecRUSAStatsPostEncapFragLtSz_Type()
)
tIPsecRUSAStatsPostEncapFragLtSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSAStatsPostEncapFragLtSz.setStatus("current")
_TmnxIPsecTunnelCountObjs_ObjectIdentity = ObjectIdentity
tmnxIPsecTunnelCountObjs = _TmnxIPsecTunnelCountObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24)
)
_TmnxIPsecPskTunnels_Type = Gauge32
_TmnxIPsecPskTunnels_Object = MibScalar
tmnxIPsecPskTunnels = _TmnxIPsecPskTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 1),
    _TmnxIPsecPskTunnels_Type()
)
tmnxIPsecPskTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecPskTunnels.setStatus("current")
_TmnxIPsecGWPskTunnels_Type = Gauge32
_TmnxIPsecGWPskTunnels_Object = MibScalar
tmnxIPsecGWPskTunnels = _TmnxIPsecGWPskTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 2),
    _TmnxIPsecGWPskTunnels_Type()
)
tmnxIPsecGWPskTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWPskTunnels.setStatus("current")
_TmnxIPsecGWPskXAuthTunnels_Type = Gauge32
_TmnxIPsecGWPskXAuthTunnels_Object = MibScalar
tmnxIPsecGWPskXAuthTunnels = _TmnxIPsecGWPskXAuthTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 3),
    _TmnxIPsecGWPskXAuthTunnels_Type()
)
tmnxIPsecGWPskXAuthTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWPskXAuthTunnels.setStatus("current")
_TmnxIPsecGWCertTunnels_Type = Gauge32
_TmnxIPsecGWCertTunnels_Object = MibScalar
tmnxIPsecGWCertTunnels = _TmnxIPsecGWCertTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 4),
    _TmnxIPsecGWCertTunnels_Type()
)
tmnxIPsecGWCertTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWCertTunnels.setStatus("current")
_TmnxIPsecGWPskRadiusTunnels_Type = Gauge32
_TmnxIPsecGWPskRadiusTunnels_Object = MibScalar
tmnxIPsecGWPskRadiusTunnels = _TmnxIPsecGWPskRadiusTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 5),
    _TmnxIPsecGWPskRadiusTunnels_Type()
)
tmnxIPsecGWPskRadiusTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWPskRadiusTunnels.setStatus("current")
_TmnxIPsecGWCertRadiusTunnels_Type = Gauge32
_TmnxIPsecGWCertRadiusTunnels_Object = MibScalar
tmnxIPsecGWCertRadiusTunnels = _TmnxIPsecGWCertRadiusTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 6),
    _TmnxIPsecGWCertRadiusTunnels_Type()
)
tmnxIPsecGWCertRadiusTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWCertRadiusTunnels.setStatus("current")
_TmnxIPsecGWEapTunnels_Type = Gauge32
_TmnxIPsecGWEapTunnels_Object = MibScalar
tmnxIPsecGWEapTunnels = _TmnxIPsecGWEapTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 7),
    _TmnxIPsecGWEapTunnels_Type()
)
tmnxIPsecGWEapTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWEapTunnels.setStatus("current")
_TmnxIPsecGWAutoEapRadiusTunnels_Type = Gauge32
_TmnxIPsecGWAutoEapRadiusTunnels_Object = MibScalar
tmnxIPsecGWAutoEapRadiusTunnels = _TmnxIPsecGWAutoEapRadiusTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 24, 8),
    _TmnxIPsecGWAutoEapRadiusTunnels_Type()
)
tmnxIPsecGWAutoEapRadiusTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecGWAutoEapRadiusTunnels.setStatus("current")
_TmnxIPsecTunnelBfdTableLastChgd_Type = TimeStamp
_TmnxIPsecTunnelBfdTableLastChgd_Object = MibScalar
tmnxIPsecTunnelBfdTableLastChgd = _TmnxIPsecTunnelBfdTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 25),
    _TmnxIPsecTunnelBfdTableLastChgd_Type()
)
tmnxIPsecTunnelBfdTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdTableLastChgd.setStatus("current")
_TmnxIPsecTunnelBfdTable_Object = MibTable
tmnxIPsecTunnelBfdTable = _TmnxIPsecTunnelBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26)
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdTable.setStatus("current")
_TmnxIPsecTunnelBfdEntry_Object = MibTableRow
tmnxIPsecTunnelBfdEntry = _TmnxIPsecTunnelBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1)
)
tmnxIPsecTunnelBfdEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSvcId"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdIfName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdDstAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdDstAddr"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdEntry.setStatus("current")
_TmnxIPsecTunnelBfdSvcId_Type = TmnxServId
_TmnxIPsecTunnelBfdSvcId_Object = MibTableColumn
tmnxIPsecTunnelBfdSvcId = _TmnxIPsecTunnelBfdSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 1),
    _TmnxIPsecTunnelBfdSvcId_Type()
)
tmnxIPsecTunnelBfdSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdSvcId.setStatus("current")
_TmnxIPsecTunnelBfdIfName_Type = TNamedItem
_TmnxIPsecTunnelBfdIfName_Object = MibTableColumn
tmnxIPsecTunnelBfdIfName = _TmnxIPsecTunnelBfdIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 2),
    _TmnxIPsecTunnelBfdIfName_Type()
)
tmnxIPsecTunnelBfdIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdIfName.setStatus("current")
_TmnxIPsecTunnelBfdDstAddrType_Type = InetAddressType
_TmnxIPsecTunnelBfdDstAddrType_Object = MibTableColumn
tmnxIPsecTunnelBfdDstAddrType = _TmnxIPsecTunnelBfdDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 3),
    _TmnxIPsecTunnelBfdDstAddrType_Type()
)
tmnxIPsecTunnelBfdDstAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdDstAddrType.setStatus("current")


class _TmnxIPsecTunnelBfdDstAddr_Type(InetAddress):
    """Custom type tmnxIPsecTunnelBfdDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTunnelBfdDstAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTunnelBfdDstAddr_Object = MibTableColumn
tmnxIPsecTunnelBfdDstAddr = _TmnxIPsecTunnelBfdDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 4),
    _TmnxIPsecTunnelBfdDstAddr_Type()
)
tmnxIPsecTunnelBfdDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdDstAddr.setStatus("current")
_TmnxIPsecTunnelBfdRowStatus_Type = RowStatus
_TmnxIPsecTunnelBfdRowStatus_Object = MibTableColumn
tmnxIPsecTunnelBfdRowStatus = _TmnxIPsecTunnelBfdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 5),
    _TmnxIPsecTunnelBfdRowStatus_Type()
)
tmnxIPsecTunnelBfdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdRowStatus.setStatus("current")
_TmnxIPsecTunnelBfdLastChanged_Type = TimeStamp
_TmnxIPsecTunnelBfdLastChanged_Object = MibTableColumn
tmnxIPsecTunnelBfdLastChanged = _TmnxIPsecTunnelBfdLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 6),
    _TmnxIPsecTunnelBfdLastChanged_Type()
)
tmnxIPsecTunnelBfdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdLastChanged.setStatus("current")
_TmnxIPsecTunnelBfdSrcAddrType_Type = InetAddressType
_TmnxIPsecTunnelBfdSrcAddrType_Object = MibTableColumn
tmnxIPsecTunnelBfdSrcAddrType = _TmnxIPsecTunnelBfdSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 7),
    _TmnxIPsecTunnelBfdSrcAddrType_Type()
)
tmnxIPsecTunnelBfdSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdSrcAddrType.setStatus("current")


class _TmnxIPsecTunnelBfdSrcAddr_Type(InetAddress):
    """Custom type tmnxIPsecTunnelBfdSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTunnelBfdSrcAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTunnelBfdSrcAddr_Object = MibTableColumn
tmnxIPsecTunnelBfdSrcAddr = _TmnxIPsecTunnelBfdSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 8),
    _TmnxIPsecTunnelBfdSrcAddr_Type()
)
tmnxIPsecTunnelBfdSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdSrcAddr.setStatus("current")
_TmnxIPsecTunnelBfdSessOperState_Type = TmnxBfdSessOperState
_TmnxIPsecTunnelBfdSessOperState_Object = MibTableColumn
tmnxIPsecTunnelBfdSessOperState = _TmnxIPsecTunnelBfdSessOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 26, 1, 9),
    _TmnxIPsecTunnelBfdSessOperState_Type()
)
tmnxIPsecTunnelBfdSessOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTunnelBfdSessOperState.setStatus("current")
_TIPsecRadAuthPlcyTblLastChgd_Type = TimeStamp
_TIPsecRadAuthPlcyTblLastChgd_Object = MibScalar
tIPsecRadAuthPlcyTblLastChgd = _TIPsecRadAuthPlcyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 27),
    _TIPsecRadAuthPlcyTblLastChgd_Type()
)
tIPsecRadAuthPlcyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyTblLastChgd.setStatus("current")
_TIPsecRadAuthPlcyTable_Object = MibTable
tIPsecRadAuthPlcyTable = _TIPsecRadAuthPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28)
)
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyTable.setStatus("current")
_TIPsecRadAuthPlcyEntry_Object = MibTableRow
tIPsecRadAuthPlcyEntry = _TIPsecRadAuthPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1)
)
tIPsecRadAuthPlcyEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyName"),
)
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyEntry.setStatus("current")
_TIPsecRadAuthPlcyName_Type = TNamedItem
_TIPsecRadAuthPlcyName_Object = MibTableColumn
tIPsecRadAuthPlcyName = _TIPsecRadAuthPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 1),
    _TIPsecRadAuthPlcyName_Type()
)
tIPsecRadAuthPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyName.setStatus("current")
_TIPsecRadAuthPlcyRowStatus_Type = RowStatus
_TIPsecRadAuthPlcyRowStatus_Object = MibTableColumn
tIPsecRadAuthPlcyRowStatus = _TIPsecRadAuthPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 2),
    _TIPsecRadAuthPlcyRowStatus_Type()
)
tIPsecRadAuthPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyRowStatus.setStatus("current")
_TIPsecRadAuthPlcyLastMgmtChange_Type = TimeStamp
_TIPsecRadAuthPlcyLastMgmtChange_Object = MibTableColumn
tIPsecRadAuthPlcyLastMgmtChange = _TIPsecRadAuthPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 3),
    _TIPsecRadAuthPlcyLastMgmtChange_Type()
)
tIPsecRadAuthPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyLastMgmtChange.setStatus("current")


class _TIPsecRadAuthPlcyInclAttr_Type(Bits):
    """Custom type tIPsecRadAuthPlcyInclAttr based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("callingStationId", 0),
          ("calledStationId", 1),
          ("nasPortId", 2),
          ("nasIdentifier", 3),
          ("nasIpAddr", 4))
    )

_TIPsecRadAuthPlcyInclAttr_Type.__name__ = "Bits"
_TIPsecRadAuthPlcyInclAttr_Object = MibTableColumn
tIPsecRadAuthPlcyInclAttr = _TIPsecRadAuthPlcyInclAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 4),
    _TIPsecRadAuthPlcyInclAttr_Type()
)
tIPsecRadAuthPlcyInclAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyInclAttr.setStatus("current")


class _TIPsecRadAuthPlcyRadSrvPlcy_Type(TNamedItemOrEmpty):
    """Custom type tIPsecRadAuthPlcyRadSrvPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPsecRadAuthPlcyRadSrvPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecRadAuthPlcyRadSrvPlcy_Object = MibTableColumn
tIPsecRadAuthPlcyRadSrvPlcy = _TIPsecRadAuthPlcyRadSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 5),
    _TIPsecRadAuthPlcyRadSrvPlcy_Type()
)
tIPsecRadAuthPlcyRadSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyRadSrvPlcy.setStatus("current")


class _TIPsecRadAuthPlcyPassword_Type(DisplayString):
    """Custom type tIPsecRadAuthPlcyPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TIPsecRadAuthPlcyPassword_Type.__name__ = "DisplayString"
_TIPsecRadAuthPlcyPassword_Object = MibTableColumn
tIPsecRadAuthPlcyPassword = _TIPsecRadAuthPlcyPassword_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 28, 1, 6),
    _TIPsecRadAuthPlcyPassword_Type()
)
tIPsecRadAuthPlcyPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAuthPlcyPassword.setStatus("current")
_TIPsecRadAcctPlcyTblLastChgd_Type = TimeStamp
_TIPsecRadAcctPlcyTblLastChgd_Object = MibScalar
tIPsecRadAcctPlcyTblLastChgd = _TIPsecRadAcctPlcyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 29),
    _TIPsecRadAcctPlcyTblLastChgd_Type()
)
tIPsecRadAcctPlcyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyTblLastChgd.setStatus("current")
_TIPsecRadAcctPlcyTable_Object = MibTable
tIPsecRadAcctPlcyTable = _TIPsecRadAcctPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30)
)
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyTable.setStatus("current")
_TIPsecRadAcctPlcyEntry_Object = MibTableRow
tIPsecRadAcctPlcyEntry = _TIPsecRadAcctPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1)
)
tIPsecRadAcctPlcyEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyName"),
)
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyEntry.setStatus("current")
_TIPsecRadAcctPlcyName_Type = TNamedItem
_TIPsecRadAcctPlcyName_Object = MibTableColumn
tIPsecRadAcctPlcyName = _TIPsecRadAcctPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 1),
    _TIPsecRadAcctPlcyName_Type()
)
tIPsecRadAcctPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyName.setStatus("current")
_TIPsecRadAcctPlcyRowStatus_Type = RowStatus
_TIPsecRadAcctPlcyRowStatus_Object = MibTableColumn
tIPsecRadAcctPlcyRowStatus = _TIPsecRadAcctPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 2),
    _TIPsecRadAcctPlcyRowStatus_Type()
)
tIPsecRadAcctPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyRowStatus.setStatus("current")
_TIPsecRadAcctPlcyLastMgmtChange_Type = TimeStamp
_TIPsecRadAcctPlcyLastMgmtChange_Object = MibTableColumn
tIPsecRadAcctPlcyLastMgmtChange = _TIPsecRadAcctPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 3),
    _TIPsecRadAcctPlcyLastMgmtChange_Type()
)
tIPsecRadAcctPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyLastMgmtChange.setStatus("current")


class _TIPsecRadAcctPlcyInclAttr_Type(Bits):
    """Custom type tIPsecRadAcctPlcyInclAttr based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("callingStationId", 0),
          ("calledStationId", 1),
          ("nasPortId", 2),
          ("nasIdentifier", 3),
          ("nasIpAddr", 4),
          ("framedIpAddr", 5),
          ("framedIpv6Prefix", 6))
    )

_TIPsecRadAcctPlcyInclAttr_Type.__name__ = "Bits"
_TIPsecRadAcctPlcyInclAttr_Object = MibTableColumn
tIPsecRadAcctPlcyInclAttr = _TIPsecRadAcctPlcyInclAttr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 4),
    _TIPsecRadAcctPlcyInclAttr_Type()
)
tIPsecRadAcctPlcyInclAttr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyInclAttr.setStatus("current")


class _TIPsecRadAcctPlcyRadSrvPlcy_Type(TNamedItemOrEmpty):
    """Custom type tIPsecRadAcctPlcyRadSrvPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TIPsecRadAcctPlcyRadSrvPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecRadAcctPlcyRadSrvPlcy_Object = MibTableColumn
tIPsecRadAcctPlcyRadSrvPlcy = _TIPsecRadAcctPlcyRadSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 30, 1, 5),
    _TIPsecRadAcctPlcyRadSrvPlcy_Type()
)
tIPsecRadAcctPlcyRadSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyRadSrvPlcy.setStatus("current")
_TmnxIPsecTnlDstAddrTblLastChngd_Type = TimeStamp
_TmnxIPsecTnlDstAddrTblLastChngd_Object = MibScalar
tmnxIPsecTnlDstAddrTblLastChngd = _TmnxIPsecTnlDstAddrTblLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 31),
    _TmnxIPsecTnlDstAddrTblLastChngd_Type()
)
tmnxIPsecTnlDstAddrTblLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrTblLastChngd.setStatus("current")
_TmnxIPsecTnlDstAddrTable_Object = MibTable
tmnxIPsecTnlDstAddrTable = _TmnxIPsecTnlDstAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32)
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrTable.setStatus("current")
_TmnxIPsecTnlDstAddrEntry_Object = MibTableRow
tmnxIPsecTnlDstAddrEntry = _TmnxIPsecTnlDstAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1)
)
tmnxIPsecTnlDstAddrEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelName"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddr"),
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrEntry.setStatus("current")
_TmnxIPsecTnlDstAddrType_Type = InetAddressType
_TmnxIPsecTnlDstAddrType_Object = MibTableColumn
tmnxIPsecTnlDstAddrType = _TmnxIPsecTnlDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1, 1),
    _TmnxIPsecTnlDstAddrType_Type()
)
tmnxIPsecTnlDstAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrType.setStatus("current")


class _TmnxIPsecTnlDstAddr_Type(InetAddress):
    """Custom type tmnxIPsecTnlDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxIPsecTnlDstAddr_Type.__name__ = "InetAddress"
_TmnxIPsecTnlDstAddr_Object = MibTableColumn
tmnxIPsecTnlDstAddr = _TmnxIPsecTnlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1, 2),
    _TmnxIPsecTnlDstAddr_Type()
)
tmnxIPsecTnlDstAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddr.setStatus("current")
_TmnxIPsecTnlDstAddrRowStatus_Type = RowStatus
_TmnxIPsecTnlDstAddrRowStatus_Object = MibTableColumn
tmnxIPsecTnlDstAddrRowStatus = _TmnxIPsecTnlDstAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1, 3),
    _TmnxIPsecTnlDstAddrRowStatus_Type()
)
tmnxIPsecTnlDstAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrRowStatus.setStatus("current")
_TmnxIPsecTnlDstAddrLastChanged_Type = TimeStamp
_TmnxIPsecTnlDstAddrLastChanged_Object = MibTableColumn
tmnxIPsecTnlDstAddrLastChanged = _TmnxIPsecTnlDstAddrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1, 4),
    _TmnxIPsecTnlDstAddrLastChanged_Type()
)
tmnxIPsecTnlDstAddrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrLastChanged.setStatus("current")
_TmnxIPsecTnlDstAddrResolved_Type = TruthValue
_TmnxIPsecTnlDstAddrResolved_Object = MibTableColumn
tmnxIPsecTnlDstAddrResolved = _TmnxIPsecTnlDstAddrResolved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 32, 1, 5),
    _TmnxIPsecTnlDstAddrResolved_Type()
)
tmnxIPsecTnlDstAddrResolved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstAddrResolved.setStatus("current")
_TIPsecCertProfileTblLastChgd_Type = TimeStamp
_TIPsecCertProfileTblLastChgd_Object = MibScalar
tIPsecCertProfileTblLastChgd = _TIPsecCertProfileTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 33),
    _TIPsecCertProfileTblLastChgd_Type()
)
tIPsecCertProfileTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfileTblLastChgd.setStatus("current")
_TIPsecCertProfileTable_Object = MibTable
tIPsecCertProfileTable = _TIPsecCertProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34)
)
if mibBuilder.loadTexts:
    tIPsecCertProfileTable.setStatus("current")
_TIPsecCertProfileEntry_Object = MibTableRow
tIPsecCertProfileEntry = _TIPsecCertProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1)
)
tIPsecCertProfileEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfileName"),
)
if mibBuilder.loadTexts:
    tIPsecCertProfileEntry.setStatus("current")
_TIPsecCertProfileName_Type = TNamedItem
_TIPsecCertProfileName_Object = MibTableColumn
tIPsecCertProfileName = _TIPsecCertProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 1),
    _TIPsecCertProfileName_Type()
)
tIPsecCertProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecCertProfileName.setStatus("current")
_TIPsecCertProfileRowStatus_Type = RowStatus
_TIPsecCertProfileRowStatus_Object = MibTableColumn
tIPsecCertProfileRowStatus = _TIPsecCertProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 2),
    _TIPsecCertProfileRowStatus_Type()
)
tIPsecCertProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfileRowStatus.setStatus("current")
_TIPsecCertProfileLastChgd_Type = TimeStamp
_TIPsecCertProfileLastChgd_Object = MibTableColumn
tIPsecCertProfileLastChgd = _TIPsecCertProfileLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 3),
    _TIPsecCertProfileLastChgd_Type()
)
tIPsecCertProfileLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfileLastChgd.setStatus("current")


class _TIPsecCertProfileAdminState_Type(TmnxAdminState):
    """Custom type tIPsecCertProfileAdminState based on TmnxAdminState"""
    defaultValue = 3


_TIPsecCertProfileAdminState_Type.__name__ = "TmnxAdminState"
_TIPsecCertProfileAdminState_Object = MibTableColumn
tIPsecCertProfileAdminState = _TIPsecCertProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 4),
    _TIPsecCertProfileAdminState_Type()
)
tIPsecCertProfileAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfileAdminState.setStatus("current")
_TIPsecCertProfileOperState_Type = TmnxOperState
_TIPsecCertProfileOperState_Object = MibTableColumn
tIPsecCertProfileOperState = _TIPsecCertProfileOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 5),
    _TIPsecCertProfileOperState_Type()
)
tIPsecCertProfileOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfileOperState.setStatus("current")


class _TIPsecCertProfileOperFlags_Type(Bits):
    """Custom type tIPsecCertProfileOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("profileAdminDown", 0),
          ("invalidCertFile", 1),
          ("invalidKeyFile", 2),
          ("invalidCertKeyCombo", 3),
          ("caProfileOperDown", 4),
          ("invalidCAProfEntry", 5))
    )

_TIPsecCertProfileOperFlags_Type.__name__ = "Bits"
_TIPsecCertProfileOperFlags_Object = MibTableColumn
tIPsecCertProfileOperFlags = _TIPsecCertProfileOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 34, 1, 6),
    _TIPsecCertProfileOperFlags_Type()
)
tIPsecCertProfileOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfileOperFlags.setStatus("current")
_TIPsecCertProfEntryIdTblLastChgd_Type = TimeStamp
_TIPsecCertProfEntryIdTblLastChgd_Object = MibScalar
tIPsecCertProfEntryIdTblLastChgd = _TIPsecCertProfEntryIdTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 35),
    _TIPsecCertProfEntryIdTblLastChgd_Type()
)
tIPsecCertProfEntryIdTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdTblLastChgd.setStatus("current")
_TIPsecCertProfEntryIdTable_Object = MibTable
tIPsecCertProfEntryIdTable = _TIPsecCertProfEntryIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36)
)
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdTable.setStatus("current")
_TIPsecCertProfEntryIdEntry_Object = MibTableRow
tIPsecCertProfEntryIdEntry = _TIPsecCertProfEntryIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1)
)
tIPsecCertProfEntryIdEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfileName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryId"),
)
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdEntry.setStatus("current")


class _TIPsecCertProfEntryId_Type(Integer32):
    """Custom type tIPsecCertProfEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TIPsecCertProfEntryId_Type.__name__ = "Integer32"
_TIPsecCertProfEntryId_Object = MibTableColumn
tIPsecCertProfEntryId = _TIPsecCertProfEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 1),
    _TIPsecCertProfEntryId_Type()
)
tIPsecCertProfEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryId.setStatus("current")
_TIPsecCertProfEntryIdRowStatus_Type = RowStatus
_TIPsecCertProfEntryIdRowStatus_Object = MibTableColumn
tIPsecCertProfEntryIdRowStatus = _TIPsecCertProfEntryIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 2),
    _TIPsecCertProfEntryIdRowStatus_Type()
)
tIPsecCertProfEntryIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdRowStatus.setStatus("current")
_TIPsecCertProfEntryIdLastChgd_Type = TimeStamp
_TIPsecCertProfEntryIdLastChgd_Object = MibTableColumn
tIPsecCertProfEntryIdLastChgd = _TIPsecCertProfEntryIdLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 3),
    _TIPsecCertProfEntryIdLastChgd_Type()
)
tIPsecCertProfEntryIdLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdLastChgd.setStatus("current")


class _TIPsecCertProfEntryIdCertFile_Type(DisplayString):
    """Custom type tIPsecCertProfEntryIdCertFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_TIPsecCertProfEntryIdCertFile_Type.__name__ = "DisplayString"
_TIPsecCertProfEntryIdCertFile_Object = MibTableColumn
tIPsecCertProfEntryIdCertFile = _TIPsecCertProfEntryIdCertFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 4),
    _TIPsecCertProfEntryIdCertFile_Type()
)
tIPsecCertProfEntryIdCertFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdCertFile.setStatus("current")


class _TIPsecCertProfEntryIdKeyFile_Type(DisplayString):
    """Custom type tIPsecCertProfEntryIdKeyFile based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 95),
    )


_TIPsecCertProfEntryIdKeyFile_Type.__name__ = "DisplayString"
_TIPsecCertProfEntryIdKeyFile_Object = MibTableColumn
tIPsecCertProfEntryIdKeyFile = _TIPsecCertProfEntryIdKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 5),
    _TIPsecCertProfEntryIdKeyFile_Type()
)
tIPsecCertProfEntryIdKeyFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdKeyFile.setStatus("current")


class _TIPsecCertProfEntryIdCompChain_Type(Integer32):
    """Custom type tIPsecCertProfEntryIdCompChain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("partial", 1),
          ("complete", 2))
    )


_TIPsecCertProfEntryIdCompChain_Type.__name__ = "Integer32"
_TIPsecCertProfEntryIdCompChain_Object = MibTableColumn
tIPsecCertProfEntryIdCompChain = _TIPsecCertProfEntryIdCompChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 6),
    _TIPsecCertProfEntryIdCompChain_Type()
)
tIPsecCertProfEntryIdCompChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdCompChain.setStatus("current")


class _TIPsecCertProfEntryIdOperFlags_Type(Bits):
    """Custom type tIPsecCertProfEntryIdOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("profileAdminDown", 0),
          ("invalidCertFile", 1),
          ("invalidKeyFile", 2),
          ("invalidCertKeyCombo", 3),
          ("caProfileOperDown", 4),
          ("invalidCAProfEntry", 5))
    )

_TIPsecCertProfEntryIdOperFlags_Type.__name__ = "Bits"
_TIPsecCertProfEntryIdOperFlags_Object = MibTableColumn
tIPsecCertProfEntryIdOperFlags = _TIPsecCertProfEntryIdOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 36, 1, 7),
    _TIPsecCertProfEntryIdOperFlags_Type()
)
tIPsecCertProfEntryIdOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertProfEntryIdOperFlags.setStatus("current")
_TIPsecCompChainCAProfTable_Object = MibTable
tIPsecCompChainCAProfTable = _TIPsecCompChainCAProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 37)
)
if mibBuilder.loadTexts:
    tIPsecCompChainCAProfTable.setStatus("current")
_TIPsecCompChainCAProfEntry_Object = MibTableRow
tIPsecCompChainCAProfEntry = _TIPsecCompChainCAProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 37, 1)
)
tIPsecCompChainCAProfEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfileName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryId"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCompChainCAProfOrder"),
)
if mibBuilder.loadTexts:
    tIPsecCompChainCAProfEntry.setStatus("current")
_TIPsecCompChainCAProfOrder_Type = Integer32
_TIPsecCompChainCAProfOrder_Object = MibTableColumn
tIPsecCompChainCAProfOrder = _TIPsecCompChainCAProfOrder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 37, 1, 1),
    _TIPsecCompChainCAProfOrder_Type()
)
tIPsecCompChainCAProfOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecCompChainCAProfOrder.setStatus("current")
_TIPsecCompChainCAProfName_Type = TNamedItem
_TIPsecCompChainCAProfName_Object = MibTableColumn
tIPsecCompChainCAProfName = _TIPsecCompChainCAProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 37, 1, 2),
    _TIPsecCompChainCAProfName_Type()
)
tIPsecCompChainCAProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCompChainCAProfName.setStatus("current")
_TIPsecCertChainCAProfTblLastChgd_Type = TimeStamp
_TIPsecCertChainCAProfTblLastChgd_Object = MibScalar
tIPsecCertChainCAProfTblLastChgd = _TIPsecCertChainCAProfTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 41),
    _TIPsecCertChainCAProfTblLastChgd_Type()
)
tIPsecCertChainCAProfTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfTblLastChgd.setStatus("current")
_TIPsecCertChainCAProfTable_Object = MibTable
tIPsecCertChainCAProfTable = _TIPsecCertChainCAProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 42)
)
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfTable.setStatus("current")
_TIPsecCertChainCAProfEntry_Object = MibTableRow
tIPsecCertChainCAProfEntry = _TIPsecCertChainCAProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 42, 1)
)
tIPsecCertChainCAProfEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfileName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryId"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecCertChainCAProfName"),
)
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfEntry.setStatus("current")
_TIPsecCertChainCAProfName_Type = TNamedItem
_TIPsecCertChainCAProfName_Object = MibTableColumn
tIPsecCertChainCAProfName = _TIPsecCertChainCAProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 42, 1, 1),
    _TIPsecCertChainCAProfName_Type()
)
tIPsecCertChainCAProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfName.setStatus("current")
_TIPsecCertChainCAProfRowStatus_Type = RowStatus
_TIPsecCertChainCAProfRowStatus_Object = MibTableColumn
tIPsecCertChainCAProfRowStatus = _TIPsecCertChainCAProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 42, 1, 2),
    _TIPsecCertChainCAProfRowStatus_Type()
)
tIPsecCertChainCAProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfRowStatus.setStatus("current")
_TIPsecCertChainCAProfLastChgd_Type = TimeStamp
_TIPsecCertChainCAProfLastChgd_Object = MibTableColumn
tIPsecCertChainCAProfLastChgd = _TIPsecCertChainCAProfLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 42, 1, 3),
    _TIPsecCertChainCAProfLastChgd_Type()
)
tIPsecCertChainCAProfLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecCertChainCAProfLastChgd.setStatus("current")
_TIPsecTsListTblLastChgd_Type = TimeStamp
_TIPsecTsListTblLastChgd_Object = MibScalar
tIPsecTsListTblLastChgd = _TIPsecTsListTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 43),
    _TIPsecTsListTblLastChgd_Type()
)
tIPsecTsListTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTsListTblLastChgd.setStatus("current")
_TIPsecTsListTable_Object = MibTable
tIPsecTsListTable = _TIPsecTsListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 44)
)
if mibBuilder.loadTexts:
    tIPsecTsListTable.setStatus("current")
_TIPsecTsListEntry_Object = MibTableRow
tIPsecTsListEntry = _TIPsecTsListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 44, 1)
)
tIPsecTsListEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTsListName"),
)
if mibBuilder.loadTexts:
    tIPsecTsListEntry.setStatus("current")
_TIPsecTsListName_Type = TNamedItem
_TIPsecTsListName_Object = MibTableColumn
tIPsecTsListName = _TIPsecTsListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 44, 1, 1),
    _TIPsecTsListName_Type()
)
tIPsecTsListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTsListName.setStatus("current")
_TIPsecTsListRowStatus_Type = RowStatus
_TIPsecTsListRowStatus_Object = MibTableColumn
tIPsecTsListRowStatus = _TIPsecTsListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 44, 1, 2),
    _TIPsecTsListRowStatus_Type()
)
tIPsecTsListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListRowStatus.setStatus("current")
_TIPsecTsListLastChgd_Type = TimeStamp
_TIPsecTsListLastChgd_Object = MibTableColumn
tIPsecTsListLastChgd = _TIPsecTsListLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 44, 1, 3),
    _TIPsecTsListLastChgd_Type()
)
tIPsecTsListLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTsListLastChgd.setStatus("current")
_TIPsecTsListLclEntryTblLastChgd_Type = TimeStamp
_TIPsecTsListLclEntryTblLastChgd_Object = MibScalar
tIPsecTsListLclEntryTblLastChgd = _TIPsecTsListLclEntryTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 45),
    _TIPsecTsListLclEntryTblLastChgd_Type()
)
tIPsecTsListLclEntryTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryTblLastChgd.setStatus("current")
_TIPsecTsListLclEntryTable_Object = MibTable
tIPsecTsListLclEntryTable = _TIPsecTsListLclEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46)
)
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryTable.setStatus("current")
_TIPsecTsListLclEntryEntry_Object = MibTableRow
tIPsecTsListLclEntryEntry = _TIPsecTsListLclEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1)
)
tIPsecTsListLclEntryEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTsListName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryId"),
)
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryEntry.setStatus("current")


class _TIPsecTsListLclEntryId_Type(Integer32):
    """Custom type tIPsecTsListLclEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TIPsecTsListLclEntryId_Type.__name__ = "Integer32"
_TIPsecTsListLclEntryId_Object = MibTableColumn
tIPsecTsListLclEntryId = _TIPsecTsListLclEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 1),
    _TIPsecTsListLclEntryId_Type()
)
tIPsecTsListLclEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryId.setStatus("current")
_TIPsecTsListLclEntryRowStatus_Type = RowStatus
_TIPsecTsListLclEntryRowStatus_Object = MibTableColumn
tIPsecTsListLclEntryRowStatus = _TIPsecTsListLclEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 2),
    _TIPsecTsListLclEntryRowStatus_Type()
)
tIPsecTsListLclEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryRowStatus.setStatus("current")
_TIPsecTsListLclEntryLastChgd_Type = TimeStamp
_TIPsecTsListLclEntryLastChgd_Object = MibTableColumn
tIPsecTsListLclEntryLastChgd = _TIPsecTsListLclEntryLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 3),
    _TIPsecTsListLclEntryLastChgd_Type()
)
tIPsecTsListLclEntryLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryLastChgd.setStatus("current")


class _TIPsecTsListLclEntryFrAddrType_Type(InetAddressType):
    """Custom type tIPsecTsListLclEntryFrAddrType based on InetAddressType"""
    defaultValue = 0


_TIPsecTsListLclEntryFrAddrType_Type.__name__ = "InetAddressType"
_TIPsecTsListLclEntryFrAddrType_Object = MibTableColumn
tIPsecTsListLclEntryFrAddrType = _TIPsecTsListLclEntryFrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 5),
    _TIPsecTsListLclEntryFrAddrType_Type()
)
tIPsecTsListLclEntryFrAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryFrAddrType.setStatus("current")


class _TIPsecTsListLclEntryFrAddr_Type(InetAddress):
    """Custom type tIPsecTsListLclEntryFrAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecTsListLclEntryFrAddr_Type.__name__ = "InetAddress"
_TIPsecTsListLclEntryFrAddr_Object = MibTableColumn
tIPsecTsListLclEntryFrAddr = _TIPsecTsListLclEntryFrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 6),
    _TIPsecTsListLclEntryFrAddr_Type()
)
tIPsecTsListLclEntryFrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryFrAddr.setStatus("current")


class _TIPsecTsListLclEntryToAddrType_Type(InetAddressType):
    """Custom type tIPsecTsListLclEntryToAddrType based on InetAddressType"""
    defaultValue = 0


_TIPsecTsListLclEntryToAddrType_Type.__name__ = "InetAddressType"
_TIPsecTsListLclEntryToAddrType_Object = MibTableColumn
tIPsecTsListLclEntryToAddrType = _TIPsecTsListLclEntryToAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 7),
    _TIPsecTsListLclEntryToAddrType_Type()
)
tIPsecTsListLclEntryToAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryToAddrType.setStatus("current")


class _TIPsecTsListLclEntryToAddr_Type(InetAddress):
    """Custom type tIPsecTsListLclEntryToAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecTsListLclEntryToAddr_Type.__name__ = "InetAddress"
_TIPsecTsListLclEntryToAddr_Object = MibTableColumn
tIPsecTsListLclEntryToAddr = _TIPsecTsListLclEntryToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 8),
    _TIPsecTsListLclEntryToAddr_Type()
)
tIPsecTsListLclEntryToAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryToAddr.setStatus("current")


class _TIPsecTsListLclEntryPfxAddrType_Type(InetAddressType):
    """Custom type tIPsecTsListLclEntryPfxAddrType based on InetAddressType"""
    defaultValue = 0


_TIPsecTsListLclEntryPfxAddrType_Type.__name__ = "InetAddressType"
_TIPsecTsListLclEntryPfxAddrType_Object = MibTableColumn
tIPsecTsListLclEntryPfxAddrType = _TIPsecTsListLclEntryPfxAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 9),
    _TIPsecTsListLclEntryPfxAddrType_Type()
)
tIPsecTsListLclEntryPfxAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryPfxAddrType.setStatus("current")


class _TIPsecTsListLclEntryPfxAddr_Type(InetAddress):
    """Custom type tIPsecTsListLclEntryPfxAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecTsListLclEntryPfxAddr_Type.__name__ = "InetAddress"
_TIPsecTsListLclEntryPfxAddr_Object = MibTableColumn
tIPsecTsListLclEntryPfxAddr = _TIPsecTsListLclEntryPfxAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 10),
    _TIPsecTsListLclEntryPfxAddr_Type()
)
tIPsecTsListLclEntryPfxAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryPfxAddr.setStatus("current")


class _TIPsecTsListLclEntryPfxLen_Type(InetAddressPrefixLength):
    """Custom type tIPsecTsListLclEntryPfxLen based on InetAddressPrefixLength"""
    defaultValue = 0


_TIPsecTsListLclEntryPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TIPsecTsListLclEntryPfxLen_Object = MibTableColumn
tIPsecTsListLclEntryPfxLen = _TIPsecTsListLclEntryPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 46, 1, 11),
    _TIPsecTsListLclEntryPfxLen_Type()
)
tIPsecTsListLclEntryPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTsListLclEntryPfxLen.setStatus("current")
_TIPsecGWTsNegSelPlcyTblLastChgd_Type = TimeStamp
_TIPsecGWTsNegSelPlcyTblLastChgd_Object = MibScalar
tIPsecGWTsNegSelPlcyTblLastChgd = _TIPsecGWTsNegSelPlcyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 47),
    _TIPsecGWTsNegSelPlcyTblLastChgd_Type()
)
tIPsecGWTsNegSelPlcyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyTblLastChgd.setStatus("current")
_TIPsecGWTsNegSelPlcyTable_Object = MibTable
tIPsecGWTsNegSelPlcyTable = _TIPsecGWTsNegSelPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48)
)
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyTable.setStatus("current")
_TIPsecGWTsNegSelPlcyEntry_Object = MibTableRow
tIPsecGWTsNegSelPlcyEntry = _TIPsecGWTsNegSelPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48, 1)
)
tIPsecGWTsNegSelPlcyEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecGWTsNegSelPlcyName"),
)
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyEntry.setStatus("current")
_TIPsecGWTsNegSelPlcyName_Type = TNamedItemOrEmpty
_TIPsecGWTsNegSelPlcyName_Object = MibTableColumn
tIPsecGWTsNegSelPlcyName = _TIPsecGWTsNegSelPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48, 1, 1),
    _TIPsecGWTsNegSelPlcyName_Type()
)
tIPsecGWTsNegSelPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyName.setStatus("current")
_TIPsecGWTsNegSelPlcyRowStatus_Type = RowStatus
_TIPsecGWTsNegSelPlcyRowStatus_Object = MibTableColumn
tIPsecGWTsNegSelPlcyRowStatus = _TIPsecGWTsNegSelPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48, 1, 2),
    _TIPsecGWTsNegSelPlcyRowStatus_Type()
)
tIPsecGWTsNegSelPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyRowStatus.setStatus("current")
_TIPsecGWTsNegSelPlcyLastChgd_Type = TimeStamp
_TIPsecGWTsNegSelPlcyLastChgd_Object = MibTableColumn
tIPsecGWTsNegSelPlcyLastChgd = _TIPsecGWTsNegSelPlcyLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48, 1, 3),
    _TIPsecGWTsNegSelPlcyLastChgd_Type()
)
tIPsecGWTsNegSelPlcyLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyLastChgd.setStatus("current")


class _TIPsecGWTsNegSelPlcyTsList_Type(TNamedItemOrEmpty):
    """Custom type tIPsecGWTsNegSelPlcyTsList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TIPsecGWTsNegSelPlcyTsList_Type.__name__ = "TNamedItemOrEmpty"
_TIPsecGWTsNegSelPlcyTsList_Object = MibTableColumn
tIPsecGWTsNegSelPlcyTsList = _TIPsecGWTsNegSelPlcyTsList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 48, 1, 4),
    _TIPsecGWTsNegSelPlcyTsList_Type()
)
tIPsecGWTsNegSelPlcyTsList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecGWTsNegSelPlcyTsList.setStatus("current")
_TIPsecTrustAnchorProfTblLastChgd_Type = TimeStamp
_TIPsecTrustAnchorProfTblLastChgd_Object = MibScalar
tIPsecTrustAnchorProfTblLastChgd = _TIPsecTrustAnchorProfTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 49),
    _TIPsecTrustAnchorProfTblLastChgd_Type()
)
tIPsecTrustAnchorProfTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfTblLastChgd.setStatus("current")
_TIPsecTrustAnchorProfTable_Object = MibTable
tIPsecTrustAnchorProfTable = _TIPsecTrustAnchorProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50)
)
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfTable.setStatus("current")
_TIPsecTrustAnchorProfEntry_Object = MibTableRow
tIPsecTrustAnchorProfEntry = _TIPsecTrustAnchorProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50, 1)
)
tIPsecTrustAnchorProfEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorProfName"),
)
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfEntry.setStatus("current")
_TIPsecTrustAnchorProfName_Type = TNamedItem
_TIPsecTrustAnchorProfName_Object = MibTableColumn
tIPsecTrustAnchorProfName = _TIPsecTrustAnchorProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50, 1, 1),
    _TIPsecTrustAnchorProfName_Type()
)
tIPsecTrustAnchorProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfName.setStatus("current")
_TIPsecTrustAnchorProfRowStatus_Type = RowStatus
_TIPsecTrustAnchorProfRowStatus_Object = MibTableColumn
tIPsecTrustAnchorProfRowStatus = _TIPsecTrustAnchorProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50, 1, 2),
    _TIPsecTrustAnchorProfRowStatus_Type()
)
tIPsecTrustAnchorProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfRowStatus.setStatus("current")
_TIPsecTrustAnchorProfLastChgd_Type = TimeStamp
_TIPsecTrustAnchorProfLastChgd_Object = MibTableColumn
tIPsecTrustAnchorProfLastChgd = _TIPsecTrustAnchorProfLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50, 1, 3),
    _TIPsecTrustAnchorProfLastChgd_Type()
)
tIPsecTrustAnchorProfLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorProfLastChgd.setStatus("current")
_TIPsecTrustAnchorCAProfDown_Type = Integer32
_TIPsecTrustAnchorCAProfDown_Object = MibTableColumn
tIPsecTrustAnchorCAProfDown = _TIPsecTrustAnchorCAProfDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 50, 1, 4),
    _TIPsecTrustAnchorCAProfDown_Type()
)
tIPsecTrustAnchorCAProfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorCAProfDown.setStatus("current")
_TIPsecTrustAnchorsTblLastChgd_Type = TimeStamp
_TIPsecTrustAnchorsTblLastChgd_Object = MibScalar
tIPsecTrustAnchorsTblLastChgd = _TIPsecTrustAnchorsTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 51),
    _TIPsecTrustAnchorsTblLastChgd_Type()
)
tIPsecTrustAnchorsTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsTblLastChgd.setStatus("current")
_TIPsecTrustAnchorsTable_Object = MibTable
tIPsecTrustAnchorsTable = _TIPsecTrustAnchorsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 52)
)
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsTable.setStatus("current")
_TIPsecTrustAnchorsEntry_Object = MibTableRow
tIPsecTrustAnchorsEntry = _TIPsecTrustAnchorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 52, 1)
)
tIPsecTrustAnchorsEntry.setIndexNames(
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorProfName"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorsCAProfile"),
)
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsEntry.setStatus("current")
_TIPsecTrustAnchorsCAProfile_Type = TNamedItem
_TIPsecTrustAnchorsCAProfile_Object = MibTableColumn
tIPsecTrustAnchorsCAProfile = _TIPsecTrustAnchorsCAProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 52, 1, 1),
    _TIPsecTrustAnchorsCAProfile_Type()
)
tIPsecTrustAnchorsCAProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsCAProfile.setStatus("current")
_TIPsecTrustAnchorsRowStatus_Type = RowStatus
_TIPsecTrustAnchorsRowStatus_Object = MibTableColumn
tIPsecTrustAnchorsRowStatus = _TIPsecTrustAnchorsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 52, 1, 2),
    _TIPsecTrustAnchorsRowStatus_Type()
)
tIPsecTrustAnchorsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsRowStatus.setStatus("current")
_TIPsecTrustAnchorsLastChgd_Type = TimeStamp
_TIPsecTrustAnchorsLastChgd_Object = MibTableColumn
tIPsecTrustAnchorsLastChgd = _TIPsecTrustAnchorsLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 52, 1, 3),
    _TIPsecTrustAnchorsLastChgd_Type()
)
tIPsecTrustAnchorsLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecTrustAnchorsLastChgd.setStatus("current")
_TIPsecRUSATrafficSelTable_Object = MibTable
tIPsecRUSATrafficSelTable = _TIPsecRUSATrafficSelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53)
)
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelTable.setStatus("current")
_TIPsecRUSATrafficSelEntry_Object = MibTableRow
tIPsecRUSATrafficSelEntry = _TIPsecRUSATrafficSelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1)
)
tIPsecRUSATrafficSelEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlInetAddress"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUTnlPort"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAId"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSADirection"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSAIndex"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelSide"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelFrAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelFrAddr"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelToAddrType"),
    (0, "TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelToAddr"),
)
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelEntry.setStatus("current")
_TIPsecRUSATrafficSelSide_Type = TmnxIpsecTrafficSelSide
_TIPsecRUSATrafficSelSide_Object = MibTableColumn
tIPsecRUSATrafficSelSide = _TIPsecRUSATrafficSelSide_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 1),
    _TIPsecRUSATrafficSelSide_Type()
)
tIPsecRUSATrafficSelSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelSide.setStatus("current")
_TIPsecRUSATrafficSelFrAddrType_Type = InetAddressType
_TIPsecRUSATrafficSelFrAddrType_Object = MibTableColumn
tIPsecRUSATrafficSelFrAddrType = _TIPsecRUSATrafficSelFrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 2),
    _TIPsecRUSATrafficSelFrAddrType_Type()
)
tIPsecRUSATrafficSelFrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelFrAddrType.setStatus("current")


class _TIPsecRUSATrafficSelFrAddr_Type(InetAddress):
    """Custom type tIPsecRUSATrafficSelFrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUSATrafficSelFrAddr_Type.__name__ = "InetAddress"
_TIPsecRUSATrafficSelFrAddr_Object = MibTableColumn
tIPsecRUSATrafficSelFrAddr = _TIPsecRUSATrafficSelFrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 3),
    _TIPsecRUSATrafficSelFrAddr_Type()
)
tIPsecRUSATrafficSelFrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelFrAddr.setStatus("current")
_TIPsecRUSATrafficSelToAddrType_Type = InetAddressType
_TIPsecRUSATrafficSelToAddrType_Object = MibTableColumn
tIPsecRUSATrafficSelToAddrType = _TIPsecRUSATrafficSelToAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 4),
    _TIPsecRUSATrafficSelToAddrType_Type()
)
tIPsecRUSATrafficSelToAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelToAddrType.setStatus("current")


class _TIPsecRUSATrafficSelToAddr_Type(InetAddress):
    """Custom type tIPsecRUSATrafficSelToAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecRUSATrafficSelToAddr_Type.__name__ = "InetAddress"
_TIPsecRUSATrafficSelToAddr_Object = MibTableColumn
tIPsecRUSATrafficSelToAddr = _TIPsecRUSATrafficSelToAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 5),
    _TIPsecRUSATrafficSelToAddr_Type()
)
tIPsecRUSATrafficSelToAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelToAddr.setStatus("current")
_TIPsecRUSATrafficSelLastChgd_Type = TimeStamp
_TIPsecRUSATrafficSelLastChgd_Object = MibTableColumn
tIPsecRUSATrafficSelLastChgd = _TIPsecRUSATrafficSelLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 53, 1, 6),
    _TIPsecRUSATrafficSelLastChgd_Type()
)
tIPsecRUSATrafficSelLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelLastChgd.setStatus("current")
_TmnxIPsecNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxIPsecNotifyObjs = _TmnxIPsecNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100)
)
_TIPsecNotifRUTnlInetAddrType_Type = InetAddressType
_TIPsecNotifRUTnlInetAddrType_Object = MibScalar
tIPsecNotifRUTnlInetAddrType = _TIPsecNotifRUTnlInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 1),
    _TIPsecNotifRUTnlInetAddrType_Type()
)
tIPsecNotifRUTnlInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifRUTnlInetAddrType.setStatus("current")


class _TIPsecNotifRUTnlInetAddress_Type(InetAddress):
    """Custom type tIPsecNotifRUTnlInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecNotifRUTnlInetAddress_Type.__name__ = "InetAddress"
_TIPsecNotifRUTnlInetAddress_Object = MibScalar
tIPsecNotifRUTnlInetAddress = _TIPsecNotifRUTnlInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 2),
    _TIPsecNotifRUTnlInetAddress_Type()
)
tIPsecNotifRUTnlInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifRUTnlInetAddress.setStatus("current")
_TIPsecNotifRUTnlPort_Type = TTcpUdpPort
_TIPsecNotifRUTnlPort_Object = MibScalar
tIPsecNotifRUTnlPort = _TIPsecNotifRUTnlPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 3),
    _TIPsecNotifRUTnlPort_Type()
)
tIPsecNotifRUTnlPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifRUTnlPort.setStatus("current")
_TIPsecNotifReason_Type = DisplayString
_TIPsecNotifReason_Object = MibScalar
tIPsecNotifReason = _TIPsecNotifReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 4),
    _TIPsecNotifReason_Type()
)
tIPsecNotifReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifReason.setStatus("current")
_TIPsecNotifBfdIntfSvcId_Type = TmnxServId
_TIPsecNotifBfdIntfSvcId_Object = MibScalar
tIPsecNotifBfdIntfSvcId = _TIPsecNotifBfdIntfSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 5),
    _TIPsecNotifBfdIntfSvcId_Type()
)
tIPsecNotifBfdIntfSvcId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifBfdIntfSvcId.setStatus("current")
_TIPsecNotifBfdIntfIfName_Type = TNamedItem
_TIPsecNotifBfdIntfIfName_Object = MibScalar
tIPsecNotifBfdIntfIfName = _TIPsecNotifBfdIntfIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 6),
    _TIPsecNotifBfdIntfIfName_Type()
)
tIPsecNotifBfdIntfIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifBfdIntfIfName.setStatus("current")
_TIPsecNotifBfdIntfDestIpType_Type = InetAddressType
_TIPsecNotifBfdIntfDestIpType_Object = MibScalar
tIPsecNotifBfdIntfDestIpType = _TIPsecNotifBfdIntfDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 7),
    _TIPsecNotifBfdIntfDestIpType_Type()
)
tIPsecNotifBfdIntfDestIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifBfdIntfDestIpType.setStatus("current")


class _TIPsecNotifBfdIntfDestIp_Type(InetAddress):
    """Custom type tIPsecNotifBfdIntfDestIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TIPsecNotifBfdIntfDestIp_Type.__name__ = "InetAddress"
_TIPsecNotifBfdIntfDestIp_Object = MibScalar
tIPsecNotifBfdIntfDestIp = _TIPsecNotifBfdIntfDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 8),
    _TIPsecNotifBfdIntfDestIp_Type()
)
tIPsecNotifBfdIntfDestIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifBfdIntfDestIp.setStatus("current")
_TIPsecNotifBfdIntfSessState_Type = TmnxBfdSessOperState
_TIPsecNotifBfdIntfSessState_Object = MibScalar
tIPsecNotifBfdIntfSessState = _TIPsecNotifBfdIntfSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 9),
    _TIPsecNotifBfdIntfSessState_Type()
)
tIPsecNotifBfdIntfSessState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifBfdIntfSessState.setStatus("current")
_TIPsecRadAcctPlcyFailReason_Type = DisplayString
_TIPsecRadAcctPlcyFailReason_Object = MibScalar
tIPsecRadAcctPlcyFailReason = _TIPsecRadAcctPlcyFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 10),
    _TIPsecRadAcctPlcyFailReason_Type()
)
tIPsecRadAcctPlcyFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyFailReason.setStatus("current")
_TIPsecNotifIPsecTunnelName_Type = TNamedItem
_TIPsecNotifIPsecTunnelName_Object = MibScalar
tIPsecNotifIPsecTunnelName = _TIPsecNotifIPsecTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 11),
    _TIPsecNotifIPsecTunnelName_Type()
)
tIPsecNotifIPsecTunnelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifIPsecTunnelName.setStatus("current")
_TIPsecNotifConfigIpMtu_Type = Unsigned32
_TIPsecNotifConfigIpMtu_Object = MibScalar
tIPsecNotifConfigIpMtu = _TIPsecNotifConfigIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 12),
    _TIPsecNotifConfigIpMtu_Type()
)
tIPsecNotifConfigIpMtu.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifConfigIpMtu.setStatus("current")
_TIPsecNotifEncapOverhead_Type = Unsigned32
_TIPsecNotifEncapOverhead_Object = MibScalar
tIPsecNotifEncapOverhead = _TIPsecNotifEncapOverhead_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 13),
    _TIPsecNotifEncapOverhead_Type()
)
tIPsecNotifEncapOverhead.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifEncapOverhead.setStatus("current")
_TIPsecNotifConfigEncapIpMtu_Type = Unsigned32
_TIPsecNotifConfigEncapIpMtu_Object = MibScalar
tIPsecNotifConfigEncapIpMtu = _TIPsecNotifConfigEncapIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 14),
    _TIPsecNotifConfigEncapIpMtu_Type()
)
tIPsecNotifConfigEncapIpMtu.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifConfigEncapIpMtu.setStatus("current")
_TIPsecNotifCertProfileName_Type = TNamedItem
_TIPsecNotifCertProfileName_Object = MibScalar
tIPsecNotifCertProfileName = _TIPsecNotifCertProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 15),
    _TIPsecNotifCertProfileName_Type()
)
tIPsecNotifCertProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifCertProfileName.setStatus("current")
_TIPsecNotifCertProfEntryId_Type = TEntryId
_TIPsecNotifCertProfEntryId_Object = MibScalar
tIPsecNotifCertProfEntryId = _TIPsecNotifCertProfEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 16),
    _TIPsecNotifCertProfEntryId_Type()
)
tIPsecNotifCertProfEntryId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifCertProfEntryId.setStatus("current")
_TIPsecNotifCaProfNames_Type = DisplayString
_TIPsecNotifCaProfNames_Object = MibScalar
tIPsecNotifCaProfNames = _TIPsecNotifCaProfNames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 48, 100, 17),
    _TIPsecNotifCaProfNames_Type()
)
tIPsecNotifCaProfNames.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tIPsecNotifCaProfNames.setStatus("current")
_TmnxIPsecNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxIPsecNotifyPrefix = _TmnxIPsecNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48)
)
_TmnxIPsecNotifications_ObjectIdentity = ObjectIdentity
tmnxIPsecNotifications = _TmnxIPsecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0)
)

# Managed Objects groups

tmnxIPsecV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 1)
)
tmnxIPsecV6v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformTblLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTransformEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyTableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyDescription"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyIkeMode"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyDHGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyPFSEnabled"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyPFSDHGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyIsakmpLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyIPsecLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyNatTraversal"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyNatTKeepAliveIntvl"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyNatTBehindNatOnly"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyDpd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyDpdInterval"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyDpdMaxRetries"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelTableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelDescription"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelLclGwAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelLclGwAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelRemGwAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelRemGwAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelPublicSvcId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelSecurityPolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelKeyingType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelDynTransformId1"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelDynTransformId2"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelDynTransformId3"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelDynTransformId4"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIkePolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIkePreSharedKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIsakmpState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIsakmpEstabTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIsakmpNegLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumDpdTx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumDpdAckTx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumDpdAckRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumExpRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumInvalidDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumCtrlPktsTx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumCtrlPktsRx"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumCtrlTxErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelNumCtrlRxErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyTableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsTblLastChangd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsLclAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsLclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsLclAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsLclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsRemAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsRemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsRemAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPolicyParamsRemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSATableLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSARowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSALastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAEncryptionKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAAuthenticationKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSASpi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAManualTransformId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStorageType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAEstablishedTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSANegotiatedLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsBytesProcessed"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsBytesProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsBytesProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPktsProcessed"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPktsProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPktsProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsCryptoErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsReplayErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsSAErrors"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPolicyErrors"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV6v0Group.setStatus("current")

tmnxIPsecMdaDpStatsV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 2)
)
tmnxIPsecMdaDpStatsV6v1Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptPktsLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptPktsHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptBytesLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsEncryptBytesHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptPktsLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptPktsHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptBytesLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsDecryptBytesHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsTxPktErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBDropPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBDropPktsLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBDropPktsHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBSAMisses"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBSAMissesLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBSAMissesHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsOutBPolicyEntryMisses"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBDropPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBDropPktsLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBDropPktsHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBSAMisses"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBSAMissesLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBSAMissesHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsInBIPDstSrcMismatches"))
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsV6v1Group.setStatus("current")

tIPsecTnlTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 3)
)
tIPsecTnlTempGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDescr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId1"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId2"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId3"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempDynKeyTransformId4"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempReverseRoute"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempTblLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAuthMethod"))
)
if mibBuilder.loadTexts:
    tIPsecTnlTempGroup.setStatus("current")

tmnxIPsecGWGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 4)
)
tmnxIPsecGWGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelAutoEstablish"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLastMgmtChange"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWSecureService"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTunnelPolicyTemp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePreShared"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclX509Cert"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclPrivateKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCACert"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCACertRevocList"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthenticationKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncryptionKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEstablishedTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSANegotiatedLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSASpi"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsCryptoErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPolicyErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsReplayErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsSAErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIPsecSALifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpEstabTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpNegLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlRxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlTxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumExpRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumInvalidDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPfsDHGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlHasBiDirectionalSA"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIfIndex"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpPrefixLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateSvcId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlTempId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskXAuthTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPskTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWGroup.setStatus("obsolete")

tmnxIPsecNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 5)
)
tmnxIPsecNotifyObjsGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifReason"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfDestIp"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfDestIpType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfIfName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfSessState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfSvcId"))
)
if mibBuilder.loadTexts:
    tmnxIPsecNotifyObjsGroup.setStatus("current")

tmnxIPsecTnlBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 6)
)
tmnxIPsecTnlBfdGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdDesignate"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSrcAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSrcAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdSessOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelBfdTableLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlBfdGroup.setStatus("current")

tmnxIPsecIkeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 7)
)
tmnxIPsecIkeGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyIkeVersion")
)
if mibBuilder.loadTexts:
    tmnxIPsecIkeGroup.setStatus("current")

tmnxIPsecCertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 8)
)
tmnxIPsecCertGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertTrustAnchor"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLocalIdType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLocalIdValue"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCertFile"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelKeyFile"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCertTrustAnchor"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelLocalIdType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelLocalIdValue"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelClearDfBit"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyOwnAuthMethod"))
)
if mibBuilder.loadTexts:
    tmnxIPsecCertGroup.setStatus("current")

tmnxIpsecObsoletedV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 9)
)
tmnxIpsecObsoletedV10v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCACert"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCACertRevocList"))
)
if mibBuilder.loadTexts:
    tmnxIpsecObsoletedV10v0Group.setStatus("current")

tmnxIPsecGWV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 10)
)
tmnxIPsecGWV10v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelAutoEstablish"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLastMgmtChange"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWSecureService"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTunnelPolicyTemp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePreShared"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclX509Cert"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclPrivateKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthenticationKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncryptionKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEstablishedTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSANegotiatedLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSASpi"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsCryptoErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPolicyErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsReplayErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsSAErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIPsecSALifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpEstabTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpNegLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlRxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlTxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumExpRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumInvalidDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPfsDHGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlHasBiDirectionalSA"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIfIndex"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpPrefixLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateSvcId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlTempId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskXAuthTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPskTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWV10v0Group.setStatus("obsolete")

tmnxIPsecMdaDpStatsV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 11)
)
tmnxIPsecMdaDpStatsV10v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStaticIPsecTnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpDynIPsecTnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpIpGreTnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpIpv4Tnls"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytesHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytesLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPktsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPktsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytesHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytesLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPktsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPktsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDropTime"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDropTimeHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDropTimeLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDropped"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDroppedHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpFragDroppedLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpInFragments"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpInFragmentsHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpInFragmentsLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsReassem"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsReassemHigh32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsReassemLow32"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsDropDfSet"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsDropDfSetLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpPktsDropDfSetHi"))
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpStatsV10v0Group.setStatus("current")

tmnxIPsecMdaDpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 12)
)
tmnxIPsecMdaDpGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytesHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInBytesLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInErrsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPktsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlInPktsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytes"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytesHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutBytesLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrs"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutErrsLo"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPkts"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPktsHi"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGreTnlOutPktsLo"))
)
if mibBuilder.loadTexts:
    tmnxIPsecMdaDpGroup.setStatus("current")

tmnxIPsecV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 13)
)
tmnxIPsecV10v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelHostISA"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlHostISA"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV10v0Group.setStatus("current")

tmnxIPsecV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 14)
)
tmnxIPsecV11v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCSVPrimary"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCSVSecondary"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCSVDefResult"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCSVPrimary"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCSVSecondary"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCSVDefResult"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV11v0Group.setStatus("current")

tmnxIPsecIkev2RatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 15)
)
tmnxIPsecIkev2RatGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskRadiusTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertRadiusTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWEapTunnels"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyLastMgmtChange"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyInclAttr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyRadSrvPlcy"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyLastMgmtChange"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyPassword"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyInclAttr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAuthPlcyRadSrvPlcy"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWRadAuthPolicy"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWRadAcctgPolicy"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyMatchPeerToCert"))
)
if mibBuilder.loadTexts:
    tmnxIPsecIkev2RatGroup.setStatus("current")

tIPsecIkev2RaTunNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 16)
)
tIPsecIkev2RaTunNotifyObjsGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyFailReason")
)
if mibBuilder.loadTexts:
    tIPsecIkev2RaTunNotifyObjsGroup.setStatus("current")

tmnxIPsecTnlDstv12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 17)
)
tmnxIPsecTnlDstv12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddrLastChanged"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddrRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddrTblLastChngd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstAddrResolved"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlDstv12v0Group.setStatus("current")

tmnxIPsecV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 18)
)
tmnxIPsecV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6LclAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6LclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6LclAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6LclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6RemAddrAny"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6RemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6RemAddr"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPlcyParamsV6RemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelEncapIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIcmp6Pkt2Big"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIcmp6NumPkt2Big"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelIcmp6Pkt2BigTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempEncapIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempIcmp6Pkt2Big"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempIcmp6NumPkt2Big"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempIcmp6Pkt2BigTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempClearDfBit"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV12v0Group.setStatus("current")

tIPsecIkev2CertAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 19)
)
tIPsecIkev2CertAuthGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecCompChainCAProfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCertTrstAnchrProf"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertTrstAnchrProf"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorsTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorsRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorsLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorProfTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorProfRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorProfLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelMatchTrustAnchor"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlMatchTrustAnchor"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdCertFile"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdCompChain"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCertProfile"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertProfile"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdKeyFile"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileAdminState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileOperState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfileOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorCAProfDown"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelMatCertEntryId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelCertProfName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlMatCertEntryId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlCertProfName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertProfEntryIdOperFlags"))
)
if mibBuilder.loadTexts:
    tIPsecIkev2CertAuthGroup.setStatus("current")

tIPsecIkev2CertAuthChainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 20)
)
tIPsecIkev2CertAuthChainGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecCertChainCAProfTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertChainCAProfRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecCertChainCAProfLastChgd"))
)
if mibBuilder.loadTexts:
    tIPsecIkev2CertAuthChainGroup.setStatus("current")

tIPsecTsReductionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 21)
)
tIPsecTsReductionGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecGWTsNegSelPlcyLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWTsNegSelPlcyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWTsNegSelPlcyTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecGWTsNegSelPlcyTsList"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryFrAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryFrAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryPfxAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryPfxAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryPfxLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryToAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListLclEntryToAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsListTblLastChgd"))
)
if mibBuilder.loadTexts:
    tIPsecTsReductionGroup.setStatus("current")

tIPsecRUSATrafficSelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 22)
)
tIPsecRUSATrafficSelGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelLastChgd")
)
if mibBuilder.loadTexts:
    tIPsecRUSATrafficSelGroup.setStatus("current")

tmnxIPsecGWV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 23)
)
tmnxIPsecGWV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelAutoEstablish"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIfName"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLastMgmtChange"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWSecureService"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTblLastChgd"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWTunnelPolicyTemp"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePolicyId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWIkePreShared"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclX509Cert"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWLclPrivateKey"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWOperFlags"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAAuthenticationKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncrAlgorithm"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEncryptionKey"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAEstablishedTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSANegotiatedLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSASpi"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsBytesProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsCryptoErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcHigh32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcLow32"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPktsProcessed"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPolicyErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsReplayErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsSAErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIPsecSALifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpEstabTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpNegLifeTime"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlIsakmpState"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlPktsTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlRxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumCtrlTxErrors"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdAckTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumDpdTx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumExpRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlNumInvalidDpdRx"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPfsDHGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlHasBiDirectionalSA"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIfIndex"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpPrefixLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateIpAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlPrivateSvcId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlReplayWindow"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlTempId"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskXAuthTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWPskTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWCertTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecPskTunnels"))
)
if mibBuilder.loadTexts:
    tmnxIPsecGWV12v0Group.setStatus("current")

tmnxIpsecObsoletedV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 24)
)
tmnxIpsecObsoletedV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSALclAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddrType"))
)
if mibBuilder.loadTexts:
    tmnxIpsecObsoletedV12v0Group.setStatus("current")

tIkev2SendUnSolCfgAttr12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 26)
)
tIkev2SendUnSolCfgAttr12v0Group.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyRelayUnSolCfgAttr")
)
if mibBuilder.loadTexts:
    tIkev2SendUnSolCfgAttr12v0Group.setStatus("current")

tmnxIPsecSAStatsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 27)
)
tmnxIPsecSAStatsV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPreEncapFragCnt"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPreEncapFragLtSz"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPstEncapFragCnt"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsPstEncapFragLtSz"))
)
if mibBuilder.loadTexts:
    tmnxIPsecSAStatsV12v0Group.setStatus("current")

tmnxIPsecRUSAStatsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 28)
)
tmnxIPsecRUSAStatsV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPreEncapFragCnt"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPreEncapFragLtSz"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPostEncapFragCnt"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAStatsPostEncapFragLtSz"))
)
if mibBuilder.loadTexts:
    tmnxIPsecRUSAStatsV12v0Group.setStatus("current")

tmnxIPsecEncapNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 29)
)
tmnxIPsecEncapNotifyObjsGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifIPsecTunnelName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigEncapIpMtu"))
)
if mibBuilder.loadTexts:
    tmnxIPsecEncapNotifyObjsGroup.setStatus("current")

tmnxIPsecTnlOperChgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 30)
)
tmnxIPsecTnlOperChgGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperChanged"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUTnlOperChanged"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTnlOperChgGroup.setStatus("current")

tmnxIkePolicyAutoEapRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 31)
)
tmnxIkePolicyAutoEapRadiusGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecGWAutoEapRadiusTunnels"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAutoEapMethod"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAutoEapOwnMethod"))
)
if mibBuilder.loadTexts:
    tmnxIkePolicyAutoEapRadiusGroup.setStatus("current")

tmnxSecNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 35)
)
tmnxSecNotifyObjsV12v0Group.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfileName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfEntryId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCaProfNames"))
)
if mibBuilder.loadTexts:
    tmnxSecNotifyObjsV12v0Group.setStatus("current")


# Notification objects

tIPsecRUTnlFailToCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 1)
)
tIPsecRUTnlFailToCreate.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifReason"))
)
if mibBuilder.loadTexts:
    tIPsecRUTnlFailToCreate.setStatus(
        "current"
    )

tIPsecRUSAFailToAddRoute = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 2)
)
tIPsecRUSAFailToAddRoute.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAddr"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSARemAPrefLen"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifReason"))
)
if mibBuilder.loadTexts:
    tIPsecRUSAFailToAddRoute.setStatus(
        "current"
    )

tIPsecBfdIntfSessStateChgd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 3)
)
tIPsecBfdIntfSessStateChgd.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfSvcId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfIfName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfDestIpType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfDestIp"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifBfdIntfSessState"))
)
if mibBuilder.loadTexts:
    tIPsecBfdIntfSessStateChgd.setStatus(
        "current"
    )

tIPsecRadAcctPlcyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 4)
)
tIPsecRadAcctPlcyFailure.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyRowStatus"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyFailReason"))
)
if mibBuilder.loadTexts:
    tIPsecRadAcctPlcyFailure.setStatus(
        "current"
    )

tIPSecTrustAnchorPrfOprChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 5)
)
tIPSecTrustAnchorPrfOprChg.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecTrustAnchorCAProfDown")
)
if mibBuilder.loadTexts:
    tIPSecTrustAnchorPrfOprChg.setStatus(
        "current"
    )

tIPsecTunnelEncapIpMtuTooSmall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 6)
)
tIPsecTunnelEncapIpMtuTooSmall.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifIPsecTunnelName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigEncapIpMtu"))
)
if mibBuilder.loadTexts:
    tIPsecTunnelEncapIpMtuTooSmall.setStatus(
        "current"
    )

tIPsecRuTnlEncapIpMtuTooSmall = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 7)
)
tIPsecRuTnlEncapIpMtuTooSmall.setObjects(
      *(("TIMETRA-SERV-MIB", "svcId"),
        ("TIMETRA-SAP-MIB", "sapPortId"),
        ("TIMETRA-SAP-MIB", "sapEncapValue"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddrType"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlInetAddress"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifRUTnlPort"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigIpMtu"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifEncapOverhead"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifConfigEncapIpMtu"))
)
if mibBuilder.loadTexts:
    tIPsecRuTnlEncapIpMtuTooSmall.setStatus(
        "current"
    )

tmnxSecNotifCmptedCertHashChngd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 8)
)
tmnxSecNotifCmptedCertHashChngd.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfileName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfEntryId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCaProfNames"))
)
if mibBuilder.loadTexts:
    tmnxSecNotifCmptedCertHashChngd.setStatus(
        "current"
    )

tmnxSecNotifCmptedCertChnChngd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 9)
)
tmnxSecNotifCmptedCertChnChngd.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfileName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfEntryId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCaProfNames"))
)
if mibBuilder.loadTexts:
    tmnxSecNotifCmptedCertChnChngd.setStatus(
        "current"
    )

tmnxSecNotifSendChnNotInCmptChn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 10)
)
tmnxSecNotifSendChnNotInCmptChn.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfileName"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCertProfEntryId"),
        ("TIMETRA-IPSEC-MIB", "tIPsecNotifCaProfNames"))
)
if mibBuilder.loadTexts:
    tmnxSecNotifSendChnNotInCmptChn.setStatus(
        "current"
    )

tmnxIPsecTunnelOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 48, 0, 11)
)
tmnxIPsecTunnelOperStateChange.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelAdminState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperState"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxIPsecTunnelOperStateChange.setStatus(
        "current"
    )


# Notifications groups

tmnxCrtAutRecNotifV12v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 2, 36)
)
tmnxCrtAutRecNotifV12v0Grp.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxSecNotifCmptedCertHashChngd"),
        ("TIMETRA-IPSEC-MIB", "tmnxSecNotifCmptedCertChnChngd"),
        ("TIMETRA-IPSEC-MIB", "tmnxSecNotifSendChnNotInCmptChn"))
)
if mibBuilder.loadTexts:
    tmnxCrtAutRecNotifV12v0Grp.setStatus(
        "current"
    )

tmnxIPsecNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 1)
)
tmnxIPsecNotifGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecRUTnlFailToCreate"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSAFailToAddRoute"),
        ("TIMETRA-IPSEC-MIB", "tIPsecBfdIntfSessStateChgd"))
)
if mibBuilder.loadTexts:
    tmnxIPsecNotifGroup.setStatus(
        "current"
    )

tIPsecIkev2RaTunNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 2)
)
tIPsecIkev2RaTunNotifGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPsecRadAcctPlcyFailure")
)
if mibBuilder.loadTexts:
    tIPsecIkev2RaTunNotifGroup.setStatus(
        "current"
    )

tIPSecTrustAnchorProfNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 3)
)
tIPSecTrustAnchorProfNotifGroup.setObjects(
    ("TIMETRA-IPSEC-MIB", "tIPSecTrustAnchorPrfOprChg")
)
if mibBuilder.loadTexts:
    tIPSecTrustAnchorProfNotifGroup.setStatus(
        "current"
    )

tIPSecTunnelEncapNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 4)
)
tIPSecTunnelEncapNotifGroup.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tIPsecTunnelEncapIpMtuTooSmall"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRuTnlEncapIpMtuTooSmall"))
)
if mibBuilder.loadTexts:
    tIPSecTunnelEncapNotifGroup.setStatus(
        "current"
    )

tmnxIPSecTunnelNotifV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 3, 5)
)
tmnxIPSecTunnelNotifV11v0Group.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIPsecTunnelOperStateChange")
)
if mibBuilder.loadTexts:
    tmnxIPSecTunnelNotifV11v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxIPsecCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 1)
)
tmnxIPsecCompliance.setObjects(
    ("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group")
)
if mibBuilder.loadTexts:
    tmnxIPsecCompliance.setStatus(
        "obsolete"
    )

tmnxIPsecV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 2)
)
tmnxIPsecV6v1Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 3)
)
tmnxIPsecV7v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 4)
)
tmnxIPsecV8v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 5)
)
tmnxIPsecV9v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecCertGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 6)
)
tmnxIPsecV10v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecCertGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlOperChgGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 7)
)
tmnxIPsecV11v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecCertGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV11v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkev2RatGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2RaTunNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2RaTunNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlOperChgGroup"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxIPsecV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 48, 1, 8)
)
tmnxIPsecV12v0Compliance.setObjects(
      *(("TIMETRA-IPSEC-MIB", "tmnxIPsecV6v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV6v1Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTnlTempGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecGWV12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlBfdGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkeGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecCertGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV11v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecMdaDpStatsV10v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecIkev2RatGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2RaTunNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2RaTunNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlDstv12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecV12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2CertAuthGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecIkev2CertAuthChainGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecTsReductionGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPsecRUSATrafficSelGroup"),
        ("TIMETRA-IPSEC-MIB", "tIkev2SendUnSolCfgAttr12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tIPSecTrustAnchorProfNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecSAStatsV12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecRUSAStatsV12v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecEncapNotifyObjsGroup"),
        ("TIMETRA-IPSEC-MIB", "tIPSecTunnelEncapNotifGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPsecTnlOperChgGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIkePolicyAutoEapRadiusGroup"),
        ("TIMETRA-IPSEC-MIB", "tmnxIPSecTunnelNotifV11v0Group"),
        ("TIMETRA-IPSEC-MIB", "tmnxCrtAutRecNotifV12v0Grp"),
        ("TIMETRA-IPSEC-MIB", "tmnxSecNotifyObjsV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxIPsecV12v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-IPSEC-MIB",
    **{"TmnxIPsecTransformId": TmnxIPsecTransformId,
       "TmnxIPsecTransformIdOrZero": TmnxIPsecTransformIdOrZero,
       "TmnxAuthAlgorithm": TmnxAuthAlgorithm,
       "TmnxEncrAlgorithm": TmnxEncrAlgorithm,
       "TmnxIkePolicyId": TmnxIkePolicyId,
       "TmnxIkePolicyIdOrZero": TmnxIkePolicyIdOrZero,
       "TmnxIkeVersion": TmnxIkeVersion,
       "TmnxIkePolicyIkeMode": TmnxIkePolicyIkeMode,
       "TmnxIkePolicyDHGroup": TmnxIkePolicyDHGroup,
       "TmnxIkePolicyDHGroupOrZero": TmnxIkePolicyDHGroupOrZero,
       "TmnxIPsecPolicyId": TmnxIPsecPolicyId,
       "TmnxIPsecPolicyIdOrZero": TmnxIPsecPolicyIdOrZero,
       "TmnxIPsecKeyingType": TmnxIPsecKeyingType,
       "TmnxIPsecDirection": TmnxIPsecDirection,
       "TmnxIPsecDirection2": TmnxIPsecDirection2,
       "TmnxIPsecProtocol": TmnxIPsecProtocol,
       "TmnxIPsecLocalIdType": TmnxIPsecLocalIdType,
       "TmnxCertRevStatus": TmnxCertRevStatus,
       "TmnxCertRevStatusOrNone": TmnxCertRevStatusOrNone,
       "TmnxIkePolicyRelayUnSolCfgAttr": TmnxIkePolicyRelayUnSolCfgAttr,
       "TmnxIpsecTrafficSelSide": TmnxIpsecTrafficSelSide,
       "timetraIPsecMIBModule": timetraIPsecMIBModule,
       "tmnxIPsecConformance": tmnxIPsecConformance,
       "tmnxIPsecCompliances": tmnxIPsecCompliances,
       "tmnxIPsecCompliance": tmnxIPsecCompliance,
       "tmnxIPsecV6v1Compliance": tmnxIPsecV6v1Compliance,
       "tmnxIPsecV7v0Compliance": tmnxIPsecV7v0Compliance,
       "tmnxIPsecV8v0Compliance": tmnxIPsecV8v0Compliance,
       "tmnxIPsecV9v0Compliance": tmnxIPsecV9v0Compliance,
       "tmnxIPsecV10v0Compliance": tmnxIPsecV10v0Compliance,
       "tmnxIPsecV11v0Compliance": tmnxIPsecV11v0Compliance,
       "tmnxIPsecV12v0Compliance": tmnxIPsecV12v0Compliance,
       "tmnxIPsecGroups": tmnxIPsecGroups,
       "tmnxIPsecV6v0Group": tmnxIPsecV6v0Group,
       "tmnxIPsecMdaDpStatsV6v1Group": tmnxIPsecMdaDpStatsV6v1Group,
       "tIPsecTnlTempGroup": tIPsecTnlTempGroup,
       "tmnxIPsecGWGroup": tmnxIPsecGWGroup,
       "tmnxIPsecNotifyObjsGroup": tmnxIPsecNotifyObjsGroup,
       "tmnxIPsecTnlBfdGroup": tmnxIPsecTnlBfdGroup,
       "tmnxIPsecIkeGroup": tmnxIPsecIkeGroup,
       "tmnxIPsecCertGroup": tmnxIPsecCertGroup,
       "tmnxIpsecObsoletedV10v0Group": tmnxIpsecObsoletedV10v0Group,
       "tmnxIPsecGWV10v0Group": tmnxIPsecGWV10v0Group,
       "tmnxIPsecMdaDpStatsV10v0Group": tmnxIPsecMdaDpStatsV10v0Group,
       "tmnxIPsecMdaDpGroup": tmnxIPsecMdaDpGroup,
       "tmnxIPsecV10v0Group": tmnxIPsecV10v0Group,
       "tmnxIPsecV11v0Group": tmnxIPsecV11v0Group,
       "tmnxIPsecIkev2RatGroup": tmnxIPsecIkev2RatGroup,
       "tIPsecIkev2RaTunNotifyObjsGroup": tIPsecIkev2RaTunNotifyObjsGroup,
       "tmnxIPsecTnlDstv12v0Group": tmnxIPsecTnlDstv12v0Group,
       "tmnxIPsecV12v0Group": tmnxIPsecV12v0Group,
       "tIPsecIkev2CertAuthGroup": tIPsecIkev2CertAuthGroup,
       "tIPsecIkev2CertAuthChainGroup": tIPsecIkev2CertAuthChainGroup,
       "tIPsecTsReductionGroup": tIPsecTsReductionGroup,
       "tIPsecRUSATrafficSelGroup": tIPsecRUSATrafficSelGroup,
       "tmnxIPsecGWV12v0Group": tmnxIPsecGWV12v0Group,
       "tmnxIpsecObsoletedV12v0Group": tmnxIpsecObsoletedV12v0Group,
       "tIkev2SendUnSolCfgAttr12v0Group": tIkev2SendUnSolCfgAttr12v0Group,
       "tmnxIPsecSAStatsV12v0Group": tmnxIPsecSAStatsV12v0Group,
       "tmnxIPsecRUSAStatsV12v0Group": tmnxIPsecRUSAStatsV12v0Group,
       "tmnxIPsecEncapNotifyObjsGroup": tmnxIPsecEncapNotifyObjsGroup,
       "tmnxIPsecTnlOperChgGroup": tmnxIPsecTnlOperChgGroup,
       "tmnxIkePolicyAutoEapRadiusGroup": tmnxIkePolicyAutoEapRadiusGroup,
       "tmnxSecNotifyObjsV12v0Group": tmnxSecNotifyObjsV12v0Group,
       "tmnxCrtAutRecNotifV12v0Grp": tmnxCrtAutRecNotifV12v0Grp,
       "tmnxIPsecNotifGroups": tmnxIPsecNotifGroups,
       "tmnxIPsecNotifGroup": tmnxIPsecNotifGroup,
       "tIPsecIkev2RaTunNotifGroup": tIPsecIkev2RaTunNotifGroup,
       "tIPSecTrustAnchorProfNotifGroup": tIPSecTrustAnchorProfNotifGroup,
       "tIPSecTunnelEncapNotifGroup": tIPSecTunnelEncapNotifGroup,
       "tmnxIPSecTunnelNotifV11v0Group": tmnxIPSecTunnelNotifV11v0Group,
       "tmnxIPsecObjects": tmnxIPsecObjects,
       "tmnxIPsecTransformTblLastChanged": tmnxIPsecTransformTblLastChanged,
       "tmnxIPsecTransformTable": tmnxIPsecTransformTable,
       "tmnxIPsecTransformEntry": tmnxIPsecTransformEntry,
       "tmnxIPsecTransformId": tmnxIPsecTransformId,
       "tmnxIPsecTransformRowStatus": tmnxIPsecTransformRowStatus,
       "tmnxIPsecTransformLastChanged": tmnxIPsecTransformLastChanged,
       "tmnxIPsecTransformAuthAlgorithm": tmnxIPsecTransformAuthAlgorithm,
       "tmnxIPsecTransformEncrAlgorithm": tmnxIPsecTransformEncrAlgorithm,
       "tmnxIkePolicyTableLastChanged": tmnxIkePolicyTableLastChanged,
       "tmnxIkePolicyTable": tmnxIkePolicyTable,
       "tmnxIkePolicyEntry": tmnxIkePolicyEntry,
       "tmnxIkePolicyId": tmnxIkePolicyId,
       "tmnxIkePolicyRowStatus": tmnxIkePolicyRowStatus,
       "tmnxIkePolicyLastChanged": tmnxIkePolicyLastChanged,
       "tmnxIkePolicyDescription": tmnxIkePolicyDescription,
       "tmnxIkePolicyIkeMode": tmnxIkePolicyIkeMode,
       "tmnxIkePolicyDHGroup": tmnxIkePolicyDHGroup,
       "tmnxIkePolicyPFSEnabled": tmnxIkePolicyPFSEnabled,
       "tmnxIkePolicyPFSDHGroup": tmnxIkePolicyPFSDHGroup,
       "tmnxIkePolicyAuthAlgorithm": tmnxIkePolicyAuthAlgorithm,
       "tmnxIkePolicyEncrAlgorithm": tmnxIkePolicyEncrAlgorithm,
       "tmnxIkePolicyIsakmpLifeTime": tmnxIkePolicyIsakmpLifeTime,
       "tmnxIkePolicyIPsecLifeTime": tmnxIkePolicyIPsecLifeTime,
       "tmnxIkePolicyNatTraversal": tmnxIkePolicyNatTraversal,
       "tmnxIkePolicyNatTKeepAliveIntvl": tmnxIkePolicyNatTKeepAliveIntvl,
       "tmnxIkePolicyNatTBehindNatOnly": tmnxIkePolicyNatTBehindNatOnly,
       "tmnxIkePolicyDpd": tmnxIkePolicyDpd,
       "tmnxIkePolicyDpdInterval": tmnxIkePolicyDpdInterval,
       "tmnxIkePolicyDpdMaxRetries": tmnxIkePolicyDpdMaxRetries,
       "tmnxIkePolicyAuthMethod": tmnxIkePolicyAuthMethod,
       "tmnxIkePolicyIkeVersion": tmnxIkePolicyIkeVersion,
       "tmnxIkePolicyOwnAuthMethod": tmnxIkePolicyOwnAuthMethod,
       "tmnxIkePolicyMatchPeerToCert": tmnxIkePolicyMatchPeerToCert,
       "tmnxIkePolicyRelayUnSolCfgAttr": tmnxIkePolicyRelayUnSolCfgAttr,
       "tmnxIkePolicyAutoEapMethod": tmnxIkePolicyAutoEapMethod,
       "tmnxIkePolicyAutoEapOwnMethod": tmnxIkePolicyAutoEapOwnMethod,
       "tmnxIPsecTunnelTableLastChanged": tmnxIPsecTunnelTableLastChanged,
       "tmnxIPsecTunnelTable": tmnxIPsecTunnelTable,
       "tmnxIPsecTunnelEntry": tmnxIPsecTunnelEntry,
       "tmnxIPsecTunnelName": tmnxIPsecTunnelName,
       "tmnxIPsecTunnelRowStatus": tmnxIPsecTunnelRowStatus,
       "tmnxIPsecTunnelLastChanged": tmnxIPsecTunnelLastChanged,
       "tmnxIPsecTunnelDescription": tmnxIPsecTunnelDescription,
       "tmnxIPsecTunnelLclGwAddrType": tmnxIPsecTunnelLclGwAddrType,
       "tmnxIPsecTunnelLclGwAddr": tmnxIPsecTunnelLclGwAddr,
       "tmnxIPsecTunnelRemGwAddrType": tmnxIPsecTunnelRemGwAddrType,
       "tmnxIPsecTunnelRemGwAddr": tmnxIPsecTunnelRemGwAddr,
       "tmnxIPsecTunnelPublicSvcId": tmnxIPsecTunnelPublicSvcId,
       "tmnxIPsecTunnelSecurityPolicyId": tmnxIPsecTunnelSecurityPolicyId,
       "tmnxIPsecTunnelKeyingType": tmnxIPsecTunnelKeyingType,
       "tmnxIPsecTunnelDynTransformId1": tmnxIPsecTunnelDynTransformId1,
       "tmnxIPsecTunnelDynTransformId2": tmnxIPsecTunnelDynTransformId2,
       "tmnxIPsecTunnelDynTransformId3": tmnxIPsecTunnelDynTransformId3,
       "tmnxIPsecTunnelDynTransformId4": tmnxIPsecTunnelDynTransformId4,
       "tmnxIPsecTunnelIkePolicyId": tmnxIPsecTunnelIkePolicyId,
       "tmnxIPsecTunnelIkePreSharedKey": tmnxIPsecTunnelIkePreSharedKey,
       "tmnxIPsecTunnelAdminState": tmnxIPsecTunnelAdminState,
       "tmnxIPsecTunnelOperState": tmnxIPsecTunnelOperState,
       "tmnxIPsecTunnelOperFlags": tmnxIPsecTunnelOperFlags,
       "tmnxIPsecTunnelReplayWindow": tmnxIPsecTunnelReplayWindow,
       "tmnxIPsecTunnelAutoEstablish": tmnxIPsecTunnelAutoEstablish,
       "tmnxIPsecTunnelBfdDesignate": tmnxIPsecTunnelBfdDesignate,
       "tmnxIPsecTunnelCertTrustAnchor": tmnxIPsecTunnelCertTrustAnchor,
       "tmnxIPsecTunnelCertFile": tmnxIPsecTunnelCertFile,
       "tmnxIPsecTunnelKeyFile": tmnxIPsecTunnelKeyFile,
       "tmnxIPsecTunnelLocalIdType": tmnxIPsecTunnelLocalIdType,
       "tmnxIPsecTunnelLocalIdValue": tmnxIPsecTunnelLocalIdValue,
       "tmnxIPsecTunnelClearDfBit": tmnxIPsecTunnelClearDfBit,
       "tmnxIPsecTunnelIpMtu": tmnxIPsecTunnelIpMtu,
       "tmnxIPsecTunnelHostISA": tmnxIPsecTunnelHostISA,
       "tmnxIPsecTunnelCSVPrimary": tmnxIPsecTunnelCSVPrimary,
       "tmnxIPsecTunnelCSVSecondary": tmnxIPsecTunnelCSVSecondary,
       "tmnxIPsecTunnelCSVDefResult": tmnxIPsecTunnelCSVDefResult,
       "tmnxIPsecTunnelCertProfile": tmnxIPsecTunnelCertProfile,
       "tmnxIPsecTunnelMatchTrustAnchor": tmnxIPsecTunnelMatchTrustAnchor,
       "tmnxIPsecTunnelCertTrstAnchrProf": tmnxIPsecTunnelCertTrstAnchrProf,
       "tmnxIPsecTunnelEncapIpMtu": tmnxIPsecTunnelEncapIpMtu,
       "tmnxIPsecTunnelIcmp6Pkt2Big": tmnxIPsecTunnelIcmp6Pkt2Big,
       "tmnxIPsecTunnelIcmp6NumPkt2Big": tmnxIPsecTunnelIcmp6NumPkt2Big,
       "tmnxIPsecTunnelIcmp6Pkt2BigTime": tmnxIPsecTunnelIcmp6Pkt2BigTime,
       "tmnxIPsecTunnelOperChanged": tmnxIPsecTunnelOperChanged,
       "tmnxIPsecTunnelStatsTable": tmnxIPsecTunnelStatsTable,
       "tmnxIPsecTunnelStatsEntry": tmnxIPsecTunnelStatsEntry,
       "tmnxIPsecTunnelIsakmpState": tmnxIPsecTunnelIsakmpState,
       "tmnxIPsecTunnelIsakmpEstabTime": tmnxIPsecTunnelIsakmpEstabTime,
       "tmnxIPsecTunnelIsakmpNegLifeTime": tmnxIPsecTunnelIsakmpNegLifeTime,
       "tmnxIPsecTunnelNumDpdTx": tmnxIPsecTunnelNumDpdTx,
       "tmnxIPsecTunnelNumDpdRx": tmnxIPsecTunnelNumDpdRx,
       "tmnxIPsecTunnelNumDpdAckTx": tmnxIPsecTunnelNumDpdAckTx,
       "tmnxIPsecTunnelNumDpdAckRx": tmnxIPsecTunnelNumDpdAckRx,
       "tmnxIPsecTunnelNumExpRx": tmnxIPsecTunnelNumExpRx,
       "tmnxIPsecTunnelNumInvalidDpdRx": tmnxIPsecTunnelNumInvalidDpdRx,
       "tmnxIPsecTunnelNumCtrlPktsTx": tmnxIPsecTunnelNumCtrlPktsTx,
       "tmnxIPsecTunnelNumCtrlPktsRx": tmnxIPsecTunnelNumCtrlPktsRx,
       "tmnxIPsecTunnelNumCtrlTxErrors": tmnxIPsecTunnelNumCtrlTxErrors,
       "tmnxIPsecTunnelNumCtrlRxErrors": tmnxIPsecTunnelNumCtrlRxErrors,
       "tmnxIPsecTunnelMatCertEntryId": tmnxIPsecTunnelMatCertEntryId,
       "tmnxIPsecTunnelCertProfName": tmnxIPsecTunnelCertProfName,
       "tmnxIPsecPolicyTableLastChanged": tmnxIPsecPolicyTableLastChanged,
       "tmnxIPsecPolicyTable": tmnxIPsecPolicyTable,
       "tmnxIPsecPolicyEntry": tmnxIPsecPolicyEntry,
       "tmnxIPsecPolicyId": tmnxIPsecPolicyId,
       "tmnxIPsecPolicyRowStatus": tmnxIPsecPolicyRowStatus,
       "tmnxIPsecPolicyLastChanged": tmnxIPsecPolicyLastChanged,
       "tmnxIPsecPlcyParamsTblLastChangd": tmnxIPsecPlcyParamsTblLastChangd,
       "tmnxIPsecPolicyParamsTable": tmnxIPsecPolicyParamsTable,
       "tmnxIPsecPolicyParamsEntry": tmnxIPsecPolicyParamsEntry,
       "tmnxIPsecPolicyParamsId": tmnxIPsecPolicyParamsId,
       "tmnxIPsecPolicyParamsRowStatus": tmnxIPsecPolicyParamsRowStatus,
       "tmnxIPsecPolicyParamsLastChanged": tmnxIPsecPolicyParamsLastChanged,
       "tmnxIPsecPolicyParamsLclAddrAny": tmnxIPsecPolicyParamsLclAddrAny,
       "tmnxIPsecPolicyParamsLclAddrType": tmnxIPsecPolicyParamsLclAddrType,
       "tmnxIPsecPolicyParamsLclAddr": tmnxIPsecPolicyParamsLclAddr,
       "tmnxIPsecPolicyParamsLclAPrefLen": tmnxIPsecPolicyParamsLclAPrefLen,
       "tmnxIPsecPolicyParamsRemAddrAny": tmnxIPsecPolicyParamsRemAddrAny,
       "tmnxIPsecPolicyParamsRemAddrType": tmnxIPsecPolicyParamsRemAddrType,
       "tmnxIPsecPolicyParamsRemAddr": tmnxIPsecPolicyParamsRemAddr,
       "tmnxIPsecPolicyParamsRemAPrefLen": tmnxIPsecPolicyParamsRemAPrefLen,
       "tmnxIPsecPlcyParamsV6LclAddrAny": tmnxIPsecPlcyParamsV6LclAddrAny,
       "tmnxIPsecPlcyParamsV6LclAddrType": tmnxIPsecPlcyParamsV6LclAddrType,
       "tmnxIPsecPlcyParamsV6LclAddr": tmnxIPsecPlcyParamsV6LclAddr,
       "tmnxIPsecPlcyParamsV6LclAPrefLen": tmnxIPsecPlcyParamsV6LclAPrefLen,
       "tmnxIPsecPlcyParamsV6RemAddrAny": tmnxIPsecPlcyParamsV6RemAddrAny,
       "tmnxIPsecPlcyParamsV6RemAddrType": tmnxIPsecPlcyParamsV6RemAddrType,
       "tmnxIPsecPlcyParamsV6RemAddr": tmnxIPsecPlcyParamsV6RemAddr,
       "tmnxIPsecPlcyParamsV6RemAPrefLen": tmnxIPsecPlcyParamsV6RemAPrefLen,
       "tmnxIPsecSATableLastChanged": tmnxIPsecSATableLastChanged,
       "tmnxIPsecSATable": tmnxIPsecSATable,
       "tmnxIPsecSAEntry": tmnxIPsecSAEntry,
       "tmnxIPsecSAId": tmnxIPsecSAId,
       "tmnxIPsecSAIndex": tmnxIPsecSAIndex,
       "tmnxIPsecSADirection": tmnxIPsecSADirection,
       "tmnxIPsecSARowStatus": tmnxIPsecSARowStatus,
       "tmnxIPsecSALastChanged": tmnxIPsecSALastChanged,
       "tmnxIPsecSAType": tmnxIPsecSAType,
       "tmnxIPsecSAEncryptionKey": tmnxIPsecSAEncryptionKey,
       "tmnxIPsecSAAuthenticationKey": tmnxIPsecSAAuthenticationKey,
       "tmnxIPsecSASpi": tmnxIPsecSASpi,
       "tmnxIPsecSAManualTransformId": tmnxIPsecSAManualTransformId,
       "tmnxIPsecSAAuthAlgorithm": tmnxIPsecSAAuthAlgorithm,
       "tmnxIPsecSAEncrAlgorithm": tmnxIPsecSAEncrAlgorithm,
       "tmnxIPsecSAStorageType": tmnxIPsecSAStorageType,
       "tmnxIPsecSAEstablishedTime": tmnxIPsecSAEstablishedTime,
       "tmnxIPsecSANegotiatedLifeTime": tmnxIPsecSANegotiatedLifeTime,
       "tmnxIPsecSAStatsTable": tmnxIPsecSAStatsTable,
       "tmnxIPsecSAStatsEntry": tmnxIPsecSAStatsEntry,
       "tmnxIPsecSAStatsBytesProcessed": tmnxIPsecSAStatsBytesProcessed,
       "tmnxIPsecSAStatsBytesProcLow32": tmnxIPsecSAStatsBytesProcLow32,
       "tmnxIPsecSAStatsBytesProcHigh32": tmnxIPsecSAStatsBytesProcHigh32,
       "tmnxIPsecSAStatsPktsProcessed": tmnxIPsecSAStatsPktsProcessed,
       "tmnxIPsecSAStatsPktsProcLow32": tmnxIPsecSAStatsPktsProcLow32,
       "tmnxIPsecSAStatsPktsProcHigh32": tmnxIPsecSAStatsPktsProcHigh32,
       "tmnxIPsecSAStatsCryptoErrors": tmnxIPsecSAStatsCryptoErrors,
       "tmnxIPsecSAStatsReplayErrors": tmnxIPsecSAStatsReplayErrors,
       "tmnxIPsecSAStatsSAErrors": tmnxIPsecSAStatsSAErrors,
       "tmnxIPsecSAStatsPolicyErrors": tmnxIPsecSAStatsPolicyErrors,
       "tmnxIPsecSAStatsEncapOverhead": tmnxIPsecSAStatsEncapOverhead,
       "tmnxIPsecSAStatsPreEncapFragCnt": tmnxIPsecSAStatsPreEncapFragCnt,
       "tmnxIPsecSAStatsPreEncapFragLtSz": tmnxIPsecSAStatsPreEncapFragLtSz,
       "tmnxIPsecSAStatsPstEncapFragCnt": tmnxIPsecSAStatsPstEncapFragCnt,
       "tmnxIPsecSAStatsPstEncapFragLtSz": tmnxIPsecSAStatsPstEncapFragLtSz,
       "tmnxIPsecMdaDpStatsTable": tmnxIPsecMdaDpStatsTable,
       "tmnxIPsecMdaDpStatsEntry": tmnxIPsecMdaDpStatsEntry,
       "tmnxIPsecMdaDpStatsEncryptPkts": tmnxIPsecMdaDpStatsEncryptPkts,
       "tmnxIPsecMdaDpStatsEncryptPktsLow32": tmnxIPsecMdaDpStatsEncryptPktsLow32,
       "tmnxIPsecMdaDpStatsEncryptPktsHigh32": tmnxIPsecMdaDpStatsEncryptPktsHigh32,
       "tmnxIPsecMdaDpStatsEncryptBytes": tmnxIPsecMdaDpStatsEncryptBytes,
       "tmnxIPsecMdaDpStatsEncryptBytesLow32": tmnxIPsecMdaDpStatsEncryptBytesLow32,
       "tmnxIPsecMdaDpStatsEncryptBytesHigh32": tmnxIPsecMdaDpStatsEncryptBytesHigh32,
       "tmnxIPsecMdaDpStatsDecryptPkts": tmnxIPsecMdaDpStatsDecryptPkts,
       "tmnxIPsecMdaDpStatsDecryptPktsLow32": tmnxIPsecMdaDpStatsDecryptPktsLow32,
       "tmnxIPsecMdaDpStatsDecryptPktsHigh32": tmnxIPsecMdaDpStatsDecryptPktsHigh32,
       "tmnxIPsecMdaDpStatsDecryptBytes": tmnxIPsecMdaDpStatsDecryptBytes,
       "tmnxIPsecMdaDpStatsDecryptBytesLow32": tmnxIPsecMdaDpStatsDecryptBytesLow32,
       "tmnxIPsecMdaDpStatsDecryptBytesHigh32": tmnxIPsecMdaDpStatsDecryptBytesHigh32,
       "tmnxIPsecMdaDpStatsTxPktErrs": tmnxIPsecMdaDpStatsTxPktErrs,
       "tmnxIPsecMdaDpStatsOutBDropPkts": tmnxIPsecMdaDpStatsOutBDropPkts,
       "tmnxIPsecMdaDpStatsOutBDropPktsLow32": tmnxIPsecMdaDpStatsOutBDropPktsLow32,
       "tmnxIPsecMdaDpStatsOutBDropPktsHigh32": tmnxIPsecMdaDpStatsOutBDropPktsHigh32,
       "tmnxIPsecMdaDpStatsOutBSAMisses": tmnxIPsecMdaDpStatsOutBSAMisses,
       "tmnxIPsecMdaDpStatsOutBSAMissesLow32": tmnxIPsecMdaDpStatsOutBSAMissesLow32,
       "tmnxIPsecMdaDpStatsOutBSAMissesHigh32": tmnxIPsecMdaDpStatsOutBSAMissesHigh32,
       "tmnxIPsecMdaDpStatsOutBPolicyEntryMisses": tmnxIPsecMdaDpStatsOutBPolicyEntryMisses,
       "tmnxIPsecMdaDpStatsInBDropPkts": tmnxIPsecMdaDpStatsInBDropPkts,
       "tmnxIPsecMdaDpStatsInBDropPktsLow32": tmnxIPsecMdaDpStatsInBDropPktsLow32,
       "tmnxIPsecMdaDpStatsInBDropPktsHigh32": tmnxIPsecMdaDpStatsInBDropPktsHigh32,
       "tmnxIPsecMdaDpStatsInBSAMisses": tmnxIPsecMdaDpStatsInBSAMisses,
       "tmnxIPsecMdaDpStatsInBSAMissesLow32": tmnxIPsecMdaDpStatsInBSAMissesLow32,
       "tmnxIPsecMdaDpStatsInBSAMissesHigh32": tmnxIPsecMdaDpStatsInBSAMissesHigh32,
       "tmnxIPsecMdaDpStatsInBIPDstSrcMismatches": tmnxIPsecMdaDpStatsInBIPDstSrcMismatches,
       "tmnxIPsecMdaDpInFragments": tmnxIPsecMdaDpInFragments,
       "tmnxIPsecMdaDpInFragmentsLow32": tmnxIPsecMdaDpInFragmentsLow32,
       "tmnxIPsecMdaDpInFragmentsHigh32": tmnxIPsecMdaDpInFragmentsHigh32,
       "tmnxIPsecMdaDpPktsReassem": tmnxIPsecMdaDpPktsReassem,
       "tmnxIPsecMdaDpPktsReassemLow32": tmnxIPsecMdaDpPktsReassemLow32,
       "tmnxIPsecMdaDpPktsReassemHigh32": tmnxIPsecMdaDpPktsReassemHigh32,
       "tmnxIPsecMdaDpFragDropTime": tmnxIPsecMdaDpFragDropTime,
       "tmnxIPsecMdaDpFragDropTimeLow32": tmnxIPsecMdaDpFragDropTimeLow32,
       "tmnxIPsecMdaDpFragDropTimeHigh32": tmnxIPsecMdaDpFragDropTimeHigh32,
       "tmnxIPsecMdaDpFragDropped": tmnxIPsecMdaDpFragDropped,
       "tmnxIPsecMdaDpFragDroppedLow32": tmnxIPsecMdaDpFragDroppedLow32,
       "tmnxIPsecMdaDpFragDroppedHigh32": tmnxIPsecMdaDpFragDroppedHigh32,
       "tmnxIPsecMdaDpGreTnlInPkts": tmnxIPsecMdaDpGreTnlInPkts,
       "tmnxIPsecMdaDpGreTnlInPktsLo": tmnxIPsecMdaDpGreTnlInPktsLo,
       "tmnxIPsecMdaDpGreTnlInPktsHi": tmnxIPsecMdaDpGreTnlInPktsHi,
       "tmnxIPsecMdaDpGreTnlInBytes": tmnxIPsecMdaDpGreTnlInBytes,
       "tmnxIPsecMdaDpGreTnlInBytesLo": tmnxIPsecMdaDpGreTnlInBytesLo,
       "tmnxIPsecMdaDpGreTnlInBytesHi": tmnxIPsecMdaDpGreTnlInBytesHi,
       "tmnxIPsecMdaDpGreTnlInErrs": tmnxIPsecMdaDpGreTnlInErrs,
       "tmnxIPsecMdaDpGreTnlInErrsLo": tmnxIPsecMdaDpGreTnlInErrsLo,
       "tmnxIPsecMdaDpGreTnlInErrsHi": tmnxIPsecMdaDpGreTnlInErrsHi,
       "tmnxIPsecMdaDpGreTnlOutPkts": tmnxIPsecMdaDpGreTnlOutPkts,
       "tmnxIPsecMdaDpGreTnlOutPktsLo": tmnxIPsecMdaDpGreTnlOutPktsLo,
       "tmnxIPsecMdaDpGreTnlOutPktsHi": tmnxIPsecMdaDpGreTnlOutPktsHi,
       "tmnxIPsecMdaDpGreTnlOutBytes": tmnxIPsecMdaDpGreTnlOutBytes,
       "tmnxIPsecMdaDpGreTnlOutBytesLo": tmnxIPsecMdaDpGreTnlOutBytesLo,
       "tmnxIPsecMdaDpGreTnlOutBytesHi": tmnxIPsecMdaDpGreTnlOutBytesHi,
       "tmnxIPsecMdaDpGreTnlOutErrs": tmnxIPsecMdaDpGreTnlOutErrs,
       "tmnxIPsecMdaDpGreTnlOutErrsLo": tmnxIPsecMdaDpGreTnlOutErrsLo,
       "tmnxIPsecMdaDpGreTnlOutErrsHi": tmnxIPsecMdaDpGreTnlOutErrsHi,
       "tmnxIPsecMdaDpPktsDropDfSet": tmnxIPsecMdaDpPktsDropDfSet,
       "tmnxIPsecMdaDpPktsDropDfSetLo": tmnxIPsecMdaDpPktsDropDfSetLo,
       "tmnxIPsecMdaDpPktsDropDfSetHi": tmnxIPsecMdaDpPktsDropDfSetHi,
       "tmnxIPsecMdaDpStaticIPsecTnls": tmnxIPsecMdaDpStaticIPsecTnls,
       "tmnxIPsecMdaDpDynIPsecTnls": tmnxIPsecMdaDpDynIPsecTnls,
       "tmnxIPsecMdaDpIpGreTnls": tmnxIPsecMdaDpIpGreTnls,
       "tmnxIPsecMdaDpIpv4Tnls": tmnxIPsecMdaDpIpv4Tnls,
       "tIPsecTnlTempTblLastChanged": tIPsecTnlTempTblLastChanged,
       "tIPsecTnlTempTable": tIPsecTnlTempTable,
       "tIPsecTnlTempEntry": tIPsecTnlTempEntry,
       "tIPsecTnlTempId": tIPsecTnlTempId,
       "tIPsecTnlTempRowStatus": tIPsecTnlTempRowStatus,
       "tIPsecTnlTempLastChanged": tIPsecTnlTempLastChanged,
       "tIPsecTnlTempDescr": tIPsecTnlTempDescr,
       "tIPsecTnlTempReverseRoute": tIPsecTnlTempReverseRoute,
       "tIPsecTnlTempDynKeyTransformId1": tIPsecTnlTempDynKeyTransformId1,
       "tIPsecTnlTempDynKeyTransformId2": tIPsecTnlTempDynKeyTransformId2,
       "tIPsecTnlTempDynKeyTransformId3": tIPsecTnlTempDynKeyTransformId3,
       "tIPsecTnlTempDynKeyTransformId4": tIPsecTnlTempDynKeyTransformId4,
       "tIPsecTnlTempReplayWindow": tIPsecTnlTempReplayWindow,
       "tIPsecTnlTempIpMtu": tIPsecTnlTempIpMtu,
       "tIPsecTnlTempEncapIpMtu": tIPsecTnlTempEncapIpMtu,
       "tIPsecTnlTempIcmp6Pkt2Big": tIPsecTnlTempIcmp6Pkt2Big,
       "tIPsecTnlTempIcmp6NumPkt2Big": tIPsecTnlTempIcmp6NumPkt2Big,
       "tIPsecTnlTempIcmp6Pkt2BigTime": tIPsecTnlTempIcmp6Pkt2BigTime,
       "tIPsecTnlTempClearDfBit": tIPsecTnlTempClearDfBit,
       "tmnxIPsecGWTblLastChgd": tmnxIPsecGWTblLastChgd,
       "tmnxIPsecGWTable": tmnxIPsecGWTable,
       "tmnxIPsecGWEntry": tmnxIPsecGWEntry,
       "tmnxIPsecGWRowStatus": tmnxIPsecGWRowStatus,
       "tmnxIPsecGWLastMgmtChange": tmnxIPsecGWLastMgmtChange,
       "tmnxIPsecGWAdminState": tmnxIPsecGWAdminState,
       "tmnxIPsecGWOperState": tmnxIPsecGWOperState,
       "tmnxIPsecGWTunnelPolicyTemp": tmnxIPsecGWTunnelPolicyTemp,
       "tmnxIPsecGWSecureService": tmnxIPsecGWSecureService,
       "tmnxIPsecGWIfName": tmnxIPsecGWIfName,
       "tmnxIPsecGWInetAddrType": tmnxIPsecGWInetAddrType,
       "tmnxIPsecGWInetAddress": tmnxIPsecGWInetAddress,
       "tmnxIPsecGWIkePolicyId": tmnxIPsecGWIkePolicyId,
       "tmnxIPsecGWIkePreShared": tmnxIPsecGWIkePreShared,
       "tmnxIPsecGWLclX509Cert": tmnxIPsecGWLclX509Cert,
       "tmnxIPsecGWLclPrivateKey": tmnxIPsecGWLclPrivateKey,
       "tmnxIPsecGWOperFlags": tmnxIPsecGWOperFlags,
       "tmnxIPsecGWCACert": tmnxIPsecGWCACert,
       "tmnxIPsecGWCACertRevocList": tmnxIPsecGWCACertRevocList,
       "tmnxIPsecGWName": tmnxIPsecGWName,
       "tmnxIPsecGWCertTrustAnchor": tmnxIPsecGWCertTrustAnchor,
       "tmnxIPsecGWLocalIdType": tmnxIPsecGWLocalIdType,
       "tmnxIPsecGWLocalIdValue": tmnxIPsecGWLocalIdValue,
       "tmnxIPsecGWCSVPrimary": tmnxIPsecGWCSVPrimary,
       "tmnxIPsecGWCSVSecondary": tmnxIPsecGWCSVSecondary,
       "tmnxIPsecGWCSVDefResult": tmnxIPsecGWCSVDefResult,
       "tmnxIPsecGWRadAcctgPolicy": tmnxIPsecGWRadAcctgPolicy,
       "tmnxIPsecGWRadAuthPolicy": tmnxIPsecGWRadAuthPolicy,
       "tmnxIPsecGWCertProfile": tmnxIPsecGWCertProfile,
       "tmnxIPsecGWCertTrstAnchrProf": tmnxIPsecGWCertTrstAnchrProf,
       "tIPsecRUTnlTable": tIPsecRUTnlTable,
       "tIPsecRUTnlEntry": tIPsecRUTnlEntry,
       "tIPsecRUTnlInetAddrType": tIPsecRUTnlInetAddrType,
       "tIPsecRUTnlInetAddress": tIPsecRUTnlInetAddress,
       "tIPsecRUTnlPort": tIPsecRUTnlPort,
       "tIPsecRUTnlPrivateIpAddrType": tIPsecRUTnlPrivateIpAddrType,
       "tIPsecRUTnlPrivateIpAddr": tIPsecRUTnlPrivateIpAddr,
       "tIPsecRUTnlPrivateIpPrefixLen": tIPsecRUTnlPrivateIpPrefixLen,
       "tIPsecRUTnlTempId": tIPsecRUTnlTempId,
       "tIPsecRUTnlIPsecSALifeTime": tIPsecRUTnlIPsecSALifeTime,
       "tIPsecRUTnlPfsDHGroup": tIPsecRUTnlPfsDHGroup,
       "tIPsecRUTnlReplayWindow": tIPsecRUTnlReplayWindow,
       "tIPsecRUTnlPrivateSvcId": tIPsecRUTnlPrivateSvcId,
       "tIPsecRUTnlPrivateIfIndex": tIPsecRUTnlPrivateIfIndex,
       "tIPsecRUTnlHasBiDirectionalSA": tIPsecRUTnlHasBiDirectionalSA,
       "tIPsecRUTnlHostISA": tIPsecRUTnlHostISA,
       "tIPsecRUTnlMatchTrustAnchor": tIPsecRUTnlMatchTrustAnchor,
       "tIPsecRUTnlOperChanged": tIPsecRUTnlOperChanged,
       "tIPsecRUTnlStatsTable": tIPsecRUTnlStatsTable,
       "tIPsecRUTnlStatsEntry": tIPsecRUTnlStatsEntry,
       "tIPsecRUTnlIsakmpState": tIPsecRUTnlIsakmpState,
       "tIPsecRUTnlIsakmpEstabTime": tIPsecRUTnlIsakmpEstabTime,
       "tIPsecRUTnlIsakmpNegLifeTime": tIPsecRUTnlIsakmpNegLifeTime,
       "tIPsecRUTnlNumDpdTx": tIPsecRUTnlNumDpdTx,
       "tIPsecRUTnlNumDpdRx": tIPsecRUTnlNumDpdRx,
       "tIPsecRUTnlNumDpdAckTx": tIPsecRUTnlNumDpdAckTx,
       "tIPsecRUTnlNumDpdAckRx": tIPsecRUTnlNumDpdAckRx,
       "tIPsecRUTnlNumExpRx": tIPsecRUTnlNumExpRx,
       "tIPsecRUTnlNumInvalidDpdRx": tIPsecRUTnlNumInvalidDpdRx,
       "tIPsecRUTnlNumCtrlPktsTx": tIPsecRUTnlNumCtrlPktsTx,
       "tIPsecRUTnlNumCtrlPktsRx": tIPsecRUTnlNumCtrlPktsRx,
       "tIPsecRUTnlNumCtrlTxErrors": tIPsecRUTnlNumCtrlTxErrors,
       "tIPsecRUTnlNumCtrlRxErrors": tIPsecRUTnlNumCtrlRxErrors,
       "tIPsecRUTnlMatCertEntryId": tIPsecRUTnlMatCertEntryId,
       "tIPsecRUTnlCertProfName": tIPsecRUTnlCertProfName,
       "tIPsecRUSATable": tIPsecRUSATable,
       "tIPsecRUSAEntry": tIPsecRUSAEntry,
       "tIPsecRUSAId": tIPsecRUSAId,
       "tIPsecRUSAIndex": tIPsecRUSAIndex,
       "tIPsecRUSADirection": tIPsecRUSADirection,
       "tIPsecRUSAEncryptionKey": tIPsecRUSAEncryptionKey,
       "tIPsecRUSAAuthenticationKey": tIPsecRUSAAuthenticationKey,
       "tIPsecRUSASpi": tIPsecRUSASpi,
       "tIPsecRUSAAuthAlgorithm": tIPsecRUSAAuthAlgorithm,
       "tIPsecRUSAEncrAlgorithm": tIPsecRUSAEncrAlgorithm,
       "tIPsecRUSAEstablishedTime": tIPsecRUSAEstablishedTime,
       "tIPsecRUSANegotiatedLifeTime": tIPsecRUSANegotiatedLifeTime,
       "tIPsecRUSALclAddrType": tIPsecRUSALclAddrType,
       "tIPsecRUSALclAddr": tIPsecRUSALclAddr,
       "tIPsecRUSALclAPrefLen": tIPsecRUSALclAPrefLen,
       "tIPsecRUSARemAddrType": tIPsecRUSARemAddrType,
       "tIPsecRUSARemAddr": tIPsecRUSARemAddr,
       "tIPsecRUSARemAPrefLen": tIPsecRUSARemAPrefLen,
       "tIPsecRUSAStatsTable": tIPsecRUSAStatsTable,
       "tIPsecRUSAStatsEntry": tIPsecRUSAStatsEntry,
       "tIPsecRUSAStatsBytesProcessed": tIPsecRUSAStatsBytesProcessed,
       "tIPsecRUSAStatsBytesProcLow32": tIPsecRUSAStatsBytesProcLow32,
       "tIPsecRUSAStatsBytesProcHigh32": tIPsecRUSAStatsBytesProcHigh32,
       "tIPsecRUSAStatsPktsProcessed": tIPsecRUSAStatsPktsProcessed,
       "tIPsecRUSAStatsPktsProcLow32": tIPsecRUSAStatsPktsProcLow32,
       "tIPsecRUSAStatsPktsProcHigh32": tIPsecRUSAStatsPktsProcHigh32,
       "tIPsecRUSAStatsCryptoErrors": tIPsecRUSAStatsCryptoErrors,
       "tIPsecRUSAStatsReplayErrors": tIPsecRUSAStatsReplayErrors,
       "tIPsecRUSAStatsSAErrors": tIPsecRUSAStatsSAErrors,
       "tIPsecRUSAStatsPolicyErrors": tIPsecRUSAStatsPolicyErrors,
       "tIPsecRUSAStatsEncapOverhead": tIPsecRUSAStatsEncapOverhead,
       "tIPsecRUSAStatsPreEncapFragCnt": tIPsecRUSAStatsPreEncapFragCnt,
       "tIPsecRUSAStatsPreEncapFragLtSz": tIPsecRUSAStatsPreEncapFragLtSz,
       "tIPsecRUSAStatsPostEncapFragCnt": tIPsecRUSAStatsPostEncapFragCnt,
       "tIPsecRUSAStatsPostEncapFragLtSz": tIPsecRUSAStatsPostEncapFragLtSz,
       "tmnxIPsecTunnelCountObjs": tmnxIPsecTunnelCountObjs,
       "tmnxIPsecPskTunnels": tmnxIPsecPskTunnels,
       "tmnxIPsecGWPskTunnels": tmnxIPsecGWPskTunnels,
       "tmnxIPsecGWPskXAuthTunnels": tmnxIPsecGWPskXAuthTunnels,
       "tmnxIPsecGWCertTunnels": tmnxIPsecGWCertTunnels,
       "tmnxIPsecGWPskRadiusTunnels": tmnxIPsecGWPskRadiusTunnels,
       "tmnxIPsecGWCertRadiusTunnels": tmnxIPsecGWCertRadiusTunnels,
       "tmnxIPsecGWEapTunnels": tmnxIPsecGWEapTunnels,
       "tmnxIPsecGWAutoEapRadiusTunnels": tmnxIPsecGWAutoEapRadiusTunnels,
       "tmnxIPsecTunnelBfdTableLastChgd": tmnxIPsecTunnelBfdTableLastChgd,
       "tmnxIPsecTunnelBfdTable": tmnxIPsecTunnelBfdTable,
       "tmnxIPsecTunnelBfdEntry": tmnxIPsecTunnelBfdEntry,
       "tmnxIPsecTunnelBfdSvcId": tmnxIPsecTunnelBfdSvcId,
       "tmnxIPsecTunnelBfdIfName": tmnxIPsecTunnelBfdIfName,
       "tmnxIPsecTunnelBfdDstAddrType": tmnxIPsecTunnelBfdDstAddrType,
       "tmnxIPsecTunnelBfdDstAddr": tmnxIPsecTunnelBfdDstAddr,
       "tmnxIPsecTunnelBfdRowStatus": tmnxIPsecTunnelBfdRowStatus,
       "tmnxIPsecTunnelBfdLastChanged": tmnxIPsecTunnelBfdLastChanged,
       "tmnxIPsecTunnelBfdSrcAddrType": tmnxIPsecTunnelBfdSrcAddrType,
       "tmnxIPsecTunnelBfdSrcAddr": tmnxIPsecTunnelBfdSrcAddr,
       "tmnxIPsecTunnelBfdSessOperState": tmnxIPsecTunnelBfdSessOperState,
       "tIPsecRadAuthPlcyTblLastChgd": tIPsecRadAuthPlcyTblLastChgd,
       "tIPsecRadAuthPlcyTable": tIPsecRadAuthPlcyTable,
       "tIPsecRadAuthPlcyEntry": tIPsecRadAuthPlcyEntry,
       "tIPsecRadAuthPlcyName": tIPsecRadAuthPlcyName,
       "tIPsecRadAuthPlcyRowStatus": tIPsecRadAuthPlcyRowStatus,
       "tIPsecRadAuthPlcyLastMgmtChange": tIPsecRadAuthPlcyLastMgmtChange,
       "tIPsecRadAuthPlcyInclAttr": tIPsecRadAuthPlcyInclAttr,
       "tIPsecRadAuthPlcyRadSrvPlcy": tIPsecRadAuthPlcyRadSrvPlcy,
       "tIPsecRadAuthPlcyPassword": tIPsecRadAuthPlcyPassword,
       "tIPsecRadAcctPlcyTblLastChgd": tIPsecRadAcctPlcyTblLastChgd,
       "tIPsecRadAcctPlcyTable": tIPsecRadAcctPlcyTable,
       "tIPsecRadAcctPlcyEntry": tIPsecRadAcctPlcyEntry,
       "tIPsecRadAcctPlcyName": tIPsecRadAcctPlcyName,
       "tIPsecRadAcctPlcyRowStatus": tIPsecRadAcctPlcyRowStatus,
       "tIPsecRadAcctPlcyLastMgmtChange": tIPsecRadAcctPlcyLastMgmtChange,
       "tIPsecRadAcctPlcyInclAttr": tIPsecRadAcctPlcyInclAttr,
       "tIPsecRadAcctPlcyRadSrvPlcy": tIPsecRadAcctPlcyRadSrvPlcy,
       "tmnxIPsecTnlDstAddrTblLastChngd": tmnxIPsecTnlDstAddrTblLastChngd,
       "tmnxIPsecTnlDstAddrTable": tmnxIPsecTnlDstAddrTable,
       "tmnxIPsecTnlDstAddrEntry": tmnxIPsecTnlDstAddrEntry,
       "tmnxIPsecTnlDstAddrType": tmnxIPsecTnlDstAddrType,
       "tmnxIPsecTnlDstAddr": tmnxIPsecTnlDstAddr,
       "tmnxIPsecTnlDstAddrRowStatus": tmnxIPsecTnlDstAddrRowStatus,
       "tmnxIPsecTnlDstAddrLastChanged": tmnxIPsecTnlDstAddrLastChanged,
       "tmnxIPsecTnlDstAddrResolved": tmnxIPsecTnlDstAddrResolved,
       "tIPsecCertProfileTblLastChgd": tIPsecCertProfileTblLastChgd,
       "tIPsecCertProfileTable": tIPsecCertProfileTable,
       "tIPsecCertProfileEntry": tIPsecCertProfileEntry,
       "tIPsecCertProfileName": tIPsecCertProfileName,
       "tIPsecCertProfileRowStatus": tIPsecCertProfileRowStatus,
       "tIPsecCertProfileLastChgd": tIPsecCertProfileLastChgd,
       "tIPsecCertProfileAdminState": tIPsecCertProfileAdminState,
       "tIPsecCertProfileOperState": tIPsecCertProfileOperState,
       "tIPsecCertProfileOperFlags": tIPsecCertProfileOperFlags,
       "tIPsecCertProfEntryIdTblLastChgd": tIPsecCertProfEntryIdTblLastChgd,
       "tIPsecCertProfEntryIdTable": tIPsecCertProfEntryIdTable,
       "tIPsecCertProfEntryIdEntry": tIPsecCertProfEntryIdEntry,
       "tIPsecCertProfEntryId": tIPsecCertProfEntryId,
       "tIPsecCertProfEntryIdRowStatus": tIPsecCertProfEntryIdRowStatus,
       "tIPsecCertProfEntryIdLastChgd": tIPsecCertProfEntryIdLastChgd,
       "tIPsecCertProfEntryIdCertFile": tIPsecCertProfEntryIdCertFile,
       "tIPsecCertProfEntryIdKeyFile": tIPsecCertProfEntryIdKeyFile,
       "tIPsecCertProfEntryIdCompChain": tIPsecCertProfEntryIdCompChain,
       "tIPsecCertProfEntryIdOperFlags": tIPsecCertProfEntryIdOperFlags,
       "tIPsecCompChainCAProfTable": tIPsecCompChainCAProfTable,
       "tIPsecCompChainCAProfEntry": tIPsecCompChainCAProfEntry,
       "tIPsecCompChainCAProfOrder": tIPsecCompChainCAProfOrder,
       "tIPsecCompChainCAProfName": tIPsecCompChainCAProfName,
       "tIPsecCertChainCAProfTblLastChgd": tIPsecCertChainCAProfTblLastChgd,
       "tIPsecCertChainCAProfTable": tIPsecCertChainCAProfTable,
       "tIPsecCertChainCAProfEntry": tIPsecCertChainCAProfEntry,
       "tIPsecCertChainCAProfName": tIPsecCertChainCAProfName,
       "tIPsecCertChainCAProfRowStatus": tIPsecCertChainCAProfRowStatus,
       "tIPsecCertChainCAProfLastChgd": tIPsecCertChainCAProfLastChgd,
       "tIPsecTsListTblLastChgd": tIPsecTsListTblLastChgd,
       "tIPsecTsListTable": tIPsecTsListTable,
       "tIPsecTsListEntry": tIPsecTsListEntry,
       "tIPsecTsListName": tIPsecTsListName,
       "tIPsecTsListRowStatus": tIPsecTsListRowStatus,
       "tIPsecTsListLastChgd": tIPsecTsListLastChgd,
       "tIPsecTsListLclEntryTblLastChgd": tIPsecTsListLclEntryTblLastChgd,
       "tIPsecTsListLclEntryTable": tIPsecTsListLclEntryTable,
       "tIPsecTsListLclEntryEntry": tIPsecTsListLclEntryEntry,
       "tIPsecTsListLclEntryId": tIPsecTsListLclEntryId,
       "tIPsecTsListLclEntryRowStatus": tIPsecTsListLclEntryRowStatus,
       "tIPsecTsListLclEntryLastChgd": tIPsecTsListLclEntryLastChgd,
       "tIPsecTsListLclEntryFrAddrType": tIPsecTsListLclEntryFrAddrType,
       "tIPsecTsListLclEntryFrAddr": tIPsecTsListLclEntryFrAddr,
       "tIPsecTsListLclEntryToAddrType": tIPsecTsListLclEntryToAddrType,
       "tIPsecTsListLclEntryToAddr": tIPsecTsListLclEntryToAddr,
       "tIPsecTsListLclEntryPfxAddrType": tIPsecTsListLclEntryPfxAddrType,
       "tIPsecTsListLclEntryPfxAddr": tIPsecTsListLclEntryPfxAddr,
       "tIPsecTsListLclEntryPfxLen": tIPsecTsListLclEntryPfxLen,
       "tIPsecGWTsNegSelPlcyTblLastChgd": tIPsecGWTsNegSelPlcyTblLastChgd,
       "tIPsecGWTsNegSelPlcyTable": tIPsecGWTsNegSelPlcyTable,
       "tIPsecGWTsNegSelPlcyEntry": tIPsecGWTsNegSelPlcyEntry,
       "tIPsecGWTsNegSelPlcyName": tIPsecGWTsNegSelPlcyName,
       "tIPsecGWTsNegSelPlcyRowStatus": tIPsecGWTsNegSelPlcyRowStatus,
       "tIPsecGWTsNegSelPlcyLastChgd": tIPsecGWTsNegSelPlcyLastChgd,
       "tIPsecGWTsNegSelPlcyTsList": tIPsecGWTsNegSelPlcyTsList,
       "tIPsecTrustAnchorProfTblLastChgd": tIPsecTrustAnchorProfTblLastChgd,
       "tIPsecTrustAnchorProfTable": tIPsecTrustAnchorProfTable,
       "tIPsecTrustAnchorProfEntry": tIPsecTrustAnchorProfEntry,
       "tIPsecTrustAnchorProfName": tIPsecTrustAnchorProfName,
       "tIPsecTrustAnchorProfRowStatus": tIPsecTrustAnchorProfRowStatus,
       "tIPsecTrustAnchorProfLastChgd": tIPsecTrustAnchorProfLastChgd,
       "tIPsecTrustAnchorCAProfDown": tIPsecTrustAnchorCAProfDown,
       "tIPsecTrustAnchorsTblLastChgd": tIPsecTrustAnchorsTblLastChgd,
       "tIPsecTrustAnchorsTable": tIPsecTrustAnchorsTable,
       "tIPsecTrustAnchorsEntry": tIPsecTrustAnchorsEntry,
       "tIPsecTrustAnchorsCAProfile": tIPsecTrustAnchorsCAProfile,
       "tIPsecTrustAnchorsRowStatus": tIPsecTrustAnchorsRowStatus,
       "tIPsecTrustAnchorsLastChgd": tIPsecTrustAnchorsLastChgd,
       "tIPsecRUSATrafficSelTable": tIPsecRUSATrafficSelTable,
       "tIPsecRUSATrafficSelEntry": tIPsecRUSATrafficSelEntry,
       "tIPsecRUSATrafficSelSide": tIPsecRUSATrafficSelSide,
       "tIPsecRUSATrafficSelFrAddrType": tIPsecRUSATrafficSelFrAddrType,
       "tIPsecRUSATrafficSelFrAddr": tIPsecRUSATrafficSelFrAddr,
       "tIPsecRUSATrafficSelToAddrType": tIPsecRUSATrafficSelToAddrType,
       "tIPsecRUSATrafficSelToAddr": tIPsecRUSATrafficSelToAddr,
       "tIPsecRUSATrafficSelLastChgd": tIPsecRUSATrafficSelLastChgd,
       "tmnxIPsecNotifyObjs": tmnxIPsecNotifyObjs,
       "tIPsecNotifRUTnlInetAddrType": tIPsecNotifRUTnlInetAddrType,
       "tIPsecNotifRUTnlInetAddress": tIPsecNotifRUTnlInetAddress,
       "tIPsecNotifRUTnlPort": tIPsecNotifRUTnlPort,
       "tIPsecNotifReason": tIPsecNotifReason,
       "tIPsecNotifBfdIntfSvcId": tIPsecNotifBfdIntfSvcId,
       "tIPsecNotifBfdIntfIfName": tIPsecNotifBfdIntfIfName,
       "tIPsecNotifBfdIntfDestIpType": tIPsecNotifBfdIntfDestIpType,
       "tIPsecNotifBfdIntfDestIp": tIPsecNotifBfdIntfDestIp,
       "tIPsecNotifBfdIntfSessState": tIPsecNotifBfdIntfSessState,
       "tIPsecRadAcctPlcyFailReason": tIPsecRadAcctPlcyFailReason,
       "tIPsecNotifIPsecTunnelName": tIPsecNotifIPsecTunnelName,
       "tIPsecNotifConfigIpMtu": tIPsecNotifConfigIpMtu,
       "tIPsecNotifEncapOverhead": tIPsecNotifEncapOverhead,
       "tIPsecNotifConfigEncapIpMtu": tIPsecNotifConfigEncapIpMtu,
       "tIPsecNotifCertProfileName": tIPsecNotifCertProfileName,
       "tIPsecNotifCertProfEntryId": tIPsecNotifCertProfEntryId,
       "tIPsecNotifCaProfNames": tIPsecNotifCaProfNames,
       "tmnxIPsecNotifyPrefix": tmnxIPsecNotifyPrefix,
       "tmnxIPsecNotifications": tmnxIPsecNotifications,
       "tIPsecRUTnlFailToCreate": tIPsecRUTnlFailToCreate,
       "tIPsecRUSAFailToAddRoute": tIPsecRUSAFailToAddRoute,
       "tIPsecBfdIntfSessStateChgd": tIPsecBfdIntfSessStateChgd,
       "tIPsecRadAcctPlcyFailure": tIPsecRadAcctPlcyFailure,
       "tIPSecTrustAnchorPrfOprChg": tIPSecTrustAnchorPrfOprChg,
       "tIPsecTunnelEncapIpMtuTooSmall": tIPsecTunnelEncapIpMtuTooSmall,
       "tIPsecRuTnlEncapIpMtuTooSmall": tIPsecRuTnlEncapIpMtuTooSmall,
       "tmnxSecNotifCmptedCertHashChngd": tmnxSecNotifCmptedCertHashChngd,
       "tmnxSecNotifCmptedCertChnChngd": tmnxSecNotifCmptedCertChnChngd,
       "tmnxSecNotifSendChnNotInCmptChn": tmnxSecNotifSendChnNotInCmptChn,
       "tmnxIPsecTunnelOperStateChange": tmnxIPsecTunnelOperStateChange}
)
