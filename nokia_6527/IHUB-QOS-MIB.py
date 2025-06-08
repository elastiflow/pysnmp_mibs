# SNMP MIB module (IHUB-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/IHUB-QOS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:45:25 2025
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

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
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
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
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

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")

(Dot1PPriority,
 TCIRRate,
 TDSCPName,
 TFCName,
 TFCType,
 TItemDescription,
 TItemScope,
 TLspExpValue,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRRate,
 TPrecValue,
 TProfile,
 TProfileOrNone) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "Dot1PPriority",
    "TCIRRate",
    "TDSCPName",
    "TFCName",
    "TFCType",
    "TItemDescription",
    "TItemScope",
    "TLspExpValue",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRRate",
    "TPrecValue",
    "TProfile",
    "TProfileOrNone")


# MODULE-IDENTITY

ihubQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87)
)
if mibBuilder.loadTexts:
    ihubQosMIB.setRevisions(
        ("2013-03-15 00:00",
         "2012-01-18 00:00",
         "2011-06-13 00:00",
         "2010-03-15 00:00",
         "2009-05-24 00:00",
         "2008-11-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PolicyRefCount(TextualConvention, Integer32):
    status = "current"


class TQosVcTypeSet(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class IhubRateLimitBurstSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 262144),
    )



class IhubEgressPortQueue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_IhubIngressQos_ObjectIdentity = ObjectIdentity
ihubIngressQos = _IhubIngressQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1)
)
_IhubQosIngressPolicyTable_Object = MibTable
ihubQosIngressPolicyTable = _IhubQosIngressPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1)
)
if mibBuilder.loadTexts:
    ihubQosIngressPolicyTable.setStatus("current")
_IhubQosIngressPolicyEntry_Object = MibTableRow
ihubQosIngressPolicyEntry = _IhubQosIngressPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1, 1)
)
ihubQosIngressPolicyEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosIngressPolicyIndex"),
)
if mibBuilder.loadTexts:
    ihubQosIngressPolicyEntry.setStatus("current")


class _IhubQosIngressPolicyIndex_Type(Integer32):
    """Custom type ihubQosIngressPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IhubQosIngressPolicyIndex_Type.__name__ = "Integer32"
_IhubQosIngressPolicyIndex_Object = MibTableColumn
ihubQosIngressPolicyIndex = _IhubQosIngressPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1, 1, 1),
    _IhubQosIngressPolicyIndex_Type()
)
ihubQosIngressPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosIngressPolicyIndex.setStatus("current")
_IhubQosIngressPolicyRowStatus_Type = RowStatus
_IhubQosIngressPolicyRowStatus_Object = MibTableColumn
ihubQosIngressPolicyRowStatus = _IhubQosIngressPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1, 1, 2),
    _IhubQosIngressPolicyRowStatus_Type()
)
ihubQosIngressPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressPolicyRowStatus.setStatus("current")


class _IhubQosIngressPolicyScope_Type(TItemScope):
    """Custom type ihubQosIngressPolicyScope based on TItemScope"""
    defaultValue = 2


_IhubQosIngressPolicyScope_Type.__name__ = "TItemScope"
_IhubQosIngressPolicyScope_Object = MibTableColumn
ihubQosIngressPolicyScope = _IhubQosIngressPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1, 1, 3),
    _IhubQosIngressPolicyScope_Type()
)
ihubQosIngressPolicyScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressPolicyScope.setStatus("current")


class _IhubQosIngressPolicyDescription_Type(TItemDescription):
    """Custom type ihubQosIngressPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_IhubQosIngressPolicyDescription_Type.__name__ = "TItemDescription"
_IhubQosIngressPolicyDescription_Object = MibTableColumn
ihubQosIngressPolicyDescription = _IhubQosIngressPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1, 1, 4),
    _IhubQosIngressPolicyDescription_Type()
)
ihubQosIngressPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressPolicyDescription.setStatus("current")
_IhubQosIngressPolicyRefCount_Type = PolicyRefCount
_IhubQosIngressPolicyRefCount_Object = MibTableColumn
ihubQosIngressPolicyRefCount = _IhubQosIngressPolicyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1, 1, 5),
    _IhubQosIngressPolicyRefCount_Type()
)
ihubQosIngressPolicyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressPolicyRefCount.setStatus("current")


class _IhubQosIngressPolicyDefaultFC_Type(TNamedItem):
    """Custom type ihubQosIngressPolicyDefaultFC based on TNamedItem"""
    defaultHexValue = "be"


_IhubQosIngressPolicyDefaultFC_Type.__name__ = "TNamedItem"
_IhubQosIngressPolicyDefaultFC_Object = MibTableColumn
ihubQosIngressPolicyDefaultFC = _IhubQosIngressPolicyDefaultFC_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1, 1, 6),
    _IhubQosIngressPolicyDefaultFC_Type()
)
ihubQosIngressPolicyDefaultFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressPolicyDefaultFC.setStatus("current")


class _IhubQosIngressPolicyDefaultProfile_Type(TProfile):
    """Custom type ihubQosIngressPolicyDefaultProfile based on TProfile"""
    defaultValue = 1


_IhubQosIngressPolicyDefaultProfile_Type.__name__ = "TProfile"
_IhubQosIngressPolicyDefaultProfile_Object = MibTableColumn
ihubQosIngressPolicyDefaultProfile = _IhubQosIngressPolicyDefaultProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1, 1, 7),
    _IhubQosIngressPolicyDefaultProfile_Type()
)
ihubQosIngressPolicyDefaultProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressPolicyDefaultProfile.setStatus("current")


class _IhubQosIngressPolicyUntaggedDot1p_Type(Dot1PPriority):
    """Custom type ihubQosIngressPolicyUntaggedDot1p based on Dot1PPriority"""
    defaultValue = 0


_IhubQosIngressPolicyUntaggedDot1p_Type.__name__ = "Dot1PPriority"
_IhubQosIngressPolicyUntaggedDot1p_Object = MibTableColumn
ihubQosIngressPolicyUntaggedDot1p = _IhubQosIngressPolicyUntaggedDot1p_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1, 1, 8),
    _IhubQosIngressPolicyUntaggedDot1p_Type()
)
ihubQosIngressPolicyUntaggedDot1p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressPolicyUntaggedDot1p.setStatus("current")
_IhubQosIngressPolicyLastChanged_Type = TimeStamp
_IhubQosIngressPolicyLastChanged_Object = MibTableColumn
ihubQosIngressPolicyLastChanged = _IhubQosIngressPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 1, 1, 9),
    _IhubQosIngressPolicyLastChanged_Type()
)
ihubQosIngressPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressPolicyLastChanged.setStatus("current")
_IhubQosIngressDSCPTable_Object = MibTable
ihubQosIngressDSCPTable = _IhubQosIngressDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 2)
)
if mibBuilder.loadTexts:
    ihubQosIngressDSCPTable.setStatus("current")
_IhubQosIngressDSCPEntry_Object = MibTableRow
ihubQosIngressDSCPEntry = _IhubQosIngressDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 2, 1)
)
ihubQosIngressDSCPEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosIngressPolicyIndex"),
    (0, "IHUB-QOS-MIB", "ihubQosIngressDSCP"),
)
if mibBuilder.loadTexts:
    ihubQosIngressDSCPEntry.setStatus("current")
_IhubQosIngressDSCP_Type = TDSCPName
_IhubQosIngressDSCP_Object = MibTableColumn
ihubQosIngressDSCP = _IhubQosIngressDSCP_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 2, 1, 1),
    _IhubQosIngressDSCP_Type()
)
ihubQosIngressDSCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosIngressDSCP.setStatus("current")
_IhubQosIngressDSCPRowStatus_Type = RowStatus
_IhubQosIngressDSCPRowStatus_Object = MibTableColumn
ihubQosIngressDSCPRowStatus = _IhubQosIngressDSCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 2, 1, 2),
    _IhubQosIngressDSCPRowStatus_Type()
)
ihubQosIngressDSCPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressDSCPRowStatus.setStatus("current")


class _IhubQosIngressDSCPFC_Type(TNamedItemOrEmpty):
    """Custom type ihubQosIngressDSCPFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_IhubQosIngressDSCPFC_Type.__name__ = "TNamedItemOrEmpty"
_IhubQosIngressDSCPFC_Object = MibTableColumn
ihubQosIngressDSCPFC = _IhubQosIngressDSCPFC_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 2, 1, 3),
    _IhubQosIngressDSCPFC_Type()
)
ihubQosIngressDSCPFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressDSCPFC.setStatus("current")


class _IhubQosIngressDSCPProfile_Type(TProfileOrNone):
    """Custom type ihubQosIngressDSCPProfile based on TProfileOrNone"""
    defaultValue = 0


_IhubQosIngressDSCPProfile_Type.__name__ = "TProfileOrNone"
_IhubQosIngressDSCPProfile_Object = MibTableColumn
ihubQosIngressDSCPProfile = _IhubQosIngressDSCPProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 2, 1, 4),
    _IhubQosIngressDSCPProfile_Type()
)
ihubQosIngressDSCPProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressDSCPProfile.setStatus("current")
_IhubQosIngressDSCPLastChanged_Type = TimeStamp
_IhubQosIngressDSCPLastChanged_Object = MibTableColumn
ihubQosIngressDSCPLastChanged = _IhubQosIngressDSCPLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 2, 1, 5),
    _IhubQosIngressDSCPLastChanged_Type()
)
ihubQosIngressDSCPLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressDSCPLastChanged.setStatus("current")
_IhubQosIngressPrecTable_Object = MibTable
ihubQosIngressPrecTable = _IhubQosIngressPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 3)
)
if mibBuilder.loadTexts:
    ihubQosIngressPrecTable.setStatus("current")
_IhubQosIngressPrecEntry_Object = MibTableRow
ihubQosIngressPrecEntry = _IhubQosIngressPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 3, 1)
)
ihubQosIngressPrecEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosIngressPolicyIndex"),
    (0, "IHUB-QOS-MIB", "ihubQosIngressPrecValue"),
)
if mibBuilder.loadTexts:
    ihubQosIngressPrecEntry.setStatus("current")
_IhubQosIngressPrecValue_Type = TPrecValue
_IhubQosIngressPrecValue_Object = MibTableColumn
ihubQosIngressPrecValue = _IhubQosIngressPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 3, 1, 1),
    _IhubQosIngressPrecValue_Type()
)
ihubQosIngressPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosIngressPrecValue.setStatus("current")
_IhubQosIngressPrecRowStatus_Type = RowStatus
_IhubQosIngressPrecRowStatus_Object = MibTableColumn
ihubQosIngressPrecRowStatus = _IhubQosIngressPrecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 3, 1, 2),
    _IhubQosIngressPrecRowStatus_Type()
)
ihubQosIngressPrecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressPrecRowStatus.setStatus("current")


class _IhubQosIngressPrecFC_Type(TNamedItemOrEmpty):
    """Custom type ihubQosIngressPrecFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_IhubQosIngressPrecFC_Type.__name__ = "TNamedItemOrEmpty"
_IhubQosIngressPrecFC_Object = MibTableColumn
ihubQosIngressPrecFC = _IhubQosIngressPrecFC_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 3, 1, 3),
    _IhubQosIngressPrecFC_Type()
)
ihubQosIngressPrecFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressPrecFC.setStatus("current")


class _IhubQosIngressPrecProfile_Type(TProfileOrNone):
    """Custom type ihubQosIngressPrecProfile based on TProfileOrNone"""
    defaultValue = 0


_IhubQosIngressPrecProfile_Type.__name__ = "TProfileOrNone"
_IhubQosIngressPrecProfile_Object = MibTableColumn
ihubQosIngressPrecProfile = _IhubQosIngressPrecProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 3, 1, 4),
    _IhubQosIngressPrecProfile_Type()
)
ihubQosIngressPrecProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressPrecProfile.setStatus("current")
_IhubQosIngressPrecLastChanged_Type = TimeStamp
_IhubQosIngressPrecLastChanged_Object = MibTableColumn
ihubQosIngressPrecLastChanged = _IhubQosIngressPrecLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 3, 1, 5),
    _IhubQosIngressPrecLastChanged_Type()
)
ihubQosIngressPrecLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressPrecLastChanged.setStatus("current")
_IhubQosIngressDot1pTable_Object = MibTable
ihubQosIngressDot1pTable = _IhubQosIngressDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 4)
)
if mibBuilder.loadTexts:
    ihubQosIngressDot1pTable.setStatus("current")
_IhubQosIngressDot1pEntry_Object = MibTableRow
ihubQosIngressDot1pEntry = _IhubQosIngressDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 4, 1)
)
ihubQosIngressDot1pEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosIngressPolicyIndex"),
    (0, "IHUB-QOS-MIB", "ihubQosIngressDot1pValue"),
)
if mibBuilder.loadTexts:
    ihubQosIngressDot1pEntry.setStatus("current")
_IhubQosIngressDot1pValue_Type = Dot1PPriority
_IhubQosIngressDot1pValue_Object = MibTableColumn
ihubQosIngressDot1pValue = _IhubQosIngressDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 4, 1, 1),
    _IhubQosIngressDot1pValue_Type()
)
ihubQosIngressDot1pValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosIngressDot1pValue.setStatus("current")
_IhubQosIngressDot1pRowStatus_Type = RowStatus
_IhubQosIngressDot1pRowStatus_Object = MibTableColumn
ihubQosIngressDot1pRowStatus = _IhubQosIngressDot1pRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 4, 1, 2),
    _IhubQosIngressDot1pRowStatus_Type()
)
ihubQosIngressDot1pRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressDot1pRowStatus.setStatus("current")


class _IhubQosIngressDot1pFC_Type(TNamedItemOrEmpty):
    """Custom type ihubQosIngressDot1pFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_IhubQosIngressDot1pFC_Type.__name__ = "TNamedItemOrEmpty"
_IhubQosIngressDot1pFC_Object = MibTableColumn
ihubQosIngressDot1pFC = _IhubQosIngressDot1pFC_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 4, 1, 3),
    _IhubQosIngressDot1pFC_Type()
)
ihubQosIngressDot1pFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressDot1pFC.setStatus("current")


class _IhubQosIngressDot1pProfile_Type(TProfileOrNone):
    """Custom type ihubQosIngressDot1pProfile based on TProfileOrNone"""
    defaultValue = 0


_IhubQosIngressDot1pProfile_Type.__name__ = "TProfileOrNone"
_IhubQosIngressDot1pProfile_Object = MibTableColumn
ihubQosIngressDot1pProfile = _IhubQosIngressDot1pProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 4, 1, 4),
    _IhubQosIngressDot1pProfile_Type()
)
ihubQosIngressDot1pProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressDot1pProfile.setStatus("current")
_IhubQosIngressDot1pLastChanged_Type = TimeStamp
_IhubQosIngressDot1pLastChanged_Object = MibTableColumn
ihubQosIngressDot1pLastChanged = _IhubQosIngressDot1pLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 1, 4, 1, 5),
    _IhubQosIngressDot1pLastChanged_Type()
)
ihubQosIngressDot1pLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressDot1pLastChanged.setStatus("current")
_IhubSgtQos_ObjectIdentity = ObjectIdentity
ihubSgtQos = _IhubSgtQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2)
)
_IhubQosSgtPolicyTable_Object = MibTable
ihubQosSgtPolicyTable = _IhubQosSgtPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1)
)
if mibBuilder.loadTexts:
    ihubQosSgtPolicyTable.setStatus("current")
_IhubQosSgtPolicyEntry_Object = MibTableRow
ihubQosSgtPolicyEntry = _IhubQosSgtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1, 1)
)
ihubQosSgtPolicyEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosSgtPolicyIndex"),
)
if mibBuilder.loadTexts:
    ihubQosSgtPolicyEntry.setStatus("current")


class _IhubQosSgtPolicyIndex_Type(Integer32):
    """Custom type ihubQosSgtPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IhubQosSgtPolicyIndex_Type.__name__ = "Integer32"
_IhubQosSgtPolicyIndex_Object = MibTableColumn
ihubQosSgtPolicyIndex = _IhubQosSgtPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1, 1, 1),
    _IhubQosSgtPolicyIndex_Type()
)
ihubQosSgtPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosSgtPolicyIndex.setStatus("current")
_IhubQosSgtPolicyRowStatus_Type = RowStatus
_IhubQosSgtPolicyRowStatus_Object = MibTableColumn
ihubQosSgtPolicyRowStatus = _IhubQosSgtPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1, 1, 2),
    _IhubQosSgtPolicyRowStatus_Type()
)
ihubQosSgtPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosSgtPolicyRowStatus.setStatus("current")


class _IhubQosSgtPolicyScope_Type(TItemScope):
    """Custom type ihubQosSgtPolicyScope based on TItemScope"""
    defaultValue = 2


_IhubQosSgtPolicyScope_Type.__name__ = "TItemScope"
_IhubQosSgtPolicyScope_Object = MibTableColumn
ihubQosSgtPolicyScope = _IhubQosSgtPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1, 1, 3),
    _IhubQosSgtPolicyScope_Type()
)
ihubQosSgtPolicyScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosSgtPolicyScope.setStatus("current")


class _IhubQosSgtPolicyDescription_Type(TItemDescription):
    """Custom type ihubQosSgtPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_IhubQosSgtPolicyDescription_Type.__name__ = "TItemDescription"
_IhubQosSgtPolicyDescription_Object = MibTableColumn
ihubQosSgtPolicyDescription = _IhubQosSgtPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1, 1, 4),
    _IhubQosSgtPolicyDescription_Type()
)
ihubQosSgtPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosSgtPolicyDescription.setStatus("current")
_IhubQosSgtPolicyRefCount_Type = PolicyRefCount
_IhubQosSgtPolicyRefCount_Object = MibTableColumn
ihubQosSgtPolicyRefCount = _IhubQosSgtPolicyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1, 1, 5),
    _IhubQosSgtPolicyRefCount_Type()
)
ihubQosSgtPolicyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosSgtPolicyRefCount.setStatus("current")


class _IhubQosSgtPolicyDefaultDSCP_Type(TDSCPName):
    """Custom type ihubQosSgtPolicyDefaultDSCP based on TDSCPName"""
    defaultValue = OctetString("nc2")


_IhubQosSgtPolicyDefaultDSCP_Type.__name__ = "TDSCPName"
_IhubQosSgtPolicyDefaultDSCP_Object = MibTableColumn
ihubQosSgtPolicyDefaultDSCP = _IhubQosSgtPolicyDefaultDSCP_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1, 1, 6),
    _IhubQosSgtPolicyDefaultDSCP_Type()
)
ihubQosSgtPolicyDefaultDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosSgtPolicyDefaultDSCP.setStatus("current")


class _IhubQosSgtPolicyDefaultDot1p_Type(Dot1PPriority):
    """Custom type ihubQosSgtPolicyDefaultDot1p based on Dot1PPriority"""
    defaultValue = 7


_IhubQosSgtPolicyDefaultDot1p_Type.__name__ = "Dot1PPriority"
_IhubQosSgtPolicyDefaultDot1p_Object = MibTableColumn
ihubQosSgtPolicyDefaultDot1p = _IhubQosSgtPolicyDefaultDot1p_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1, 1, 7),
    _IhubQosSgtPolicyDefaultDot1p_Type()
)
ihubQosSgtPolicyDefaultDot1p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosSgtPolicyDefaultDot1p.setStatus("current")
_IhubQosSgtPolicyLastChanged_Type = TimeStamp
_IhubQosSgtPolicyLastChanged_Object = MibTableColumn
ihubQosSgtPolicyLastChanged = _IhubQosSgtPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1, 1, 8),
    _IhubQosSgtPolicyLastChanged_Type()
)
ihubQosSgtPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosSgtPolicyLastChanged.setStatus("current")


class _IhubQosSgtPolicyDefaultLspExp_Type(TLspExpValue):
    """Custom type ihubQosSgtPolicyDefaultLspExp based on TLspExpValue"""
    defaultValue = 7


_IhubQosSgtPolicyDefaultLspExp_Type.__name__ = "TLspExpValue"
_IhubQosSgtPolicyDefaultLspExp_Object = MibTableColumn
ihubQosSgtPolicyDefaultLspExp = _IhubQosSgtPolicyDefaultLspExp_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 2, 1, 1, 9),
    _IhubQosSgtPolicyDefaultLspExp_Type()
)
ihubQosSgtPolicyDefaultLspExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosSgtPolicyDefaultLspExp.setStatus("current")
_IhubIngressNetworkQos_ObjectIdentity = ObjectIdentity
ihubIngressNetworkQos = _IhubIngressNetworkQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3)
)
_IhubQosIngressNetworkPolicyTable_Object = MibTable
ihubQosIngressNetworkPolicyTable = _IhubQosIngressNetworkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1)
)
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyTable.setStatus("current")
_IhubQosIngressNetworkPolicyEntry_Object = MibTableRow
ihubQosIngressNetworkPolicyEntry = _IhubQosIngressNetworkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1, 1)
)
ihubQosIngressNetworkPolicyEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosIngressNetworkPolicyIndex"),
)
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyEntry.setStatus("current")


class _IhubQosIngressNetworkPolicyIndex_Type(Integer32):
    """Custom type ihubQosIngressNetworkPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IhubQosIngressNetworkPolicyIndex_Type.__name__ = "Integer32"
_IhubQosIngressNetworkPolicyIndex_Object = MibTableColumn
ihubQosIngressNetworkPolicyIndex = _IhubQosIngressNetworkPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1, 1, 1),
    _IhubQosIngressNetworkPolicyIndex_Type()
)
ihubQosIngressNetworkPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyIndex.setStatus("current")
_IhubQosIngressNetworkPolicyRowStatus_Type = RowStatus
_IhubQosIngressNetworkPolicyRowStatus_Object = MibTableColumn
ihubQosIngressNetworkPolicyRowStatus = _IhubQosIngressNetworkPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1, 1, 2),
    _IhubQosIngressNetworkPolicyRowStatus_Type()
)
ihubQosIngressNetworkPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyRowStatus.setStatus("current")


class _IhubQosIngressNetworkPolicyScope_Type(TItemScope):
    """Custom type ihubQosIngressNetworkPolicyScope based on TItemScope"""
    defaultValue = 2


_IhubQosIngressNetworkPolicyScope_Type.__name__ = "TItemScope"
_IhubQosIngressNetworkPolicyScope_Object = MibTableColumn
ihubQosIngressNetworkPolicyScope = _IhubQosIngressNetworkPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1, 1, 3),
    _IhubQosIngressNetworkPolicyScope_Type()
)
ihubQosIngressNetworkPolicyScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyScope.setStatus("current")


class _IhubQosIngressNetworkPolicyDescription_Type(TItemDescription):
    """Custom type ihubQosIngressNetworkPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_IhubQosIngressNetworkPolicyDescription_Type.__name__ = "TItemDescription"
_IhubQosIngressNetworkPolicyDescription_Object = MibTableColumn
ihubQosIngressNetworkPolicyDescription = _IhubQosIngressNetworkPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1, 1, 4),
    _IhubQosIngressNetworkPolicyDescription_Type()
)
ihubQosIngressNetworkPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyDescription.setStatus("current")
_IhubQosIngressNetworkPolicyRefCount_Type = PolicyRefCount
_IhubQosIngressNetworkPolicyRefCount_Object = MibTableColumn
ihubQosIngressNetworkPolicyRefCount = _IhubQosIngressNetworkPolicyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1, 1, 5),
    _IhubQosIngressNetworkPolicyRefCount_Type()
)
ihubQosIngressNetworkPolicyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyRefCount.setStatus("current")


class _IhubQosIngressNetworkPolicyDefaultFC_Type(TNamedItem):
    """Custom type ihubQosIngressNetworkPolicyDefaultFC based on TNamedItem"""
    defaultHexValue = "be"


_IhubQosIngressNetworkPolicyDefaultFC_Type.__name__ = "TNamedItem"
_IhubQosIngressNetworkPolicyDefaultFC_Object = MibTableColumn
ihubQosIngressNetworkPolicyDefaultFC = _IhubQosIngressNetworkPolicyDefaultFC_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1, 1, 6),
    _IhubQosIngressNetworkPolicyDefaultFC_Type()
)
ihubQosIngressNetworkPolicyDefaultFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyDefaultFC.setStatus("current")


class _IhubQosIngressNetworkPolicyDefaultProfile_Type(TProfile):
    """Custom type ihubQosIngressNetworkPolicyDefaultProfile based on TProfile"""
    defaultValue = 1


_IhubQosIngressNetworkPolicyDefaultProfile_Type.__name__ = "TProfile"
_IhubQosIngressNetworkPolicyDefaultProfile_Object = MibTableColumn
ihubQosIngressNetworkPolicyDefaultProfile = _IhubQosIngressNetworkPolicyDefaultProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1, 1, 7),
    _IhubQosIngressNetworkPolicyDefaultProfile_Type()
)
ihubQosIngressNetworkPolicyDefaultProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyDefaultProfile.setStatus("current")


class _IhubQosIngressNetworkPolicyLerUseDot1p_Type(TQosVcTypeSet):
    """Custom type ihubQosIngressNetworkPolicyLerUseDot1p based on TQosVcTypeSet"""
    defaultValue = 0


_IhubQosIngressNetworkPolicyLerUseDot1p_Type.__name__ = "TQosVcTypeSet"
_IhubQosIngressNetworkPolicyLerUseDot1p_Object = MibTableColumn
ihubQosIngressNetworkPolicyLerUseDot1p = _IhubQosIngressNetworkPolicyLerUseDot1p_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1, 1, 8),
    _IhubQosIngressNetworkPolicyLerUseDot1p_Type()
)
ihubQosIngressNetworkPolicyLerUseDot1p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyLerUseDot1p.setStatus("current")
_IhubQosIngressNetworkPolicyLastChanged_Type = TimeStamp
_IhubQosIngressNetworkPolicyLastChanged_Object = MibTableColumn
ihubQosIngressNetworkPolicyLastChanged = _IhubQosIngressNetworkPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 1, 1, 9),
    _IhubQosIngressNetworkPolicyLastChanged_Type()
)
ihubQosIngressNetworkPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkPolicyLastChanged.setStatus("current")
_IhubQosIngressNetworkDot1pTable_Object = MibTable
ihubQosIngressNetworkDot1pTable = _IhubQosIngressNetworkDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 2)
)
if mibBuilder.loadTexts:
    ihubQosIngressNetworkDot1pTable.setStatus("current")
_IhubQosIngressNetworkDot1pEntry_Object = MibTableRow
ihubQosIngressNetworkDot1pEntry = _IhubQosIngressNetworkDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 2, 1)
)
ihubQosIngressNetworkDot1pEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosIngressNetworkPolicyIndex"),
    (0, "IHUB-QOS-MIB", "ihubQosIngressNetworkDot1pValue"),
)
if mibBuilder.loadTexts:
    ihubQosIngressNetworkDot1pEntry.setStatus("current")
_IhubQosIngressNetworkDot1pValue_Type = Dot1PPriority
_IhubQosIngressNetworkDot1pValue_Object = MibTableColumn
ihubQosIngressNetworkDot1pValue = _IhubQosIngressNetworkDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 2, 1, 1),
    _IhubQosIngressNetworkDot1pValue_Type()
)
ihubQosIngressNetworkDot1pValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkDot1pValue.setStatus("current")
_IhubQosIngressNetworkDot1pRowStatus_Type = RowStatus
_IhubQosIngressNetworkDot1pRowStatus_Object = MibTableColumn
ihubQosIngressNetworkDot1pRowStatus = _IhubQosIngressNetworkDot1pRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 2, 1, 2),
    _IhubQosIngressNetworkDot1pRowStatus_Type()
)
ihubQosIngressNetworkDot1pRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkDot1pRowStatus.setStatus("current")


class _IhubQosIngressNetworkDot1pFC_Type(TNamedItemOrEmpty):
    """Custom type ihubQosIngressNetworkDot1pFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_IhubQosIngressNetworkDot1pFC_Type.__name__ = "TNamedItemOrEmpty"
_IhubQosIngressNetworkDot1pFC_Object = MibTableColumn
ihubQosIngressNetworkDot1pFC = _IhubQosIngressNetworkDot1pFC_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 2, 1, 3),
    _IhubQosIngressNetworkDot1pFC_Type()
)
ihubQosIngressNetworkDot1pFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkDot1pFC.setStatus("current")


class _IhubQosIngressNetworkDot1pProfile_Type(TProfileOrNone):
    """Custom type ihubQosIngressNetworkDot1pProfile based on TProfileOrNone"""
    defaultValue = 0


_IhubQosIngressNetworkDot1pProfile_Type.__name__ = "TProfileOrNone"
_IhubQosIngressNetworkDot1pProfile_Object = MibTableColumn
ihubQosIngressNetworkDot1pProfile = _IhubQosIngressNetworkDot1pProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 2, 1, 4),
    _IhubQosIngressNetworkDot1pProfile_Type()
)
ihubQosIngressNetworkDot1pProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkDot1pProfile.setStatus("current")
_IhubQosIngressNetworkDot1pLastChanged_Type = TimeStamp
_IhubQosIngressNetworkDot1pLastChanged_Object = MibTableColumn
ihubQosIngressNetworkDot1pLastChanged = _IhubQosIngressNetworkDot1pLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 2, 1, 5),
    _IhubQosIngressNetworkDot1pLastChanged_Type()
)
ihubQosIngressNetworkDot1pLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkDot1pLastChanged.setStatus("current")
_IhubQosIngressNetworkLspExpTable_Object = MibTable
ihubQosIngressNetworkLspExpTable = _IhubQosIngressNetworkLspExpTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 3)
)
if mibBuilder.loadTexts:
    ihubQosIngressNetworkLspExpTable.setStatus("current")
_IhubQosIngressNetworkLspExpEntry_Object = MibTableRow
ihubQosIngressNetworkLspExpEntry = _IhubQosIngressNetworkLspExpEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 3, 1)
)
ihubQosIngressNetworkLspExpEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosIngressNetworkPolicyIndex"),
    (0, "IHUB-QOS-MIB", "ihubQosIngressNetworkLspExpValue"),
)
if mibBuilder.loadTexts:
    ihubQosIngressNetworkLspExpEntry.setStatus("current")
_IhubQosIngressNetworkLspExpValue_Type = TLspExpValue
_IhubQosIngressNetworkLspExpValue_Object = MibTableColumn
ihubQosIngressNetworkLspExpValue = _IhubQosIngressNetworkLspExpValue_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 3, 1, 1),
    _IhubQosIngressNetworkLspExpValue_Type()
)
ihubQosIngressNetworkLspExpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkLspExpValue.setStatus("current")
_IhubQosIngressNetworkLspExpRowStatus_Type = RowStatus
_IhubQosIngressNetworkLspExpRowStatus_Object = MibTableColumn
ihubQosIngressNetworkLspExpRowStatus = _IhubQosIngressNetworkLspExpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 3, 1, 2),
    _IhubQosIngressNetworkLspExpRowStatus_Type()
)
ihubQosIngressNetworkLspExpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkLspExpRowStatus.setStatus("current")


class _IhubQosIngressNetworkLspExpFC_Type(TNamedItemOrEmpty):
    """Custom type ihubQosIngressNetworkLspExpFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_IhubQosIngressNetworkLspExpFC_Type.__name__ = "TNamedItemOrEmpty"
_IhubQosIngressNetworkLspExpFC_Object = MibTableColumn
ihubQosIngressNetworkLspExpFC = _IhubQosIngressNetworkLspExpFC_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 3, 1, 3),
    _IhubQosIngressNetworkLspExpFC_Type()
)
ihubQosIngressNetworkLspExpFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkLspExpFC.setStatus("current")


class _IhubQosIngressNetworkLspExpProfile_Type(TProfileOrNone):
    """Custom type ihubQosIngressNetworkLspExpProfile based on TProfileOrNone"""
    defaultValue = 0


_IhubQosIngressNetworkLspExpProfile_Type.__name__ = "TProfileOrNone"
_IhubQosIngressNetworkLspExpProfile_Object = MibTableColumn
ihubQosIngressNetworkLspExpProfile = _IhubQosIngressNetworkLspExpProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 3, 1, 4),
    _IhubQosIngressNetworkLspExpProfile_Type()
)
ihubQosIngressNetworkLspExpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkLspExpProfile.setStatus("current")
_IhubQosIngressNetworkLspExpLastChanged_Type = TimeStamp
_IhubQosIngressNetworkLspExpLastChanged_Object = MibTableColumn
ihubQosIngressNetworkLspExpLastChanged = _IhubQosIngressNetworkLspExpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 3, 1, 5),
    _IhubQosIngressNetworkLspExpLastChanged_Type()
)
ihubQosIngressNetworkLspExpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressNetworkLspExpLastChanged.setStatus("current")
_IhubQosIngressLsrNetworkPolicyTable_Object = MibTable
ihubQosIngressLsrNetworkPolicyTable = _IhubQosIngressLsrNetworkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 4)
)
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkPolicyTable.setStatus("current")
_IhubQosIngressLsrNetworkPolicyEntry_Object = MibTableRow
ihubQosIngressLsrNetworkPolicyEntry = _IhubQosIngressLsrNetworkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 4, 1)
)
ihubQosIngressLsrNetworkPolicyEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosIngressLsrNetworkPolicyIndex"),
)
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkPolicyEntry.setStatus("current")


class _IhubQosIngressLsrNetworkPolicyIndex_Type(Integer32):
    """Custom type ihubQosIngressLsrNetworkPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IhubQosIngressLsrNetworkPolicyIndex_Type.__name__ = "Integer32"
_IhubQosIngressLsrNetworkPolicyIndex_Object = MibTableColumn
ihubQosIngressLsrNetworkPolicyIndex = _IhubQosIngressLsrNetworkPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 4, 1, 1),
    _IhubQosIngressLsrNetworkPolicyIndex_Type()
)
ihubQosIngressLsrNetworkPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkPolicyIndex.setStatus("current")
_IhubQosIngressLsrNetworkPolicyRowStatus_Type = RowStatus
_IhubQosIngressLsrNetworkPolicyRowStatus_Object = MibTableColumn
ihubQosIngressLsrNetworkPolicyRowStatus = _IhubQosIngressLsrNetworkPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 4, 1, 2),
    _IhubQosIngressLsrNetworkPolicyRowStatus_Type()
)
ihubQosIngressLsrNetworkPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkPolicyRowStatus.setStatus("current")


class _IhubQosIngressLsrNetworkPolicyScope_Type(TItemScope):
    """Custom type ihubQosIngressLsrNetworkPolicyScope based on TItemScope"""
    defaultValue = 2


_IhubQosIngressLsrNetworkPolicyScope_Type.__name__ = "TItemScope"
_IhubQosIngressLsrNetworkPolicyScope_Object = MibTableColumn
ihubQosIngressLsrNetworkPolicyScope = _IhubQosIngressLsrNetworkPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 4, 1, 3),
    _IhubQosIngressLsrNetworkPolicyScope_Type()
)
ihubQosIngressLsrNetworkPolicyScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkPolicyScope.setStatus("current")


class _IhubQosIngressLsrNetworkPolicyDescription_Type(TItemDescription):
    """Custom type ihubQosIngressLsrNetworkPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_IhubQosIngressLsrNetworkPolicyDescription_Type.__name__ = "TItemDescription"
_IhubQosIngressLsrNetworkPolicyDescription_Object = MibTableColumn
ihubQosIngressLsrNetworkPolicyDescription = _IhubQosIngressLsrNetworkPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 4, 1, 4),
    _IhubQosIngressLsrNetworkPolicyDescription_Type()
)
ihubQosIngressLsrNetworkPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkPolicyDescription.setStatus("current")
_IhubQosIngressLsrNetworkPolicyRefCount_Type = PolicyRefCount
_IhubQosIngressLsrNetworkPolicyRefCount_Object = MibTableColumn
ihubQosIngressLsrNetworkPolicyRefCount = _IhubQosIngressLsrNetworkPolicyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 4, 1, 5),
    _IhubQosIngressLsrNetworkPolicyRefCount_Type()
)
ihubQosIngressLsrNetworkPolicyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkPolicyRefCount.setStatus("current")


class _IhubQosIngressLsrNetworkPolicyDefaultFC_Type(TNamedItem):
    """Custom type ihubQosIngressLsrNetworkPolicyDefaultFC based on TNamedItem"""
    defaultHexValue = "be"


_IhubQosIngressLsrNetworkPolicyDefaultFC_Type.__name__ = "TNamedItem"
_IhubQosIngressLsrNetworkPolicyDefaultFC_Object = MibTableColumn
ihubQosIngressLsrNetworkPolicyDefaultFC = _IhubQosIngressLsrNetworkPolicyDefaultFC_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 4, 1, 6),
    _IhubQosIngressLsrNetworkPolicyDefaultFC_Type()
)
ihubQosIngressLsrNetworkPolicyDefaultFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkPolicyDefaultFC.setStatus("current")


class _IhubQosIngressLsrNetworkPolicyDefaultProfile_Type(TProfile):
    """Custom type ihubQosIngressLsrNetworkPolicyDefaultProfile based on TProfile"""
    defaultValue = 2


_IhubQosIngressLsrNetworkPolicyDefaultProfile_Type.__name__ = "TProfile"
_IhubQosIngressLsrNetworkPolicyDefaultProfile_Object = MibTableColumn
ihubQosIngressLsrNetworkPolicyDefaultProfile = _IhubQosIngressLsrNetworkPolicyDefaultProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 4, 1, 7),
    _IhubQosIngressLsrNetworkPolicyDefaultProfile_Type()
)
ihubQosIngressLsrNetworkPolicyDefaultProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkPolicyDefaultProfile.setStatus("current")
_IhubQosIngressLsrNetworkPolicyLastChanged_Type = TimeStamp
_IhubQosIngressLsrNetworkPolicyLastChanged_Object = MibTableColumn
ihubQosIngressLsrNetworkPolicyLastChanged = _IhubQosIngressLsrNetworkPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 4, 1, 8),
    _IhubQosIngressLsrNetworkPolicyLastChanged_Type()
)
ihubQosIngressLsrNetworkPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkPolicyLastChanged.setStatus("current")
_IhubQosIngressLsrNetworkLspExpTable_Object = MibTable
ihubQosIngressLsrNetworkLspExpTable = _IhubQosIngressLsrNetworkLspExpTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 5)
)
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkLspExpTable.setStatus("current")
_IhubQosIngressLsrNetworkLspExpEntry_Object = MibTableRow
ihubQosIngressLsrNetworkLspExpEntry = _IhubQosIngressLsrNetworkLspExpEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 5, 1)
)
ihubQosIngressLsrNetworkLspExpEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosIngressLsrNetworkPolicyIndex"),
    (0, "IHUB-QOS-MIB", "ihubQosIngressLsrNetworkLspExpValue"),
)
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkLspExpEntry.setStatus("current")
_IhubQosIngressLsrNetworkLspExpValue_Type = TLspExpValue
_IhubQosIngressLsrNetworkLspExpValue_Object = MibTableColumn
ihubQosIngressLsrNetworkLspExpValue = _IhubQosIngressLsrNetworkLspExpValue_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 5, 1, 1),
    _IhubQosIngressLsrNetworkLspExpValue_Type()
)
ihubQosIngressLsrNetworkLspExpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkLspExpValue.setStatus("current")
_IhubQosIngressLsrNetworkLspExpRowStatus_Type = RowStatus
_IhubQosIngressLsrNetworkLspExpRowStatus_Object = MibTableColumn
ihubQosIngressLsrNetworkLspExpRowStatus = _IhubQosIngressLsrNetworkLspExpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 5, 1, 2),
    _IhubQosIngressLsrNetworkLspExpRowStatus_Type()
)
ihubQosIngressLsrNetworkLspExpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkLspExpRowStatus.setStatus("current")


class _IhubQosIngressLsrNetworkLspExpFC_Type(TNamedItemOrEmpty):
    """Custom type ihubQosIngressLsrNetworkLspExpFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_IhubQosIngressLsrNetworkLspExpFC_Type.__name__ = "TNamedItemOrEmpty"
_IhubQosIngressLsrNetworkLspExpFC_Object = MibTableColumn
ihubQosIngressLsrNetworkLspExpFC = _IhubQosIngressLsrNetworkLspExpFC_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 5, 1, 3),
    _IhubQosIngressLsrNetworkLspExpFC_Type()
)
ihubQosIngressLsrNetworkLspExpFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkLspExpFC.setStatus("current")


class _IhubQosIngressLsrNetworkLspExpProfile_Type(TProfileOrNone):
    """Custom type ihubQosIngressLsrNetworkLspExpProfile based on TProfileOrNone"""
    defaultValue = 0


_IhubQosIngressLsrNetworkLspExpProfile_Type.__name__ = "TProfileOrNone"
_IhubQosIngressLsrNetworkLspExpProfile_Object = MibTableColumn
ihubQosIngressLsrNetworkLspExpProfile = _IhubQosIngressLsrNetworkLspExpProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 5, 1, 4),
    _IhubQosIngressLsrNetworkLspExpProfile_Type()
)
ihubQosIngressLsrNetworkLspExpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkLspExpProfile.setStatus("current")
_IhubQosIngressLsrNetworkLspExpLastChanged_Type = TimeStamp
_IhubQosIngressLsrNetworkLspExpLastChanged_Object = MibTableColumn
ihubQosIngressLsrNetworkLspExpLastChanged = _IhubQosIngressLsrNetworkLspExpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 3, 5, 1, 5),
    _IhubQosIngressLsrNetworkLspExpLastChanged_Type()
)
ihubQosIngressLsrNetworkLspExpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosIngressLsrNetworkLspExpLastChanged.setStatus("current")
_IhubEgressNetworkQos_ObjectIdentity = ObjectIdentity
ihubEgressNetworkQos = _IhubEgressNetworkQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4)
)
_IhubQosEgressNetworkPolicyTable_Object = MibTable
ihubQosEgressNetworkPolicyTable = _IhubQosEgressNetworkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 1)
)
if mibBuilder.loadTexts:
    ihubQosEgressNetworkPolicyTable.setStatus("current")
_IhubQosEgressNetworkPolicyEntry_Object = MibTableRow
ihubQosEgressNetworkPolicyEntry = _IhubQosEgressNetworkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 1, 1)
)
ihubQosEgressNetworkPolicyEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosEgressNetworkPolicyIndex"),
)
if mibBuilder.loadTexts:
    ihubQosEgressNetworkPolicyEntry.setStatus("current")


class _IhubQosEgressNetworkPolicyIndex_Type(Integer32):
    """Custom type ihubQosEgressNetworkPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IhubQosEgressNetworkPolicyIndex_Type.__name__ = "Integer32"
_IhubQosEgressNetworkPolicyIndex_Object = MibTableColumn
ihubQosEgressNetworkPolicyIndex = _IhubQosEgressNetworkPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 1, 1, 1),
    _IhubQosEgressNetworkPolicyIndex_Type()
)
ihubQosEgressNetworkPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosEgressNetworkPolicyIndex.setStatus("current")
_IhubQosEgressNetworkPolicyRowStatus_Type = RowStatus
_IhubQosEgressNetworkPolicyRowStatus_Object = MibTableColumn
ihubQosEgressNetworkPolicyRowStatus = _IhubQosEgressNetworkPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 1, 1, 2),
    _IhubQosEgressNetworkPolicyRowStatus_Type()
)
ihubQosEgressNetworkPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosEgressNetworkPolicyRowStatus.setStatus("current")


class _IhubQosEgressNetworkPolicyScope_Type(TItemScope):
    """Custom type ihubQosEgressNetworkPolicyScope based on TItemScope"""
    defaultValue = 2


_IhubQosEgressNetworkPolicyScope_Type.__name__ = "TItemScope"
_IhubQosEgressNetworkPolicyScope_Object = MibTableColumn
ihubQosEgressNetworkPolicyScope = _IhubQosEgressNetworkPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 1, 1, 3),
    _IhubQosEgressNetworkPolicyScope_Type()
)
ihubQosEgressNetworkPolicyScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosEgressNetworkPolicyScope.setStatus("current")


class _IhubQosEgressNetworkPolicyDescription_Type(TItemDescription):
    """Custom type ihubQosEgressNetworkPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_IhubQosEgressNetworkPolicyDescription_Type.__name__ = "TItemDescription"
_IhubQosEgressNetworkPolicyDescription_Object = MibTableColumn
ihubQosEgressNetworkPolicyDescription = _IhubQosEgressNetworkPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 1, 1, 4),
    _IhubQosEgressNetworkPolicyDescription_Type()
)
ihubQosEgressNetworkPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosEgressNetworkPolicyDescription.setStatus("current")
_IhubQosEgressNetworkPolicyRefCount_Type = PolicyRefCount
_IhubQosEgressNetworkPolicyRefCount_Object = MibTableColumn
ihubQosEgressNetworkPolicyRefCount = _IhubQosEgressNetworkPolicyRefCount_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 1, 1, 5),
    _IhubQosEgressNetworkPolicyRefCount_Type()
)
ihubQosEgressNetworkPolicyRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosEgressNetworkPolicyRefCount.setStatus("current")
_IhubQosEgressNetworkPolicyLastChanged_Type = TimeStamp
_IhubQosEgressNetworkPolicyLastChanged_Object = MibTableColumn
ihubQosEgressNetworkPolicyLastChanged = _IhubQosEgressNetworkPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 1, 1, 6),
    _IhubQosEgressNetworkPolicyLastChanged_Type()
)
ihubQosEgressNetworkPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosEgressNetworkPolicyLastChanged.setStatus("current")
_IhubQosEgressNetworkFCTable_Object = MibTable
ihubQosEgressNetworkFCTable = _IhubQosEgressNetworkFCTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 2)
)
if mibBuilder.loadTexts:
    ihubQosEgressNetworkFCTable.setStatus("current")
_IhubQosEgressNetworkFCEntry_Object = MibTableRow
ihubQosEgressNetworkFCEntry = _IhubQosEgressNetworkFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 2, 1)
)
ihubQosEgressNetworkFCEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubQosEgressNetworkPolicyIndex"),
    (0, "IHUB-QOS-MIB", "ihubQosEgressNetworkFCName"),
)
if mibBuilder.loadTexts:
    ihubQosEgressNetworkFCEntry.setStatus("current")
_IhubQosEgressNetworkFCName_Type = TFCName
_IhubQosEgressNetworkFCName_Object = MibTableColumn
ihubQosEgressNetworkFCName = _IhubQosEgressNetworkFCName_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 2, 1, 1),
    _IhubQosEgressNetworkFCName_Type()
)
ihubQosEgressNetworkFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubQosEgressNetworkFCName.setStatus("current")
_IhubQosEgressNetworkFCRowStatus_Type = RowStatus
_IhubQosEgressNetworkFCRowStatus_Object = MibTableColumn
ihubQosEgressNetworkFCRowStatus = _IhubQosEgressNetworkFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 2, 1, 2),
    _IhubQosEgressNetworkFCRowStatus_Type()
)
ihubQosEgressNetworkFCRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosEgressNetworkFCRowStatus.setStatus("current")


class _IhubQosEgressNetworkFCLspExpInProfile_Type(TLspExpValue):
    """Custom type ihubQosEgressNetworkFCLspExpInProfile based on TLspExpValue"""
    defaultValue = 0


_IhubQosEgressNetworkFCLspExpInProfile_Type.__name__ = "TLspExpValue"
_IhubQosEgressNetworkFCLspExpInProfile_Object = MibTableColumn
ihubQosEgressNetworkFCLspExpInProfile = _IhubQosEgressNetworkFCLspExpInProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 2, 1, 3),
    _IhubQosEgressNetworkFCLspExpInProfile_Type()
)
ihubQosEgressNetworkFCLspExpInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosEgressNetworkFCLspExpInProfile.setStatus("current")


class _IhubQosEgressNetworkFCLspExpOutProfile_Type(TLspExpValue):
    """Custom type ihubQosEgressNetworkFCLspExpOutProfile based on TLspExpValue"""
    defaultValue = 0


_IhubQosEgressNetworkFCLspExpOutProfile_Type.__name__ = "TLspExpValue"
_IhubQosEgressNetworkFCLspExpOutProfile_Object = MibTableColumn
ihubQosEgressNetworkFCLspExpOutProfile = _IhubQosEgressNetworkFCLspExpOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 2, 1, 4),
    _IhubQosEgressNetworkFCLspExpOutProfile_Type()
)
ihubQosEgressNetworkFCLspExpOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosEgressNetworkFCLspExpOutProfile.setStatus("current")
_IhubQosEngressNetworkFCLastChanged_Type = TimeStamp
_IhubQosEngressNetworkFCLastChanged_Object = MibTableColumn
ihubQosEngressNetworkFCLastChanged = _IhubQosEngressNetworkFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 4, 2, 1, 5),
    _IhubQosEngressNetworkFCLastChanged_Type()
)
ihubQosEngressNetworkFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubQosEngressNetworkFCLastChanged.setStatus("current")
_IhubBaseRouterPolicyIds_ObjectIdentity = ObjectIdentity
ihubBaseRouterPolicyIds = _IhubBaseRouterPolicyIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 6)
)


class _IhubBaseRouterNetworkPolicyId_Type(Integer32):
    """Custom type ihubBaseRouterNetworkPolicyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IhubBaseRouterNetworkPolicyId_Type.__name__ = "Integer32"
_IhubBaseRouterNetworkPolicyId_Object = MibScalar
ihubBaseRouterNetworkPolicyId = _IhubBaseRouterNetworkPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 6, 1),
    _IhubBaseRouterNetworkPolicyId_Type()
)
ihubBaseRouterNetworkPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubBaseRouterNetworkPolicyId.setStatus("current")


class _IhubBaseRouterSgtPolicyId_Type(Integer32):
    """Custom type ihubBaseRouterSgtPolicyId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IhubBaseRouterSgtPolicyId_Type.__name__ = "Integer32"
_IhubBaseRouterSgtPolicyId_Object = MibScalar
ihubBaseRouterSgtPolicyId = _IhubBaseRouterSgtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 6, 2),
    _IhubBaseRouterSgtPolicyId_Type()
)
ihubBaseRouterSgtPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubBaseRouterSgtPolicyId.setStatus("current")
_IhubIngressSystemCosQos_ObjectIdentity = ObjectIdentity
ihubIngressSystemCosQos = _IhubIngressSystemCosQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 7)
)


class _IhubQosEgressRateLimitNtLoadSharingPercentage_Type(Integer32):
    """Custom type ihubQosEgressRateLimitNtLoadSharingPercentage based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IhubQosEgressRateLimitNtLoadSharingPercentage_Type.__name__ = "Integer32"
_IhubQosEgressRateLimitNtLoadSharingPercentage_Object = MibScalar
ihubQosEgressRateLimitNtLoadSharingPercentage = _IhubQosEgressRateLimitNtLoadSharingPercentage_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 7, 1),
    _IhubQosEgressRateLimitNtLoadSharingPercentage_Type()
)
ihubQosEgressRateLimitNtLoadSharingPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubQosEgressRateLimitNtLoadSharingPercentage.setStatus("current")
_IhubIngressSystemDot1pTable_Object = MibTable
ihubIngressSystemDot1pTable = _IhubIngressSystemDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 7, 2)
)
if mibBuilder.loadTexts:
    ihubIngressSystemDot1pTable.setStatus("current")
_IhubIngressSystemDot1pEntry_Object = MibTableRow
ihubIngressSystemDot1pEntry = _IhubIngressSystemDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 7, 2, 1)
)
ihubIngressSystemDot1pEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubIngressSystemDot1pValue"),
)
if mibBuilder.loadTexts:
    ihubIngressSystemDot1pEntry.setStatus("current")
_IhubIngressSystemDot1pValue_Type = Dot1PPriority
_IhubIngressSystemDot1pValue_Object = MibTableColumn
ihubIngressSystemDot1pValue = _IhubIngressSystemDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 7, 2, 1, 1),
    _IhubIngressSystemDot1pValue_Type()
)
ihubIngressSystemDot1pValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubIngressSystemDot1pValue.setStatus("current")
_IhubIngressSystemDot1pProfile_Type = TProfileOrNone
_IhubIngressSystemDot1pProfile_Object = MibTableColumn
ihubIngressSystemDot1pProfile = _IhubIngressSystemDot1pProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 7, 2, 1, 2),
    _IhubIngressSystemDot1pProfile_Type()
)
ihubIngressSystemDot1pProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubIngressSystemDot1pProfile.setStatus("current")
_IhubIngressSystemDot1pLastChanged_Type = TimeStamp
_IhubIngressSystemDot1pLastChanged_Object = MibTableColumn
ihubIngressSystemDot1pLastChanged = _IhubIngressSystemDot1pLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 7, 2, 1, 3),
    _IhubIngressSystemDot1pLastChanged_Type()
)
ihubIngressSystemDot1pLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubIngressSystemDot1pLastChanged.setStatus("current")
_IhubEgressSystemPerCosMap_ObjectIdentity = ObjectIdentity
ihubEgressSystemPerCosMap = _IhubEgressSystemPerCosMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 8)
)
_IhubEgressSystemDot1pMapTable_Object = MibTable
ihubEgressSystemDot1pMapTable = _IhubEgressSystemDot1pMapTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 8, 1)
)
if mibBuilder.loadTexts:
    ihubEgressSystemDot1pMapTable.setStatus("current")
_IhubEgressSystemDot1pMapEntry_Object = MibTableRow
ihubEgressSystemDot1pMapEntry = _IhubEgressSystemDot1pMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 8, 1, 1)
)
ihubEgressSystemDot1pMapEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubEgressSystemDot1pFC"),
)
if mibBuilder.loadTexts:
    ihubEgressSystemDot1pMapEntry.setStatus("current")
_IhubEgressSystemDot1pFC_Type = TFCType
_IhubEgressSystemDot1pFC_Object = MibTableColumn
ihubEgressSystemDot1pFC = _IhubEgressSystemDot1pFC_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 8, 1, 1, 1),
    _IhubEgressSystemDot1pFC_Type()
)
ihubEgressSystemDot1pFC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubEgressSystemDot1pFC.setStatus("current")
_IhubEgressSystemDot1pInProfile_Type = Dot1PPriority
_IhubEgressSystemDot1pInProfile_Object = MibTableColumn
ihubEgressSystemDot1pInProfile = _IhubEgressSystemDot1pInProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 8, 1, 1, 2),
    _IhubEgressSystemDot1pInProfile_Type()
)
ihubEgressSystemDot1pInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressSystemDot1pInProfile.setStatus("current")
_IhubEgressSystemDot1pOutProfile_Type = Dot1PPriority
_IhubEgressSystemDot1pOutProfile_Object = MibTableColumn
ihubEgressSystemDot1pOutProfile = _IhubEgressSystemDot1pOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 8, 1, 1, 3),
    _IhubEgressSystemDot1pOutProfile_Type()
)
ihubEgressSystemDot1pOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressSystemDot1pOutProfile.setStatus("current")
_IhubEgressSystemDot1pLastChanged_Type = TimeStamp
_IhubEgressSystemDot1pLastChanged_Object = MibTableColumn
ihubEgressSystemDot1pLastChanged = _IhubEgressSystemDot1pLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 8, 1, 1, 4),
    _IhubEgressSystemDot1pLastChanged_Type()
)
ihubEgressSystemDot1pLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubEgressSystemDot1pLastChanged.setStatus("current")
_IhubEgressPerCosQos_ObjectIdentity = ObjectIdentity
ihubEgressPerCosQos = _IhubEgressPerCosQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9)
)
_IhubEgressPerCosQosTable_Object = MibTable
ihubEgressPerCosQosTable = _IhubEgressPerCosQosTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1)
)
if mibBuilder.loadTexts:
    ihubEgressPerCosQosTable.setStatus("current")
_IhubEgressPerCosQosEntry_Object = MibTableRow
ihubEgressPerCosQosEntry = _IhubEgressPerCosQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1)
)
ihubEgressPerCosQosEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "IHUB-QOS-MIB", "ihubEgressPerCosQosPbitsIndex"),
)
if mibBuilder.loadTexts:
    ihubEgressPerCosQosEntry.setStatus("current")


class _IhubEgressPerCosQosPbitsIndex_Type(Integer32):
    """Custom type ihubEgressPerCosQosPbitsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IhubEgressPerCosQosPbitsIndex_Type.__name__ = "Integer32"
_IhubEgressPerCosQosPbitsIndex_Object = MibTableColumn
ihubEgressPerCosQosPbitsIndex = _IhubEgressPerCosQosPbitsIndex_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1, 1),
    _IhubEgressPerCosQosPbitsIndex_Type()
)
ihubEgressPerCosQosPbitsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubEgressPerCosQosPbitsIndex.setStatus("current")
_IhubEgressPerCosQosRowStatus_Type = RowStatus
_IhubEgressPerCosQosRowStatus_Object = MibTableColumn
ihubEgressPerCosQosRowStatus = _IhubEgressPerCosQosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1, 2),
    _IhubEgressPerCosQosRowStatus_Type()
)
ihubEgressPerCosQosRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressPerCosQosRowStatus.setStatus("current")


class _IhubEgressPerCosQosPktPrio_Type(Integer32):
    """Custom type ihubEgressPerCosQosPktPrio based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IhubEgressPerCosQosPktPrio_Type.__name__ = "Integer32"
_IhubEgressPerCosQosPktPrio_Object = MibTableColumn
ihubEgressPerCosQosPktPrio = _IhubEgressPerCosQosPktPrio_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1, 3),
    _IhubEgressPerCosQosPktPrio_Type()
)
ihubEgressPerCosQosPktPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressPerCosQosPktPrio.setStatus("current")


class _IhubEgressPerCosQosCirRate_Type(TCIRRate):
    """Custom type ihubEgressPerCosQosCirRate based on TCIRRate"""
    defaultValue = -1


_IhubEgressPerCosQosCirRate_Type.__name__ = "TCIRRate"
_IhubEgressPerCosQosCirRate_Object = MibTableColumn
ihubEgressPerCosQosCirRate = _IhubEgressPerCosQosCirRate_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1, 4),
    _IhubEgressPerCosQosCirRate_Type()
)
ihubEgressPerCosQosCirRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressPerCosQosCirRate.setStatus("current")


class _IhubEgressPerCosQosPirRate_Type(TPIRRate):
    """Custom type ihubEgressPerCosQosPirRate based on TPIRRate"""
    defaultValue = -1


_IhubEgressPerCosQosPirRate_Type.__name__ = "TPIRRate"
_IhubEgressPerCosQosPirRate_Object = MibTableColumn
ihubEgressPerCosQosPirRate = _IhubEgressPerCosQosPirRate_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1, 5),
    _IhubEgressPerCosQosPirRate_Type()
)
ihubEgressPerCosQosPirRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressPerCosQosPirRate.setStatus("current")


class _IhubEgressPerCosQosCBurstSize_Type(IhubRateLimitBurstSize):
    """Custom type ihubEgressPerCosQosCBurstSize based on IhubRateLimitBurstSize"""
    defaultValue = -1


_IhubEgressPerCosQosCBurstSize_Type.__name__ = "IhubRateLimitBurstSize"
_IhubEgressPerCosQosCBurstSize_Object = MibTableColumn
ihubEgressPerCosQosCBurstSize = _IhubEgressPerCosQosCBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1, 6),
    _IhubEgressPerCosQosCBurstSize_Type()
)
ihubEgressPerCosQosCBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressPerCosQosCBurstSize.setStatus("current")


class _IhubEgressPerCosQosPBurstSize_Type(IhubRateLimitBurstSize):
    """Custom type ihubEgressPerCosQosPBurstSize based on IhubRateLimitBurstSize"""
    defaultValue = -1


_IhubEgressPerCosQosPBurstSize_Type.__name__ = "IhubRateLimitBurstSize"
_IhubEgressPerCosQosPBurstSize_Object = MibTableColumn
ihubEgressPerCosQosPBurstSize = _IhubEgressPerCosQosPBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1, 7),
    _IhubEgressPerCosQosPBurstSize_Type()
)
ihubEgressPerCosQosPBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressPerCosQosPBurstSize.setStatus("current")


class _IhubEgressPerCosQostrTcmMode_Type(Integer32):
    """Custom type ihubEgressPerCosQostrTcmMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trTCM", 1),
          ("modifiedtrTCM", 2))
    )


_IhubEgressPerCosQostrTcmMode_Type.__name__ = "Integer32"
_IhubEgressPerCosQostrTcmMode_Object = MibTableColumn
ihubEgressPerCosQostrTcmMode = _IhubEgressPerCosQostrTcmMode_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1, 8),
    _IhubEgressPerCosQostrTcmMode_Type()
)
ihubEgressPerCosQostrTcmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressPerCosQostrTcmMode.setStatus("current")


class _IhubEgressPerCosQosAdminStatus_Type(Integer32):
    """Custom type ihubEgressPerCosQosAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("disabled", 1))
    )


_IhubEgressPerCosQosAdminStatus_Type.__name__ = "Integer32"
_IhubEgressPerCosQosAdminStatus_Object = MibTableColumn
ihubEgressPerCosQosAdminStatus = _IhubEgressPerCosQosAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1, 9),
    _IhubEgressPerCosQosAdminStatus_Type()
)
ihubEgressPerCosQosAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressPerCosQosAdminStatus.setStatus("current")
_IhubEgressPerCosQosLastChanged_Type = TimeStamp
_IhubEgressPerCosQosLastChanged_Object = MibTableColumn
ihubEgressPerCosQosLastChanged = _IhubEgressPerCosQosLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 9, 1, 1, 10),
    _IhubEgressPerCosQosLastChanged_Type()
)
ihubEgressPerCosQosLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubEgressPerCosQosLastChanged.setStatus("current")
_IhubEgressSystemPortQos_ObjectIdentity = ObjectIdentity
ihubEgressSystemPortQos = _IhubEgressSystemPortQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10)
)
_IhubEgressSystemPortQosPolicyTable_Object = MibTable
ihubEgressSystemPortQosPolicyTable = _IhubEgressSystemPortQosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 1)
)
if mibBuilder.loadTexts:
    ihubEgressSystemPortQosPolicyTable.setStatus("current")
_IhubEgressSystemPortQosPolicyEntry_Object = MibTableRow
ihubEgressSystemPortQosPolicyEntry = _IhubEgressSystemPortQosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 1, 1)
)
ihubEgressSystemPortQosPolicyEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubEgressSystemPortQosPolicyId"),
)
if mibBuilder.loadTexts:
    ihubEgressSystemPortQosPolicyEntry.setStatus("current")


class _IhubEgressSystemPortQosPolicyId_Type(Integer32):
    """Custom type ihubEgressSystemPortQosPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IhubEgressSystemPortQosPolicyId_Type.__name__ = "Integer32"
_IhubEgressSystemPortQosPolicyId_Object = MibTableColumn
ihubEgressSystemPortQosPolicyId = _IhubEgressSystemPortQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 1, 1, 1),
    _IhubEgressSystemPortQosPolicyId_Type()
)
ihubEgressSystemPortQosPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubEgressSystemPortQosPolicyId.setStatus("current")


class _IhubEgressSystemPortQosPolicyDescription_Type(TItemDescription):
    """Custom type ihubEgressSystemPortQosPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_IhubEgressSystemPortQosPolicyDescription_Type.__name__ = "TItemDescription"
_IhubEgressSystemPortQosPolicyDescription_Object = MibTableColumn
ihubEgressSystemPortQosPolicyDescription = _IhubEgressSystemPortQosPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 1, 1, 2),
    _IhubEgressSystemPortQosPolicyDescription_Type()
)
ihubEgressSystemPortQosPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressSystemPortQosPolicyDescription.setStatus("current")


class _IhubEgressSystemPortQosPolicyQueueMode_Type(Integer32):
    """Custom type ihubEgressSystemPortQosPolicyQueueMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("four", 1),
          ("eight", 2))
    )


_IhubEgressSystemPortQosPolicyQueueMode_Type.__name__ = "Integer32"
_IhubEgressSystemPortQosPolicyQueueMode_Object = MibTableColumn
ihubEgressSystemPortQosPolicyQueueMode = _IhubEgressSystemPortQosPolicyQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 1, 1, 3),
    _IhubEgressSystemPortQosPolicyQueueMode_Type()
)
ihubEgressSystemPortQosPolicyQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressSystemPortQosPolicyQueueMode.setStatus("current")
_IhubEgressSystemPortQosPolicyRowStatus_Type = RowStatus
_IhubEgressSystemPortQosPolicyRowStatus_Object = MibTableColumn
ihubEgressSystemPortQosPolicyRowStatus = _IhubEgressSystemPortQosPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 1, 1, 4),
    _IhubEgressSystemPortQosPolicyRowStatus_Type()
)
ihubEgressSystemPortQosPolicyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressSystemPortQosPolicyRowStatus.setStatus("current")
_IhubEgressSystemPortQosPolicyLastChanged_Type = TimeStamp
_IhubEgressSystemPortQosPolicyLastChanged_Object = MibTableColumn
ihubEgressSystemPortQosPolicyLastChanged = _IhubEgressSystemPortQosPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 1, 1, 5),
    _IhubEgressSystemPortQosPolicyLastChanged_Type()
)
ihubEgressSystemPortQosPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubEgressSystemPortQosPolicyLastChanged.setStatus("current")
_IhubFCToQueueMapTable_Object = MibTable
ihubFCToQueueMapTable = _IhubFCToQueueMapTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 2)
)
if mibBuilder.loadTexts:
    ihubFCToQueueMapTable.setStatus("current")
_IhubFCToQueueMapEntry_Object = MibTableRow
ihubFCToQueueMapEntry = _IhubFCToQueueMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 2, 1)
)
ihubFCToQueueMapEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubEgressSystemPortQosPolicyId"),
    (0, "IHUB-QOS-MIB", "ihubFCName"),
)
if mibBuilder.loadTexts:
    ihubFCToQueueMapEntry.setStatus("current")
_IhubFCName_Type = TFCName
_IhubFCName_Object = MibTableColumn
ihubFCName = _IhubFCName_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 2, 1, 1),
    _IhubFCName_Type()
)
ihubFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubFCName.setStatus("current")
_IhubUnicastQueueId_Type = IhubEgressPortQueue
_IhubUnicastQueueId_Object = MibTableColumn
ihubUnicastQueueId = _IhubUnicastQueueId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 2, 1, 2),
    _IhubUnicastQueueId_Type()
)
ihubUnicastQueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubUnicastQueueId.setStatus("current")
_IhubNonUnicastQueueId_Type = IhubEgressPortQueue
_IhubNonUnicastQueueId_Object = MibTableColumn
ihubNonUnicastQueueId = _IhubNonUnicastQueueId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 2, 1, 3),
    _IhubNonUnicastQueueId_Type()
)
ihubNonUnicastQueueId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubNonUnicastQueueId.setStatus("current")
_IhubEgressPortQueueTable_Object = MibTable
ihubEgressPortQueueTable = _IhubEgressPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 3)
)
if mibBuilder.loadTexts:
    ihubEgressPortQueueTable.setStatus("current")
_IhubEgressPortQueueEntry_Object = MibTableRow
ihubEgressPortQueueEntry = _IhubEgressPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 3, 1)
)
ihubEgressPortQueueEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubEgressSystemPortQosPolicyId"),
    (0, "IHUB-QOS-MIB", "ihubEgressPortQueueId"),
)
if mibBuilder.loadTexts:
    ihubEgressPortQueueEntry.setStatus("current")
_IhubEgressPortQueueId_Type = IhubEgressPortQueue
_IhubEgressPortQueueId_Object = MibTableColumn
ihubEgressPortQueueId = _IhubEgressPortQueueId_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 3, 1, 1),
    _IhubEgressPortQueueId_Type()
)
ihubEgressPortQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ihubEgressPortQueueId.setStatus("current")


class _IhubEgressPortQueueWeight_Type(Integer32):
    """Custom type ihubEgressPortQueueWeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_IhubEgressPortQueueWeight_Type.__name__ = "Integer32"
_IhubEgressPortQueueWeight_Object = MibTableColumn
ihubEgressPortQueueWeight = _IhubEgressPortQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 3, 1, 2),
    _IhubEgressPortQueueWeight_Type()
)
ihubEgressPortQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressPortQueueWeight.setStatus("current")


class _IhubEgressPortQueuePriority_Type(Integer32):
    """Custom type ihubEgressPortQueuePriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IhubEgressPortQueuePriority_Type.__name__ = "Integer32"
_IhubEgressPortQueuePriority_Object = MibTableColumn
ihubEgressPortQueuePriority = _IhubEgressPortQueuePriority_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 3, 1, 3),
    _IhubEgressPortQueuePriority_Type()
)
ihubEgressPortQueuePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressPortQueuePriority.setStatus("current")


class _IhubSystemEgressPortQosPolicy_Type(Integer32):
    """Custom type ihubSystemEgressPortQosPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IhubSystemEgressPortQosPolicy_Type.__name__ = "Integer32"
_IhubSystemEgressPortQosPolicy_Object = MibScalar
ihubSystemEgressPortQosPolicy = _IhubSystemEgressPortQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 10, 4),
    _IhubSystemEgressPortQosPolicy_Type()
)
ihubSystemEgressPortQosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubSystemEgressPortQosPolicy.setStatus("current")
_IhubIngressSystemStormControl_ObjectIdentity = ObjectIdentity
ihubIngressSystemStormControl = _IhubIngressSystemStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 11)
)
_IhubIngressSystemStormControlTable_Object = MibTable
ihubIngressSystemStormControlTable = _IhubIngressSystemStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 11, 1)
)
if mibBuilder.loadTexts:
    ihubIngressSystemStormControlTable.setStatus("current")
_IhubIngressSystemStormControlEntry_Object = MibTableRow
ihubIngressSystemStormControlEntry = _IhubIngressSystemStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 11, 1, 1)
)
ihubIngressSystemStormControlEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubIngressSystemStormControlType"),
)
if mibBuilder.loadTexts:
    ihubIngressSystemStormControlEntry.setStatus("current")


class _IhubIngressSystemStormControlType_Type(Integer32):
    """Custom type ihubIngressSystemStormControlType based on Integer32"""
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
        *(("broadcast", 1),
          ("unknown-unicast", 2),
          ("unknown-multicast", 3),
          ("aggregate", 4))
    )


_IhubIngressSystemStormControlType_Type.__name__ = "Integer32"
_IhubIngressSystemStormControlType_Object = MibTableColumn
ihubIngressSystemStormControlType = _IhubIngressSystemStormControlType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 11, 1, 1, 1),
    _IhubIngressSystemStormControlType_Type()
)
ihubIngressSystemStormControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubIngressSystemStormControlType.setStatus("current")


class _IhubIngressSystemStormControlRate_Type(Integer32):
    """Custom type ihubIngressSystemStormControlRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )


_IhubIngressSystemStormControlRate_Type.__name__ = "Integer32"
_IhubIngressSystemStormControlRate_Object = MibTableColumn
ihubIngressSystemStormControlRate = _IhubIngressSystemStormControlRate_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 11, 1, 1, 2),
    _IhubIngressSystemStormControlRate_Type()
)
ihubIngressSystemStormControlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubIngressSystemStormControlRate.setStatus("current")


class _IhubIngressSystemStormControlBurstSize_Type(IhubRateLimitBurstSize):
    """Custom type ihubIngressSystemStormControlBurstSize based on IhubRateLimitBurstSize"""
    defaultValue = -1


_IhubIngressSystemStormControlBurstSize_Type.__name__ = "IhubRateLimitBurstSize"
_IhubIngressSystemStormControlBurstSize_Object = MibTableColumn
ihubIngressSystemStormControlBurstSize = _IhubIngressSystemStormControlBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 11, 1, 1, 3),
    _IhubIngressSystemStormControlBurstSize_Type()
)
ihubIngressSystemStormControlBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubIngressSystemStormControlBurstSize.setStatus("current")
_IhubEgressSystemStormControl_ObjectIdentity = ObjectIdentity
ihubEgressSystemStormControl = _IhubEgressSystemStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 12)
)
_IhubEgressSystemStormControlTable_Object = MibTable
ihubEgressSystemStormControlTable = _IhubEgressSystemStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 12, 1)
)
if mibBuilder.loadTexts:
    ihubEgressSystemStormControlTable.setStatus("current")
_IhubEgressSystemStormControlEntry_Object = MibTableRow
ihubEgressSystemStormControlEntry = _IhubEgressSystemStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 12, 1, 1)
)
ihubEgressSystemStormControlEntry.setIndexNames(
    (0, "IHUB-QOS-MIB", "ihubEgressSystemStormControlType"),
)
if mibBuilder.loadTexts:
    ihubEgressSystemStormControlEntry.setStatus("current")


class _IhubEgressSystemStormControlType_Type(Integer32):
    """Custom type ihubEgressSystemStormControlType based on Integer32"""
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
        *(("broadcast", 1),
          ("unknown-unicast", 2),
          ("unknown-multicast", 3),
          ("aggregate", 4))
    )


_IhubEgressSystemStormControlType_Type.__name__ = "Integer32"
_IhubEgressSystemStormControlType_Object = MibTableColumn
ihubEgressSystemStormControlType = _IhubEgressSystemStormControlType_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 12, 1, 1, 1),
    _IhubEgressSystemStormControlType_Type()
)
ihubEgressSystemStormControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ihubEgressSystemStormControlType.setStatus("current")


class _IhubEgressSystemStormControlRate_Type(Integer32):
    """Custom type ihubEgressSystemStormControlRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )


_IhubEgressSystemStormControlRate_Type.__name__ = "Integer32"
_IhubEgressSystemStormControlRate_Object = MibTableColumn
ihubEgressSystemStormControlRate = _IhubEgressSystemStormControlRate_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 12, 1, 1, 2),
    _IhubEgressSystemStormControlRate_Type()
)
ihubEgressSystemStormControlRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressSystemStormControlRate.setStatus("current")


class _IhubEgressSystemStormControlBurstSize_Type(IhubRateLimitBurstSize):
    """Custom type ihubEgressSystemStormControlBurstSize based on IhubRateLimitBurstSize"""
    defaultValue = -1


_IhubEgressSystemStormControlBurstSize_Type.__name__ = "IhubRateLimitBurstSize"
_IhubEgressSystemStormControlBurstSize_Object = MibTableColumn
ihubEgressSystemStormControlBurstSize = _IhubEgressSystemStormControlBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 637, 61, 1, 87, 12, 1, 1, 3),
    _IhubEgressSystemStormControlBurstSize_Type()
)
ihubEgressSystemStormControlBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ihubEgressSystemStormControlBurstSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IHUB-QOS-MIB",
    **{"PolicyRefCount": PolicyRefCount,
       "TQosVcTypeSet": TQosVcTypeSet,
       "IhubRateLimitBurstSize": IhubRateLimitBurstSize,
       "IhubEgressPortQueue": IhubEgressPortQueue,
       "ihubQosMIB": ihubQosMIB,
       "ihubIngressQos": ihubIngressQos,
       "ihubQosIngressPolicyTable": ihubQosIngressPolicyTable,
       "ihubQosIngressPolicyEntry": ihubQosIngressPolicyEntry,
       "ihubQosIngressPolicyIndex": ihubQosIngressPolicyIndex,
       "ihubQosIngressPolicyRowStatus": ihubQosIngressPolicyRowStatus,
       "ihubQosIngressPolicyScope": ihubQosIngressPolicyScope,
       "ihubQosIngressPolicyDescription": ihubQosIngressPolicyDescription,
       "ihubQosIngressPolicyRefCount": ihubQosIngressPolicyRefCount,
       "ihubQosIngressPolicyDefaultFC": ihubQosIngressPolicyDefaultFC,
       "ihubQosIngressPolicyDefaultProfile": ihubQosIngressPolicyDefaultProfile,
       "ihubQosIngressPolicyUntaggedDot1p": ihubQosIngressPolicyUntaggedDot1p,
       "ihubQosIngressPolicyLastChanged": ihubQosIngressPolicyLastChanged,
       "ihubQosIngressDSCPTable": ihubQosIngressDSCPTable,
       "ihubQosIngressDSCPEntry": ihubQosIngressDSCPEntry,
       "ihubQosIngressDSCP": ihubQosIngressDSCP,
       "ihubQosIngressDSCPRowStatus": ihubQosIngressDSCPRowStatus,
       "ihubQosIngressDSCPFC": ihubQosIngressDSCPFC,
       "ihubQosIngressDSCPProfile": ihubQosIngressDSCPProfile,
       "ihubQosIngressDSCPLastChanged": ihubQosIngressDSCPLastChanged,
       "ihubQosIngressPrecTable": ihubQosIngressPrecTable,
       "ihubQosIngressPrecEntry": ihubQosIngressPrecEntry,
       "ihubQosIngressPrecValue": ihubQosIngressPrecValue,
       "ihubQosIngressPrecRowStatus": ihubQosIngressPrecRowStatus,
       "ihubQosIngressPrecFC": ihubQosIngressPrecFC,
       "ihubQosIngressPrecProfile": ihubQosIngressPrecProfile,
       "ihubQosIngressPrecLastChanged": ihubQosIngressPrecLastChanged,
       "ihubQosIngressDot1pTable": ihubQosIngressDot1pTable,
       "ihubQosIngressDot1pEntry": ihubQosIngressDot1pEntry,
       "ihubQosIngressDot1pValue": ihubQosIngressDot1pValue,
       "ihubQosIngressDot1pRowStatus": ihubQosIngressDot1pRowStatus,
       "ihubQosIngressDot1pFC": ihubQosIngressDot1pFC,
       "ihubQosIngressDot1pProfile": ihubQosIngressDot1pProfile,
       "ihubQosIngressDot1pLastChanged": ihubQosIngressDot1pLastChanged,
       "ihubSgtQos": ihubSgtQos,
       "ihubQosSgtPolicyTable": ihubQosSgtPolicyTable,
       "ihubQosSgtPolicyEntry": ihubQosSgtPolicyEntry,
       "ihubQosSgtPolicyIndex": ihubQosSgtPolicyIndex,
       "ihubQosSgtPolicyRowStatus": ihubQosSgtPolicyRowStatus,
       "ihubQosSgtPolicyScope": ihubQosSgtPolicyScope,
       "ihubQosSgtPolicyDescription": ihubQosSgtPolicyDescription,
       "ihubQosSgtPolicyRefCount": ihubQosSgtPolicyRefCount,
       "ihubQosSgtPolicyDefaultDSCP": ihubQosSgtPolicyDefaultDSCP,
       "ihubQosSgtPolicyDefaultDot1p": ihubQosSgtPolicyDefaultDot1p,
       "ihubQosSgtPolicyLastChanged": ihubQosSgtPolicyLastChanged,
       "ihubQosSgtPolicyDefaultLspExp": ihubQosSgtPolicyDefaultLspExp,
       "ihubIngressNetworkQos": ihubIngressNetworkQos,
       "ihubQosIngressNetworkPolicyTable": ihubQosIngressNetworkPolicyTable,
       "ihubQosIngressNetworkPolicyEntry": ihubQosIngressNetworkPolicyEntry,
       "ihubQosIngressNetworkPolicyIndex": ihubQosIngressNetworkPolicyIndex,
       "ihubQosIngressNetworkPolicyRowStatus": ihubQosIngressNetworkPolicyRowStatus,
       "ihubQosIngressNetworkPolicyScope": ihubQosIngressNetworkPolicyScope,
       "ihubQosIngressNetworkPolicyDescription": ihubQosIngressNetworkPolicyDescription,
       "ihubQosIngressNetworkPolicyRefCount": ihubQosIngressNetworkPolicyRefCount,
       "ihubQosIngressNetworkPolicyDefaultFC": ihubQosIngressNetworkPolicyDefaultFC,
       "ihubQosIngressNetworkPolicyDefaultProfile": ihubQosIngressNetworkPolicyDefaultProfile,
       "ihubQosIngressNetworkPolicyLerUseDot1p": ihubQosIngressNetworkPolicyLerUseDot1p,
       "ihubQosIngressNetworkPolicyLastChanged": ihubQosIngressNetworkPolicyLastChanged,
       "ihubQosIngressNetworkDot1pTable": ihubQosIngressNetworkDot1pTable,
       "ihubQosIngressNetworkDot1pEntry": ihubQosIngressNetworkDot1pEntry,
       "ihubQosIngressNetworkDot1pValue": ihubQosIngressNetworkDot1pValue,
       "ihubQosIngressNetworkDot1pRowStatus": ihubQosIngressNetworkDot1pRowStatus,
       "ihubQosIngressNetworkDot1pFC": ihubQosIngressNetworkDot1pFC,
       "ihubQosIngressNetworkDot1pProfile": ihubQosIngressNetworkDot1pProfile,
       "ihubQosIngressNetworkDot1pLastChanged": ihubQosIngressNetworkDot1pLastChanged,
       "ihubQosIngressNetworkLspExpTable": ihubQosIngressNetworkLspExpTable,
       "ihubQosIngressNetworkLspExpEntry": ihubQosIngressNetworkLspExpEntry,
       "ihubQosIngressNetworkLspExpValue": ihubQosIngressNetworkLspExpValue,
       "ihubQosIngressNetworkLspExpRowStatus": ihubQosIngressNetworkLspExpRowStatus,
       "ihubQosIngressNetworkLspExpFC": ihubQosIngressNetworkLspExpFC,
       "ihubQosIngressNetworkLspExpProfile": ihubQosIngressNetworkLspExpProfile,
       "ihubQosIngressNetworkLspExpLastChanged": ihubQosIngressNetworkLspExpLastChanged,
       "ihubQosIngressLsrNetworkPolicyTable": ihubQosIngressLsrNetworkPolicyTable,
       "ihubQosIngressLsrNetworkPolicyEntry": ihubQosIngressLsrNetworkPolicyEntry,
       "ihubQosIngressLsrNetworkPolicyIndex": ihubQosIngressLsrNetworkPolicyIndex,
       "ihubQosIngressLsrNetworkPolicyRowStatus": ihubQosIngressLsrNetworkPolicyRowStatus,
       "ihubQosIngressLsrNetworkPolicyScope": ihubQosIngressLsrNetworkPolicyScope,
       "ihubQosIngressLsrNetworkPolicyDescription": ihubQosIngressLsrNetworkPolicyDescription,
       "ihubQosIngressLsrNetworkPolicyRefCount": ihubQosIngressLsrNetworkPolicyRefCount,
       "ihubQosIngressLsrNetworkPolicyDefaultFC": ihubQosIngressLsrNetworkPolicyDefaultFC,
       "ihubQosIngressLsrNetworkPolicyDefaultProfile": ihubQosIngressLsrNetworkPolicyDefaultProfile,
       "ihubQosIngressLsrNetworkPolicyLastChanged": ihubQosIngressLsrNetworkPolicyLastChanged,
       "ihubQosIngressLsrNetworkLspExpTable": ihubQosIngressLsrNetworkLspExpTable,
       "ihubQosIngressLsrNetworkLspExpEntry": ihubQosIngressLsrNetworkLspExpEntry,
       "ihubQosIngressLsrNetworkLspExpValue": ihubQosIngressLsrNetworkLspExpValue,
       "ihubQosIngressLsrNetworkLspExpRowStatus": ihubQosIngressLsrNetworkLspExpRowStatus,
       "ihubQosIngressLsrNetworkLspExpFC": ihubQosIngressLsrNetworkLspExpFC,
       "ihubQosIngressLsrNetworkLspExpProfile": ihubQosIngressLsrNetworkLspExpProfile,
       "ihubQosIngressLsrNetworkLspExpLastChanged": ihubQosIngressLsrNetworkLspExpLastChanged,
       "ihubEgressNetworkQos": ihubEgressNetworkQos,
       "ihubQosEgressNetworkPolicyTable": ihubQosEgressNetworkPolicyTable,
       "ihubQosEgressNetworkPolicyEntry": ihubQosEgressNetworkPolicyEntry,
       "ihubQosEgressNetworkPolicyIndex": ihubQosEgressNetworkPolicyIndex,
       "ihubQosEgressNetworkPolicyRowStatus": ihubQosEgressNetworkPolicyRowStatus,
       "ihubQosEgressNetworkPolicyScope": ihubQosEgressNetworkPolicyScope,
       "ihubQosEgressNetworkPolicyDescription": ihubQosEgressNetworkPolicyDescription,
       "ihubQosEgressNetworkPolicyRefCount": ihubQosEgressNetworkPolicyRefCount,
       "ihubQosEgressNetworkPolicyLastChanged": ihubQosEgressNetworkPolicyLastChanged,
       "ihubQosEgressNetworkFCTable": ihubQosEgressNetworkFCTable,
       "ihubQosEgressNetworkFCEntry": ihubQosEgressNetworkFCEntry,
       "ihubQosEgressNetworkFCName": ihubQosEgressNetworkFCName,
       "ihubQosEgressNetworkFCRowStatus": ihubQosEgressNetworkFCRowStatus,
       "ihubQosEgressNetworkFCLspExpInProfile": ihubQosEgressNetworkFCLspExpInProfile,
       "ihubQosEgressNetworkFCLspExpOutProfile": ihubQosEgressNetworkFCLspExpOutProfile,
       "ihubQosEngressNetworkFCLastChanged": ihubQosEngressNetworkFCLastChanged,
       "ihubBaseRouterPolicyIds": ihubBaseRouterPolicyIds,
       "ihubBaseRouterNetworkPolicyId": ihubBaseRouterNetworkPolicyId,
       "ihubBaseRouterSgtPolicyId": ihubBaseRouterSgtPolicyId,
       "ihubIngressSystemCosQos": ihubIngressSystemCosQos,
       "ihubQosEgressRateLimitNtLoadSharingPercentage": ihubQosEgressRateLimitNtLoadSharingPercentage,
       "ihubIngressSystemDot1pTable": ihubIngressSystemDot1pTable,
       "ihubIngressSystemDot1pEntry": ihubIngressSystemDot1pEntry,
       "ihubIngressSystemDot1pValue": ihubIngressSystemDot1pValue,
       "ihubIngressSystemDot1pProfile": ihubIngressSystemDot1pProfile,
       "ihubIngressSystemDot1pLastChanged": ihubIngressSystemDot1pLastChanged,
       "ihubEgressSystemPerCosMap": ihubEgressSystemPerCosMap,
       "ihubEgressSystemDot1pMapTable": ihubEgressSystemDot1pMapTable,
       "ihubEgressSystemDot1pMapEntry": ihubEgressSystemDot1pMapEntry,
       "ihubEgressSystemDot1pFC": ihubEgressSystemDot1pFC,
       "ihubEgressSystemDot1pInProfile": ihubEgressSystemDot1pInProfile,
       "ihubEgressSystemDot1pOutProfile": ihubEgressSystemDot1pOutProfile,
       "ihubEgressSystemDot1pLastChanged": ihubEgressSystemDot1pLastChanged,
       "ihubEgressPerCosQos": ihubEgressPerCosQos,
       "ihubEgressPerCosQosTable": ihubEgressPerCosQosTable,
       "ihubEgressPerCosQosEntry": ihubEgressPerCosQosEntry,
       "ihubEgressPerCosQosPbitsIndex": ihubEgressPerCosQosPbitsIndex,
       "ihubEgressPerCosQosRowStatus": ihubEgressPerCosQosRowStatus,
       "ihubEgressPerCosQosPktPrio": ihubEgressPerCosQosPktPrio,
       "ihubEgressPerCosQosCirRate": ihubEgressPerCosQosCirRate,
       "ihubEgressPerCosQosPirRate": ihubEgressPerCosQosPirRate,
       "ihubEgressPerCosQosCBurstSize": ihubEgressPerCosQosCBurstSize,
       "ihubEgressPerCosQosPBurstSize": ihubEgressPerCosQosPBurstSize,
       "ihubEgressPerCosQostrTcmMode": ihubEgressPerCosQostrTcmMode,
       "ihubEgressPerCosQosAdminStatus": ihubEgressPerCosQosAdminStatus,
       "ihubEgressPerCosQosLastChanged": ihubEgressPerCosQosLastChanged,
       "ihubEgressSystemPortQos": ihubEgressSystemPortQos,
       "ihubEgressSystemPortQosPolicyTable": ihubEgressSystemPortQosPolicyTable,
       "ihubEgressSystemPortQosPolicyEntry": ihubEgressSystemPortQosPolicyEntry,
       "ihubEgressSystemPortQosPolicyId": ihubEgressSystemPortQosPolicyId,
       "ihubEgressSystemPortQosPolicyDescription": ihubEgressSystemPortQosPolicyDescription,
       "ihubEgressSystemPortQosPolicyQueueMode": ihubEgressSystemPortQosPolicyQueueMode,
       "ihubEgressSystemPortQosPolicyRowStatus": ihubEgressSystemPortQosPolicyRowStatus,
       "ihubEgressSystemPortQosPolicyLastChanged": ihubEgressSystemPortQosPolicyLastChanged,
       "ihubFCToQueueMapTable": ihubFCToQueueMapTable,
       "ihubFCToQueueMapEntry": ihubFCToQueueMapEntry,
       "ihubFCName": ihubFCName,
       "ihubUnicastQueueId": ihubUnicastQueueId,
       "ihubNonUnicastQueueId": ihubNonUnicastQueueId,
       "ihubEgressPortQueueTable": ihubEgressPortQueueTable,
       "ihubEgressPortQueueEntry": ihubEgressPortQueueEntry,
       "ihubEgressPortQueueId": ihubEgressPortQueueId,
       "ihubEgressPortQueueWeight": ihubEgressPortQueueWeight,
       "ihubEgressPortQueuePriority": ihubEgressPortQueuePriority,
       "ihubSystemEgressPortQosPolicy": ihubSystemEgressPortQosPolicy,
       "ihubIngressSystemStormControl": ihubIngressSystemStormControl,
       "ihubIngressSystemStormControlTable": ihubIngressSystemStormControlTable,
       "ihubIngressSystemStormControlEntry": ihubIngressSystemStormControlEntry,
       "ihubIngressSystemStormControlType": ihubIngressSystemStormControlType,
       "ihubIngressSystemStormControlRate": ihubIngressSystemStormControlRate,
       "ihubIngressSystemStormControlBurstSize": ihubIngressSystemStormControlBurstSize,
       "ihubEgressSystemStormControl": ihubEgressSystemStormControl,
       "ihubEgressSystemStormControlTable": ihubEgressSystemStormControlTable,
       "ihubEgressSystemStormControlEntry": ihubEgressSystemStormControlEntry,
       "ihubEgressSystemStormControlType": ihubEgressSystemStormControlType,
       "ihubEgressSystemStormControlRate": ihubEgressSystemStormControlRate,
       "ihubEgressSystemStormControlBurstSize": ihubEgressSystemStormControlBurstSize}
)
