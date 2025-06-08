# SNMP MIB module (CISCO-RTTMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-RTTMON-MIB-120_5_T.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:18:37 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

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


# MODULE-IDENTITY

ciscoRttMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42)
)
if mibBuilder.loadTexts:
    ciscoRttMonMIB.setRevisions(
        ("1999-03-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RttReset(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("reset", 2))
    )



class RttMonOperation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("httpGet", 1),
          ("httpRaw", 2))
    )



class RttResponseSense(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("disconnected", 2),
          ("overThreshold", 3),
          ("timeout", 4),
          ("busy", 5),
          ("notConnected", 6),
          ("dropped", 7),
          ("sequenceError", 8),
          ("verifyError", 9),
          ("applicationSpecific", 10),
          ("dnsServerTimeout", 11),
          ("tcpConnectTimeout", 12),
          ("httpTransactionTimeout", 13),
          ("dnsQueryError", 14),
          ("httpError", 15),
          ("error", 16))
    )



class RttMonRttType(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("echo", 1),
          ("pathEcho", 2),
          ("fileIO", 3),
          ("script", 4),
          ("udpEcho", 5),
          ("tcpConnect", 6),
          ("http", 7),
          ("dns", 8),
          ("jitter", 9),
          ("dlsw", 10),
          ("dhcp", 11))
    )



class RttMonProtocol(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("ipIcmpEcho", 2),
          ("ipUdpEchoAppl", 3),
          ("snaRUEcho", 4),
          ("snaLU0EchoAppl", 5),
          ("snaLU2EchoAppl", 6),
          ("snaLU62Echo", 7),
          ("snaLU62EchoAppl", 8),
          ("appleTalkEcho", 9),
          ("appleTalkEchoAppl", 10),
          ("decNetEcho", 11),
          ("decNetEchoAppl", 12),
          ("ipxEcho", 13),
          ("ipxEchoAppl", 14),
          ("isoClnsEcho", 15),
          ("isoClnsEchoAppl", 16),
          ("vinesEcho", 17),
          ("vinesEchoAppl", 18),
          ("xnsEcho", 19),
          ("xnsEchoAppl", 20),
          ("apolloEcho", 21),
          ("apolloEchoAppl", 22),
          ("netbiosEchoAppl", 23),
          ("ipTcpConn", 24),
          ("httpAppl", 25),
          ("dnsAppl", 26),
          ("jitterAppl", 27),
          ("dlswAppl", 28),
          ("dhcpAppl", 29))
    )



class RttMonTargetAddress(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoRttMonObjects_ObjectIdentity = ObjectIdentity
ciscoRttMonObjects = _CiscoRttMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1)
)
_RttMonAppl_ObjectIdentity = ObjectIdentity
rttMonAppl = _RttMonAppl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1)
)
_RttMonApplVersion_Type = DisplayString
_RttMonApplVersion_Object = MibScalar
rttMonApplVersion = _RttMonApplVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 1),
    _RttMonApplVersion_Type()
)
rttMonApplVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplVersion.setStatus("current")


class _RttMonApplMaxPacketDataSize_Type(Integer32):
    """Custom type rttMonApplMaxPacketDataSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_RttMonApplMaxPacketDataSize_Type.__name__ = "Integer32"
_RttMonApplMaxPacketDataSize_Object = MibScalar
rttMonApplMaxPacketDataSize = _RttMonApplMaxPacketDataSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 2),
    _RttMonApplMaxPacketDataSize_Type()
)
rttMonApplMaxPacketDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplMaxPacketDataSize.setStatus("current")
if mibBuilder.loadTexts:
    rttMonApplMaxPacketDataSize.setUnits("octets")
_RttMonApplTimeOfLastSet_Type = TimeStamp
_RttMonApplTimeOfLastSet_Object = MibScalar
rttMonApplTimeOfLastSet = _RttMonApplTimeOfLastSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 3),
    _RttMonApplTimeOfLastSet_Type()
)
rttMonApplTimeOfLastSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplTimeOfLastSet.setStatus("current")


class _RttMonApplNumCtrlAdminEntry_Type(Integer32):
    """Custom type rttMonApplNumCtrlAdminEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_RttMonApplNumCtrlAdminEntry_Type.__name__ = "Integer32"
_RttMonApplNumCtrlAdminEntry_Object = MibScalar
rttMonApplNumCtrlAdminEntry = _RttMonApplNumCtrlAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 4),
    _RttMonApplNumCtrlAdminEntry_Type()
)
rttMonApplNumCtrlAdminEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplNumCtrlAdminEntry.setStatus("current")
_RttMonApplReset_Type = RttReset
_RttMonApplReset_Object = MibScalar
rttMonApplReset = _RttMonApplReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 5),
    _RttMonApplReset_Type()
)
rttMonApplReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rttMonApplReset.setStatus("current")
_RttMonApplPreConfigedReset_Type = RttReset
_RttMonApplPreConfigedReset_Object = MibScalar
rttMonApplPreConfigedReset = _RttMonApplPreConfigedReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 6),
    _RttMonApplPreConfigedReset_Type()
)
rttMonApplPreConfigedReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rttMonApplPreConfigedReset.setStatus("obsolete")
_RttMonApplSupportedRttTypesTable_Object = MibTable
rttMonApplSupportedRttTypesTable = _RttMonApplSupportedRttTypesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 7)
)
if mibBuilder.loadTexts:
    rttMonApplSupportedRttTypesTable.setStatus("current")
_RttMonApplSupportedRttTypesEntry_Object = MibTableRow
rttMonApplSupportedRttTypesEntry = _RttMonApplSupportedRttTypesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 7, 1)
)
rttMonApplSupportedRttTypesEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonApplSupportedRttTypes"),
)
if mibBuilder.loadTexts:
    rttMonApplSupportedRttTypesEntry.setStatus("current")
_RttMonApplSupportedRttTypes_Type = RttMonRttType
_RttMonApplSupportedRttTypes_Object = MibTableColumn
rttMonApplSupportedRttTypes = _RttMonApplSupportedRttTypes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 7, 1, 1),
    _RttMonApplSupportedRttTypes_Type()
)
rttMonApplSupportedRttTypes.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonApplSupportedRttTypes.setStatus("current")
_RttMonApplSupportedRttTypesValid_Type = TruthValue
_RttMonApplSupportedRttTypesValid_Object = MibTableColumn
rttMonApplSupportedRttTypesValid = _RttMonApplSupportedRttTypesValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 7, 1, 2),
    _RttMonApplSupportedRttTypesValid_Type()
)
rttMonApplSupportedRttTypesValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplSupportedRttTypesValid.setStatus("current")
_RttMonApplSupportedProtocolsTable_Object = MibTable
rttMonApplSupportedProtocolsTable = _RttMonApplSupportedProtocolsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 8)
)
if mibBuilder.loadTexts:
    rttMonApplSupportedProtocolsTable.setStatus("current")
_RttMonApplSupportedProtocolsEntry_Object = MibTableRow
rttMonApplSupportedProtocolsEntry = _RttMonApplSupportedProtocolsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 8, 1)
)
rttMonApplSupportedProtocolsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonApplSupportedProtocols"),
)
if mibBuilder.loadTexts:
    rttMonApplSupportedProtocolsEntry.setStatus("current")
_RttMonApplSupportedProtocols_Type = RttMonProtocol
_RttMonApplSupportedProtocols_Object = MibTableColumn
rttMonApplSupportedProtocols = _RttMonApplSupportedProtocols_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 8, 1, 1),
    _RttMonApplSupportedProtocols_Type()
)
rttMonApplSupportedProtocols.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonApplSupportedProtocols.setStatus("current")
_RttMonApplSupportedProtocolsValid_Type = TruthValue
_RttMonApplSupportedProtocolsValid_Object = MibTableColumn
rttMonApplSupportedProtocolsValid = _RttMonApplSupportedProtocolsValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 8, 1, 2),
    _RttMonApplSupportedProtocolsValid_Type()
)
rttMonApplSupportedProtocolsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplSupportedProtocolsValid.setStatus("current")
_RttMonApplPreConfigedTable_Object = MibTable
rttMonApplPreConfigedTable = _RttMonApplPreConfigedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 9)
)
if mibBuilder.loadTexts:
    rttMonApplPreConfigedTable.setStatus("obsolete")
_RttMonApplPreConfigedEntry_Object = MibTableRow
rttMonApplPreConfigedEntry = _RttMonApplPreConfigedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 9, 1)
)
rttMonApplPreConfigedEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonApplPreConfigedType"),
    (0, "CISCO-RTTMON-MIB", "rttMonApplPreConfigedName"),
)
if mibBuilder.loadTexts:
    rttMonApplPreConfigedEntry.setStatus("obsolete")


class _RttMonApplPreConfigedType_Type(Integer32):
    """Custom type rttMonApplPreConfigedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filePath", 1),
          ("scriptName", 2))
    )


_RttMonApplPreConfigedType_Type.__name__ = "Integer32"
_RttMonApplPreConfigedType_Object = MibTableColumn
rttMonApplPreConfigedType = _RttMonApplPreConfigedType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 9, 1, 2),
    _RttMonApplPreConfigedType_Type()
)
rttMonApplPreConfigedType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonApplPreConfigedType.setStatus("obsolete")
_RttMonApplPreConfigedName_Type = DisplayString
_RttMonApplPreConfigedName_Object = MibTableColumn
rttMonApplPreConfigedName = _RttMonApplPreConfigedName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 9, 1, 3),
    _RttMonApplPreConfigedName_Type()
)
rttMonApplPreConfigedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonApplPreConfigedName.setStatus("obsolete")
_RttMonApplPreConfigedValid_Type = TruthValue
_RttMonApplPreConfigedValid_Object = MibTableColumn
rttMonApplPreConfigedValid = _RttMonApplPreConfigedValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 9, 1, 4),
    _RttMonApplPreConfigedValid_Type()
)
rttMonApplPreConfigedValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplPreConfigedValid.setStatus("obsolete")


class _RttMonApplProbeCapacity_Type(Integer32):
    """Custom type rttMonApplProbeCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RttMonApplProbeCapacity_Type.__name__ = "Integer32"
_RttMonApplProbeCapacity_Object = MibScalar
rttMonApplProbeCapacity = _RttMonApplProbeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 10),
    _RttMonApplProbeCapacity_Type()
)
rttMonApplProbeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplProbeCapacity.setStatus("current")


class _RttMonApplFreeMemLowWaterMark_Type(Integer32):
    """Custom type rttMonApplFreeMemLowWaterMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonApplFreeMemLowWaterMark_Type.__name__ = "Integer32"
_RttMonApplFreeMemLowWaterMark_Object = MibScalar
rttMonApplFreeMemLowWaterMark = _RttMonApplFreeMemLowWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 11),
    _RttMonApplFreeMemLowWaterMark_Type()
)
rttMonApplFreeMemLowWaterMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rttMonApplFreeMemLowWaterMark.setStatus("current")
_RttMonApplLatestSetError_Type = DisplayString
_RttMonApplLatestSetError_Object = MibScalar
rttMonApplLatestSetError = _RttMonApplLatestSetError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 1, 12),
    _RttMonApplLatestSetError_Type()
)
rttMonApplLatestSetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonApplLatestSetError.setStatus("current")
_RttMonCtrl_ObjectIdentity = ObjectIdentity
rttMonCtrl = _RttMonCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2)
)
_RttMonCtrlAdminTable_Object = MibTable
rttMonCtrlAdminTable = _RttMonCtrlAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rttMonCtrlAdminTable.setStatus("current")
_RttMonCtrlAdminEntry_Object = MibTableRow
rttMonCtrlAdminEntry = _RttMonCtrlAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1)
)
rttMonCtrlAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonCtrlAdminEntry.setStatus("current")


class _RttMonCtrlAdminIndex_Type(Integer32):
    """Custom type rttMonCtrlAdminIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonCtrlAdminIndex_Type.__name__ = "Integer32"
_RttMonCtrlAdminIndex_Object = MibTableColumn
rttMonCtrlAdminIndex = _RttMonCtrlAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 1),
    _RttMonCtrlAdminIndex_Type()
)
rttMonCtrlAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonCtrlAdminIndex.setStatus("current")


class _RttMonCtrlAdminOwner_Type(OwnerString):
    """Custom type rttMonCtrlAdminOwner based on OwnerString"""
    defaultValue = OctetString("")


_RttMonCtrlAdminOwner_Type.__name__ = "OwnerString"
_RttMonCtrlAdminOwner_Object = MibTableColumn
rttMonCtrlAdminOwner = _RttMonCtrlAdminOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 2),
    _RttMonCtrlAdminOwner_Type()
)
rttMonCtrlAdminOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminOwner.setStatus("current")


class _RttMonCtrlAdminTag_Type(DisplayString):
    """Custom type rttMonCtrlAdminTag based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RttMonCtrlAdminTag_Type.__name__ = "DisplayString"
_RttMonCtrlAdminTag_Object = MibTableColumn
rttMonCtrlAdminTag = _RttMonCtrlAdminTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 3),
    _RttMonCtrlAdminTag_Type()
)
rttMonCtrlAdminTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminTag.setStatus("current")


class _RttMonCtrlAdminRttType_Type(RttMonRttType):
    """Custom type rttMonCtrlAdminRttType based on RttMonRttType"""
    defaultValue = 1


_RttMonCtrlAdminRttType_Type.__name__ = "RttMonRttType"
_RttMonCtrlAdminRttType_Object = MibTableColumn
rttMonCtrlAdminRttType = _RttMonCtrlAdminRttType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 4),
    _RttMonCtrlAdminRttType_Type()
)
rttMonCtrlAdminRttType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminRttType.setStatus("current")


class _RttMonCtrlAdminThreshold_Type(Integer32):
    """Custom type rttMonCtrlAdminThreshold based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonCtrlAdminThreshold_Type.__name__ = "Integer32"
_RttMonCtrlAdminThreshold_Object = MibTableColumn
rttMonCtrlAdminThreshold = _RttMonCtrlAdminThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 5),
    _RttMonCtrlAdminThreshold_Type()
)
rttMonCtrlAdminThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rttMonCtrlAdminThreshold.setUnits("milliseconds")


class _RttMonCtrlAdminFrequency_Type(Integer32):
    """Custom type rttMonCtrlAdminFrequency based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_RttMonCtrlAdminFrequency_Type.__name__ = "Integer32"
_RttMonCtrlAdminFrequency_Object = MibTableColumn
rttMonCtrlAdminFrequency = _RttMonCtrlAdminFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 6),
    _RttMonCtrlAdminFrequency_Type()
)
rttMonCtrlAdminFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminFrequency.setStatus("current")
if mibBuilder.loadTexts:
    rttMonCtrlAdminFrequency.setUnits("seconds")


class _RttMonCtrlAdminTimeout_Type(Integer32):
    """Custom type rttMonCtrlAdminTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800000),
    )


_RttMonCtrlAdminTimeout_Type.__name__ = "Integer32"
_RttMonCtrlAdminTimeout_Object = MibTableColumn
rttMonCtrlAdminTimeout = _RttMonCtrlAdminTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 7),
    _RttMonCtrlAdminTimeout_Type()
)
rttMonCtrlAdminTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rttMonCtrlAdminTimeout.setUnits("milliseconds")


class _RttMonCtrlAdminVerifyData_Type(TruthValue):
    """Custom type rttMonCtrlAdminVerifyData based on TruthValue"""
    defaultValue = 2


_RttMonCtrlAdminVerifyData_Type.__name__ = "TruthValue"
_RttMonCtrlAdminVerifyData_Object = MibTableColumn
rttMonCtrlAdminVerifyData = _RttMonCtrlAdminVerifyData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 8),
    _RttMonCtrlAdminVerifyData_Type()
)
rttMonCtrlAdminVerifyData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminVerifyData.setStatus("current")
_RttMonCtrlAdminStatus_Type = RowStatus
_RttMonCtrlAdminStatus_Object = MibTableColumn
rttMonCtrlAdminStatus = _RttMonCtrlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 9),
    _RttMonCtrlAdminStatus_Type()
)
rttMonCtrlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminStatus.setStatus("current")


class _RttMonCtrlAdminNvgen_Type(TruthValue):
    """Custom type rttMonCtrlAdminNvgen based on TruthValue"""
    defaultValue = 2


_RttMonCtrlAdminNvgen_Type.__name__ = "TruthValue"
_RttMonCtrlAdminNvgen_Object = MibTableColumn
rttMonCtrlAdminNvgen = _RttMonCtrlAdminNvgen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 1, 1, 10),
    _RttMonCtrlAdminNvgen_Type()
)
rttMonCtrlAdminNvgen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonCtrlAdminNvgen.setStatus("current")
_RttMonEchoAdminTable_Object = MibTable
rttMonEchoAdminTable = _RttMonEchoAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rttMonEchoAdminTable.setStatus("current")
_RttMonEchoAdminEntry_Object = MibTableRow
rttMonEchoAdminEntry = _RttMonEchoAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1)
)
rttMonEchoAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonEchoAdminEntry.setStatus("current")


class _RttMonEchoAdminProtocol_Type(RttMonProtocol):
    """Custom type rttMonEchoAdminProtocol based on RttMonProtocol"""
    defaultValue = 1


_RttMonEchoAdminProtocol_Type.__name__ = "RttMonProtocol"
_RttMonEchoAdminProtocol_Object = MibTableColumn
rttMonEchoAdminProtocol = _RttMonEchoAdminProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 1),
    _RttMonEchoAdminProtocol_Type()
)
rttMonEchoAdminProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminProtocol.setStatus("current")


class _RttMonEchoAdminTargetAddress_Type(RttMonTargetAddress):
    """Custom type rttMonEchoAdminTargetAddress based on RttMonTargetAddress"""
    defaultValue = OctetString("")


_RttMonEchoAdminTargetAddress_Type.__name__ = "RttMonTargetAddress"
_RttMonEchoAdminTargetAddress_Object = MibTableColumn
rttMonEchoAdminTargetAddress = _RttMonEchoAdminTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 2),
    _RttMonEchoAdminTargetAddress_Type()
)
rttMonEchoAdminTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetAddress.setStatus("current")


class _RttMonEchoAdminPktDataRequestSize_Type(Integer32):
    """Custom type rttMonEchoAdminPktDataRequestSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_RttMonEchoAdminPktDataRequestSize_Type.__name__ = "Integer32"
_RttMonEchoAdminPktDataRequestSize_Object = MibTableColumn
rttMonEchoAdminPktDataRequestSize = _RttMonEchoAdminPktDataRequestSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 3),
    _RttMonEchoAdminPktDataRequestSize_Type()
)
rttMonEchoAdminPktDataRequestSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminPktDataRequestSize.setStatus("current")
if mibBuilder.loadTexts:
    rttMonEchoAdminPktDataRequestSize.setUnits("octets")


class _RttMonEchoAdminPktDataResponseSize_Type(Integer32):
    """Custom type rttMonEchoAdminPktDataResponseSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_RttMonEchoAdminPktDataResponseSize_Type.__name__ = "Integer32"
_RttMonEchoAdminPktDataResponseSize_Object = MibTableColumn
rttMonEchoAdminPktDataResponseSize = _RttMonEchoAdminPktDataResponseSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 4),
    _RttMonEchoAdminPktDataResponseSize_Type()
)
rttMonEchoAdminPktDataResponseSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminPktDataResponseSize.setStatus("current")


class _RttMonEchoAdminTargetPort_Type(Integer32):
    """Custom type rttMonEchoAdminTargetPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RttMonEchoAdminTargetPort_Type.__name__ = "Integer32"
_RttMonEchoAdminTargetPort_Object = MibTableColumn
rttMonEchoAdminTargetPort = _RttMonEchoAdminTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 5),
    _RttMonEchoAdminTargetPort_Type()
)
rttMonEchoAdminTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetPort.setStatus("current")


class _RttMonEchoAdminSourceAddress_Type(RttMonTargetAddress):
    """Custom type rttMonEchoAdminSourceAddress based on RttMonTargetAddress"""
    defaultValue = OctetString("")


_RttMonEchoAdminSourceAddress_Type.__name__ = "RttMonTargetAddress"
_RttMonEchoAdminSourceAddress_Object = MibTableColumn
rttMonEchoAdminSourceAddress = _RttMonEchoAdminSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 6),
    _RttMonEchoAdminSourceAddress_Type()
)
rttMonEchoAdminSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminSourceAddress.setStatus("current")


class _RttMonEchoAdminSourcePort_Type(Integer32):
    """Custom type rttMonEchoAdminSourcePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_RttMonEchoAdminSourcePort_Type.__name__ = "Integer32"
_RttMonEchoAdminSourcePort_Object = MibTableColumn
rttMonEchoAdminSourcePort = _RttMonEchoAdminSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 7),
    _RttMonEchoAdminSourcePort_Type()
)
rttMonEchoAdminSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminSourcePort.setStatus("current")


class _RttMonEchoAdminControlEnable_Type(TruthValue):
    """Custom type rttMonEchoAdminControlEnable based on TruthValue"""
    defaultValue = 1


_RttMonEchoAdminControlEnable_Type.__name__ = "TruthValue"
_RttMonEchoAdminControlEnable_Object = MibTableColumn
rttMonEchoAdminControlEnable = _RttMonEchoAdminControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 8),
    _RttMonEchoAdminControlEnable_Type()
)
rttMonEchoAdminControlEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminControlEnable.setStatus("current")


class _RttMonEchoAdminTOS_Type(Integer32):
    """Custom type rttMonEchoAdminTOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RttMonEchoAdminTOS_Type.__name__ = "Integer32"
_RttMonEchoAdminTOS_Object = MibTableColumn
rttMonEchoAdminTOS = _RttMonEchoAdminTOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 9),
    _RttMonEchoAdminTOS_Type()
)
rttMonEchoAdminTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTOS.setStatus("current")


class _RttMonEchoAdminLSREnable_Type(TruthValue):
    """Custom type rttMonEchoAdminLSREnable based on TruthValue"""
    defaultValue = 2


_RttMonEchoAdminLSREnable_Type.__name__ = "TruthValue"
_RttMonEchoAdminLSREnable_Object = MibTableColumn
rttMonEchoAdminLSREnable = _RttMonEchoAdminLSREnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 10),
    _RttMonEchoAdminLSREnable_Type()
)
rttMonEchoAdminLSREnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonEchoAdminLSREnable.setStatus("current")


class _RttMonEchoAdminTargetAddressString_Type(DisplayString):
    """Custom type rttMonEchoAdminTargetAddressString based on DisplayString"""
    defaultValue = OctetString("")


_RttMonEchoAdminTargetAddressString_Type.__name__ = "DisplayString"
_RttMonEchoAdminTargetAddressString_Object = MibTableColumn
rttMonEchoAdminTargetAddressString = _RttMonEchoAdminTargetAddressString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 11),
    _RttMonEchoAdminTargetAddressString_Type()
)
rttMonEchoAdminTargetAddressString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminTargetAddressString.setStatus("current")


class _RttMonEchoAdminNameServer_Type(RttMonTargetAddress):
    """Custom type rttMonEchoAdminNameServer based on RttMonTargetAddress"""
    defaultValue = OctetString("")


_RttMonEchoAdminNameServer_Type.__name__ = "RttMonTargetAddress"
_RttMonEchoAdminNameServer_Object = MibTableColumn
rttMonEchoAdminNameServer = _RttMonEchoAdminNameServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 12),
    _RttMonEchoAdminNameServer_Type()
)
rttMonEchoAdminNameServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminNameServer.setStatus("current")


class _RttMonEchoAdminOperation_Type(RttMonOperation):
    """Custom type rttMonEchoAdminOperation based on RttMonOperation"""
    defaultValue = 1


_RttMonEchoAdminOperation_Type.__name__ = "RttMonOperation"
_RttMonEchoAdminOperation_Object = MibTableColumn
rttMonEchoAdminOperation = _RttMonEchoAdminOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 13),
    _RttMonEchoAdminOperation_Type()
)
rttMonEchoAdminOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminOperation.setStatus("current")


class _RttMonEchoAdminHTTPVersion_Type(DisplayString):
    """Custom type rttMonEchoAdminHTTPVersion based on DisplayString"""
    defaultValue = OctetString("1.0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_RttMonEchoAdminHTTPVersion_Type.__name__ = "DisplayString"
_RttMonEchoAdminHTTPVersion_Object = MibTableColumn
rttMonEchoAdminHTTPVersion = _RttMonEchoAdminHTTPVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 14),
    _RttMonEchoAdminHTTPVersion_Type()
)
rttMonEchoAdminHTTPVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminHTTPVersion.setStatus("current")


class _RttMonEchoAdminURL_Type(DisplayString):
    """Custom type rttMonEchoAdminURL based on DisplayString"""
    defaultValue = OctetString("")


_RttMonEchoAdminURL_Type.__name__ = "DisplayString"
_RttMonEchoAdminURL_Object = MibTableColumn
rttMonEchoAdminURL = _RttMonEchoAdminURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 15),
    _RttMonEchoAdminURL_Type()
)
rttMonEchoAdminURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminURL.setStatus("current")


class _RttMonEchoAdminCache_Type(TruthValue):
    """Custom type rttMonEchoAdminCache based on TruthValue"""
    defaultValue = 1


_RttMonEchoAdminCache_Type.__name__ = "TruthValue"
_RttMonEchoAdminCache_Object = MibTableColumn
rttMonEchoAdminCache = _RttMonEchoAdminCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 16),
    _RttMonEchoAdminCache_Type()
)
rttMonEchoAdminCache.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminCache.setStatus("current")


class _RttMonEchoAdminInterval_Type(Integer32):
    """Custom type rttMonEchoAdminInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_RttMonEchoAdminInterval_Type.__name__ = "Integer32"
_RttMonEchoAdminInterval_Object = MibTableColumn
rttMonEchoAdminInterval = _RttMonEchoAdminInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 17),
    _RttMonEchoAdminInterval_Type()
)
rttMonEchoAdminInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminInterval.setStatus("current")
if mibBuilder.loadTexts:
    rttMonEchoAdminInterval.setUnits("milliseconds")


class _RttMonEchoAdminNumPackets_Type(Integer32):
    """Custom type rttMonEchoAdminNumPackets based on Integer32"""
    defaultValue = 10


_RttMonEchoAdminNumPackets_Type.__name__ = "Integer32"
_RttMonEchoAdminNumPackets_Object = MibTableColumn
rttMonEchoAdminNumPackets = _RttMonEchoAdminNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 18),
    _RttMonEchoAdminNumPackets_Type()
)
rttMonEchoAdminNumPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminNumPackets.setStatus("current")


class _RttMonEchoAdminProxy_Type(DisplayString):
    """Custom type rttMonEchoAdminProxy based on DisplayString"""
    defaultValue = OctetString("")


_RttMonEchoAdminProxy_Type.__name__ = "DisplayString"
_RttMonEchoAdminProxy_Object = MibTableColumn
rttMonEchoAdminProxy = _RttMonEchoAdminProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 19),
    _RttMonEchoAdminProxy_Type()
)
rttMonEchoAdminProxy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminProxy.setStatus("current")


class _RttMonEchoAdminString1_Type(DisplayString):
    """Custom type rttMonEchoAdminString1 based on DisplayString"""
    defaultValue = OctetString("")


_RttMonEchoAdminString1_Type.__name__ = "DisplayString"
_RttMonEchoAdminString1_Object = MibTableColumn
rttMonEchoAdminString1 = _RttMonEchoAdminString1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 20),
    _RttMonEchoAdminString1_Type()
)
rttMonEchoAdminString1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminString1.setStatus("current")


class _RttMonEchoAdminString2_Type(DisplayString):
    """Custom type rttMonEchoAdminString2 based on DisplayString"""
    defaultValue = OctetString("")


_RttMonEchoAdminString2_Type.__name__ = "DisplayString"
_RttMonEchoAdminString2_Object = MibTableColumn
rttMonEchoAdminString2 = _RttMonEchoAdminString2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 21),
    _RttMonEchoAdminString2_Type()
)
rttMonEchoAdminString2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminString2.setStatus("current")


class _RttMonEchoAdminString3_Type(DisplayString):
    """Custom type rttMonEchoAdminString3 based on DisplayString"""
    defaultValue = OctetString("")


_RttMonEchoAdminString3_Type.__name__ = "DisplayString"
_RttMonEchoAdminString3_Object = MibTableColumn
rttMonEchoAdminString3 = _RttMonEchoAdminString3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 22),
    _RttMonEchoAdminString3_Type()
)
rttMonEchoAdminString3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminString3.setStatus("current")


class _RttMonEchoAdminString4_Type(DisplayString):
    """Custom type rttMonEchoAdminString4 based on DisplayString"""
    defaultValue = OctetString("")


_RttMonEchoAdminString4_Type.__name__ = "DisplayString"
_RttMonEchoAdminString4_Object = MibTableColumn
rttMonEchoAdminString4 = _RttMonEchoAdminString4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 23),
    _RttMonEchoAdminString4_Type()
)
rttMonEchoAdminString4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminString4.setStatus("current")


class _RttMonEchoAdminString5_Type(DisplayString):
    """Custom type rttMonEchoAdminString5 based on DisplayString"""
    defaultValue = OctetString("")


_RttMonEchoAdminString5_Type.__name__ = "DisplayString"
_RttMonEchoAdminString5_Object = MibTableColumn
rttMonEchoAdminString5 = _RttMonEchoAdminString5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 2, 1, 24),
    _RttMonEchoAdminString5_Type()
)
rttMonEchoAdminString5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoAdminString5.setStatus("current")
_RttMonFileIOAdminTable_Object = MibTable
rttMonFileIOAdminTable = _RttMonFileIOAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rttMonFileIOAdminTable.setStatus("obsolete")
_RttMonFileIOAdminEntry_Object = MibTableRow
rttMonFileIOAdminEntry = _RttMonFileIOAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 3, 1)
)
rttMonFileIOAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonFileIOAdminEntry.setStatus("obsolete")


class _RttMonFileIOAdminFilePath_Type(DisplayString):
    """Custom type rttMonFileIOAdminFilePath based on DisplayString"""
    defaultValue = OctetString("")


_RttMonFileIOAdminFilePath_Type.__name__ = "DisplayString"
_RttMonFileIOAdminFilePath_Object = MibTableColumn
rttMonFileIOAdminFilePath = _RttMonFileIOAdminFilePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 3, 1, 1),
    _RttMonFileIOAdminFilePath_Type()
)
rttMonFileIOAdminFilePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonFileIOAdminFilePath.setStatus("obsolete")


class _RttMonFileIOAdminSize_Type(Integer32):
    """Custom type rttMonFileIOAdminSize based on Integer32"""
    defaultValue = 1

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
        *(("n256", 1),
          ("n1k", 2),
          ("n64k", 3),
          ("n128k", 4),
          ("n256k", 5))
    )


_RttMonFileIOAdminSize_Type.__name__ = "Integer32"
_RttMonFileIOAdminSize_Object = MibTableColumn
rttMonFileIOAdminSize = _RttMonFileIOAdminSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 3, 1, 2),
    _RttMonFileIOAdminSize_Type()
)
rttMonFileIOAdminSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonFileIOAdminSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    rttMonFileIOAdminSize.setUnits("bytes")


class _RttMonFileIOAdminAction_Type(Integer32):
    """Custom type rttMonFileIOAdminAction based on Integer32"""
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
        *(("write", 1),
          ("read", 2),
          ("writeRead", 3))
    )


_RttMonFileIOAdminAction_Type.__name__ = "Integer32"
_RttMonFileIOAdminAction_Object = MibTableColumn
rttMonFileIOAdminAction = _RttMonFileIOAdminAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 3, 1, 3),
    _RttMonFileIOAdminAction_Type()
)
rttMonFileIOAdminAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonFileIOAdminAction.setStatus("obsolete")
_RttMonScriptAdminTable_Object = MibTable
rttMonScriptAdminTable = _RttMonScriptAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rttMonScriptAdminTable.setStatus("obsolete")
_RttMonScriptAdminEntry_Object = MibTableRow
rttMonScriptAdminEntry = _RttMonScriptAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 4, 1)
)
rttMonScriptAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonScriptAdminEntry.setStatus("obsolete")


class _RttMonScriptAdminName_Type(DisplayString):
    """Custom type rttMonScriptAdminName based on DisplayString"""
    defaultValue = OctetString("")


_RttMonScriptAdminName_Type.__name__ = "DisplayString"
_RttMonScriptAdminName_Object = MibTableColumn
rttMonScriptAdminName = _RttMonScriptAdminName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 4, 1, 1),
    _RttMonScriptAdminName_Type()
)
rttMonScriptAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScriptAdminName.setStatus("obsolete")


class _RttMonScriptAdminCmdLineParams_Type(DisplayString):
    """Custom type rttMonScriptAdminCmdLineParams based on DisplayString"""
    defaultValue = OctetString("")


_RttMonScriptAdminCmdLineParams_Type.__name__ = "DisplayString"
_RttMonScriptAdminCmdLineParams_Object = MibTableColumn
rttMonScriptAdminCmdLineParams = _RttMonScriptAdminCmdLineParams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 4, 1, 2),
    _RttMonScriptAdminCmdLineParams_Type()
)
rttMonScriptAdminCmdLineParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScriptAdminCmdLineParams.setStatus("obsolete")
_RttMonScheduleAdminTable_Object = MibTable
rttMonScheduleAdminTable = _RttMonScheduleAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rttMonScheduleAdminTable.setStatus("current")
_RttMonScheduleAdminEntry_Object = MibTableRow
rttMonScheduleAdminEntry = _RttMonScheduleAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    rttMonScheduleAdminEntry.setStatus("current")


class _RttMonScheduleAdminRttLife_Type(Integer32):
    """Custom type rttMonScheduleAdminRttLife based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonScheduleAdminRttLife_Type.__name__ = "Integer32"
_RttMonScheduleAdminRttLife_Object = MibTableColumn
rttMonScheduleAdminRttLife = _RttMonScheduleAdminRttLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1, 1),
    _RttMonScheduleAdminRttLife_Type()
)
rttMonScheduleAdminRttLife.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScheduleAdminRttLife.setStatus("current")
if mibBuilder.loadTexts:
    rttMonScheduleAdminRttLife.setUnits("seconds")


class _RttMonScheduleAdminRttStartTime_Type(TimeTicks):
    """Custom type rttMonScheduleAdminRttStartTime based on TimeTicks"""
    defaultValue = 0


_RttMonScheduleAdminRttStartTime_Type.__name__ = "TimeTicks"
_RttMonScheduleAdminRttStartTime_Object = MibTableColumn
rttMonScheduleAdminRttStartTime = _RttMonScheduleAdminRttStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1, 2),
    _RttMonScheduleAdminRttStartTime_Type()
)
rttMonScheduleAdminRttStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScheduleAdminRttStartTime.setStatus("current")


class _RttMonScheduleAdminConceptRowAgeout_Type(Integer32):
    """Custom type rttMonScheduleAdminConceptRowAgeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2073600),
    )


_RttMonScheduleAdminConceptRowAgeout_Type.__name__ = "Integer32"
_RttMonScheduleAdminConceptRowAgeout_Object = MibTableColumn
rttMonScheduleAdminConceptRowAgeout = _RttMonScheduleAdminConceptRowAgeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 5, 1, 3),
    _RttMonScheduleAdminConceptRowAgeout_Type()
)
rttMonScheduleAdminConceptRowAgeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonScheduleAdminConceptRowAgeout.setStatus("current")
if mibBuilder.loadTexts:
    rttMonScheduleAdminConceptRowAgeout.setUnits("seconds")
_RttMonReactAdminTable_Object = MibTable
rttMonReactAdminTable = _RttMonReactAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6)
)
if mibBuilder.loadTexts:
    rttMonReactAdminTable.setStatus("current")
_RttMonReactAdminEntry_Object = MibTableRow
rttMonReactAdminEntry = _RttMonReactAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    rttMonReactAdminEntry.setStatus("current")


class _RttMonReactAdminConnectionEnable_Type(TruthValue):
    """Custom type rttMonReactAdminConnectionEnable based on TruthValue"""
    defaultValue = 2


_RttMonReactAdminConnectionEnable_Type.__name__ = "TruthValue"
_RttMonReactAdminConnectionEnable_Object = MibTableColumn
rttMonReactAdminConnectionEnable = _RttMonReactAdminConnectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 1),
    _RttMonReactAdminConnectionEnable_Type()
)
rttMonReactAdminConnectionEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminConnectionEnable.setStatus("current")


class _RttMonReactAdminTimeoutEnable_Type(TruthValue):
    """Custom type rttMonReactAdminTimeoutEnable based on TruthValue"""
    defaultValue = 2


_RttMonReactAdminTimeoutEnable_Type.__name__ = "TruthValue"
_RttMonReactAdminTimeoutEnable_Object = MibTableColumn
rttMonReactAdminTimeoutEnable = _RttMonReactAdminTimeoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 2),
    _RttMonReactAdminTimeoutEnable_Type()
)
rttMonReactAdminTimeoutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminTimeoutEnable.setStatus("current")


class _RttMonReactAdminThresholdType_Type(Integer32):
    """Custom type rttMonReactAdminThresholdType based on Integer32"""
    defaultValue = 1

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
        *(("never", 1),
          ("immediate", 2),
          ("consecutive", 3),
          ("xOfy", 4),
          ("average", 5))
    )


_RttMonReactAdminThresholdType_Type.__name__ = "Integer32"
_RttMonReactAdminThresholdType_Object = MibTableColumn
rttMonReactAdminThresholdType = _RttMonReactAdminThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 3),
    _RttMonReactAdminThresholdType_Type()
)
rttMonReactAdminThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminThresholdType.setStatus("current")


class _RttMonReactAdminThresholdFalling_Type(Integer32):
    """Custom type rttMonReactAdminThresholdFalling based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonReactAdminThresholdFalling_Type.__name__ = "Integer32"
_RttMonReactAdminThresholdFalling_Object = MibTableColumn
rttMonReactAdminThresholdFalling = _RttMonReactAdminThresholdFalling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 4),
    _RttMonReactAdminThresholdFalling_Type()
)
rttMonReactAdminThresholdFalling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminThresholdFalling.setStatus("current")
if mibBuilder.loadTexts:
    rttMonReactAdminThresholdFalling.setUnits("milliseconds")


class _RttMonReactAdminThresholdCount_Type(Integer32):
    """Custom type rttMonReactAdminThresholdCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RttMonReactAdminThresholdCount_Type.__name__ = "Integer32"
_RttMonReactAdminThresholdCount_Object = MibTableColumn
rttMonReactAdminThresholdCount = _RttMonReactAdminThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 5),
    _RttMonReactAdminThresholdCount_Type()
)
rttMonReactAdminThresholdCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminThresholdCount.setStatus("current")


class _RttMonReactAdminThresholdCount2_Type(Integer32):
    """Custom type rttMonReactAdminThresholdCount2 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RttMonReactAdminThresholdCount2_Type.__name__ = "Integer32"
_RttMonReactAdminThresholdCount2_Object = MibTableColumn
rttMonReactAdminThresholdCount2 = _RttMonReactAdminThresholdCount2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 6),
    _RttMonReactAdminThresholdCount2_Type()
)
rttMonReactAdminThresholdCount2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminThresholdCount2.setStatus("current")


class _RttMonReactAdminActionType_Type(Integer32):
    """Custom type rttMonReactAdminActionType based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("trapOnly", 2),
          ("nmvtOnly", 3),
          ("triggerOnly", 4),
          ("trapAndNmvt", 5),
          ("trapAndTrigger", 6),
          ("nmvtAndTrigger", 7),
          ("trapNmvtAndTrigger", 8))
    )


_RttMonReactAdminActionType_Type.__name__ = "Integer32"
_RttMonReactAdminActionType_Object = MibTableColumn
rttMonReactAdminActionType = _RttMonReactAdminActionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 6, 1, 7),
    _RttMonReactAdminActionType_Type()
)
rttMonReactAdminActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactAdminActionType.setStatus("current")
_RttMonStatisticsAdminTable_Object = MibTable
rttMonStatisticsAdminTable = _RttMonStatisticsAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7)
)
if mibBuilder.loadTexts:
    rttMonStatisticsAdminTable.setStatus("current")
_RttMonStatisticsAdminEntry_Object = MibTableRow
rttMonStatisticsAdminEntry = _RttMonStatisticsAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    rttMonStatisticsAdminEntry.setStatus("current")


class _RttMonStatisticsAdminNumHourGroups_Type(Integer32):
    """Custom type rttMonStatisticsAdminNumHourGroups based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_RttMonStatisticsAdminNumHourGroups_Type.__name__ = "Integer32"
_RttMonStatisticsAdminNumHourGroups_Object = MibTableColumn
rttMonStatisticsAdminNumHourGroups = _RttMonStatisticsAdminNumHourGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1, 1),
    _RttMonStatisticsAdminNumHourGroups_Type()
)
rttMonStatisticsAdminNumHourGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminNumHourGroups.setStatus("current")


class _RttMonStatisticsAdminNumPaths_Type(Integer32):
    """Custom type rttMonStatisticsAdminNumPaths based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_RttMonStatisticsAdminNumPaths_Type.__name__ = "Integer32"
_RttMonStatisticsAdminNumPaths_Object = MibTableColumn
rttMonStatisticsAdminNumPaths = _RttMonStatisticsAdminNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1, 2),
    _RttMonStatisticsAdminNumPaths_Type()
)
rttMonStatisticsAdminNumPaths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminNumPaths.setStatus("current")


class _RttMonStatisticsAdminNumHops_Type(Integer32):
    """Custom type rttMonStatisticsAdminNumHops based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RttMonStatisticsAdminNumHops_Type.__name__ = "Integer32"
_RttMonStatisticsAdminNumHops_Object = MibTableColumn
rttMonStatisticsAdminNumHops = _RttMonStatisticsAdminNumHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1, 3),
    _RttMonStatisticsAdminNumHops_Type()
)
rttMonStatisticsAdminNumHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminNumHops.setStatus("current")


class _RttMonStatisticsAdminNumDistBuckets_Type(Integer32):
    """Custom type rttMonStatisticsAdminNumDistBuckets based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RttMonStatisticsAdminNumDistBuckets_Type.__name__ = "Integer32"
_RttMonStatisticsAdminNumDistBuckets_Object = MibTableColumn
rttMonStatisticsAdminNumDistBuckets = _RttMonStatisticsAdminNumDistBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1, 4),
    _RttMonStatisticsAdminNumDistBuckets_Type()
)
rttMonStatisticsAdminNumDistBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminNumDistBuckets.setStatus("current")


class _RttMonStatisticsAdminDistInterval_Type(Integer32):
    """Custom type rttMonStatisticsAdminDistInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RttMonStatisticsAdminDistInterval_Type.__name__ = "Integer32"
_RttMonStatisticsAdminDistInterval_Object = MibTableColumn
rttMonStatisticsAdminDistInterval = _RttMonStatisticsAdminDistInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 7, 1, 5),
    _RttMonStatisticsAdminDistInterval_Type()
)
rttMonStatisticsAdminDistInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminDistInterval.setStatus("current")
if mibBuilder.loadTexts:
    rttMonStatisticsAdminDistInterval.setUnits("milliseconds")
_RttMonHistoryAdminTable_Object = MibTable
rttMonHistoryAdminTable = _RttMonHistoryAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8)
)
if mibBuilder.loadTexts:
    rttMonHistoryAdminTable.setStatus("current")
_RttMonHistoryAdminEntry_Object = MibTableRow
rttMonHistoryAdminEntry = _RttMonHistoryAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    rttMonHistoryAdminEntry.setStatus("current")


class _RttMonHistoryAdminNumLives_Type(Integer32):
    """Custom type rttMonHistoryAdminNumLives based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RttMonHistoryAdminNumLives_Type.__name__ = "Integer32"
_RttMonHistoryAdminNumLives_Object = MibTableColumn
rttMonHistoryAdminNumLives = _RttMonHistoryAdminNumLives_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8, 1, 1),
    _RttMonHistoryAdminNumLives_Type()
)
rttMonHistoryAdminNumLives.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonHistoryAdminNumLives.setStatus("current")


class _RttMonHistoryAdminNumBuckets_Type(Integer32):
    """Custom type rttMonHistoryAdminNumBuckets based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RttMonHistoryAdminNumBuckets_Type.__name__ = "Integer32"
_RttMonHistoryAdminNumBuckets_Object = MibTableColumn
rttMonHistoryAdminNumBuckets = _RttMonHistoryAdminNumBuckets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8, 1, 2),
    _RttMonHistoryAdminNumBuckets_Type()
)
rttMonHistoryAdminNumBuckets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonHistoryAdminNumBuckets.setStatus("current")


class _RttMonHistoryAdminNumSamples_Type(Integer32):
    """Custom type rttMonHistoryAdminNumSamples based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RttMonHistoryAdminNumSamples_Type.__name__ = "Integer32"
_RttMonHistoryAdminNumSamples_Object = MibTableColumn
rttMonHistoryAdminNumSamples = _RttMonHistoryAdminNumSamples_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8, 1, 3),
    _RttMonHistoryAdminNumSamples_Type()
)
rttMonHistoryAdminNumSamples.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonHistoryAdminNumSamples.setStatus("current")


class _RttMonHistoryAdminFilter_Type(Integer32):
    """Custom type rttMonHistoryAdminFilter based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("all", 2),
          ("overThreshold", 3),
          ("failures", 4))
    )


_RttMonHistoryAdminFilter_Type.__name__ = "Integer32"
_RttMonHistoryAdminFilter_Object = MibTableColumn
rttMonHistoryAdminFilter = _RttMonHistoryAdminFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 8, 1, 4),
    _RttMonHistoryAdminFilter_Type()
)
rttMonHistoryAdminFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonHistoryAdminFilter.setStatus("current")
_RttMonCtrlOperTable_Object = MibTable
rttMonCtrlOperTable = _RttMonCtrlOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9)
)
if mibBuilder.loadTexts:
    rttMonCtrlOperTable.setStatus("current")
_RttMonCtrlOperEntry_Object = MibTableRow
rttMonCtrlOperEntry = _RttMonCtrlOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    rttMonCtrlOperEntry.setStatus("current")
_RttMonCtrlOperModificationTime_Type = TimeStamp
_RttMonCtrlOperModificationTime_Object = MibTableColumn
rttMonCtrlOperModificationTime = _RttMonCtrlOperModificationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 1),
    _RttMonCtrlOperModificationTime_Type()
)
rttMonCtrlOperModificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperModificationTime.setStatus("current")


class _RttMonCtrlOperDiagText_Type(DisplayString):
    """Custom type rttMonCtrlOperDiagText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_RttMonCtrlOperDiagText_Type.__name__ = "DisplayString"
_RttMonCtrlOperDiagText_Object = MibTableColumn
rttMonCtrlOperDiagText = _RttMonCtrlOperDiagText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 2),
    _RttMonCtrlOperDiagText_Type()
)
rttMonCtrlOperDiagText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperDiagText.setStatus("current")
_RttMonCtrlOperResetTime_Type = TimeStamp
_RttMonCtrlOperResetTime_Object = MibTableColumn
rttMonCtrlOperResetTime = _RttMonCtrlOperResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 3),
    _RttMonCtrlOperResetTime_Type()
)
rttMonCtrlOperResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperResetTime.setStatus("current")
_RttMonCtrlOperOctetsInUse_Type = Gauge32
_RttMonCtrlOperOctetsInUse_Object = MibTableColumn
rttMonCtrlOperOctetsInUse = _RttMonCtrlOperOctetsInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 4),
    _RttMonCtrlOperOctetsInUse_Type()
)
rttMonCtrlOperOctetsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperOctetsInUse.setStatus("current")


class _RttMonCtrlOperConnectionLostOccurred_Type(TruthValue):
    """Custom type rttMonCtrlOperConnectionLostOccurred based on TruthValue"""
    defaultValue = 2


_RttMonCtrlOperConnectionLostOccurred_Type.__name__ = "TruthValue"
_RttMonCtrlOperConnectionLostOccurred_Object = MibTableColumn
rttMonCtrlOperConnectionLostOccurred = _RttMonCtrlOperConnectionLostOccurred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 5),
    _RttMonCtrlOperConnectionLostOccurred_Type()
)
rttMonCtrlOperConnectionLostOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperConnectionLostOccurred.setStatus("current")


class _RttMonCtrlOperTimeoutOccurred_Type(TruthValue):
    """Custom type rttMonCtrlOperTimeoutOccurred based on TruthValue"""
    defaultValue = 2


_RttMonCtrlOperTimeoutOccurred_Type.__name__ = "TruthValue"
_RttMonCtrlOperTimeoutOccurred_Object = MibTableColumn
rttMonCtrlOperTimeoutOccurred = _RttMonCtrlOperTimeoutOccurred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 6),
    _RttMonCtrlOperTimeoutOccurred_Type()
)
rttMonCtrlOperTimeoutOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperTimeoutOccurred.setStatus("current")


class _RttMonCtrlOperOverThresholdOccurred_Type(TruthValue):
    """Custom type rttMonCtrlOperOverThresholdOccurred based on TruthValue"""
    defaultValue = 2


_RttMonCtrlOperOverThresholdOccurred_Type.__name__ = "TruthValue"
_RttMonCtrlOperOverThresholdOccurred_Object = MibTableColumn
rttMonCtrlOperOverThresholdOccurred = _RttMonCtrlOperOverThresholdOccurred_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 7),
    _RttMonCtrlOperOverThresholdOccurred_Type()
)
rttMonCtrlOperOverThresholdOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperOverThresholdOccurred.setStatus("current")


class _RttMonCtrlOperNumRtts_Type(Integer32):
    """Custom type rttMonCtrlOperNumRtts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonCtrlOperNumRtts_Type.__name__ = "Integer32"
_RttMonCtrlOperNumRtts_Object = MibTableColumn
rttMonCtrlOperNumRtts = _RttMonCtrlOperNumRtts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 8),
    _RttMonCtrlOperNumRtts_Type()
)
rttMonCtrlOperNumRtts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperNumRtts.setStatus("current")


class _RttMonCtrlOperRttLife_Type(Integer32):
    """Custom type rttMonCtrlOperRttLife based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonCtrlOperRttLife_Type.__name__ = "Integer32"
_RttMonCtrlOperRttLife_Object = MibTableColumn
rttMonCtrlOperRttLife = _RttMonCtrlOperRttLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 9),
    _RttMonCtrlOperRttLife_Type()
)
rttMonCtrlOperRttLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonCtrlOperRttLife.setStatus("current")
if mibBuilder.loadTexts:
    rttMonCtrlOperRttLife.setUnits("seconds")


class _RttMonCtrlOperState_Type(Integer32):
    """Custom type rttMonCtrlOperState based on Integer32"""
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
        *(("reset", 1),
          ("orderlyStop", 2),
          ("immediateStop", 3),
          ("pending", 4),
          ("inactive", 5),
          ("active", 6),
          ("restart", 7))
    )


_RttMonCtrlOperState_Type.__name__ = "Integer32"
_RttMonCtrlOperState_Object = MibTableColumn
rttMonCtrlOperState = _RttMonCtrlOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 9, 1, 10),
    _RttMonCtrlOperState_Type()
)
rttMonCtrlOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rttMonCtrlOperState.setStatus("current")
_RttMonLatestRttOperTable_Object = MibTable
rttMonLatestRttOperTable = _RttMonLatestRttOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10)
)
if mibBuilder.loadTexts:
    rttMonLatestRttOperTable.setStatus("current")
_RttMonLatestRttOperEntry_Object = MibTableRow
rttMonLatestRttOperEntry = _RttMonLatestRttOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    rttMonLatestRttOperEntry.setStatus("current")
_RttMonLatestRttOperCompletionTime_Type = Gauge32
_RttMonLatestRttOperCompletionTime_Object = MibTableColumn
rttMonLatestRttOperCompletionTime = _RttMonLatestRttOperCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 1),
    _RttMonLatestRttOperCompletionTime_Type()
)
rttMonLatestRttOperCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    rttMonLatestRttOperCompletionTime.setUnits("milliseconds")
_RttMonLatestRttOperSense_Type = RttResponseSense
_RttMonLatestRttOperSense_Object = MibTableColumn
rttMonLatestRttOperSense = _RttMonLatestRttOperSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 2),
    _RttMonLatestRttOperSense_Type()
)
rttMonLatestRttOperSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperSense.setStatus("current")


class _RttMonLatestRttOperApplSpecificSense_Type(Integer32):
    """Custom type rttMonLatestRttOperApplSpecificSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 2147483647),
    )


_RttMonLatestRttOperApplSpecificSense_Type.__name__ = "Integer32"
_RttMonLatestRttOperApplSpecificSense_Object = MibTableColumn
rttMonLatestRttOperApplSpecificSense = _RttMonLatestRttOperApplSpecificSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 3),
    _RttMonLatestRttOperApplSpecificSense_Type()
)
rttMonLatestRttOperApplSpecificSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperApplSpecificSense.setStatus("current")
_RttMonLatestRttOperSenseDescription_Type = DisplayString
_RttMonLatestRttOperSenseDescription_Object = MibTableColumn
rttMonLatestRttOperSenseDescription = _RttMonLatestRttOperSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 4),
    _RttMonLatestRttOperSenseDescription_Type()
)
rttMonLatestRttOperSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperSenseDescription.setStatus("current")
_RttMonLatestRttOperTime_Type = TimeStamp
_RttMonLatestRttOperTime_Object = MibTableColumn
rttMonLatestRttOperTime = _RttMonLatestRttOperTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 5),
    _RttMonLatestRttOperTime_Type()
)
rttMonLatestRttOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperTime.setStatus("current")
_RttMonLatestRttOperAddress_Type = RttMonTargetAddress
_RttMonLatestRttOperAddress_Object = MibTableColumn
rttMonLatestRttOperAddress = _RttMonLatestRttOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 10, 1, 6),
    _RttMonLatestRttOperAddress_Type()
)
rttMonLatestRttOperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestRttOperAddress.setStatus("current")
_RttMonReactTriggerAdminTable_Object = MibTable
rttMonReactTriggerAdminTable = _RttMonReactTriggerAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 11)
)
if mibBuilder.loadTexts:
    rttMonReactTriggerAdminTable.setStatus("current")
_RttMonReactTriggerAdminEntry_Object = MibTableRow
rttMonReactTriggerAdminEntry = _RttMonReactTriggerAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 11, 1)
)
rttMonReactTriggerAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonReactTriggerAdminRttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonReactTriggerAdminEntry.setStatus("current")


class _RttMonReactTriggerAdminRttMonCtrlAdminIndex_Type(Integer32):
    """Custom type rttMonReactTriggerAdminRttMonCtrlAdminIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonReactTriggerAdminRttMonCtrlAdminIndex_Type.__name__ = "Integer32"
_RttMonReactTriggerAdminRttMonCtrlAdminIndex_Object = MibTableColumn
rttMonReactTriggerAdminRttMonCtrlAdminIndex = _RttMonReactTriggerAdminRttMonCtrlAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 11, 1, 1),
    _RttMonReactTriggerAdminRttMonCtrlAdminIndex_Type()
)
rttMonReactTriggerAdminRttMonCtrlAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonReactTriggerAdminRttMonCtrlAdminIndex.setStatus("current")


class _RttMonReactTriggerAdminStatus_Type(RowStatus):
    """Custom type rttMonReactTriggerAdminStatus based on RowStatus"""
    defaultValue = 4


_RttMonReactTriggerAdminStatus_Type.__name__ = "RowStatus"
_RttMonReactTriggerAdminStatus_Object = MibTableColumn
rttMonReactTriggerAdminStatus = _RttMonReactTriggerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 11, 1, 2),
    _RttMonReactTriggerAdminStatus_Type()
)
rttMonReactTriggerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonReactTriggerAdminStatus.setStatus("current")
_RttMonReactTriggerOperTable_Object = MibTable
rttMonReactTriggerOperTable = _RttMonReactTriggerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 12)
)
if mibBuilder.loadTexts:
    rttMonReactTriggerOperTable.setStatus("current")
_RttMonReactTriggerOperEntry_Object = MibTableRow
rttMonReactTriggerOperEntry = _RttMonReactTriggerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    rttMonReactTriggerOperEntry.setStatus("current")


class _RttMonReactTriggerOperState_Type(Integer32):
    """Custom type rttMonReactTriggerOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("pending", 2))
    )


_RttMonReactTriggerOperState_Type.__name__ = "Integer32"
_RttMonReactTriggerOperState_Object = MibTableColumn
rttMonReactTriggerOperState = _RttMonReactTriggerOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 12, 1, 1),
    _RttMonReactTriggerOperState_Type()
)
rttMonReactTriggerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonReactTriggerOperState.setStatus("current")
_RttMonEchoPathAdminTable_Object = MibTable
rttMonEchoPathAdminTable = _RttMonEchoPathAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 13)
)
if mibBuilder.loadTexts:
    rttMonEchoPathAdminTable.setStatus("current")
_RttMonEchoPathAdminEntry_Object = MibTableRow
rttMonEchoPathAdminEntry = _RttMonEchoPathAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 13, 1)
)
rttMonEchoPathAdminEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonEchoPathAdminHopIndex"),
)
if mibBuilder.loadTexts:
    rttMonEchoPathAdminEntry.setStatus("current")


class _RttMonEchoPathAdminHopIndex_Type(Integer32):
    """Custom type rttMonEchoPathAdminHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RttMonEchoPathAdminHopIndex_Type.__name__ = "Integer32"
_RttMonEchoPathAdminHopIndex_Object = MibTableColumn
rttMonEchoPathAdminHopIndex = _RttMonEchoPathAdminHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 13, 1, 1),
    _RttMonEchoPathAdminHopIndex_Type()
)
rttMonEchoPathAdminHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonEchoPathAdminHopIndex.setStatus("current")
_RttMonEchoPathAdminHopAddress_Type = RttMonTargetAddress
_RttMonEchoPathAdminHopAddress_Object = MibTableColumn
rttMonEchoPathAdminHopAddress = _RttMonEchoPathAdminHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 2, 13, 1, 2),
    _RttMonEchoPathAdminHopAddress_Type()
)
rttMonEchoPathAdminHopAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rttMonEchoPathAdminHopAddress.setStatus("current")
_RttMonStats_ObjectIdentity = ObjectIdentity
rttMonStats = _RttMonStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3)
)
_RttMonStatsCaptureTable_Object = MibTable
rttMonStatsCaptureTable = _RttMonStatsCaptureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rttMonStatsCaptureTable.setStatus("current")
_RttMonStatsCaptureEntry_Object = MibTableRow
rttMonStatsCaptureEntry = _RttMonStatsCaptureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1)
)
rttMonStatsCaptureEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureStartTimeIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCapturePathIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureHopIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureDistIndex"),
)
if mibBuilder.loadTexts:
    rttMonStatsCaptureEntry.setStatus("current")
_RttMonStatsCaptureStartTimeIndex_Type = TimeStamp
_RttMonStatsCaptureStartTimeIndex_Object = MibTableColumn
rttMonStatsCaptureStartTimeIndex = _RttMonStatsCaptureStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 1),
    _RttMonStatsCaptureStartTimeIndex_Type()
)
rttMonStatsCaptureStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonStatsCaptureStartTimeIndex.setStatus("current")


class _RttMonStatsCapturePathIndex_Type(Integer32):
    """Custom type rttMonStatsCapturePathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_RttMonStatsCapturePathIndex_Type.__name__ = "Integer32"
_RttMonStatsCapturePathIndex_Object = MibTableColumn
rttMonStatsCapturePathIndex = _RttMonStatsCapturePathIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 2),
    _RttMonStatsCapturePathIndex_Type()
)
rttMonStatsCapturePathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonStatsCapturePathIndex.setStatus("current")


class _RttMonStatsCaptureHopIndex_Type(Integer32):
    """Custom type rttMonStatsCaptureHopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RttMonStatsCaptureHopIndex_Type.__name__ = "Integer32"
_RttMonStatsCaptureHopIndex_Object = MibTableColumn
rttMonStatsCaptureHopIndex = _RttMonStatsCaptureHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 3),
    _RttMonStatsCaptureHopIndex_Type()
)
rttMonStatsCaptureHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonStatsCaptureHopIndex.setStatus("current")


class _RttMonStatsCaptureDistIndex_Type(Integer32):
    """Custom type rttMonStatsCaptureDistIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RttMonStatsCaptureDistIndex_Type.__name__ = "Integer32"
_RttMonStatsCaptureDistIndex_Object = MibTableColumn
rttMonStatsCaptureDistIndex = _RttMonStatsCaptureDistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 4),
    _RttMonStatsCaptureDistIndex_Type()
)
rttMonStatsCaptureDistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonStatsCaptureDistIndex.setStatus("current")


class _RttMonStatsCaptureCompletions_Type(Integer32):
    """Custom type rttMonStatsCaptureCompletions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCaptureCompletions_Type.__name__ = "Integer32"
_RttMonStatsCaptureCompletions_Object = MibTableColumn
rttMonStatsCaptureCompletions = _RttMonStatsCaptureCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 5),
    _RttMonStatsCaptureCompletions_Type()
)
rttMonStatsCaptureCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureCompletions.setStatus("current")


class _RttMonStatsCaptureOverThresholds_Type(Integer32):
    """Custom type rttMonStatsCaptureOverThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCaptureOverThresholds_Type.__name__ = "Integer32"
_RttMonStatsCaptureOverThresholds_Object = MibTableColumn
rttMonStatsCaptureOverThresholds = _RttMonStatsCaptureOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 6),
    _RttMonStatsCaptureOverThresholds_Type()
)
rttMonStatsCaptureOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureOverThresholds.setStatus("current")
_RttMonStatsCaptureSumCompletionTime_Type = Gauge32
_RttMonStatsCaptureSumCompletionTime_Object = MibTableColumn
rttMonStatsCaptureSumCompletionTime = _RttMonStatsCaptureSumCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 7),
    _RttMonStatsCaptureSumCompletionTime_Type()
)
rttMonStatsCaptureSumCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureSumCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    rttMonStatsCaptureSumCompletionTime.setUnits("milliseconds")
_RttMonStatsCaptureSumCompletionTime2Low_Type = Gauge32
_RttMonStatsCaptureSumCompletionTime2Low_Object = MibTableColumn
rttMonStatsCaptureSumCompletionTime2Low = _RttMonStatsCaptureSumCompletionTime2Low_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 8),
    _RttMonStatsCaptureSumCompletionTime2Low_Type()
)
rttMonStatsCaptureSumCompletionTime2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureSumCompletionTime2Low.setStatus("current")
_RttMonStatsCaptureSumCompletionTime2High_Type = Gauge32
_RttMonStatsCaptureSumCompletionTime2High_Object = MibTableColumn
rttMonStatsCaptureSumCompletionTime2High = _RttMonStatsCaptureSumCompletionTime2High_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 9),
    _RttMonStatsCaptureSumCompletionTime2High_Type()
)
rttMonStatsCaptureSumCompletionTime2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureSumCompletionTime2High.setStatus("current")
_RttMonStatsCaptureCompletionTimeMax_Type = Gauge32
_RttMonStatsCaptureCompletionTimeMax_Object = MibTableColumn
rttMonStatsCaptureCompletionTimeMax = _RttMonStatsCaptureCompletionTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 10),
    _RttMonStatsCaptureCompletionTimeMax_Type()
)
rttMonStatsCaptureCompletionTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureCompletionTimeMax.setStatus("current")
if mibBuilder.loadTexts:
    rttMonStatsCaptureCompletionTimeMax.setUnits("milliseconds")
_RttMonStatsCaptureCompletionTimeMin_Type = Gauge32
_RttMonStatsCaptureCompletionTimeMin_Object = MibTableColumn
rttMonStatsCaptureCompletionTimeMin = _RttMonStatsCaptureCompletionTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 1, 1, 11),
    _RttMonStatsCaptureCompletionTimeMin_Type()
)
rttMonStatsCaptureCompletionTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCaptureCompletionTimeMin.setStatus("current")
if mibBuilder.loadTexts:
    rttMonStatsCaptureCompletionTimeMin.setUnits("milliseconds")
_RttMonStatsCollectTable_Object = MibTable
rttMonStatsCollectTable = _RttMonStatsCollectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rttMonStatsCollectTable.setStatus("current")
_RttMonStatsCollectEntry_Object = MibTableRow
rttMonStatsCollectEntry = _RttMonStatsCollectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1)
)
rttMonStatsCollectEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureStartTimeIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCapturePathIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureHopIndex"),
)
if mibBuilder.loadTexts:
    rttMonStatsCollectEntry.setStatus("current")


class _RttMonStatsCollectNumDisconnects_Type(Integer32):
    """Custom type rttMonStatsCollectNumDisconnects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectNumDisconnects_Type.__name__ = "Integer32"
_RttMonStatsCollectNumDisconnects_Object = MibTableColumn
rttMonStatsCollectNumDisconnects = _RttMonStatsCollectNumDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 1),
    _RttMonStatsCollectNumDisconnects_Type()
)
rttMonStatsCollectNumDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectNumDisconnects.setStatus("current")


class _RttMonStatsCollectTimeouts_Type(Integer32):
    """Custom type rttMonStatsCollectTimeouts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectTimeouts_Type.__name__ = "Integer32"
_RttMonStatsCollectTimeouts_Object = MibTableColumn
rttMonStatsCollectTimeouts = _RttMonStatsCollectTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 2),
    _RttMonStatsCollectTimeouts_Type()
)
rttMonStatsCollectTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectTimeouts.setStatus("current")


class _RttMonStatsCollectBusies_Type(Integer32):
    """Custom type rttMonStatsCollectBusies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectBusies_Type.__name__ = "Integer32"
_RttMonStatsCollectBusies_Object = MibTableColumn
rttMonStatsCollectBusies = _RttMonStatsCollectBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 3),
    _RttMonStatsCollectBusies_Type()
)
rttMonStatsCollectBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectBusies.setStatus("current")


class _RttMonStatsCollectNoConnections_Type(Integer32):
    """Custom type rttMonStatsCollectNoConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectNoConnections_Type.__name__ = "Integer32"
_RttMonStatsCollectNoConnections_Object = MibTableColumn
rttMonStatsCollectNoConnections = _RttMonStatsCollectNoConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 4),
    _RttMonStatsCollectNoConnections_Type()
)
rttMonStatsCollectNoConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectNoConnections.setStatus("current")


class _RttMonStatsCollectDrops_Type(Integer32):
    """Custom type rttMonStatsCollectDrops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectDrops_Type.__name__ = "Integer32"
_RttMonStatsCollectDrops_Object = MibTableColumn
rttMonStatsCollectDrops = _RttMonStatsCollectDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 5),
    _RttMonStatsCollectDrops_Type()
)
rttMonStatsCollectDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectDrops.setStatus("current")


class _RttMonStatsCollectSequenceErrors_Type(Integer32):
    """Custom type rttMonStatsCollectSequenceErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectSequenceErrors_Type.__name__ = "Integer32"
_RttMonStatsCollectSequenceErrors_Object = MibTableColumn
rttMonStatsCollectSequenceErrors = _RttMonStatsCollectSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 6),
    _RttMonStatsCollectSequenceErrors_Type()
)
rttMonStatsCollectSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectSequenceErrors.setStatus("current")


class _RttMonStatsCollectVerifyErrors_Type(Integer32):
    """Custom type rttMonStatsCollectVerifyErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsCollectVerifyErrors_Type.__name__ = "Integer32"
_RttMonStatsCollectVerifyErrors_Object = MibTableColumn
rttMonStatsCollectVerifyErrors = _RttMonStatsCollectVerifyErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 7),
    _RttMonStatsCollectVerifyErrors_Type()
)
rttMonStatsCollectVerifyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectVerifyErrors.setStatus("current")
_RttMonStatsCollectAddress_Type = RttMonTargetAddress
_RttMonStatsCollectAddress_Object = MibTableColumn
rttMonStatsCollectAddress = _RttMonStatsCollectAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 2, 1, 8),
    _RttMonStatsCollectAddress_Type()
)
rttMonStatsCollectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsCollectAddress.setStatus("current")
_RttMonStatsTotalsTable_Object = MibTable
rttMonStatsTotalsTable = _RttMonStatsTotalsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rttMonStatsTotalsTable.setStatus("current")
_RttMonStatsTotalsEntry_Object = MibTableRow
rttMonStatsTotalsEntry = _RttMonStatsTotalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 3, 1)
)
rttMonStatsTotalsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonStatsCaptureStartTimeIndex"),
)
if mibBuilder.loadTexts:
    rttMonStatsTotalsEntry.setStatus("current")
_RttMonStatsTotalsElapsedTime_Type = TimeInterval
_RttMonStatsTotalsElapsedTime_Object = MibTableColumn
rttMonStatsTotalsElapsedTime = _RttMonStatsTotalsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 3, 1, 1),
    _RttMonStatsTotalsElapsedTime_Type()
)
rttMonStatsTotalsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsTotalsElapsedTime.setStatus("current")


class _RttMonStatsTotalsInitiations_Type(Integer32):
    """Custom type rttMonStatsTotalsInitiations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RttMonStatsTotalsInitiations_Type.__name__ = "Integer32"
_RttMonStatsTotalsInitiations_Object = MibTableColumn
rttMonStatsTotalsInitiations = _RttMonStatsTotalsInitiations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 3, 1, 2),
    _RttMonStatsTotalsInitiations_Type()
)
rttMonStatsTotalsInitiations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonStatsTotalsInitiations.setStatus("current")
_RttMonHTTPStatsTable_Object = MibTable
rttMonHTTPStatsTable = _RttMonHTTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4)
)
if mibBuilder.loadTexts:
    rttMonHTTPStatsTable.setStatus("current")
_RttMonHTTPStatsEntry_Object = MibTableRow
rttMonHTTPStatsEntry = _RttMonHTTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1)
)
rttMonHTTPStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonHTTPStatsStartTimeIndex"),
)
if mibBuilder.loadTexts:
    rttMonHTTPStatsEntry.setStatus("current")
_RttMonHTTPStatsStartTimeIndex_Type = TimeStamp
_RttMonHTTPStatsStartTimeIndex_Object = MibTableColumn
rttMonHTTPStatsStartTimeIndex = _RttMonHTTPStatsStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 1),
    _RttMonHTTPStatsStartTimeIndex_Type()
)
rttMonHTTPStatsStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonHTTPStatsStartTimeIndex.setStatus("current")
_RttMonHTTPStatsCompletions_Type = Counter32
_RttMonHTTPStatsCompletions_Object = MibTableColumn
rttMonHTTPStatsCompletions = _RttMonHTTPStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 2),
    _RttMonHTTPStatsCompletions_Type()
)
rttMonHTTPStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsCompletions.setStatus("current")
_RttMonHTTPStatsOverThresholds_Type = Counter32
_RttMonHTTPStatsOverThresholds_Object = MibTableColumn
rttMonHTTPStatsOverThresholds = _RttMonHTTPStatsOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 3),
    _RttMonHTTPStatsOverThresholds_Type()
)
rttMonHTTPStatsOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsOverThresholds.setStatus("current")
_RttMonHTTPStatsRTTSum_Type = Counter32
_RttMonHTTPStatsRTTSum_Object = MibTableColumn
rttMonHTTPStatsRTTSum = _RttMonHTTPStatsRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 4),
    _RttMonHTTPStatsRTTSum_Type()
)
rttMonHTTPStatsRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTSum.setStatus("current")
_RttMonHTTPStatsRTTSum2Low_Type = Counter32
_RttMonHTTPStatsRTTSum2Low_Object = MibTableColumn
rttMonHTTPStatsRTTSum2Low = _RttMonHTTPStatsRTTSum2Low_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 5),
    _RttMonHTTPStatsRTTSum2Low_Type()
)
rttMonHTTPStatsRTTSum2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTSum2Low.setStatus("current")
_RttMonHTTPStatsRTTSum2High_Type = Counter32
_RttMonHTTPStatsRTTSum2High_Object = MibTableColumn
rttMonHTTPStatsRTTSum2High = _RttMonHTTPStatsRTTSum2High_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 6),
    _RttMonHTTPStatsRTTSum2High_Type()
)
rttMonHTTPStatsRTTSum2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTSum2High.setStatus("current")
_RttMonHTTPStatsRTTMin_Type = Gauge32
_RttMonHTTPStatsRTTMin_Object = MibTableColumn
rttMonHTTPStatsRTTMin = _RttMonHTTPStatsRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 7),
    _RttMonHTTPStatsRTTMin_Type()
)
rttMonHTTPStatsRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTMin.setStatus("current")
_RttMonHTTPStatsRTTMax_Type = Gauge32
_RttMonHTTPStatsRTTMax_Object = MibTableColumn
rttMonHTTPStatsRTTMax = _RttMonHTTPStatsRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 8),
    _RttMonHTTPStatsRTTMax_Type()
)
rttMonHTTPStatsRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsRTTMax.setStatus("current")
_RttMonHTTPStatsDNSRTTSum_Type = Counter32
_RttMonHTTPStatsDNSRTTSum_Object = MibTableColumn
rttMonHTTPStatsDNSRTTSum = _RttMonHTTPStatsDNSRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 9),
    _RttMonHTTPStatsDNSRTTSum_Type()
)
rttMonHTTPStatsDNSRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsDNSRTTSum.setStatus("current")
_RttMonHTTPStatsTCPConnectRTTSum_Type = Counter32
_RttMonHTTPStatsTCPConnectRTTSum_Object = MibTableColumn
rttMonHTTPStatsTCPConnectRTTSum = _RttMonHTTPStatsTCPConnectRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 10),
    _RttMonHTTPStatsTCPConnectRTTSum_Type()
)
rttMonHTTPStatsTCPConnectRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsTCPConnectRTTSum.setStatus("current")
_RttMonHTTPStatsTransactionRTTSum_Type = Counter32
_RttMonHTTPStatsTransactionRTTSum_Object = MibTableColumn
rttMonHTTPStatsTransactionRTTSum = _RttMonHTTPStatsTransactionRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 11),
    _RttMonHTTPStatsTransactionRTTSum_Type()
)
rttMonHTTPStatsTransactionRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsTransactionRTTSum.setStatus("current")
_RttMonHTTPStatsMessageBodyOctetsSum_Type = Counter32
_RttMonHTTPStatsMessageBodyOctetsSum_Object = MibTableColumn
rttMonHTTPStatsMessageBodyOctetsSum = _RttMonHTTPStatsMessageBodyOctetsSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 12),
    _RttMonHTTPStatsMessageBodyOctetsSum_Type()
)
rttMonHTTPStatsMessageBodyOctetsSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsMessageBodyOctetsSum.setStatus("current")
_RttMonHTTPStatsDNSServerTimeout_Type = Counter32
_RttMonHTTPStatsDNSServerTimeout_Object = MibTableColumn
rttMonHTTPStatsDNSServerTimeout = _RttMonHTTPStatsDNSServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 13),
    _RttMonHTTPStatsDNSServerTimeout_Type()
)
rttMonHTTPStatsDNSServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsDNSServerTimeout.setStatus("current")
_RttMonHTTPStatsTCPConnectTimeout_Type = Counter32
_RttMonHTTPStatsTCPConnectTimeout_Object = MibTableColumn
rttMonHTTPStatsTCPConnectTimeout = _RttMonHTTPStatsTCPConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 14),
    _RttMonHTTPStatsTCPConnectTimeout_Type()
)
rttMonHTTPStatsTCPConnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsTCPConnectTimeout.setStatus("current")
_RttMonHTTPStatsTransactionTimeout_Type = Counter32
_RttMonHTTPStatsTransactionTimeout_Object = MibTableColumn
rttMonHTTPStatsTransactionTimeout = _RttMonHTTPStatsTransactionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 15),
    _RttMonHTTPStatsTransactionTimeout_Type()
)
rttMonHTTPStatsTransactionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsTransactionTimeout.setStatus("current")
_RttMonHTTPStatsDNSQueryError_Type = Counter32
_RttMonHTTPStatsDNSQueryError_Object = MibTableColumn
rttMonHTTPStatsDNSQueryError = _RttMonHTTPStatsDNSQueryError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 16),
    _RttMonHTTPStatsDNSQueryError_Type()
)
rttMonHTTPStatsDNSQueryError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsDNSQueryError.setStatus("current")
_RttMonHTTPStatsHTTPError_Type = Counter32
_RttMonHTTPStatsHTTPError_Object = MibTableColumn
rttMonHTTPStatsHTTPError = _RttMonHTTPStatsHTTPError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 17),
    _RttMonHTTPStatsHTTPError_Type()
)
rttMonHTTPStatsHTTPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsHTTPError.setStatus("current")
_RttMonHTTPStatsError_Type = Counter32
_RttMonHTTPStatsError_Object = MibTableColumn
rttMonHTTPStatsError = _RttMonHTTPStatsError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 18),
    _RttMonHTTPStatsError_Type()
)
rttMonHTTPStatsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsError.setStatus("current")
_RttMonHTTPStatsBusies_Type = Counter32
_RttMonHTTPStatsBusies_Object = MibTableColumn
rttMonHTTPStatsBusies = _RttMonHTTPStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 4, 1, 19),
    _RttMonHTTPStatsBusies_Type()
)
rttMonHTTPStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHTTPStatsBusies.setStatus("current")
_RttMonJitterStatsTable_Object = MibTable
rttMonJitterStatsTable = _RttMonJitterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5)
)
if mibBuilder.loadTexts:
    rttMonJitterStatsTable.setStatus("current")
_RttMonJitterStatsEntry_Object = MibTableRow
rttMonJitterStatsEntry = _RttMonJitterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1)
)
rttMonJitterStatsEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonJitterStatsStartTimeIndex"),
)
if mibBuilder.loadTexts:
    rttMonJitterStatsEntry.setStatus("current")
_RttMonJitterStatsStartTimeIndex_Type = TimeStamp
_RttMonJitterStatsStartTimeIndex_Object = MibTableColumn
rttMonJitterStatsStartTimeIndex = _RttMonJitterStatsStartTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 1),
    _RttMonJitterStatsStartTimeIndex_Type()
)
rttMonJitterStatsStartTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonJitterStatsStartTimeIndex.setStatus("current")
_RttMonJitterStatsCompletions_Type = Counter32
_RttMonJitterStatsCompletions_Object = MibTableColumn
rttMonJitterStatsCompletions = _RttMonJitterStatsCompletions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 2),
    _RttMonJitterStatsCompletions_Type()
)
rttMonJitterStatsCompletions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsCompletions.setStatus("current")
_RttMonJitterStatsOverThresholds_Type = Counter32
_RttMonJitterStatsOverThresholds_Object = MibTableColumn
rttMonJitterStatsOverThresholds = _RttMonJitterStatsOverThresholds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 3),
    _RttMonJitterStatsOverThresholds_Type()
)
rttMonJitterStatsOverThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsOverThresholds.setStatus("current")
_RttMonJitterStatsNumOfRTT_Type = Counter32
_RttMonJitterStatsNumOfRTT_Object = MibTableColumn
rttMonJitterStatsNumOfRTT = _RttMonJitterStatsNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 4),
    _RttMonJitterStatsNumOfRTT_Type()
)
rttMonJitterStatsNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfRTT.setStatus("current")
_RttMonJitterStatsRTTSum_Type = Counter32
_RttMonJitterStatsRTTSum_Object = MibTableColumn
rttMonJitterStatsRTTSum = _RttMonJitterStatsRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 5),
    _RttMonJitterStatsRTTSum_Type()
)
rttMonJitterStatsRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTSum.setStatus("current")
_RttMonJitterStatsRTTSum2Low_Type = Counter32
_RttMonJitterStatsRTTSum2Low_Object = MibTableColumn
rttMonJitterStatsRTTSum2Low = _RttMonJitterStatsRTTSum2Low_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 6),
    _RttMonJitterStatsRTTSum2Low_Type()
)
rttMonJitterStatsRTTSum2Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTSum2Low.setStatus("current")
_RttMonJitterStatsRTTSum2High_Type = Counter32
_RttMonJitterStatsRTTSum2High_Object = MibTableColumn
rttMonJitterStatsRTTSum2High = _RttMonJitterStatsRTTSum2High_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 7),
    _RttMonJitterStatsRTTSum2High_Type()
)
rttMonJitterStatsRTTSum2High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTSum2High.setStatus("current")
_RttMonJitterStatsRTTMin_Type = Gauge32
_RttMonJitterStatsRTTMin_Object = MibTableColumn
rttMonJitterStatsRTTMin = _RttMonJitterStatsRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 8),
    _RttMonJitterStatsRTTMin_Type()
)
rttMonJitterStatsRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTMin.setStatus("current")
_RttMonJitterStatsRTTMax_Type = Gauge32
_RttMonJitterStatsRTTMax_Object = MibTableColumn
rttMonJitterStatsRTTMax = _RttMonJitterStatsRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 9),
    _RttMonJitterStatsRTTMax_Type()
)
rttMonJitterStatsRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsRTTMax.setStatus("current")
_RttMonJitterStatsMinOfPositivesSD_Type = Gauge32
_RttMonJitterStatsMinOfPositivesSD_Object = MibTableColumn
rttMonJitterStatsMinOfPositivesSD = _RttMonJitterStatsMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 10),
    _RttMonJitterStatsMinOfPositivesSD_Type()
)
rttMonJitterStatsMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMinOfPositivesSD.setStatus("current")
_RttMonJitterStatsMaxOfPositivesSD_Type = Gauge32
_RttMonJitterStatsMaxOfPositivesSD_Object = MibTableColumn
rttMonJitterStatsMaxOfPositivesSD = _RttMonJitterStatsMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 11),
    _RttMonJitterStatsMaxOfPositivesSD_Type()
)
rttMonJitterStatsMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMaxOfPositivesSD.setStatus("current")
_RttMonJitterStatsNumOfPositivesSD_Type = Counter32
_RttMonJitterStatsNumOfPositivesSD_Object = MibTableColumn
rttMonJitterStatsNumOfPositivesSD = _RttMonJitterStatsNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 12),
    _RttMonJitterStatsNumOfPositivesSD_Type()
)
rttMonJitterStatsNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfPositivesSD.setStatus("current")
_RttMonJitterStatsSumOfPositivesSD_Type = Counter32
_RttMonJitterStatsSumOfPositivesSD_Object = MibTableColumn
rttMonJitterStatsSumOfPositivesSD = _RttMonJitterStatsSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 13),
    _RttMonJitterStatsSumOfPositivesSD_Type()
)
rttMonJitterStatsSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSumOfPositivesSD.setStatus("current")
_RttMonJitterStatsSum2PositivesSDLow_Type = Counter32
_RttMonJitterStatsSum2PositivesSDLow_Object = MibTableColumn
rttMonJitterStatsSum2PositivesSDLow = _RttMonJitterStatsSum2PositivesSDLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 14),
    _RttMonJitterStatsSum2PositivesSDLow_Type()
)
rttMonJitterStatsSum2PositivesSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2PositivesSDLow.setStatus("current")
_RttMonJitterStatsSum2PositivesSDHigh_Type = Counter32
_RttMonJitterStatsSum2PositivesSDHigh_Object = MibTableColumn
rttMonJitterStatsSum2PositivesSDHigh = _RttMonJitterStatsSum2PositivesSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 15),
    _RttMonJitterStatsSum2PositivesSDHigh_Type()
)
rttMonJitterStatsSum2PositivesSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2PositivesSDHigh.setStatus("current")
_RttMonJitterStatsMinOfNegativesSD_Type = Gauge32
_RttMonJitterStatsMinOfNegativesSD_Object = MibTableColumn
rttMonJitterStatsMinOfNegativesSD = _RttMonJitterStatsMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 16),
    _RttMonJitterStatsMinOfNegativesSD_Type()
)
rttMonJitterStatsMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMinOfNegativesSD.setStatus("current")
_RttMonJitterStatsMaxOfNegativesSD_Type = Gauge32
_RttMonJitterStatsMaxOfNegativesSD_Object = MibTableColumn
rttMonJitterStatsMaxOfNegativesSD = _RttMonJitterStatsMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 17),
    _RttMonJitterStatsMaxOfNegativesSD_Type()
)
rttMonJitterStatsMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMaxOfNegativesSD.setStatus("current")
_RttMonJitterStatsNumOfNegativesSD_Type = Counter32
_RttMonJitterStatsNumOfNegativesSD_Object = MibTableColumn
rttMonJitterStatsNumOfNegativesSD = _RttMonJitterStatsNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 18),
    _RttMonJitterStatsNumOfNegativesSD_Type()
)
rttMonJitterStatsNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfNegativesSD.setStatus("current")
_RttMonJitterStatsSumOfNegativesSD_Type = Counter32
_RttMonJitterStatsSumOfNegativesSD_Object = MibTableColumn
rttMonJitterStatsSumOfNegativesSD = _RttMonJitterStatsSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 19),
    _RttMonJitterStatsSumOfNegativesSD_Type()
)
rttMonJitterStatsSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSumOfNegativesSD.setStatus("current")
_RttMonJitterStatsSum2NegativesSDLow_Type = Counter32
_RttMonJitterStatsSum2NegativesSDLow_Object = MibTableColumn
rttMonJitterStatsSum2NegativesSDLow = _RttMonJitterStatsSum2NegativesSDLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 20),
    _RttMonJitterStatsSum2NegativesSDLow_Type()
)
rttMonJitterStatsSum2NegativesSDLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2NegativesSDLow.setStatus("current")
_RttMonJitterStatsSum2NegativesSDHigh_Type = Counter32
_RttMonJitterStatsSum2NegativesSDHigh_Object = MibTableColumn
rttMonJitterStatsSum2NegativesSDHigh = _RttMonJitterStatsSum2NegativesSDHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 21),
    _RttMonJitterStatsSum2NegativesSDHigh_Type()
)
rttMonJitterStatsSum2NegativesSDHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2NegativesSDHigh.setStatus("current")
_RttMonJitterStatsMinOfPositivesDS_Type = Gauge32
_RttMonJitterStatsMinOfPositivesDS_Object = MibTableColumn
rttMonJitterStatsMinOfPositivesDS = _RttMonJitterStatsMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 22),
    _RttMonJitterStatsMinOfPositivesDS_Type()
)
rttMonJitterStatsMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMinOfPositivesDS.setStatus("current")
_RttMonJitterStatsMaxOfPositivesDS_Type = Gauge32
_RttMonJitterStatsMaxOfPositivesDS_Object = MibTableColumn
rttMonJitterStatsMaxOfPositivesDS = _RttMonJitterStatsMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 23),
    _RttMonJitterStatsMaxOfPositivesDS_Type()
)
rttMonJitterStatsMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMaxOfPositivesDS.setStatus("current")
_RttMonJitterStatsNumOfPositivesDS_Type = Counter32
_RttMonJitterStatsNumOfPositivesDS_Object = MibTableColumn
rttMonJitterStatsNumOfPositivesDS = _RttMonJitterStatsNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 24),
    _RttMonJitterStatsNumOfPositivesDS_Type()
)
rttMonJitterStatsNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfPositivesDS.setStatus("current")
_RttMonJitterStatsSumOfPositivesDS_Type = Counter32
_RttMonJitterStatsSumOfPositivesDS_Object = MibTableColumn
rttMonJitterStatsSumOfPositivesDS = _RttMonJitterStatsSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 25),
    _RttMonJitterStatsSumOfPositivesDS_Type()
)
rttMonJitterStatsSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSumOfPositivesDS.setStatus("current")
_RttMonJitterStatsSum2PositivesDSLow_Type = Counter32
_RttMonJitterStatsSum2PositivesDSLow_Object = MibTableColumn
rttMonJitterStatsSum2PositivesDSLow = _RttMonJitterStatsSum2PositivesDSLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 26),
    _RttMonJitterStatsSum2PositivesDSLow_Type()
)
rttMonJitterStatsSum2PositivesDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2PositivesDSLow.setStatus("current")
_RttMonJitterStatsSum2PositivesDSHigh_Type = Counter32
_RttMonJitterStatsSum2PositivesDSHigh_Object = MibTableColumn
rttMonJitterStatsSum2PositivesDSHigh = _RttMonJitterStatsSum2PositivesDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 27),
    _RttMonJitterStatsSum2PositivesDSHigh_Type()
)
rttMonJitterStatsSum2PositivesDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2PositivesDSHigh.setStatus("current")
_RttMonJitterStatsMinOfNegativesDS_Type = Gauge32
_RttMonJitterStatsMinOfNegativesDS_Object = MibTableColumn
rttMonJitterStatsMinOfNegativesDS = _RttMonJitterStatsMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 28),
    _RttMonJitterStatsMinOfNegativesDS_Type()
)
rttMonJitterStatsMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMinOfNegativesDS.setStatus("current")
_RttMonJitterStatsMaxOfNegativesDS_Type = Gauge32
_RttMonJitterStatsMaxOfNegativesDS_Object = MibTableColumn
rttMonJitterStatsMaxOfNegativesDS = _RttMonJitterStatsMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 29),
    _RttMonJitterStatsMaxOfNegativesDS_Type()
)
rttMonJitterStatsMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsMaxOfNegativesDS.setStatus("current")
_RttMonJitterStatsNumOfNegativesDS_Type = Counter32
_RttMonJitterStatsNumOfNegativesDS_Object = MibTableColumn
rttMonJitterStatsNumOfNegativesDS = _RttMonJitterStatsNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 30),
    _RttMonJitterStatsNumOfNegativesDS_Type()
)
rttMonJitterStatsNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsNumOfNegativesDS.setStatus("current")
_RttMonJitterStatsSumOfNegativesDS_Type = Counter32
_RttMonJitterStatsSumOfNegativesDS_Object = MibTableColumn
rttMonJitterStatsSumOfNegativesDS = _RttMonJitterStatsSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 31),
    _RttMonJitterStatsSumOfNegativesDS_Type()
)
rttMonJitterStatsSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSumOfNegativesDS.setStatus("current")
_RttMonJitterStatsSum2NegativesDSLow_Type = Counter32
_RttMonJitterStatsSum2NegativesDSLow_Object = MibTableColumn
rttMonJitterStatsSum2NegativesDSLow = _RttMonJitterStatsSum2NegativesDSLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 32),
    _RttMonJitterStatsSum2NegativesDSLow_Type()
)
rttMonJitterStatsSum2NegativesDSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2NegativesDSLow.setStatus("current")
_RttMonJitterStatsSum2NegativesDSHigh_Type = Counter32
_RttMonJitterStatsSum2NegativesDSHigh_Object = MibTableColumn
rttMonJitterStatsSum2NegativesDSHigh = _RttMonJitterStatsSum2NegativesDSHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 33),
    _RttMonJitterStatsSum2NegativesDSHigh_Type()
)
rttMonJitterStatsSum2NegativesDSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsSum2NegativesDSHigh.setStatus("current")
_RttMonJitterStatsPacketLossSD_Type = Counter32
_RttMonJitterStatsPacketLossSD_Object = MibTableColumn
rttMonJitterStatsPacketLossSD = _RttMonJitterStatsPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 34),
    _RttMonJitterStatsPacketLossSD_Type()
)
rttMonJitterStatsPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsPacketLossSD.setStatus("current")
_RttMonJitterStatsPacketLossDS_Type = Counter32
_RttMonJitterStatsPacketLossDS_Object = MibTableColumn
rttMonJitterStatsPacketLossDS = _RttMonJitterStatsPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 35),
    _RttMonJitterStatsPacketLossDS_Type()
)
rttMonJitterStatsPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsPacketLossDS.setStatus("current")
_RttMonJitterStatsPacketOutOfSequence_Type = Counter32
_RttMonJitterStatsPacketOutOfSequence_Object = MibTableColumn
rttMonJitterStatsPacketOutOfSequence = _RttMonJitterStatsPacketOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 36),
    _RttMonJitterStatsPacketOutOfSequence_Type()
)
rttMonJitterStatsPacketOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsPacketOutOfSequence.setStatus("current")
_RttMonJitterStatsPacketMIA_Type = Counter32
_RttMonJitterStatsPacketMIA_Object = MibTableColumn
rttMonJitterStatsPacketMIA = _RttMonJitterStatsPacketMIA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 37),
    _RttMonJitterStatsPacketMIA_Type()
)
rttMonJitterStatsPacketMIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsPacketMIA.setStatus("current")
_RttMonJitterStatsPacketLateArrival_Type = Counter32
_RttMonJitterStatsPacketLateArrival_Object = MibTableColumn
rttMonJitterStatsPacketLateArrival = _RttMonJitterStatsPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 38),
    _RttMonJitterStatsPacketLateArrival_Type()
)
rttMonJitterStatsPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsPacketLateArrival.setStatus("current")
_RttMonJitterStatsError_Type = Counter32
_RttMonJitterStatsError_Object = MibTableColumn
rttMonJitterStatsError = _RttMonJitterStatsError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 39),
    _RttMonJitterStatsError_Type()
)
rttMonJitterStatsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsError.setStatus("current")
_RttMonJitterStatsBusies_Type = Counter32
_RttMonJitterStatsBusies_Object = MibTableColumn
rttMonJitterStatsBusies = _RttMonJitterStatsBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 3, 5, 1, 40),
    _RttMonJitterStatsBusies_Type()
)
rttMonJitterStatsBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonJitterStatsBusies.setStatus("current")
_RttMonHistory_ObjectIdentity = ObjectIdentity
rttMonHistory = _RttMonHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4)
)
_RttMonHistoryCollectionTable_Object = MibTable
rttMonHistoryCollectionTable = _RttMonHistoryCollectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rttMonHistoryCollectionTable.setStatus("current")
_RttMonHistoryCollectionEntry_Object = MibTableRow
rttMonHistoryCollectionEntry = _RttMonHistoryCollectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1)
)
rttMonHistoryCollectionEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonHistoryCollectionLifeIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonHistoryCollectionBucketIndex"),
    (0, "CISCO-RTTMON-MIB", "rttMonHistoryCollectionSampleIndex"),
)
if mibBuilder.loadTexts:
    rttMonHistoryCollectionEntry.setStatus("current")


class _RttMonHistoryCollectionLifeIndex_Type(Integer32):
    """Custom type rttMonHistoryCollectionLifeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonHistoryCollectionLifeIndex_Type.__name__ = "Integer32"
_RttMonHistoryCollectionLifeIndex_Object = MibTableColumn
rttMonHistoryCollectionLifeIndex = _RttMonHistoryCollectionLifeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 1),
    _RttMonHistoryCollectionLifeIndex_Type()
)
rttMonHistoryCollectionLifeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionLifeIndex.setStatus("current")


class _RttMonHistoryCollectionBucketIndex_Type(Integer32):
    """Custom type rttMonHistoryCollectionBucketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RttMonHistoryCollectionBucketIndex_Type.__name__ = "Integer32"
_RttMonHistoryCollectionBucketIndex_Object = MibTableColumn
rttMonHistoryCollectionBucketIndex = _RttMonHistoryCollectionBucketIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 2),
    _RttMonHistoryCollectionBucketIndex_Type()
)
rttMonHistoryCollectionBucketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionBucketIndex.setStatus("current")


class _RttMonHistoryCollectionSampleIndex_Type(Integer32):
    """Custom type rttMonHistoryCollectionSampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RttMonHistoryCollectionSampleIndex_Type.__name__ = "Integer32"
_RttMonHistoryCollectionSampleIndex_Object = MibTableColumn
rttMonHistoryCollectionSampleIndex = _RttMonHistoryCollectionSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 3),
    _RttMonHistoryCollectionSampleIndex_Type()
)
rttMonHistoryCollectionSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionSampleIndex.setStatus("current")
_RttMonHistoryCollectionSampleTime_Type = TimeStamp
_RttMonHistoryCollectionSampleTime_Object = MibTableColumn
rttMonHistoryCollectionSampleTime = _RttMonHistoryCollectionSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 4),
    _RttMonHistoryCollectionSampleTime_Type()
)
rttMonHistoryCollectionSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionSampleTime.setStatus("current")
_RttMonHistoryCollectionAddress_Type = RttMonTargetAddress
_RttMonHistoryCollectionAddress_Object = MibTableColumn
rttMonHistoryCollectionAddress = _RttMonHistoryCollectionAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 5),
    _RttMonHistoryCollectionAddress_Type()
)
rttMonHistoryCollectionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionAddress.setStatus("current")
_RttMonHistoryCollectionCompletionTime_Type = Gauge32
_RttMonHistoryCollectionCompletionTime_Object = MibTableColumn
rttMonHistoryCollectionCompletionTime = _RttMonHistoryCollectionCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 6),
    _RttMonHistoryCollectionCompletionTime_Type()
)
rttMonHistoryCollectionCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionCompletionTime.setStatus("current")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionCompletionTime.setUnits("milliseconds")
_RttMonHistoryCollectionSense_Type = RttResponseSense
_RttMonHistoryCollectionSense_Object = MibTableColumn
rttMonHistoryCollectionSense = _RttMonHistoryCollectionSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 7),
    _RttMonHistoryCollectionSense_Type()
)
rttMonHistoryCollectionSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionSense.setStatus("current")


class _RttMonHistoryCollectionApplSpecificSense_Type(Integer32):
    """Custom type rttMonHistoryCollectionApplSpecificSense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 2147483647),
    )


_RttMonHistoryCollectionApplSpecificSense_Type.__name__ = "Integer32"
_RttMonHistoryCollectionApplSpecificSense_Object = MibTableColumn
rttMonHistoryCollectionApplSpecificSense = _RttMonHistoryCollectionApplSpecificSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 8),
    _RttMonHistoryCollectionApplSpecificSense_Type()
)
rttMonHistoryCollectionApplSpecificSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionApplSpecificSense.setStatus("current")
_RttMonHistoryCollectionSenseDescription_Type = DisplayString
_RttMonHistoryCollectionSenseDescription_Object = MibTableColumn
rttMonHistoryCollectionSenseDescription = _RttMonHistoryCollectionSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 4, 1, 1, 9),
    _RttMonHistoryCollectionSenseDescription_Type()
)
rttMonHistoryCollectionSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonHistoryCollectionSenseDescription.setStatus("current")
_RttMonLatestOper_ObjectIdentity = ObjectIdentity
rttMonLatestOper = _RttMonLatestOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5)
)
_RttMonLatestHTTPOperTable_Object = MibTable
rttMonLatestHTTPOperTable = _RttMonLatestHTTPOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperTable.setStatus("current")
_RttMonLatestHTTPOperEntry_Object = MibTableRow
rttMonLatestHTTPOperEntry = _RttMonLatestHTTPOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1)
)
rttMonLatestHTTPOperEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperEntry.setStatus("current")
_RttMonLatestHTTPOperRTT_Type = Gauge32
_RttMonLatestHTTPOperRTT_Object = MibTableColumn
rttMonLatestHTTPOperRTT = _RttMonLatestHTTPOperRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 1),
    _RttMonLatestHTTPOperRTT_Type()
)
rttMonLatestHTTPOperRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperRTT.setStatus("current")
_RttMonLatestHTTPOperDNSRTT_Type = Gauge32
_RttMonLatestHTTPOperDNSRTT_Object = MibTableColumn
rttMonLatestHTTPOperDNSRTT = _RttMonLatestHTTPOperDNSRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 2),
    _RttMonLatestHTTPOperDNSRTT_Type()
)
rttMonLatestHTTPOperDNSRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperDNSRTT.setStatus("current")
_RttMonLatestHTTPOperTCPConnectRTT_Type = Gauge32
_RttMonLatestHTTPOperTCPConnectRTT_Object = MibTableColumn
rttMonLatestHTTPOperTCPConnectRTT = _RttMonLatestHTTPOperTCPConnectRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 3),
    _RttMonLatestHTTPOperTCPConnectRTT_Type()
)
rttMonLatestHTTPOperTCPConnectRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperTCPConnectRTT.setStatus("current")
_RttMonLatestHTTPOperTransactionRTT_Type = Gauge32
_RttMonLatestHTTPOperTransactionRTT_Object = MibTableColumn
rttMonLatestHTTPOperTransactionRTT = _RttMonLatestHTTPOperTransactionRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 4),
    _RttMonLatestHTTPOperTransactionRTT_Type()
)
rttMonLatestHTTPOperTransactionRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperTransactionRTT.setStatus("current")
_RttMonLatestHTTPOperMessageBodyOctets_Type = Gauge32
_RttMonLatestHTTPOperMessageBodyOctets_Object = MibTableColumn
rttMonLatestHTTPOperMessageBodyOctets = _RttMonLatestHTTPOperMessageBodyOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 5),
    _RttMonLatestHTTPOperMessageBodyOctets_Type()
)
rttMonLatestHTTPOperMessageBodyOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperMessageBodyOctets.setStatus("current")
_RttMonLatestHTTPOperSense_Type = RttResponseSense
_RttMonLatestHTTPOperSense_Object = MibTableColumn
rttMonLatestHTTPOperSense = _RttMonLatestHTTPOperSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 6),
    _RttMonLatestHTTPOperSense_Type()
)
rttMonLatestHTTPOperSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPOperSense.setStatus("current")
_RttMonLatestHTTPErrorSenseDescription_Type = DisplayString
_RttMonLatestHTTPErrorSenseDescription_Object = MibTableColumn
rttMonLatestHTTPErrorSenseDescription = _RttMonLatestHTTPErrorSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 1, 1, 7),
    _RttMonLatestHTTPErrorSenseDescription_Type()
)
rttMonLatestHTTPErrorSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestHTTPErrorSenseDescription.setStatus("current")
_RttMonLatestJitterOperTable_Object = MibTable
rttMonLatestJitterOperTable = _RttMonLatestJitterOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2)
)
if mibBuilder.loadTexts:
    rttMonLatestJitterOperTable.setStatus("current")
_RttMonLatestJitterOperEntry_Object = MibTableRow
rttMonLatestJitterOperEntry = _RttMonLatestJitterOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1)
)
rttMonLatestJitterOperEntry.setIndexNames(
    (0, "CISCO-RTTMON-MIB", "rttMonCtrlAdminIndex"),
)
if mibBuilder.loadTexts:
    rttMonLatestJitterOperEntry.setStatus("current")
_RttMonLatestJitterOperNumOfRTT_Type = Gauge32
_RttMonLatestJitterOperNumOfRTT_Object = MibTableColumn
rttMonLatestJitterOperNumOfRTT = _RttMonLatestJitterOperNumOfRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 1),
    _RttMonLatestJitterOperNumOfRTT_Type()
)
rttMonLatestJitterOperNumOfRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfRTT.setStatus("current")
_RttMonLatestJitterOperRTTSum_Type = Gauge32
_RttMonLatestJitterOperRTTSum_Object = MibTableColumn
rttMonLatestJitterOperRTTSum = _RttMonLatestJitterOperRTTSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 2),
    _RttMonLatestJitterOperRTTSum_Type()
)
rttMonLatestJitterOperRTTSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperRTTSum.setStatus("current")
_RttMonLatestJitterOperRTTSum2_Type = Gauge32
_RttMonLatestJitterOperRTTSum2_Object = MibTableColumn
rttMonLatestJitterOperRTTSum2 = _RttMonLatestJitterOperRTTSum2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 3),
    _RttMonLatestJitterOperRTTSum2_Type()
)
rttMonLatestJitterOperRTTSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperRTTSum2.setStatus("current")
_RttMonLatestJitterOperRTTMin_Type = Gauge32
_RttMonLatestJitterOperRTTMin_Object = MibTableColumn
rttMonLatestJitterOperRTTMin = _RttMonLatestJitterOperRTTMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 4),
    _RttMonLatestJitterOperRTTMin_Type()
)
rttMonLatestJitterOperRTTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperRTTMin.setStatus("current")
_RttMonLatestJitterOperRTTMax_Type = Gauge32
_RttMonLatestJitterOperRTTMax_Object = MibTableColumn
rttMonLatestJitterOperRTTMax = _RttMonLatestJitterOperRTTMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 5),
    _RttMonLatestJitterOperRTTMax_Type()
)
rttMonLatestJitterOperRTTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperRTTMax.setStatus("current")
_RttMonLatestJitterOperMinOfPositivesSD_Type = Gauge32
_RttMonLatestJitterOperMinOfPositivesSD_Object = MibTableColumn
rttMonLatestJitterOperMinOfPositivesSD = _RttMonLatestJitterOperMinOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 6),
    _RttMonLatestJitterOperMinOfPositivesSD_Type()
)
rttMonLatestJitterOperMinOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMinOfPositivesSD.setStatus("current")
_RttMonLatestJitterOperMaxOfPositivesSD_Type = Gauge32
_RttMonLatestJitterOperMaxOfPositivesSD_Object = MibTableColumn
rttMonLatestJitterOperMaxOfPositivesSD = _RttMonLatestJitterOperMaxOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 7),
    _RttMonLatestJitterOperMaxOfPositivesSD_Type()
)
rttMonLatestJitterOperMaxOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMaxOfPositivesSD.setStatus("current")
_RttMonLatestJitterOperNumOfPositivesSD_Type = Gauge32
_RttMonLatestJitterOperNumOfPositivesSD_Object = MibTableColumn
rttMonLatestJitterOperNumOfPositivesSD = _RttMonLatestJitterOperNumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 8),
    _RttMonLatestJitterOperNumOfPositivesSD_Type()
)
rttMonLatestJitterOperNumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfPositivesSD.setStatus("current")
_RttMonLatestJitterOperSumOfPositivesSD_Type = Gauge32
_RttMonLatestJitterOperSumOfPositivesSD_Object = MibTableColumn
rttMonLatestJitterOperSumOfPositivesSD = _RttMonLatestJitterOperSumOfPositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 9),
    _RttMonLatestJitterOperSumOfPositivesSD_Type()
)
rttMonLatestJitterOperSumOfPositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSumOfPositivesSD.setStatus("current")
_RttMonLatestJitterOperSum2PositivesSD_Type = Gauge32
_RttMonLatestJitterOperSum2PositivesSD_Object = MibTableColumn
rttMonLatestJitterOperSum2PositivesSD = _RttMonLatestJitterOperSum2PositivesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 10),
    _RttMonLatestJitterOperSum2PositivesSD_Type()
)
rttMonLatestJitterOperSum2PositivesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSum2PositivesSD.setStatus("current")
_RttMonLatestJitterOperMinOfNegativesSD_Type = Gauge32
_RttMonLatestJitterOperMinOfNegativesSD_Object = MibTableColumn
rttMonLatestJitterOperMinOfNegativesSD = _RttMonLatestJitterOperMinOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 11),
    _RttMonLatestJitterOperMinOfNegativesSD_Type()
)
rttMonLatestJitterOperMinOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMinOfNegativesSD.setStatus("current")
_RttMonLatestJitterOperMaxOfNegativesSD_Type = Gauge32
_RttMonLatestJitterOperMaxOfNegativesSD_Object = MibTableColumn
rttMonLatestJitterOperMaxOfNegativesSD = _RttMonLatestJitterOperMaxOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 12),
    _RttMonLatestJitterOperMaxOfNegativesSD_Type()
)
rttMonLatestJitterOperMaxOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMaxOfNegativesSD.setStatus("current")
_RttMonLatestJitterOperNumOfNegativesSD_Type = Gauge32
_RttMonLatestJitterOperNumOfNegativesSD_Object = MibTableColumn
rttMonLatestJitterOperNumOfNegativesSD = _RttMonLatestJitterOperNumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 13),
    _RttMonLatestJitterOperNumOfNegativesSD_Type()
)
rttMonLatestJitterOperNumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfNegativesSD.setStatus("current")
_RttMonLatestJitterOperSumOfNegativesSD_Type = Gauge32
_RttMonLatestJitterOperSumOfNegativesSD_Object = MibTableColumn
rttMonLatestJitterOperSumOfNegativesSD = _RttMonLatestJitterOperSumOfNegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 14),
    _RttMonLatestJitterOperSumOfNegativesSD_Type()
)
rttMonLatestJitterOperSumOfNegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSumOfNegativesSD.setStatus("current")
_RttMonLatestJitterOperSum2NegativesSD_Type = Gauge32
_RttMonLatestJitterOperSum2NegativesSD_Object = MibTableColumn
rttMonLatestJitterOperSum2NegativesSD = _RttMonLatestJitterOperSum2NegativesSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 15),
    _RttMonLatestJitterOperSum2NegativesSD_Type()
)
rttMonLatestJitterOperSum2NegativesSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSum2NegativesSD.setStatus("current")
_RttMonLatestJitterOperMinOfPositivesDS_Type = Gauge32
_RttMonLatestJitterOperMinOfPositivesDS_Object = MibTableColumn
rttMonLatestJitterOperMinOfPositivesDS = _RttMonLatestJitterOperMinOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 16),
    _RttMonLatestJitterOperMinOfPositivesDS_Type()
)
rttMonLatestJitterOperMinOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMinOfPositivesDS.setStatus("current")
_RttMonLatestJitterOperMaxOfPositivesDS_Type = Gauge32
_RttMonLatestJitterOperMaxOfPositivesDS_Object = MibTableColumn
rttMonLatestJitterOperMaxOfPositivesDS = _RttMonLatestJitterOperMaxOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 17),
    _RttMonLatestJitterOperMaxOfPositivesDS_Type()
)
rttMonLatestJitterOperMaxOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMaxOfPositivesDS.setStatus("current")
_RttMonLatestJitterOperNumOfPositivesDS_Type = Gauge32
_RttMonLatestJitterOperNumOfPositivesDS_Object = MibTableColumn
rttMonLatestJitterOperNumOfPositivesDS = _RttMonLatestJitterOperNumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 18),
    _RttMonLatestJitterOperNumOfPositivesDS_Type()
)
rttMonLatestJitterOperNumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfPositivesDS.setStatus("current")
_RttMonLatestJitterOperSumOfPositivesDS_Type = Gauge32
_RttMonLatestJitterOperSumOfPositivesDS_Object = MibTableColumn
rttMonLatestJitterOperSumOfPositivesDS = _RttMonLatestJitterOperSumOfPositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 19),
    _RttMonLatestJitterOperSumOfPositivesDS_Type()
)
rttMonLatestJitterOperSumOfPositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSumOfPositivesDS.setStatus("current")
_RttMonLatestJitterOperSum2PositivesDS_Type = Gauge32
_RttMonLatestJitterOperSum2PositivesDS_Object = MibTableColumn
rttMonLatestJitterOperSum2PositivesDS = _RttMonLatestJitterOperSum2PositivesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 20),
    _RttMonLatestJitterOperSum2PositivesDS_Type()
)
rttMonLatestJitterOperSum2PositivesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSum2PositivesDS.setStatus("current")
_RttMonLatestJitterOperMinOfNegativesDS_Type = Gauge32
_RttMonLatestJitterOperMinOfNegativesDS_Object = MibTableColumn
rttMonLatestJitterOperMinOfNegativesDS = _RttMonLatestJitterOperMinOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 21),
    _RttMonLatestJitterOperMinOfNegativesDS_Type()
)
rttMonLatestJitterOperMinOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMinOfNegativesDS.setStatus("current")
_RttMonLatestJitterOperMaxOfNegativesDS_Type = Gauge32
_RttMonLatestJitterOperMaxOfNegativesDS_Object = MibTableColumn
rttMonLatestJitterOperMaxOfNegativesDS = _RttMonLatestJitterOperMaxOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 22),
    _RttMonLatestJitterOperMaxOfNegativesDS_Type()
)
rttMonLatestJitterOperMaxOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperMaxOfNegativesDS.setStatus("current")
_RttMonLatestJitterOperNumOfNegativesDS_Type = Gauge32
_RttMonLatestJitterOperNumOfNegativesDS_Object = MibTableColumn
rttMonLatestJitterOperNumOfNegativesDS = _RttMonLatestJitterOperNumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 23),
    _RttMonLatestJitterOperNumOfNegativesDS_Type()
)
rttMonLatestJitterOperNumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperNumOfNegativesDS.setStatus("current")
_RttMonLatestJitterOperSumOfNegativesDS_Type = Gauge32
_RttMonLatestJitterOperSumOfNegativesDS_Object = MibTableColumn
rttMonLatestJitterOperSumOfNegativesDS = _RttMonLatestJitterOperSumOfNegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 24),
    _RttMonLatestJitterOperSumOfNegativesDS_Type()
)
rttMonLatestJitterOperSumOfNegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSumOfNegativesDS.setStatus("current")
_RttMonLatestJitterOperSum2NegativesDS_Type = Gauge32
_RttMonLatestJitterOperSum2NegativesDS_Object = MibTableColumn
rttMonLatestJitterOperSum2NegativesDS = _RttMonLatestJitterOperSum2NegativesDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 25),
    _RttMonLatestJitterOperSum2NegativesDS_Type()
)
rttMonLatestJitterOperSum2NegativesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSum2NegativesDS.setStatus("current")
_RttMonLatestJitterOperPacketLossSD_Type = Gauge32
_RttMonLatestJitterOperPacketLossSD_Object = MibTableColumn
rttMonLatestJitterOperPacketLossSD = _RttMonLatestJitterOperPacketLossSD_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 26),
    _RttMonLatestJitterOperPacketLossSD_Type()
)
rttMonLatestJitterOperPacketLossSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperPacketLossSD.setStatus("current")
_RttMonLatestJitterOperPacketLossDS_Type = Gauge32
_RttMonLatestJitterOperPacketLossDS_Object = MibTableColumn
rttMonLatestJitterOperPacketLossDS = _RttMonLatestJitterOperPacketLossDS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 27),
    _RttMonLatestJitterOperPacketLossDS_Type()
)
rttMonLatestJitterOperPacketLossDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperPacketLossDS.setStatus("current")
_RttMonLatestJitterOperPacketOutOfSequence_Type = Gauge32
_RttMonLatestJitterOperPacketOutOfSequence_Object = MibTableColumn
rttMonLatestJitterOperPacketOutOfSequence = _RttMonLatestJitterOperPacketOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 28),
    _RttMonLatestJitterOperPacketOutOfSequence_Type()
)
rttMonLatestJitterOperPacketOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperPacketOutOfSequence.setStatus("current")
_RttMonLatestJitterOperPacketMIA_Type = Gauge32
_RttMonLatestJitterOperPacketMIA_Object = MibTableColumn
rttMonLatestJitterOperPacketMIA = _RttMonLatestJitterOperPacketMIA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 29),
    _RttMonLatestJitterOperPacketMIA_Type()
)
rttMonLatestJitterOperPacketMIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperPacketMIA.setStatus("current")
_RttMonLatestJitterOperPacketLateArrival_Type = Gauge32
_RttMonLatestJitterOperPacketLateArrival_Object = MibTableColumn
rttMonLatestJitterOperPacketLateArrival = _RttMonLatestJitterOperPacketLateArrival_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 30),
    _RttMonLatestJitterOperPacketLateArrival_Type()
)
rttMonLatestJitterOperPacketLateArrival.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperPacketLateArrival.setStatus("current")
_RttMonLatestJitterOperSense_Type = RttResponseSense
_RttMonLatestJitterOperSense_Object = MibTableColumn
rttMonLatestJitterOperSense = _RttMonLatestJitterOperSense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 31),
    _RttMonLatestJitterOperSense_Type()
)
rttMonLatestJitterOperSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterOperSense.setStatus("current")
_RttMonLatestJitterErrorSenseDescription_Type = DisplayString
_RttMonLatestJitterErrorSenseDescription_Object = MibTableColumn
rttMonLatestJitterErrorSenseDescription = _RttMonLatestJitterErrorSenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 1, 5, 2, 1, 32),
    _RttMonLatestJitterErrorSenseDescription_Type()
)
rttMonLatestJitterErrorSenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rttMonLatestJitterErrorSenseDescription.setStatus("current")
_RttMonNotificationsPrefix_ObjectIdentity = ObjectIdentity
rttMonNotificationsPrefix = _RttMonNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2)
)
_RttMonNotifications_ObjectIdentity = ObjectIdentity
rttMonNotifications = _RttMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0)
)
_CiscoRttMonMibConformance_ObjectIdentity = ObjectIdentity
ciscoRttMonMibConformance = _CiscoRttMonMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3)
)
_CiscoRttMonMibCompliances_ObjectIdentity = ObjectIdentity
ciscoRttMonMibCompliances = _CiscoRttMonMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1)
)
_CiscoRttMonMibGroups_ObjectIdentity = ObjectIdentity
ciscoRttMonMibGroups = _CiscoRttMonMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2)
)
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonScheduleAdminEntry")
)
rttMonScheduleAdminEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonReactAdminEntry")
)
rttMonReactAdminEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonStatisticsAdminEntry")
)
rttMonStatisticsAdminEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonHistoryAdminEntry")
)
rttMonHistoryAdminEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonCtrlOperEntry")
)
rttMonCtrlOperEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonCtrlAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonLatestRttOperEntry")
)
rttMonLatestRttOperEntry.setIndexNames(*rttMonCtrlAdminEntry.getIndexNames())
rttMonReactTriggerAdminEntry.registerAugmentions(
    ("CISCO-RTTMON-MIB",
     "rttMonReactTriggerOperEntry")
)
rttMonReactTriggerOperEntry.setIndexNames(*rttMonReactTriggerAdminEntry.getIndexNames())

# Managed Objects groups

ciscoApplGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 1)
)
ciscoApplGroup.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonApplVersion"),
        ("CISCO-RTTMON-MIB", "rttMonApplMaxPacketDataSize"),
        ("CISCO-RTTMON-MIB", "rttMonApplTimeOfLastSet"),
        ("CISCO-RTTMON-MIB", "rttMonApplSupportedRttTypesValid"),
        ("CISCO-RTTMON-MIB", "rttMonApplSupportedProtocolsValid"),
        ("CISCO-RTTMON-MIB", "rttMonApplNumCtrlAdminEntry"),
        ("CISCO-RTTMON-MIB", "rttMonApplReset"),
        ("CISCO-RTTMON-MIB", "rttMonApplPreConfigedReset"),
        ("CISCO-RTTMON-MIB", "rttMonApplPreConfigedValid"),
        ("CISCO-RTTMON-MIB", "rttMonApplProbeCapacity"),
        ("CISCO-RTTMON-MIB", "rttMonApplFreeMemLowWaterMark"),
        ("CISCO-RTTMON-MIB", "rttMonApplLatestSetError"))
)
if mibBuilder.loadTexts:
    ciscoApplGroup.setStatus("obsolete")

ciscoCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 2)
)
ciscoCtrlGroup.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminOwner"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminRttType"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminThreshold"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminFrequency"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminVerifyData"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminStatus"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminProtocol"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetAddress"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminPktDataRequestSize"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminPktDataResponseSize"),
        ("CISCO-RTTMON-MIB", "rttMonFileIOAdminFilePath"),
        ("CISCO-RTTMON-MIB", "rttMonFileIOAdminSize"),
        ("CISCO-RTTMON-MIB", "rttMonFileIOAdminAction"),
        ("CISCO-RTTMON-MIB", "rttMonScriptAdminName"),
        ("CISCO-RTTMON-MIB", "rttMonScriptAdminCmdLineParams"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminRttLife"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminRttStartTime"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminConceptRowAgeout"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminConnectionEnable"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminTimeoutEnable"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdType"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdFalling"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdCount"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdCount2"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminActionType"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumHourGroups"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumPaths"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumHops"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumDistBuckets"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminDistInterval"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumLives"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumBuckets"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumSamples"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminFilter"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperModificationTime"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperDiagText"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperResetTime"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperOctetsInUse"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperConnectionLostOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperTimeoutOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperOverThresholdOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperNumRtts"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperRttLife"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperState"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperCompletionTime"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperApplSpecificSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperSenseDescription"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperTime"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperAddress"),
        ("CISCO-RTTMON-MIB", "rttMonReactTriggerAdminStatus"),
        ("CISCO-RTTMON-MIB", "rttMonReactTriggerOperState"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroup.setStatus("obsolete")

ciscoStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 3)
)
ciscoStatsGroup.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonStatsCaptureCompletions"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureOverThresholds"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureSumCompletionTime"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureSumCompletionTime2Low"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureSumCompletionTime2High"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureCompletionTimeMax"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCaptureCompletionTimeMin"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectNumDisconnects"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectTimeouts"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectBusies"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectNoConnections"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectDrops"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectSequenceErrors"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectVerifyErrors"),
        ("CISCO-RTTMON-MIB", "rttMonStatsCollectAddress"),
        ("CISCO-RTTMON-MIB", "rttMonStatsTotalsElapsedTime"),
        ("CISCO-RTTMON-MIB", "rttMonStatsTotalsInitiations"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroup.setStatus("current")

ciscoHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 4)
)
ciscoHistoryGroup.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonHistoryCollectionSampleTime"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionCompletionTime"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionSense"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionApplSpecificSense"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionSenseDescription"))
)
if mibBuilder.loadTexts:
    ciscoHistoryGroup.setStatus("current")

ciscoCtrlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 5)
)
ciscoCtrlGroupRev1.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetPort"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminSourceAddress"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminSourcePort"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminControlEnable"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminTOS"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminLSREnable"),
        ("CISCO-RTTMON-MIB", "rttMonEchoPathAdminHopAddress"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev1.setStatus("current")

ciscoCtrlGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 6)
)
ciscoCtrlGroupRev2.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetAddressString"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminNameServer"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminOperation"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminHTTPVersion"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminURL"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminCache"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminInterval"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminNumPackets"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminProxy"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminString1"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminString2"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminString3"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminString4"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminString5"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev2.setStatus("current")

ciscoLatestOperGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 7)
)
ciscoLatestOperGroupRev1.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperDNSRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperTCPConnectRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperTransactionRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperMessageBodyOctets"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPOperSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestHTTPErrorSenseDescription"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfRTT"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperRTTSum2"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperRTTMin"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperRTTMax"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMinOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMaxOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSumOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSum2PositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMinOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMaxOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSumOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSum2NegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMinOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMaxOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSumOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSum2PositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMinOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperMaxOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperNumOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSumOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSum2NegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperPacketLossSD"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperPacketLossDS"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperPacketOutOfSequence"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperPacketMIA"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperPacketLateArrival"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterOperSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestJitterErrorSenseDescription"))
)
if mibBuilder.loadTexts:
    ciscoLatestOperGroupRev1.setStatus("current")

ciscoStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 8)
)
ciscoStatsGroupRev1.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonHTTPStatsCompletions"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsOverThresholds"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsRTTSum2Low"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsRTTSum2High"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsRTTMin"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsRTTMax"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsDNSRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsTCPConnectRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsTransactionRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsMessageBodyOctetsSum"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsDNSServerTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsTCPConnectTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsTransactionTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsDNSQueryError"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsHTTPError"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsError"),
        ("CISCO-RTTMON-MIB", "rttMonHTTPStatsBusies"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsCompletions"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsOverThresholds"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfRTT"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTSum"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTSum2Low"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTSum2High"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTMin"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsRTTMax"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMinOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMaxOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSumOfPositivesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2PositivesSDLow"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2PositivesSDHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMinOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMaxOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSumOfNegativesSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2NegativesSDLow"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2NegativesSDHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMinOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMaxOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSumOfPositivesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2PositivesDSLow"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2PositivesDSHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMinOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsMaxOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsNumOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSumOfNegativesDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2NegativesDSLow"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsSum2NegativesDSHigh"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsPacketLossSD"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsPacketLossDS"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsPacketOutOfSequence"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsPacketMIA"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsPacketLateArrival"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsError"),
        ("CISCO-RTTMON-MIB", "rttMonJitterStatsBusies"))
)
if mibBuilder.loadTexts:
    ciscoStatsGroupRev1.setStatus("current")

ciscoApplGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 9)
)
ciscoApplGroupRev1.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonApplVersion"),
        ("CISCO-RTTMON-MIB", "rttMonApplMaxPacketDataSize"),
        ("CISCO-RTTMON-MIB", "rttMonApplTimeOfLastSet"),
        ("CISCO-RTTMON-MIB", "rttMonApplSupportedRttTypesValid"),
        ("CISCO-RTTMON-MIB", "rttMonApplSupportedProtocolsValid"),
        ("CISCO-RTTMON-MIB", "rttMonApplNumCtrlAdminEntry"),
        ("CISCO-RTTMON-MIB", "rttMonApplReset"))
)
if mibBuilder.loadTexts:
    ciscoApplGroupRev1.setStatus("current")

ciscoCtrlGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 2, 10)
)
ciscoCtrlGroupRev3.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminOwner"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminRttType"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminThreshold"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminFrequency"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminTimeout"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminVerifyData"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminStatus"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlAdminNvgen"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminProtocol"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminTargetAddress"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminPktDataRequestSize"),
        ("CISCO-RTTMON-MIB", "rttMonEchoAdminPktDataResponseSize"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminRttLife"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminRttStartTime"),
        ("CISCO-RTTMON-MIB", "rttMonScheduleAdminConceptRowAgeout"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminConnectionEnable"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminTimeoutEnable"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdType"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdFalling"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdCount"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminThresholdCount2"),
        ("CISCO-RTTMON-MIB", "rttMonReactAdminActionType"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumHourGroups"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumPaths"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumHops"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminNumDistBuckets"),
        ("CISCO-RTTMON-MIB", "rttMonStatisticsAdminDistInterval"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumLives"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumBuckets"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminNumSamples"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryAdminFilter"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperModificationTime"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperDiagText"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperResetTime"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperOctetsInUse"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperConnectionLostOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperTimeoutOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperOverThresholdOccurred"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperNumRtts"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperRttLife"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperState"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperCompletionTime"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperApplSpecificSense"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperSenseDescription"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperTime"),
        ("CISCO-RTTMON-MIB", "rttMonLatestRttOperAddress"),
        ("CISCO-RTTMON-MIB", "rttMonReactTriggerAdminStatus"),
        ("CISCO-RTTMON-MIB", "rttMonReactTriggerOperState"))
)
if mibBuilder.loadTexts:
    ciscoCtrlGroupRev3.setStatus("current")


# Notification objects

rttMonConnectionChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 1)
)
rttMonConnectionChangeNotification.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperConnectionLostOccurred"))
)
if mibBuilder.loadTexts:
    rttMonConnectionChangeNotification.setStatus(
        "current"
    )

rttMonTimeoutNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 2)
)
rttMonTimeoutNotification.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperTimeoutOccurred"))
)
if mibBuilder.loadTexts:
    rttMonTimeoutNotification.setStatus(
        "current"
    )

rttMonThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 2, 0, 3)
)
rttMonThresholdNotification.setObjects(
      *(("CISCO-RTTMON-MIB", "rttMonCtrlAdminTag"),
        ("CISCO-RTTMON-MIB", "rttMonHistoryCollectionAddress"),
        ("CISCO-RTTMON-MIB", "rttMonCtrlOperOverThresholdOccurred"))
)
if mibBuilder.loadTexts:
    rttMonThresholdNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoRttMonMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 1)
)
ciscoRttMonMibCompliance.setObjects(
      *(("CISCO-RTTMON-MIB", "ciscoApplGroup"),
        ("CISCO-RTTMON-MIB", "ciscoCtrlGroup"),
        ("CISCO-RTTMON-MIB", "ciscoStatsGroup"),
        ("CISCO-RTTMON-MIB", "ciscoHistoryGroup"))
)
if mibBuilder.loadTexts:
    ciscoRttMonMibCompliance.setStatus(
        "obsolete"
    )

ciscoRttMonMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 2)
)
ciscoRttMonMibComplianceRev1.setObjects(
      *(("CISCO-RTTMON-MIB", "ciscoApplGroup"),
        ("CISCO-RTTMON-MIB", "ciscoCtrlGroup"),
        ("CISCO-RTTMON-MIB", "ciscoStatsGroup"),
        ("CISCO-RTTMON-MIB", "ciscoHistoryGroup"),
        ("CISCO-RTTMON-MIB", "ciscoCtrlGroupRev1"))
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev1.setStatus(
        "obsolete"
    )

ciscoRttMonMibComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 3)
)
ciscoRttMonMibComplianceRev2.setObjects(
      *(("CISCO-RTTMON-MIB", "ciscoApplGroup"),
        ("CISCO-RTTMON-MIB", "ciscoCtrlGroup"),
        ("CISCO-RTTMON-MIB", "ciscoStatsGroup"),
        ("CISCO-RTTMON-MIB", "ciscoHistoryGroup"),
        ("CISCO-RTTMON-MIB", "ciscoCtrlGroupRev1"),
        ("CISCO-RTTMON-MIB", "ciscoCtrlGroupRev2"),
        ("CISCO-RTTMON-MIB", "ciscoLatestOperGroupRev1"),
        ("CISCO-RTTMON-MIB", "ciscoStatsGroupRev1"))
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev2.setStatus(
        "obsolete"
    )

ciscoRttMonMibComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 42, 3, 1, 4)
)
ciscoRttMonMibComplianceRev3.setObjects(
      *(("CISCO-RTTMON-MIB", "ciscoApplGroupRev1"),
        ("CISCO-RTTMON-MIB", "ciscoCtrlGroupRev3"),
        ("CISCO-RTTMON-MIB", "ciscoStatsGroup"),
        ("CISCO-RTTMON-MIB", "ciscoHistoryGroup"),
        ("CISCO-RTTMON-MIB", "ciscoCtrlGroupRev1"),
        ("CISCO-RTTMON-MIB", "ciscoCtrlGroupRev2"),
        ("CISCO-RTTMON-MIB", "ciscoLatestOperGroupRev1"),
        ("CISCO-RTTMON-MIB", "ciscoStatsGroupRev1"))
)
if mibBuilder.loadTexts:
    ciscoRttMonMibComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RTTMON-MIB",
    **{"RttReset": RttReset,
       "RttMonOperation": RttMonOperation,
       "RttResponseSense": RttResponseSense,
       "RttMonRttType": RttMonRttType,
       "RttMonProtocol": RttMonProtocol,
       "RttMonTargetAddress": RttMonTargetAddress,
       "ciscoRttMonMIB": ciscoRttMonMIB,
       "ciscoRttMonObjects": ciscoRttMonObjects,
       "rttMonAppl": rttMonAppl,
       "rttMonApplVersion": rttMonApplVersion,
       "rttMonApplMaxPacketDataSize": rttMonApplMaxPacketDataSize,
       "rttMonApplTimeOfLastSet": rttMonApplTimeOfLastSet,
       "rttMonApplNumCtrlAdminEntry": rttMonApplNumCtrlAdminEntry,
       "rttMonApplReset": rttMonApplReset,
       "rttMonApplPreConfigedReset": rttMonApplPreConfigedReset,
       "rttMonApplSupportedRttTypesTable": rttMonApplSupportedRttTypesTable,
       "rttMonApplSupportedRttTypesEntry": rttMonApplSupportedRttTypesEntry,
       "rttMonApplSupportedRttTypes": rttMonApplSupportedRttTypes,
       "rttMonApplSupportedRttTypesValid": rttMonApplSupportedRttTypesValid,
       "rttMonApplSupportedProtocolsTable": rttMonApplSupportedProtocolsTable,
       "rttMonApplSupportedProtocolsEntry": rttMonApplSupportedProtocolsEntry,
       "rttMonApplSupportedProtocols": rttMonApplSupportedProtocols,
       "rttMonApplSupportedProtocolsValid": rttMonApplSupportedProtocolsValid,
       "rttMonApplPreConfigedTable": rttMonApplPreConfigedTable,
       "rttMonApplPreConfigedEntry": rttMonApplPreConfigedEntry,
       "rttMonApplPreConfigedType": rttMonApplPreConfigedType,
       "rttMonApplPreConfigedName": rttMonApplPreConfigedName,
       "rttMonApplPreConfigedValid": rttMonApplPreConfigedValid,
       "rttMonApplProbeCapacity": rttMonApplProbeCapacity,
       "rttMonApplFreeMemLowWaterMark": rttMonApplFreeMemLowWaterMark,
       "rttMonApplLatestSetError": rttMonApplLatestSetError,
       "rttMonCtrl": rttMonCtrl,
       "rttMonCtrlAdminTable": rttMonCtrlAdminTable,
       "rttMonCtrlAdminEntry": rttMonCtrlAdminEntry,
       "rttMonCtrlAdminIndex": rttMonCtrlAdminIndex,
       "rttMonCtrlAdminOwner": rttMonCtrlAdminOwner,
       "rttMonCtrlAdminTag": rttMonCtrlAdminTag,
       "rttMonCtrlAdminRttType": rttMonCtrlAdminRttType,
       "rttMonCtrlAdminThreshold": rttMonCtrlAdminThreshold,
       "rttMonCtrlAdminFrequency": rttMonCtrlAdminFrequency,
       "rttMonCtrlAdminTimeout": rttMonCtrlAdminTimeout,
       "rttMonCtrlAdminVerifyData": rttMonCtrlAdminVerifyData,
       "rttMonCtrlAdminStatus": rttMonCtrlAdminStatus,
       "rttMonCtrlAdminNvgen": rttMonCtrlAdminNvgen,
       "rttMonEchoAdminTable": rttMonEchoAdminTable,
       "rttMonEchoAdminEntry": rttMonEchoAdminEntry,
       "rttMonEchoAdminProtocol": rttMonEchoAdminProtocol,
       "rttMonEchoAdminTargetAddress": rttMonEchoAdminTargetAddress,
       "rttMonEchoAdminPktDataRequestSize": rttMonEchoAdminPktDataRequestSize,
       "rttMonEchoAdminPktDataResponseSize": rttMonEchoAdminPktDataResponseSize,
       "rttMonEchoAdminTargetPort": rttMonEchoAdminTargetPort,
       "rttMonEchoAdminSourceAddress": rttMonEchoAdminSourceAddress,
       "rttMonEchoAdminSourcePort": rttMonEchoAdminSourcePort,
       "rttMonEchoAdminControlEnable": rttMonEchoAdminControlEnable,
       "rttMonEchoAdminTOS": rttMonEchoAdminTOS,
       "rttMonEchoAdminLSREnable": rttMonEchoAdminLSREnable,
       "rttMonEchoAdminTargetAddressString": rttMonEchoAdminTargetAddressString,
       "rttMonEchoAdminNameServer": rttMonEchoAdminNameServer,
       "rttMonEchoAdminOperation": rttMonEchoAdminOperation,
       "rttMonEchoAdminHTTPVersion": rttMonEchoAdminHTTPVersion,
       "rttMonEchoAdminURL": rttMonEchoAdminURL,
       "rttMonEchoAdminCache": rttMonEchoAdminCache,
       "rttMonEchoAdminInterval": rttMonEchoAdminInterval,
       "rttMonEchoAdminNumPackets": rttMonEchoAdminNumPackets,
       "rttMonEchoAdminProxy": rttMonEchoAdminProxy,
       "rttMonEchoAdminString1": rttMonEchoAdminString1,
       "rttMonEchoAdminString2": rttMonEchoAdminString2,
       "rttMonEchoAdminString3": rttMonEchoAdminString3,
       "rttMonEchoAdminString4": rttMonEchoAdminString4,
       "rttMonEchoAdminString5": rttMonEchoAdminString5,
       "rttMonFileIOAdminTable": rttMonFileIOAdminTable,
       "rttMonFileIOAdminEntry": rttMonFileIOAdminEntry,
       "rttMonFileIOAdminFilePath": rttMonFileIOAdminFilePath,
       "rttMonFileIOAdminSize": rttMonFileIOAdminSize,
       "rttMonFileIOAdminAction": rttMonFileIOAdminAction,
       "rttMonScriptAdminTable": rttMonScriptAdminTable,
       "rttMonScriptAdminEntry": rttMonScriptAdminEntry,
       "rttMonScriptAdminName": rttMonScriptAdminName,
       "rttMonScriptAdminCmdLineParams": rttMonScriptAdminCmdLineParams,
       "rttMonScheduleAdminTable": rttMonScheduleAdminTable,
       "rttMonScheduleAdminEntry": rttMonScheduleAdminEntry,
       "rttMonScheduleAdminRttLife": rttMonScheduleAdminRttLife,
       "rttMonScheduleAdminRttStartTime": rttMonScheduleAdminRttStartTime,
       "rttMonScheduleAdminConceptRowAgeout": rttMonScheduleAdminConceptRowAgeout,
       "rttMonReactAdminTable": rttMonReactAdminTable,
       "rttMonReactAdminEntry": rttMonReactAdminEntry,
       "rttMonReactAdminConnectionEnable": rttMonReactAdminConnectionEnable,
       "rttMonReactAdminTimeoutEnable": rttMonReactAdminTimeoutEnable,
       "rttMonReactAdminThresholdType": rttMonReactAdminThresholdType,
       "rttMonReactAdminThresholdFalling": rttMonReactAdminThresholdFalling,
       "rttMonReactAdminThresholdCount": rttMonReactAdminThresholdCount,
       "rttMonReactAdminThresholdCount2": rttMonReactAdminThresholdCount2,
       "rttMonReactAdminActionType": rttMonReactAdminActionType,
       "rttMonStatisticsAdminTable": rttMonStatisticsAdminTable,
       "rttMonStatisticsAdminEntry": rttMonStatisticsAdminEntry,
       "rttMonStatisticsAdminNumHourGroups": rttMonStatisticsAdminNumHourGroups,
       "rttMonStatisticsAdminNumPaths": rttMonStatisticsAdminNumPaths,
       "rttMonStatisticsAdminNumHops": rttMonStatisticsAdminNumHops,
       "rttMonStatisticsAdminNumDistBuckets": rttMonStatisticsAdminNumDistBuckets,
       "rttMonStatisticsAdminDistInterval": rttMonStatisticsAdminDistInterval,
       "rttMonHistoryAdminTable": rttMonHistoryAdminTable,
       "rttMonHistoryAdminEntry": rttMonHistoryAdminEntry,
       "rttMonHistoryAdminNumLives": rttMonHistoryAdminNumLives,
       "rttMonHistoryAdminNumBuckets": rttMonHistoryAdminNumBuckets,
       "rttMonHistoryAdminNumSamples": rttMonHistoryAdminNumSamples,
       "rttMonHistoryAdminFilter": rttMonHistoryAdminFilter,
       "rttMonCtrlOperTable": rttMonCtrlOperTable,
       "rttMonCtrlOperEntry": rttMonCtrlOperEntry,
       "rttMonCtrlOperModificationTime": rttMonCtrlOperModificationTime,
       "rttMonCtrlOperDiagText": rttMonCtrlOperDiagText,
       "rttMonCtrlOperResetTime": rttMonCtrlOperResetTime,
       "rttMonCtrlOperOctetsInUse": rttMonCtrlOperOctetsInUse,
       "rttMonCtrlOperConnectionLostOccurred": rttMonCtrlOperConnectionLostOccurred,
       "rttMonCtrlOperTimeoutOccurred": rttMonCtrlOperTimeoutOccurred,
       "rttMonCtrlOperOverThresholdOccurred": rttMonCtrlOperOverThresholdOccurred,
       "rttMonCtrlOperNumRtts": rttMonCtrlOperNumRtts,
       "rttMonCtrlOperRttLife": rttMonCtrlOperRttLife,
       "rttMonCtrlOperState": rttMonCtrlOperState,
       "rttMonLatestRttOperTable": rttMonLatestRttOperTable,
       "rttMonLatestRttOperEntry": rttMonLatestRttOperEntry,
       "rttMonLatestRttOperCompletionTime": rttMonLatestRttOperCompletionTime,
       "rttMonLatestRttOperSense": rttMonLatestRttOperSense,
       "rttMonLatestRttOperApplSpecificSense": rttMonLatestRttOperApplSpecificSense,
       "rttMonLatestRttOperSenseDescription": rttMonLatestRttOperSenseDescription,
       "rttMonLatestRttOperTime": rttMonLatestRttOperTime,
       "rttMonLatestRttOperAddress": rttMonLatestRttOperAddress,
       "rttMonReactTriggerAdminTable": rttMonReactTriggerAdminTable,
       "rttMonReactTriggerAdminEntry": rttMonReactTriggerAdminEntry,
       "rttMonReactTriggerAdminRttMonCtrlAdminIndex": rttMonReactTriggerAdminRttMonCtrlAdminIndex,
       "rttMonReactTriggerAdminStatus": rttMonReactTriggerAdminStatus,
       "rttMonReactTriggerOperTable": rttMonReactTriggerOperTable,
       "rttMonReactTriggerOperEntry": rttMonReactTriggerOperEntry,
       "rttMonReactTriggerOperState": rttMonReactTriggerOperState,
       "rttMonEchoPathAdminTable": rttMonEchoPathAdminTable,
       "rttMonEchoPathAdminEntry": rttMonEchoPathAdminEntry,
       "rttMonEchoPathAdminHopIndex": rttMonEchoPathAdminHopIndex,
       "rttMonEchoPathAdminHopAddress": rttMonEchoPathAdminHopAddress,
       "rttMonStats": rttMonStats,
       "rttMonStatsCaptureTable": rttMonStatsCaptureTable,
       "rttMonStatsCaptureEntry": rttMonStatsCaptureEntry,
       "rttMonStatsCaptureStartTimeIndex": rttMonStatsCaptureStartTimeIndex,
       "rttMonStatsCapturePathIndex": rttMonStatsCapturePathIndex,
       "rttMonStatsCaptureHopIndex": rttMonStatsCaptureHopIndex,
       "rttMonStatsCaptureDistIndex": rttMonStatsCaptureDistIndex,
       "rttMonStatsCaptureCompletions": rttMonStatsCaptureCompletions,
       "rttMonStatsCaptureOverThresholds": rttMonStatsCaptureOverThresholds,
       "rttMonStatsCaptureSumCompletionTime": rttMonStatsCaptureSumCompletionTime,
       "rttMonStatsCaptureSumCompletionTime2Low": rttMonStatsCaptureSumCompletionTime2Low,
       "rttMonStatsCaptureSumCompletionTime2High": rttMonStatsCaptureSumCompletionTime2High,
       "rttMonStatsCaptureCompletionTimeMax": rttMonStatsCaptureCompletionTimeMax,
       "rttMonStatsCaptureCompletionTimeMin": rttMonStatsCaptureCompletionTimeMin,
       "rttMonStatsCollectTable": rttMonStatsCollectTable,
       "rttMonStatsCollectEntry": rttMonStatsCollectEntry,
       "rttMonStatsCollectNumDisconnects": rttMonStatsCollectNumDisconnects,
       "rttMonStatsCollectTimeouts": rttMonStatsCollectTimeouts,
       "rttMonStatsCollectBusies": rttMonStatsCollectBusies,
       "rttMonStatsCollectNoConnections": rttMonStatsCollectNoConnections,
       "rttMonStatsCollectDrops": rttMonStatsCollectDrops,
       "rttMonStatsCollectSequenceErrors": rttMonStatsCollectSequenceErrors,
       "rttMonStatsCollectVerifyErrors": rttMonStatsCollectVerifyErrors,
       "rttMonStatsCollectAddress": rttMonStatsCollectAddress,
       "rttMonStatsTotalsTable": rttMonStatsTotalsTable,
       "rttMonStatsTotalsEntry": rttMonStatsTotalsEntry,
       "rttMonStatsTotalsElapsedTime": rttMonStatsTotalsElapsedTime,
       "rttMonStatsTotalsInitiations": rttMonStatsTotalsInitiations,
       "rttMonHTTPStatsTable": rttMonHTTPStatsTable,
       "rttMonHTTPStatsEntry": rttMonHTTPStatsEntry,
       "rttMonHTTPStatsStartTimeIndex": rttMonHTTPStatsStartTimeIndex,
       "rttMonHTTPStatsCompletions": rttMonHTTPStatsCompletions,
       "rttMonHTTPStatsOverThresholds": rttMonHTTPStatsOverThresholds,
       "rttMonHTTPStatsRTTSum": rttMonHTTPStatsRTTSum,
       "rttMonHTTPStatsRTTSum2Low": rttMonHTTPStatsRTTSum2Low,
       "rttMonHTTPStatsRTTSum2High": rttMonHTTPStatsRTTSum2High,
       "rttMonHTTPStatsRTTMin": rttMonHTTPStatsRTTMin,
       "rttMonHTTPStatsRTTMax": rttMonHTTPStatsRTTMax,
       "rttMonHTTPStatsDNSRTTSum": rttMonHTTPStatsDNSRTTSum,
       "rttMonHTTPStatsTCPConnectRTTSum": rttMonHTTPStatsTCPConnectRTTSum,
       "rttMonHTTPStatsTransactionRTTSum": rttMonHTTPStatsTransactionRTTSum,
       "rttMonHTTPStatsMessageBodyOctetsSum": rttMonHTTPStatsMessageBodyOctetsSum,
       "rttMonHTTPStatsDNSServerTimeout": rttMonHTTPStatsDNSServerTimeout,
       "rttMonHTTPStatsTCPConnectTimeout": rttMonHTTPStatsTCPConnectTimeout,
       "rttMonHTTPStatsTransactionTimeout": rttMonHTTPStatsTransactionTimeout,
       "rttMonHTTPStatsDNSQueryError": rttMonHTTPStatsDNSQueryError,
       "rttMonHTTPStatsHTTPError": rttMonHTTPStatsHTTPError,
       "rttMonHTTPStatsError": rttMonHTTPStatsError,
       "rttMonHTTPStatsBusies": rttMonHTTPStatsBusies,
       "rttMonJitterStatsTable": rttMonJitterStatsTable,
       "rttMonJitterStatsEntry": rttMonJitterStatsEntry,
       "rttMonJitterStatsStartTimeIndex": rttMonJitterStatsStartTimeIndex,
       "rttMonJitterStatsCompletions": rttMonJitterStatsCompletions,
       "rttMonJitterStatsOverThresholds": rttMonJitterStatsOverThresholds,
       "rttMonJitterStatsNumOfRTT": rttMonJitterStatsNumOfRTT,
       "rttMonJitterStatsRTTSum": rttMonJitterStatsRTTSum,
       "rttMonJitterStatsRTTSum2Low": rttMonJitterStatsRTTSum2Low,
       "rttMonJitterStatsRTTSum2High": rttMonJitterStatsRTTSum2High,
       "rttMonJitterStatsRTTMin": rttMonJitterStatsRTTMin,
       "rttMonJitterStatsRTTMax": rttMonJitterStatsRTTMax,
       "rttMonJitterStatsMinOfPositivesSD": rttMonJitterStatsMinOfPositivesSD,
       "rttMonJitterStatsMaxOfPositivesSD": rttMonJitterStatsMaxOfPositivesSD,
       "rttMonJitterStatsNumOfPositivesSD": rttMonJitterStatsNumOfPositivesSD,
       "rttMonJitterStatsSumOfPositivesSD": rttMonJitterStatsSumOfPositivesSD,
       "rttMonJitterStatsSum2PositivesSDLow": rttMonJitterStatsSum2PositivesSDLow,
       "rttMonJitterStatsSum2PositivesSDHigh": rttMonJitterStatsSum2PositivesSDHigh,
       "rttMonJitterStatsMinOfNegativesSD": rttMonJitterStatsMinOfNegativesSD,
       "rttMonJitterStatsMaxOfNegativesSD": rttMonJitterStatsMaxOfNegativesSD,
       "rttMonJitterStatsNumOfNegativesSD": rttMonJitterStatsNumOfNegativesSD,
       "rttMonJitterStatsSumOfNegativesSD": rttMonJitterStatsSumOfNegativesSD,
       "rttMonJitterStatsSum2NegativesSDLow": rttMonJitterStatsSum2NegativesSDLow,
       "rttMonJitterStatsSum2NegativesSDHigh": rttMonJitterStatsSum2NegativesSDHigh,
       "rttMonJitterStatsMinOfPositivesDS": rttMonJitterStatsMinOfPositivesDS,
       "rttMonJitterStatsMaxOfPositivesDS": rttMonJitterStatsMaxOfPositivesDS,
       "rttMonJitterStatsNumOfPositivesDS": rttMonJitterStatsNumOfPositivesDS,
       "rttMonJitterStatsSumOfPositivesDS": rttMonJitterStatsSumOfPositivesDS,
       "rttMonJitterStatsSum2PositivesDSLow": rttMonJitterStatsSum2PositivesDSLow,
       "rttMonJitterStatsSum2PositivesDSHigh": rttMonJitterStatsSum2PositivesDSHigh,
       "rttMonJitterStatsMinOfNegativesDS": rttMonJitterStatsMinOfNegativesDS,
       "rttMonJitterStatsMaxOfNegativesDS": rttMonJitterStatsMaxOfNegativesDS,
       "rttMonJitterStatsNumOfNegativesDS": rttMonJitterStatsNumOfNegativesDS,
       "rttMonJitterStatsSumOfNegativesDS": rttMonJitterStatsSumOfNegativesDS,
       "rttMonJitterStatsSum2NegativesDSLow": rttMonJitterStatsSum2NegativesDSLow,
       "rttMonJitterStatsSum2NegativesDSHigh": rttMonJitterStatsSum2NegativesDSHigh,
       "rttMonJitterStatsPacketLossSD": rttMonJitterStatsPacketLossSD,
       "rttMonJitterStatsPacketLossDS": rttMonJitterStatsPacketLossDS,
       "rttMonJitterStatsPacketOutOfSequence": rttMonJitterStatsPacketOutOfSequence,
       "rttMonJitterStatsPacketMIA": rttMonJitterStatsPacketMIA,
       "rttMonJitterStatsPacketLateArrival": rttMonJitterStatsPacketLateArrival,
       "rttMonJitterStatsError": rttMonJitterStatsError,
       "rttMonJitterStatsBusies": rttMonJitterStatsBusies,
       "rttMonHistory": rttMonHistory,
       "rttMonHistoryCollectionTable": rttMonHistoryCollectionTable,
       "rttMonHistoryCollectionEntry": rttMonHistoryCollectionEntry,
       "rttMonHistoryCollectionLifeIndex": rttMonHistoryCollectionLifeIndex,
       "rttMonHistoryCollectionBucketIndex": rttMonHistoryCollectionBucketIndex,
       "rttMonHistoryCollectionSampleIndex": rttMonHistoryCollectionSampleIndex,
       "rttMonHistoryCollectionSampleTime": rttMonHistoryCollectionSampleTime,
       "rttMonHistoryCollectionAddress": rttMonHistoryCollectionAddress,
       "rttMonHistoryCollectionCompletionTime": rttMonHistoryCollectionCompletionTime,
       "rttMonHistoryCollectionSense": rttMonHistoryCollectionSense,
       "rttMonHistoryCollectionApplSpecificSense": rttMonHistoryCollectionApplSpecificSense,
       "rttMonHistoryCollectionSenseDescription": rttMonHistoryCollectionSenseDescription,
       "rttMonLatestOper": rttMonLatestOper,
       "rttMonLatestHTTPOperTable": rttMonLatestHTTPOperTable,
       "rttMonLatestHTTPOperEntry": rttMonLatestHTTPOperEntry,
       "rttMonLatestHTTPOperRTT": rttMonLatestHTTPOperRTT,
       "rttMonLatestHTTPOperDNSRTT": rttMonLatestHTTPOperDNSRTT,
       "rttMonLatestHTTPOperTCPConnectRTT": rttMonLatestHTTPOperTCPConnectRTT,
       "rttMonLatestHTTPOperTransactionRTT": rttMonLatestHTTPOperTransactionRTT,
       "rttMonLatestHTTPOperMessageBodyOctets": rttMonLatestHTTPOperMessageBodyOctets,
       "rttMonLatestHTTPOperSense": rttMonLatestHTTPOperSense,
       "rttMonLatestHTTPErrorSenseDescription": rttMonLatestHTTPErrorSenseDescription,
       "rttMonLatestJitterOperTable": rttMonLatestJitterOperTable,
       "rttMonLatestJitterOperEntry": rttMonLatestJitterOperEntry,
       "rttMonLatestJitterOperNumOfRTT": rttMonLatestJitterOperNumOfRTT,
       "rttMonLatestJitterOperRTTSum": rttMonLatestJitterOperRTTSum,
       "rttMonLatestJitterOperRTTSum2": rttMonLatestJitterOperRTTSum2,
       "rttMonLatestJitterOperRTTMin": rttMonLatestJitterOperRTTMin,
       "rttMonLatestJitterOperRTTMax": rttMonLatestJitterOperRTTMax,
       "rttMonLatestJitterOperMinOfPositivesSD": rttMonLatestJitterOperMinOfPositivesSD,
       "rttMonLatestJitterOperMaxOfPositivesSD": rttMonLatestJitterOperMaxOfPositivesSD,
       "rttMonLatestJitterOperNumOfPositivesSD": rttMonLatestJitterOperNumOfPositivesSD,
       "rttMonLatestJitterOperSumOfPositivesSD": rttMonLatestJitterOperSumOfPositivesSD,
       "rttMonLatestJitterOperSum2PositivesSD": rttMonLatestJitterOperSum2PositivesSD,
       "rttMonLatestJitterOperMinOfNegativesSD": rttMonLatestJitterOperMinOfNegativesSD,
       "rttMonLatestJitterOperMaxOfNegativesSD": rttMonLatestJitterOperMaxOfNegativesSD,
       "rttMonLatestJitterOperNumOfNegativesSD": rttMonLatestJitterOperNumOfNegativesSD,
       "rttMonLatestJitterOperSumOfNegativesSD": rttMonLatestJitterOperSumOfNegativesSD,
       "rttMonLatestJitterOperSum2NegativesSD": rttMonLatestJitterOperSum2NegativesSD,
       "rttMonLatestJitterOperMinOfPositivesDS": rttMonLatestJitterOperMinOfPositivesDS,
       "rttMonLatestJitterOperMaxOfPositivesDS": rttMonLatestJitterOperMaxOfPositivesDS,
       "rttMonLatestJitterOperNumOfPositivesDS": rttMonLatestJitterOperNumOfPositivesDS,
       "rttMonLatestJitterOperSumOfPositivesDS": rttMonLatestJitterOperSumOfPositivesDS,
       "rttMonLatestJitterOperSum2PositivesDS": rttMonLatestJitterOperSum2PositivesDS,
       "rttMonLatestJitterOperMinOfNegativesDS": rttMonLatestJitterOperMinOfNegativesDS,
       "rttMonLatestJitterOperMaxOfNegativesDS": rttMonLatestJitterOperMaxOfNegativesDS,
       "rttMonLatestJitterOperNumOfNegativesDS": rttMonLatestJitterOperNumOfNegativesDS,
       "rttMonLatestJitterOperSumOfNegativesDS": rttMonLatestJitterOperSumOfNegativesDS,
       "rttMonLatestJitterOperSum2NegativesDS": rttMonLatestJitterOperSum2NegativesDS,
       "rttMonLatestJitterOperPacketLossSD": rttMonLatestJitterOperPacketLossSD,
       "rttMonLatestJitterOperPacketLossDS": rttMonLatestJitterOperPacketLossDS,
       "rttMonLatestJitterOperPacketOutOfSequence": rttMonLatestJitterOperPacketOutOfSequence,
       "rttMonLatestJitterOperPacketMIA": rttMonLatestJitterOperPacketMIA,
       "rttMonLatestJitterOperPacketLateArrival": rttMonLatestJitterOperPacketLateArrival,
       "rttMonLatestJitterOperSense": rttMonLatestJitterOperSense,
       "rttMonLatestJitterErrorSenseDescription": rttMonLatestJitterErrorSenseDescription,
       "rttMonNotificationsPrefix": rttMonNotificationsPrefix,
       "rttMonNotifications": rttMonNotifications,
       "rttMonConnectionChangeNotification": rttMonConnectionChangeNotification,
       "rttMonTimeoutNotification": rttMonTimeoutNotification,
       "rttMonThresholdNotification": rttMonThresholdNotification,
       "ciscoRttMonMibConformance": ciscoRttMonMibConformance,
       "ciscoRttMonMibCompliances": ciscoRttMonMibCompliances,
       "ciscoRttMonMibCompliance": ciscoRttMonMibCompliance,
       "ciscoRttMonMibComplianceRev1": ciscoRttMonMibComplianceRev1,
       "ciscoRttMonMibComplianceRev2": ciscoRttMonMibComplianceRev2,
       "ciscoRttMonMibComplianceRev3": ciscoRttMonMibComplianceRev3,
       "ciscoRttMonMibGroups": ciscoRttMonMibGroups,
       "ciscoApplGroup": ciscoApplGroup,
       "ciscoCtrlGroup": ciscoCtrlGroup,
       "ciscoStatsGroup": ciscoStatsGroup,
       "ciscoHistoryGroup": ciscoHistoryGroup,
       "ciscoCtrlGroupRev1": ciscoCtrlGroupRev1,
       "ciscoCtrlGroupRev2": ciscoCtrlGroupRev2,
       "ciscoLatestOperGroupRev1": ciscoLatestOperGroupRev1,
       "ciscoStatsGroupRev1": ciscoStatsGroupRev1,
       "ciscoApplGroupRev1": ciscoApplGroupRev1,
       "ciscoCtrlGroupRev3": ciscoCtrlGroupRev3}
)
