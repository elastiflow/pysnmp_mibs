# SNMP MIB module (CAPWAP-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/CAPWAP-BASE-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:02:24 2025
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

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(InterfaceIndex,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifGeneralInformationGroup")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(LongUtf8String,) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "LongUtf8String")


# MODULE-IDENTITY

capwapBaseMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 196)
)
if mibBuilder.loadTexts:
    capwapBaseMIB.setRevisions(
        ("2010-04-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CapwapBaseWtpProfileIdTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )



class CapwapBaseWtpIdTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )



class CapwapBaseStationIdTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )



class CapwapBaseRadioIdTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )



class CapwapBaseTunnelModeTC(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("localBridging", 0),
          ("dot3Tunnel", 1),
          ("nativeTunnel", 2))
    )


class CapwapBaseMacTypeTC(TextualConvention, Integer32):
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
        *(("localMAC", 0),
          ("splitMAC", 1),
          ("both", 2))
    )



class CapwapBaseChannelTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("control", 2))
    )



class CapwapBaseAuthenMethodTC(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("clear", 2),
          ("x509", 3),
          ("psk", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CapwapBaseNotifications_ObjectIdentity = ObjectIdentity
capwapBaseNotifications = _CapwapBaseNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 0)
)
_CapwapBaseObjects_ObjectIdentity = ObjectIdentity
capwapBaseObjects = _CapwapBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 1)
)
_CapwapBaseAc_ObjectIdentity = ObjectIdentity
capwapBaseAc = _CapwapBaseAc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 1, 1)
)


class _CapwapBaseWtpSessions_Type(Gauge32):
    """Custom type capwapBaseWtpSessions based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CapwapBaseWtpSessions_Type.__name__ = "Gauge32"
_CapwapBaseWtpSessions_Object = MibScalar
capwapBaseWtpSessions = _CapwapBaseWtpSessions_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 1),
    _CapwapBaseWtpSessions_Type()
)
capwapBaseWtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpSessions.setStatus("current")


class _CapwapBaseWtpSessionsLimit_Type(Unsigned32):
    """Custom type capwapBaseWtpSessionsLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CapwapBaseWtpSessionsLimit_Type.__name__ = "Unsigned32"
_CapwapBaseWtpSessionsLimit_Object = MibScalar
capwapBaseWtpSessionsLimit = _CapwapBaseWtpSessionsLimit_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 2),
    _CapwapBaseWtpSessionsLimit_Type()
)
capwapBaseWtpSessionsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseWtpSessionsLimit.setStatus("current")


class _CapwapBaseStationSessions_Type(Gauge32):
    """Custom type capwapBaseStationSessions based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CapwapBaseStationSessions_Type.__name__ = "Gauge32"
_CapwapBaseStationSessions_Object = MibScalar
capwapBaseStationSessions = _CapwapBaseStationSessions_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 3),
    _CapwapBaseStationSessions_Type()
)
capwapBaseStationSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseStationSessions.setStatus("current")


class _CapwapBaseStationSessionsLimit_Type(Unsigned32):
    """Custom type capwapBaseStationSessionsLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CapwapBaseStationSessionsLimit_Type.__name__ = "Unsigned32"
_CapwapBaseStationSessionsLimit_Object = MibScalar
capwapBaseStationSessionsLimit = _CapwapBaseStationSessionsLimit_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 4),
    _CapwapBaseStationSessionsLimit_Type()
)
capwapBaseStationSessionsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseStationSessionsLimit.setStatus("current")


class _CapwapBaseDataChannelDTLSPolicyOptions_Type(Bits):
    """Custom type capwapBaseDataChannelDTLSPolicyOptions based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("clear", 1),
          ("dtls", 2))
    )

_CapwapBaseDataChannelDTLSPolicyOptions_Type.__name__ = "Bits"
_CapwapBaseDataChannelDTLSPolicyOptions_Object = MibScalar
capwapBaseDataChannelDTLSPolicyOptions = _CapwapBaseDataChannelDTLSPolicyOptions_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 5),
    _CapwapBaseDataChannelDTLSPolicyOptions_Type()
)
capwapBaseDataChannelDTLSPolicyOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseDataChannelDTLSPolicyOptions.setStatus("current")


class _CapwapBaseControlChannelAuthenOptions_Type(Bits):
    """Custom type capwapBaseControlChannelAuthenOptions based on Bits"""
    namedValues = NamedValues(
        *(("x509", 0),
          ("psk", 1))
    )

_CapwapBaseControlChannelAuthenOptions_Type.__name__ = "Bits"
_CapwapBaseControlChannelAuthenOptions_Object = MibScalar
capwapBaseControlChannelAuthenOptions = _CapwapBaseControlChannelAuthenOptions_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 6),
    _CapwapBaseControlChannelAuthenOptions_Type()
)
capwapBaseControlChannelAuthenOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseControlChannelAuthenOptions.setStatus("current")
_CapwapBaseAcNameListTable_Object = MibTable
capwapBaseAcNameListTable = _CapwapBaseAcNameListTable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 9)
)
if mibBuilder.loadTexts:
    capwapBaseAcNameListTable.setStatus("current")
_CapwapBaseAcNameListEntry_Object = MibTableRow
capwapBaseAcNameListEntry = _CapwapBaseAcNameListEntry_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 9, 1)
)
capwapBaseAcNameListEntry.setIndexNames(
    (0, "CAPWAP-BASE-MIB", "capwapBaseAcNameListId"),
)
if mibBuilder.loadTexts:
    capwapBaseAcNameListEntry.setStatus("current")


class _CapwapBaseAcNameListId_Type(Unsigned32):
    """Custom type capwapBaseAcNameListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CapwapBaseAcNameListId_Type.__name__ = "Unsigned32"
_CapwapBaseAcNameListId_Object = MibTableColumn
capwapBaseAcNameListId = _CapwapBaseAcNameListId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 9, 1, 1),
    _CapwapBaseAcNameListId_Type()
)
capwapBaseAcNameListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapBaseAcNameListId.setStatus("current")


class _CapwapBaseAcNameListName_Type(LongUtf8String):
    """Custom type capwapBaseAcNameListName based on LongUtf8String"""
    subtypeSpec = LongUtf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_CapwapBaseAcNameListName_Type.__name__ = "LongUtf8String"
_CapwapBaseAcNameListName_Object = MibTableColumn
capwapBaseAcNameListName = _CapwapBaseAcNameListName_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 9, 1, 2),
    _CapwapBaseAcNameListName_Type()
)
capwapBaseAcNameListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseAcNameListName.setStatus("current")


class _CapwapBaseAcNameListPriority_Type(Unsigned32):
    """Custom type capwapBaseAcNameListPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CapwapBaseAcNameListPriority_Type.__name__ = "Unsigned32"
_CapwapBaseAcNameListPriority_Object = MibTableColumn
capwapBaseAcNameListPriority = _CapwapBaseAcNameListPriority_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 9, 1, 3),
    _CapwapBaseAcNameListPriority_Type()
)
capwapBaseAcNameListPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseAcNameListPriority.setStatus("current")
_CapwapBaseAcNameListRowStatus_Type = RowStatus
_CapwapBaseAcNameListRowStatus_Object = MibTableColumn
capwapBaseAcNameListRowStatus = _CapwapBaseAcNameListRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 9, 1, 4),
    _CapwapBaseAcNameListRowStatus_Type()
)
capwapBaseAcNameListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseAcNameListRowStatus.setStatus("current")
_CapwapBaseMacAclTable_Object = MibTable
capwapBaseMacAclTable = _CapwapBaseMacAclTable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 10)
)
if mibBuilder.loadTexts:
    capwapBaseMacAclTable.setStatus("current")
_CapwapBaseMacAclEntry_Object = MibTableRow
capwapBaseMacAclEntry = _CapwapBaseMacAclEntry_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 10, 1)
)
capwapBaseMacAclEntry.setIndexNames(
    (0, "CAPWAP-BASE-MIB", "capwapBaseMacAclId"),
)
if mibBuilder.loadTexts:
    capwapBaseMacAclEntry.setStatus("current")
_CapwapBaseMacAclId_Type = Unsigned32
_CapwapBaseMacAclId_Object = MibTableColumn
capwapBaseMacAclId = _CapwapBaseMacAclId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 10, 1, 1),
    _CapwapBaseMacAclId_Type()
)
capwapBaseMacAclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapBaseMacAclId.setStatus("current")
_CapwapBaseMacAclStationId_Type = CapwapBaseStationIdTC
_CapwapBaseMacAclStationId_Object = MibTableColumn
capwapBaseMacAclStationId = _CapwapBaseMacAclStationId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 10, 1, 2),
    _CapwapBaseMacAclStationId_Type()
)
capwapBaseMacAclStationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseMacAclStationId.setStatus("current")
_CapwapBaseMacAclRowStatus_Type = RowStatus
_CapwapBaseMacAclRowStatus_Object = MibTableColumn
capwapBaseMacAclRowStatus = _CapwapBaseMacAclRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 1, 10, 1, 3),
    _CapwapBaseMacAclRowStatus_Type()
)
capwapBaseMacAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseMacAclRowStatus.setStatus("current")
_CapwapBaseWtps_ObjectIdentity = ObjectIdentity
capwapBaseWtps = _CapwapBaseWtps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 1, 2)
)
_CapwapBaseWtpProfileTable_Object = MibTable
capwapBaseWtpProfileTable = _CapwapBaseWtpProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1)
)
if mibBuilder.loadTexts:
    capwapBaseWtpProfileTable.setStatus("current")
_CapwapBaseWtpProfileEntry_Object = MibTableRow
capwapBaseWtpProfileEntry = _CapwapBaseWtpProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1)
)
capwapBaseWtpProfileEntry.setIndexNames(
    (0, "CAPWAP-BASE-MIB", "capwapBaseWtpProfileId"),
)
if mibBuilder.loadTexts:
    capwapBaseWtpProfileEntry.setStatus("current")
_CapwapBaseWtpProfileId_Type = CapwapBaseWtpProfileIdTC
_CapwapBaseWtpProfileId_Object = MibTableColumn
capwapBaseWtpProfileId = _CapwapBaseWtpProfileId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 1),
    _CapwapBaseWtpProfileId_Type()
)
capwapBaseWtpProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileId.setStatus("current")
_CapwapBaseWtpProfileName_Type = SnmpAdminString
_CapwapBaseWtpProfileName_Object = MibTableColumn
capwapBaseWtpProfileName = _CapwapBaseWtpProfileName_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 2),
    _CapwapBaseWtpProfileName_Type()
)
capwapBaseWtpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileName.setStatus("current")
_CapwapBaseWtpProfileWtpMacAddress_Type = CapwapBaseWtpIdTC
_CapwapBaseWtpProfileWtpMacAddress_Object = MibTableColumn
capwapBaseWtpProfileWtpMacAddress = _CapwapBaseWtpProfileWtpMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 3),
    _CapwapBaseWtpProfileWtpMacAddress_Type()
)
capwapBaseWtpProfileWtpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpMacAddress.setStatus("current")
_CapwapBaseWtpProfileWtpModelNumber_Type = SnmpAdminString
_CapwapBaseWtpProfileWtpModelNumber_Object = MibTableColumn
capwapBaseWtpProfileWtpModelNumber = _CapwapBaseWtpProfileWtpModelNumber_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 4),
    _CapwapBaseWtpProfileWtpModelNumber_Type()
)
capwapBaseWtpProfileWtpModelNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpModelNumber.setStatus("current")


class _CapwapBaseWtpProfileWtpName_Type(LongUtf8String):
    """Custom type capwapBaseWtpProfileWtpName based on LongUtf8String"""
    subtypeSpec = LongUtf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_CapwapBaseWtpProfileWtpName_Type.__name__ = "LongUtf8String"
_CapwapBaseWtpProfileWtpName_Object = MibTableColumn
capwapBaseWtpProfileWtpName = _CapwapBaseWtpProfileWtpName_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 5),
    _CapwapBaseWtpProfileWtpName_Type()
)
capwapBaseWtpProfileWtpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpName.setStatus("current")


class _CapwapBaseWtpProfileWtpLocation_Type(LongUtf8String):
    """Custom type capwapBaseWtpProfileWtpLocation based on LongUtf8String"""
    subtypeSpec = LongUtf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CapwapBaseWtpProfileWtpLocation_Type.__name__ = "LongUtf8String"
_CapwapBaseWtpProfileWtpLocation_Object = MibTableColumn
capwapBaseWtpProfileWtpLocation = _CapwapBaseWtpProfileWtpLocation_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 6),
    _CapwapBaseWtpProfileWtpLocation_Type()
)
capwapBaseWtpProfileWtpLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpLocation.setStatus("current")
_CapwapBaseWtpProfileWtpStaticIpEnable_Type = TruthValue
_CapwapBaseWtpProfileWtpStaticIpEnable_Object = MibTableColumn
capwapBaseWtpProfileWtpStaticIpEnable = _CapwapBaseWtpProfileWtpStaticIpEnable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 7),
    _CapwapBaseWtpProfileWtpStaticIpEnable_Type()
)
capwapBaseWtpProfileWtpStaticIpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpStaticIpEnable.setStatus("current")


class _CapwapBaseWtpProfileWtpStaticIpType_Type(InetAddressType):
    """Custom type capwapBaseWtpProfileWtpStaticIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_CapwapBaseWtpProfileWtpStaticIpType_Type.__name__ = "InetAddressType"
_CapwapBaseWtpProfileWtpStaticIpType_Object = MibTableColumn
capwapBaseWtpProfileWtpStaticIpType = _CapwapBaseWtpProfileWtpStaticIpType_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 8),
    _CapwapBaseWtpProfileWtpStaticIpType_Type()
)
capwapBaseWtpProfileWtpStaticIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpStaticIpType.setStatus("current")


class _CapwapBaseWtpProfileWtpStaticIpAddress_Type(InetAddress):
    """Custom type capwapBaseWtpProfileWtpStaticIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4


_CapwapBaseWtpProfileWtpStaticIpAddress_Type.__name__ = "InetAddress"
_CapwapBaseWtpProfileWtpStaticIpAddress_Object = MibTableColumn
capwapBaseWtpProfileWtpStaticIpAddress = _CapwapBaseWtpProfileWtpStaticIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 9),
    _CapwapBaseWtpProfileWtpStaticIpAddress_Type()
)
capwapBaseWtpProfileWtpStaticIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpStaticIpAddress.setStatus("current")


class _CapwapBaseWtpProfileWtpNetmask_Type(InetAddress):
    """Custom type capwapBaseWtpProfileWtpNetmask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4


_CapwapBaseWtpProfileWtpNetmask_Type.__name__ = "InetAddress"
_CapwapBaseWtpProfileWtpNetmask_Object = MibTableColumn
capwapBaseWtpProfileWtpNetmask = _CapwapBaseWtpProfileWtpNetmask_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 10),
    _CapwapBaseWtpProfileWtpNetmask_Type()
)
capwapBaseWtpProfileWtpNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpNetmask.setStatus("current")


class _CapwapBaseWtpProfileWtpGateway_Type(InetAddress):
    """Custom type capwapBaseWtpProfileWtpGateway based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4


_CapwapBaseWtpProfileWtpGateway_Type.__name__ = "InetAddress"
_CapwapBaseWtpProfileWtpGateway_Object = MibTableColumn
capwapBaseWtpProfileWtpGateway = _CapwapBaseWtpProfileWtpGateway_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 11),
    _CapwapBaseWtpProfileWtpGateway_Type()
)
capwapBaseWtpProfileWtpGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpGateway.setStatus("current")


class _CapwapBaseWtpProfileWtpFallbackEnable_Type(Integer32):
    """Custom type capwapBaseWtpProfileWtpFallbackEnable based on Integer32"""
    defaultValue = 1

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


_CapwapBaseWtpProfileWtpFallbackEnable_Type.__name__ = "Integer32"
_CapwapBaseWtpProfileWtpFallbackEnable_Object = MibTableColumn
capwapBaseWtpProfileWtpFallbackEnable = _CapwapBaseWtpProfileWtpFallbackEnable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 12),
    _CapwapBaseWtpProfileWtpFallbackEnable_Type()
)
capwapBaseWtpProfileWtpFallbackEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpFallbackEnable.setStatus("current")


class _CapwapBaseWtpProfileWtpEchoInterval_Type(Unsigned32):
    """Custom type capwapBaseWtpProfileWtpEchoInterval based on Unsigned32"""
    defaultValue = 30


_CapwapBaseWtpProfileWtpEchoInterval_Type.__name__ = "Unsigned32"
_CapwapBaseWtpProfileWtpEchoInterval_Object = MibTableColumn
capwapBaseWtpProfileWtpEchoInterval = _CapwapBaseWtpProfileWtpEchoInterval_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 13),
    _CapwapBaseWtpProfileWtpEchoInterval_Type()
)
capwapBaseWtpProfileWtpEchoInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpEchoInterval.setUnits("second")


class _CapwapBaseWtpProfileWtpIdleTimeout_Type(Unsigned32):
    """Custom type capwapBaseWtpProfileWtpIdleTimeout based on Unsigned32"""
    defaultValue = 300


_CapwapBaseWtpProfileWtpIdleTimeout_Type.__name__ = "Unsigned32"
_CapwapBaseWtpProfileWtpIdleTimeout_Object = MibTableColumn
capwapBaseWtpProfileWtpIdleTimeout = _CapwapBaseWtpProfileWtpIdleTimeout_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 14),
    _CapwapBaseWtpProfileWtpIdleTimeout_Type()
)
capwapBaseWtpProfileWtpIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpIdleTimeout.setUnits("second")


class _CapwapBaseWtpProfileWtpMaxDiscoveryInterval_Type(Unsigned32):
    """Custom type capwapBaseWtpProfileWtpMaxDiscoveryInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 180),
    )


_CapwapBaseWtpProfileWtpMaxDiscoveryInterval_Type.__name__ = "Unsigned32"
_CapwapBaseWtpProfileWtpMaxDiscoveryInterval_Object = MibTableColumn
capwapBaseWtpProfileWtpMaxDiscoveryInterval = _CapwapBaseWtpProfileWtpMaxDiscoveryInterval_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 15),
    _CapwapBaseWtpProfileWtpMaxDiscoveryInterval_Type()
)
capwapBaseWtpProfileWtpMaxDiscoveryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpMaxDiscoveryInterval.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpMaxDiscoveryInterval.setUnits("second")


class _CapwapBaseWtpProfileWtpReportInterval_Type(Unsigned32):
    """Custom type capwapBaseWtpProfileWtpReportInterval based on Unsigned32"""
    defaultValue = 120


_CapwapBaseWtpProfileWtpReportInterval_Type.__name__ = "Unsigned32"
_CapwapBaseWtpProfileWtpReportInterval_Object = MibTableColumn
capwapBaseWtpProfileWtpReportInterval = _CapwapBaseWtpProfileWtpReportInterval_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 16),
    _CapwapBaseWtpProfileWtpReportInterval_Type()
)
capwapBaseWtpProfileWtpReportInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpReportInterval.setUnits("second")


class _CapwapBaseWtpProfileWtpStatisticsTimer_Type(Unsigned32):
    """Custom type capwapBaseWtpProfileWtpStatisticsTimer based on Unsigned32"""
    defaultValue = 120


_CapwapBaseWtpProfileWtpStatisticsTimer_Type.__name__ = "Unsigned32"
_CapwapBaseWtpProfileWtpStatisticsTimer_Object = MibTableColumn
capwapBaseWtpProfileWtpStatisticsTimer = _CapwapBaseWtpProfileWtpStatisticsTimer_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 17),
    _CapwapBaseWtpProfileWtpStatisticsTimer_Type()
)
capwapBaseWtpProfileWtpStatisticsTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpStatisticsTimer.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpStatisticsTimer.setUnits("second")


class _CapwapBaseWtpProfileWtpEcnSupport_Type(Integer32):
    """Custom type capwapBaseWtpProfileWtpEcnSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("limited", 0),
          ("fullAndLimited", 1))
    )


_CapwapBaseWtpProfileWtpEcnSupport_Type.__name__ = "Integer32"
_CapwapBaseWtpProfileWtpEcnSupport_Object = MibTableColumn
capwapBaseWtpProfileWtpEcnSupport = _CapwapBaseWtpProfileWtpEcnSupport_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 18),
    _CapwapBaseWtpProfileWtpEcnSupport_Type()
)
capwapBaseWtpProfileWtpEcnSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileWtpEcnSupport.setStatus("current")
_CapwapBaseWtpProfileRowStatus_Type = RowStatus
_CapwapBaseWtpProfileRowStatus_Object = MibTableColumn
capwapBaseWtpProfileRowStatus = _CapwapBaseWtpProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 1, 1, 19),
    _CapwapBaseWtpProfileRowStatus_Type()
)
capwapBaseWtpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    capwapBaseWtpProfileRowStatus.setStatus("current")
_CapwapBaseWtpStateTable_Object = MibTable
capwapBaseWtpStateTable = _CapwapBaseWtpStateTable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2)
)
if mibBuilder.loadTexts:
    capwapBaseWtpStateTable.setStatus("current")
_CapwapBaseWtpStateEntry_Object = MibTableRow
capwapBaseWtpStateEntry = _CapwapBaseWtpStateEntry_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2, 1)
)
capwapBaseWtpStateEntry.setIndexNames(
    (0, "CAPWAP-BASE-MIB", "capwapBaseWtpStateWtpId"),
)
if mibBuilder.loadTexts:
    capwapBaseWtpStateEntry.setStatus("current")
_CapwapBaseWtpStateWtpId_Type = CapwapBaseWtpIdTC
_CapwapBaseWtpStateWtpId_Object = MibTableColumn
capwapBaseWtpStateWtpId = _CapwapBaseWtpStateWtpId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2, 1, 1),
    _CapwapBaseWtpStateWtpId_Type()
)
capwapBaseWtpStateWtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapBaseWtpStateWtpId.setStatus("current")
_CapwapBaseWtpStateWtpIpAddressType_Type = InetAddressType
_CapwapBaseWtpStateWtpIpAddressType_Object = MibTableColumn
capwapBaseWtpStateWtpIpAddressType = _CapwapBaseWtpStateWtpIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2, 1, 2),
    _CapwapBaseWtpStateWtpIpAddressType_Type()
)
capwapBaseWtpStateWtpIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpStateWtpIpAddressType.setStatus("current")
_CapwapBaseWtpStateWtpIpAddress_Type = InetAddress
_CapwapBaseWtpStateWtpIpAddress_Object = MibTableColumn
capwapBaseWtpStateWtpIpAddress = _CapwapBaseWtpStateWtpIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2, 1, 3),
    _CapwapBaseWtpStateWtpIpAddress_Type()
)
capwapBaseWtpStateWtpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpStateWtpIpAddress.setStatus("current")
_CapwapBaseWtpStateWtpLocalIpAddressType_Type = InetAddressType
_CapwapBaseWtpStateWtpLocalIpAddressType_Object = MibTableColumn
capwapBaseWtpStateWtpLocalIpAddressType = _CapwapBaseWtpStateWtpLocalIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2, 1, 4),
    _CapwapBaseWtpStateWtpLocalIpAddressType_Type()
)
capwapBaseWtpStateWtpLocalIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpStateWtpLocalIpAddressType.setStatus("current")
_CapwapBaseWtpStateWtpLocalIpAddress_Type = InetAddress
_CapwapBaseWtpStateWtpLocalIpAddress_Object = MibTableColumn
capwapBaseWtpStateWtpLocalIpAddress = _CapwapBaseWtpStateWtpLocalIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2, 1, 5),
    _CapwapBaseWtpStateWtpLocalIpAddress_Type()
)
capwapBaseWtpStateWtpLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpStateWtpLocalIpAddress.setStatus("current")


class _CapwapBaseWtpStateWtpBaseMacAddress_Type(PhysAddress):
    """Custom type capwapBaseWtpStateWtpBaseMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_CapwapBaseWtpStateWtpBaseMacAddress_Type.__name__ = "PhysAddress"
_CapwapBaseWtpStateWtpBaseMacAddress_Object = MibTableColumn
capwapBaseWtpStateWtpBaseMacAddress = _CapwapBaseWtpStateWtpBaseMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2, 1, 6),
    _CapwapBaseWtpStateWtpBaseMacAddress_Type()
)
capwapBaseWtpStateWtpBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpStateWtpBaseMacAddress.setStatus("current")


class _CapwapBaseWtpState_Type(Integer32):
    """Custom type capwapBaseWtpState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 1),
          ("join", 2),
          ("image", 3),
          ("configure", 4),
          ("dataCheck", 5),
          ("run", 6),
          ("reset", 7),
          ("dtlsTeardown", 8),
          ("unknown", 9))
    )


_CapwapBaseWtpState_Type.__name__ = "Integer32"
_CapwapBaseWtpState_Object = MibTableColumn
capwapBaseWtpState = _CapwapBaseWtpState_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2, 1, 7),
    _CapwapBaseWtpState_Type()
)
capwapBaseWtpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpState.setStatus("current")
_CapwapBaseWtpStateWtpUpTime_Type = TimeTicks
_CapwapBaseWtpStateWtpUpTime_Object = MibTableColumn
capwapBaseWtpStateWtpUpTime = _CapwapBaseWtpStateWtpUpTime_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2, 1, 8),
    _CapwapBaseWtpStateWtpUpTime_Type()
)
capwapBaseWtpStateWtpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpStateWtpUpTime.setStatus("current")
_CapwapBaseWtpStateWtpCurrWtpProfileId_Type = CapwapBaseWtpProfileIdTC
_CapwapBaseWtpStateWtpCurrWtpProfileId_Object = MibTableColumn
capwapBaseWtpStateWtpCurrWtpProfileId = _CapwapBaseWtpStateWtpCurrWtpProfileId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 2, 1, 9),
    _CapwapBaseWtpStateWtpCurrWtpProfileId_Type()
)
capwapBaseWtpStateWtpCurrWtpProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpStateWtpCurrWtpProfileId.setStatus("current")
_CapwapBaseWtpTable_Object = MibTable
capwapBaseWtpTable = _CapwapBaseWtpTable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3)
)
if mibBuilder.loadTexts:
    capwapBaseWtpTable.setStatus("current")
_CapwapBaseWtpEntry_Object = MibTableRow
capwapBaseWtpEntry = _CapwapBaseWtpEntry_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3, 1)
)
capwapBaseWtpEntry.setIndexNames(
    (0, "CAPWAP-BASE-MIB", "capwapBaseWtpCurrId"),
)
if mibBuilder.loadTexts:
    capwapBaseWtpEntry.setStatus("current")
_CapwapBaseWtpCurrId_Type = CapwapBaseWtpIdTC
_CapwapBaseWtpCurrId_Object = MibTableColumn
capwapBaseWtpCurrId = _CapwapBaseWtpCurrId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3, 1, 1),
    _CapwapBaseWtpCurrId_Type()
)
capwapBaseWtpCurrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapBaseWtpCurrId.setStatus("current")
_CapwapBaseWtpPhyIndex_Type = PhysicalIndex
_CapwapBaseWtpPhyIndex_Object = MibTableColumn
capwapBaseWtpPhyIndex = _CapwapBaseWtpPhyIndex_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3, 1, 2),
    _CapwapBaseWtpPhyIndex_Type()
)
capwapBaseWtpPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpPhyIndex.setStatus("current")


class _CapwapBaseWtpBaseMacAddress_Type(PhysAddress):
    """Custom type capwapBaseWtpBaseMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_CapwapBaseWtpBaseMacAddress_Type.__name__ = "PhysAddress"
_CapwapBaseWtpBaseMacAddress_Object = MibTableColumn
capwapBaseWtpBaseMacAddress = _CapwapBaseWtpBaseMacAddress_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3, 1, 3),
    _CapwapBaseWtpBaseMacAddress_Type()
)
capwapBaseWtpBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpBaseMacAddress.setStatus("current")
_CapwapBaseWtpTunnelModeOptions_Type = CapwapBaseTunnelModeTC
_CapwapBaseWtpTunnelModeOptions_Object = MibTableColumn
capwapBaseWtpTunnelModeOptions = _CapwapBaseWtpTunnelModeOptions_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3, 1, 4),
    _CapwapBaseWtpTunnelModeOptions_Type()
)
capwapBaseWtpTunnelModeOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpTunnelModeOptions.setStatus("current")
_CapwapBaseWtpMacTypeOptions_Type = CapwapBaseMacTypeTC
_CapwapBaseWtpMacTypeOptions_Object = MibTableColumn
capwapBaseWtpMacTypeOptions = _CapwapBaseWtpMacTypeOptions_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3, 1, 5),
    _CapwapBaseWtpMacTypeOptions_Type()
)
capwapBaseWtpMacTypeOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpMacTypeOptions.setStatus("current")


class _CapwapBaseWtpDiscoveryType_Type(Integer32):
    """Custom type capwapBaseWtpDiscoveryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("staticConfig", 1),
          ("dhcp", 2),
          ("dns", 3),
          ("acRef", 4))
    )


_CapwapBaseWtpDiscoveryType_Type.__name__ = "Integer32"
_CapwapBaseWtpDiscoveryType_Object = MibTableColumn
capwapBaseWtpDiscoveryType = _CapwapBaseWtpDiscoveryType_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3, 1, 6),
    _CapwapBaseWtpDiscoveryType_Type()
)
capwapBaseWtpDiscoveryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpDiscoveryType.setStatus("current")


class _CapwapBaseWtpRadiosInUseNum_Type(Gauge32):
    """Custom type capwapBaseWtpRadiosInUseNum based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CapwapBaseWtpRadiosInUseNum_Type.__name__ = "Gauge32"
_CapwapBaseWtpRadiosInUseNum_Object = MibTableColumn
capwapBaseWtpRadiosInUseNum = _CapwapBaseWtpRadiosInUseNum_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3, 1, 7),
    _CapwapBaseWtpRadiosInUseNum_Type()
)
capwapBaseWtpRadiosInUseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpRadiosInUseNum.setStatus("current")


class _CapwapBaseWtpRadioNumLimit_Type(Unsigned32):
    """Custom type capwapBaseWtpRadioNumLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CapwapBaseWtpRadioNumLimit_Type.__name__ = "Unsigned32"
_CapwapBaseWtpRadioNumLimit_Object = MibTableColumn
capwapBaseWtpRadioNumLimit = _CapwapBaseWtpRadioNumLimit_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3, 1, 8),
    _CapwapBaseWtpRadioNumLimit_Type()
)
capwapBaseWtpRadioNumLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpRadioNumLimit.setStatus("current")
_CapwapBaseWtpRetransmitCount_Type = Counter32
_CapwapBaseWtpRetransmitCount_Object = MibTableColumn
capwapBaseWtpRetransmitCount = _CapwapBaseWtpRetransmitCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 3, 1, 9),
    _CapwapBaseWtpRetransmitCount_Type()
)
capwapBaseWtpRetransmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpRetransmitCount.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseWtpRetransmitCount.setUnits("retransmissions")
_CapwapBaseWirelessBindingTable_Object = MibTable
capwapBaseWirelessBindingTable = _CapwapBaseWirelessBindingTable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 4)
)
if mibBuilder.loadTexts:
    capwapBaseWirelessBindingTable.setStatus("current")
_CapwapBaseWirelessBindingEntry_Object = MibTableRow
capwapBaseWirelessBindingEntry = _CapwapBaseWirelessBindingEntry_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 4, 1)
)
capwapBaseWirelessBindingEntry.setIndexNames(
    (0, "CAPWAP-BASE-MIB", "capwapBaseWtpProfileId"),
    (0, "CAPWAP-BASE-MIB", "capwapBaseWirelessBindingRadioId"),
)
if mibBuilder.loadTexts:
    capwapBaseWirelessBindingEntry.setStatus("current")
_CapwapBaseWirelessBindingRadioId_Type = CapwapBaseRadioIdTC
_CapwapBaseWirelessBindingRadioId_Object = MibTableColumn
capwapBaseWirelessBindingRadioId = _CapwapBaseWirelessBindingRadioId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 4, 1, 1),
    _CapwapBaseWirelessBindingRadioId_Type()
)
capwapBaseWirelessBindingRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapBaseWirelessBindingRadioId.setStatus("current")
_CapwapBaseWirelessBindingVirtualRadioIfIndex_Type = InterfaceIndex
_CapwapBaseWirelessBindingVirtualRadioIfIndex_Object = MibTableColumn
capwapBaseWirelessBindingVirtualRadioIfIndex = _CapwapBaseWirelessBindingVirtualRadioIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 4, 1, 2),
    _CapwapBaseWirelessBindingVirtualRadioIfIndex_Type()
)
capwapBaseWirelessBindingVirtualRadioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWirelessBindingVirtualRadioIfIndex.setStatus("current")


class _CapwapBaseWirelessBindingType_Type(Integer32):
    """Custom type capwapBaseWirelessBindingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11", 1),
          ("epc", 3))
    )


_CapwapBaseWirelessBindingType_Type.__name__ = "Integer32"
_CapwapBaseWirelessBindingType_Object = MibTableColumn
capwapBaseWirelessBindingType = _CapwapBaseWirelessBindingType_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 4, 1, 3),
    _CapwapBaseWirelessBindingType_Type()
)
capwapBaseWirelessBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWirelessBindingType.setStatus("current")
_CapwapBaseStationTable_Object = MibTable
capwapBaseStationTable = _CapwapBaseStationTable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 5)
)
if mibBuilder.loadTexts:
    capwapBaseStationTable.setStatus("current")
_CapwapBaseStationEntry_Object = MibTableRow
capwapBaseStationEntry = _CapwapBaseStationEntry_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 5, 1)
)
capwapBaseStationEntry.setIndexNames(
    (0, "CAPWAP-BASE-MIB", "capwapBaseStationId"),
)
if mibBuilder.loadTexts:
    capwapBaseStationEntry.setStatus("current")
_CapwapBaseStationId_Type = CapwapBaseStationIdTC
_CapwapBaseStationId_Object = MibTableColumn
capwapBaseStationId = _CapwapBaseStationId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 5, 1, 1),
    _CapwapBaseStationId_Type()
)
capwapBaseStationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapBaseStationId.setStatus("current")
_CapwapBaseStationWtpId_Type = CapwapBaseWtpIdTC
_CapwapBaseStationWtpId_Object = MibTableColumn
capwapBaseStationWtpId = _CapwapBaseStationWtpId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 5, 1, 2),
    _CapwapBaseStationWtpId_Type()
)
capwapBaseStationWtpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseStationWtpId.setStatus("current")
_CapwapBaseStationWtpRadioId_Type = CapwapBaseRadioIdTC
_CapwapBaseStationWtpRadioId_Object = MibTableColumn
capwapBaseStationWtpRadioId = _CapwapBaseStationWtpRadioId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 5, 1, 3),
    _CapwapBaseStationWtpRadioId_Type()
)
capwapBaseStationWtpRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseStationWtpRadioId.setStatus("current")
_CapwapBaseStationAddedTime_Type = DateAndTime
_CapwapBaseStationAddedTime_Object = MibTableColumn
capwapBaseStationAddedTime = _CapwapBaseStationAddedTime_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 5, 1, 4),
    _CapwapBaseStationAddedTime_Type()
)
capwapBaseStationAddedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseStationAddedTime.setStatus("current")


class _CapwapBaseStationVlanName_Type(SnmpAdminString):
    """Custom type capwapBaseStationVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CapwapBaseStationVlanName_Type.__name__ = "SnmpAdminString"
_CapwapBaseStationVlanName_Object = MibTableColumn
capwapBaseStationVlanName = _CapwapBaseStationVlanName_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 5, 1, 5),
    _CapwapBaseStationVlanName_Type()
)
capwapBaseStationVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseStationVlanName.setStatus("current")
_CapwapBaseWtpEventsStatsTable_Object = MibTable
capwapBaseWtpEventsStatsTable = _CapwapBaseWtpEventsStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 6)
)
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsTable.setStatus("current")
_CapwapBaseWtpEventsStatsEntry_Object = MibTableRow
capwapBaseWtpEventsStatsEntry = _CapwapBaseWtpEventsStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 6, 1)
)
capwapBaseWtpEventsStatsEntry.setIndexNames(
    (0, "CAPWAP-BASE-MIB", "capwapBaseWtpCurrId"),
)
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsEntry.setStatus("current")
_CapwapBaseWtpEventsStatsRebootCount_Type = Counter32
_CapwapBaseWtpEventsStatsRebootCount_Object = MibTableColumn
capwapBaseWtpEventsStatsRebootCount = _CapwapBaseWtpEventsStatsRebootCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 6, 1, 1),
    _CapwapBaseWtpEventsStatsRebootCount_Type()
)
capwapBaseWtpEventsStatsRebootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsRebootCount.setStatus("current")
_CapwapBaseWtpEventsStatsInitCount_Type = Counter32
_CapwapBaseWtpEventsStatsInitCount_Object = MibTableColumn
capwapBaseWtpEventsStatsInitCount = _CapwapBaseWtpEventsStatsInitCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 6, 1, 2),
    _CapwapBaseWtpEventsStatsInitCount_Type()
)
capwapBaseWtpEventsStatsInitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsInitCount.setStatus("current")
_CapwapBaseWtpEventsStatsLinkFailureCount_Type = Counter32
_CapwapBaseWtpEventsStatsLinkFailureCount_Object = MibTableColumn
capwapBaseWtpEventsStatsLinkFailureCount = _CapwapBaseWtpEventsStatsLinkFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 6, 1, 3),
    _CapwapBaseWtpEventsStatsLinkFailureCount_Type()
)
capwapBaseWtpEventsStatsLinkFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsLinkFailureCount.setStatus("current")
_CapwapBaseWtpEventsStatsSwFailureCount_Type = Counter32
_CapwapBaseWtpEventsStatsSwFailureCount_Object = MibTableColumn
capwapBaseWtpEventsStatsSwFailureCount = _CapwapBaseWtpEventsStatsSwFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 6, 1, 4),
    _CapwapBaseWtpEventsStatsSwFailureCount_Type()
)
capwapBaseWtpEventsStatsSwFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsSwFailureCount.setStatus("current")
_CapwapBaseWtpEventsStatsHwFailureCount_Type = Counter32
_CapwapBaseWtpEventsStatsHwFailureCount_Object = MibTableColumn
capwapBaseWtpEventsStatsHwFailureCount = _CapwapBaseWtpEventsStatsHwFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 6, 1, 5),
    _CapwapBaseWtpEventsStatsHwFailureCount_Type()
)
capwapBaseWtpEventsStatsHwFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsHwFailureCount.setStatus("current")
_CapwapBaseWtpEventsStatsOtherFailureCount_Type = Counter32
_CapwapBaseWtpEventsStatsOtherFailureCount_Object = MibTableColumn
capwapBaseWtpEventsStatsOtherFailureCount = _CapwapBaseWtpEventsStatsOtherFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 6, 1, 6),
    _CapwapBaseWtpEventsStatsOtherFailureCount_Type()
)
capwapBaseWtpEventsStatsOtherFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsOtherFailureCount.setStatus("current")
_CapwapBaseWtpEventsStatsUnknownFailureCount_Type = Counter32
_CapwapBaseWtpEventsStatsUnknownFailureCount_Object = MibTableColumn
capwapBaseWtpEventsStatsUnknownFailureCount = _CapwapBaseWtpEventsStatsUnknownFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 6, 1, 7),
    _CapwapBaseWtpEventsStatsUnknownFailureCount_Type()
)
capwapBaseWtpEventsStatsUnknownFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsUnknownFailureCount.setStatus("current")


class _CapwapBaseWtpEventsStatsLastFailureType_Type(Integer32):
    """Custom type capwapBaseWtpEventsStatsLastFailureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 0),
          ("acInit", 1),
          ("linkFailure", 2),
          ("swFailure", 3),
          ("hwFailure", 4),
          ("otherFailure", 5),
          ("unknown", 255))
    )


_CapwapBaseWtpEventsStatsLastFailureType_Type.__name__ = "Integer32"
_CapwapBaseWtpEventsStatsLastFailureType_Object = MibTableColumn
capwapBaseWtpEventsStatsLastFailureType = _CapwapBaseWtpEventsStatsLastFailureType_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 6, 1, 8),
    _CapwapBaseWtpEventsStatsLastFailureType_Type()
)
capwapBaseWtpEventsStatsLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsLastFailureType.setStatus("current")
_CapwapBaseRadioEventsStatsTable_Object = MibTable
capwapBaseRadioEventsStatsTable = _CapwapBaseRadioEventsStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7)
)
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsTable.setStatus("current")
_CapwapBaseRadioEventsStatsEntry_Object = MibTableRow
capwapBaseRadioEventsStatsEntry = _CapwapBaseRadioEventsStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1)
)
capwapBaseRadioEventsStatsEntry.setIndexNames(
    (0, "CAPWAP-BASE-MIB", "capwapBaseWtpCurrId"),
    (0, "CAPWAP-BASE-MIB", "capwapBaseRadioEventsWtpRadioId"),
)
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsEntry.setStatus("current")
_CapwapBaseRadioEventsWtpRadioId_Type = CapwapBaseRadioIdTC
_CapwapBaseRadioEventsWtpRadioId_Object = MibTableColumn
capwapBaseRadioEventsWtpRadioId = _CapwapBaseRadioEventsWtpRadioId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 1),
    _CapwapBaseRadioEventsWtpRadioId_Type()
)
capwapBaseRadioEventsWtpRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsWtpRadioId.setStatus("current")
_CapwapBaseRadioEventsStatsResetCount_Type = Counter32
_CapwapBaseRadioEventsStatsResetCount_Object = MibTableColumn
capwapBaseRadioEventsStatsResetCount = _CapwapBaseRadioEventsStatsResetCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 2),
    _CapwapBaseRadioEventsStatsResetCount_Type()
)
capwapBaseRadioEventsStatsResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsResetCount.setStatus("current")
_CapwapBaseRadioEventsStatsSwFailureCount_Type = Counter32
_CapwapBaseRadioEventsStatsSwFailureCount_Object = MibTableColumn
capwapBaseRadioEventsStatsSwFailureCount = _CapwapBaseRadioEventsStatsSwFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 3),
    _CapwapBaseRadioEventsStatsSwFailureCount_Type()
)
capwapBaseRadioEventsStatsSwFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsSwFailureCount.setStatus("current")
_CapwapBaseRadioEventsStatsHwFailureCount_Type = Counter32
_CapwapBaseRadioEventsStatsHwFailureCount_Object = MibTableColumn
capwapBaseRadioEventsStatsHwFailureCount = _CapwapBaseRadioEventsStatsHwFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 4),
    _CapwapBaseRadioEventsStatsHwFailureCount_Type()
)
capwapBaseRadioEventsStatsHwFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsHwFailureCount.setStatus("current")
_CapwapBaseRadioEventsStatsOtherFailureCount_Type = Counter32
_CapwapBaseRadioEventsStatsOtherFailureCount_Object = MibTableColumn
capwapBaseRadioEventsStatsOtherFailureCount = _CapwapBaseRadioEventsStatsOtherFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 5),
    _CapwapBaseRadioEventsStatsOtherFailureCount_Type()
)
capwapBaseRadioEventsStatsOtherFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsOtherFailureCount.setStatus("current")
_CapwapBaseRadioEventsStatsUnknownFailureCount_Type = Counter32
_CapwapBaseRadioEventsStatsUnknownFailureCount_Object = MibTableColumn
capwapBaseRadioEventsStatsUnknownFailureCount = _CapwapBaseRadioEventsStatsUnknownFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 6),
    _CapwapBaseRadioEventsStatsUnknownFailureCount_Type()
)
capwapBaseRadioEventsStatsUnknownFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsUnknownFailureCount.setStatus("current")
_CapwapBaseRadioEventsStatsConfigUpdateCount_Type = Counter32
_CapwapBaseRadioEventsStatsConfigUpdateCount_Object = MibTableColumn
capwapBaseRadioEventsStatsConfigUpdateCount = _CapwapBaseRadioEventsStatsConfigUpdateCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 7),
    _CapwapBaseRadioEventsStatsConfigUpdateCount_Type()
)
capwapBaseRadioEventsStatsConfigUpdateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsConfigUpdateCount.setStatus("current")
_CapwapBaseRadioEventsStatsChannelChangeCount_Type = Counter32
_CapwapBaseRadioEventsStatsChannelChangeCount_Object = MibTableColumn
capwapBaseRadioEventsStatsChannelChangeCount = _CapwapBaseRadioEventsStatsChannelChangeCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 8),
    _CapwapBaseRadioEventsStatsChannelChangeCount_Type()
)
capwapBaseRadioEventsStatsChannelChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsChannelChangeCount.setStatus("current")
_CapwapBaseRadioEventsStatsBandChangeCount_Type = Counter32
_CapwapBaseRadioEventsStatsBandChangeCount_Object = MibTableColumn
capwapBaseRadioEventsStatsBandChangeCount = _CapwapBaseRadioEventsStatsBandChangeCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 9),
    _CapwapBaseRadioEventsStatsBandChangeCount_Type()
)
capwapBaseRadioEventsStatsBandChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsBandChangeCount.setStatus("current")
_CapwapBaseRadioEventsStatsCurrNoiseFloor_Type = Integer32
_CapwapBaseRadioEventsStatsCurrNoiseFloor_Object = MibTableColumn
capwapBaseRadioEventsStatsCurrNoiseFloor = _CapwapBaseRadioEventsStatsCurrNoiseFloor_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 10),
    _CapwapBaseRadioEventsStatsCurrNoiseFloor_Type()
)
capwapBaseRadioEventsStatsCurrNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsCurrNoiseFloor.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsCurrNoiseFloor.setUnits("dBm")
_CapwapBaseRadioEventsStatsDecryptErrorCount_Type = Counter32
_CapwapBaseRadioEventsStatsDecryptErrorCount_Object = MibTableColumn
capwapBaseRadioEventsStatsDecryptErrorCount = _CapwapBaseRadioEventsStatsDecryptErrorCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 11),
    _CapwapBaseRadioEventsStatsDecryptErrorCount_Type()
)
capwapBaseRadioEventsStatsDecryptErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsDecryptErrorCount.setStatus("current")


class _CapwapBaseRadioEventsStatsLastFailureType_Type(Integer32):
    """Custom type capwapBaseRadioEventsStatsLastFailureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 0),
          ("swFailure", 1),
          ("hwFailure", 2),
          ("otherFailure", 3),
          ("unknown", 255))
    )


_CapwapBaseRadioEventsStatsLastFailureType_Type.__name__ = "Integer32"
_CapwapBaseRadioEventsStatsLastFailureType_Object = MibTableColumn
capwapBaseRadioEventsStatsLastFailureType = _CapwapBaseRadioEventsStatsLastFailureType_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 2, 7, 1, 12),
    _CapwapBaseRadioEventsStatsLastFailureType_Type()
)
capwapBaseRadioEventsStatsLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsLastFailureType.setStatus("current")
_CapwapBaseParameters_ObjectIdentity = ObjectIdentity
capwapBaseParameters = _CapwapBaseParameters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 1, 3)
)


class _CapwapBaseAcMaxRetransmit_Type(Unsigned32):
    """Custom type capwapBaseAcMaxRetransmit based on Unsigned32"""
    defaultValue = 5


_CapwapBaseAcMaxRetransmit_Type.__name__ = "Unsigned32"
_CapwapBaseAcMaxRetransmit_Object = MibScalar
capwapBaseAcMaxRetransmit = _CapwapBaseAcMaxRetransmit_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 3, 1),
    _CapwapBaseAcMaxRetransmit_Type()
)
capwapBaseAcMaxRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcMaxRetransmit.setStatus("current")


class _CapwapBaseAcChangeStatePendingTimer_Type(Unsigned32):
    """Custom type capwapBaseAcChangeStatePendingTimer based on Unsigned32"""
    defaultValue = 25


_CapwapBaseAcChangeStatePendingTimer_Type.__name__ = "Unsigned32"
_CapwapBaseAcChangeStatePendingTimer_Object = MibScalar
capwapBaseAcChangeStatePendingTimer = _CapwapBaseAcChangeStatePendingTimer_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 3, 2),
    _CapwapBaseAcChangeStatePendingTimer_Type()
)
capwapBaseAcChangeStatePendingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcChangeStatePendingTimer.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcChangeStatePendingTimer.setUnits("second")


class _CapwapBaseAcDataCheckTimer_Type(Unsigned32):
    """Custom type capwapBaseAcDataCheckTimer based on Unsigned32"""
    defaultValue = 30


_CapwapBaseAcDataCheckTimer_Type.__name__ = "Unsigned32"
_CapwapBaseAcDataCheckTimer_Object = MibScalar
capwapBaseAcDataCheckTimer = _CapwapBaseAcDataCheckTimer_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 3, 3),
    _CapwapBaseAcDataCheckTimer_Type()
)
capwapBaseAcDataCheckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcDataCheckTimer.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcDataCheckTimer.setUnits("second")


class _CapwapBaseAcDTLSSessionDeleteTimer_Type(Unsigned32):
    """Custom type capwapBaseAcDTLSSessionDeleteTimer based on Unsigned32"""
    defaultValue = 5


_CapwapBaseAcDTLSSessionDeleteTimer_Type.__name__ = "Unsigned32"
_CapwapBaseAcDTLSSessionDeleteTimer_Object = MibScalar
capwapBaseAcDTLSSessionDeleteTimer = _CapwapBaseAcDTLSSessionDeleteTimer_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 3, 4),
    _CapwapBaseAcDTLSSessionDeleteTimer_Type()
)
capwapBaseAcDTLSSessionDeleteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcDTLSSessionDeleteTimer.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcDTLSSessionDeleteTimer.setUnits("second")


class _CapwapBaseAcEchoInterval_Type(Unsigned32):
    """Custom type capwapBaseAcEchoInterval based on Unsigned32"""
    defaultValue = 30


_CapwapBaseAcEchoInterval_Type.__name__ = "Unsigned32"
_CapwapBaseAcEchoInterval_Object = MibScalar
capwapBaseAcEchoInterval = _CapwapBaseAcEchoInterval_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 3, 5),
    _CapwapBaseAcEchoInterval_Type()
)
capwapBaseAcEchoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcEchoInterval.setUnits("second")


class _CapwapBaseAcRetransmitInterval_Type(Unsigned32):
    """Custom type capwapBaseAcRetransmitInterval based on Unsigned32"""
    defaultValue = 3


_CapwapBaseAcRetransmitInterval_Type.__name__ = "Unsigned32"
_CapwapBaseAcRetransmitInterval_Object = MibScalar
capwapBaseAcRetransmitInterval = _CapwapBaseAcRetransmitInterval_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 3, 6),
    _CapwapBaseAcRetransmitInterval_Type()
)
capwapBaseAcRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcRetransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcRetransmitInterval.setUnits("second")


class _CapwapBaseAcSilentInterval_Type(Unsigned32):
    """Custom type capwapBaseAcSilentInterval based on Unsigned32"""
    defaultValue = 30


_CapwapBaseAcSilentInterval_Type.__name__ = "Unsigned32"
_CapwapBaseAcSilentInterval_Object = MibScalar
capwapBaseAcSilentInterval = _CapwapBaseAcSilentInterval_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 3, 7),
    _CapwapBaseAcSilentInterval_Type()
)
capwapBaseAcSilentInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcSilentInterval.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcSilentInterval.setUnits("second")


class _CapwapBaseAcWaitDTLSTimer_Type(Unsigned32):
    """Custom type capwapBaseAcWaitDTLSTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 4294967295),
    )


_CapwapBaseAcWaitDTLSTimer_Type.__name__ = "Unsigned32"
_CapwapBaseAcWaitDTLSTimer_Object = MibScalar
capwapBaseAcWaitDTLSTimer = _CapwapBaseAcWaitDTLSTimer_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 3, 8),
    _CapwapBaseAcWaitDTLSTimer_Type()
)
capwapBaseAcWaitDTLSTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcWaitDTLSTimer.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcWaitDTLSTimer.setUnits("second")


class _CapwapBaseAcWaitJoinTimer_Type(Unsigned32):
    """Custom type capwapBaseAcWaitJoinTimer based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 4294967295),
    )


_CapwapBaseAcWaitJoinTimer_Type.__name__ = "Unsigned32"
_CapwapBaseAcWaitJoinTimer_Object = MibScalar
capwapBaseAcWaitJoinTimer = _CapwapBaseAcWaitJoinTimer_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 3, 9),
    _CapwapBaseAcWaitJoinTimer_Type()
)
capwapBaseAcWaitJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcWaitJoinTimer.setStatus("current")
if mibBuilder.loadTexts:
    capwapBaseAcWaitJoinTimer.setUnits("second")


class _CapwapBaseAcEcnSupport_Type(Integer32):
    """Custom type capwapBaseAcEcnSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("limited", 0),
          ("fullAndLimited", 1))
    )


_CapwapBaseAcEcnSupport_Type.__name__ = "Integer32"
_CapwapBaseAcEcnSupport_Object = MibScalar
capwapBaseAcEcnSupport = _CapwapBaseAcEcnSupport_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 3, 10),
    _CapwapBaseAcEcnSupport_Type()
)
capwapBaseAcEcnSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAcEcnSupport.setStatus("current")
_CapwapBaseStats_ObjectIdentity = ObjectIdentity
capwapBaseStats = _CapwapBaseStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 1, 4)
)
_CapwapBaseFailedDTLSAuthFailureCount_Type = Counter32
_CapwapBaseFailedDTLSAuthFailureCount_Object = MibScalar
capwapBaseFailedDTLSAuthFailureCount = _CapwapBaseFailedDTLSAuthFailureCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 4, 1),
    _CapwapBaseFailedDTLSAuthFailureCount_Type()
)
capwapBaseFailedDTLSAuthFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseFailedDTLSAuthFailureCount.setStatus("current")
_CapwapBaseFailedDTLSSessionCount_Type = Counter32
_CapwapBaseFailedDTLSSessionCount_Object = MibScalar
capwapBaseFailedDTLSSessionCount = _CapwapBaseFailedDTLSSessionCount_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 4, 2),
    _CapwapBaseFailedDTLSSessionCount_Type()
)
capwapBaseFailedDTLSSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capwapBaseFailedDTLSSessionCount.setStatus("current")
_CapwapBaseNotifyVarObjects_ObjectIdentity = ObjectIdentity
capwapBaseNotifyVarObjects = _CapwapBaseNotifyVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 1, 5)
)
_CapwapBaseNtfWtpId_Type = CapwapBaseWtpIdTC
_CapwapBaseNtfWtpId_Object = MibScalar
capwapBaseNtfWtpId = _CapwapBaseNtfWtpId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 1),
    _CapwapBaseNtfWtpId_Type()
)
capwapBaseNtfWtpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfWtpId.setStatus("current")
_CapwapBaseNtfRadioId_Type = CapwapBaseRadioIdTC
_CapwapBaseNtfRadioId_Object = MibScalar
capwapBaseNtfRadioId = _CapwapBaseNtfRadioId_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 2),
    _CapwapBaseNtfRadioId_Type()
)
capwapBaseNtfRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfRadioId.setStatus("current")
_CapwapBaseNtfChannelType_Type = CapwapBaseChannelTypeTC
_CapwapBaseNtfChannelType_Object = MibScalar
capwapBaseNtfChannelType = _CapwapBaseNtfChannelType_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 3),
    _CapwapBaseNtfChannelType_Type()
)
capwapBaseNtfChannelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfChannelType.setStatus("current")
_CapwapBaseNtfAuthenMethod_Type = CapwapBaseAuthenMethodTC
_CapwapBaseNtfAuthenMethod_Object = MibScalar
capwapBaseNtfAuthenMethod = _CapwapBaseNtfAuthenMethod_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 4),
    _CapwapBaseNtfAuthenMethod_Type()
)
capwapBaseNtfAuthenMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfAuthenMethod.setStatus("current")


class _CapwapBaseNtfChannelDownReason_Type(Integer32):
    """Custom type capwapBaseNtfChannelDownReason based on Integer32"""
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
        *(("timeout", 1),
          ("rekeyFailure", 2),
          ("acRebootWtp", 3),
          ("dtlsError", 4),
          ("maxRetransmit", 5))
    )


_CapwapBaseNtfChannelDownReason_Type.__name__ = "Integer32"
_CapwapBaseNtfChannelDownReason_Object = MibScalar
capwapBaseNtfChannelDownReason = _CapwapBaseNtfChannelDownReason_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 5),
    _CapwapBaseNtfChannelDownReason_Type()
)
capwapBaseNtfChannelDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfChannelDownReason.setStatus("current")


class _CapwapBaseNtfStationIdList_Type(LongUtf8String):
    """Custom type capwapBaseNtfStationIdList based on LongUtf8String"""
    subtypeSpec = LongUtf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 1024),
    )


_CapwapBaseNtfStationIdList_Type.__name__ = "LongUtf8String"
_CapwapBaseNtfStationIdList_Object = MibScalar
capwapBaseNtfStationIdList = _CapwapBaseNtfStationIdList_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 6),
    _CapwapBaseNtfStationIdList_Type()
)
capwapBaseNtfStationIdList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfStationIdList.setStatus("current")


class _CapwapBaseNtfAuthenFailureReason_Type(Integer32):
    """Custom type capwapBaseNtfAuthenFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("keyMismatch", 1),
          ("invalidCert", 2),
          ("reassemblyFailure", 3),
          ("decapFailure", 4),
          ("encapFailure", 5),
          ("timeout", 6),
          ("unknown", 8))
    )


_CapwapBaseNtfAuthenFailureReason_Type.__name__ = "Integer32"
_CapwapBaseNtfAuthenFailureReason_Object = MibScalar
capwapBaseNtfAuthenFailureReason = _CapwapBaseNtfAuthenFailureReason_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 7),
    _CapwapBaseNtfAuthenFailureReason_Type()
)
capwapBaseNtfAuthenFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfAuthenFailureReason.setStatus("current")


class _CapwapBaseNtfRadioOperStatusFlag_Type(Integer32):
    """Custom type capwapBaseNtfRadioOperStatusFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("operable", 0),
          ("inoperable", 1))
    )


_CapwapBaseNtfRadioOperStatusFlag_Type.__name__ = "Integer32"
_CapwapBaseNtfRadioOperStatusFlag_Object = MibScalar
capwapBaseNtfRadioOperStatusFlag = _CapwapBaseNtfRadioOperStatusFlag_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 8),
    _CapwapBaseNtfRadioOperStatusFlag_Type()
)
capwapBaseNtfRadioOperStatusFlag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfRadioOperStatusFlag.setStatus("current")


class _CapwapBaseNtfRadioStatusCause_Type(Integer32):
    """Custom type capwapBaseNtfRadioStatusCause based on Integer32"""
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
        *(("normal", 0),
          ("hwError", 1),
          ("swError", 2),
          ("adminSet", 3))
    )


_CapwapBaseNtfRadioStatusCause_Type.__name__ = "Integer32"
_CapwapBaseNtfRadioStatusCause_Object = MibScalar
capwapBaseNtfRadioStatusCause = _CapwapBaseNtfRadioStatusCause_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 9),
    _CapwapBaseNtfRadioStatusCause_Type()
)
capwapBaseNtfRadioStatusCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfRadioStatusCause.setStatus("current")


class _CapwapBaseNtfJoinFailureReason_Type(Integer32):
    """Custom type capwapBaseNtfJoinFailureReason based on Integer32"""
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
        *(("unspecified", 1),
          ("resDepletion", 2),
          ("unknownSource", 3),
          ("incorrectData", 4),
          ("sessionIdInUse", 5),
          ("unsupportedHw", 6),
          ("unsupportedBinding", 7))
    )


_CapwapBaseNtfJoinFailureReason_Type.__name__ = "Integer32"
_CapwapBaseNtfJoinFailureReason_Object = MibScalar
capwapBaseNtfJoinFailureReason = _CapwapBaseNtfJoinFailureReason_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 10),
    _CapwapBaseNtfJoinFailureReason_Type()
)
capwapBaseNtfJoinFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfJoinFailureReason.setStatus("current")


class _CapwapBaseNtfImageFailureReason_Type(Integer32):
    """Custom type capwapBaseNtfImageFailureReason based on Integer32"""
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
        *(("invalidChecksum", 1),
          ("invalidLength", 2),
          ("other", 3),
          ("inStorage", 4))
    )


_CapwapBaseNtfImageFailureReason_Type.__name__ = "Integer32"
_CapwapBaseNtfImageFailureReason_Object = MibScalar
capwapBaseNtfImageFailureReason = _CapwapBaseNtfImageFailureReason_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 11),
    _CapwapBaseNtfImageFailureReason_Type()
)
capwapBaseNtfImageFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfImageFailureReason.setStatus("current")


class _CapwapBaseNtfConfigMsgErrorType_Type(Integer32):
    """Custom type capwapBaseNtfConfigMsgErrorType based on Integer32"""
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
        *(("unknownElement", 1),
          ("unsupportedElement", 2),
          ("unknownValue", 3),
          ("unsupportedValue", 4))
    )


_CapwapBaseNtfConfigMsgErrorType_Type.__name__ = "Integer32"
_CapwapBaseNtfConfigMsgErrorType_Object = MibScalar
capwapBaseNtfConfigMsgErrorType = _CapwapBaseNtfConfigMsgErrorType_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 12),
    _CapwapBaseNtfConfigMsgErrorType_Type()
)
capwapBaseNtfConfigMsgErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfConfigMsgErrorType.setStatus("current")
_CapwapBaseNtfMsgErrorElements_Type = SnmpAdminString
_CapwapBaseNtfMsgErrorElements_Object = MibScalar
capwapBaseNtfMsgErrorElements = _CapwapBaseNtfMsgErrorElements_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 5, 13),
    _CapwapBaseNtfMsgErrorElements_Type()
)
capwapBaseNtfMsgErrorElements.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    capwapBaseNtfMsgErrorElements.setStatus("current")
_CapwapBaseNotifyControlObjects_ObjectIdentity = ObjectIdentity
capwapBaseNotifyControlObjects = _CapwapBaseNotifyControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 1, 6)
)


class _CapwapBaseChannelUpDownNotifyEnable_Type(TruthValue):
    """Custom type capwapBaseChannelUpDownNotifyEnable based on TruthValue"""
    defaultValue = 2


_CapwapBaseChannelUpDownNotifyEnable_Type.__name__ = "TruthValue"
_CapwapBaseChannelUpDownNotifyEnable_Object = MibScalar
capwapBaseChannelUpDownNotifyEnable = _CapwapBaseChannelUpDownNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 6, 1),
    _CapwapBaseChannelUpDownNotifyEnable_Type()
)
capwapBaseChannelUpDownNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseChannelUpDownNotifyEnable.setStatus("current")


class _CapwapBaseDecryptErrorNotifyEnable_Type(TruthValue):
    """Custom type capwapBaseDecryptErrorNotifyEnable based on TruthValue"""
    defaultValue = 1


_CapwapBaseDecryptErrorNotifyEnable_Type.__name__ = "TruthValue"
_CapwapBaseDecryptErrorNotifyEnable_Object = MibScalar
capwapBaseDecryptErrorNotifyEnable = _CapwapBaseDecryptErrorNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 6, 2),
    _CapwapBaseDecryptErrorNotifyEnable_Type()
)
capwapBaseDecryptErrorNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseDecryptErrorNotifyEnable.setStatus("current")


class _CapwapBaseJoinFailureNotifyEnable_Type(TruthValue):
    """Custom type capwapBaseJoinFailureNotifyEnable based on TruthValue"""
    defaultValue = 1


_CapwapBaseJoinFailureNotifyEnable_Type.__name__ = "TruthValue"
_CapwapBaseJoinFailureNotifyEnable_Object = MibScalar
capwapBaseJoinFailureNotifyEnable = _CapwapBaseJoinFailureNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 6, 3),
    _CapwapBaseJoinFailureNotifyEnable_Type()
)
capwapBaseJoinFailureNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseJoinFailureNotifyEnable.setStatus("current")


class _CapwapBaseImageUpgradeFailureNotifyEnable_Type(TruthValue):
    """Custom type capwapBaseImageUpgradeFailureNotifyEnable based on TruthValue"""
    defaultValue = 1


_CapwapBaseImageUpgradeFailureNotifyEnable_Type.__name__ = "TruthValue"
_CapwapBaseImageUpgradeFailureNotifyEnable_Object = MibScalar
capwapBaseImageUpgradeFailureNotifyEnable = _CapwapBaseImageUpgradeFailureNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 6, 4),
    _CapwapBaseImageUpgradeFailureNotifyEnable_Type()
)
capwapBaseImageUpgradeFailureNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseImageUpgradeFailureNotifyEnable.setStatus("current")


class _CapwapBaseConfigMsgErrorNotifyEnable_Type(TruthValue):
    """Custom type capwapBaseConfigMsgErrorNotifyEnable based on TruthValue"""
    defaultValue = 2


_CapwapBaseConfigMsgErrorNotifyEnable_Type.__name__ = "TruthValue"
_CapwapBaseConfigMsgErrorNotifyEnable_Object = MibScalar
capwapBaseConfigMsgErrorNotifyEnable = _CapwapBaseConfigMsgErrorNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 6, 5),
    _CapwapBaseConfigMsgErrorNotifyEnable_Type()
)
capwapBaseConfigMsgErrorNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseConfigMsgErrorNotifyEnable.setStatus("current")


class _CapwapBaseRadioOperableStatusNotifyEnable_Type(TruthValue):
    """Custom type capwapBaseRadioOperableStatusNotifyEnable based on TruthValue"""
    defaultValue = 2


_CapwapBaseRadioOperableStatusNotifyEnable_Type.__name__ = "TruthValue"
_CapwapBaseRadioOperableStatusNotifyEnable_Object = MibScalar
capwapBaseRadioOperableStatusNotifyEnable = _CapwapBaseRadioOperableStatusNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 6, 6),
    _CapwapBaseRadioOperableStatusNotifyEnable_Type()
)
capwapBaseRadioOperableStatusNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseRadioOperableStatusNotifyEnable.setStatus("current")


class _CapwapBaseAuthenFailureNotifyEnable_Type(TruthValue):
    """Custom type capwapBaseAuthenFailureNotifyEnable based on TruthValue"""
    defaultValue = 1


_CapwapBaseAuthenFailureNotifyEnable_Type.__name__ = "TruthValue"
_CapwapBaseAuthenFailureNotifyEnable_Object = MibScalar
capwapBaseAuthenFailureNotifyEnable = _CapwapBaseAuthenFailureNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 196, 1, 6, 7),
    _CapwapBaseAuthenFailureNotifyEnable_Type()
)
capwapBaseAuthenFailureNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capwapBaseAuthenFailureNotifyEnable.setStatus("current")
_CapwapBaseConformance_ObjectIdentity = ObjectIdentity
capwapBaseConformance = _CapwapBaseConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 2)
)
_CapwapBaseCompliances_ObjectIdentity = ObjectIdentity
capwapBaseCompliances = _CapwapBaseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 2, 1)
)
_CapwapBaseGroups_ObjectIdentity = ObjectIdentity
capwapBaseGroups = _CapwapBaseGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 196, 2, 2)
)

# Managed Objects groups

capwapBaseAcNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 1)
)
capwapBaseAcNodeGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseWtpSessions"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpSessionsLimit"),
        ("CAPWAP-BASE-MIB", "capwapBaseStationSessions"),
        ("CAPWAP-BASE-MIB", "capwapBaseStationSessionsLimit"))
)
if mibBuilder.loadTexts:
    capwapBaseAcNodeGroup.setStatus("current")

capwapBaseAcNodeGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 2)
)
capwapBaseAcNodeGroup2.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseDataChannelDTLSPolicyOptions"),
        ("CAPWAP-BASE-MIB", "capwapBaseControlChannelAuthenOptions"))
)
if mibBuilder.loadTexts:
    capwapBaseAcNodeGroup2.setStatus("current")

capwapBaseAcNameListGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 3)
)
capwapBaseAcNameListGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseAcNameListName"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcNameListPriority"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcNameListRowStatus"))
)
if mibBuilder.loadTexts:
    capwapBaseAcNameListGroup.setStatus("current")

capwapBaseMacAclsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 4)
)
capwapBaseMacAclsGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseMacAclStationId"),
        ("CAPWAP-BASE-MIB", "capwapBaseMacAclRowStatus"))
)
if mibBuilder.loadTexts:
    capwapBaseMacAclsGroup.setStatus("current")

capwapBaseWtpProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 5)
)
capwapBaseWtpProfileGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseWtpProfileName"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpMacAddress"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpModelNumber"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpName"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpLocation"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileRowStatus"))
)
if mibBuilder.loadTexts:
    capwapBaseWtpProfileGroup.setStatus("current")

capwapBaseWtpProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 6)
)
capwapBaseWtpProfileGroup2.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpStaticIpEnable"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpStaticIpType"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpStaticIpAddress"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpNetmask"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpGateway"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpFallbackEnable"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpEchoInterval"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpIdleTimeout"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpMaxDiscoveryInterval"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpReportInterval"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpStatisticsTimer"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileWtpEcnSupport"))
)
if mibBuilder.loadTexts:
    capwapBaseWtpProfileGroup2.setStatus("current")

capwapBaseWtpStateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 7)
)
capwapBaseWtpStateGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseWtpStateWtpIpAddressType"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpStateWtpIpAddress"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpStateWtpLocalIpAddressType"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpStateWtpLocalIpAddress"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpStateWtpBaseMacAddress"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpState"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpStateWtpUpTime"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpStateWtpCurrWtpProfileId"))
)
if mibBuilder.loadTexts:
    capwapBaseWtpStateGroup.setStatus("current")

capwapBaseWtpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 8)
)
capwapBaseWtpGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseWtpBaseMacAddress"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpTunnelModeOptions"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpMacTypeOptions"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpDiscoveryType"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpRadiosInUseNum"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpRadioNumLimit"))
)
if mibBuilder.loadTexts:
    capwapBaseWtpGroup.setStatus("current")

capwapBaseWtpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 9)
)
capwapBaseWtpGroup2.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseWtpPhyIndex"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpRetransmitCount"))
)
if mibBuilder.loadTexts:
    capwapBaseWtpGroup2.setStatus("current")

capwapBaseRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 10)
)
capwapBaseRadioGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseWirelessBindingVirtualRadioIfIndex"),
        ("CAPWAP-BASE-MIB", "capwapBaseWirelessBindingType"))
)
if mibBuilder.loadTexts:
    capwapBaseRadioGroup.setStatus("current")

capwapBaseStationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 11)
)
capwapBaseStationGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseStationWtpId"),
        ("CAPWAP-BASE-MIB", "capwapBaseStationWtpRadioId"),
        ("CAPWAP-BASE-MIB", "capwapBaseStationAddedTime"),
        ("CAPWAP-BASE-MIB", "capwapBaseStationVlanName"))
)
if mibBuilder.loadTexts:
    capwapBaseStationGroup.setStatus("current")

capwapBaseWtpEventsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 12)
)
capwapBaseWtpEventsStatsGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseWtpEventsStatsRebootCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpEventsStatsInitCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpEventsStatsLinkFailureCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpEventsStatsSwFailureCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpEventsStatsHwFailureCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpEventsStatsOtherFailureCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpEventsStatsUnknownFailureCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpEventsStatsLastFailureType"))
)
if mibBuilder.loadTexts:
    capwapBaseWtpEventsStatsGroup.setStatus("current")

capwapBaseRadioEventsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 13)
)
capwapBaseRadioEventsStatsGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsResetCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsSwFailureCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsHwFailureCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsOtherFailureCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsUnknownFailureCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsConfigUpdateCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsChannelChangeCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsBandChangeCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsCurrNoiseFloor"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsDecryptErrorCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsLastFailureType"))
)
if mibBuilder.loadTexts:
    capwapBaseRadioEventsStatsGroup.setStatus("current")

capwapBaseParametersGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 14)
)
capwapBaseParametersGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseAcMaxRetransmit"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcChangeStatePendingTimer"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcDataCheckTimer"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcDTLSSessionDeleteTimer"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcEchoInterval"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcRetransmitInterval"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcSilentInterval"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcWaitDTLSTimer"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcWaitJoinTimer"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcEcnSupport"))
)
if mibBuilder.loadTexts:
    capwapBaseParametersGroup.setStatus("current")

capwapBaseStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 15)
)
capwapBaseStatsGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseFailedDTLSAuthFailureCount"),
        ("CAPWAP-BASE-MIB", "capwapBaseFailedDTLSSessionCount"))
)
if mibBuilder.loadTexts:
    capwapBaseStatsGroup.setStatus("current")

capwapBaseNotifyVarsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 17)
)
capwapBaseNotifyVarsGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseNtfWtpId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfRadioId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelType"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfAuthenMethod"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelDownReason"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfStationIdList"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfAuthenFailureReason"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfRadioOperStatusFlag"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfRadioStatusCause"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfJoinFailureReason"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfImageFailureReason"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfConfigMsgErrorType"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfMsgErrorElements"))
)
if mibBuilder.loadTexts:
    capwapBaseNotifyVarsGroup.setStatus("current")

capwapBaseNotifyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 18)
)
capwapBaseNotifyControlGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseChannelUpDownNotifyEnable"),
        ("CAPWAP-BASE-MIB", "capwapBaseDecryptErrorNotifyEnable"),
        ("CAPWAP-BASE-MIB", "capwapBaseJoinFailureNotifyEnable"),
        ("CAPWAP-BASE-MIB", "capwapBaseImageUpgradeFailureNotifyEnable"),
        ("CAPWAP-BASE-MIB", "capwapBaseConfigMsgErrorNotifyEnable"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioOperableStatusNotifyEnable"),
        ("CAPWAP-BASE-MIB", "capwapBaseAuthenFailureNotifyEnable"))
)
if mibBuilder.loadTexts:
    capwapBaseNotifyControlGroup.setStatus("current")


# Notification objects

capwapBaseChannelUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 196, 0, 1)
)
capwapBaseChannelUp.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseNtfWtpId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelType"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfAuthenMethod"))
)
if mibBuilder.loadTexts:
    capwapBaseChannelUp.setStatus(
        "current"
    )

capwapBaseChannelDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 196, 0, 2)
)
capwapBaseChannelDown.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseNtfWtpId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelType"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelDownReason"))
)
if mibBuilder.loadTexts:
    capwapBaseChannelDown.setStatus(
        "current"
    )

capwapBaseDecryptErrorReport = NotificationType(
    (1, 3, 6, 1, 2, 1, 196, 0, 3)
)
capwapBaseDecryptErrorReport.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseNtfWtpId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfRadioId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfStationIdList"))
)
if mibBuilder.loadTexts:
    capwapBaseDecryptErrorReport.setStatus(
        "current"
    )

capwapBaseJoinFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 196, 0, 4)
)
capwapBaseJoinFailure.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseNtfWtpId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfJoinFailureReason"))
)
if mibBuilder.loadTexts:
    capwapBaseJoinFailure.setStatus(
        "current"
    )

capwapBaseImageUpgradeFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 196, 0, 5)
)
capwapBaseImageUpgradeFailure.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseNtfWtpId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfImageFailureReason"))
)
if mibBuilder.loadTexts:
    capwapBaseImageUpgradeFailure.setStatus(
        "current"
    )

capwapBaseConfigMsgError = NotificationType(
    (1, 3, 6, 1, 2, 1, 196, 0, 6)
)
capwapBaseConfigMsgError.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseNtfWtpId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfConfigMsgErrorType"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfMsgErrorElements"))
)
if mibBuilder.loadTexts:
    capwapBaseConfigMsgError.setStatus(
        "current"
    )

capwapBaseRadioOperableStatus = NotificationType(
    (1, 3, 6, 1, 2, 1, 196, 0, 7)
)
capwapBaseRadioOperableStatus.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseNtfWtpId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfRadioId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfRadioOperStatusFlag"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfRadioStatusCause"))
)
if mibBuilder.loadTexts:
    capwapBaseRadioOperableStatus.setStatus(
        "current"
    )

capwapBaseAuthenFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 196, 0, 8)
)
capwapBaseAuthenFailure.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseNtfWtpId"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelType"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfAuthenMethod"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfAuthenFailureReason"))
)
if mibBuilder.loadTexts:
    capwapBaseAuthenFailure.setStatus(
        "current"
    )


# Notifications groups

capwapBaseNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 196, 2, 2, 16)
)
capwapBaseNotificationsGroup.setObjects(
      *(("CAPWAP-BASE-MIB", "capwapBaseChannelUp"),
        ("CAPWAP-BASE-MIB", "capwapBaseChannelDown"),
        ("CAPWAP-BASE-MIB", "capwapBaseDecryptErrorReport"),
        ("CAPWAP-BASE-MIB", "capwapBaseJoinFailure"),
        ("CAPWAP-BASE-MIB", "capwapBaseImageUpgradeFailure"),
        ("CAPWAP-BASE-MIB", "capwapBaseConfigMsgError"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioOperableStatus"),
        ("CAPWAP-BASE-MIB", "capwapBaseAuthenFailure"))
)
if mibBuilder.loadTexts:
    capwapBaseNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

capwapBaseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 196, 2, 1, 1)
)
capwapBaseCompliance.setObjects(
      *(("IF-MIB", "ifGeneralInformationGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcNodeGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpStateGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseStationGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcNodeGroup2"),
        ("CAPWAP-BASE-MIB", "capwapBaseAcNameListGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseMacAclsGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpProfileGroup2"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpGroup2"),
        ("CAPWAP-BASE-MIB", "capwapBaseWtpEventsStatsGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseRadioEventsStatsGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseParametersGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseStatsGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseNotificationsGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseNotifyVarsGroup"),
        ("CAPWAP-BASE-MIB", "capwapBaseNotifyControlGroup"))
)
if mibBuilder.loadTexts:
    capwapBaseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAPWAP-BASE-MIB",
    **{"CapwapBaseWtpProfileIdTC": CapwapBaseWtpProfileIdTC,
       "CapwapBaseWtpIdTC": CapwapBaseWtpIdTC,
       "CapwapBaseStationIdTC": CapwapBaseStationIdTC,
       "CapwapBaseRadioIdTC": CapwapBaseRadioIdTC,
       "CapwapBaseTunnelModeTC": CapwapBaseTunnelModeTC,
       "CapwapBaseMacTypeTC": CapwapBaseMacTypeTC,
       "CapwapBaseChannelTypeTC": CapwapBaseChannelTypeTC,
       "CapwapBaseAuthenMethodTC": CapwapBaseAuthenMethodTC,
       "capwapBaseMIB": capwapBaseMIB,
       "capwapBaseNotifications": capwapBaseNotifications,
       "capwapBaseChannelUp": capwapBaseChannelUp,
       "capwapBaseChannelDown": capwapBaseChannelDown,
       "capwapBaseDecryptErrorReport": capwapBaseDecryptErrorReport,
       "capwapBaseJoinFailure": capwapBaseJoinFailure,
       "capwapBaseImageUpgradeFailure": capwapBaseImageUpgradeFailure,
       "capwapBaseConfigMsgError": capwapBaseConfigMsgError,
       "capwapBaseRadioOperableStatus": capwapBaseRadioOperableStatus,
       "capwapBaseAuthenFailure": capwapBaseAuthenFailure,
       "capwapBaseObjects": capwapBaseObjects,
       "capwapBaseAc": capwapBaseAc,
       "capwapBaseWtpSessions": capwapBaseWtpSessions,
       "capwapBaseWtpSessionsLimit": capwapBaseWtpSessionsLimit,
       "capwapBaseStationSessions": capwapBaseStationSessions,
       "capwapBaseStationSessionsLimit": capwapBaseStationSessionsLimit,
       "capwapBaseDataChannelDTLSPolicyOptions": capwapBaseDataChannelDTLSPolicyOptions,
       "capwapBaseControlChannelAuthenOptions": capwapBaseControlChannelAuthenOptions,
       "capwapBaseAcNameListTable": capwapBaseAcNameListTable,
       "capwapBaseAcNameListEntry": capwapBaseAcNameListEntry,
       "capwapBaseAcNameListId": capwapBaseAcNameListId,
       "capwapBaseAcNameListName": capwapBaseAcNameListName,
       "capwapBaseAcNameListPriority": capwapBaseAcNameListPriority,
       "capwapBaseAcNameListRowStatus": capwapBaseAcNameListRowStatus,
       "capwapBaseMacAclTable": capwapBaseMacAclTable,
       "capwapBaseMacAclEntry": capwapBaseMacAclEntry,
       "capwapBaseMacAclId": capwapBaseMacAclId,
       "capwapBaseMacAclStationId": capwapBaseMacAclStationId,
       "capwapBaseMacAclRowStatus": capwapBaseMacAclRowStatus,
       "capwapBaseWtps": capwapBaseWtps,
       "capwapBaseWtpProfileTable": capwapBaseWtpProfileTable,
       "capwapBaseWtpProfileEntry": capwapBaseWtpProfileEntry,
       "capwapBaseWtpProfileId": capwapBaseWtpProfileId,
       "capwapBaseWtpProfileName": capwapBaseWtpProfileName,
       "capwapBaseWtpProfileWtpMacAddress": capwapBaseWtpProfileWtpMacAddress,
       "capwapBaseWtpProfileWtpModelNumber": capwapBaseWtpProfileWtpModelNumber,
       "capwapBaseWtpProfileWtpName": capwapBaseWtpProfileWtpName,
       "capwapBaseWtpProfileWtpLocation": capwapBaseWtpProfileWtpLocation,
       "capwapBaseWtpProfileWtpStaticIpEnable": capwapBaseWtpProfileWtpStaticIpEnable,
       "capwapBaseWtpProfileWtpStaticIpType": capwapBaseWtpProfileWtpStaticIpType,
       "capwapBaseWtpProfileWtpStaticIpAddress": capwapBaseWtpProfileWtpStaticIpAddress,
       "capwapBaseWtpProfileWtpNetmask": capwapBaseWtpProfileWtpNetmask,
       "capwapBaseWtpProfileWtpGateway": capwapBaseWtpProfileWtpGateway,
       "capwapBaseWtpProfileWtpFallbackEnable": capwapBaseWtpProfileWtpFallbackEnable,
       "capwapBaseWtpProfileWtpEchoInterval": capwapBaseWtpProfileWtpEchoInterval,
       "capwapBaseWtpProfileWtpIdleTimeout": capwapBaseWtpProfileWtpIdleTimeout,
       "capwapBaseWtpProfileWtpMaxDiscoveryInterval": capwapBaseWtpProfileWtpMaxDiscoveryInterval,
       "capwapBaseWtpProfileWtpReportInterval": capwapBaseWtpProfileWtpReportInterval,
       "capwapBaseWtpProfileWtpStatisticsTimer": capwapBaseWtpProfileWtpStatisticsTimer,
       "capwapBaseWtpProfileWtpEcnSupport": capwapBaseWtpProfileWtpEcnSupport,
       "capwapBaseWtpProfileRowStatus": capwapBaseWtpProfileRowStatus,
       "capwapBaseWtpStateTable": capwapBaseWtpStateTable,
       "capwapBaseWtpStateEntry": capwapBaseWtpStateEntry,
       "capwapBaseWtpStateWtpId": capwapBaseWtpStateWtpId,
       "capwapBaseWtpStateWtpIpAddressType": capwapBaseWtpStateWtpIpAddressType,
       "capwapBaseWtpStateWtpIpAddress": capwapBaseWtpStateWtpIpAddress,
       "capwapBaseWtpStateWtpLocalIpAddressType": capwapBaseWtpStateWtpLocalIpAddressType,
       "capwapBaseWtpStateWtpLocalIpAddress": capwapBaseWtpStateWtpLocalIpAddress,
       "capwapBaseWtpStateWtpBaseMacAddress": capwapBaseWtpStateWtpBaseMacAddress,
       "capwapBaseWtpState": capwapBaseWtpState,
       "capwapBaseWtpStateWtpUpTime": capwapBaseWtpStateWtpUpTime,
       "capwapBaseWtpStateWtpCurrWtpProfileId": capwapBaseWtpStateWtpCurrWtpProfileId,
       "capwapBaseWtpTable": capwapBaseWtpTable,
       "capwapBaseWtpEntry": capwapBaseWtpEntry,
       "capwapBaseWtpCurrId": capwapBaseWtpCurrId,
       "capwapBaseWtpPhyIndex": capwapBaseWtpPhyIndex,
       "capwapBaseWtpBaseMacAddress": capwapBaseWtpBaseMacAddress,
       "capwapBaseWtpTunnelModeOptions": capwapBaseWtpTunnelModeOptions,
       "capwapBaseWtpMacTypeOptions": capwapBaseWtpMacTypeOptions,
       "capwapBaseWtpDiscoveryType": capwapBaseWtpDiscoveryType,
       "capwapBaseWtpRadiosInUseNum": capwapBaseWtpRadiosInUseNum,
       "capwapBaseWtpRadioNumLimit": capwapBaseWtpRadioNumLimit,
       "capwapBaseWtpRetransmitCount": capwapBaseWtpRetransmitCount,
       "capwapBaseWirelessBindingTable": capwapBaseWirelessBindingTable,
       "capwapBaseWirelessBindingEntry": capwapBaseWirelessBindingEntry,
       "capwapBaseWirelessBindingRadioId": capwapBaseWirelessBindingRadioId,
       "capwapBaseWirelessBindingVirtualRadioIfIndex": capwapBaseWirelessBindingVirtualRadioIfIndex,
       "capwapBaseWirelessBindingType": capwapBaseWirelessBindingType,
       "capwapBaseStationTable": capwapBaseStationTable,
       "capwapBaseStationEntry": capwapBaseStationEntry,
       "capwapBaseStationId": capwapBaseStationId,
       "capwapBaseStationWtpId": capwapBaseStationWtpId,
       "capwapBaseStationWtpRadioId": capwapBaseStationWtpRadioId,
       "capwapBaseStationAddedTime": capwapBaseStationAddedTime,
       "capwapBaseStationVlanName": capwapBaseStationVlanName,
       "capwapBaseWtpEventsStatsTable": capwapBaseWtpEventsStatsTable,
       "capwapBaseWtpEventsStatsEntry": capwapBaseWtpEventsStatsEntry,
       "capwapBaseWtpEventsStatsRebootCount": capwapBaseWtpEventsStatsRebootCount,
       "capwapBaseWtpEventsStatsInitCount": capwapBaseWtpEventsStatsInitCount,
       "capwapBaseWtpEventsStatsLinkFailureCount": capwapBaseWtpEventsStatsLinkFailureCount,
       "capwapBaseWtpEventsStatsSwFailureCount": capwapBaseWtpEventsStatsSwFailureCount,
       "capwapBaseWtpEventsStatsHwFailureCount": capwapBaseWtpEventsStatsHwFailureCount,
       "capwapBaseWtpEventsStatsOtherFailureCount": capwapBaseWtpEventsStatsOtherFailureCount,
       "capwapBaseWtpEventsStatsUnknownFailureCount": capwapBaseWtpEventsStatsUnknownFailureCount,
       "capwapBaseWtpEventsStatsLastFailureType": capwapBaseWtpEventsStatsLastFailureType,
       "capwapBaseRadioEventsStatsTable": capwapBaseRadioEventsStatsTable,
       "capwapBaseRadioEventsStatsEntry": capwapBaseRadioEventsStatsEntry,
       "capwapBaseRadioEventsWtpRadioId": capwapBaseRadioEventsWtpRadioId,
       "capwapBaseRadioEventsStatsResetCount": capwapBaseRadioEventsStatsResetCount,
       "capwapBaseRadioEventsStatsSwFailureCount": capwapBaseRadioEventsStatsSwFailureCount,
       "capwapBaseRadioEventsStatsHwFailureCount": capwapBaseRadioEventsStatsHwFailureCount,
       "capwapBaseRadioEventsStatsOtherFailureCount": capwapBaseRadioEventsStatsOtherFailureCount,
       "capwapBaseRadioEventsStatsUnknownFailureCount": capwapBaseRadioEventsStatsUnknownFailureCount,
       "capwapBaseRadioEventsStatsConfigUpdateCount": capwapBaseRadioEventsStatsConfigUpdateCount,
       "capwapBaseRadioEventsStatsChannelChangeCount": capwapBaseRadioEventsStatsChannelChangeCount,
       "capwapBaseRadioEventsStatsBandChangeCount": capwapBaseRadioEventsStatsBandChangeCount,
       "capwapBaseRadioEventsStatsCurrNoiseFloor": capwapBaseRadioEventsStatsCurrNoiseFloor,
       "capwapBaseRadioEventsStatsDecryptErrorCount": capwapBaseRadioEventsStatsDecryptErrorCount,
       "capwapBaseRadioEventsStatsLastFailureType": capwapBaseRadioEventsStatsLastFailureType,
       "capwapBaseParameters": capwapBaseParameters,
       "capwapBaseAcMaxRetransmit": capwapBaseAcMaxRetransmit,
       "capwapBaseAcChangeStatePendingTimer": capwapBaseAcChangeStatePendingTimer,
       "capwapBaseAcDataCheckTimer": capwapBaseAcDataCheckTimer,
       "capwapBaseAcDTLSSessionDeleteTimer": capwapBaseAcDTLSSessionDeleteTimer,
       "capwapBaseAcEchoInterval": capwapBaseAcEchoInterval,
       "capwapBaseAcRetransmitInterval": capwapBaseAcRetransmitInterval,
       "capwapBaseAcSilentInterval": capwapBaseAcSilentInterval,
       "capwapBaseAcWaitDTLSTimer": capwapBaseAcWaitDTLSTimer,
       "capwapBaseAcWaitJoinTimer": capwapBaseAcWaitJoinTimer,
       "capwapBaseAcEcnSupport": capwapBaseAcEcnSupport,
       "capwapBaseStats": capwapBaseStats,
       "capwapBaseFailedDTLSAuthFailureCount": capwapBaseFailedDTLSAuthFailureCount,
       "capwapBaseFailedDTLSSessionCount": capwapBaseFailedDTLSSessionCount,
       "capwapBaseNotifyVarObjects": capwapBaseNotifyVarObjects,
       "capwapBaseNtfWtpId": capwapBaseNtfWtpId,
       "capwapBaseNtfRadioId": capwapBaseNtfRadioId,
       "capwapBaseNtfChannelType": capwapBaseNtfChannelType,
       "capwapBaseNtfAuthenMethod": capwapBaseNtfAuthenMethod,
       "capwapBaseNtfChannelDownReason": capwapBaseNtfChannelDownReason,
       "capwapBaseNtfStationIdList": capwapBaseNtfStationIdList,
       "capwapBaseNtfAuthenFailureReason": capwapBaseNtfAuthenFailureReason,
       "capwapBaseNtfRadioOperStatusFlag": capwapBaseNtfRadioOperStatusFlag,
       "capwapBaseNtfRadioStatusCause": capwapBaseNtfRadioStatusCause,
       "capwapBaseNtfJoinFailureReason": capwapBaseNtfJoinFailureReason,
       "capwapBaseNtfImageFailureReason": capwapBaseNtfImageFailureReason,
       "capwapBaseNtfConfigMsgErrorType": capwapBaseNtfConfigMsgErrorType,
       "capwapBaseNtfMsgErrorElements": capwapBaseNtfMsgErrorElements,
       "capwapBaseNotifyControlObjects": capwapBaseNotifyControlObjects,
       "capwapBaseChannelUpDownNotifyEnable": capwapBaseChannelUpDownNotifyEnable,
       "capwapBaseDecryptErrorNotifyEnable": capwapBaseDecryptErrorNotifyEnable,
       "capwapBaseJoinFailureNotifyEnable": capwapBaseJoinFailureNotifyEnable,
       "capwapBaseImageUpgradeFailureNotifyEnable": capwapBaseImageUpgradeFailureNotifyEnable,
       "capwapBaseConfigMsgErrorNotifyEnable": capwapBaseConfigMsgErrorNotifyEnable,
       "capwapBaseRadioOperableStatusNotifyEnable": capwapBaseRadioOperableStatusNotifyEnable,
       "capwapBaseAuthenFailureNotifyEnable": capwapBaseAuthenFailureNotifyEnable,
       "capwapBaseConformance": capwapBaseConformance,
       "capwapBaseCompliances": capwapBaseCompliances,
       "capwapBaseCompliance": capwapBaseCompliance,
       "capwapBaseGroups": capwapBaseGroups,
       "capwapBaseAcNodeGroup": capwapBaseAcNodeGroup,
       "capwapBaseAcNodeGroup2": capwapBaseAcNodeGroup2,
       "capwapBaseAcNameListGroup": capwapBaseAcNameListGroup,
       "capwapBaseMacAclsGroup": capwapBaseMacAclsGroup,
       "capwapBaseWtpProfileGroup": capwapBaseWtpProfileGroup,
       "capwapBaseWtpProfileGroup2": capwapBaseWtpProfileGroup2,
       "capwapBaseWtpStateGroup": capwapBaseWtpStateGroup,
       "capwapBaseWtpGroup": capwapBaseWtpGroup,
       "capwapBaseWtpGroup2": capwapBaseWtpGroup2,
       "capwapBaseRadioGroup": capwapBaseRadioGroup,
       "capwapBaseStationGroup": capwapBaseStationGroup,
       "capwapBaseWtpEventsStatsGroup": capwapBaseWtpEventsStatsGroup,
       "capwapBaseRadioEventsStatsGroup": capwapBaseRadioEventsStatsGroup,
       "capwapBaseParametersGroup": capwapBaseParametersGroup,
       "capwapBaseStatsGroup": capwapBaseStatsGroup,
       "capwapBaseNotificationsGroup": capwapBaseNotificationsGroup,
       "capwapBaseNotifyVarsGroup": capwapBaseNotifyVarsGroup,
       "capwapBaseNotifyControlGroup": capwapBaseNotifyControlGroup}
)
