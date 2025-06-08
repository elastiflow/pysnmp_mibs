# SNMP MIB module (BLADEOS-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/bnt_26543/BLADEOS-BASE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:58:10 2025
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

(BridgeId,
 dot1dBasePort,
 dot1dBasePortEntry,
 dot1dBridge,
 dot1dTp,
 dot1dTpPort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "dot1dBasePort",
    "dot1dBasePortEntry",
    "dot1dBridge",
    "dot1dTp",
    "dot1dTpPort")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,
 SnmpEngineID,
 SnmpMessageProcessingModel,
 SnmpSecurityLevel,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID",
    "SnmpMessageProcessingModel",
    "SnmpSecurityLevel",
    "SnmpSecurityModel")

(usmNoAuthProtocol,
 usmNoPrivProtocol) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmNoAuthProtocol",
    "usmNoPrivProtocol")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
    "enterprises",
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 InetAddress,
 InetAddressType,
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "InetAddress",
    "InetAddressType",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

blade = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26543)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class PortLaMode(TextualConvention, Integer32):
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
        *(("lacp", 1),
          ("manual", 2),
          ("disable", 3))
    )



class LacpKey(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class LacpState(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("lacpActivity", 0),
          ("lacpTimeout", 1),
          ("aggregation", 2),
          ("synchronization", 3),
          ("collecting", 4),
          ("distributing", 5),
          ("defaulted", 6),
          ("expired", 7))
    )


class PaeControlledPortStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2))
    )



class AuthenticMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteServer", 1),
          ("localServer", 2))
    )



class PermissionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class BridgeId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class Timeout(TextualConvention, Integer32):
    status = "current"
    displayHint = "d4"


class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



class BosKeyChange(TextualConvention, OctetString):
    status = "current"


class SnmpTagValue(TextualConvention, OctetString):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SnmpTagList(TextualConvention, OctetString):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_ProductID_ObjectIdentity = ObjectIdentity
productID = _ProductID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100)
)
_Bladeip_ObjectIdentity = ObjectIdentity
bladeip = _Bladeip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2)
)
_Bosip_ObjectIdentity = ObjectIdentity
bosip = _Bosip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1)
)
_BosIpInLengthErrors_Type = Counter32
_BosIpInLengthErrors_Object = MibScalar
bosIpInLengthErrors = _BosIpInLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 1),
    _BosIpInLengthErrors_Type()
)
bosIpInLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpInLengthErrors.setStatus("current")
_BosIpInCksumErrors_Type = Counter32
_BosIpInCksumErrors_Object = MibScalar
bosIpInCksumErrors = _BosIpInCksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 2),
    _BosIpInCksumErrors_Type()
)
bosIpInCksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpInCksumErrors.setStatus("current")
_BosIpInVersionErrors_Type = Counter32
_BosIpInVersionErrors_Object = MibScalar
bosIpInVersionErrors = _BosIpInVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 3),
    _BosIpInVersionErrors_Type()
)
bosIpInVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpInVersionErrors.setStatus("current")
_BosIpInTTLErrors_Type = Counter32
_BosIpInTTLErrors_Object = MibScalar
bosIpInTTLErrors = _BosIpInTTLErrors_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 4),
    _BosIpInTTLErrors_Type()
)
bosIpInTTLErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpInTTLErrors.setStatus("current")
_BosIpInOptionErrors_Type = Counter32
_BosIpInOptionErrors_Object = MibScalar
bosIpInOptionErrors = _BosIpInOptionErrors_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 5),
    _BosIpInOptionErrors_Type()
)
bosIpInOptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpInOptionErrors.setStatus("current")
_BosIpInBroadCasts_Type = Counter32
_BosIpInBroadCasts_Object = MibScalar
bosIpInBroadCasts = _BosIpInBroadCasts_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 6),
    _BosIpInBroadCasts_Type()
)
bosIpInBroadCasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpInBroadCasts.setStatus("current")
_BosIpOutGenErrors_Type = Counter32
_BosIpOutGenErrors_Object = MibScalar
bosIpOutGenErrors = _BosIpOutGenErrors_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 7),
    _BosIpOutGenErrors_Type()
)
bosIpOutGenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpOutGenErrors.setStatus("current")


class _BosIpOptProcEnable_Type(Integer32):
    """Custom type bosIpOptProcEnable based on Integer32"""
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


_BosIpOptProcEnable_Type.__name__ = "Integer32"
_BosIpOptProcEnable_Object = MibScalar
bosIpOptProcEnable = _BosIpOptProcEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 9),
    _BosIpOptProcEnable_Type()
)
bosIpOptProcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpOptProcEnable.setStatus("current")


class _BosIpNumMultipath_Type(Integer32):
    """Custom type bosIpNumMultipath based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BosIpNumMultipath_Type.__name__ = "Integer32"
_BosIpNumMultipath_Object = MibScalar
bosIpNumMultipath = _BosIpNumMultipath_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 10),
    _BosIpNumMultipath_Type()
)
bosIpNumMultipath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpNumMultipath.setStatus("current")


class _BosIpLoadShareEnable_Type(Integer32):
    """Custom type bosIpLoadShareEnable based on Integer32"""
    defaultValue = 2

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


_BosIpLoadShareEnable_Type.__name__ = "Integer32"
_BosIpLoadShareEnable_Object = MibScalar
bosIpLoadShareEnable = _BosIpLoadShareEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 11),
    _BosIpLoadShareEnable_Type()
)
bosIpLoadShareEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpLoadShareEnable.setStatus("current")


class _BosIpEnablePMTUD_Type(Integer32):
    """Custom type bosIpEnablePMTUD based on Integer32"""
    defaultValue = 2

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


_BosIpEnablePMTUD_Type.__name__ = "Integer32"
_BosIpEnablePMTUD_Object = MibScalar
bosIpEnablePMTUD = _BosIpEnablePMTUD_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 12),
    _BosIpEnablePMTUD_Type()
)
bosIpEnablePMTUD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpEnablePMTUD.setStatus("current")


class _BosIpPmtuEntryAge_Type(Integer32):
    """Custom type bosIpPmtuEntryAge based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_BosIpPmtuEntryAge_Type.__name__ = "Integer32"
_BosIpPmtuEntryAge_Object = MibScalar
bosIpPmtuEntryAge = _BosIpPmtuEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 13),
    _BosIpPmtuEntryAge_Type()
)
bosIpPmtuEntryAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpPmtuEntryAge.setStatus("current")


class _BosIpPmtuTableSize_Type(Integer32):
    """Custom type bosIpPmtuTableSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BosIpPmtuTableSize_Type.__name__ = "Integer32"
_BosIpPmtuTableSize_Object = MibScalar
bosIpPmtuTableSize = _BosIpPmtuTableSize_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 14),
    _BosIpPmtuTableSize_Type()
)
bosIpPmtuTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpPmtuTableSize.setStatus("current")
_BosIpTraceConfigTable_Object = MibTable
bosIpTraceConfigTable = _BosIpTraceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16)
)
if mibBuilder.loadTexts:
    bosIpTraceConfigTable.setStatus("current")
_BosIpTraceConfigEntry_Object = MibTableRow
bosIpTraceConfigEntry = _BosIpTraceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16, 1)
)
bosIpTraceConfigEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosIpTraceConfigIndex"),
)
if mibBuilder.loadTexts:
    bosIpTraceConfigEntry.setStatus("current")


class _BosIpTraceConfigIndex_Type(Integer32):
    """Custom type bosIpTraceConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_BosIpTraceConfigIndex_Type.__name__ = "Integer32"
_BosIpTraceConfigIndex_Object = MibTableColumn
bosIpTraceConfigIndex = _BosIpTraceConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16, 1, 1),
    _BosIpTraceConfigIndex_Type()
)
bosIpTraceConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpTraceConfigIndex.setStatus("current")
_BosIpTraceConfigDest_Type = IpAddress
_BosIpTraceConfigDest_Object = MibTableColumn
bosIpTraceConfigDest = _BosIpTraceConfigDest_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16, 1, 2),
    _BosIpTraceConfigDest_Type()
)
bosIpTraceConfigDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpTraceConfigDest.setStatus("current")


class _BosIpTraceConfigAdminStatus_Type(Integer32):
    """Custom type bosIpTraceConfigAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_BosIpTraceConfigAdminStatus_Type.__name__ = "Integer32"
_BosIpTraceConfigAdminStatus_Object = MibTableColumn
bosIpTraceConfigAdminStatus = _BosIpTraceConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16, 1, 3),
    _BosIpTraceConfigAdminStatus_Type()
)
bosIpTraceConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpTraceConfigAdminStatus.setStatus("current")


class _BosIpTraceConfigMaxTTL_Type(Integer32):
    """Custom type bosIpTraceConfigMaxTTL based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BosIpTraceConfigMaxTTL_Type.__name__ = "Integer32"
_BosIpTraceConfigMaxTTL_Object = MibTableColumn
bosIpTraceConfigMaxTTL = _BosIpTraceConfigMaxTTL_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16, 1, 4),
    _BosIpTraceConfigMaxTTL_Type()
)
bosIpTraceConfigMaxTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpTraceConfigMaxTTL.setStatus("current")


class _BosIpTraceConfigMinTTL_Type(Integer32):
    """Custom type bosIpTraceConfigMinTTL based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BosIpTraceConfigMinTTL_Type.__name__ = "Integer32"
_BosIpTraceConfigMinTTL_Object = MibTableColumn
bosIpTraceConfigMinTTL = _BosIpTraceConfigMinTTL_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16, 1, 5),
    _BosIpTraceConfigMinTTL_Type()
)
bosIpTraceConfigMinTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpTraceConfigMinTTL.setStatus("current")


class _BosIpTraceConfigOperStatus_Type(Integer32):
    """Custom type bosIpTraceConfigOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inprogress", 1),
          ("notinprogress", 2))
    )


_BosIpTraceConfigOperStatus_Type.__name__ = "Integer32"
_BosIpTraceConfigOperStatus_Object = MibTableColumn
bosIpTraceConfigOperStatus = _BosIpTraceConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16, 1, 6),
    _BosIpTraceConfigOperStatus_Type()
)
bosIpTraceConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpTraceConfigOperStatus.setStatus("current")


class _BosIpTraceConfigTimeout_Type(Integer32):
    """Custom type bosIpTraceConfigTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BosIpTraceConfigTimeout_Type.__name__ = "Integer32"
_BosIpTraceConfigTimeout_Object = MibTableColumn
bosIpTraceConfigTimeout = _BosIpTraceConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16, 1, 7),
    _BosIpTraceConfigTimeout_Type()
)
bosIpTraceConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpTraceConfigTimeout.setStatus("current")


class _BosIpTraceConfigMtu_Type(Integer32):
    """Custom type bosIpTraceConfigMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BosIpTraceConfigMtu_Type.__name__ = "Integer32"
_BosIpTraceConfigMtu_Object = MibTableColumn
bosIpTraceConfigMtu = _BosIpTraceConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16, 1, 8),
    _BosIpTraceConfigMtu_Type()
)
bosIpTraceConfigMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpTraceConfigMtu.setStatus("current")


class _BosIpTraceConfigPort_Type(Integer32):
    """Custom type bosIpTraceConfigPort based on Integer32"""
    defaultValue = 84

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(84, 84),
        ValueRangeConstraint(49152, 65535),
    )


_BosIpTraceConfigPort_Type.__name__ = "Integer32"
_BosIpTraceConfigPort_Object = MibTableColumn
bosIpTraceConfigPort = _BosIpTraceConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 16, 1, 9),
    _BosIpTraceConfigPort_Type()
)
bosIpTraceConfigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpTraceConfigPort.setStatus("current")
_BosIpTraceTable_Object = MibTable
bosIpTraceTable = _BosIpTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 17)
)
if mibBuilder.loadTexts:
    bosIpTraceTable.setStatus("current")
_BosIpTraceEntry_Object = MibTableRow
bosIpTraceEntry = _BosIpTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 17, 1)
)
bosIpTraceEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosIpTraceConfigIndex"),
    (0, "BLADEOS-BASE-MIB", "bosIpTraceDest"),
    (0, "BLADEOS-BASE-MIB", "bosIpTraceHopCount"),
)
if mibBuilder.loadTexts:
    bosIpTraceEntry.setStatus("current")
_BosIpTraceDest_Type = IpAddress
_BosIpTraceDest_Object = MibTableColumn
bosIpTraceDest = _BosIpTraceDest_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 17, 1, 1),
    _BosIpTraceDest_Type()
)
bosIpTraceDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpTraceDest.setStatus("current")


class _BosIpTraceHopCount_Type(Integer32):
    """Custom type bosIpTraceHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpTraceHopCount_Type.__name__ = "Integer32"
_BosIpTraceHopCount_Object = MibTableColumn
bosIpTraceHopCount = _BosIpTraceHopCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 17, 1, 2),
    _BosIpTraceHopCount_Type()
)
bosIpTraceHopCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpTraceHopCount.setStatus("current")
_BosIpTraceIntermHop_Type = IpAddress
_BosIpTraceIntermHop_Object = MibTableColumn
bosIpTraceIntermHop = _BosIpTraceIntermHop_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 17, 1, 3),
    _BosIpTraceIntermHop_Type()
)
bosIpTraceIntermHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpTraceIntermHop.setStatus("current")


class _BosIpTraceReachTime1_Type(Integer32):
    """Custom type bosIpTraceReachTime1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpTraceReachTime1_Type.__name__ = "Integer32"
_BosIpTraceReachTime1_Object = MibTableColumn
bosIpTraceReachTime1 = _BosIpTraceReachTime1_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 17, 1, 4),
    _BosIpTraceReachTime1_Type()
)
bosIpTraceReachTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpTraceReachTime1.setStatus("current")


class _BosIpTraceReachTime2_Type(Integer32):
    """Custom type bosIpTraceReachTime2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpTraceReachTime2_Type.__name__ = "Integer32"
_BosIpTraceReachTime2_Object = MibTableColumn
bosIpTraceReachTime2 = _BosIpTraceReachTime2_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 17, 1, 5),
    _BosIpTraceReachTime2_Type()
)
bosIpTraceReachTime2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpTraceReachTime2.setStatus("current")


class _BosIpTraceReachTime3_Type(Integer32):
    """Custom type bosIpTraceReachTime3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpTraceReachTime3_Type.__name__ = "Integer32"
_BosIpTraceReachTime3_Object = MibTableColumn
bosIpTraceReachTime3 = _BosIpTraceReachTime3_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 17, 1, 6),
    _BosIpTraceReachTime3_Type()
)
bosIpTraceReachTime3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpTraceReachTime3.setStatus("current")
_BosIpAddressTable_Object = MibTable
bosIpAddressTable = _BosIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 18)
)
if mibBuilder.loadTexts:
    bosIpAddressTable.setStatus("current")
_BosIpAddressEntry_Object = MibTableRow
bosIpAddressEntry = _BosIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 18, 1)
)
bosIpAddressEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosIpAddrTabAddress"),
)
if mibBuilder.loadTexts:
    bosIpAddressEntry.setStatus("current")


class _BosIpAddrTabIfaceId_Type(Integer32):
    """Custom type bosIpAddrTabIfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpAddrTabIfaceId_Type.__name__ = "Integer32"
_BosIpAddrTabIfaceId_Object = MibTableColumn
bosIpAddrTabIfaceId = _BosIpAddrTabIfaceId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 18, 1, 1),
    _BosIpAddrTabIfaceId_Type()
)
bosIpAddrTabIfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpAddrTabIfaceId.setStatus("current")
_BosIpAddrTabAddress_Type = IpAddress
_BosIpAddrTabAddress_Object = MibTableColumn
bosIpAddrTabAddress = _BosIpAddrTabAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 18, 1, 2),
    _BosIpAddrTabAddress_Type()
)
bosIpAddrTabAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpAddrTabAddress.setStatus("current")
_BosIpAddrTabAdvertise_Type = TruthValue
_BosIpAddrTabAdvertise_Object = MibTableColumn
bosIpAddrTabAdvertise = _BosIpAddrTabAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 18, 1, 3),
    _BosIpAddrTabAdvertise_Type()
)
bosIpAddrTabAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAddrTabAdvertise.setStatus("current")


class _BosIpAddrTabPreflevel_Type(Integer32):
    """Custom type bosIpAddrTabPreflevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpAddrTabPreflevel_Type.__name__ = "Integer32"
_BosIpAddrTabPreflevel_Object = MibTableColumn
bosIpAddrTabPreflevel = _BosIpAddrTabPreflevel_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 18, 1, 4),
    _BosIpAddrTabPreflevel_Type()
)
bosIpAddrTabPreflevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAddrTabPreflevel.setStatus("current")
_BosIpAddrTabStatus_Type = RowStatus
_BosIpAddrTabStatus_Object = MibTableColumn
bosIpAddrTabStatus = _BosIpAddrTabStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 18, 1, 5),
    _BosIpAddrTabStatus_Type()
)
bosIpAddrTabStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpAddrTabStatus.setStatus("current")
_BosIpRtrLstTable_Object = MibTable
bosIpRtrLstTable = _BosIpRtrLstTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 19)
)
if mibBuilder.loadTexts:
    bosIpRtrLstTable.setStatus("current")
_BosIpRtrLstEntry_Object = MibTableRow
bosIpRtrLstEntry = _BosIpRtrLstEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 19, 1)
)
bosIpRtrLstEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosIpRtrLstAddress"),
)
if mibBuilder.loadTexts:
    bosIpRtrLstEntry.setStatus("current")


class _BosIpRtrLstIface_Type(Integer32):
    """Custom type bosIpRtrLstIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpRtrLstIface_Type.__name__ = "Integer32"
_BosIpRtrLstIface_Object = MibTableColumn
bosIpRtrLstIface = _BosIpRtrLstIface_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 19, 1, 1),
    _BosIpRtrLstIface_Type()
)
bosIpRtrLstIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpRtrLstIface.setStatus("current")
_BosIpRtrLstAddress_Type = IpAddress
_BosIpRtrLstAddress_Object = MibTableColumn
bosIpRtrLstAddress = _BosIpRtrLstAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 19, 1, 2),
    _BosIpRtrLstAddress_Type()
)
bosIpRtrLstAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpRtrLstAddress.setStatus("current")


class _BosIpRtrLstPreflevel_Type(Integer32):
    """Custom type bosIpRtrLstPreflevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpRtrLstPreflevel_Type.__name__ = "Integer32"
_BosIpRtrLstPreflevel_Object = MibTableColumn
bosIpRtrLstPreflevel = _BosIpRtrLstPreflevel_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 19, 1, 3),
    _BosIpRtrLstPreflevel_Type()
)
bosIpRtrLstPreflevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpRtrLstPreflevel.setStatus("current")
_BosIpRtrLstStatic_Type = TruthValue
_BosIpRtrLstStatic_Object = MibTableColumn
bosIpRtrLstStatic = _BosIpRtrLstStatic_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 19, 1, 4),
    _BosIpRtrLstStatic_Type()
)
bosIpRtrLstStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpRtrLstStatic.setStatus("current")
_BosIpRtrLstStatus_Type = RowStatus
_BosIpRtrLstStatus_Object = MibTableColumn
bosIpRtrLstStatus = _BosIpRtrLstStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 19, 1, 5),
    _BosIpRtrLstStatus_Type()
)
bosIpRtrLstStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpRtrLstStatus.setStatus("current")
_BosIpPathMtuTable_Object = MibTable
bosIpPathMtuTable = _BosIpPathMtuTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 20)
)
if mibBuilder.loadTexts:
    bosIpPathMtuTable.setStatus("current")
_BosIpPathMtuEntry_Object = MibTableRow
bosIpPathMtuEntry = _BosIpPathMtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 20, 1)
)
bosIpPathMtuEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosIpPmtuDestination"),
    (0, "BLADEOS-BASE-MIB", "bosIpPmtuTos"),
)
if mibBuilder.loadTexts:
    bosIpPathMtuEntry.setStatus("current")
_BosIpPmtuDestination_Type = IpAddress
_BosIpPmtuDestination_Object = MibTableColumn
bosIpPmtuDestination = _BosIpPmtuDestination_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 20, 1, 1),
    _BosIpPmtuDestination_Type()
)
bosIpPmtuDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpPmtuDestination.setStatus("current")


class _BosIpPmtuTos_Type(Integer32):
    """Custom type bosIpPmtuTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpPmtuTos_Type.__name__ = "Integer32"
_BosIpPmtuTos_Object = MibTableColumn
bosIpPmtuTos = _BosIpPmtuTos_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 20, 1, 2),
    _BosIpPmtuTos_Type()
)
bosIpPmtuTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpPmtuTos.setStatus("current")


class _BosIpPathMtu_Type(Integer32):
    """Custom type bosIpPathMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 65535),
    )


_BosIpPathMtu_Type.__name__ = "Integer32"
_BosIpPathMtu_Object = MibTableColumn
bosIpPathMtu = _BosIpPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 20, 1, 3),
    _BosIpPathMtu_Type()
)
bosIpPathMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpPathMtu.setStatus("current")


class _BosIpPmtuDisc_Type(Integer32):
    """Custom type bosIpPmtuDisc based on Integer32"""
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


_BosIpPmtuDisc_Type.__name__ = "Integer32"
_BosIpPmtuDisc_Object = MibTableColumn
bosIpPmtuDisc = _BosIpPmtuDisc_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 20, 1, 4),
    _BosIpPmtuDisc_Type()
)
bosIpPmtuDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpPmtuDisc.setStatus("current")
_BosIpPmtuEntryStatus_Type = RowStatus
_BosIpPmtuEntryStatus_Object = MibTableColumn
bosIpPmtuEntryStatus = _BosIpPmtuEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 20, 1, 5),
    _BosIpPmtuEntryStatus_Type()
)
bosIpPmtuEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpPmtuEntryStatus.setStatus("current")
_BosIpCommonRoutingTable_Object = MibTable
bosIpCommonRoutingTable = _BosIpCommonRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22)
)
if mibBuilder.loadTexts:
    bosIpCommonRoutingTable.setStatus("current")
_BosIpCommonRoutingEntry_Object = MibTableRow
bosIpCommonRoutingEntry = _BosIpCommonRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1)
)
bosIpCommonRoutingEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosIpRouteDest"),
    (0, "BLADEOS-BASE-MIB", "bosIpRouteMask"),
    (0, "BLADEOS-BASE-MIB", "bosIpRouteTos"),
    (0, "BLADEOS-BASE-MIB", "bosIpRouteNextHop"),
    (0, "BLADEOS-BASE-MIB", "bosIpRouteProto"),
)
if mibBuilder.loadTexts:
    bosIpCommonRoutingEntry.setStatus("current")
_BosIpRouteDest_Type = IpAddress
_BosIpRouteDest_Object = MibTableColumn
bosIpRouteDest = _BosIpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 1),
    _BosIpRouteDest_Type()
)
bosIpRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpRouteDest.setStatus("current")
_BosIpRouteMask_Type = IpAddress
_BosIpRouteMask_Object = MibTableColumn
bosIpRouteMask = _BosIpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 2),
    _BosIpRouteMask_Type()
)
bosIpRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpRouteMask.setStatus("current")


class _BosIpRouteTos_Type(Integer32):
    """Custom type bosIpRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpRouteTos_Type.__name__ = "Integer32"
_BosIpRouteTos_Object = MibTableColumn
bosIpRouteTos = _BosIpRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 3),
    _BosIpRouteTos_Type()
)
bosIpRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpRouteTos.setStatus("current")
_BosIpRouteNextHop_Type = IpAddress
_BosIpRouteNextHop_Object = MibTableColumn
bosIpRouteNextHop = _BosIpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 4),
    _BosIpRouteNextHop_Type()
)
bosIpRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpRouteNextHop.setStatus("current")


class _BosIpRouteProto_Type(Integer32):
    """Custom type bosIpRouteProto based on Integer32"""
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
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("addr", 11),
          ("bcast", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16))
    )


_BosIpRouteProto_Type.__name__ = "Integer32"
_BosIpRouteProto_Object = MibTableColumn
bosIpRouteProto = _BosIpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 5),
    _BosIpRouteProto_Type()
)
bosIpRouteProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpRouteProto.setStatus("current")
_BosIpRouteProtoInstanceId_Type = Integer32
_BosIpRouteProtoInstanceId_Object = MibTableColumn
bosIpRouteProtoInstanceId = _BosIpRouteProtoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 6),
    _BosIpRouteProtoInstanceId_Type()
)
bosIpRouteProtoInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpRouteProtoInstanceId.setStatus("current")
_BosIpRouteIfIndex_Type = Integer32
_BosIpRouteIfIndex_Object = MibTableColumn
bosIpRouteIfIndex = _BosIpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 7),
    _BosIpRouteIfIndex_Type()
)
bosIpRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpRouteIfIndex.setStatus("current")


class _BosIpRouteType_Type(Integer32):
    """Custom type bosIpRouteType based on Integer32"""
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
        *(("other", 1),
          ("reject", 2),
          ("direct", 3),
          ("remote", 4),
          ("local", 5),
          ("bcast", 6))
    )


_BosIpRouteType_Type.__name__ = "Integer32"
_BosIpRouteType_Object = MibTableColumn
bosIpRouteType = _BosIpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 8),
    _BosIpRouteType_Type()
)
bosIpRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpRouteType.setStatus("current")


class _BosIpRouteAge_Type(Integer32):
    """Custom type bosIpRouteAge based on Integer32"""
    defaultValue = 0


_BosIpRouteAge_Type.__name__ = "Integer32"
_BosIpRouteAge_Object = MibTableColumn
bosIpRouteAge = _BosIpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 9),
    _BosIpRouteAge_Type()
)
bosIpRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpRouteAge.setStatus("current")


class _BosIpRouteNextHopAS_Type(Integer32):
    """Custom type bosIpRouteNextHopAS based on Integer32"""
    defaultValue = 0


_BosIpRouteNextHopAS_Type.__name__ = "Integer32"
_BosIpRouteNextHopAS_Object = MibTableColumn
bosIpRouteNextHopAS = _BosIpRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 10),
    _BosIpRouteNextHopAS_Type()
)
bosIpRouteNextHopAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpRouteNextHopAS.setStatus("current")


class _BosIpRouteMetric1_Type(Integer32):
    """Custom type bosIpRouteMetric1 based on Integer32"""
    defaultValue = -1


_BosIpRouteMetric1_Type.__name__ = "Integer32"
_BosIpRouteMetric1_Object = MibTableColumn
bosIpRouteMetric1 = _BosIpRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 11),
    _BosIpRouteMetric1_Type()
)
bosIpRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpRouteMetric1.setStatus("current")


class _BosIpRoutePreference_Type(Integer32):
    """Custom type bosIpRoutePreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosIpRoutePreference_Type.__name__ = "Integer32"
_BosIpRoutePreference_Object = MibTableColumn
bosIpRoutePreference = _BosIpRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 12),
    _BosIpRoutePreference_Type()
)
bosIpRoutePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpRoutePreference.setStatus("current")
_BosIpRouteStatus_Type = RowStatus
_BosIpRouteStatus_Object = MibTableColumn
bosIpRouteStatus = _BosIpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 22, 1, 13),
    _BosIpRouteStatus_Type()
)
bosIpRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpRouteStatus.setStatus("current")
_BosIpifTable_Object = MibTable
bosIpifTable = _BosIpifTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 23)
)
if mibBuilder.loadTexts:
    bosIpifTable.setStatus("current")
_BosIpifEntry_Object = MibTableRow
bosIpifEntry = _BosIpifEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 23, 1)
)
bosIpifEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosIpifIndex"),
)
if mibBuilder.loadTexts:
    bosIpifEntry.setStatus("current")


class _BosIpifIndex_Type(Integer32):
    """Custom type bosIpifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosIpifIndex_Type.__name__ = "Integer32"
_BosIpifIndex_Object = MibTableColumn
bosIpifIndex = _BosIpifIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 23, 1, 1),
    _BosIpifIndex_Type()
)
bosIpifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpifIndex.setStatus("current")


class _BosIpifMaxReasmSize_Type(Integer32):
    """Custom type bosIpifMaxReasmSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 33280),
    )


_BosIpifMaxReasmSize_Type.__name__ = "Integer32"
_BosIpifMaxReasmSize_Object = MibTableColumn
bosIpifMaxReasmSize = _BosIpifMaxReasmSize_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 23, 1, 2),
    _BosIpifMaxReasmSize_Type()
)
bosIpifMaxReasmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpifMaxReasmSize.setStatus("current")


class _BosIpifIcmpRedirectEnable_Type(Integer32):
    """Custom type bosIpifIcmpRedirectEnable based on Integer32"""
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


_BosIpifIcmpRedirectEnable_Type.__name__ = "Integer32"
_BosIpifIcmpRedirectEnable_Object = MibTableColumn
bosIpifIcmpRedirectEnable = _BosIpifIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 23, 1, 3),
    _BosIpifIcmpRedirectEnable_Type()
)
bosIpifIcmpRedirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpifIcmpRedirectEnable.setStatus("current")


class _BosIpifDrtBcastFwdingEnable_Type(Integer32):
    """Custom type bosIpifDrtBcastFwdingEnable based on Integer32"""
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


_BosIpifDrtBcastFwdingEnable_Type.__name__ = "Integer32"
_BosIpifDrtBcastFwdingEnable_Object = MibTableColumn
bosIpifDrtBcastFwdingEnable = _BosIpifDrtBcastFwdingEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 1, 23, 1, 4),
    _BosIpifDrtBcastFwdingEnable_Type()
)
bosIpifDrtBcastFwdingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpifDrtBcastFwdingEnable.setStatus("current")
_Bosicmp_ObjectIdentity = ObjectIdentity
bosicmp = _Bosicmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 3)
)
_BosIcmpInDomainNameRequests_Type = Counter32
_BosIcmpInDomainNameRequests_Object = MibScalar
bosIcmpInDomainNameRequests = _BosIcmpInDomainNameRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 3, 1),
    _BosIcmpInDomainNameRequests_Type()
)
bosIcmpInDomainNameRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIcmpInDomainNameRequests.setStatus("current")
_BosIcmpInDomainNameReply_Type = Counter32
_BosIcmpInDomainNameReply_Object = MibScalar
bosIcmpInDomainNameReply = _BosIcmpInDomainNameReply_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 3, 2),
    _BosIcmpInDomainNameReply_Type()
)
bosIcmpInDomainNameReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIcmpInDomainNameReply.setStatus("current")
_BosIcmpOutDomainNameRequests_Type = Counter32
_BosIcmpOutDomainNameRequests_Object = MibScalar
bosIcmpOutDomainNameRequests = _BosIcmpOutDomainNameRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 3, 3),
    _BosIcmpOutDomainNameRequests_Type()
)
bosIcmpOutDomainNameRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIcmpOutDomainNameRequests.setStatus("current")
_BosIcmpOutDomainNameReply_Type = Counter32
_BosIcmpOutDomainNameReply_Object = MibScalar
bosIcmpOutDomainNameReply = _BosIcmpOutDomainNameReply_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 3, 4),
    _BosIcmpOutDomainNameReply_Type()
)
bosIcmpOutDomainNameReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIcmpOutDomainNameReply.setStatus("current")


class _BosIcmpDirectQueryEnable_Type(Integer32):
    """Custom type bosIcmpDirectQueryEnable based on Integer32"""
    defaultValue = 2

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


_BosIcmpDirectQueryEnable_Type.__name__ = "Integer32"
_BosIcmpDirectQueryEnable_Object = MibScalar
bosIcmpDirectQueryEnable = _BosIcmpDirectQueryEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 3, 5),
    _BosIcmpDirectQueryEnable_Type()
)
bosIcmpDirectQueryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIcmpDirectQueryEnable.setStatus("current")
_BosIcmpInSecurityFailures_Type = Counter32
_BosIcmpInSecurityFailures_Object = MibScalar
bosIcmpInSecurityFailures = _BosIcmpInSecurityFailures_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 3, 6),
    _BosIcmpInSecurityFailures_Type()
)
bosIcmpInSecurityFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIcmpInSecurityFailures.setStatus("current")
_BosIcmpOutSecurityFailures_Type = Counter32
_BosIcmpOutSecurityFailures_Object = MibScalar
bosIcmpOutSecurityFailures = _BosIcmpOutSecurityFailures_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 3, 7),
    _BosIcmpOutSecurityFailures_Type()
)
bosIcmpOutSecurityFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIcmpOutSecurityFailures.setStatus("current")
_Bosudp_ObjectIdentity = ObjectIdentity
bosudp = _Bosudp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 4)
)
_BosUdpInNoCksum_Type = Counter32
_BosUdpInNoCksum_Object = MibScalar
bosUdpInNoCksum = _BosUdpInNoCksum_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 4, 1),
    _BosUdpInNoCksum_Type()
)
bosUdpInNoCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosUdpInNoCksum.setStatus("current")
_BosUdpInIcmpErr_Type = Counter32
_BosUdpInIcmpErr_Object = MibScalar
bosUdpInIcmpErr = _BosUdpInIcmpErr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 4, 2),
    _BosUdpInIcmpErr_Type()
)
bosUdpInIcmpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosUdpInIcmpErr.setStatus("current")
_BosUdpInErrCksum_Type = Counter32
_BosUdpInErrCksum_Object = MibScalar
bosUdpInErrCksum = _BosUdpInErrCksum_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 4, 3),
    _BosUdpInErrCksum_Type()
)
bosUdpInErrCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosUdpInErrCksum.setStatus("current")
_BosUdpInBcast_Type = Counter32
_BosUdpInBcast_Object = MibScalar
bosUdpInBcast = _BosUdpInBcast_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 4, 4),
    _BosUdpInBcast_Type()
)
bosUdpInBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosUdpInBcast.setStatus("current")
_Bossystemresize_ObjectIdentity = ObjectIdentity
bossystemresize = _Bossystemresize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 16)
)
_BosNoOfReassemblyLists_Type = Integer32
_BosNoOfReassemblyLists_Object = MibScalar
bosNoOfReassemblyLists = _BosNoOfReassemblyLists_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 16, 3),
    _BosNoOfReassemblyLists_Type()
)
bosNoOfReassemblyLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosNoOfReassemblyLists.setStatus("current")
_BosNoOfFragmentsPerList_Type = Integer32
_BosNoOfFragmentsPerList_Object = MibScalar
bosNoOfFragmentsPerList = _BosNoOfFragmentsPerList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 16, 4),
    _BosNoOfFragmentsPerList_Type()
)
bosNoOfFragmentsPerList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosNoOfFragmentsPerList.setStatus("current")
_Boslogandtrace_ObjectIdentity = ObjectIdentity
boslogandtrace = _Boslogandtrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 17)
)
_BosIpGlobalDebug_Type = Integer32
_BosIpGlobalDebug_Object = MibScalar
bosIpGlobalDebug = _BosIpGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 2, 17, 1),
    _BosIpGlobalDebug_Type()
)
bosIpGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpGlobalDebug.setStatus("current")
_Bosntp_ObjectIdentity = ObjectIdentity
bosntp = _Bosntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15)
)
_NtpCfg_ObjectIdentity = ObjectIdentity
ntpCfg = _NtpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1)
)


class _NtpCfgAdminStatus_Type(Integer32):
    """Custom type ntpCfgAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NtpCfgAdminStatus_Type.__name__ = "Integer32"
_NtpCfgAdminStatus_Object = MibScalar
ntpCfgAdminStatus = _NtpCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 1),
    _NtpCfgAdminStatus_Type()
)
ntpCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCfgAdminStatus.setStatus("current")


class _NtpCfgPollInterval_Type(Integer32):
    """Custom type ntpCfgPollInterval based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_NtpCfgPollInterval_Type.__name__ = "Integer32"
_NtpCfgPollInterval_Object = MibScalar
ntpCfgPollInterval = _NtpCfgPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 2),
    _NtpCfgPollInterval_Type()
)
ntpCfgPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCfgPollInterval.setStatus("current")
_NtpCfgPriServer_Type = IpAddress
_NtpCfgPriServer_Object = MibScalar
ntpCfgPriServer = _NtpCfgPriServer_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 3),
    _NtpCfgPriServer_Type()
)
ntpCfgPriServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCfgPriServer.setStatus("current")
_NtpCfgSecServer_Type = IpAddress
_NtpCfgSecServer_Object = MibScalar
ntpCfgSecServer = _NtpCfgSecServer_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 4),
    _NtpCfgSecServer_Type()
)
ntpCfgSecServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpCfgSecServer.setStatus("current")
_NtpSysTime_Type = DisplayString
_NtpSysTime_Object = MibScalar
ntpSysTime = _NtpSysTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 5),
    _NtpSysTime_Type()
)
ntpSysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysTime.setStatus("current")
_NtpLastUpdtTime_Type = DisplayString
_NtpLastUpdtTime_Object = MibScalar
ntpLastUpdtTime = _NtpLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 6),
    _NtpLastUpdtTime_Type()
)
ntpLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpLastUpdtTime.setStatus("current")
_NtpLastUpdtServer_Type = IpAddress
_NtpLastUpdtServer_Object = MibScalar
ntpLastUpdtServer = _NtpLastUpdtServer_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 7),
    _NtpLastUpdtServer_Type()
)
ntpLastUpdtServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpLastUpdtServer.setStatus("current")
_NtpServerStatsTable_Object = MibTable
ntpServerStatsTable = _NtpServerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 8)
)
if mibBuilder.loadTexts:
    ntpServerStatsTable.setStatus("current")
_NtpServerStatsEntry_Object = MibTableRow
ntpServerStatsEntry = _NtpServerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 8, 1)
)
ntpServerStatsEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "ntpIpAddress"),
)
if mibBuilder.loadTexts:
    ntpServerStatsEntry.setStatus("current")
_NtpIpAddress_Type = IpAddress
_NtpIpAddress_Object = MibTableColumn
ntpIpAddress = _NtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 8, 1, 1),
    _NtpIpAddress_Type()
)
ntpIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpIpAddress.setStatus("current")
_NtpStatSerReq_Type = Counter32
_NtpStatSerReq_Object = MibTableColumn
ntpStatSerReq = _NtpStatSerReq_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 8, 1, 2),
    _NtpStatSerReq_Type()
)
ntpStatSerReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatSerReq.setStatus("current")
_NtpStatSerRep_Type = Counter32
_NtpStatSerRep_Object = MibTableColumn
ntpStatSerRep = _NtpStatSerRep_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 8, 1, 3),
    _NtpStatSerRep_Type()
)
ntpStatSerRep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatSerRep.setStatus("current")
_NtpStatSerUpd_Type = Counter32
_NtpStatSerUpd_Object = MibTableColumn
ntpStatSerUpd = _NtpStatSerUpd_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 8, 1, 4),
    _NtpStatSerUpd_Type()
)
ntpStatSerUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatSerUpd.setStatus("current")


class _NtpSerClearStat_Type(Integer32):
    """Custom type ntpSerClearStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_NtpSerClearStat_Type.__name__ = "Integer32"
_NtpSerClearStat_Object = MibTableColumn
ntpSerClearStat = _NtpSerClearStat_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 1, 8, 1, 5),
    _NtpSerClearStat_Type()
)
ntpSerClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpSerClearStat.setStatus("current")
_NtpOps_ObjectIdentity = ObjectIdentity
ntpOps = _NtpOps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 2)
)


class _NtpOpsPollServer_Type(Integer32):
    """Custom type ntpOpsPollServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NtpOpsPollServer_Type.__name__ = "Integer32"
_NtpOpsPollServer_Object = MibScalar
ntpOpsPollServer = _NtpOpsPollServer_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 15, 2, 1),
    _NtpOpsPollServer_Type()
)
ntpOpsPollServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpOpsPollServer.setStatus("current")
_Bostcp_ObjectIdentity = ObjectIdentity
bostcp = _Bostcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 18)
)
_BosTcpTraceDebug_Type = Integer32
_BosTcpTraceDebug_Object = MibScalar
bosTcpTraceDebug = _BosTcpTraceDebug_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 18, 1),
    _BosTcpTraceDebug_Type()
)
bosTcpTraceDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosTcpTraceDebug.setStatus("current")
_BosTcpConnTable_Object = MibTable
bosTcpConnTable = _BosTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 18, 2)
)
if mibBuilder.loadTexts:
    bosTcpConnTable.setStatus("current")
_BosTcpConnEntry_Object = MibTableRow
bosTcpConnEntry = _BosTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 18, 2, 1)
)
bosTcpConnEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosTcpConnLocalAddress"),
    (0, "BLADEOS-BASE-MIB", "bosTcpConnLocalPort"),
    (0, "BLADEOS-BASE-MIB", "bosTcpConnRemAddress"),
    (0, "BLADEOS-BASE-MIB", "bosTcpConnRemPort"),
)
if mibBuilder.loadTexts:
    bosTcpConnEntry.setStatus("current")
_BosTcpConnLocalAddress_Type = IpAddress
_BosTcpConnLocalAddress_Object = MibTableColumn
bosTcpConnLocalAddress = _BosTcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 18, 2, 1, 1),
    _BosTcpConnLocalAddress_Type()
)
bosTcpConnLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosTcpConnLocalAddress.setStatus("current")


class _BosTcpConnLocalPort_Type(Integer32):
    """Custom type bosTcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BosTcpConnLocalPort_Type.__name__ = "Integer32"
_BosTcpConnLocalPort_Object = MibTableColumn
bosTcpConnLocalPort = _BosTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 18, 2, 1, 2),
    _BosTcpConnLocalPort_Type()
)
bosTcpConnLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosTcpConnLocalPort.setStatus("current")
_BosTcpConnRemAddress_Type = IpAddress
_BosTcpConnRemAddress_Object = MibTableColumn
bosTcpConnRemAddress = _BosTcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 18, 2, 1, 3),
    _BosTcpConnRemAddress_Type()
)
bosTcpConnRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosTcpConnRemAddress.setStatus("current")


class _BosTcpConnRemPort_Type(Integer32):
    """Custom type bosTcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BosTcpConnRemPort_Type.__name__ = "Integer32"
_BosTcpConnRemPort_Object = MibTableColumn
bosTcpConnRemPort = _BosTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 18, 2, 1, 4),
    _BosTcpConnRemPort_Type()
)
bosTcpConnRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosTcpConnRemPort.setStatus("current")


class _BosTcpConnState_Type(Integer32):
    """Custom type bosTcpConnState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("listen", 2),
          ("synSent", 3),
          ("synReceived", 4),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("closeWait", 8),
          ("lastAck", 9),
          ("closing", 10),
          ("timeWait", 11),
          ("deleteTCB", 12))
    )


_BosTcpConnState_Type.__name__ = "Integer32"
_BosTcpConnState_Object = MibTableColumn
bosTcpConnState = _BosTcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 18, 2, 1, 5),
    _BosTcpConnState_Type()
)
bosTcpConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTcpConnState.setStatus("current")
_Bosradius_ObjectIdentity = ObjectIdentity
bosradius = _Bosradius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25)
)
_RadiusExtClient_ObjectIdentity = ObjectIdentity
radiusExtClient = _RadiusExtClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1)
)


class _RadiusExtDebugMask_Type(Integer32):
    """Custom type radiusExtDebugMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disableall", 0),
          ("enableall", 1),
          ("error", 2),
          ("event", 3),
          ("packet", 4),
          ("response", 5),
          ("timer", 6))
    )


_RadiusExtDebugMask_Type.__name__ = "Integer32"
_RadiusExtDebugMask_Object = MibScalar
radiusExtDebugMask = _RadiusExtDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 1),
    _RadiusExtDebugMask_Type()
)
radiusExtDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtDebugMask.setStatus("current")


class _RadiusMaxNoOfUserEntries_Type(Integer32):
    """Custom type radiusMaxNoOfUserEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RadiusMaxNoOfUserEntries_Type.__name__ = "Integer32"
_RadiusMaxNoOfUserEntries_Object = MibScalar
radiusMaxNoOfUserEntries = _RadiusMaxNoOfUserEntries_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 2),
    _RadiusMaxNoOfUserEntries_Type()
)
radiusMaxNoOfUserEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMaxNoOfUserEntries.setStatus("current")


class _RadiusSecureBackdoorStatus_Type(Integer32):
    """Custom type radiusSecureBackdoorStatus based on Integer32"""
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


_RadiusSecureBackdoorStatus_Type.__name__ = "Integer32"
_RadiusSecureBackdoorStatus_Object = MibScalar
radiusSecureBackdoorStatus = _RadiusSecureBackdoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 3),
    _RadiusSecureBackdoorStatus_Type()
)
radiusSecureBackdoorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSecureBackdoorStatus.setStatus("current")


class _RadiusNewCfgPort_Type(Integer32):
    """Custom type radiusNewCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 3000),
    )


_RadiusNewCfgPort_Type.__name__ = "Integer32"
_RadiusNewCfgPort_Object = MibScalar
radiusNewCfgPort = _RadiusNewCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 4),
    _RadiusNewCfgPort_Type()
)
radiusNewCfgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusNewCfgPort.setStatus("current")
_RadiusExtServerTable_Object = MibTable
radiusExtServerTable = _RadiusExtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 5)
)
if mibBuilder.loadTexts:
    radiusExtServerTable.setStatus("current")
_RadiusExtServerEntry_Object = MibTableRow
radiusExtServerEntry = _RadiusExtServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 5, 1)
)
radiusExtServerEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "radiusExtServerIndex"),
)
if mibBuilder.loadTexts:
    radiusExtServerEntry.setStatus("current")
_RadiusExtServerIndex_Type = InterfaceIndex
_RadiusExtServerIndex_Object = MibTableColumn
radiusExtServerIndex = _RadiusExtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 5, 1, 1),
    _RadiusExtServerIndex_Type()
)
radiusExtServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusExtServerIndex.setStatus("current")
_RadiusExtServerAddress_Type = IpAddress
_RadiusExtServerAddress_Object = MibTableColumn
radiusExtServerAddress = _RadiusExtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 5, 1, 2),
    _RadiusExtServerAddress_Type()
)
radiusExtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerAddress.setStatus("current")


class _RadiusExtServerType_Type(Integer32):
    """Custom type radiusExtServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auth", 1),
          ("acct", 2),
          ("both", 3))
    )


_RadiusExtServerType_Type.__name__ = "Integer32"
_RadiusExtServerType_Object = MibTableColumn
radiusExtServerType = _RadiusExtServerType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 5, 1, 3),
    _RadiusExtServerType_Type()
)
radiusExtServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerType.setStatus("current")
_RadiusExtServerSharedSecret_Type = DisplayString
_RadiusExtServerSharedSecret_Object = MibTableColumn
radiusExtServerSharedSecret = _RadiusExtServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 5, 1, 4),
    _RadiusExtServerSharedSecret_Type()
)
radiusExtServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerSharedSecret.setStatus("current")


class _RadiusExtServerEnabled_Type(Integer32):
    """Custom type radiusExtServerEnabled based on Integer32"""
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


_RadiusExtServerEnabled_Type.__name__ = "Integer32"
_RadiusExtServerEnabled_Object = MibTableColumn
radiusExtServerEnabled = _RadiusExtServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 5, 1, 5),
    _RadiusExtServerEnabled_Type()
)
radiusExtServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerEnabled.setStatus("current")


class _RadiusExtServerResponseTime_Type(Integer32):
    """Custom type radiusExtServerResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RadiusExtServerResponseTime_Type.__name__ = "Integer32"
_RadiusExtServerResponseTime_Object = MibTableColumn
radiusExtServerResponseTime = _RadiusExtServerResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 5, 1, 6),
    _RadiusExtServerResponseTime_Type()
)
radiusExtServerResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerResponseTime.setStatus("current")


class _RadiusExtServerMaximumRetransmission_Type(Integer32):
    """Custom type radiusExtServerMaximumRetransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_RadiusExtServerMaximumRetransmission_Type.__name__ = "Integer32"
_RadiusExtServerMaximumRetransmission_Object = MibTableColumn
radiusExtServerMaximumRetransmission = _RadiusExtServerMaximumRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 5, 1, 7),
    _RadiusExtServerMaximumRetransmission_Type()
)
radiusExtServerMaximumRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerMaximumRetransmission.setStatus("current")
_RadiusExtServerEntryStatus_Type = RowStatus
_RadiusExtServerEntryStatus_Object = MibTableColumn
radiusExtServerEntryStatus = _RadiusExtServerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 25, 1, 5, 1, 8),
    _RadiusExtServerEntryStatus_Type()
)
radiusExtServerEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerEntryStatus.setStatus("current")
_BosBridgeMIB_ObjectIdentity = ObjectIdentity
bosBridgeMIB = _BosBridgeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26)
)
_Dot1dBosBridge_ObjectIdentity = ObjectIdentity
dot1dBosBridge = _Dot1dBosBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1)
)
_Dot1dBosBase_ObjectIdentity = ObjectIdentity
dot1dBosBase = _Dot1dBosBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1)
)


class _Dot1dBridgeSystemControl_Type(Integer32):
    """Custom type dot1dBridgeSystemControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_Dot1dBridgeSystemControl_Type.__name__ = "Integer32"
_Dot1dBridgeSystemControl_Object = MibScalar
dot1dBridgeSystemControl = _Dot1dBridgeSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 1),
    _Dot1dBridgeSystemControl_Type()
)
dot1dBridgeSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dBridgeSystemControl.setStatus("current")


class _Dot1dBaseBridgeStatus_Type(Integer32):
    """Custom type dot1dBaseBridgeStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("downwithallinterfacesdown", 3))
    )


_Dot1dBaseBridgeStatus_Type.__name__ = "Integer32"
_Dot1dBaseBridgeStatus_Object = MibScalar
dot1dBaseBridgeStatus = _Dot1dBaseBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 2),
    _Dot1dBaseBridgeStatus_Type()
)
dot1dBaseBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dBaseBridgeStatus.setStatus("current")


class _Dot1dBaseBridgeCRCStatus_Type(Integer32):
    """Custom type dot1dBaseBridgeCRCStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("withCRC", 1),
          ("withoutCRC", 2))
    )


_Dot1dBaseBridgeCRCStatus_Type.__name__ = "Integer32"
_Dot1dBaseBridgeCRCStatus_Object = MibScalar
dot1dBaseBridgeCRCStatus = _Dot1dBaseBridgeCRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 3),
    _Dot1dBaseBridgeCRCStatus_Type()
)
dot1dBaseBridgeCRCStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dBaseBridgeCRCStatus.setStatus("current")


class _Dot1dBaseBridgeDebug_Type(Integer32):
    """Custom type dot1dBaseBridgeDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1dBaseBridgeDebug_Type.__name__ = "Integer32"
_Dot1dBaseBridgeDebug_Object = MibScalar
dot1dBaseBridgeDebug = _Dot1dBaseBridgeDebug_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 4),
    _Dot1dBaseBridgeDebug_Type()
)
dot1dBaseBridgeDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dBaseBridgeDebug.setStatus("current")


class _Dot1dBaseBridgeTrace_Type(Integer32):
    """Custom type dot1dBaseBridgeTrace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot1dBaseBridgeTrace_Type.__name__ = "Integer32"
_Dot1dBaseBridgeTrace_Object = MibScalar
dot1dBaseBridgeTrace = _Dot1dBaseBridgeTrace_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 5),
    _Dot1dBaseBridgeTrace_Type()
)
dot1dBaseBridgeTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dBaseBridgeTrace.setStatus("current")


class _Dot1dBaseBridgeMaxFwdDbEntries_Type(Integer32):
    """Custom type dot1dBaseBridgeMaxFwdDbEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dBaseBridgeMaxFwdDbEntries_Type.__name__ = "Integer32"
_Dot1dBaseBridgeMaxFwdDbEntries_Object = MibScalar
dot1dBaseBridgeMaxFwdDbEntries = _Dot1dBaseBridgeMaxFwdDbEntries_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 6),
    _Dot1dBaseBridgeMaxFwdDbEntries_Type()
)
dot1dBaseBridgeMaxFwdDbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBaseBridgeMaxFwdDbEntries.setStatus("current")
_Dot1dBosBasePortTable_Object = MibTable
dot1dBosBasePortTable = _Dot1dBosBasePortTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 7)
)
if mibBuilder.loadTexts:
    dot1dBosBasePortTable.setStatus("current")
_Dot1dBosBasePortEntry_Object = MibTableRow
dot1dBosBasePortEntry = _Dot1dBosBasePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 7, 1)
)
dot1dBosBasePortEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "dot1dBosBasePort"),
)
if mibBuilder.loadTexts:
    dot1dBosBasePortEntry.setStatus("current")


class _Dot1dBosBasePort_Type(Integer32):
    """Custom type dot1dBosBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dBosBasePort_Type.__name__ = "Integer32"
_Dot1dBosBasePort_Object = MibTableColumn
dot1dBosBasePort = _Dot1dBosBasePort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 7, 1, 1),
    _Dot1dBosBasePort_Type()
)
dot1dBosBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dBosBasePort.setStatus("current")


class _Dot1dBasePortAdminStatus_Type(Integer32):
    """Custom type dot1dBasePortAdminStatus based on Integer32"""
    defaultValue = 1

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


_Dot1dBasePortAdminStatus_Type.__name__ = "Integer32"
_Dot1dBasePortAdminStatus_Object = MibTableColumn
dot1dBasePortAdminStatus = _Dot1dBasePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 7, 1, 2),
    _Dot1dBasePortAdminStatus_Type()
)
dot1dBasePortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dBasePortAdminStatus.setStatus("current")


class _Dot1dBasePortOperStatus_Type(Integer32):
    """Custom type dot1dBasePortOperStatus based on Integer32"""
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


_Dot1dBasePortOperStatus_Type.__name__ = "Integer32"
_Dot1dBasePortOperStatus_Object = MibTableColumn
dot1dBasePortOperStatus = _Dot1dBasePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 7, 1, 3),
    _Dot1dBasePortOperStatus_Type()
)
dot1dBasePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortOperStatus.setStatus("current")


class _Dot1dBasePortBcastStatus_Type(Integer32):
    """Custom type dot1dBasePortBcastStatus based on Integer32"""
    defaultValue = 1

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


_Dot1dBasePortBcastStatus_Type.__name__ = "Integer32"
_Dot1dBasePortBcastStatus_Object = MibTableColumn
dot1dBasePortBcastStatus = _Dot1dBasePortBcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 7, 1, 4),
    _Dot1dBasePortBcastStatus_Type()
)
dot1dBasePortBcastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dBasePortBcastStatus.setStatus("current")


class _Dot1dBasePortFilterNumber_Type(Integer32):
    """Custom type dot1dBasePortFilterNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Dot1dBasePortFilterNumber_Type.__name__ = "Integer32"
_Dot1dBasePortFilterNumber_Object = MibTableColumn
dot1dBasePortFilterNumber = _Dot1dBasePortFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 7, 1, 5),
    _Dot1dBasePortFilterNumber_Type()
)
dot1dBasePortFilterNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dBasePortFilterNumber.setStatus("current")


class _Dot1dBasePortMcastNumber_Type(Integer32):
    """Custom type dot1dBasePortMcastNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Dot1dBasePortMcastNumber_Type.__name__ = "Integer32"
_Dot1dBasePortMcastNumber_Object = MibTableColumn
dot1dBasePortMcastNumber = _Dot1dBasePortMcastNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 7, 1, 6),
    _Dot1dBasePortMcastNumber_Type()
)
dot1dBasePortMcastNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dBasePortMcastNumber.setStatus("current")
_Dot1dBasePortBcastOutFrames_Type = Counter32
_Dot1dBasePortBcastOutFrames_Object = MibTableColumn
dot1dBasePortBcastOutFrames = _Dot1dBasePortBcastOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 7, 1, 7),
    _Dot1dBasePortBcastOutFrames_Type()
)
dot1dBasePortBcastOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortBcastOutFrames.setStatus("current")
_Dot1dBasePortMcastOutFrames_Type = Counter32
_Dot1dBasePortMcastOutFrames_Object = MibTableColumn
dot1dBasePortMcastOutFrames = _Dot1dBasePortMcastOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 1, 7, 1, 8),
    _Dot1dBasePortMcastOutFrames_Type()
)
dot1dBasePortMcastOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dBasePortMcastOutFrames.setStatus("current")
_Dot1dBosTp_ObjectIdentity = ObjectIdentity
dot1dBosTp = _Dot1dBosTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 2)
)
_Dot1dBosTpPortTable_Object = MibTable
dot1dBosTpPortTable = _Dot1dBosTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot1dBosTpPortTable.setStatus("current")
_Dot1dBosTpPortEntry_Object = MibTableRow
dot1dBosTpPortEntry = _Dot1dBosTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 2, 1, 1)
)
dot1dBosTpPortEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "dot1dBosTpPort"),
)
if mibBuilder.loadTexts:
    dot1dBosTpPortEntry.setStatus("current")


class _Dot1dBosTpPort_Type(Integer32):
    """Custom type dot1dBosTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dBosTpPort_Type.__name__ = "Integer32"
_Dot1dBosTpPort_Object = MibTableColumn
dot1dBosTpPort = _Dot1dBosTpPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 2, 1, 1, 1),
    _Dot1dBosTpPort_Type()
)
dot1dBosTpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dBosTpPort.setStatus("current")
_Dot1dTpPortInProtoDiscards_Type = Counter32
_Dot1dTpPortInProtoDiscards_Object = MibTableColumn
dot1dTpPortInProtoDiscards = _Dot1dTpPortInProtoDiscards_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 2, 1, 1, 2),
    _Dot1dTpPortInProtoDiscards_Type()
)
dot1dTpPortInProtoDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInProtoDiscards.setStatus("current")
_Dot1dTpPortInFilterDiscards_Type = Counter32
_Dot1dTpPortInFilterDiscards_Object = MibTableColumn
dot1dTpPortInFilterDiscards = _Dot1dTpPortInFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 2, 1, 1, 3),
    _Dot1dTpPortInFilterDiscards_Type()
)
dot1dTpPortInFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dTpPortInFilterDiscards.setStatus("current")


class _Dot1dTpPortProtocolFilterMask_Type(Integer32):
    """Custom type dot1dTpPortProtocolFilterMask based on Integer32"""
    defaultValue = 0


_Dot1dTpPortProtocolFilterMask_Type.__name__ = "Integer32"
_Dot1dTpPortProtocolFilterMask_Object = MibTableColumn
dot1dTpPortProtocolFilterMask = _Dot1dTpPortProtocolFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 2, 1, 1, 4),
    _Dot1dTpPortProtocolFilterMask_Type()
)
dot1dTpPortProtocolFilterMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dTpPortProtocolFilterMask.setStatus("current")
_Dot1dFilter_ObjectIdentity = ObjectIdentity
dot1dFilter = _Dot1dFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 3)
)
_Dot1dFilterTable_Object = MibTable
dot1dFilterTable = _Dot1dFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot1dFilterTable.setStatus("current")
_Dot1dFilterEntry_Object = MibTableRow
dot1dFilterEntry = _Dot1dFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 3, 1, 1)
)
dot1dFilterEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "dot1dFilterNumber"),
    (0, "BLADEOS-BASE-MIB", "dot1dFilterSrcAddress"),
    (0, "BLADEOS-BASE-MIB", "dot1dFilterDstAddress"),
)
if mibBuilder.loadTexts:
    dot1dFilterEntry.setStatus("current")


class _Dot1dFilterNumber_Type(Integer32):
    """Custom type dot1dFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Dot1dFilterNumber_Type.__name__ = "Integer32"
_Dot1dFilterNumber_Object = MibTableColumn
dot1dFilterNumber = _Dot1dFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 3, 1, 1, 1),
    _Dot1dFilterNumber_Type()
)
dot1dFilterNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dFilterNumber.setStatus("current")
_Dot1dFilterSrcAddress_Type = MacAddress
_Dot1dFilterSrcAddress_Object = MibTableColumn
dot1dFilterSrcAddress = _Dot1dFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 3, 1, 1, 2),
    _Dot1dFilterSrcAddress_Type()
)
dot1dFilterSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dFilterSrcAddress.setStatus("current")


class _Dot1dFilterSrcMask_Type(MacAddress):
    """Custom type dot1dFilterSrcMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_Dot1dFilterSrcMask_Type.__name__ = "MacAddress"
_Dot1dFilterSrcMask_Object = MibTableColumn
dot1dFilterSrcMask = _Dot1dFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 3, 1, 1, 3),
    _Dot1dFilterSrcMask_Type()
)
dot1dFilterSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dFilterSrcMask.setStatus("current")
_Dot1dFilterDstAddress_Type = MacAddress
_Dot1dFilterDstAddress_Object = MibTableColumn
dot1dFilterDstAddress = _Dot1dFilterDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 3, 1, 1, 4),
    _Dot1dFilterDstAddress_Type()
)
dot1dFilterDstAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dFilterDstAddress.setStatus("current")


class _Dot1dFilterDstMask_Type(MacAddress):
    """Custom type dot1dFilterDstMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_Dot1dFilterDstMask_Type.__name__ = "MacAddress"
_Dot1dFilterDstMask_Object = MibTableColumn
dot1dFilterDstMask = _Dot1dFilterDstMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 3, 1, 1, 5),
    _Dot1dFilterDstMask_Type()
)
dot1dFilterDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dFilterDstMask.setStatus("current")


class _Dot1dFilterPermiss_Type(Integer32):
    """Custom type dot1dFilterPermiss based on Integer32"""
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
        *(("block", 1),
          ("allow", 2),
          ("invalid", 3))
    )


_Dot1dFilterPermiss_Type.__name__ = "Integer32"
_Dot1dFilterPermiss_Object = MibTableColumn
dot1dFilterPermiss = _Dot1dFilterPermiss_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 3, 1, 1, 6),
    _Dot1dFilterPermiss_Type()
)
dot1dFilterPermiss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dFilterPermiss.setStatus("current")
_Dot1dMcast_ObjectIdentity = ObjectIdentity
dot1dMcast = _Dot1dMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 4)
)
_Dot1dMcastTable_Object = MibTable
dot1dMcastTable = _Dot1dMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dot1dMcastTable.setStatus("current")
_Dot1dMcastEntry_Object = MibTableRow
dot1dMcastEntry = _Dot1dMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 4, 1, 1)
)
dot1dMcastEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "dot1dMcastMacaddress"),
    (0, "BLADEOS-BASE-MIB", "dot1dMlistNumber"),
)
if mibBuilder.loadTexts:
    dot1dMcastEntry.setStatus("current")


class _Dot1dMlistNumber_Type(Integer32):
    """Custom type dot1dMlistNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_Dot1dMlistNumber_Type.__name__ = "Integer32"
_Dot1dMlistNumber_Object = MibTableColumn
dot1dMlistNumber = _Dot1dMlistNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 4, 1, 1, 1),
    _Dot1dMlistNumber_Type()
)
dot1dMlistNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dMlistNumber.setStatus("current")
_Dot1dMcastMacaddress_Type = MacAddress
_Dot1dMcastMacaddress_Object = MibTableColumn
dot1dMcastMacaddress = _Dot1dMcastMacaddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 4, 1, 1, 2),
    _Dot1dMcastMacaddress_Type()
)
dot1dMcastMacaddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1dMcastMacaddress.setStatus("current")


class _Dot1dMcastPermiss_Type(Integer32):
    """Custom type dot1dMcastPermiss based on Integer32"""
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
        *(("block", 1),
          ("allow", 2),
          ("invalid", 3))
    )


_Dot1dMcastPermiss_Type.__name__ = "Integer32"
_Dot1dMcastPermiss_Object = MibTableColumn
dot1dMcastPermiss = _Dot1dMcastPermiss_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 26, 1, 4, 1, 1, 3),
    _Dot1dMcastPermiss_Type()
)
dot1dMcastPermiss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1dMcastPermiss.setStatus("current")
_Boscfa_ObjectIdentity = ObjectIdentity
boscfa = _Boscfa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27)
)
__pysmi_if_ObjectIdentity = ObjectIdentity
_pysmi_if = __pysmi_if_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1)
)
_IfMaxInterfaces_Type = InterfaceIndex
_IfMaxInterfaces_Object = MibScalar
ifMaxInterfaces = _IfMaxInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 1),
    _IfMaxInterfaces_Type()
)
ifMaxInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMaxInterfaces.setStatus("deprecated")
_IfMaxPhysInterfaces_Type = InterfaceIndex
_IfMaxPhysInterfaces_Object = MibScalar
ifMaxPhysInterfaces = _IfMaxPhysInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 2),
    _IfMaxPhysInterfaces_Type()
)
ifMaxPhysInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMaxPhysInterfaces.setStatus("deprecated")
_IfMaxIpInterfaces_Type = InterfaceIndex
_IfMaxIpInterfaces_Object = MibScalar
ifMaxIpInterfaces = _IfMaxIpInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 3),
    _IfMaxIpInterfaces_Type()
)
ifMaxIpInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMaxIpInterfaces.setStatus("current")
_IfMaxMgmInterfaces_Type = InterfaceIndex
_IfMaxMgmInterfaces_Object = MibScalar
ifMaxMgmInterfaces = _IfMaxMgmInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 4),
    _IfMaxMgmInterfaces_Type()
)
ifMaxMgmInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMaxMgmInterfaces.setStatus("current")
_IfMaxLogicalInterfaces_Type = InterfaceIndex
_IfMaxLogicalInterfaces_Object = MibScalar
ifMaxLogicalInterfaces = _IfMaxLogicalInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 5),
    _IfMaxLogicalInterfaces_Type()
)
ifMaxLogicalInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMaxLogicalInterfaces.setStatus("current")
_IfAvailableIndex_Type = InterfaceIndex
_IfAvailableIndex_Object = MibScalar
ifAvailableIndex = _IfAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 6),
    _IfAvailableIndex_Type()
)
ifAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAvailableIndex.setStatus("current")
_IfMainTable_Object = MibTable
ifMainTable = _IfMainTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8)
)
if mibBuilder.loadTexts:
    ifMainTable.setStatus("current")
_IfMainEntry_Object = MibTableRow
ifMainEntry = _IfMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1)
)
ifMainEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifMainEntry.setStatus("current")
_IfMainIndex_Type = InterfaceIndex
_IfMainIndex_Object = MibTableColumn
ifMainIndex = _IfMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 1),
    _IfMainIndex_Type()
)
ifMainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifMainIndex.setStatus("current")


class _IfMainType_Type(Integer32):
    """Custom type ifMainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              9,
              23,
              24,
              32,
              38,
              49,
              84,
              92,
              108,
              114,
              118,
              131,
              134,
              136,
              150,
              161,
              166)
        )
    )
    namedValues = NamedValues(
        *(("rfc877x25", 5),
          ("ethernetCsmacd", 6),
          ("iso88025TokenRing", 9),
          ("ppp", 23),
          ("softwareLoopback", 24),
          ("frameRelay", 32),
          ("miox25", 38),
          ("aal5", 49),
          ("async", 84),
          ("frameRelayMPI", 92),
          ("pppMultilinkBundle", 108),
          ("ipOverAtm", 114),
          ("hdlc", 118),
          ("tunnel", 131),
          ("atmSubInterface", 134),
          ("l3ipvlan", 136),
          ("mplsTunnel", 150),
          ("ieee8023ad", 161),
          ("mpls", 166))
    )


_IfMainType_Type.__name__ = "Integer32"
_IfMainType_Object = MibTableColumn
ifMainType = _IfMainType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 2),
    _IfMainType_Type()
)
ifMainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainType.setStatus("current")
_IfMainMtu_Type = Integer32
_IfMainMtu_Object = MibTableColumn
ifMainMtu = _IfMainMtu_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 3),
    _IfMainMtu_Type()
)
ifMainMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainMtu.setStatus("current")


class _IfMainAdminStatus_Type(Integer32):
    """Custom type ifMainAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_IfMainAdminStatus_Type.__name__ = "Integer32"
_IfMainAdminStatus_Object = MibTableColumn
ifMainAdminStatus = _IfMainAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 4),
    _IfMainAdminStatus_Type()
)
ifMainAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainAdminStatus.setStatus("current")


class _IfMainOperStatus_Type(Integer32):
    """Custom type ifMainOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_IfMainOperStatus_Type.__name__ = "Integer32"
_IfMainOperStatus_Object = MibTableColumn
ifMainOperStatus = _IfMainOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 5),
    _IfMainOperStatus_Type()
)
ifMainOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainOperStatus.setStatus("current")


class _IfMainEncapType_Type(Integer32):
    """Custom type ifMainEncapType based on Integer32"""
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
        *(("other", 1),
          ("nlpid", 2),
          ("nlpidSnap", 3),
          ("cudNlpid", 4),
          ("cudNlpidSnap", 5),
          ("llcSnap", 6),
          ("vcMultiplexed", 7),
          ("ethernetV2", 8))
    )


_IfMainEncapType_Type.__name__ = "Integer32"
_IfMainEncapType_Object = MibTableColumn
ifMainEncapType = _IfMainEncapType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 6),
    _IfMainEncapType_Type()
)
ifMainEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainEncapType.setStatus("current")


class _IfMainBrgPortType_Type(Integer32):
    """Custom type ifMainBrgPortType based on Integer32"""
    defaultValue = 8

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
        *(("providerNetworkPort", 1),
          ("customerNetworkPortPortBased", 2),
          ("customerNetworkPortStagged", 3),
          ("customerEdgePort", 4),
          ("propCustomerEdgePort", 5),
          ("propCustomerNetworkPort", 6),
          ("propProviderNetworkPort", 7),
          ("customerBridgePort", 8))
    )


_IfMainBrgPortType_Type.__name__ = "Integer32"
_IfMainBrgPortType_Object = MibTableColumn
ifMainBrgPortType = _IfMainBrgPortType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 7),
    _IfMainBrgPortType_Type()
)
ifMainBrgPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainBrgPortType.setStatus("current")
_IfMainRowStatus_Type = RowStatus
_IfMainRowStatus_Object = MibTableColumn
ifMainRowStatus = _IfMainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 8),
    _IfMainRowStatus_Type()
)
ifMainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainRowStatus.setStatus("current")
_IfMainPortName_Type = DisplayString
_IfMainPortName_Object = MibTableColumn
ifMainPortName = _IfMainPortName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 9),
    _IfMainPortName_Type()
)
ifMainPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainPortName.setStatus("current")
_IfMainLinkStateChangeCount_Type = Counter32
_IfMainLinkStateChangeCount_Object = MibTableColumn
ifMainLinkStateChangeCount = _IfMainLinkStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 11),
    _IfMainLinkStateChangeCount_Type()
)
ifMainLinkStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainLinkStateChangeCount.setStatus("current")
_IfMainVlanId_Type = Integer32
_IfMainVlanId_Object = MibTableColumn
ifMainVlanId = _IfMainVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 12),
    _IfMainVlanId_Type()
)
ifMainVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainVlanId.setStatus("current")
_IfMainIntfIpNum_Type = Integer32
_IfMainIntfIpNum_Object = MibTableColumn
ifMainIntfIpNum = _IfMainIntfIpNum_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 8, 1, 13),
    _IfMainIntfIpNum_Type()
)
ifMainIntfIpNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainIntfIpNum.setStatus("current")
_IfIpTable_Object = MibTable
ifIpTable = _IfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 9)
)
if mibBuilder.loadTexts:
    ifIpTable.setStatus("current")
_IfIpEntry_Object = MibTableRow
ifIpEntry = _IfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 9, 1)
)
ifIpEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifIpEntry.setStatus("current")


class _IfIpAddrAllocMethod_Type(Integer32):
    """Custom type ifIpAddrAllocMethod based on Integer32"""
    defaultValue = 4

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
        *(("manual", 1),
          ("negotiation", 2),
          ("dynamic", 3),
          ("none", 4))
    )


_IfIpAddrAllocMethod_Type.__name__ = "Integer32"
_IfIpAddrAllocMethod_Object = MibTableColumn
ifIpAddrAllocMethod = _IfIpAddrAllocMethod_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 9, 1, 1),
    _IfIpAddrAllocMethod_Type()
)
ifIpAddrAllocMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpAddrAllocMethod.setStatus("current")


class _IfIpAddr_Type(IpAddress):
    """Custom type ifIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IfIpAddr_Type.__name__ = "IpAddress"
_IfIpAddr_Object = MibTableColumn
ifIpAddr = _IfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 9, 1, 2),
    _IfIpAddr_Type()
)
ifIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpAddr.setStatus("current")
_IfIpSubnetMask_Type = IpAddress
_IfIpSubnetMask_Object = MibTableColumn
ifIpSubnetMask = _IfIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 9, 1, 3),
    _IfIpSubnetMask_Type()
)
ifIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpSubnetMask.setStatus("current")
_IfIpBroadcastAddr_Type = IpAddress
_IfIpBroadcastAddr_Object = MibTableColumn
ifIpBroadcastAddr = _IfIpBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 9, 1, 4),
    _IfIpBroadcastAddr_Type()
)
ifIpBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpBroadcastAddr.setStatus("current")


class _IfIpForwardingEnable_Type(TruthValue):
    """Custom type ifIpForwardingEnable based on TruthValue"""
    defaultValue = 1


_IfIpForwardingEnable_Type.__name__ = "TruthValue"
_IfIpForwardingEnable_Object = MibTableColumn
ifIpForwardingEnable = _IfIpForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 9, 1, 5),
    _IfIpForwardingEnable_Type()
)
ifIpForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpForwardingEnable.setStatus("current")


class _IfIpAddrAllocProtocol_Type(Integer32):
    """Custom type ifIpAddrAllocProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("dhcp", 2)
    )


_IfIpAddrAllocProtocol_Type.__name__ = "Integer32"
_IfIpAddrAllocProtocol_Object = MibTableColumn
ifIpAddrAllocProtocol = _IfIpAddrAllocProtocol_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 9, 1, 6),
    _IfIpAddrAllocProtocol_Type()
)
ifIpAddrAllocProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpAddrAllocProtocol.setStatus("current")
_IfIvrTable_Object = MibTable
ifIvrTable = _IfIvrTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 10)
)
if mibBuilder.loadTexts:
    ifIvrTable.setStatus("current")
_IfIvrEntry_Object = MibTableRow
ifIvrEntry = _IfIvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 10, 1)
)
ifIvrEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifIvrEntry.setStatus("current")
_IfIvrBridgedIface_Type = TruthValue
_IfIvrBridgedIface_Object = MibTableColumn
ifIvrBridgedIface = _IfIvrBridgedIface_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 1, 10, 1, 1),
    _IfIvrBridgedIface_Type()
)
ifIvrBridgedIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIvrBridgedIface.setStatus("current")
_Ff_ObjectIdentity = ObjectIdentity
ff = _Ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2)
)


class _FfFastForwardingEnable_Type(TruthValue):
    """Custom type ffFastForwardingEnable based on TruthValue"""
    defaultValue = 2


_FfFastForwardingEnable_Type.__name__ = "TruthValue"
_FfFastForwardingEnable_Object = MibScalar
ffFastForwardingEnable = _FfFastForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 1),
    _FfFastForwardingEnable_Type()
)
ffFastForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffFastForwardingEnable.setStatus("deprecated")


class _FfCacheSize_Type(Integer32):
    """Custom type ffCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_FfCacheSize_Type.__name__ = "Integer32"
_FfCacheSize_Object = MibScalar
ffCacheSize = _FfCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 2),
    _FfCacheSize_Type()
)
ffCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCacheSize.setStatus("deprecated")


class _FfIpChecksumValidationEnable_Type(TruthValue):
    """Custom type ffIpChecksumValidationEnable based on TruthValue"""
    defaultValue = 1


_FfIpChecksumValidationEnable_Type.__name__ = "TruthValue"
_FfIpChecksumValidationEnable_Object = MibScalar
ffIpChecksumValidationEnable = _FfIpChecksumValidationEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 3),
    _FfIpChecksumValidationEnable_Type()
)
ffIpChecksumValidationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffIpChecksumValidationEnable.setStatus("deprecated")
_FfCachePurgeCount_Type = Counter32
_FfCachePurgeCount_Object = MibScalar
ffCachePurgeCount = _FfCachePurgeCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 4),
    _FfCachePurgeCount_Type()
)
ffCachePurgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCachePurgeCount.setStatus("deprecated")
_FfCacheLastPurgeTime_Type = TimeStamp
_FfCacheLastPurgeTime_Object = MibScalar
ffCacheLastPurgeTime = _FfCacheLastPurgeTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 5),
    _FfCacheLastPurgeTime_Type()
)
ffCacheLastPurgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCacheLastPurgeTime.setStatus("deprecated")


class _FfStaticEntryInvalidTrapEnable_Type(TruthValue):
    """Custom type ffStaticEntryInvalidTrapEnable based on TruthValue"""
    defaultValue = 1


_FfStaticEntryInvalidTrapEnable_Type.__name__ = "TruthValue"
_FfStaticEntryInvalidTrapEnable_Object = MibScalar
ffStaticEntryInvalidTrapEnable = _FfStaticEntryInvalidTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 6),
    _FfStaticEntryInvalidTrapEnable_Type()
)
ffStaticEntryInvalidTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffStaticEntryInvalidTrapEnable.setStatus("deprecated")
_FfCurrentStaticEntryInvalidCount_Type = Counter32
_FfCurrentStaticEntryInvalidCount_Object = MibScalar
ffCurrentStaticEntryInvalidCount = _FfCurrentStaticEntryInvalidCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 7),
    _FfCurrentStaticEntryInvalidCount_Type()
)
ffCurrentStaticEntryInvalidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCurrentStaticEntryInvalidCount.setStatus("deprecated")
_FfTotalEntryCount_Type = Counter32
_FfTotalEntryCount_Object = MibScalar
ffTotalEntryCount = _FfTotalEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 8),
    _FfTotalEntryCount_Type()
)
ffTotalEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffTotalEntryCount.setStatus("deprecated")
_FfStaticEntryCount_Type = Counter32
_FfStaticEntryCount_Object = MibScalar
ffStaticEntryCount = _FfStaticEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 9),
    _FfStaticEntryCount_Type()
)
ffStaticEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffStaticEntryCount.setStatus("deprecated")
_FfTotalPktsFastForwarded_Type = Counter32
_FfTotalPktsFastForwarded_Object = MibScalar
ffTotalPktsFastForwarded = _FfTotalPktsFastForwarded_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 10),
    _FfTotalPktsFastForwarded_Type()
)
ffTotalPktsFastForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffTotalPktsFastForwarded.setStatus("deprecated")
_FfHostCacheTable_Object = MibTable
ffHostCacheTable = _FfHostCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 11)
)
if mibBuilder.loadTexts:
    ffHostCacheTable.setStatus("deprecated")
_FfHostCacheEntry_Object = MibTableRow
ffHostCacheEntry = _FfHostCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 11, 1)
)
ffHostCacheEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "ffHostCacheDestAddr"),
)
if mibBuilder.loadTexts:
    ffHostCacheEntry.setStatus("deprecated")
_FfHostCacheDestAddr_Type = IpAddress
_FfHostCacheDestAddr_Object = MibTableColumn
ffHostCacheDestAddr = _FfHostCacheDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 11, 1, 1),
    _FfHostCacheDestAddr_Type()
)
ffHostCacheDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ffHostCacheDestAddr.setStatus("deprecated")
_FfHostCacheNextHopAddr_Type = IpAddress
_FfHostCacheNextHopAddr_Object = MibTableColumn
ffHostCacheNextHopAddr = _FfHostCacheNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 11, 1, 2),
    _FfHostCacheNextHopAddr_Type()
)
ffHostCacheNextHopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ffHostCacheNextHopAddr.setStatus("deprecated")
_FfHostCacheIfIndex_Type = InterfaceIndex
_FfHostCacheIfIndex_Object = MibTableColumn
ffHostCacheIfIndex = _FfHostCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 11, 1, 3),
    _FfHostCacheIfIndex_Type()
)
ffHostCacheIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ffHostCacheIfIndex.setStatus("deprecated")


class _FfHostCacheNextHopMediaAddr_Type(OctetString):
    """Custom type ffHostCacheNextHopMediaAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_FfHostCacheNextHopMediaAddr_Type.__name__ = "OctetString"
_FfHostCacheNextHopMediaAddr_Object = MibTableColumn
ffHostCacheNextHopMediaAddr = _FfHostCacheNextHopMediaAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 11, 1, 4),
    _FfHostCacheNextHopMediaAddr_Type()
)
ffHostCacheNextHopMediaAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ffHostCacheNextHopMediaAddr.setStatus("deprecated")
_FfHostCacheHits_Type = Counter32
_FfHostCacheHits_Object = MibTableColumn
ffHostCacheHits = _FfHostCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 11, 1, 5),
    _FfHostCacheHits_Type()
)
ffHostCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffHostCacheHits.setStatus("deprecated")
_FfHostCacheLastHitTime_Type = TimeStamp
_FfHostCacheLastHitTime_Object = MibTableColumn
ffHostCacheLastHitTime = _FfHostCacheLastHitTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 11, 1, 6),
    _FfHostCacheLastHitTime_Type()
)
ffHostCacheLastHitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffHostCacheLastHitTime.setStatus("deprecated")


class _FfHostCacheEntryType_Type(Integer32):
    """Custom type ffHostCacheEntryType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_FfHostCacheEntryType_Type.__name__ = "Integer32"
_FfHostCacheEntryType_Object = MibTableColumn
ffHostCacheEntryType = _FfHostCacheEntryType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 11, 1, 7),
    _FfHostCacheEntryType_Type()
)
ffHostCacheEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ffHostCacheEntryType.setStatus("deprecated")
_FfHostCacheRowStatus_Type = RowStatus
_FfHostCacheRowStatus_Object = MibTableColumn
ffHostCacheRowStatus = _FfHostCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 2, 11, 1, 8),
    _FfHostCacheRowStatus_Type()
)
ffHostCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ffHostCacheRowStatus.setStatus("deprecated")
_Fm_ObjectIdentity = ObjectIdentity
fm = _Fm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 3)
)


class _FmMemoryResourceTrapEnable_Type(TruthValue):
    """Custom type fmMemoryResourceTrapEnable based on TruthValue"""
    defaultValue = 1


_FmMemoryResourceTrapEnable_Type.__name__ = "TruthValue"
_FmMemoryResourceTrapEnable_Object = MibScalar
fmMemoryResourceTrapEnable = _FmMemoryResourceTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 3, 1),
    _FmMemoryResourceTrapEnable_Type()
)
fmMemoryResourceTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmMemoryResourceTrapEnable.setStatus("deprecated")


class _FmTimersResourceTrapEnable_Type(TruthValue):
    """Custom type fmTimersResourceTrapEnable based on TruthValue"""
    defaultValue = 1


_FmTimersResourceTrapEnable_Type.__name__ = "TruthValue"
_FmTimersResourceTrapEnable_Object = MibScalar
fmTimersResourceTrapEnable = _FmTimersResourceTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 3, 2),
    _FmTimersResourceTrapEnable_Type()
)
fmTimersResourceTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmTimersResourceTrapEnable.setStatus("deprecated")


class _FmTracingEnable_Type(Integer32):
    """Custom type fmTracingEnable based on Integer32"""
    defaultValue = 0


_FmTracingEnable_Type.__name__ = "Integer32"
_FmTracingEnable_Object = MibScalar
fmTracingEnable = _FmTracingEnable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 3, 3),
    _FmTracingEnable_Type()
)
fmTracingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmTracingEnable.setStatus("deprecated")
_FmMemAllocFailCount_Type = Counter32
_FmMemAllocFailCount_Object = MibScalar
fmMemAllocFailCount = _FmMemAllocFailCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 3, 4),
    _FmMemAllocFailCount_Type()
)
fmMemAllocFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmMemAllocFailCount.setStatus("current")
_FmTimerReqFailCount_Type = Counter32
_FmTimerReqFailCount_Object = MibScalar
fmTimerReqFailCount = _FmTimerReqFailCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 3, 5),
    _FmTimerReqFailCount_Type()
)
fmTimerReqFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmTimerReqFailCount.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 4)
)
_TrapPrefix_ObjectIdentity = ObjectIdentity
trapPrefix = _TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 4, 0)
)
_Bosrmon_ObjectIdentity = ObjectIdentity
bosrmon = _Bosrmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 44)
)
_RmonDebugType_Type = Unsigned32
_RmonDebugType_Object = MibScalar
rmonDebugType = _RmonDebugType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 44, 1),
    _RmonDebugType_Type()
)
rmonDebugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonDebugType.setStatus("current")


class _RmonEnableStatus_Type(Integer32):
    """Custom type rmonEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rmonenabled", 1),
          ("rmondisabled", 2))
    )


_RmonEnableStatus_Type.__name__ = "Integer32"
_RmonEnableStatus_Object = MibScalar
rmonEnableStatus = _RmonEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 44, 2),
    _RmonEnableStatus_Type()
)
rmonEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEnableStatus.setStatus("current")


class _RmonHwStatsSupp_Type(Integer32):
    """Custom type rmonHwStatsSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwStatsSupp_Type.__name__ = "Integer32"
_RmonHwStatsSupp_Object = MibScalar
rmonHwStatsSupp = _RmonHwStatsSupp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 44, 3),
    _RmonHwStatsSupp_Type()
)
rmonHwStatsSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwStatsSupp.setStatus("current")


class _RmonHwHistorySupp_Type(Integer32):
    """Custom type rmonHwHistorySupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwHistorySupp_Type.__name__ = "Integer32"
_RmonHwHistorySupp_Object = MibScalar
rmonHwHistorySupp = _RmonHwHistorySupp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 44, 4),
    _RmonHwHistorySupp_Type()
)
rmonHwHistorySupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwHistorySupp.setStatus("current")


class _RmonHwAlarmSupp_Type(Integer32):
    """Custom type rmonHwAlarmSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwAlarmSupp_Type.__name__ = "Integer32"
_RmonHwAlarmSupp_Object = MibScalar
rmonHwAlarmSupp = _RmonHwAlarmSupp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 44, 5),
    _RmonHwAlarmSupp_Type()
)
rmonHwAlarmSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwAlarmSupp.setStatus("current")


class _RmonHwHostSupp_Type(Integer32):
    """Custom type rmonHwHostSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwHostSupp_Type.__name__ = "Integer32"
_RmonHwHostSupp_Object = MibScalar
rmonHwHostSupp = _RmonHwHostSupp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 44, 6),
    _RmonHwHostSupp_Type()
)
rmonHwHostSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwHostSupp.setStatus("current")


class _RmonHwHostTopNSupp_Type(Integer32):
    """Custom type rmonHwHostTopNSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwHostTopNSupp_Type.__name__ = "Integer32"
_RmonHwHostTopNSupp_Object = MibScalar
rmonHwHostTopNSupp = _RmonHwHostTopNSupp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 44, 7),
    _RmonHwHostTopNSupp_Type()
)
rmonHwHostTopNSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwHostTopNSupp.setStatus("current")


class _RmonHwMatrixSupp_Type(Integer32):
    """Custom type rmonHwMatrixSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwMatrixSupp_Type.__name__ = "Integer32"
_RmonHwMatrixSupp_Object = MibScalar
rmonHwMatrixSupp = _RmonHwMatrixSupp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 44, 8),
    _RmonHwMatrixSupp_Type()
)
rmonHwMatrixSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwMatrixSupp.setStatus("current")


class _RmonHwEventSupp_Type(Integer32):
    """Custom type rmonHwEventSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwEventSupp_Type.__name__ = "Integer32"
_RmonHwEventSupp_Object = MibScalar
rmonHwEventSupp = _RmonHwEventSupp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 44, 9),
    _RmonHwEventSupp_Type()
)
rmonHwEventSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwEventSupp.setStatus("current")
_Bosla_ObjectIdentity = ObjectIdentity
bosla = _Bosla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63)
)
_BosLaSystem_ObjectIdentity = ObjectIdentity
bosLaSystem = _BosLaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1)
)
_BosLaMaxPortsPerPortChannel_Type = Integer32
_BosLaMaxPortsPerPortChannel_Object = MibScalar
bosLaMaxPortsPerPortChannel = _BosLaMaxPortsPerPortChannel_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1, 1),
    _BosLaMaxPortsPerPortChannel_Type()
)
bosLaMaxPortsPerPortChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosLaMaxPortsPerPortChannel.setStatus("current")
_BosLaMaxPortChannels_Type = Integer32
_BosLaMaxPortChannels_Object = MibScalar
bosLaMaxPortChannels = _BosLaMaxPortChannels_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1, 2),
    _BosLaMaxPortChannels_Type()
)
bosLaMaxPortChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosLaMaxPortChannels.setStatus("current")
_BosLaActorSystemID_Type = MacAddress
_BosLaActorSystemID_Object = MibScalar
bosLaActorSystemID = _BosLaActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1, 3),
    _BosLaActorSystemID_Type()
)
bosLaActorSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosLaActorSystemID.setStatus("current")


class _BosLaGlobalTimeout_Type(Integer32):
    """Custom type bosLaGlobalTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("long", 0),
          ("short", 1))
    )


_BosLaGlobalTimeout_Type.__name__ = "Integer32"
_BosLaGlobalTimeout_Object = MibScalar
bosLaGlobalTimeout = _BosLaGlobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1, 4),
    _BosLaGlobalTimeout_Type()
)
bosLaGlobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaGlobalTimeout.setStatus("current")


class _BosLaHashCfgSmacState_Type(Integer32):
    """Custom type bosLaHashCfgSmacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosLaHashCfgSmacState_Type.__name__ = "Integer32"
_BosLaHashCfgSmacState_Object = MibScalar
bosLaHashCfgSmacState = _BosLaHashCfgSmacState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1, 5),
    _BosLaHashCfgSmacState_Type()
)
bosLaHashCfgSmacState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaHashCfgSmacState.setStatus("current")


class _BosLaHashCfgDmacState_Type(Integer32):
    """Custom type bosLaHashCfgDmacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosLaHashCfgDmacState_Type.__name__ = "Integer32"
_BosLaHashCfgDmacState_Object = MibScalar
bosLaHashCfgDmacState = _BosLaHashCfgDmacState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1, 6),
    _BosLaHashCfgDmacState_Type()
)
bosLaHashCfgDmacState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaHashCfgDmacState.setStatus("current")


class _BosLaHashCfgSIpState_Type(Integer32):
    """Custom type bosLaHashCfgSIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosLaHashCfgSIpState_Type.__name__ = "Integer32"
_BosLaHashCfgSIpState_Object = MibScalar
bosLaHashCfgSIpState = _BosLaHashCfgSIpState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1, 7),
    _BosLaHashCfgSIpState_Type()
)
bosLaHashCfgSIpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaHashCfgSIpState.setStatus("current")


class _BosLaHashCfgDIpState_Type(Integer32):
    """Custom type bosLaHashCfgDIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosLaHashCfgDIpState_Type.__name__ = "Integer32"
_BosLaHashCfgDIpState_Object = MibScalar
bosLaHashCfgDIpState = _BosLaHashCfgDIpState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1, 8),
    _BosLaHashCfgDIpState_Type()
)
bosLaHashCfgDIpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaHashCfgDIpState.setStatus("current")


class _BosLaHashCfgSmacDmacState_Type(Integer32):
    """Custom type bosLaHashCfgSmacDmacState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosLaHashCfgSmacDmacState_Type.__name__ = "Integer32"
_BosLaHashCfgSmacDmacState_Object = MibScalar
bosLaHashCfgSmacDmacState = _BosLaHashCfgSmacDmacState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1, 9),
    _BosLaHashCfgSmacDmacState_Type()
)
bosLaHashCfgSmacDmacState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaHashCfgSmacDmacState.setStatus("current")


class _BosLaHashCfgSIpDIpState_Type(Integer32):
    """Custom type bosLaHashCfgSIpDIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosLaHashCfgSIpDIpState_Type.__name__ = "Integer32"
_BosLaHashCfgSIpDIpState_Object = MibScalar
bosLaHashCfgSIpDIpState = _BosLaHashCfgSIpDIpState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 1, 10),
    _BosLaHashCfgSIpDIpState_Type()
)
bosLaHashCfgSIpDIpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaHashCfgSIpDIpState.setStatus("current")
_BosLaPortChannel_ObjectIdentity = ObjectIdentity
bosLaPortChannel = _BosLaPortChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2)
)
_BosLaPortChannelTable_Object = MibTable
bosLaPortChannelTable = _BosLaPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2, 1)
)
if mibBuilder.loadTexts:
    bosLaPortChannelTable.setStatus("current")
_BosLaPortChannelEntry_Object = MibTableRow
bosLaPortChannelEntry = _BosLaPortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2, 1, 1)
)
bosLaPortChannelEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosLaPortChannelIfIndex"),
)
if mibBuilder.loadTexts:
    bosLaPortChannelEntry.setStatus("current")
_BosLaPortChannelIfIndex_Type = InterfaceIndex
_BosLaPortChannelIfIndex_Object = MibTableColumn
bosLaPortChannelIfIndex = _BosLaPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2, 1, 1, 1),
    _BosLaPortChannelIfIndex_Type()
)
bosLaPortChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosLaPortChannelIfIndex.setStatus("current")
_BosLaPortChannelGroup_Type = LacpKey
_BosLaPortChannelGroup_Object = MibTableColumn
bosLaPortChannelGroup = _BosLaPortChannelGroup_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2, 1, 1, 2),
    _BosLaPortChannelGroup_Type()
)
bosLaPortChannelGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosLaPortChannelGroup.setStatus("current")
_BosLaPortChannelAdminMacAddress_Type = MacAddress
_BosLaPortChannelAdminMacAddress_Object = MibTableColumn
bosLaPortChannelAdminMacAddress = _BosLaPortChannelAdminMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2, 1, 1, 3),
    _BosLaPortChannelAdminMacAddress_Type()
)
bosLaPortChannelAdminMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaPortChannelAdminMacAddress.setStatus("current")


class _BosLaPortChannelMacSelection_Type(Integer32):
    """Custom type bosLaPortChannelMacSelection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("force", 2))
    )


_BosLaPortChannelMacSelection_Type.__name__ = "Integer32"
_BosLaPortChannelMacSelection_Object = MibTableColumn
bosLaPortChannelMacSelection = _BosLaPortChannelMacSelection_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2, 1, 1, 4),
    _BosLaPortChannelMacSelection_Type()
)
bosLaPortChannelMacSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaPortChannelMacSelection.setStatus("current")
_BosLaPortChannelMode_Type = PortLaMode
_BosLaPortChannelMode_Object = MibTableColumn
bosLaPortChannelMode = _BosLaPortChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2, 1, 1, 5),
    _BosLaPortChannelMode_Type()
)
bosLaPortChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosLaPortChannelMode.setStatus("current")
_BosLaPortChannelPortCount_Type = Integer32
_BosLaPortChannelPortCount_Object = MibTableColumn
bosLaPortChannelPortCount = _BosLaPortChannelPortCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2, 1, 1, 6),
    _BosLaPortChannelPortCount_Type()
)
bosLaPortChannelPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosLaPortChannelPortCount.setStatus("current")
_BosLaPortChannelActivePortCount_Type = Integer32
_BosLaPortChannelActivePortCount_Object = MibTableColumn
bosLaPortChannelActivePortCount = _BosLaPortChannelActivePortCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2, 1, 1, 7),
    _BosLaPortChannelActivePortCount_Type()
)
bosLaPortChannelActivePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosLaPortChannelActivePortCount.setStatus("current")


class _BosLaPortChannelDefaultPortIndex_Type(InterfaceIndexOrZero):
    """Custom type bosLaPortChannelDefaultPortIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_BosLaPortChannelDefaultPortIndex_Type.__name__ = "InterfaceIndexOrZero"
_BosLaPortChannelDefaultPortIndex_Object = MibTableColumn
bosLaPortChannelDefaultPortIndex = _BosLaPortChannelDefaultPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 2, 1, 1, 8),
    _BosLaPortChannelDefaultPortIndex_Type()
)
bosLaPortChannelDefaultPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaPortChannelDefaultPortIndex.setStatus("current")
_BosLaPort_ObjectIdentity = ObjectIdentity
bosLaPort = _BosLaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3)
)
_BosLaPortTable_Object = MibTable
bosLaPortTable = _BosLaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1)
)
if mibBuilder.loadTexts:
    bosLaPortTable.setStatus("current")
_BosLaPortEntry_Object = MibTableRow
bosLaPortEntry = _BosLaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1, 1)
)
bosLaPortEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosLaPortIndex"),
)
if mibBuilder.loadTexts:
    bosLaPortEntry.setStatus("current")
_BosLaPortIndex_Type = InterfaceIndex
_BosLaPortIndex_Object = MibTableColumn
bosLaPortIndex = _BosLaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1, 1, 1),
    _BosLaPortIndex_Type()
)
bosLaPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosLaPortIndex.setStatus("current")
_BosLaPortMode_Type = PortLaMode
_BosLaPortMode_Object = MibTableColumn
bosLaPortMode = _BosLaPortMode_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1, 1, 2),
    _BosLaPortMode_Type()
)
bosLaPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaPortMode.setStatus("current")


class _BosLaPortBundleState_Type(Integer32):
    """Custom type bosLaPortBundleState based on Integer32"""
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
        *(("upInBndl", 0),
          ("standby", 1),
          ("down", 2),
          ("upIndividual", 3))
    )


_BosLaPortBundleState_Type.__name__ = "Integer32"
_BosLaPortBundleState_Object = MibTableColumn
bosLaPortBundleState = _BosLaPortBundleState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1, 1, 3),
    _BosLaPortBundleState_Type()
)
bosLaPortBundleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosLaPortBundleState.setStatus("current")
_BosLaPortActorResetAdminState_Type = LacpState
_BosLaPortActorResetAdminState_Object = MibTableColumn
bosLaPortActorResetAdminState = _BosLaPortActorResetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1, 1, 4),
    _BosLaPortActorResetAdminState_Type()
)
bosLaPortActorResetAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaPortActorResetAdminState.setStatus("current")


class _BosLaPortAggregateWaitTime_Type(TimeTicks):
    """Custom type bosLaPortAggregateWaitTime based on TimeTicks"""
    defaultValue = 2


_BosLaPortAggregateWaitTime_Type.__name__ = "TimeTicks"
_BosLaPortAggregateWaitTime_Object = MibTableColumn
bosLaPortAggregateWaitTime = _BosLaPortAggregateWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1, 1, 5),
    _BosLaPortAggregateWaitTime_Type()
)
bosLaPortAggregateWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaPortAggregateWaitTime.setStatus("current")
_BosLaPortPartnerResetAdminState_Type = LacpState
_BosLaPortPartnerResetAdminState_Object = MibTableColumn
bosLaPortPartnerResetAdminState = _BosLaPortPartnerResetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1, 1, 6),
    _BosLaPortPartnerResetAdminState_Type()
)
bosLaPortPartnerResetAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaPortPartnerResetAdminState.setStatus("current")


class _BosLaPortActorAdminPort_Type(Integer32):
    """Custom type bosLaPortActorAdminPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BosLaPortActorAdminPort_Type.__name__ = "Integer32"
_BosLaPortActorAdminPort_Object = MibTableColumn
bosLaPortActorAdminPort = _BosLaPortActorAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1, 1, 7),
    _BosLaPortActorAdminPort_Type()
)
bosLaPortActorAdminPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaPortActorAdminPort.setStatus("current")
_BosLaPortRestoreMtu_Type = Integer32
_BosLaPortRestoreMtu_Object = MibTableColumn
bosLaPortRestoreMtu = _BosLaPortRestoreMtu_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1, 1, 8),
    _BosLaPortRestoreMtu_Type()
)
bosLaPortRestoreMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLaPortRestoreMtu.setStatus("current")


class _BosLaPortSelectAggregator_Type(Integer32):
    """Custom type bosLaPortSelectAggregator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_BosLaPortSelectAggregator_Type.__name__ = "Integer32"
_BosLaPortSelectAggregator_Object = MibTableColumn
bosLaPortSelectAggregator = _BosLaPortSelectAggregator_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 3, 1, 1, 9),
    _BosLaPortSelectAggregator_Type()
)
bosLaPortSelectAggregator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosLaPortSelectAggregator.setStatus("current")
_BosLaTraps_ObjectIdentity = ObjectIdentity
bosLaTraps = _BosLaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 4)
)
_BosLaLacpTraps_ObjectIdentity = ObjectIdentity
bosLaLacpTraps = _BosLaLacpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 4, 0)
)
_Bospnac_ObjectIdentity = ObjectIdentity
bospnac = _Bospnac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64)
)
_BosPnacPaeSystem_ObjectIdentity = ObjectIdentity
bosPnacPaeSystem = _BosPnacPaeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1)
)


class _BosPnacSystemControl_Type(Integer32):
    """Custom type bosPnacSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_BosPnacSystemControl_Type.__name__ = "Integer32"
_BosPnacSystemControl_Object = MibScalar
bosPnacSystemControl = _BosPnacSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 1),
    _BosPnacSystemControl_Type()
)
bosPnacSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacSystemControl.setStatus("current")


class _BosPnacTraceOption_Type(Integer32):
    """Custom type bosPnacTraceOption based on Integer32"""
    defaultValue = 1


_BosPnacTraceOption_Type.__name__ = "Integer32"
_BosPnacTraceOption_Object = MibScalar
bosPnacTraceOption = _BosPnacTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 2),
    _BosPnacTraceOption_Type()
)
bosPnacTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacTraceOption.setStatus("current")
_BosPnacAuthenticServer_Type = AuthenticMethod
_BosPnacAuthenticServer_Object = MibScalar
bosPnacAuthenticServer = _BosPnacAuthenticServer_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 3),
    _BosPnacAuthenticServer_Type()
)
bosPnacAuthenticServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacAuthenticServer.setStatus("current")
_BosPnacNasId_Type = DisplayString
_BosPnacNasId_Object = MibScalar
bosPnacNasId = _BosPnacNasId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 4),
    _BosPnacNasId_Type()
)
bosPnacNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacNasId.setStatus("current")
_BosPnacPaePortTable_Object = MibTable
bosPnacPaePortTable = _BosPnacPaePortTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 5)
)
if mibBuilder.loadTexts:
    bosPnacPaePortTable.setStatus("current")
_BosPnacPaePortEntry_Object = MibTableRow
bosPnacPaePortEntry = _BosPnacPaePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 5, 1)
)
bosPnacPaePortEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPnacPaePortNumber"),
)
if mibBuilder.loadTexts:
    bosPnacPaePortEntry.setStatus("current")
_BosPnacPaePortNumber_Type = InterfaceIndex
_BosPnacPaePortNumber_Object = MibTableColumn
bosPnacPaePortNumber = _BosPnacPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 5, 1, 1),
    _BosPnacPaePortNumber_Type()
)
bosPnacPaePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosPnacPaePortNumber.setStatus("current")


class _BosPnacPaePortAuthMode_Type(Integer32):
    """Custom type bosPnacPaePortAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 1),
          ("macBased", 2))
    )


_BosPnacPaePortAuthMode_Type.__name__ = "Integer32"
_BosPnacPaePortAuthMode_Object = MibTableColumn
bosPnacPaePortAuthMode = _BosPnacPaePortAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 5, 1, 2),
    _BosPnacPaePortAuthMode_Type()
)
bosPnacPaePortAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacPaePortAuthMode.setStatus("current")
_BosPnacPaePortSupplicantCount_Type = Counter32
_BosPnacPaePortSupplicantCount_Object = MibTableColumn
bosPnacPaePortSupplicantCount = _BosPnacPaePortSupplicantCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 5, 1, 3),
    _BosPnacPaePortSupplicantCount_Type()
)
bosPnacPaePortSupplicantCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacPaePortSupplicantCount.setStatus("current")
_BosPnacPaePortUserName_Type = DisplayString
_BosPnacPaePortUserName_Object = MibTableColumn
bosPnacPaePortUserName = _BosPnacPaePortUserName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 5, 1, 4),
    _BosPnacPaePortUserName_Type()
)
bosPnacPaePortUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacPaePortUserName.setStatus("current")
_BosPnacPaePortPassword_Type = DisplayString
_BosPnacPaePortPassword_Object = MibTableColumn
bosPnacPaePortPassword = _BosPnacPaePortPassword_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 5, 1, 5),
    _BosPnacPaePortPassword_Type()
)
bosPnacPaePortPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacPaePortPassword.setStatus("current")
_BosPnacPaePortStatus_Type = PaeControlledPortStatus
_BosPnacPaePortStatus_Object = MibTableColumn
bosPnacPaePortStatus = _BosPnacPaePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 5, 1, 6),
    _BosPnacPaePortStatus_Type()
)
bosPnacPaePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacPaePortStatus.setStatus("current")


class _BosPnacModuleOperStatus_Type(Integer32):
    """Custom type bosPnacModuleOperStatus based on Integer32"""
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


_BosPnacModuleOperStatus_Type.__name__ = "Integer32"
_BosPnacModuleOperStatus_Object = MibScalar
bosPnacModuleOperStatus = _BosPnacModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 1, 6),
    _BosPnacModuleOperStatus_Type()
)
bosPnacModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacModuleOperStatus.setStatus("current")
_BosPnacPaeAuthenticator_ObjectIdentity = ObjectIdentity
bosPnacPaeAuthenticator = _BosPnacPaeAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2)
)
_BosPnacAuthSessionTable_Object = MibTable
bosPnacAuthSessionTable = _BosPnacAuthSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 1)
)
if mibBuilder.loadTexts:
    bosPnacAuthSessionTable.setStatus("current")
_BosPnacAuthSessionEntry_Object = MibTableRow
bosPnacAuthSessionEntry = _BosPnacAuthSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 1, 1)
)
bosPnacAuthSessionEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPnacAuthSessionSuppAddress"),
)
if mibBuilder.loadTexts:
    bosPnacAuthSessionEntry.setStatus("current")
_BosPnacAuthSessionSuppAddress_Type = MacAddress
_BosPnacAuthSessionSuppAddress_Object = MibTableColumn
bosPnacAuthSessionSuppAddress = _BosPnacAuthSessionSuppAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 1, 1, 1),
    _BosPnacAuthSessionSuppAddress_Type()
)
bosPnacAuthSessionSuppAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosPnacAuthSessionSuppAddress.setStatus("current")
_BosPnacAuthSessionIdentifier_Type = Integer32
_BosPnacAuthSessionIdentifier_Object = MibTableColumn
bosPnacAuthSessionIdentifier = _BosPnacAuthSessionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 1, 1, 2),
    _BosPnacAuthSessionIdentifier_Type()
)
bosPnacAuthSessionIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionIdentifier.setStatus("current")


class _BosPnacAuthSessionAuthPaeState_Type(Integer32):
    """Custom type bosPnacAuthSessionAuthPaeState based on Integer32"""
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
        *(("initialize", 1),
          ("disconnected", 2),
          ("connecting", 3),
          ("authenticating", 4),
          ("authenticated", 5),
          ("aborting", 6),
          ("held", 7),
          ("forceAuth", 8),
          ("forceUnauth", 9))
    )


_BosPnacAuthSessionAuthPaeState_Type.__name__ = "Integer32"
_BosPnacAuthSessionAuthPaeState_Object = MibTableColumn
bosPnacAuthSessionAuthPaeState = _BosPnacAuthSessionAuthPaeState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 1, 1, 3),
    _BosPnacAuthSessionAuthPaeState_Type()
)
bosPnacAuthSessionAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionAuthPaeState.setStatus("current")


class _BosPnacAuthSessionBackendAuthState_Type(Integer32):
    """Custom type bosPnacAuthSessionBackendAuthState based on Integer32"""
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
        *(("request", 1),
          ("response", 2),
          ("success", 3),
          ("fail", 4),
          ("timeout", 5),
          ("idle", 6),
          ("initialize", 7))
    )


_BosPnacAuthSessionBackendAuthState_Type.__name__ = "Integer32"
_BosPnacAuthSessionBackendAuthState_Object = MibTableColumn
bosPnacAuthSessionBackendAuthState = _BosPnacAuthSessionBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 1, 1, 4),
    _BosPnacAuthSessionBackendAuthState_Type()
)
bosPnacAuthSessionBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionBackendAuthState.setStatus("current")
_BosPnacAuthSessionPortStatus_Type = PaeControlledPortStatus
_BosPnacAuthSessionPortStatus_Object = MibTableColumn
bosPnacAuthSessionPortStatus = _BosPnacAuthSessionPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 1, 1, 5),
    _BosPnacAuthSessionPortStatus_Type()
)
bosPnacAuthSessionPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionPortStatus.setStatus("current")
_BosPnacAuthSessionPortNumber_Type = InterfaceIndex
_BosPnacAuthSessionPortNumber_Object = MibTableColumn
bosPnacAuthSessionPortNumber = _BosPnacAuthSessionPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 1, 1, 6),
    _BosPnacAuthSessionPortNumber_Type()
)
bosPnacAuthSessionPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionPortNumber.setStatus("current")
_BosPnacAuthSessionInitialize_Type = TruthValue
_BosPnacAuthSessionInitialize_Object = MibTableColumn
bosPnacAuthSessionInitialize = _BosPnacAuthSessionInitialize_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 1, 1, 7),
    _BosPnacAuthSessionInitialize_Type()
)
bosPnacAuthSessionInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacAuthSessionInitialize.setStatus("current")
_BosPnacAuthSessionReauthenticate_Type = TruthValue
_BosPnacAuthSessionReauthenticate_Object = MibTableColumn
bosPnacAuthSessionReauthenticate = _BosPnacAuthSessionReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 1, 1, 8),
    _BosPnacAuthSessionReauthenticate_Type()
)
bosPnacAuthSessionReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacAuthSessionReauthenticate.setStatus("current")
_BosPnacAuthSessionStatsTable_Object = MibTable
bosPnacAuthSessionStatsTable = _BosPnacAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2)
)
if mibBuilder.loadTexts:
    bosPnacAuthSessionStatsTable.setStatus("current")
_BosPnacAuthSessionStatsEntry_Object = MibTableRow
bosPnacAuthSessionStatsEntry = _BosPnacAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2, 1)
)
bosPnacAuthSessionStatsEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPnacAuthSessionSuppAddress"),
)
if mibBuilder.loadTexts:
    bosPnacAuthSessionStatsEntry.setStatus("current")
_BosPnacAuthSessionOctetsRx_Type = Counter64
_BosPnacAuthSessionOctetsRx_Object = MibTableColumn
bosPnacAuthSessionOctetsRx = _BosPnacAuthSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2, 1, 1),
    _BosPnacAuthSessionOctetsRx_Type()
)
bosPnacAuthSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionOctetsRx.setStatus("current")
_BosPnacAuthSessionOctetsTx_Type = Counter64
_BosPnacAuthSessionOctetsTx_Object = MibTableColumn
bosPnacAuthSessionOctetsTx = _BosPnacAuthSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2, 1, 2),
    _BosPnacAuthSessionOctetsTx_Type()
)
bosPnacAuthSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionOctetsTx.setStatus("current")
_BosPnacAuthSessionFramesRx_Type = Counter32
_BosPnacAuthSessionFramesRx_Object = MibTableColumn
bosPnacAuthSessionFramesRx = _BosPnacAuthSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2, 1, 3),
    _BosPnacAuthSessionFramesRx_Type()
)
bosPnacAuthSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionFramesRx.setStatus("current")
_BosPnacAuthSessionFramesTx_Type = Counter32
_BosPnacAuthSessionFramesTx_Object = MibTableColumn
bosPnacAuthSessionFramesTx = _BosPnacAuthSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2, 1, 4),
    _BosPnacAuthSessionFramesTx_Type()
)
bosPnacAuthSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionFramesTx.setStatus("current")
_BosPnacAuthSessionId_Type = SnmpAdminString
_BosPnacAuthSessionId_Object = MibTableColumn
bosPnacAuthSessionId = _BosPnacAuthSessionId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2, 1, 5),
    _BosPnacAuthSessionId_Type()
)
bosPnacAuthSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionId.setStatus("current")


class _BosPnacAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type bosPnacAuthSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteAuthServer", 1),
          ("localAuthServer", 2))
    )


_BosPnacAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_BosPnacAuthSessionAuthenticMethod_Object = MibTableColumn
bosPnacAuthSessionAuthenticMethod = _BosPnacAuthSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2, 1, 6),
    _BosPnacAuthSessionAuthenticMethod_Type()
)
bosPnacAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionAuthenticMethod.setStatus("current")
_BosPnacAuthSessionTime_Type = TimeTicks
_BosPnacAuthSessionTime_Object = MibTableColumn
bosPnacAuthSessionTime = _BosPnacAuthSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2, 1, 7),
    _BosPnacAuthSessionTime_Type()
)
bosPnacAuthSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionTime.setStatus("current")


class _BosPnacAuthSessionTerminateCause_Type(Integer32):
    """Custom type bosPnacAuthSessionTerminateCause based on Integer32"""
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
              999)
        )
    )
    namedValues = NamedValues(
        *(("supplicantLogoff", 1),
          ("portFailure", 2),
          ("supplicantRestart", 3),
          ("reauthFailed", 4),
          ("authControlForceUnauth", 5),
          ("portReInit", 6),
          ("portAdminDisabled", 7),
          ("notTerminatedYet", 999))
    )


_BosPnacAuthSessionTerminateCause_Type.__name__ = "Integer32"
_BosPnacAuthSessionTerminateCause_Object = MibTableColumn
bosPnacAuthSessionTerminateCause = _BosPnacAuthSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2, 1, 8),
    _BosPnacAuthSessionTerminateCause_Type()
)
bosPnacAuthSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionTerminateCause.setStatus("current")
_BosPnacAuthSessionUserName_Type = SnmpAdminString
_BosPnacAuthSessionUserName_Object = MibTableColumn
bosPnacAuthSessionUserName = _BosPnacAuthSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 2, 2, 1, 9),
    _BosPnacAuthSessionUserName_Type()
)
bosPnacAuthSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacAuthSessionUserName.setStatus("current")
_BosPnacAuthServer_ObjectIdentity = ObjectIdentity
bosPnacAuthServer = _BosPnacAuthServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 3)
)
_BosPnacASUserConfigTable_Object = MibTable
bosPnacASUserConfigTable = _BosPnacASUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 3, 1)
)
if mibBuilder.loadTexts:
    bosPnacASUserConfigTable.setStatus("current")
_BosPnacASUserConfigEntry_Object = MibTableRow
bosPnacASUserConfigEntry = _BosPnacASUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 3, 1, 1)
)
bosPnacASUserConfigEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPnacASUserConfigUserName"),
)
if mibBuilder.loadTexts:
    bosPnacASUserConfigEntry.setStatus("current")


class _BosPnacASUserConfigUserName_Type(OctetString):
    """Custom type bosPnacASUserConfigUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 115),
    )


_BosPnacASUserConfigUserName_Type.__name__ = "OctetString"
_BosPnacASUserConfigUserName_Object = MibTableColumn
bosPnacASUserConfigUserName = _BosPnacASUserConfigUserName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 3, 1, 1, 1),
    _BosPnacASUserConfigUserName_Type()
)
bosPnacASUserConfigUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosPnacASUserConfigUserName.setStatus("current")
_BosPnacASUserConfigPassword_Type = DisplayString
_BosPnacASUserConfigPassword_Object = MibTableColumn
bosPnacASUserConfigPassword = _BosPnacASUserConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 3, 1, 1, 2),
    _BosPnacASUserConfigPassword_Type()
)
bosPnacASUserConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacASUserConfigPassword.setStatus("current")
_BosPnacASUserConfigAuthProtocol_Type = Unsigned32
_BosPnacASUserConfigAuthProtocol_Object = MibTableColumn
bosPnacASUserConfigAuthProtocol = _BosPnacASUserConfigAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 3, 1, 1, 3),
    _BosPnacASUserConfigAuthProtocol_Type()
)
bosPnacASUserConfigAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPnacASUserConfigAuthProtocol.setStatus("current")
_BosPnacASUserConfigAuthTimeout_Type = Unsigned32
_BosPnacASUserConfigAuthTimeout_Object = MibTableColumn
bosPnacASUserConfigAuthTimeout = _BosPnacASUserConfigAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 3, 1, 1, 4),
    _BosPnacASUserConfigAuthTimeout_Type()
)
bosPnacASUserConfigAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacASUserConfigAuthTimeout.setStatus("current")
_BosPnacASUserConfigPortList_Type = PortList
_BosPnacASUserConfigPortList_Object = MibTableColumn
bosPnacASUserConfigPortList = _BosPnacASUserConfigPortList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 3, 1, 1, 5),
    _BosPnacASUserConfigPortList_Type()
)
bosPnacASUserConfigPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacASUserConfigPortList.setStatus("current")
_BosPnacASUserConfigPermission_Type = PermissionType
_BosPnacASUserConfigPermission_Object = MibTableColumn
bosPnacASUserConfigPermission = _BosPnacASUserConfigPermission_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 3, 1, 1, 6),
    _BosPnacASUserConfigPermission_Type()
)
bosPnacASUserConfigPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPnacASUserConfigPermission.setStatus("current")
_BosPnacASUserConfigRowStatus_Type = RowStatus
_BosPnacASUserConfigRowStatus_Object = MibTableColumn
bosPnacASUserConfigRowStatus = _BosPnacASUserConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 64, 3, 1, 1, 7),
    _BosPnacASUserConfigRowStatus_Type()
)
bosPnacASUserConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosPnacASUserConfigRowStatus.setStatus("current")
_Bntufd_ObjectIdentity = ObjectIdentity
bntufd = _Bntufd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68)
)
_UfdGeneralCfg_ObjectIdentity = ObjectIdentity
ufdGeneralCfg = _UfdGeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1)
)


class _UfdFdpCfgState_Type(Integer32):
    """Custom type ufdFdpCfgState based on Integer32"""
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


_UfdFdpCfgState_Type.__name__ = "Integer32"
_UfdFdpCfgState_Object = MibScalar
ufdFdpCfgState = _UfdFdpCfgState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 1),
    _UfdFdpCfgState_Type()
)
ufdFdpCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdFdpCfgState.setStatus("current")
_UfdCfgLtMPorts_Type = OctetString
_UfdCfgLtMPorts_Object = MibScalar
ufdCfgLtMPorts = _UfdCfgLtMPorts_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 2),
    _UfdCfgLtMPorts_Type()
)
ufdCfgLtMPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCfgLtMPorts.setStatus("current")
_UfdCfgLtMTrunks_Type = OctetString
_UfdCfgLtMTrunks_Object = MibScalar
ufdCfgLtMTrunks = _UfdCfgLtMTrunks_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 3),
    _UfdCfgLtMTrunks_Type()
)
ufdCfgLtMTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCfgLtMTrunks.setStatus("current")
_UfdCfgLtMAdminkey_Type = Integer32
_UfdCfgLtMAdminkey_Object = MibScalar
ufdCfgLtMAdminkey = _UfdCfgLtMAdminkey_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 4),
    _UfdCfgLtMAdminkey_Type()
)
ufdCfgLtMAdminkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCfgLtMAdminkey.setStatus("current")
_UfdCfgLtDPorts_Type = OctetString
_UfdCfgLtDPorts_Object = MibScalar
ufdCfgLtDPorts = _UfdCfgLtDPorts_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 5),
    _UfdCfgLtDPorts_Type()
)
ufdCfgLtDPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCfgLtDPorts.setStatus("current")
_UfdCfgLtDTrunks_Type = OctetString
_UfdCfgLtDTrunks_Object = MibScalar
ufdCfgLtDTrunks = _UfdCfgLtDTrunks_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 6),
    _UfdCfgLtDTrunks_Type()
)
ufdCfgLtDTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdCfgLtDTrunks.setStatus("current")
_UfdLtDAdminkeyMaxEnt_Type = Integer32
_UfdLtDAdminkeyMaxEnt_Object = MibScalar
ufdLtDAdminkeyMaxEnt = _UfdLtDAdminkeyMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 7),
    _UfdLtDAdminkeyMaxEnt_Type()
)
ufdLtDAdminkeyMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdLtDAdminkeyMaxEnt.setStatus("current")
_UfdLtDAdminkeyCfgTable_Object = MibTable
ufdLtDAdminkeyCfgTable = _UfdLtDAdminkeyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 8)
)
if mibBuilder.loadTexts:
    ufdLtDAdminkeyCfgTable.setStatus("current")
_UfdLtDAdminkeyCfgTableEntry_Object = MibTableRow
ufdLtDAdminkeyCfgTableEntry = _UfdLtDAdminkeyCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 8, 1)
)
ufdLtDAdminkeyCfgTableEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "ufdLtDAdminkeyCfg"),
)
if mibBuilder.loadTexts:
    ufdLtDAdminkeyCfgTableEntry.setStatus("current")
_UfdLtDAdminkeyCfg_Type = Integer32
_UfdLtDAdminkeyCfg_Object = MibTableColumn
ufdLtDAdminkeyCfg = _UfdLtDAdminkeyCfg_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 8, 1, 1),
    _UfdLtDAdminkeyCfg_Type()
)
ufdLtDAdminkeyCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdLtDAdminkeyCfg.setStatus("current")
_UfdCfgAddLtMPort_Type = Integer32
_UfdCfgAddLtMPort_Object = MibScalar
ufdCfgAddLtMPort = _UfdCfgAddLtMPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 9),
    _UfdCfgAddLtMPort_Type()
)
ufdCfgAddLtMPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgAddLtMPort.setStatus("current")
_UfdCfgRemoveLtMPort_Type = Integer32
_UfdCfgRemoveLtMPort_Object = MibScalar
ufdCfgRemoveLtMPort = _UfdCfgRemoveLtMPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 10),
    _UfdCfgRemoveLtMPort_Type()
)
ufdCfgRemoveLtMPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgRemoveLtMPort.setStatus("current")
_UfdCfgAddLtMTrunk_Type = Integer32
_UfdCfgAddLtMTrunk_Object = MibScalar
ufdCfgAddLtMTrunk = _UfdCfgAddLtMTrunk_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 11),
    _UfdCfgAddLtMTrunk_Type()
)
ufdCfgAddLtMTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgAddLtMTrunk.setStatus("current")
_UfdCfgRemoveLtMTrunk_Type = Integer32
_UfdCfgRemoveLtMTrunk_Object = MibScalar
ufdCfgRemoveLtMTrunk = _UfdCfgRemoveLtMTrunk_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 12),
    _UfdCfgRemoveLtMTrunk_Type()
)
ufdCfgRemoveLtMTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgRemoveLtMTrunk.setStatus("current")
_UfdCfgAddLtMAdminkey_Type = Integer32
_UfdCfgAddLtMAdminkey_Object = MibScalar
ufdCfgAddLtMAdminkey = _UfdCfgAddLtMAdminkey_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 13),
    _UfdCfgAddLtMAdminkey_Type()
)
ufdCfgAddLtMAdminkey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgAddLtMAdminkey.setStatus("current")
_UfdCfgRemoveLtMAdminkey_Type = Integer32
_UfdCfgRemoveLtMAdminkey_Object = MibScalar
ufdCfgRemoveLtMAdminkey = _UfdCfgRemoveLtMAdminkey_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 14),
    _UfdCfgRemoveLtMAdminkey_Type()
)
ufdCfgRemoveLtMAdminkey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgRemoveLtMAdminkey.setStatus("current")
_UfdCfgAddLtDPort_Type = Integer32
_UfdCfgAddLtDPort_Object = MibScalar
ufdCfgAddLtDPort = _UfdCfgAddLtDPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 15),
    _UfdCfgAddLtDPort_Type()
)
ufdCfgAddLtDPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgAddLtDPort.setStatus("current")
_UfdCfgRemoveLtDPort_Type = Integer32
_UfdCfgRemoveLtDPort_Object = MibScalar
ufdCfgRemoveLtDPort = _UfdCfgRemoveLtDPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 16),
    _UfdCfgRemoveLtDPort_Type()
)
ufdCfgRemoveLtDPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgRemoveLtDPort.setStatus("current")
_UfdCfgAddLtDTrunk_Type = Integer32
_UfdCfgAddLtDTrunk_Object = MibScalar
ufdCfgAddLtDTrunk = _UfdCfgAddLtDTrunk_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 17),
    _UfdCfgAddLtDTrunk_Type()
)
ufdCfgAddLtDTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgAddLtDTrunk.setStatus("current")
_UfdCfgRemoveLtDTrunk_Type = Integer32
_UfdCfgRemoveLtDTrunk_Object = MibScalar
ufdCfgRemoveLtDTrunk = _UfdCfgRemoveLtDTrunk_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 18),
    _UfdCfgRemoveLtDTrunk_Type()
)
ufdCfgRemoveLtDTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgRemoveLtDTrunk.setStatus("current")
_UfdCfgAddLtDAdminkey_Type = Integer32
_UfdCfgAddLtDAdminkey_Object = MibScalar
ufdCfgAddLtDAdminkey = _UfdCfgAddLtDAdminkey_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 19),
    _UfdCfgAddLtDAdminkey_Type()
)
ufdCfgAddLtDAdminkey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgAddLtDAdminkey.setStatus("current")
_UfdCfgRemoveLtDAdminkey_Type = Integer32
_UfdCfgRemoveLtDAdminkey_Object = MibScalar
ufdCfgRemoveLtDAdminkey = _UfdCfgRemoveLtDAdminkey_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 20),
    _UfdCfgRemoveLtDAdminkey_Type()
)
ufdCfgRemoveLtDAdminkey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgRemoveLtDAdminkey.setStatus("current")


class _UfdCfgGlobalState_Type(Integer32):
    """Custom type ufdCfgGlobalState based on Integer32"""
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


_UfdCfgGlobalState_Type.__name__ = "Integer32"
_UfdCfgGlobalState_Object = MibScalar
ufdCfgGlobalState = _UfdCfgGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 1, 21),
    _UfdCfgGlobalState_Type()
)
ufdCfgGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdCfgGlobalState.setStatus("current")
_UfdStats_ObjectIdentity = ObjectIdentity
ufdStats = _UfdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 2)
)
_UfdNoLtMLinkFailure_Type = Integer32
_UfdNoLtMLinkFailure_Object = MibScalar
ufdNoLtMLinkFailure = _UfdNoLtMLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 2, 1),
    _UfdNoLtMLinkFailure_Type()
)
ufdNoLtMLinkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdNoLtMLinkFailure.setStatus("current")
_UfdNoLtMLinkBlockingState_Type = Integer32
_UfdNoLtMLinkBlockingState_Object = MibScalar
ufdNoLtMLinkBlockingState = _UfdNoLtMLinkBlockingState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 2, 2),
    _UfdNoLtMLinkBlockingState_Type()
)
ufdNoLtMLinkBlockingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdNoLtMLinkBlockingState.setStatus("current")
_UfdNoLtDAutoDisabled_Type = Integer32
_UfdNoLtDAutoDisabled_Object = MibScalar
ufdNoLtDAutoDisabled = _UfdNoLtDAutoDisabled_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 2, 3),
    _UfdNoLtDAutoDisabled_Type()
)
ufdNoLtDAutoDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ufdNoLtDAutoDisabled.setStatus("current")


class _UfdClearStats_Type(Integer32):
    """Custom type ufdClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_UfdClearStats_Type.__name__ = "Integer32"
_UfdClearStats_Object = MibScalar
ufdClearStats = _UfdClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 68, 2, 4),
    _UfdClearStats_Type()
)
ufdClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufdClearStats.setStatus("current")
_Bostacacs_ObjectIdentity = ObjectIdentity
bostacacs = _Bostacacs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77)
)
_BosTacacsClientScalarGroup_ObjectIdentity = ObjectIdentity
bosTacacsClientScalarGroup = _BosTacacsClientScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1)
)
_BosTacClntActiveServer_Type = IpAddress
_BosTacClntActiveServer_Object = MibScalar
bosTacClntActiveServer = _BosTacClntActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 1),
    _BosTacClntActiveServer_Type()
)
bosTacClntActiveServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosTacClntActiveServer.setStatus("current")
_BosTacClntTraceLevel_Type = Unsigned32
_BosTacClntTraceLevel_Object = MibScalar
bosTacClntTraceLevel = _BosTacClntTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 2),
    _BosTacClntTraceLevel_Type()
)
bosTacClntTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosTacClntTraceLevel.setStatus("current")


class _BosTacClntRetransmit_Type(Integer32):
    """Custom type bosTacClntRetransmit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BosTacClntRetransmit_Type.__name__ = "Integer32"
_BosTacClntRetransmit_Object = MibScalar
bosTacClntRetransmit = _BosTacClntRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 3),
    _BosTacClntRetransmit_Type()
)
bosTacClntRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosTacClntRetransmit.setStatus("current")
_BosTacClntStatisticsGroup_ObjectIdentity = ObjectIdentity
bosTacClntStatisticsGroup = _BosTacClntStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4)
)
_BosTacClntAuthenStartRequests_Type = Counter32
_BosTacClntAuthenStartRequests_Object = MibScalar
bosTacClntAuthenStartRequests = _BosTacClntAuthenStartRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 1),
    _BosTacClntAuthenStartRequests_Type()
)
bosTacClntAuthenStartRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenStartRequests.setStatus("current")
_BosTacClntAuthenContinueRequests_Type = Counter32
_BosTacClntAuthenContinueRequests_Object = MibScalar
bosTacClntAuthenContinueRequests = _BosTacClntAuthenContinueRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 2),
    _BosTacClntAuthenContinueRequests_Type()
)
bosTacClntAuthenContinueRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenContinueRequests.setStatus("current")
_BosTacClntAuthenEnableRequests_Type = Counter32
_BosTacClntAuthenEnableRequests_Object = MibScalar
bosTacClntAuthenEnableRequests = _BosTacClntAuthenEnableRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 3),
    _BosTacClntAuthenEnableRequests_Type()
)
bosTacClntAuthenEnableRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenEnableRequests.setStatus("current")
_BosTacClntAuthenAbortRequests_Type = Counter32
_BosTacClntAuthenAbortRequests_Object = MibScalar
bosTacClntAuthenAbortRequests = _BosTacClntAuthenAbortRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 4),
    _BosTacClntAuthenAbortRequests_Type()
)
bosTacClntAuthenAbortRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenAbortRequests.setStatus("current")
_BosTacClntAuthenPassReceived_Type = Counter32
_BosTacClntAuthenPassReceived_Object = MibScalar
bosTacClntAuthenPassReceived = _BosTacClntAuthenPassReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 5),
    _BosTacClntAuthenPassReceived_Type()
)
bosTacClntAuthenPassReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenPassReceived.setStatus("current")
_BosTacClntAuthenFailReceived_Type = Counter32
_BosTacClntAuthenFailReceived_Object = MibScalar
bosTacClntAuthenFailReceived = _BosTacClntAuthenFailReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 6),
    _BosTacClntAuthenFailReceived_Type()
)
bosTacClntAuthenFailReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenFailReceived.setStatus("current")
_BosTacClntAuthenGetUserReceived_Type = Counter32
_BosTacClntAuthenGetUserReceived_Object = MibScalar
bosTacClntAuthenGetUserReceived = _BosTacClntAuthenGetUserReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 7),
    _BosTacClntAuthenGetUserReceived_Type()
)
bosTacClntAuthenGetUserReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenGetUserReceived.setStatus("current")
_BosTacClntAuthenGetPassReceived_Type = Counter32
_BosTacClntAuthenGetPassReceived_Object = MibScalar
bosTacClntAuthenGetPassReceived = _BosTacClntAuthenGetPassReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 8),
    _BosTacClntAuthenGetPassReceived_Type()
)
bosTacClntAuthenGetPassReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenGetPassReceived.setStatus("current")
_BosTacClntAuthenGetDataReceived_Type = Counter32
_BosTacClntAuthenGetDataReceived_Object = MibScalar
bosTacClntAuthenGetDataReceived = _BosTacClntAuthenGetDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 9),
    _BosTacClntAuthenGetDataReceived_Type()
)
bosTacClntAuthenGetDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenGetDataReceived.setStatus("current")
_BosTacClntAuthenErrorReceived_Type = Counter32
_BosTacClntAuthenErrorReceived_Object = MibScalar
bosTacClntAuthenErrorReceived = _BosTacClntAuthenErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 10),
    _BosTacClntAuthenErrorReceived_Type()
)
bosTacClntAuthenErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenErrorReceived.setStatus("current")
_BosTacClntAuthenFollowReceived_Type = Counter32
_BosTacClntAuthenFollowReceived_Object = MibScalar
bosTacClntAuthenFollowReceived = _BosTacClntAuthenFollowReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 11),
    _BosTacClntAuthenFollowReceived_Type()
)
bosTacClntAuthenFollowReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenFollowReceived.setStatus("current")
_BosTacClntAuthenRestartReceived_Type = Counter32
_BosTacClntAuthenRestartReceived_Object = MibScalar
bosTacClntAuthenRestartReceived = _BosTacClntAuthenRestartReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 12),
    _BosTacClntAuthenRestartReceived_Type()
)
bosTacClntAuthenRestartReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenRestartReceived.setStatus("current")
_BosTacClntAuthenSessionTimouts_Type = Counter32
_BosTacClntAuthenSessionTimouts_Object = MibScalar
bosTacClntAuthenSessionTimouts = _BosTacClntAuthenSessionTimouts_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 13),
    _BosTacClntAuthenSessionTimouts_Type()
)
bosTacClntAuthenSessionTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthenSessionTimouts.setStatus("current")
_BosTacClntAuthorRequests_Type = Counter32
_BosTacClntAuthorRequests_Object = MibScalar
bosTacClntAuthorRequests = _BosTacClntAuthorRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 14),
    _BosTacClntAuthorRequests_Type()
)
bosTacClntAuthorRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthorRequests.setStatus("current")
_BosTacClntAuthorPassAddReceived_Type = Counter32
_BosTacClntAuthorPassAddReceived_Object = MibScalar
bosTacClntAuthorPassAddReceived = _BosTacClntAuthorPassAddReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 15),
    _BosTacClntAuthorPassAddReceived_Type()
)
bosTacClntAuthorPassAddReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthorPassAddReceived.setStatus("current")
_BosTacClntAuthorPassReplReceived_Type = Counter32
_BosTacClntAuthorPassReplReceived_Object = MibScalar
bosTacClntAuthorPassReplReceived = _BosTacClntAuthorPassReplReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 16),
    _BosTacClntAuthorPassReplReceived_Type()
)
bosTacClntAuthorPassReplReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthorPassReplReceived.setStatus("current")
_BosTacClntAuthorFailReceived_Type = Counter32
_BosTacClntAuthorFailReceived_Object = MibScalar
bosTacClntAuthorFailReceived = _BosTacClntAuthorFailReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 17),
    _BosTacClntAuthorFailReceived_Type()
)
bosTacClntAuthorFailReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthorFailReceived.setStatus("current")
_BosTacClntAuthorErrorReceived_Type = Counter32
_BosTacClntAuthorErrorReceived_Object = MibScalar
bosTacClntAuthorErrorReceived = _BosTacClntAuthorErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 18),
    _BosTacClntAuthorErrorReceived_Type()
)
bosTacClntAuthorErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthorErrorReceived.setStatus("current")
_BosTacClntAuthorFollowReceived_Type = Counter32
_BosTacClntAuthorFollowReceived_Object = MibScalar
bosTacClntAuthorFollowReceived = _BosTacClntAuthorFollowReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 19),
    _BosTacClntAuthorFollowReceived_Type()
)
bosTacClntAuthorFollowReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthorFollowReceived.setStatus("current")
_BosTacClntAuthorSessionTimeouts_Type = Counter32
_BosTacClntAuthorSessionTimeouts_Object = MibScalar
bosTacClntAuthorSessionTimeouts = _BosTacClntAuthorSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 20),
    _BosTacClntAuthorSessionTimeouts_Type()
)
bosTacClntAuthorSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAuthorSessionTimeouts.setStatus("current")
_BosTacClntAcctStartRequests_Type = Counter32
_BosTacClntAcctStartRequests_Object = MibScalar
bosTacClntAcctStartRequests = _BosTacClntAcctStartRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 21),
    _BosTacClntAcctStartRequests_Type()
)
bosTacClntAcctStartRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAcctStartRequests.setStatus("current")
_BosTacClntAcctWdRequests_Type = Counter32
_BosTacClntAcctWdRequests_Object = MibScalar
bosTacClntAcctWdRequests = _BosTacClntAcctWdRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 22),
    _BosTacClntAcctWdRequests_Type()
)
bosTacClntAcctWdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAcctWdRequests.setStatus("current")
_BosTacClntAcctStopRequests_Type = Counter32
_BosTacClntAcctStopRequests_Object = MibScalar
bosTacClntAcctStopRequests = _BosTacClntAcctStopRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 23),
    _BosTacClntAcctStopRequests_Type()
)
bosTacClntAcctStopRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAcctStopRequests.setStatus("current")
_BosTacClntAcctSuccessReceived_Type = Counter32
_BosTacClntAcctSuccessReceived_Object = MibScalar
bosTacClntAcctSuccessReceived = _BosTacClntAcctSuccessReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 24),
    _BosTacClntAcctSuccessReceived_Type()
)
bosTacClntAcctSuccessReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAcctSuccessReceived.setStatus("current")
_BosTacClntAcctErrorReceived_Type = Counter32
_BosTacClntAcctErrorReceived_Object = MibScalar
bosTacClntAcctErrorReceived = _BosTacClntAcctErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 25),
    _BosTacClntAcctErrorReceived_Type()
)
bosTacClntAcctErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAcctErrorReceived.setStatus("current")
_BosTacClntAcctFollowReceived_Type = Counter32
_BosTacClntAcctFollowReceived_Object = MibScalar
bosTacClntAcctFollowReceived = _BosTacClntAcctFollowReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 26),
    _BosTacClntAcctFollowReceived_Type()
)
bosTacClntAcctFollowReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAcctFollowReceived.setStatus("current")
_BosTacClntAcctSessionTimeouts_Type = Counter32
_BosTacClntAcctSessionTimeouts_Object = MibScalar
bosTacClntAcctSessionTimeouts = _BosTacClntAcctSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 27),
    _BosTacClntAcctSessionTimeouts_Type()
)
bosTacClntAcctSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntAcctSessionTimeouts.setStatus("current")
_BosTacClntMalformedPktsReceived_Type = Counter32
_BosTacClntMalformedPktsReceived_Object = MibScalar
bosTacClntMalformedPktsReceived = _BosTacClntMalformedPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 28),
    _BosTacClntMalformedPktsReceived_Type()
)
bosTacClntMalformedPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntMalformedPktsReceived.setStatus("current")
_BosTacClntSocketFailures_Type = Counter32
_BosTacClntSocketFailures_Object = MibScalar
bosTacClntSocketFailures = _BosTacClntSocketFailures_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 29),
    _BosTacClntSocketFailures_Type()
)
bosTacClntSocketFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntSocketFailures.setStatus("current")
_BosTacClntConnectionFailures_Type = Counter32
_BosTacClntConnectionFailures_Object = MibScalar
bosTacClntConnectionFailures = _BosTacClntConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 4, 30),
    _BosTacClntConnectionFailures_Type()
)
bosTacClntConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosTacClntConnectionFailures.setStatus("current")


class _BosTacClntPrivLevelMap_Type(Integer32):
    """Custom type bosTacClntPrivLevelMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BosTacClntPrivLevelMap_Type.__name__ = "Integer32"
_BosTacClntPrivLevelMap_Object = MibScalar
bosTacClntPrivLevelMap = _BosTacClntPrivLevelMap_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 5),
    _BosTacClntPrivLevelMap_Type()
)
bosTacClntPrivLevelMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosTacClntPrivLevelMap.setStatus("current")


class _BosTacClntSecureBackdoorStatus_Type(Integer32):
    """Custom type bosTacClntSecureBackdoorStatus based on Integer32"""
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


_BosTacClntSecureBackdoorStatus_Type.__name__ = "Integer32"
_BosTacClntSecureBackdoorStatus_Object = MibScalar
bosTacClntSecureBackdoorStatus = _BosTacClntSecureBackdoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 1, 6),
    _BosTacClntSecureBackdoorStatus_Type()
)
bosTacClntSecureBackdoorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosTacClntSecureBackdoorStatus.setStatus("current")
_BosTacacsClientTableGroup_ObjectIdentity = ObjectIdentity
bosTacacsClientTableGroup = _BosTacacsClientTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 2)
)
_BosTacClntServerTable_Object = MibTable
bosTacClntServerTable = _BosTacClntServerTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 2, 1)
)
if mibBuilder.loadTexts:
    bosTacClntServerTable.setStatus("current")
_BosTacClntServerEntry_Object = MibTableRow
bosTacClntServerEntry = _BosTacClntServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 2, 1, 1)
)
bosTacClntServerEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosTacClntServerAddress"),
)
if mibBuilder.loadTexts:
    bosTacClntServerEntry.setStatus("current")
_BosTacClntServerAddress_Type = IpAddress
_BosTacClntServerAddress_Object = MibTableColumn
bosTacClntServerAddress = _BosTacClntServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 2, 1, 1, 1),
    _BosTacClntServerAddress_Type()
)
bosTacClntServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosTacClntServerAddress.setStatus("current")
_BosTacClntServerStatus_Type = RowStatus
_BosTacClntServerStatus_Object = MibTableColumn
bosTacClntServerStatus = _BosTacClntServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 2, 1, 1, 2),
    _BosTacClntServerStatus_Type()
)
bosTacClntServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosTacClntServerStatus.setStatus("current")


class _BosTacClntServerSingleConnect_Type(Integer32):
    """Custom type bosTacClntServerSingleConnect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_BosTacClntServerSingleConnect_Type.__name__ = "Integer32"
_BosTacClntServerSingleConnect_Object = MibTableColumn
bosTacClntServerSingleConnect = _BosTacClntServerSingleConnect_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 2, 1, 1, 3),
    _BosTacClntServerSingleConnect_Type()
)
bosTacClntServerSingleConnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosTacClntServerSingleConnect.setStatus("current")


class _BosTacClntServerPort_Type(Integer32):
    """Custom type bosTacClntServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BosTacClntServerPort_Type.__name__ = "Integer32"
_BosTacClntServerPort_Object = MibTableColumn
bosTacClntServerPort = _BosTacClntServerPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 2, 1, 1, 4),
    _BosTacClntServerPort_Type()
)
bosTacClntServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosTacClntServerPort.setStatus("current")


class _BosTacClntServerTimeout_Type(Integer32):
    """Custom type bosTacClntServerTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BosTacClntServerTimeout_Type.__name__ = "Integer32"
_BosTacClntServerTimeout_Object = MibTableColumn
bosTacClntServerTimeout = _BosTacClntServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 2, 1, 1, 5),
    _BosTacClntServerTimeout_Type()
)
bosTacClntServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosTacClntServerTimeout.setStatus("current")
_BosTacClntServerKey_Type = DisplayString
_BosTacClntServerKey_Object = MibTableColumn
bosTacClntServerKey = _BosTacClntServerKey_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 77, 2, 1, 1, 6),
    _BosTacClntServerKey_Type()
)
bosTacClntServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosTacClntServerKey.setStatus("current")
_BosPvrstMIB_ObjectIdentity = ObjectIdentity
bosPvrstMIB = _BosPvrstMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78)
)
_BosPvrst_ObjectIdentity = ObjectIdentity
bosPvrst = _BosPvrst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1)
)


class _BosPvrstSystemControl_Type(Integer32):
    """Custom type bosPvrstSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_BosPvrstSystemControl_Type.__name__ = "Integer32"
_BosPvrstSystemControl_Object = MibScalar
bosPvrstSystemControl = _BosPvrstSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 1),
    _BosPvrstSystemControl_Type()
)
bosPvrstSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstSystemControl.setStatus("current")
_BosPvrstModuleStatus_Type = EnabledStatus
_BosPvrstModuleStatus_Object = MibScalar
bosPvrstModuleStatus = _BosPvrstModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 2),
    _BosPvrstModuleStatus_Type()
)
bosPvrstModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstModuleStatus.setStatus("current")
_BosPvrstNoOfActiveInstances_Type = Integer32
_BosPvrstNoOfActiveInstances_Object = MibScalar
bosPvrstNoOfActiveInstances = _BosPvrstNoOfActiveInstances_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 3),
    _BosPvrstNoOfActiveInstances_Type()
)
bosPvrstNoOfActiveInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstNoOfActiveInstances.setStatus("current")
_BosPvrstBrgAddress_Type = MacAddress
_BosPvrstBrgAddress_Object = MibScalar
bosPvrstBrgAddress = _BosPvrstBrgAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 4),
    _BosPvrstBrgAddress_Type()
)
bosPvrstBrgAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstBrgAddress.setStatus("current")
_BosPvrstUpCount_Type = Counter32
_BosPvrstUpCount_Object = MibScalar
bosPvrstUpCount = _BosPvrstUpCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 5),
    _BosPvrstUpCount_Type()
)
bosPvrstUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstUpCount.setStatus("current")
_BosPvrstDownCount_Type = Counter32
_BosPvrstDownCount_Object = MibScalar
bosPvrstDownCount = _BosPvrstDownCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 6),
    _BosPvrstDownCount_Type()
)
bosPvrstDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstDownCount.setStatus("current")


class _BosPvrstTrace_Type(Integer32):
    """Custom type bosPvrstTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosPvrstTrace_Type.__name__ = "Integer32"
_BosPvrstTrace_Object = MibScalar
bosPvrstTrace = _BosPvrstTrace_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 7),
    _BosPvrstTrace_Type()
)
bosPvrstTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstTrace.setStatus("current")


class _BosPvrstDebug_Type(Integer32):
    """Custom type bosPvrstDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )


_BosPvrstDebug_Type.__name__ = "Integer32"
_BosPvrstDebug_Object = MibScalar
bosPvrstDebug = _BosPvrstDebug_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 8),
    _BosPvrstDebug_Type()
)
bosPvrstDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstDebug.setStatus("current")
_BosPvrstBufferOverFlowCount_Type = Counter32
_BosPvrstBufferOverFlowCount_Object = MibScalar
bosPvrstBufferOverFlowCount = _BosPvrstBufferOverFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 9),
    _BosPvrstBufferOverFlowCount_Type()
)
bosPvrstBufferOverFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstBufferOverFlowCount.setStatus("current")
_BosPvrstMemAllocFailureCount_Type = Counter32
_BosPvrstMemAllocFailureCount_Object = MibScalar
bosPvrstMemAllocFailureCount = _BosPvrstMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 10),
    _BosPvrstMemAllocFailureCount_Type()
)
bosPvrstMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstMemAllocFailureCount.setStatus("current")
_BosPvrstUplinkFastStatus_Type = EnabledStatus
_BosPvrstUplinkFastStatus_Object = MibScalar
bosPvrstUplinkFastStatus = _BosPvrstUplinkFastStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 12),
    _BosPvrstUplinkFastStatus_Type()
)
bosPvrstUplinkFastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstUplinkFastStatus.setStatus("current")


class _BosPvrstUplinkFastMaxRate_Type(Integer32):
    """Custom type bosPvrstUplinkFastMaxRate based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_BosPvrstUplinkFastMaxRate_Type.__name__ = "Integer32"
_BosPvrstUplinkFastMaxRate_Object = MibScalar
bosPvrstUplinkFastMaxRate = _BosPvrstUplinkFastMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 13),
    _BosPvrstUplinkFastMaxRate_Type()
)
bosPvrstUplinkFastMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstUplinkFastMaxRate.setStatus("current")
_BosPvrstPortTable_Object = MibTable
bosPvrstPortTable = _BosPvrstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 14)
)
if mibBuilder.loadTexts:
    bosPvrstPortTable.setStatus("current")
_BosPvrstPortEntry_Object = MibTableRow
bosPvrstPortEntry = _BosPvrstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 14, 1)
)
bosPvrstPortEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPvrstPort"),
)
if mibBuilder.loadTexts:
    bosPvrstPortEntry.setStatus("current")
_BosPvrstPort_Type = Integer32
_BosPvrstPort_Object = MibTableColumn
bosPvrstPort = _BosPvrstPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 14, 1, 1),
    _BosPvrstPort_Type()
)
bosPvrstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstPort.setStatus("current")
_BosPvrstPortAdminEdgeStatus_Type = TruthValue
_BosPvrstPortAdminEdgeStatus_Object = MibTableColumn
bosPvrstPortAdminEdgeStatus = _BosPvrstPortAdminEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 14, 1, 2),
    _BosPvrstPortAdminEdgeStatus_Type()
)
bosPvrstPortAdminEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstPortAdminEdgeStatus.setStatus("current")
_BosPvrstPortOperEdgePortStatus_Type = TruthValue
_BosPvrstPortOperEdgePortStatus_Object = MibTableColumn
bosPvrstPortOperEdgePortStatus = _BosPvrstPortOperEdgePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 14, 1, 3),
    _BosPvrstPortOperEdgePortStatus_Type()
)
bosPvrstPortOperEdgePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstPortOperEdgePortStatus.setStatus("current")


class _BosPvrstBridgeDetectionSemState_Type(Integer32):
    """Custom type bosPvrstBridgeDetectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("edge", 0),
          ("notedge", 1))
    )


_BosPvrstBridgeDetectionSemState_Type.__name__ = "Integer32"
_BosPvrstBridgeDetectionSemState_Object = MibTableColumn
bosPvrstBridgeDetectionSemState = _BosPvrstBridgeDetectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 14, 1, 4),
    _BosPvrstBridgeDetectionSemState_Type()
)
bosPvrstBridgeDetectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstBridgeDetectionSemState.setStatus("current")


class _BosPvrstPortAdminPointToPoint_Type(Integer32):
    """Custom type bosPvrstPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_BosPvrstPortAdminPointToPoint_Type.__name__ = "Integer32"
_BosPvrstPortAdminPointToPoint_Object = MibTableColumn
bosPvrstPortAdminPointToPoint = _BosPvrstPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 14, 1, 5),
    _BosPvrstPortAdminPointToPoint_Type()
)
bosPvrstPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstPortAdminPointToPoint.setStatus("current")
_BosPvrstPortOperPointToPoint_Type = TruthValue
_BosPvrstPortOperPointToPoint_Object = MibTableColumn
bosPvrstPortOperPointToPoint = _BosPvrstPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 14, 1, 6),
    _BosPvrstPortOperPointToPoint_Type()
)
bosPvrstPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstPortOperPointToPoint.setStatus("current")
_BosPvrstInstBridgeTable_Object = MibTable
bosPvrstInstBridgeTable = _BosPvrstInstBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15)
)
if mibBuilder.loadTexts:
    bosPvrstInstBridgeTable.setStatus("current")
_BosPvrstInstBridgeEntry_Object = MibTableRow
bosPvrstInstBridgeEntry = _BosPvrstInstBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1)
)
bosPvrstInstBridgeEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPvrstInstInstanceIndex"),
)
if mibBuilder.loadTexts:
    bosPvrstInstBridgeEntry.setStatus("current")


class _BosPvrstInstInstanceIndex_Type(Integer32):
    """Custom type bosPvrstInstInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BosPvrstInstInstanceIndex_Type.__name__ = "Integer32"
_BosPvrstInstInstanceIndex_Object = MibTableColumn
bosPvrstInstInstanceIndex = _BosPvrstInstInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 1),
    _BosPvrstInstInstanceIndex_Type()
)
bosPvrstInstInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosPvrstInstInstanceIndex.setStatus("current")


class _BosPvrstInstBridgePriority_Type(Integer32):
    """Custom type bosPvrstInstBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BosPvrstInstBridgePriority_Type.__name__ = "Integer32"
_BosPvrstInstBridgePriority_Object = MibTableColumn
bosPvrstInstBridgePriority = _BosPvrstInstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 2),
    _BosPvrstInstBridgePriority_Type()
)
bosPvrstInstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstInstBridgePriority.setStatus("current")
_BosPvrstInstRootCost_Type = Integer32
_BosPvrstInstRootCost_Object = MibTableColumn
bosPvrstInstRootCost = _BosPvrstInstRootCost_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 3),
    _BosPvrstInstRootCost_Type()
)
bosPvrstInstRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstRootCost.setStatus("current")
_BosPvrstInstRootPort_Type = Integer32
_BosPvrstInstRootPort_Object = MibTableColumn
bosPvrstInstRootPort = _BosPvrstInstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 4),
    _BosPvrstInstRootPort_Type()
)
bosPvrstInstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstRootPort.setStatus("current")
_BosPvrstInstBridgeMaxAge_Type = Timeout
_BosPvrstInstBridgeMaxAge_Object = MibTableColumn
bosPvrstInstBridgeMaxAge = _BosPvrstInstBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 5),
    _BosPvrstInstBridgeMaxAge_Type()
)
bosPvrstInstBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstInstBridgeMaxAge.setStatus("current")
_BosPvrstInstBridgeHelloTime_Type = Timeout
_BosPvrstInstBridgeHelloTime_Object = MibTableColumn
bosPvrstInstBridgeHelloTime = _BosPvrstInstBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 6),
    _BosPvrstInstBridgeHelloTime_Type()
)
bosPvrstInstBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstInstBridgeHelloTime.setStatus("current")
_BosPvrstInstBridgeForwardDelay_Type = Timeout
_BosPvrstInstBridgeForwardDelay_Object = MibTableColumn
bosPvrstInstBridgeForwardDelay = _BosPvrstInstBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 7),
    _BosPvrstInstBridgeForwardDelay_Type()
)
bosPvrstInstBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstInstBridgeForwardDelay.setStatus("current")
_BosPvrstInstHoldTime_Type = Integer32
_BosPvrstInstHoldTime_Object = MibTableColumn
bosPvrstInstHoldTime = _BosPvrstInstHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 8),
    _BosPvrstInstHoldTime_Type()
)
bosPvrstInstHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstHoldTime.setStatus("current")
_BosPvrstInstTimeSinceTopologyChange_Type = TimeTicks
_BosPvrstInstTimeSinceTopologyChange_Object = MibTableColumn
bosPvrstInstTimeSinceTopologyChange = _BosPvrstInstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 9),
    _BosPvrstInstTimeSinceTopologyChange_Type()
)
bosPvrstInstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstTimeSinceTopologyChange.setStatus("current")
_BosPvrstInstTopChanges_Type = Counter32
_BosPvrstInstTopChanges_Object = MibTableColumn
bosPvrstInstTopChanges = _BosPvrstInstTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 10),
    _BosPvrstInstTopChanges_Type()
)
bosPvrstInstTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstTopChanges.setStatus("current")
_BosPvrstInstNewRootCount_Type = Counter32
_BosPvrstInstNewRootCount_Object = MibTableColumn
bosPvrstInstNewRootCount = _BosPvrstInstNewRootCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 11),
    _BosPvrstInstNewRootCount_Type()
)
bosPvrstInstNewRootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstNewRootCount.setStatus("current")
_BosPvrstInstInstanceUpCount_Type = Counter32
_BosPvrstInstInstanceUpCount_Object = MibTableColumn
bosPvrstInstInstanceUpCount = _BosPvrstInstInstanceUpCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 12),
    _BosPvrstInstInstanceUpCount_Type()
)
bosPvrstInstInstanceUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstInstanceUpCount.setStatus("current")
_BosPvrstInstInstanceDownCount_Type = Counter32
_BosPvrstInstInstanceDownCount_Object = MibTableColumn
bosPvrstInstInstanceDownCount = _BosPvrstInstInstanceDownCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 13),
    _BosPvrstInstInstanceDownCount_Type()
)
bosPvrstInstInstanceDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstInstanceDownCount.setStatus("current")


class _BosPvrstInstPortRoleSelSemState_Type(Integer32):
    """Custom type bosPvrstInstPortRoleSelSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_BosPvrstInstPortRoleSelSemState_Type.__name__ = "Integer32"
_BosPvrstInstPortRoleSelSemState_Object = MibTableColumn
bosPvrstInstPortRoleSelSemState = _BosPvrstInstPortRoleSelSemState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 14),
    _BosPvrstInstPortRoleSelSemState_Type()
)
bosPvrstInstPortRoleSelSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortRoleSelSemState.setStatus("current")
_BosPvrstInstDesignatedRoot_Type = BridgeId
_BosPvrstInstDesignatedRoot_Object = MibTableColumn
bosPvrstInstDesignatedRoot = _BosPvrstInstDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 15),
    _BosPvrstInstDesignatedRoot_Type()
)
bosPvrstInstDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstDesignatedRoot.setStatus("current")
_BosPvrstInstRootMaxAge_Type = Timeout
_BosPvrstInstRootMaxAge_Object = MibTableColumn
bosPvrstInstRootMaxAge = _BosPvrstInstRootMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 16),
    _BosPvrstInstRootMaxAge_Type()
)
bosPvrstInstRootMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstRootMaxAge.setStatus("current")
_BosPvrstInstRootHelloTime_Type = Timeout
_BosPvrstInstRootHelloTime_Object = MibTableColumn
bosPvrstInstRootHelloTime = _BosPvrstInstRootHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 17),
    _BosPvrstInstRootHelloTime_Type()
)
bosPvrstInstRootHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstRootHelloTime.setStatus("current")
_BosPvrstInstRootForwardDelay_Type = Timeout
_BosPvrstInstRootForwardDelay_Object = MibTableColumn
bosPvrstInstRootForwardDelay = _BosPvrstInstRootForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 18),
    _BosPvrstInstRootForwardDelay_Type()
)
bosPvrstInstRootForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstRootForwardDelay.setStatus("current")


class _BosPvrstInstSetVlanList_Type(OctetString):
    """Custom type bosPvrstInstSetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_BosPvrstInstSetVlanList_Type.__name__ = "OctetString"
_BosPvrstInstSetVlanList_Object = MibTableColumn
bosPvrstInstSetVlanList = _BosPvrstInstSetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 19),
    _BosPvrstInstSetVlanList_Type()
)
bosPvrstInstSetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstInstSetVlanList.setStatus("current")


class _BosPvrstInstResetVlanList_Type(OctetString):
    """Custom type bosPvrstInstResetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_BosPvrstInstResetVlanList_Type.__name__ = "OctetString"
_BosPvrstInstResetVlanList_Object = MibTableColumn
bosPvrstInstResetVlanList = _BosPvrstInstResetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 20),
    _BosPvrstInstResetVlanList_Type()
)
bosPvrstInstResetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstInstResetVlanList.setStatus("current")


class _BosPvrstInstEnableStatus_Type(Integer32):
    """Custom type bosPvrstInstEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BosPvrstInstEnableStatus_Type.__name__ = "Integer32"
_BosPvrstInstEnableStatus_Object = MibTableColumn
bosPvrstInstEnableStatus = _BosPvrstInstEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 15, 1, 21),
    _BosPvrstInstEnableStatus_Type()
)
bosPvrstInstEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstInstEnableStatus.setStatus("current")
_BosPvrstInstPortTable_Object = MibTable
bosPvrstInstPortTable = _BosPvrstInstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16)
)
if mibBuilder.loadTexts:
    bosPvrstInstPortTable.setStatus("current")
_BosPvrstInstPortEntry_Object = MibTableRow
bosPvrstInstPortEntry = _BosPvrstInstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1)
)
bosPvrstInstPortEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPvrstInstInstanceIndex"),
    (0, "BLADEOS-BASE-MIB", "bosPvrstInstPortIndex"),
)
if mibBuilder.loadTexts:
    bosPvrstInstPortEntry.setStatus("current")


class _BosPvrstInstPortIndex_Type(Integer32):
    """Custom type bosPvrstInstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BosPvrstInstPortIndex_Type.__name__ = "Integer32"
_BosPvrstInstPortIndex_Object = MibTableColumn
bosPvrstInstPortIndex = _BosPvrstInstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 1),
    _BosPvrstInstPortIndex_Type()
)
bosPvrstInstPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosPvrstInstPortIndex.setStatus("current")


class _BosPvrstInstPortStatus_Type(Integer32):
    """Custom type bosPvrstInstPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosPvrstInstPortStatus_Type.__name__ = "Integer32"
_BosPvrstInstPortStatus_Object = MibTableColumn
bosPvrstInstPortStatus = _BosPvrstInstPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 2),
    _BosPvrstInstPortStatus_Type()
)
bosPvrstInstPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstInstPortStatus.setStatus("current")


class _BosPvrstInstPortPathCost_Type(Integer32):
    """Custom type bosPvrstInstPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_BosPvrstInstPortPathCost_Type.__name__ = "Integer32"
_BosPvrstInstPortPathCost_Object = MibTableColumn
bosPvrstInstPortPathCost = _BosPvrstInstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 3),
    _BosPvrstInstPortPathCost_Type()
)
bosPvrstInstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstInstPortPathCost.setStatus("current")


class _BosPvrstInstPortPriority_Type(Integer32):
    """Custom type bosPvrstInstPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_BosPvrstInstPortPriority_Type.__name__ = "Integer32"
_BosPvrstInstPortPriority_Object = MibTableColumn
bosPvrstInstPortPriority = _BosPvrstInstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 4),
    _BosPvrstInstPortPriority_Type()
)
bosPvrstInstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstInstPortPriority.setStatus("current")
_BosPvrstInstPortDesignatedRoot_Type = BridgeId
_BosPvrstInstPortDesignatedRoot_Object = MibTableColumn
bosPvrstInstPortDesignatedRoot = _BosPvrstInstPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 5),
    _BosPvrstInstPortDesignatedRoot_Type()
)
bosPvrstInstPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortDesignatedRoot.setStatus("current")
_BosPvrstInstPortDesignatedBridge_Type = BridgeId
_BosPvrstInstPortDesignatedBridge_Object = MibTableColumn
bosPvrstInstPortDesignatedBridge = _BosPvrstInstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 6),
    _BosPvrstInstPortDesignatedBridge_Type()
)
bosPvrstInstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortDesignatedBridge.setStatus("current")


class _BosPvrstInstPortDesignatedPort_Type(OctetString):
    """Custom type bosPvrstInstPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_BosPvrstInstPortDesignatedPort_Type.__name__ = "OctetString"
_BosPvrstInstPortDesignatedPort_Object = MibTableColumn
bosPvrstInstPortDesignatedPort = _BosPvrstInstPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 7),
    _BosPvrstInstPortDesignatedPort_Type()
)
bosPvrstInstPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortDesignatedPort.setStatus("current")


class _BosPvrstInstPortOperVersion_Type(Integer32):
    """Custom type bosPvrstInstPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stpCompatible", 0),
          ("rstp", 2))
    )


_BosPvrstInstPortOperVersion_Type.__name__ = "Integer32"
_BosPvrstInstPortOperVersion_Object = MibTableColumn
bosPvrstInstPortOperVersion = _BosPvrstInstPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 8),
    _BosPvrstInstPortOperVersion_Type()
)
bosPvrstInstPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortOperVersion.setStatus("current")
_BosPvrstInstPortProtocolMigration_Type = TruthValue
_BosPvrstInstPortProtocolMigration_Object = MibTableColumn
bosPvrstInstPortProtocolMigration = _BosPvrstInstPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 9),
    _BosPvrstInstPortProtocolMigration_Type()
)
bosPvrstInstPortProtocolMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortProtocolMigration.setStatus("current")


class _BosPvrstInstPortState_Type(Integer32):
    """Custom type bosPvrstInstPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("learning", 4),
          ("forwarding", 5))
    )


_BosPvrstInstPortState_Type.__name__ = "Integer32"
_BosPvrstInstPortState_Object = MibTableColumn
bosPvrstInstPortState = _BosPvrstInstPortState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 10),
    _BosPvrstInstPortState_Type()
)
bosPvrstInstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortState.setStatus("current")
_BosPvrstInstPortForwardTransitions_Type = Counter32
_BosPvrstInstPortForwardTransitions_Object = MibTableColumn
bosPvrstInstPortForwardTransitions = _BosPvrstInstPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 11),
    _BosPvrstInstPortForwardTransitions_Type()
)
bosPvrstInstPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortForwardTransitions.setStatus("current")
_BosPvrstInstPortReceivedBpdus_Type = Counter32
_BosPvrstInstPortReceivedBpdus_Object = MibTableColumn
bosPvrstInstPortReceivedBpdus = _BosPvrstInstPortReceivedBpdus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 12),
    _BosPvrstInstPortReceivedBpdus_Type()
)
bosPvrstInstPortReceivedBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortReceivedBpdus.setStatus("current")
_BosPvrstInstPortRxConfigBpduCount_Type = Counter32
_BosPvrstInstPortRxConfigBpduCount_Object = MibTableColumn
bosPvrstInstPortRxConfigBpduCount = _BosPvrstInstPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 13),
    _BosPvrstInstPortRxConfigBpduCount_Type()
)
bosPvrstInstPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortRxConfigBpduCount.setStatus("current")
_BosPvrstInstPortRxTcnBpduCount_Type = Counter32
_BosPvrstInstPortRxTcnBpduCount_Object = MibTableColumn
bosPvrstInstPortRxTcnBpduCount = _BosPvrstInstPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 14),
    _BosPvrstInstPortRxTcnBpduCount_Type()
)
bosPvrstInstPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortRxTcnBpduCount.setStatus("current")
_BosPvrstInstPortTransmittedBpdus_Type = Counter32
_BosPvrstInstPortTransmittedBpdus_Object = MibTableColumn
bosPvrstInstPortTransmittedBpdus = _BosPvrstInstPortTransmittedBpdus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 15),
    _BosPvrstInstPortTransmittedBpdus_Type()
)
bosPvrstInstPortTransmittedBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortTransmittedBpdus.setStatus("current")
_BosPvrstInstPortTxConfigBpduCount_Type = Counter32
_BosPvrstInstPortTxConfigBpduCount_Object = MibTableColumn
bosPvrstInstPortTxConfigBpduCount = _BosPvrstInstPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 16),
    _BosPvrstInstPortTxConfigBpduCount_Type()
)
bosPvrstInstPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortTxConfigBpduCount.setStatus("current")
_BosPvrstInstPortTxTcnBpduCount_Type = Counter32
_BosPvrstInstPortTxTcnBpduCount_Object = MibTableColumn
bosPvrstInstPortTxTcnBpduCount = _BosPvrstInstPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 17),
    _BosPvrstInstPortTxTcnBpduCount_Type()
)
bosPvrstInstPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortTxTcnBpduCount.setStatus("current")
_BosPvrstInstPortInvalidBpdusRcvd_Type = Counter32
_BosPvrstInstPortInvalidBpdusRcvd_Object = MibTableColumn
bosPvrstInstPortInvalidBpdusRcvd = _BosPvrstInstPortInvalidBpdusRcvd_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 18),
    _BosPvrstInstPortInvalidBpdusRcvd_Type()
)
bosPvrstInstPortInvalidBpdusRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortInvalidBpdusRcvd.setStatus("current")
_BosPvrstInstPortInvalidConfigBpduRxCount_Type = Counter32
_BosPvrstInstPortInvalidConfigBpduRxCount_Object = MibTableColumn
bosPvrstInstPortInvalidConfigBpduRxCount = _BosPvrstInstPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 19),
    _BosPvrstInstPortInvalidConfigBpduRxCount_Type()
)
bosPvrstInstPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortInvalidConfigBpduRxCount.setStatus("current")
_BosPvrstInstPortInvalidTcnBpduRxCount_Type = Counter32
_BosPvrstInstPortInvalidTcnBpduRxCount_Object = MibTableColumn
bosPvrstInstPortInvalidTcnBpduRxCount = _BosPvrstInstPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 20),
    _BosPvrstInstPortInvalidTcnBpduRxCount_Type()
)
bosPvrstInstPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortInvalidTcnBpduRxCount.setStatus("current")


class _BosPvrstInstPortTxSemState_Type(Integer32):
    """Custom type bosPvrstInstPortTxSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("transmitinit", 0),
          ("transmitperiodic", 1),
          ("transmitconfig", 2),
          ("transmittcn", 3),
          ("transmitrstp", 4),
          ("idle", 5))
    )


_BosPvrstInstPortTxSemState_Type.__name__ = "Integer32"
_BosPvrstInstPortTxSemState_Object = MibTableColumn
bosPvrstInstPortTxSemState = _BosPvrstInstPortTxSemState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 21),
    _BosPvrstInstPortTxSemState_Type()
)
bosPvrstInstPortTxSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortTxSemState.setStatus("current")


class _BosPvrstInstPortProtMigrationSemState_Type(Integer32):
    """Custom type bosPvrstInstPortProtMigrationSemState based on Integer32"""
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
        *(("init", 0),
          ("sendrstp", 1),
          ("sendingrstp", 2),
          ("sendstp", 3),
          ("sendingstp", 4))
    )


_BosPvrstInstPortProtMigrationSemState_Type.__name__ = "Integer32"
_BosPvrstInstPortProtMigrationSemState_Object = MibTableColumn
bosPvrstInstPortProtMigrationSemState = _BosPvrstInstPortProtMigrationSemState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 22),
    _BosPvrstInstPortProtMigrationSemState_Type()
)
bosPvrstInstPortProtMigrationSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortProtMigrationSemState.setStatus("current")
_BosPvrstInstProtocolMigrationCount_Type = Counter32
_BosPvrstInstProtocolMigrationCount_Object = MibTableColumn
bosPvrstInstProtocolMigrationCount = _BosPvrstInstProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 23),
    _BosPvrstInstProtocolMigrationCount_Type()
)
bosPvrstInstProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstProtocolMigrationCount.setStatus("current")


class _BosPvrstInstPortRole_Type(Integer32):
    """Custom type bosPvrstInstPortRole based on Integer32"""
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
        *(("disabled", 0),
          ("alternate", 1),
          ("backup", 2),
          ("root", 3),
          ("designated", 4))
    )


_BosPvrstInstPortRole_Type.__name__ = "Integer32"
_BosPvrstInstPortRole_Object = MibTableColumn
bosPvrstInstPortRole = _BosPvrstInstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 24),
    _BosPvrstInstPortRole_Type()
)
bosPvrstInstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortRole.setStatus("current")


class _BosPvrstInstCurrentPortRole_Type(Integer32):
    """Custom type bosPvrstInstCurrentPortRole based on Integer32"""
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
        *(("disabled", 0),
          ("alternate", 1),
          ("backup", 2),
          ("root", 3),
          ("designated", 4))
    )


_BosPvrstInstCurrentPortRole_Type.__name__ = "Integer32"
_BosPvrstInstCurrentPortRole_Object = MibTableColumn
bosPvrstInstCurrentPortRole = _BosPvrstInstCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 25),
    _BosPvrstInstCurrentPortRole_Type()
)
bosPvrstInstCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstCurrentPortRole.setStatus("current")


class _BosPvrstInstPortInfoSemState_Type(Integer32):
    """Custom type bosPvrstInstPortInfoSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("aged", 1),
          ("update", 2),
          ("superiordesg", 3),
          ("repeatdesg", 4),
          ("aggerment", 5),
          ("present", 6),
          ("receive", 7))
    )


_BosPvrstInstPortInfoSemState_Type.__name__ = "Integer32"
_BosPvrstInstPortInfoSemState_Object = MibTableColumn
bosPvrstInstPortInfoSemState = _BosPvrstInstPortInfoSemState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 26),
    _BosPvrstInstPortInfoSemState_Type()
)
bosPvrstInstPortInfoSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortInfoSemState.setStatus("current")


class _BosPvrstInstPortRoleTransitionSemState_Type(Integer32):
    """Custom type bosPvrstInstPortRoleTransitionSemState based on Integer32"""
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
        *(("init", 0),
          ("blockport", 1),
          ("blockedport", 2),
          ("rootport", 3),
          ("designatedport", 4))
    )


_BosPvrstInstPortRoleTransitionSemState_Type.__name__ = "Integer32"
_BosPvrstInstPortRoleTransitionSemState_Object = MibTableColumn
bosPvrstInstPortRoleTransitionSemState = _BosPvrstInstPortRoleTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 27),
    _BosPvrstInstPortRoleTransitionSemState_Type()
)
bosPvrstInstPortRoleTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortRoleTransitionSemState.setStatus("current")


class _BosPvrstInstPortStateTransitionSemState_Type(Integer32):
    """Custom type bosPvrstInstPortStateTransitionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("learning", 1),
          ("forwarding", 2))
    )


_BosPvrstInstPortStateTransitionSemState_Type.__name__ = "Integer32"
_BosPvrstInstPortStateTransitionSemState_Object = MibTableColumn
bosPvrstInstPortStateTransitionSemState = _BosPvrstInstPortStateTransitionSemState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 28),
    _BosPvrstInstPortStateTransitionSemState_Type()
)
bosPvrstInstPortStateTransitionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortStateTransitionSemState.setStatus("current")


class _BosPvrstInstPortTopologyChangeSemState_Type(Integer32):
    """Custom type bosPvrstInstPortTopologyChangeSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("inactive", 1),
          ("active", 2),
          ("detected", 3),
          ("notifiedtcn", 4),
          ("notifiedtc", 5),
          ("propagating", 6),
          ("acknowledged", 7))
    )


_BosPvrstInstPortTopologyChangeSemState_Type.__name__ = "Integer32"
_BosPvrstInstPortTopologyChangeSemState_Object = MibTableColumn
bosPvrstInstPortTopologyChangeSemState = _BosPvrstInstPortTopologyChangeSemState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 29),
    _BosPvrstInstPortTopologyChangeSemState_Type()
)
bosPvrstInstPortTopologyChangeSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortTopologyChangeSemState.setStatus("current")
_BosPvrstInstPortEffectivePortState_Type = TruthValue
_BosPvrstInstPortEffectivePortState_Object = MibTableColumn
bosPvrstInstPortEffectivePortState = _BosPvrstInstPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 30),
    _BosPvrstInstPortEffectivePortState_Type()
)
bosPvrstInstPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortEffectivePortState.setStatus("current")


class _BosPvrstInstPortHelloTime_Type(Timeout):
    """Custom type bosPvrstInstPortHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_BosPvrstInstPortHelloTime_Type.__name__ = "Timeout"
_BosPvrstInstPortHelloTime_Object = MibTableColumn
bosPvrstInstPortHelloTime = _BosPvrstInstPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 31),
    _BosPvrstInstPortHelloTime_Type()
)
bosPvrstInstPortHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortHelloTime.setStatus("current")
_BosPvrstInstPortMaxAge_Type = Timeout
_BosPvrstInstPortMaxAge_Object = MibTableColumn
bosPvrstInstPortMaxAge = _BosPvrstInstPortMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 32),
    _BosPvrstInstPortMaxAge_Type()
)
bosPvrstInstPortMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortMaxAge.setStatus("current")
_BosPvrstInstPortForwardDelay_Type = Timeout
_BosPvrstInstPortForwardDelay_Object = MibTableColumn
bosPvrstInstPortForwardDelay = _BosPvrstInstPortForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 33),
    _BosPvrstInstPortForwardDelay_Type()
)
bosPvrstInstPortForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortForwardDelay.setStatus("current")
_BosPvrstInstPortHoldTime_Type = Integer32
_BosPvrstInstPortHoldTime_Object = MibTableColumn
bosPvrstInstPortHoldTime = _BosPvrstInstPortHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 1, 16, 1, 34),
    _BosPvrstInstPortHoldTime_Type()
)
bosPvrstInstPortHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstInstPortHoldTime.setStatus("current")
_BosPvrstTrapsControl_ObjectIdentity = ObjectIdentity
bosPvrstTrapsControl = _BosPvrstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2)
)


class _BosPvrstSetGlobalTrapOption_Type(Integer32):
    """Custom type bosPvrstSetGlobalTrapOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BosPvrstSetGlobalTrapOption_Type.__name__ = "Integer32"
_BosPvrstSetGlobalTrapOption_Object = MibScalar
bosPvrstSetGlobalTrapOption = _BosPvrstSetGlobalTrapOption_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2, 1),
    _BosPvrstSetGlobalTrapOption_Type()
)
bosPvrstSetGlobalTrapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstSetGlobalTrapOption.setStatus("current")


class _BosPvrstGlobalErrTrapType_Type(Integer32):
    """Custom type bosPvrstGlobalErrTrapType based on Integer32"""
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
          ("memfail", 1),
          ("bufffail", 2))
    )


_BosPvrstGlobalErrTrapType_Type.__name__ = "Integer32"
_BosPvrstGlobalErrTrapType_Object = MibScalar
bosPvrstGlobalErrTrapType = _BosPvrstGlobalErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2, 2),
    _BosPvrstGlobalErrTrapType_Type()
)
bosPvrstGlobalErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstGlobalErrTrapType.setStatus("current")


class _BosPvrstSetTraps_Type(Integer32):
    """Custom type bosPvrstSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BosPvrstSetTraps_Type.__name__ = "Integer32"
_BosPvrstSetTraps_Object = MibScalar
bosPvrstSetTraps = _BosPvrstSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2, 3),
    _BosPvrstSetTraps_Type()
)
bosPvrstSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPvrstSetTraps.setStatus("current")


class _BosPvrstGenTrapType_Type(Integer32):
    """Custom type bosPvrstGenTrapType based on Integer32"""
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
          ("up", 1),
          ("down", 2))
    )


_BosPvrstGenTrapType_Type.__name__ = "Integer32"
_BosPvrstGenTrapType_Object = MibScalar
bosPvrstGenTrapType = _BosPvrstGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2, 4),
    _BosPvrstGenTrapType_Type()
)
bosPvrstGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstGenTrapType.setStatus("current")
_BosPvrstPortTrapNotificationTable_Object = MibTable
bosPvrstPortTrapNotificationTable = _BosPvrstPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2, 5)
)
if mibBuilder.loadTexts:
    bosPvrstPortTrapNotificationTable.setStatus("current")
_BosPvrstPortTrapNotificationEntry_Object = MibTableRow
bosPvrstPortTrapNotificationEntry = _BosPvrstPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2, 5, 1)
)
bosPvrstPortTrapNotificationEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPvrstPortTrapIndex"),
)
if mibBuilder.loadTexts:
    bosPvrstPortTrapNotificationEntry.setStatus("current")


class _BosPvrstPortTrapIndex_Type(Integer32):
    """Custom type bosPvrstPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_BosPvrstPortTrapIndex_Type.__name__ = "Integer32"
_BosPvrstPortTrapIndex_Object = MibTableColumn
bosPvrstPortTrapIndex = _BosPvrstPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2, 5, 1, 1),
    _BosPvrstPortTrapIndex_Type()
)
bosPvrstPortTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstPortTrapIndex.setStatus("current")


class _BosPvrstPortMigrationType_Type(Integer32):
    """Custom type bosPvrstPortMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendstp", 0),
          ("sendrstp", 1))
    )


_BosPvrstPortMigrationType_Type.__name__ = "Integer32"
_BosPvrstPortMigrationType_Object = MibTableColumn
bosPvrstPortMigrationType = _BosPvrstPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2, 5, 1, 2),
    _BosPvrstPortMigrationType_Type()
)
bosPvrstPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstPortMigrationType.setStatus("current")


class _BosPvrstPktErrType_Type(Integer32):
    """Custom type bosPvrstPktErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("protocolIdErr", 0),
          ("invalidBpdu", 1),
          ("configLengthErr", 2),
          ("tcnLengthErr", 3),
          ("rstpLengthErr", 4),
          ("maxAgeErr", 5),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7),
          ("pvrstpLengthErr", 8))
    )


_BosPvrstPktErrType_Type.__name__ = "Integer32"
_BosPvrstPktErrType_Object = MibTableColumn
bosPvrstPktErrType = _BosPvrstPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2, 5, 1, 3),
    _BosPvrstPktErrType_Type()
)
bosPvrstPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstPktErrType.setStatus("current")
_BosPvrstPktErrVal_Type = Integer32
_BosPvrstPktErrVal_Object = MibTableColumn
bosPvrstPktErrVal = _BosPvrstPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 2, 5, 1, 4),
    _BosPvrstPktErrVal_Type()
)
bosPvrstPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPvrstPktErrVal.setStatus("current")
_BosPvrstTraps_ObjectIdentity = ObjectIdentity
bosPvrstTraps = _BosPvrstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 3)
)
_BosPvrstNotifyTraps_ObjectIdentity = ObjectIdentity
bosPvrstNotifyTraps = _BosPvrstNotifyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 3, 0)
)
_BosRstMIB_ObjectIdentity = ObjectIdentity
bosRstMIB = _BosRstMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79)
)
_Dot1wBosRst_ObjectIdentity = ObjectIdentity
dot1wBosRst = _Dot1wBosRst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1)
)


class _BosRstSystemControl_Type(Integer32):
    """Custom type bosRstSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_BosRstSystemControl_Type.__name__ = "Integer32"
_BosRstSystemControl_Object = MibScalar
bosRstSystemControl = _BosRstSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 1),
    _BosRstSystemControl_Type()
)
bosRstSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRstSystemControl.setStatus("current")
_BosRstModuleStatus_Type = EnabledStatus
_BosRstModuleStatus_Object = MibScalar
bosRstModuleStatus = _BosRstModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 2),
    _BosRstModuleStatus_Type()
)
bosRstModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRstModuleStatus.setStatus("current")
_BosRstPortExtTable_Object = MibTable
bosRstPortExtTable = _BosRstPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3)
)
if mibBuilder.loadTexts:
    bosRstPortExtTable.setStatus("current")
_BosRstPortExtEntry_Object = MibTableRow
bosRstPortExtEntry = _BosRstPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1)
)
bosRstPortExtEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosRstPort"),
)
if mibBuilder.loadTexts:
    bosRstPortExtEntry.setStatus("current")


class _BosRstPort_Type(Integer32):
    """Custom type bosRstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_BosRstPort_Type.__name__ = "Integer32"
_BosRstPort_Object = MibTableColumn
bosRstPort = _BosRstPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 1),
    _BosRstPort_Type()
)
bosRstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosRstPort.setStatus("current")


class _BosRstPortRole_Type(Integer32):
    """Custom type bosRstPortRole based on Integer32"""
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
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_BosRstPortRole_Type.__name__ = "Integer32"
_BosRstPortRole_Object = MibTableColumn
bosRstPortRole = _BosRstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 2),
    _BosRstPortRole_Type()
)
bosRstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortRole.setStatus("current")


class _BosRstPortOperVersion_Type(Integer32):
    """Custom type bosRstPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stpCompatible", 0),
          ("rstp", 2))
    )


_BosRstPortOperVersion_Type.__name__ = "Integer32"
_BosRstPortOperVersion_Object = MibTableColumn
bosRstPortOperVersion = _BosRstPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 3),
    _BosRstPortOperVersion_Type()
)
bosRstPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortOperVersion.setStatus("current")


class _BosRstPortRoleTransSmState_Type(Integer32):
    """Custom type bosRstPortRoleTransSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("disableport", 1),
          ("disabledport", 2),
          ("rootport", 3),
          ("designatedport", 4),
          ("backupport", 5),
          ("rootproposed", 6),
          ("rootagreed", 7),
          ("reroot", 8),
          ("rootforward", 9),
          ("rootlearn", 10),
          ("rerooted", 11),
          ("designatedpropose", 12),
          ("designatedsynced", 13),
          ("designatedretired", 14),
          ("designatedforward", 15),
          ("designatedlearn", 16),
          ("designatedlisten", 17))
    )


_BosRstPortRoleTransSmState_Type.__name__ = "Integer32"
_BosRstPortRoleTransSmState_Object = MibTableColumn
bosRstPortRoleTransSmState = _BosRstPortRoleTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 4),
    _BosRstPortRoleTransSmState_Type()
)
bosRstPortRoleTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortRoleTransSmState.setStatus("current")


class _BosRstPortStateTransSmState_Type(Integer32):
    """Custom type bosRstPortStateTransSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("learning", 1),
          ("forwarding", 2))
    )


_BosRstPortStateTransSmState_Type.__name__ = "Integer32"
_BosRstPortStateTransSmState_Object = MibTableColumn
bosRstPortStateTransSmState = _BosRstPortStateTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 5),
    _BosRstPortStateTransSmState_Type()
)
bosRstPortStateTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortStateTransSmState.setStatus("current")
_BosRstPortRxRstBpduCount_Type = Counter32
_BosRstPortRxRstBpduCount_Object = MibTableColumn
bosRstPortRxRstBpduCount = _BosRstPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 6),
    _BosRstPortRxRstBpduCount_Type()
)
bosRstPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortRxRstBpduCount.setStatus("current")
_BosRstPortRxConfigBpduCount_Type = Counter32
_BosRstPortRxConfigBpduCount_Object = MibTableColumn
bosRstPortRxConfigBpduCount = _BosRstPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 7),
    _BosRstPortRxConfigBpduCount_Type()
)
bosRstPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortRxConfigBpduCount.setStatus("current")
_BosRstPortRxTcnBpduCount_Type = Counter32
_BosRstPortRxTcnBpduCount_Object = MibTableColumn
bosRstPortRxTcnBpduCount = _BosRstPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 8),
    _BosRstPortRxTcnBpduCount_Type()
)
bosRstPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortRxTcnBpduCount.setStatus("current")
_BosRstPortTxRstBpduCount_Type = Counter32
_BosRstPortTxRstBpduCount_Object = MibTableColumn
bosRstPortTxRstBpduCount = _BosRstPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 9),
    _BosRstPortTxRstBpduCount_Type()
)
bosRstPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortTxRstBpduCount.setStatus("current")
_BosRstPortTxConfigBpduCount_Type = Counter32
_BosRstPortTxConfigBpduCount_Object = MibTableColumn
bosRstPortTxConfigBpduCount = _BosRstPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 10),
    _BosRstPortTxConfigBpduCount_Type()
)
bosRstPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortTxConfigBpduCount.setStatus("current")
_BosRstPortTxTcnBpduCount_Type = Counter32
_BosRstPortTxTcnBpduCount_Object = MibTableColumn
bosRstPortTxTcnBpduCount = _BosRstPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 11),
    _BosRstPortTxTcnBpduCount_Type()
)
bosRstPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortTxTcnBpduCount.setStatus("current")
_BosRstPortInvalidRstBpduRxCount_Type = Counter32
_BosRstPortInvalidRstBpduRxCount_Object = MibTableColumn
bosRstPortInvalidRstBpduRxCount = _BosRstPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 12),
    _BosRstPortInvalidRstBpduRxCount_Type()
)
bosRstPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortInvalidRstBpduRxCount.setStatus("current")
_BosRstPortInvalidConfigBpduRxCount_Type = Counter32
_BosRstPortInvalidConfigBpduRxCount_Object = MibTableColumn
bosRstPortInvalidConfigBpduRxCount = _BosRstPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 13),
    _BosRstPortInvalidConfigBpduRxCount_Type()
)
bosRstPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortInvalidConfigBpduRxCount.setStatus("current")
_BosRstPortInvalidTcnBpduRxCount_Type = Counter32
_BosRstPortInvalidTcnBpduRxCount_Object = MibTableColumn
bosRstPortInvalidTcnBpduRxCount = _BosRstPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 14),
    _BosRstPortInvalidTcnBpduRxCount_Type()
)
bosRstPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortInvalidTcnBpduRxCount.setStatus("current")
_BosRstPortProtocolMigrationCount_Type = Counter32
_BosRstPortProtocolMigrationCount_Object = MibTableColumn
bosRstPortProtocolMigrationCount = _BosRstPortProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 15),
    _BosRstPortProtocolMigrationCount_Type()
)
bosRstPortProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortProtocolMigrationCount.setStatus("current")
_BosRstPortAutoEdge_Type = TruthValue
_BosRstPortAutoEdge_Object = MibTableColumn
bosRstPortAutoEdge = _BosRstPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 3, 1, 16),
    _BosRstPortAutoEdge_Type()
)
bosRstPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRstPortAutoEdge.setStatus("current")


class _BosRstDynamicPathcostCalculation_Type(TruthValue):
    """Custom type bosRstDynamicPathcostCalculation based on TruthValue"""
    defaultValue = 2


_BosRstDynamicPathcostCalculation_Type.__name__ = "TruthValue"
_BosRstDynamicPathcostCalculation_Object = MibScalar
bosRstDynamicPathcostCalculation = _BosRstDynamicPathcostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 4),
    _BosRstDynamicPathcostCalculation_Type()
)
bosRstDynamicPathcostCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRstDynamicPathcostCalculation.setStatus("current")
_BosRstOldDesignatedRoot_Type = BridgeId
_BosRstOldDesignatedRoot_Object = MibScalar
bosRstOldDesignatedRoot = _BosRstOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 1, 5),
    _BosRstOldDesignatedRoot_Type()
)
bosRstOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstOldDesignatedRoot.setStatus("current")
_Dot1wBosRstTrapsControl_ObjectIdentity = ObjectIdentity
dot1wBosRstTrapsControl = _Dot1wBosRstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2)
)


class _BosRstSetTraps_Type(Integer32):
    """Custom type bosRstSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosRstSetTraps_Type.__name__ = "Integer32"
_BosRstSetTraps_Object = MibScalar
bosRstSetTraps = _BosRstSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 1),
    _BosRstSetTraps_Type()
)
bosRstSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRstSetTraps.setStatus("current")


class _BosRstGenTrapType_Type(Integer32):
    """Custom type bosRstGenTrapType based on Integer32"""
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
          ("up", 1),
          ("down", 2))
    )


_BosRstGenTrapType_Type.__name__ = "Integer32"
_BosRstGenTrapType_Object = MibScalar
bosRstGenTrapType = _BosRstGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 2),
    _BosRstGenTrapType_Type()
)
bosRstGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstGenTrapType.setStatus("current")


class _BosRstErrTrapType_Type(Integer32):
    """Custom type bosRstErrTrapType based on Integer32"""
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
          ("memfail", 1),
          ("bufffail", 2))
    )


_BosRstErrTrapType_Type.__name__ = "Integer32"
_BosRstErrTrapType_Object = MibScalar
bosRstErrTrapType = _BosRstErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 3),
    _BosRstErrTrapType_Type()
)
bosRstErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstErrTrapType.setStatus("current")
_BosRstPortTrapNotificationTable_Object = MibTable
bosRstPortTrapNotificationTable = _BosRstPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 4)
)
if mibBuilder.loadTexts:
    bosRstPortTrapNotificationTable.setStatus("current")
_BosRstPortTrapNotificationEntry_Object = MibTableRow
bosRstPortTrapNotificationEntry = _BosRstPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 4, 1)
)
bosRstPortTrapNotificationEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosRstPortTrapIndex"),
)
if mibBuilder.loadTexts:
    bosRstPortTrapNotificationEntry.setStatus("current")


class _BosRstPortTrapIndex_Type(Integer32):
    """Custom type bosRstPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_BosRstPortTrapIndex_Type.__name__ = "Integer32"
_BosRstPortTrapIndex_Object = MibTableColumn
bosRstPortTrapIndex = _BosRstPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 4, 1, 1),
    _BosRstPortTrapIndex_Type()
)
bosRstPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosRstPortTrapIndex.setStatus("current")


class _BosRstPortMigrationType_Type(Integer32):
    """Custom type bosRstPortMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendstp", 0),
          ("sendrstp", 1))
    )


_BosRstPortMigrationType_Type.__name__ = "Integer32"
_BosRstPortMigrationType_Object = MibTableColumn
bosRstPortMigrationType = _BosRstPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 4, 1, 2),
    _BosRstPortMigrationType_Type()
)
bosRstPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortMigrationType.setStatus("current")


class _BosRstPktErrType_Type(Integer32):
    """Custom type bosRstPktErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("protocolIdErr", 0),
          ("invalidBpdu", 1),
          ("configLengthErr", 2),
          ("tcnLengthErr", 3),
          ("rstpLengthErr", 4),
          ("maxAgeErr", 5),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7))
    )


_BosRstPktErrType_Type.__name__ = "Integer32"
_BosRstPktErrType_Object = MibTableColumn
bosRstPktErrType = _BosRstPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 4, 1, 3),
    _BosRstPktErrType_Type()
)
bosRstPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPktErrType.setStatus("current")
_BosRstPktErrVal_Type = Integer32
_BosRstPktErrVal_Object = MibTableColumn
bosRstPktErrVal = _BosRstPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 4, 1, 4),
    _BosRstPktErrVal_Type()
)
bosRstPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPktErrVal.setStatus("current")


class _BosRstPortRoleType_Type(Integer32):
    """Custom type bosRstPortRoleType based on Integer32"""
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
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_BosRstPortRoleType_Type.__name__ = "Integer32"
_BosRstPortRoleType_Object = MibTableColumn
bosRstPortRoleType = _BosRstPortRoleType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 4, 1, 5),
    _BosRstPortRoleType_Type()
)
bosRstPortRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstPortRoleType.setStatus("current")


class _BosRstOldRoleType_Type(Integer32):
    """Custom type bosRstOldRoleType based on Integer32"""
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
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_BosRstOldRoleType_Type.__name__ = "Integer32"
_BosRstOldRoleType_Object = MibTableColumn
bosRstOldRoleType = _BosRstOldRoleType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 2, 4, 1, 6),
    _BosRstOldRoleType_Type()
)
bosRstOldRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRstOldRoleType.setStatus("current")
_Dot1wBosRstTraps_ObjectIdentity = ObjectIdentity
dot1wBosRstTraps = _Dot1wBosRstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 3)
)
_BosRstTraps_ObjectIdentity = ObjectIdentity
bosRstTraps = _BosRstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 3, 0)
)
_BosMstMIB_ObjectIdentity = ObjectIdentity
bosMstMIB = _BosMstMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80)
)
_Dot1sBosMst_ObjectIdentity = ObjectIdentity
dot1sBosMst = _Dot1sBosMst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1)
)


class _BosMstSystemControl_Type(Integer32):
    """Custom type bosMstSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_BosMstSystemControl_Type.__name__ = "Integer32"
_BosMstSystemControl_Object = MibScalar
bosMstSystemControl = _BosMstSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 1),
    _BosMstSystemControl_Type()
)
bosMstSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstSystemControl.setStatus("current")


class _BosMstMaxHopCount_Type(Integer32):
    """Custom type bosMstMaxHopCount based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_BosMstMaxHopCount_Type.__name__ = "Integer32"
_BosMstMaxHopCount_Object = MibScalar
bosMstMaxHopCount = _BosMstMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 3),
    _BosMstMaxHopCount_Type()
)
bosMstMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstMaxHopCount.setStatus("current")
_BosMstBrgAddress_Type = MacAddress
_BosMstBrgAddress_Object = MibScalar
bosMstBrgAddress = _BosMstBrgAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 4),
    _BosMstBrgAddress_Type()
)
bosMstBrgAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstBrgAddress.setStatus("current")
_BosMstCistRoot_Type = BridgeId
_BosMstCistRoot_Object = MibScalar
bosMstCistRoot = _BosMstCistRoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 5),
    _BosMstCistRoot_Type()
)
bosMstCistRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistRoot.setStatus("current")
_BosMstCistRegionalRoot_Type = BridgeId
_BosMstCistRegionalRoot_Object = MibScalar
bosMstCistRegionalRoot = _BosMstCistRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 6),
    _BosMstCistRegionalRoot_Type()
)
bosMstCistRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistRegionalRoot.setStatus("current")
_BosMstCistRootCost_Type = Integer32
_BosMstCistRootCost_Object = MibScalar
bosMstCistRootCost = _BosMstCistRootCost_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 7),
    _BosMstCistRootCost_Type()
)
bosMstCistRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistRootCost.setStatus("current")
_BosMstCistRegionalRootCost_Type = Integer32
_BosMstCistRegionalRootCost_Object = MibScalar
bosMstCistRegionalRootCost = _BosMstCistRegionalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 8),
    _BosMstCistRegionalRootCost_Type()
)
bosMstCistRegionalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistRegionalRootCost.setStatus("current")
_BosMstCistRootPort_Type = Integer32
_BosMstCistRootPort_Object = MibScalar
bosMstCistRootPort = _BosMstCistRootPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 9),
    _BosMstCistRootPort_Type()
)
bosMstCistRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistRootPort.setStatus("current")


class _BosMstCistBridgePriority_Type(Integer32):
    """Custom type bosMstCistBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_BosMstCistBridgePriority_Type.__name__ = "Integer32"
_BosMstCistBridgePriority_Object = MibScalar
bosMstCistBridgePriority = _BosMstCistBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 10),
    _BosMstCistBridgePriority_Type()
)
bosMstCistBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistBridgePriority.setStatus("current")


class _BosMstCistBridgeMaxAge_Type(Timeout):
    """Custom type bosMstCistBridgeMaxAge based on Timeout"""
    defaultValue = 20

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_BosMstCistBridgeMaxAge_Type.__name__ = "Timeout"
_BosMstCistBridgeMaxAge_Object = MibScalar
bosMstCistBridgeMaxAge = _BosMstCistBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 11),
    _BosMstCistBridgeMaxAge_Type()
)
bosMstCistBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistBridgeMaxAge.setStatus("current")


class _BosMstCistBridgeForwardDelay_Type(Timeout):
    """Custom type bosMstCistBridgeForwardDelay based on Timeout"""
    defaultValue = 15

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_BosMstCistBridgeForwardDelay_Type.__name__ = "Timeout"
_BosMstCistBridgeForwardDelay_Object = MibScalar
bosMstCistBridgeForwardDelay = _BosMstCistBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 12),
    _BosMstCistBridgeForwardDelay_Type()
)
bosMstCistBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistBridgeForwardDelay.setStatus("current")
_BosMstCistMaxAge_Type = Timeout
_BosMstCistMaxAge_Object = MibScalar
bosMstCistMaxAge = _BosMstCistMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 13),
    _BosMstCistMaxAge_Type()
)
bosMstCistMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistMaxAge.setStatus("current")
_BosMstCistForwardDelay_Type = Timeout
_BosMstCistForwardDelay_Object = MibScalar
bosMstCistForwardDelay = _BosMstCistForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 14),
    _BosMstCistForwardDelay_Type()
)
bosMstCistForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistForwardDelay.setStatus("current")


class _BosMstMstiRegionName_Type(DisplayString):
    """Custom type bosMstMstiRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BosMstMstiRegionName_Type.__name__ = "DisplayString"
_BosMstMstiRegionName_Object = MibScalar
bosMstMstiRegionName = _BosMstMstiRegionName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 15),
    _BosMstMstiRegionName_Type()
)
bosMstMstiRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstMstiRegionName.setStatus("current")


class _BosMstMstiRegionVersion_Type(Integer32):
    """Custom type bosMstMstiRegionVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BosMstMstiRegionVersion_Type.__name__ = "Integer32"
_BosMstMstiRegionVersion_Object = MibScalar
bosMstMstiRegionVersion = _BosMstMstiRegionVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 16),
    _BosMstMstiRegionVersion_Type()
)
bosMstMstiRegionVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstMstiRegionVersion.setStatus("current")


class _BosMstMstiConfigDigest_Type(OctetString):
    """Custom type bosMstMstiConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BosMstMstiConfigDigest_Type.__name__ = "OctetString"
_BosMstMstiConfigDigest_Object = MibScalar
bosMstMstiConfigDigest = _BosMstMstiConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 17),
    _BosMstMstiConfigDigest_Type()
)
bosMstMstiConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiConfigDigest.setStatus("current")
_BosMstBufferOverFlowCount_Type = Counter32
_BosMstBufferOverFlowCount_Object = MibScalar
bosMstBufferOverFlowCount = _BosMstBufferOverFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 18),
    _BosMstBufferOverFlowCount_Type()
)
bosMstBufferOverFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstBufferOverFlowCount.setStatus("current")
_BosMstMemAllocFailureCount_Type = Counter32
_BosMstMemAllocFailureCount_Object = MibScalar
bosMstMemAllocFailureCount = _BosMstMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 19),
    _BosMstMemAllocFailureCount_Type()
)
bosMstMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMemAllocFailureCount.setStatus("current")
_BosMstRegionConfigChangeCount_Type = Counter32
_BosMstRegionConfigChangeCount_Object = MibScalar
bosMstRegionConfigChangeCount = _BosMstRegionConfigChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 20),
    _BosMstRegionConfigChangeCount_Type()
)
bosMstRegionConfigChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstRegionConfigChangeCount.setStatus("current")


class _BosMstCistBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type bosMstCistBridgeRoleSelectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_BosMstCistBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_BosMstCistBridgeRoleSelectionSemState_Object = MibScalar
bosMstCistBridgeRoleSelectionSemState = _BosMstCistBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 21),
    _BosMstCistBridgeRoleSelectionSemState_Type()
)
bosMstCistBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistBridgeRoleSelectionSemState.setStatus("current")
_BosMstCistTopChanges_Type = Counter32
_BosMstCistTopChanges_Object = MibScalar
bosMstCistTopChanges = _BosMstCistTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 23),
    _BosMstCistTopChanges_Type()
)
bosMstCistTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistTopChanges.setStatus("current")
_BosMstCistNewRootBridgeCount_Type = Counter32
_BosMstCistNewRootBridgeCount_Object = MibScalar
bosMstCistNewRootBridgeCount = _BosMstCistNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 24),
    _BosMstCistNewRootBridgeCount_Type()
)
bosMstCistNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistNewRootBridgeCount.setStatus("current")
_BosMstCistHelloTime_Type = Timeout
_BosMstCistHelloTime_Object = MibScalar
bosMstCistHelloTime = _BosMstCistHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 25),
    _BosMstCistHelloTime_Type()
)
bosMstCistHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistHelloTime.setStatus("current")


class _BosMstCistBridgeHelloTime_Type(Timeout):
    """Custom type bosMstCistBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BosMstCistBridgeHelloTime_Type.__name__ = "Timeout"
_BosMstCistBridgeHelloTime_Object = MibScalar
bosMstCistBridgeHelloTime = _BosMstCistBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 26),
    _BosMstCistBridgeHelloTime_Type()
)
bosMstCistBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistBridgeHelloTime.setStatus("current")
_BosMstMstiBridgeTable_Object = MibTable
bosMstMstiBridgeTable = _BosMstMstiBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27)
)
if mibBuilder.loadTexts:
    bosMstMstiBridgeTable.setStatus("current")
_BosMstMstiBridgeEntry_Object = MibTableRow
bosMstMstiBridgeEntry = _BosMstMstiBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1)
)
if mibBuilder.loadTexts:
    bosMstMstiBridgeEntry.setStatus("current")
_BosMstMstiBridgeRegionalRoot_Type = BridgeId
_BosMstMstiBridgeRegionalRoot_Object = MibTableColumn
bosMstMstiBridgeRegionalRoot = _BosMstMstiBridgeRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1, 2),
    _BosMstMstiBridgeRegionalRoot_Type()
)
bosMstMstiBridgeRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiBridgeRegionalRoot.setStatus("current")


class _BosMstMstiBridgePriority_Type(Integer32):
    """Custom type bosMstMstiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_BosMstMstiBridgePriority_Type.__name__ = "Integer32"
_BosMstMstiBridgePriority_Object = MibTableColumn
bosMstMstiBridgePriority = _BosMstMstiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1, 3),
    _BosMstMstiBridgePriority_Type()
)
bosMstMstiBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstMstiBridgePriority.setStatus("current")
_BosMstMstiRootCost_Type = Integer32
_BosMstMstiRootCost_Object = MibTableColumn
bosMstMstiRootCost = _BosMstMstiRootCost_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1, 4),
    _BosMstMstiRootCost_Type()
)
bosMstMstiRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiRootCost.setStatus("current")
_BosMstMstiRootPort_Type = Integer32
_BosMstMstiRootPort_Object = MibTableColumn
bosMstMstiRootPort = _BosMstMstiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1, 5),
    _BosMstMstiRootPort_Type()
)
bosMstMstiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiRootPort.setStatus("current")
_BosMstMstiTopChanges_Type = Counter32
_BosMstMstiTopChanges_Object = MibTableColumn
bosMstMstiTopChanges = _BosMstMstiTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1, 7),
    _BosMstMstiTopChanges_Type()
)
bosMstMstiTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiTopChanges.setStatus("current")
_BosMstMstiNewRootBridgeCount_Type = Counter32
_BosMstMstiNewRootBridgeCount_Object = MibTableColumn
bosMstMstiNewRootBridgeCount = _BosMstMstiNewRootBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1, 8),
    _BosMstMstiNewRootBridgeCount_Type()
)
bosMstMstiNewRootBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiNewRootBridgeCount.setStatus("current")


class _BosMstMstiBridgeRoleSelectionSemState_Type(Integer32):
    """Custom type bosMstMstiBridgeRoleSelectionSemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_BosMstMstiBridgeRoleSelectionSemState_Type.__name__ = "Integer32"
_BosMstMstiBridgeRoleSelectionSemState_Object = MibTableColumn
bosMstMstiBridgeRoleSelectionSemState = _BosMstMstiBridgeRoleSelectionSemState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1, 9),
    _BosMstMstiBridgeRoleSelectionSemState_Type()
)
bosMstMstiBridgeRoleSelectionSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiBridgeRoleSelectionSemState.setStatus("current")
_BosMstInstanceUpCount_Type = Counter32
_BosMstInstanceUpCount_Object = MibTableColumn
bosMstInstanceUpCount = _BosMstInstanceUpCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1, 10),
    _BosMstInstanceUpCount_Type()
)
bosMstInstanceUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstInstanceUpCount.setStatus("current")
_BosMstInstanceDownCount_Type = Counter32
_BosMstInstanceDownCount_Object = MibTableColumn
bosMstInstanceDownCount = _BosMstInstanceDownCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1, 11),
    _BosMstInstanceDownCount_Type()
)
bosMstInstanceDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstInstanceDownCount.setStatus("current")
_BosMstOldDesignatedRoot_Type = BridgeId
_BosMstOldDesignatedRoot_Object = MibTableColumn
bosMstOldDesignatedRoot = _BosMstOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 27, 1, 12),
    _BosMstOldDesignatedRoot_Type()
)
bosMstOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstOldDesignatedRoot.setStatus("current")
_BosMstVlanInstanceMappingTable_Object = MibTable
bosMstVlanInstanceMappingTable = _BosMstVlanInstanceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28)
)
if mibBuilder.loadTexts:
    bosMstVlanInstanceMappingTable.setStatus("current")
_BosMstVlanInstanceMappingEntry_Object = MibTableRow
bosMstVlanInstanceMappingEntry = _BosMstVlanInstanceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28, 1)
)
bosMstVlanInstanceMappingEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosMstInstanceIndex"),
)
if mibBuilder.loadTexts:
    bosMstVlanInstanceMappingEntry.setStatus("current")


class _BosMstInstanceIndex_Type(Integer32):
    """Custom type bosMstInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BosMstInstanceIndex_Type.__name__ = "Integer32"
_BosMstInstanceIndex_Object = MibTableColumn
bosMstInstanceIndex = _BosMstInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28, 1, 1),
    _BosMstInstanceIndex_Type()
)
bosMstInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosMstInstanceIndex.setStatus("current")
_BosMstMapVlanIndex_Type = VlanId
_BosMstMapVlanIndex_Object = MibTableColumn
bosMstMapVlanIndex = _BosMstMapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28, 1, 2),
    _BosMstMapVlanIndex_Type()
)
bosMstMapVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstMapVlanIndex.setStatus("current")
_BosMstUnMapVlanIndex_Type = VlanId
_BosMstUnMapVlanIndex_Object = MibTableColumn
bosMstUnMapVlanIndex = _BosMstUnMapVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28, 1, 3),
    _BosMstUnMapVlanIndex_Type()
)
bosMstUnMapVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstUnMapVlanIndex.setStatus("current")


class _BosMstSetVlanList_Type(OctetString):
    """Custom type bosMstSetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_BosMstSetVlanList_Type.__name__ = "OctetString"
_BosMstSetVlanList_Object = MibTableColumn
bosMstSetVlanList = _BosMstSetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28, 1, 4),
    _BosMstSetVlanList_Type()
)
bosMstSetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstSetVlanList.setStatus("current")


class _BosMstResetVlanList_Type(OctetString):
    """Custom type bosMstResetVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_BosMstResetVlanList_Type.__name__ = "OctetString"
_BosMstResetVlanList_Object = MibTableColumn
bosMstResetVlanList = _BosMstResetVlanList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28, 1, 5),
    _BosMstResetVlanList_Type()
)
bosMstResetVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstResetVlanList.setStatus("current")


class _BosMstInstanceVlanMapped_Type(OctetString):
    """Custom type bosMstInstanceVlanMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BosMstInstanceVlanMapped_Type.__name__ = "OctetString"
_BosMstInstanceVlanMapped_Object = MibTableColumn
bosMstInstanceVlanMapped = _BosMstInstanceVlanMapped_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28, 1, 6),
    _BosMstInstanceVlanMapped_Type()
)
bosMstInstanceVlanMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstInstanceVlanMapped.setStatus("current")


class _BosMstInstanceVlanMapped2k_Type(OctetString):
    """Custom type bosMstInstanceVlanMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BosMstInstanceVlanMapped2k_Type.__name__ = "OctetString"
_BosMstInstanceVlanMapped2k_Object = MibTableColumn
bosMstInstanceVlanMapped2k = _BosMstInstanceVlanMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28, 1, 7),
    _BosMstInstanceVlanMapped2k_Type()
)
bosMstInstanceVlanMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstInstanceVlanMapped2k.setStatus("current")


class _BosMstInstanceVlanMapped3k_Type(OctetString):
    """Custom type bosMstInstanceVlanMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BosMstInstanceVlanMapped3k_Type.__name__ = "OctetString"
_BosMstInstanceVlanMapped3k_Object = MibTableColumn
bosMstInstanceVlanMapped3k = _BosMstInstanceVlanMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28, 1, 8),
    _BosMstInstanceVlanMapped3k_Type()
)
bosMstInstanceVlanMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstInstanceVlanMapped3k.setStatus("current")


class _BosMstInstanceVlanMapped4k_Type(OctetString):
    """Custom type bosMstInstanceVlanMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BosMstInstanceVlanMapped4k_Type.__name__ = "OctetString"
_BosMstInstanceVlanMapped4k_Object = MibTableColumn
bosMstInstanceVlanMapped4k = _BosMstInstanceVlanMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 28, 1, 9),
    _BosMstInstanceVlanMapped4k_Type()
)
bosMstInstanceVlanMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstInstanceVlanMapped4k.setStatus("current")
_BosMstCistPortTable_Object = MibTable
bosMstCistPortTable = _BosMstCistPortTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29)
)
if mibBuilder.loadTexts:
    bosMstCistPortTable.setStatus("current")
_BosMstCistPortEntry_Object = MibTableRow
bosMstCistPortEntry = _BosMstCistPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1)
)
bosMstCistPortEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosMstCistPort"),
)
if mibBuilder.loadTexts:
    bosMstCistPortEntry.setStatus("current")


class _BosMstCistPort_Type(Integer32):
    """Custom type bosMstCistPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BosMstCistPort_Type.__name__ = "Integer32"
_BosMstCistPort_Object = MibTableColumn
bosMstCistPort = _BosMstCistPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 1),
    _BosMstCistPort_Type()
)
bosMstCistPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosMstCistPort.setStatus("current")


class _BosMstCistPortPathCost_Type(Integer32):
    """Custom type bosMstCistPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_BosMstCistPortPathCost_Type.__name__ = "Integer32"
_BosMstCistPortPathCost_Object = MibTableColumn
bosMstCistPortPathCost = _BosMstCistPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 2),
    _BosMstCistPortPathCost_Type()
)
bosMstCistPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistPortPathCost.setStatus("current")


class _BosMstCistPortPriority_Type(Integer32):
    """Custom type bosMstCistPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_BosMstCistPortPriority_Type.__name__ = "Integer32"
_BosMstCistPortPriority_Object = MibTableColumn
bosMstCistPortPriority = _BosMstCistPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 3),
    _BosMstCistPortPriority_Type()
)
bosMstCistPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistPortPriority.setStatus("current")
_BosMstCistPortDesignatedRoot_Type = BridgeId
_BosMstCistPortDesignatedRoot_Object = MibTableColumn
bosMstCistPortDesignatedRoot = _BosMstCistPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 4),
    _BosMstCistPortDesignatedRoot_Type()
)
bosMstCistPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistPortDesignatedRoot.setStatus("current")
_BosMstCistPortDesignatedBridge_Type = BridgeId
_BosMstCistPortDesignatedBridge_Object = MibTableColumn
bosMstCistPortDesignatedBridge = _BosMstCistPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 5),
    _BosMstCistPortDesignatedBridge_Type()
)
bosMstCistPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistPortDesignatedBridge.setStatus("current")


class _BosMstCistPortDesignatedPort_Type(OctetString):
    """Custom type bosMstCistPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_BosMstCistPortDesignatedPort_Type.__name__ = "OctetString"
_BosMstCistPortDesignatedPort_Object = MibTableColumn
bosMstCistPortDesignatedPort = _BosMstCistPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 6),
    _BosMstCistPortDesignatedPort_Type()
)
bosMstCistPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistPortDesignatedPort.setStatus("current")


class _BosMstCistPortAdminP2P_Type(Integer32):
    """Custom type bosMstCistPortAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_BosMstCistPortAdminP2P_Type.__name__ = "Integer32"
_BosMstCistPortAdminP2P_Object = MibTableColumn
bosMstCistPortAdminP2P = _BosMstCistPortAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 7),
    _BosMstCistPortAdminP2P_Type()
)
bosMstCistPortAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistPortAdminP2P.setStatus("current")
_BosMstCistPortOperP2P_Type = TruthValue
_BosMstCistPortOperP2P_Object = MibTableColumn
bosMstCistPortOperP2P = _BosMstCistPortOperP2P_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 8),
    _BosMstCistPortOperP2P_Type()
)
bosMstCistPortOperP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistPortOperP2P.setStatus("current")
_BosMstCistPortAdminEdgeStatus_Type = TruthValue
_BosMstCistPortAdminEdgeStatus_Object = MibTableColumn
bosMstCistPortAdminEdgeStatus = _BosMstCistPortAdminEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 9),
    _BosMstCistPortAdminEdgeStatus_Type()
)
bosMstCistPortAdminEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistPortAdminEdgeStatus.setStatus("current")
_BosMstCistPortOperEdgeStatus_Type = TruthValue
_BosMstCistPortOperEdgeStatus_Object = MibTableColumn
bosMstCistPortOperEdgeStatus = _BosMstCistPortOperEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 10),
    _BosMstCistPortOperEdgeStatus_Type()
)
bosMstCistPortOperEdgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistPortOperEdgeStatus.setStatus("current")
_BosMstCistPortProtocolMigration_Type = TruthValue
_BosMstCistPortProtocolMigration_Object = MibTableColumn
bosMstCistPortProtocolMigration = _BosMstCistPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 11),
    _BosMstCistPortProtocolMigration_Type()
)
bosMstCistPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistPortProtocolMigration.setStatus("current")


class _BosMstCistPortState_Type(Integer32):
    """Custom type bosMstCistPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("learning", 4),
          ("forwarding", 5))
    )


_BosMstCistPortState_Type.__name__ = "Integer32"
_BosMstCistPortState_Object = MibTableColumn
bosMstCistPortState = _BosMstCistPortState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 12),
    _BosMstCistPortState_Type()
)
bosMstCistPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistPortState.setStatus("current")


class _BosMstCistForcePortState_Type(Integer32):
    """Custom type bosMstCistForcePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BosMstCistForcePortState_Type.__name__ = "Integer32"
_BosMstCistForcePortState_Object = MibTableColumn
bosMstCistForcePortState = _BosMstCistForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 13),
    _BosMstCistForcePortState_Type()
)
bosMstCistForcePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistForcePortState.setStatus("current")
_BosMstCistPortDesignatedCost_Type = Integer32
_BosMstCistPortDesignatedCost_Object = MibTableColumn
bosMstCistPortDesignatedCost = _BosMstCistPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 14),
    _BosMstCistPortDesignatedCost_Type()
)
bosMstCistPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistPortDesignatedCost.setStatus("current")
_BosMstCistPortRegionalRoot_Type = BridgeId
_BosMstCistPortRegionalRoot_Object = MibTableColumn
bosMstCistPortRegionalRoot = _BosMstCistPortRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 15),
    _BosMstCistPortRegionalRoot_Type()
)
bosMstCistPortRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistPortRegionalRoot.setStatus("current")
_BosMstCistPortRegionalPathCost_Type = Integer32
_BosMstCistPortRegionalPathCost_Object = MibTableColumn
bosMstCistPortRegionalPathCost = _BosMstCistPortRegionalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 16),
    _BosMstCistPortRegionalPathCost_Type()
)
bosMstCistPortRegionalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistPortRegionalPathCost.setStatus("current")


class _BosMstCistCurrentPortRole_Type(Integer32):
    """Custom type bosMstCistCurrentPortRole based on Integer32"""
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
        *(("disabled", 0),
          ("alternate", 1),
          ("backup", 2),
          ("root", 3),
          ("designated", 4))
    )


_BosMstCistCurrentPortRole_Type.__name__ = "Integer32"
_BosMstCistCurrentPortRole_Object = MibTableColumn
bosMstCistCurrentPortRole = _BosMstCistCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 17),
    _BosMstCistCurrentPortRole_Type()
)
bosMstCistCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstCistCurrentPortRole.setStatus("current")


class _BosMstCistPortHelloTime_Type(Timeout):
    """Custom type bosMstCistPortHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BosMstCistPortHelloTime_Type.__name__ = "Timeout"
_BosMstCistPortHelloTime_Object = MibTableColumn
bosMstCistPortHelloTime = _BosMstCistPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 18),
    _BosMstCistPortHelloTime_Type()
)
bosMstCistPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistPortHelloTime.setStatus("current")
_BosMstCistPortAutoEdgeStatus_Type = TruthValue
_BosMstCistPortAutoEdgeStatus_Object = MibTableColumn
bosMstCistPortAutoEdgeStatus = _BosMstCistPortAutoEdgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 19),
    _BosMstCistPortAutoEdgeStatus_Type()
)
bosMstCistPortAutoEdgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistPortAutoEdgeStatus.setStatus("current")
_BosMstCistPortPvstProtectionStatus_Type = TruthValue
_BosMstCistPortPvstProtectionStatus_Object = MibTableColumn
bosMstCistPortPvstProtectionStatus = _BosMstCistPortPvstProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 29, 1, 20),
    _BosMstCistPortPvstProtectionStatus_Type()
)
bosMstCistPortPvstProtectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistPortPvstProtectionStatus.setStatus("current")
_BosMstMstiPortTable_Object = MibTable
bosMstMstiPortTable = _BosMstMstiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30)
)
if mibBuilder.loadTexts:
    bosMstMstiPortTable.setStatus("current")
_BosMstMstiPortEntry_Object = MibTableRow
bosMstMstiPortEntry = _BosMstMstiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1)
)
bosMstMstiPortEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosMstMstiPort"),
    (0, "BLADEOS-BASE-MIB", "bosMstInstanceIndex"),
)
if mibBuilder.loadTexts:
    bosMstMstiPortEntry.setStatus("current")


class _BosMstMstiPort_Type(Integer32):
    """Custom type bosMstMstiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BosMstMstiPort_Type.__name__ = "Integer32"
_BosMstMstiPort_Object = MibTableColumn
bosMstMstiPort = _BosMstMstiPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1, 1),
    _BosMstMstiPort_Type()
)
bosMstMstiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosMstMstiPort.setStatus("current")


class _BosMstMstiPortPathCost_Type(Integer32):
    """Custom type bosMstMstiPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_BosMstMstiPortPathCost_Type.__name__ = "Integer32"
_BosMstMstiPortPathCost_Object = MibTableColumn
bosMstMstiPortPathCost = _BosMstMstiPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1, 2),
    _BosMstMstiPortPathCost_Type()
)
bosMstMstiPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstMstiPortPathCost.setStatus("current")


class _BosMstMstiPortPriority_Type(Integer32):
    """Custom type bosMstMstiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_BosMstMstiPortPriority_Type.__name__ = "Integer32"
_BosMstMstiPortPriority_Object = MibTableColumn
bosMstMstiPortPriority = _BosMstMstiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1, 3),
    _BosMstMstiPortPriority_Type()
)
bosMstMstiPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstMstiPortPriority.setStatus("current")
_BosMstMstiPortDesignatedRoot_Type = BridgeId
_BosMstMstiPortDesignatedRoot_Object = MibTableColumn
bosMstMstiPortDesignatedRoot = _BosMstMstiPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1, 4),
    _BosMstMstiPortDesignatedRoot_Type()
)
bosMstMstiPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiPortDesignatedRoot.setStatus("current")
_BosMstMstiPortDesignatedBridge_Type = BridgeId
_BosMstMstiPortDesignatedBridge_Object = MibTableColumn
bosMstMstiPortDesignatedBridge = _BosMstMstiPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1, 5),
    _BosMstMstiPortDesignatedBridge_Type()
)
bosMstMstiPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiPortDesignatedBridge.setStatus("current")


class _BosMstMstiPortDesignatedPort_Type(OctetString):
    """Custom type bosMstMstiPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_BosMstMstiPortDesignatedPort_Type.__name__ = "OctetString"
_BosMstMstiPortDesignatedPort_Object = MibTableColumn
bosMstMstiPortDesignatedPort = _BosMstMstiPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1, 6),
    _BosMstMstiPortDesignatedPort_Type()
)
bosMstMstiPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiPortDesignatedPort.setStatus("current")


class _BosMstMstiPortState_Type(Integer32):
    """Custom type bosMstMstiPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("learning", 4),
          ("forwarding", 5))
    )


_BosMstMstiPortState_Type.__name__ = "Integer32"
_BosMstMstiPortState_Object = MibTableColumn
bosMstMstiPortState = _BosMstMstiPortState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1, 7),
    _BosMstMstiPortState_Type()
)
bosMstMstiPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiPortState.setStatus("current")


class _BosMstMstiForcePortState_Type(Integer32):
    """Custom type bosMstMstiForcePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BosMstMstiForcePortState_Type.__name__ = "Integer32"
_BosMstMstiForcePortState_Object = MibTableColumn
bosMstMstiForcePortState = _BosMstMstiForcePortState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1, 8),
    _BosMstMstiForcePortState_Type()
)
bosMstMstiForcePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstMstiForcePortState.setStatus("current")
_BosMstMstiPortDesignatedCost_Type = Integer32
_BosMstMstiPortDesignatedCost_Object = MibTableColumn
bosMstMstiPortDesignatedCost = _BosMstMstiPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1, 9),
    _BosMstMstiPortDesignatedCost_Type()
)
bosMstMstiPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiPortDesignatedCost.setStatus("current")


class _BosMstMstiCurrentPortRole_Type(Integer32):
    """Custom type bosMstMstiCurrentPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("alternate", 1),
          ("backup", 2),
          ("root", 3),
          ("designated", 4),
          ("master", 5))
    )


_BosMstMstiCurrentPortRole_Type.__name__ = "Integer32"
_BosMstMstiCurrentPortRole_Object = MibTableColumn
bosMstMstiCurrentPortRole = _BosMstMstiCurrentPortRole_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 30, 1, 10),
    _BosMstMstiCurrentPortRole_Type()
)
bosMstMstiCurrentPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiCurrentPortRole.setStatus("current")


class _BosMstCistDynamicPathcostCalculation_Type(TruthValue):
    """Custom type bosMstCistDynamicPathcostCalculation based on TruthValue"""
    defaultValue = 2


_BosMstCistDynamicPathcostCalculation_Type.__name__ = "TruthValue"
_BosMstCistDynamicPathcostCalculation_Object = MibScalar
bosMstCistDynamicPathcostCalculation = _BosMstCistDynamicPathcostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 1, 31),
    _BosMstCistDynamicPathcostCalculation_Type()
)
bosMstCistDynamicPathcostCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistDynamicPathcostCalculation.setStatus("current")
_Dot1sBosMstTrapsControl_ObjectIdentity = ObjectIdentity
dot1sBosMstTrapsControl = _Dot1sBosMstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2)
)


class _BosMstSetTraps_Type(Integer32):
    """Custom type bosMstSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosMstSetTraps_Type.__name__ = "Integer32"
_BosMstSetTraps_Object = MibScalar
bosMstSetTraps = _BosMstSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 1),
    _BosMstSetTraps_Type()
)
bosMstSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstSetTraps.setStatus("current")


class _BosMstGenTrapType_Type(Integer32):
    """Custom type bosMstGenTrapType based on Integer32"""
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
          ("up", 1),
          ("down", 2))
    )


_BosMstGenTrapType_Type.__name__ = "Integer32"
_BosMstGenTrapType_Object = MibScalar
bosMstGenTrapType = _BosMstGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 2),
    _BosMstGenTrapType_Type()
)
bosMstGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstGenTrapType.setStatus("current")


class _BosMstErrTrapType_Type(Integer32):
    """Custom type bosMstErrTrapType based on Integer32"""
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
          ("memfail", 1),
          ("bufffail", 2))
    )


_BosMstErrTrapType_Type.__name__ = "Integer32"
_BosMstErrTrapType_Object = MibScalar
bosMstErrTrapType = _BosMstErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 3),
    _BosMstErrTrapType_Type()
)
bosMstErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstErrTrapType.setStatus("current")
_BosMstPortTrapNotificationTable_Object = MibTable
bosMstPortTrapNotificationTable = _BosMstPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 4)
)
if mibBuilder.loadTexts:
    bosMstPortTrapNotificationTable.setStatus("current")
_BosMstPortTrapNotificationEntry_Object = MibTableRow
bosMstPortTrapNotificationEntry = _BosMstPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 4, 1)
)
bosMstPortTrapNotificationEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosMstPortTrapIndex"),
)
if mibBuilder.loadTexts:
    bosMstPortTrapNotificationEntry.setStatus("current")


class _BosMstPortTrapIndex_Type(Integer32):
    """Custom type bosMstPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_BosMstPortTrapIndex_Type.__name__ = "Integer32"
_BosMstPortTrapIndex_Object = MibTableColumn
bosMstPortTrapIndex = _BosMstPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 4, 1, 1),
    _BosMstPortTrapIndex_Type()
)
bosMstPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosMstPortTrapIndex.setStatus("current")


class _BosMstPortMigrationType_Type(Integer32):
    """Custom type bosMstPortMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendstp", 0),
          ("sendrstp", 1))
    )


_BosMstPortMigrationType_Type.__name__ = "Integer32"
_BosMstPortMigrationType_Object = MibTableColumn
bosMstPortMigrationType = _BosMstPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 4, 1, 2),
    _BosMstPortMigrationType_Type()
)
bosMstPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstPortMigrationType.setStatus("current")


class _BosMstPktErrType_Type(Integer32):
    """Custom type bosMstPktErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("protocolIdErr", 0),
          ("invalidBpdu", 1),
          ("configLengthErr", 2),
          ("tcnLengthErr", 3),
          ("rstpLengthErr", 4),
          ("maxAgeErr", 5),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7),
          ("mstpLengthErr", 8))
    )


_BosMstPktErrType_Type.__name__ = "Integer32"
_BosMstPktErrType_Object = MibTableColumn
bosMstPktErrType = _BosMstPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 4, 1, 3),
    _BosMstPktErrType_Type()
)
bosMstPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstPktErrType.setStatus("current")
_BosMstPktErrVal_Type = Integer32
_BosMstPktErrVal_Object = MibTableColumn
bosMstPktErrVal = _BosMstPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 4, 1, 4),
    _BosMstPktErrVal_Type()
)
bosMstPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstPktErrVal.setStatus("current")
_BosMstPortRoleTrapNotificationTable_Object = MibTable
bosMstPortRoleTrapNotificationTable = _BosMstPortRoleTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 5)
)
if mibBuilder.loadTexts:
    bosMstPortRoleTrapNotificationTable.setStatus("current")
_BosMstPortRoleTrapNotificationEntry_Object = MibTableRow
bosMstPortRoleTrapNotificationEntry = _BosMstPortRoleTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 5, 1)
)
bosMstPortRoleTrapNotificationEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosMstPortTrapIndex"),
    (0, "BLADEOS-BASE-MIB", "bosMstMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    bosMstPortRoleTrapNotificationEntry.setStatus("current")


class _BosMstPortRoleType_Type(Integer32):
    """Custom type bosMstPortRoleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4),
          ("masterport", 5))
    )


_BosMstPortRoleType_Type.__name__ = "Integer32"
_BosMstPortRoleType_Object = MibTableColumn
bosMstPortRoleType = _BosMstPortRoleType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 5, 1, 1),
    _BosMstPortRoleType_Type()
)
bosMstPortRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstPortRoleType.setStatus("current")


class _BosMstOldRoleType_Type(Integer32):
    """Custom type bosMstOldRoleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4),
          ("masterport", 5))
    )


_BosMstOldRoleType_Type.__name__ = "Integer32"
_BosMstOldRoleType_Object = MibTableColumn
bosMstOldRoleType = _BosMstOldRoleType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 2, 5, 1, 2),
    _BosMstOldRoleType_Type()
)
bosMstOldRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstOldRoleType.setStatus("current")
_Dot1sBosMstTraps_ObjectIdentity = ObjectIdentity
dot1sBosMstTraps = _Dot1sBosMstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 3)
)
_BosMstTraps_ObjectIdentity = ObjectIdentity
bosMstTraps = _BosMstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 3, 0)
)
_Bos_ObjectIdentity = ObjectIdentity
bos = _Bos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81)
)
_BosSystem_ObjectIdentity = ObjectIdentity
bosSystem = _BosSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1)
)


class _BosHardwareVersion_Type(DisplayString):
    """Custom type bosHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_BosHardwareVersion_Type.__name__ = "DisplayString"
_BosHardwareVersion_Object = MibScalar
bosHardwareVersion = _BosHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 2),
    _BosHardwareVersion_Type()
)
bosHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosHardwareVersion.setStatus("current")


class _BosConfigSaveStatus_Type(Integer32):
    """Custom type bosConfigSaveStatus based on Integer32"""
    defaultValue = 4

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
        *(("saveInProgress", 1),
          ("saveSuccessful", 2),
          ("saveFailed", 3),
          ("notInitiated", 4),
          ("saveNotRequired", 5))
    )


_BosConfigSaveStatus_Type.__name__ = "Integer32"
_BosConfigSaveStatus_Object = MibScalar
bosConfigSaveStatus = _BosConfigSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 14),
    _BosConfigSaveStatus_Type()
)
bosConfigSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosConfigSaveStatus.setStatus("current")


class _BosLoginAuthentication_Type(Integer32):
    """Custom type bosLoginAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remoteRadius", 2),
          ("remoteTacacs", 3))
    )


_BosLoginAuthentication_Type.__name__ = "Integer32"
_BosLoginAuthentication_Object = MibScalar
bosLoginAuthentication = _BosLoginAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 32),
    _BosLoginAuthentication_Type()
)
bosLoginAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosLoginAuthentication.setStatus("current")


class _BosSwitchDate_Type(DisplayString):
    """Custom type bosSwitchDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixed_length = 40


_BosSwitchDate_Type.__name__ = "DisplayString"
_BosSwitchDate_Object = MibScalar
bosSwitchDate = _BosSwitchDate_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 35),
    _BosSwitchDate_Type()
)
bosSwitchDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSwitchDate.setStatus("current")


class _BosHttpStatus_Type(Integer32):
    """Custom type bosHttpStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosHttpStatus_Type.__name__ = "Integer32"
_BosHttpStatus_Object = MibScalar
bosHttpStatus = _BosHttpStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 39),
    _BosHttpStatus_Type()
)
bosHttpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosHttpStatus.setStatus("current")


class _BosConfigRestoreFileVersion_Type(DisplayString):
    """Custom type bosConfigRestoreFileVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_BosConfigRestoreFileVersion_Type.__name__ = "DisplayString"
_BosConfigRestoreFileVersion_Object = MibScalar
bosConfigRestoreFileVersion = _BosConfigRestoreFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 40),
    _BosConfigRestoreFileVersion_Type()
)
bosConfigRestoreFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosConfigRestoreFileVersion.setStatus("current")


class _BosTelnetStatus_Type(Integer32):
    """Custom type bosTelnetStatus based on Integer32"""
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
        *(("enable", 1),
          ("disable", 2),
          ("enableInProgress", 3),
          ("disableInProgress", 4))
    )


_BosTelnetStatus_Type.__name__ = "Integer32"
_BosTelnetStatus_Object = MibScalar
bosTelnetStatus = _BosTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 46),
    _BosTelnetStatus_Type()
)
bosTelnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosTelnetStatus.setStatus("current")
_BosTimeZone_Type = Integer32
_BosTimeZone_Object = MibScalar
bosTimeZone = _BosTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 47),
    _BosTimeZone_Type()
)
bosTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosTimeZone.setStatus("current")


class _BosDayLightSaving_Type(Integer32):
    """Custom type bosDayLightSaving based on Integer32"""
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


_BosDayLightSaving_Type.__name__ = "Integer32"
_BosDayLightSaving_Object = MibScalar
bosDayLightSaving = _BosDayLightSaving_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 48),
    _BosDayLightSaving_Type()
)
bosDayLightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosDayLightSaving.setStatus("current")


class _BosLastBootTime_Type(DisplayString):
    """Custom type bosLastBootTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixed_length = 40


_BosLastBootTime_Type.__name__ = "DisplayString"
_BosLastBootTime_Object = MibScalar
bosLastBootTime = _BosLastBootTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 49),
    _BosLastBootTime_Type()
)
bosLastBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosLastBootTime.setStatus("current")
_BosAllocCount_Type = Unsigned32
_BosAllocCount_Object = MibScalar
bosAllocCount = _BosAllocCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 50),
    _BosAllocCount_Type()
)
bosAllocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosAllocCount.setStatus("current")
_BosReleaseCount_Type = Unsigned32
_BosReleaseCount_Object = MibScalar
bosReleaseCount = _BosReleaseCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 51),
    _BosReleaseCount_Type()
)
bosReleaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosReleaseCount.setStatus("current")
_BosAllocFailCount_Type = Unsigned32
_BosAllocFailCount_Object = MibScalar
bosAllocFailCount = _BosAllocFailCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 52),
    _BosAllocFailCount_Type()
)
bosAllocFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosAllocFailCount.setStatus("current")
_BosPeakUsageCount_Type = Unsigned32
_BosPeakUsageCount_Object = MibScalar
bosPeakUsageCount = _BosPeakUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 1, 53),
    _BosPeakUsageCount_Type()
)
bosPeakUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPeakUsageCount.setStatus("current")
_BosConfigControl_ObjectIdentity = ObjectIdentity
bosConfigControl = _BosConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2)
)
_BosConfigCtrlTable_Object = MibTable
bosConfigCtrlTable = _BosConfigCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 1)
)
if mibBuilder.loadTexts:
    bosConfigCtrlTable.setStatus("current")
_BosConfigCtrlEntry_Object = MibTableRow
bosConfigCtrlEntry = _BosConfigCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 1, 1)
)
bosConfigCtrlEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosConfigCtrlIndex"),
)
if mibBuilder.loadTexts:
    bosConfigCtrlEntry.setStatus("current")


class _BosConfigCtrlIndex_Type(Integer32):
    """Custom type bosConfigCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BosConfigCtrlIndex_Type.__name__ = "Integer32"
_BosConfigCtrlIndex_Object = MibTableColumn
bosConfigCtrlIndex = _BosConfigCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 1, 1, 1),
    _BosConfigCtrlIndex_Type()
)
bosConfigCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosConfigCtrlIndex.setStatus("current")


class _BosConfigCtrlEgressStatus_Type(Integer32):
    """Custom type bosConfigCtrlEgressStatus based on Integer32"""
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


_BosConfigCtrlEgressStatus_Type.__name__ = "Integer32"
_BosConfigCtrlEgressStatus_Object = MibTableColumn
bosConfigCtrlEgressStatus = _BosConfigCtrlEgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 1, 1, 2),
    _BosConfigCtrlEgressStatus_Type()
)
bosConfigCtrlEgressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosConfigCtrlEgressStatus.setStatus("current")


class _BosConfigCtrlStatsCollection_Type(Integer32):
    """Custom type bosConfigCtrlStatsCollection based on Integer32"""
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


_BosConfigCtrlStatsCollection_Type.__name__ = "Integer32"
_BosConfigCtrlStatsCollection_Object = MibTableColumn
bosConfigCtrlStatsCollection = _BosConfigCtrlStatsCollection_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 1, 1, 3),
    _BosConfigCtrlStatsCollection_Type()
)
bosConfigCtrlStatsCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosConfigCtrlStatsCollection.setStatus("current")


class _BosConfigCtrlStatus_Type(Integer32):
    """Custom type bosConfigCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_BosConfigCtrlStatus_Type.__name__ = "Integer32"
_BosConfigCtrlStatus_Object = MibTableColumn
bosConfigCtrlStatus = _BosConfigCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 1, 1, 4),
    _BosConfigCtrlStatus_Type()
)
bosConfigCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosConfigCtrlStatus.setStatus("current")
_BosPortCtrlTable_Object = MibTable
bosPortCtrlTable = _BosPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 2)
)
if mibBuilder.loadTexts:
    bosPortCtrlTable.setStatus("current")
_BosPortCtrlEntry_Object = MibTableRow
bosPortCtrlEntry = _BosPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 2, 1)
)
bosPortCtrlEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPortCtrlIndex"),
)
if mibBuilder.loadTexts:
    bosPortCtrlEntry.setStatus("current")


class _BosPortCtrlIndex_Type(Integer32):
    """Custom type bosPortCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BosPortCtrlIndex_Type.__name__ = "Integer32"
_BosPortCtrlIndex_Object = MibTableColumn
bosPortCtrlIndex = _BosPortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 2, 1, 1),
    _BosPortCtrlIndex_Type()
)
bosPortCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosPortCtrlIndex.setStatus("current")


class _BosPortCtrlMode_Type(Integer32):
    """Custom type bosPortCtrlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("noNegotiation", 2))
    )


_BosPortCtrlMode_Type.__name__ = "Integer32"
_BosPortCtrlMode_Object = MibTableColumn
bosPortCtrlMode = _BosPortCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 2, 1, 2),
    _BosPortCtrlMode_Type()
)
bosPortCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPortCtrlMode.setStatus("current")


class _BosPortCtrlDuplex_Type(Integer32):
    """Custom type bosPortCtrlDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("any", 3))
    )


_BosPortCtrlDuplex_Type.__name__ = "Integer32"
_BosPortCtrlDuplex_Object = MibTableColumn
bosPortCtrlDuplex = _BosPortCtrlDuplex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 2, 1, 3),
    _BosPortCtrlDuplex_Type()
)
bosPortCtrlDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPortCtrlDuplex.setStatus("current")


class _BosPortCtrlSpeed_Type(Integer32):
    """Custom type bosPortCtrlSpeed based on Integer32"""
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
        *(("tenMBPS", 1),
          ("hundredMBPS", 2),
          ("oneGB", 3),
          ("tenGB", 4),
          ("any", 5))
    )


_BosPortCtrlSpeed_Type.__name__ = "Integer32"
_BosPortCtrlSpeed_Object = MibTableColumn
bosPortCtrlSpeed = _BosPortCtrlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 2, 1, 4),
    _BosPortCtrlSpeed_Type()
)
bosPortCtrlSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPortCtrlSpeed.setStatus("current")


class _BosPortCtrlOperDuplex_Type(Integer32):
    """Custom type bosPortCtrlOperDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_BosPortCtrlOperDuplex_Type.__name__ = "Integer32"
_BosPortCtrlOperDuplex_Object = MibTableColumn
bosPortCtrlOperDuplex = _BosPortCtrlOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 2, 1, 5),
    _BosPortCtrlOperDuplex_Type()
)
bosPortCtrlOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPortCtrlOperDuplex.setStatus("current")


class _BosPortCtrlOperSpeed_Type(Integer32):
    """Custom type bosPortCtrlOperSpeed based on Integer32"""
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
        *(("tenMBPS", 1),
          ("hundredMBPS", 2),
          ("oneGB", 3),
          ("tenGB", 4))
    )


_BosPortCtrlOperSpeed_Type.__name__ = "Integer32"
_BosPortCtrlOperSpeed_Object = MibTableColumn
bosPortCtrlOperSpeed = _BosPortCtrlOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 2, 2, 1, 6),
    _BosPortCtrlOperSpeed_Type()
)
bosPortCtrlOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPortCtrlOperSpeed.setStatus("current")
_Bosext_ObjectIdentity = ObjectIdentity
bosext = _Bosext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8)
)
_BosRateControl_ObjectIdentity = ObjectIdentity
bosRateControl = _BosRateControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 4)
)
_BosRateCtrlTable_Object = MibTable
bosRateCtrlTable = _BosRateCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 4, 1)
)
if mibBuilder.loadTexts:
    bosRateCtrlTable.setStatus("current")
_BosRateCtrlEntry_Object = MibTableRow
bosRateCtrlEntry = _BosRateCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 4, 1, 1)
)
bosRateCtrlEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosRateCtrlIndex"),
)
if mibBuilder.loadTexts:
    bosRateCtrlEntry.setStatus("current")


class _BosRateCtrlIndex_Type(Integer32):
    """Custom type bosRateCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BosRateCtrlIndex_Type.__name__ = "Integer32"
_BosRateCtrlIndex_Object = MibTableColumn
bosRateCtrlIndex = _BosRateCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 4, 1, 1, 1),
    _BosRateCtrlIndex_Type()
)
bosRateCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosRateCtrlIndex.setStatus("current")


class _BosRateCtrlDLFLimitValue_Type(Integer32):
    """Custom type bosRateCtrlDLFLimitValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosRateCtrlDLFLimitValue_Type.__name__ = "Integer32"
_BosRateCtrlDLFLimitValue_Object = MibTableColumn
bosRateCtrlDLFLimitValue = _BosRateCtrlDLFLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 4, 1, 1, 2),
    _BosRateCtrlDLFLimitValue_Type()
)
bosRateCtrlDLFLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRateCtrlDLFLimitValue.setStatus("current")


class _BosRateCtrlBCASTLimitValue_Type(Integer32):
    """Custom type bosRateCtrlBCASTLimitValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosRateCtrlBCASTLimitValue_Type.__name__ = "Integer32"
_BosRateCtrlBCASTLimitValue_Object = MibTableColumn
bosRateCtrlBCASTLimitValue = _BosRateCtrlBCASTLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 4, 1, 1, 3),
    _BosRateCtrlBCASTLimitValue_Type()
)
bosRateCtrlBCASTLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRateCtrlBCASTLimitValue.setStatus("current")


class _BosRateCtrlMCASTLimitValue_Type(Integer32):
    """Custom type bosRateCtrlMCASTLimitValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosRateCtrlMCASTLimitValue_Type.__name__ = "Integer32"
_BosRateCtrlMCASTLimitValue_Object = MibTableColumn
bosRateCtrlMCASTLimitValue = _BosRateCtrlMCASTLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 4, 1, 1, 4),
    _BosRateCtrlMCASTLimitValue_Type()
)
bosRateCtrlMCASTLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRateCtrlMCASTLimitValue.setStatus("current")
_BosMacAcl_ObjectIdentity = ObjectIdentity
bosMacAcl = _BosMacAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5)
)
_BosMacAclTable_Object = MibTable
bosMacAclTable = _BosMacAclTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1)
)
if mibBuilder.loadTexts:
    bosMacAclTable.setStatus("current")
_BosMacAclEntry_Object = MibTableRow
bosMacAclEntry = _BosMacAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1)
)
bosMacAclEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosMacAclNo"),
)
if mibBuilder.loadTexts:
    bosMacAclEntry.setStatus("current")


class _BosMacAclNo_Type(Integer32):
    """Custom type bosMacAclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BosMacAclNo_Type.__name__ = "Integer32"
_BosMacAclNo_Object = MibTableColumn
bosMacAclNo = _BosMacAclNo_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 1),
    _BosMacAclNo_Type()
)
bosMacAclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosMacAclNo.setStatus("current")


class _BosMacAclProtocolType_Type(Unsigned32):
    """Custom type bosMacAclProtocolType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BosMacAclProtocolType_Type.__name__ = "Unsigned32"
_BosMacAclProtocolType_Object = MibTableColumn
bosMacAclProtocolType = _BosMacAclProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 2),
    _BosMacAclProtocolType_Type()
)
bosMacAclProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMacAclProtocolType.setStatus("current")
_BosMacAclDstMacAddr_Type = MacAddress
_BosMacAclDstMacAddr_Object = MibTableColumn
bosMacAclDstMacAddr = _BosMacAclDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 3),
    _BosMacAclDstMacAddr_Type()
)
bosMacAclDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMacAclDstMacAddr.setStatus("current")
_BosMacAclSrcMacAddr_Type = MacAddress
_BosMacAclSrcMacAddr_Object = MibTableColumn
bosMacAclSrcMacAddr = _BosMacAclSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 4),
    _BosMacAclSrcMacAddr_Type()
)
bosMacAclSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMacAclSrcMacAddr.setStatus("current")


class _BosMacAclVlanId_Type(Integer32):
    """Custom type bosMacAclVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_BosMacAclVlanId_Type.__name__ = "Integer32"
_BosMacAclVlanId_Object = MibTableColumn
bosMacAclVlanId = _BosMacAclVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 5),
    _BosMacAclVlanId_Type()
)
bosMacAclVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMacAclVlanId.setStatus("current")
_BosMacAclInPortList_Type = PortList
_BosMacAclInPortList_Object = MibTableColumn
bosMacAclInPortList = _BosMacAclInPortList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 6),
    _BosMacAclInPortList_Type()
)
bosMacAclInPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMacAclInPortList.setStatus("current")
_BosMacAclOutPortList_Type = PortList
_BosMacAclOutPortList_Object = MibTableColumn
bosMacAclOutPortList = _BosMacAclOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 7),
    _BosMacAclOutPortList_Type()
)
bosMacAclOutPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMacAclOutPortList.setStatus("current")


class _BosMacAclAction_Type(Integer32):
    """Custom type bosMacAclAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_BosMacAclAction_Type.__name__ = "Integer32"
_BosMacAclAction_Object = MibTableColumn
bosMacAclAction = _BosMacAclAction_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 8),
    _BosMacAclAction_Type()
)
bosMacAclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMacAclAction.setStatus("current")
_BosMacAclMatchCount_Type = Counter32
_BosMacAclMatchCount_Object = MibTableColumn
bosMacAclMatchCount = _BosMacAclMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 9),
    _BosMacAclMatchCount_Type()
)
bosMacAclMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMacAclMatchCount.setStatus("current")
_BosMacAclStatsStatus_Type = TruthValue
_BosMacAclStatsStatus_Object = MibTableColumn
bosMacAclStatsStatus = _BosMacAclStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 10),
    _BosMacAclStatsStatus_Type()
)
bosMacAclStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMacAclStatsStatus.setStatus("current")
_BosMacAclStats_Type = Counter32
_BosMacAclStats_Object = MibTableColumn
bosMacAclStats = _BosMacAclStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 11),
    _BosMacAclStats_Type()
)
bosMacAclStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMacAclStats.setStatus("current")


class _BosMacAclClearStats_Type(Integer32):
    """Custom type bosMacAclClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_BosMacAclClearStats_Type.__name__ = "Integer32"
_BosMacAclClearStats_Object = MibTableColumn
bosMacAclClearStats = _BosMacAclClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 12),
    _BosMacAclClearStats_Type()
)
bosMacAclClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMacAclClearStats.setStatus("current")


class _BosMacAclUserPriority_Type(Integer32):
    """Custom type bosMacAclUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BosMacAclUserPriority_Type.__name__ = "Integer32"
_BosMacAclUserPriority_Object = MibTableColumn
bosMacAclUserPriority = _BosMacAclUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 13),
    _BosMacAclUserPriority_Type()
)
bosMacAclUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosMacAclUserPriority.setStatus("current")
_BosMacAclStatus_Type = RowStatus
_BosMacAclStatus_Object = MibTableColumn
bosMacAclStatus = _BosMacAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 5, 1, 1, 14),
    _BosMacAclStatus_Type()
)
bosMacAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosMacAclStatus.setStatus("current")
_BosIpAcl_ObjectIdentity = ObjectIdentity
bosIpAcl = _BosIpAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6)
)
_BosIpAclTable_Object = MibTable
bosIpAclTable = _BosIpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1)
)
if mibBuilder.loadTexts:
    bosIpAclTable.setStatus("current")
_BosIpAclEntry_Object = MibTableRow
bosIpAclEntry = _BosIpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1)
)
bosIpAclEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosIpAclNo"),
)
if mibBuilder.loadTexts:
    bosIpAclEntry.setStatus("current")


class _BosIpAclNo_Type(Integer32):
    """Custom type bosIpAclNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BosIpAclNo_Type.__name__ = "Integer32"
_BosIpAclNo_Object = MibTableColumn
bosIpAclNo = _BosIpAclNo_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 1),
    _BosIpAclNo_Type()
)
bosIpAclNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpAclNo.setStatus("current")


class _BosIpAclProtocol_Type(Integer32):
    """Custom type bosIpAclProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosIpAclProtocol_Type.__name__ = "Integer32"
_BosIpAclProtocol_Object = MibTableColumn
bosIpAclProtocol = _BosIpAclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 2),
    _BosIpAclProtocol_Type()
)
bosIpAclProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclProtocol.setStatus("current")


class _BosIpAclMessageType_Type(Integer32):
    """Custom type bosIpAclMessageType based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BosIpAclMessageType_Type.__name__ = "Integer32"
_BosIpAclMessageType_Object = MibTableColumn
bosIpAclMessageType = _BosIpAclMessageType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 3),
    _BosIpAclMessageType_Type()
)
bosIpAclMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclMessageType.setStatus("current")


class _BosIpAclMessageCode_Type(Integer32):
    """Custom type bosIpAclMessageCode based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BosIpAclMessageCode_Type.__name__ = "Integer32"
_BosIpAclMessageCode_Object = MibTableColumn
bosIpAclMessageCode = _BosIpAclMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 4),
    _BosIpAclMessageCode_Type()
)
bosIpAclMessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclMessageCode.setStatus("current")
_BosIpAclDstIpAddr_Type = IpAddress
_BosIpAclDstIpAddr_Object = MibTableColumn
bosIpAclDstIpAddr = _BosIpAclDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 5),
    _BosIpAclDstIpAddr_Type()
)
bosIpAclDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclDstIpAddr.setStatus("current")
_BosIpAclSrcIpAddr_Type = IpAddress
_BosIpAclSrcIpAddr_Object = MibTableColumn
bosIpAclSrcIpAddr = _BosIpAclSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 6),
    _BosIpAclSrcIpAddr_Type()
)
bosIpAclSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclSrcIpAddr.setStatus("current")


class _BosIpAclDstIpAddrMask_Type(IpAddress):
    """Custom type bosIpAclDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_BosIpAclDstIpAddrMask_Type.__name__ = "IpAddress"
_BosIpAclDstIpAddrMask_Object = MibTableColumn
bosIpAclDstIpAddrMask = _BosIpAclDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 7),
    _BosIpAclDstIpAddrMask_Type()
)
bosIpAclDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclDstIpAddrMask.setStatus("current")


class _BosIpAclSrcIpAddrMask_Type(IpAddress):
    """Custom type bosIpAclSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_BosIpAclSrcIpAddrMask_Type.__name__ = "IpAddress"
_BosIpAclSrcIpAddrMask_Object = MibTableColumn
bosIpAclSrcIpAddrMask = _BosIpAclSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 8),
    _BosIpAclSrcIpAddrMask_Type()
)
bosIpAclSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclSrcIpAddrMask.setStatus("current")


class _BosIpAclMinDstProtPort_Type(Unsigned32):
    """Custom type bosIpAclMinDstProtPort based on Unsigned32"""
    defaultValue = 0


_BosIpAclMinDstProtPort_Type.__name__ = "Unsigned32"
_BosIpAclMinDstProtPort_Object = MibTableColumn
bosIpAclMinDstProtPort = _BosIpAclMinDstProtPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 9),
    _BosIpAclMinDstProtPort_Type()
)
bosIpAclMinDstProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclMinDstProtPort.setStatus("current")


class _BosIpAclMaxDstProtPort_Type(Unsigned32):
    """Custom type bosIpAclMaxDstProtPort based on Unsigned32"""
    defaultValue = 65535


_BosIpAclMaxDstProtPort_Type.__name__ = "Unsigned32"
_BosIpAclMaxDstProtPort_Object = MibTableColumn
bosIpAclMaxDstProtPort = _BosIpAclMaxDstProtPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 10),
    _BosIpAclMaxDstProtPort_Type()
)
bosIpAclMaxDstProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclMaxDstProtPort.setStatus("current")


class _BosIpAclMinSrcProtPort_Type(Unsigned32):
    """Custom type bosIpAclMinSrcProtPort based on Unsigned32"""
    defaultValue = 0


_BosIpAclMinSrcProtPort_Type.__name__ = "Unsigned32"
_BosIpAclMinSrcProtPort_Object = MibTableColumn
bosIpAclMinSrcProtPort = _BosIpAclMinSrcProtPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 11),
    _BosIpAclMinSrcProtPort_Type()
)
bosIpAclMinSrcProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclMinSrcProtPort.setStatus("current")


class _BosIpAclMaxSrcProtPort_Type(Unsigned32):
    """Custom type bosIpAclMaxSrcProtPort based on Unsigned32"""
    defaultValue = 65535


_BosIpAclMaxSrcProtPort_Type.__name__ = "Unsigned32"
_BosIpAclMaxSrcProtPort_Object = MibTableColumn
bosIpAclMaxSrcProtPort = _BosIpAclMaxSrcProtPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 12),
    _BosIpAclMaxSrcProtPort_Type()
)
bosIpAclMaxSrcProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclMaxSrcProtPort.setStatus("current")
_BosIpAclInPortList_Type = PortList
_BosIpAclInPortList_Object = MibTableColumn
bosIpAclInPortList = _BosIpAclInPortList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 13),
    _BosIpAclInPortList_Type()
)
bosIpAclInPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclInPortList.setStatus("current")
_BosIpAclOutPortList_Type = PortList
_BosIpAclOutPortList_Object = MibTableColumn
bosIpAclOutPortList = _BosIpAclOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 14),
    _BosIpAclOutPortList_Type()
)
bosIpAclOutPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclOutPortList.setStatus("current")


class _BosIpAclAckBit_Type(Integer32):
    """Custom type bosIpAclAckBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("establish", 1),
          ("notEstablish", 2),
          ("any", 3))
    )


_BosIpAclAckBit_Type.__name__ = "Integer32"
_BosIpAclAckBit_Object = MibTableColumn
bosIpAclAckBit = _BosIpAclAckBit_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 15),
    _BosIpAclAckBit_Type()
)
bosIpAclAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpAclAckBit.setStatus("current")


class _BosIpAclRstBit_Type(Integer32):
    """Custom type bosIpAclRstBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notSet", 2),
          ("any", 3))
    )


_BosIpAclRstBit_Type.__name__ = "Integer32"
_BosIpAclRstBit_Object = MibTableColumn
bosIpAclRstBit = _BosIpAclRstBit_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 16),
    _BosIpAclRstBit_Type()
)
bosIpAclRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpAclRstBit.setStatus("current")


class _BosIpAclFinBit_Type(Integer32):
    """Custom type bosIpAclFinBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notSet", 2),
          ("any", 3))
    )


_BosIpAclFinBit_Type.__name__ = "Integer32"
_BosIpAclFinBit_Object = MibScalar
bosIpAclFinBit = _BosIpAclFinBit_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 17),
    _BosIpAclFinBit_Type()
)
bosIpAclFinBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpAclFinBit.setStatus("current")


class _BosIpAclSynBit_Type(Integer32):
    """Custom type bosIpAclSynBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notSet", 2),
          ("any", 3))
    )


_BosIpAclSynBit_Type.__name__ = "Integer32"
_BosIpAclSynBit_Object = MibTableColumn
bosIpAclSynBit = _BosIpAclSynBit_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 18),
    _BosIpAclSynBit_Type()
)
bosIpAclSynBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpAclSynBit.setStatus("current")


class _BosIpAclUrgBit_Type(Integer32):
    """Custom type bosIpAclUrgBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notSet", 2),
          ("any", 3))
    )


_BosIpAclUrgBit_Type.__name__ = "Integer32"
_BosIpAclUrgBit_Object = MibTableColumn
bosIpAclUrgBit = _BosIpAclUrgBit_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 19),
    _BosIpAclUrgBit_Type()
)
bosIpAclUrgBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpAclUrgBit.setStatus("current")


class _BosIpAclPshBit_Type(Integer32):
    """Custom type bosIpAclPshBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notSet", 2),
          ("any", 3))
    )


_BosIpAclPshBit_Type.__name__ = "Integer32"
_BosIpAclPshBit_Object = MibTableColumn
bosIpAclPshBit = _BosIpAclPshBit_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 20),
    _BosIpAclPshBit_Type()
)
bosIpAclPshBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpAclPshBit.setStatus("current")


class _BosIpAclTos_Type(Integer32):
    """Custom type bosIpAclTos based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BosIpAclTos_Type.__name__ = "Integer32"
_BosIpAclTos_Object = MibTableColumn
bosIpAclTos = _BosIpAclTos_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 21),
    _BosIpAclTos_Type()
)
bosIpAclTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpAclTos.setStatus("current")


class _BosIpAclDscp_Type(Integer32):
    """Custom type bosIpAclDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_BosIpAclDscp_Type.__name__ = "Integer32"
_BosIpAclDscp_Object = MibTableColumn
bosIpAclDscp = _BosIpAclDscp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 22),
    _BosIpAclDscp_Type()
)
bosIpAclDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpAclDscp.setStatus("current")


class _BosIpAclAction_Type(Integer32):
    """Custom type bosIpAclAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2))
    )


_BosIpAclAction_Type.__name__ = "Integer32"
_BosIpAclAction_Object = MibTableColumn
bosIpAclAction = _BosIpAclAction_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 23),
    _BosIpAclAction_Type()
)
bosIpAclAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclAction.setStatus("current")
_BosIpAclMatchCount_Type = Counter32
_BosIpAclMatchCount_Object = MibTableColumn
bosIpAclMatchCount = _BosIpAclMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 24),
    _BosIpAclMatchCount_Type()
)
bosIpAclMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpAclMatchCount.setStatus("current")
_BosIpAclStatsStatus_Type = TruthValue
_BosIpAclStatsStatus_Object = MibTableColumn
bosIpAclStatsStatus = _BosIpAclStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 25),
    _BosIpAclStatsStatus_Type()
)
bosIpAclStatsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclStatsStatus.setStatus("current")
_BosIpAclStats_Type = Counter32
_BosIpAclStats_Object = MibTableColumn
bosIpAclStats = _BosIpAclStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 26),
    _BosIpAclStats_Type()
)
bosIpAclStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpAclStats.setStatus("current")


class _BosIpAclClearStats_Type(Integer32):
    """Custom type bosIpAclClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_BosIpAclClearStats_Type.__name__ = "Integer32"
_BosIpAclClearStats_Object = MibTableColumn
bosIpAclClearStats = _BosIpAclClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 27),
    _BosIpAclClearStats_Type()
)
bosIpAclClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpAclClearStats.setStatus("current")


class _BosIpAclUserPriority_Type(Integer32):
    """Custom type bosIpAclUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BosIpAclUserPriority_Type.__name__ = "Integer32"
_BosIpAclUserPriority_Object = MibTableColumn
bosIpAclUserPriority = _BosIpAclUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 28),
    _BosIpAclUserPriority_Type()
)
bosIpAclUserPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpAclUserPriority.setStatus("current")
_BosIpAclStatus_Type = RowStatus
_BosIpAclStatus_Object = MibTableColumn
bosIpAclStatus = _BosIpAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 81, 8, 6, 1, 1, 29),
    _BosIpAclStatus_Type()
)
bosIpAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosIpAclStatus.setStatus("current")
_BosDiffServMib_ObjectIdentity = ObjectIdentity
bosDiffServMib = _BosDiffServMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 83)
)
_BosDhcpClientMIB_ObjectIdentity = ObjectIdentity
bosDhcpClientMIB = _BosDhcpClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87)
)
_DhcpClientConfig_ObjectIdentity = ObjectIdentity
dhcpClientConfig = _DhcpClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 1)
)
_DhcpClientConfigTable_Object = MibTable
dhcpClientConfigTable = _DhcpClientConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpClientConfigTable.setStatus("current")
_DhcpClientConfigEntry_Object = MibTableRow
dhcpClientConfigEntry = _DhcpClientConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 1, 1, 1)
)
dhcpClientConfigEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "dhcpClientConfigIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpClientConfigEntry.setStatus("current")


class _DhcpClientConfigIfIndex_Type(Integer32):
    """Custom type dhcpClientConfigIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpClientConfigIfIndex_Type.__name__ = "Integer32"
_DhcpClientConfigIfIndex_Object = MibTableColumn
dhcpClientConfigIfIndex = _DhcpClientConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 1, 1, 1, 1),
    _DhcpClientConfigIfIndex_Type()
)
dhcpClientConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpClientConfigIfIndex.setStatus("current")


class _DhcpClientRenew_Type(Integer32):
    """Custom type dhcpClientRenew based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notset", 2))
    )


_DhcpClientRenew_Type.__name__ = "Integer32"
_DhcpClientRenew_Object = MibTableColumn
dhcpClientRenew = _DhcpClientRenew_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 1, 1, 1, 2),
    _DhcpClientRenew_Type()
)
dhcpClientRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientRenew.setStatus("current")


class _DhcpClientRelease_Type(Integer32):
    """Custom type dhcpClientRelease based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notset", 2))
    )


_DhcpClientRelease_Type.__name__ = "Integer32"
_DhcpClientRelease_Object = MibTableColumn
dhcpClientRelease = _DhcpClientRelease_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 1, 1, 1, 5),
    _DhcpClientRelease_Type()
)
dhcpClientRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientRelease.setStatus("current")
_DhcpClientCounters_ObjectIdentity = ObjectIdentity
dhcpClientCounters = _DhcpClientCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2)
)
_DhcpClientCounterTable_Object = MibTable
dhcpClientCounterTable = _DhcpClientCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpClientCounterTable.setStatus("current")
_DhcpClientCounterEntry_Object = MibTableRow
dhcpClientCounterEntry = _DhcpClientCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2, 1, 1)
)
dhcpClientCounterEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "dhcpClientIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpClientCounterEntry.setStatus("current")


class _DhcpClientIfIndex_Type(Integer32):
    """Custom type dhcpClientIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DhcpClientIfIndex_Type.__name__ = "Integer32"
_DhcpClientIfIndex_Object = MibTableColumn
dhcpClientIfIndex = _DhcpClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2, 1, 1, 1),
    _DhcpClientIfIndex_Type()
)
dhcpClientIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpClientIfIndex.setStatus("current")
_DhcpClientCountDiscovers_Type = Counter32
_DhcpClientCountDiscovers_Object = MibTableColumn
dhcpClientCountDiscovers = _DhcpClientCountDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2, 1, 1, 2),
    _DhcpClientCountDiscovers_Type()
)
dhcpClientCountDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientCountDiscovers.setStatus("current")
_DhcpClientCountRequests_Type = Counter32
_DhcpClientCountRequests_Object = MibTableColumn
dhcpClientCountRequests = _DhcpClientCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2, 1, 1, 3),
    _DhcpClientCountRequests_Type()
)
dhcpClientCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientCountRequests.setStatus("current")
_DhcpClientCountReleases_Type = Counter32
_DhcpClientCountReleases_Object = MibTableColumn
dhcpClientCountReleases = _DhcpClientCountReleases_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2, 1, 1, 4),
    _DhcpClientCountReleases_Type()
)
dhcpClientCountReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientCountReleases.setStatus("current")
_DhcpClientCountDeclines_Type = Counter32
_DhcpClientCountDeclines_Object = MibTableColumn
dhcpClientCountDeclines = _DhcpClientCountDeclines_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2, 1, 1, 5),
    _DhcpClientCountDeclines_Type()
)
dhcpClientCountDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientCountDeclines.setStatus("current")
_DhcpClientLeaseTime_Type = Integer32
_DhcpClientLeaseTime_Object = MibTableColumn
dhcpClientLeaseTime = _DhcpClientLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2, 1, 1, 20),
    _DhcpClientLeaseTime_Type()
)
dhcpClientLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientLeaseTime.setStatus("current")


class _DhcpClientCounterReset_Type(Integer32):
    """Custom type dhcpClientCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notset", 2))
    )


_DhcpClientCounterReset_Type.__name__ = "Integer32"
_DhcpClientCounterReset_Object = MibTableColumn
dhcpClientCounterReset = _DhcpClientCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2, 1, 1, 21),
    _DhcpClientCounterReset_Type()
)
dhcpClientCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientCounterReset.setStatus("current")
_DhcpClientRemainLeaseTime_Type = Integer32
_DhcpClientRemainLeaseTime_Object = MibTableColumn
dhcpClientRemainLeaseTime = _DhcpClientRemainLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 87, 2, 1, 1, 22),
    _DhcpClientRemainLeaseTime_Type()
)
dhcpClientRemainLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientRemainLeaseTime.setStatus("current")
_BosSyslog_ObjectIdentity = ObjectIdentity
bosSyslog = _BosSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89)
)
_BosSyslogGeneralGroup_ObjectIdentity = ObjectIdentity
bosSyslogGeneralGroup = _BosSyslogGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 1)
)


class _BosSyslogLogging_Type(Integer32):
    """Custom type bosSyslogLogging based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosSyslogLogging_Type.__name__ = "Integer32"
_BosSyslogLogging_Object = MibScalar
bosSyslogLogging = _BosSyslogLogging_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 1, 1),
    _BosSyslogLogging_Type()
)
bosSyslogLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogLogging.setStatus("current")


class _BosSyslogTimeStamp_Type(Integer32):
    """Custom type bosSyslogTimeStamp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosSyslogTimeStamp_Type.__name__ = "Integer32"
_BosSyslogTimeStamp_Object = MibScalar
bosSyslogTimeStamp = _BosSyslogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 1, 2),
    _BosSyslogTimeStamp_Type()
)
bosSyslogTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogTimeStamp.setStatus("current")


class _BosSyslogConsoleLog_Type(Integer32):
    """Custom type bosSyslogConsoleLog based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosSyslogConsoleLog_Type.__name__ = "Integer32"
_BosSyslogConsoleLog_Object = MibScalar
bosSyslogConsoleLog = _BosSyslogConsoleLog_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 1, 3),
    _BosSyslogConsoleLog_Type()
)
bosSyslogConsoleLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogConsoleLog.setStatus("current")


class _BosSyslogSysBuffers_Type(Integer32):
    """Custom type bosSyslogSysBuffers based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_BosSyslogSysBuffers_Type.__name__ = "Integer32"
_BosSyslogSysBuffers_Object = MibScalar
bosSyslogSysBuffers = _BosSyslogSysBuffers_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 1, 4),
    _BosSyslogSysBuffers_Type()
)
bosSyslogSysBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogSysBuffers.setStatus("current")


class _BosSyslogClearLog_Type(TruthValue):
    """Custom type bosSyslogClearLog based on TruthValue"""
    defaultValue = 2


_BosSyslogClearLog_Type.__name__ = "TruthValue"
_BosSyslogClearLog_Object = MibScalar
bosSyslogClearLog = _BosSyslogClearLog_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 1, 5),
    _BosSyslogClearLog_Type()
)
bosSyslogClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogClearLog.setStatus("current")


class _BosSyslogFacility_Type(Integer32):
    """Custom type bosSyslogFacility based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              136,
              144,
              152,
              160,
              168,
              176,
              184)
        )
    )
    namedValues = NamedValues(
        *(("local0", 128),
          ("local1", 136),
          ("local2", 144),
          ("local3", 152),
          ("local4", 160),
          ("local5", 168),
          ("local6", 176),
          ("local7", 184))
    )


_BosSyslogFacility_Type.__name__ = "Integer32"
_BosSyslogFacility_Object = MibScalar
bosSyslogFacility = _BosSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 1, 7),
    _BosSyslogFacility_Type()
)
bosSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogFacility.setStatus("current")


class _BosSyslogFacilitySec_Type(Integer32):
    """Custom type bosSyslogFacilitySec based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(128,
              136,
              144,
              152,
              160,
              168,
              176,
              184)
        )
    )
    namedValues = NamedValues(
        *(("local0", 128),
          ("local1", 136),
          ("local2", 144),
          ("local3", 152),
          ("local4", 160),
          ("local5", 168),
          ("local6", 176),
          ("local7", 184))
    )


_BosSyslogFacilitySec_Type.__name__ = "Integer32"
_BosSyslogFacilitySec_Object = MibScalar
bosSyslogFacilitySec = _BosSyslogFacilitySec_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 1, 8),
    _BosSyslogFacilitySec_Type()
)
bosSyslogFacilitySec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogFacilitySec.setStatus("current")


class _BosSyslogSeverity_Type(Integer32):
    """Custom type bosSyslogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_BosSyslogSeverity_Type.__name__ = "Integer32"
_BosSyslogSeverity_Object = MibScalar
bosSyslogSeverity = _BosSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 1, 9),
    _BosSyslogSeverity_Type()
)
bosSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogSeverity.setStatus("current")


class _BosSyslogSeveritySec_Type(Integer32):
    """Custom type bosSyslogSeveritySec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_BosSyslogSeveritySec_Type.__name__ = "Integer32"
_BosSyslogSeveritySec_Object = MibScalar
bosSyslogSeveritySec = _BosSyslogSeveritySec_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 1, 10),
    _BosSyslogSeveritySec_Type()
)
bosSyslogSeveritySec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogSeveritySec.setStatus("current")
_BosSyslogLogs_ObjectIdentity = ObjectIdentity
bosSyslogLogs = _BosSyslogLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 2)
)
_BosSyslogLogSrvAddr_Type = IpAddress
_BosSyslogLogSrvAddr_Object = MibScalar
bosSyslogLogSrvAddr = _BosSyslogLogSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 2, 1),
    _BosSyslogLogSrvAddr_Type()
)
bosSyslogLogSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogLogSrvAddr.setStatus("current")
_BosSyslogLogNoLogServer_Type = TruthValue
_BosSyslogLogNoLogServer_Object = MibScalar
bosSyslogLogNoLogServer = _BosSyslogLogNoLogServer_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 2, 2),
    _BosSyslogLogNoLogServer_Type()
)
bosSyslogLogNoLogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogLogNoLogServer.setStatus("current")
_BosSyslogLogSrvAddrSec_Type = IpAddress
_BosSyslogLogSrvAddrSec_Object = MibScalar
bosSyslogLogSrvAddrSec = _BosSyslogLogSrvAddrSec_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 2, 3),
    _BosSyslogLogSrvAddrSec_Type()
)
bosSyslogLogSrvAddrSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogLogSrvAddrSec.setStatus("current")
_BosSyslogLogNoLogServerSec_Type = TruthValue
_BosSyslogLogNoLogServerSec_Object = MibScalar
bosSyslogLogNoLogServerSec = _BosSyslogLogNoLogServerSec_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 89, 2, 4),
    _BosSyslogLogNoLogServerSec_Type()
)
bosSyslogLogNoLogServerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSyslogLogNoLogServerSec.setStatus("current")
_Ssl_ObjectIdentity = ObjectIdentity
ssl = _Ssl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 96)
)
_SslGeneralGroup_ObjectIdentity = ObjectIdentity
sslGeneralGroup = _SslGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 96, 1)
)


class _SslSecureHttpStatus_Type(Integer32):
    """Custom type sslSecureHttpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SslSecureHttpStatus_Type.__name__ = "Integer32"
_SslSecureHttpStatus_Object = MibScalar
sslSecureHttpStatus = _SslSecureHttpStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 96, 1, 2),
    _SslSecureHttpStatus_Type()
)
sslSecureHttpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslSecureHttpStatus.setStatus("current")


class _SslPort_Type(Integer32):
    """Custom type sslPort based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SslPort_Type.__name__ = "Integer32"
_SslPort_Object = MibScalar
sslPort = _SslPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 96, 1, 3),
    _SslPort_Type()
)
sslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslPort.setStatus("current")
_SslTrace_Type = Integer32
_SslTrace_Object = MibScalar
sslTrace = _SslTrace_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 96, 1, 4),
    _SslTrace_Type()
)
sslTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslTrace.setStatus("current")
_SslCiphers_ObjectIdentity = ObjectIdentity
sslCiphers = _SslCiphers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 96, 2)
)


class _SslCipherList_Type(Integer32):
    """Custom type sslCipherList based on Integer32"""
    defaultValue = 0


_SslCipherList_Type.__name__ = "Integer32"
_SslCipherList_Object = MibScalar
sslCipherList = _SslCipherList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 96, 2, 1),
    _SslCipherList_Type()
)
sslCipherList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCipherList.setStatus("current")


class _SslDefaultCipherList_Type(TruthValue):
    """Custom type sslDefaultCipherList based on TruthValue"""
    defaultValue = 2


_SslDefaultCipherList_Type.__name__ = "TruthValue"
_SslDefaultCipherList_Object = MibScalar
sslDefaultCipherList = _SslDefaultCipherList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 96, 2, 2),
    _SslDefaultCipherList_Type()
)
sslDefaultCipherList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslDefaultCipherList.setStatus("current")
_Ssh_ObjectIdentity = ObjectIdentity
ssh = _Ssh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 97)
)
_G8000addon_ObjectIdentity = ObjectIdentity
g8000addon = _G8000addon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100)
)
_Cfa_ObjectIdentity = ObjectIdentity
cfa = _Cfa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2)
)
_BosPortCfgTable_Object = MibTable
bosPortCfgTable = _BosPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 1)
)
if mibBuilder.loadTexts:
    bosPortCfgTable.setStatus("current")
_BosPortCfgTableEntry_Object = MibTableRow
bosPortCfgTableEntry = _BosPortCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 1, 1)
)
bosPortCfgTableEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPortCfgIndx"),
)
if mibBuilder.loadTexts:
    bosPortCfgTableEntry.setStatus("current")
_BosPortCfgIndx_Type = Integer32
_BosPortCfgIndx_Object = MibTableColumn
bosPortCfgIndx = _BosPortCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 1, 1, 1),
    _BosPortCfgIndx_Type()
)
bosPortCfgIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosPortCfgIndx.setStatus("current")


class _BosPortCfgVlanTag_Type(Integer32):
    """Custom type bosPortCfgVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosPortCfgVlanTag_Type.__name__ = "Integer32"
_BosPortCfgVlanTag_Object = MibTableColumn
bosPortCfgVlanTag = _BosPortCfgVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 1, 1, 2),
    _BosPortCfgVlanTag_Type()
)
bosPortCfgVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPortCfgVlanTag.setStatus("current")
_BosPortCfgStateChangeCount_Type = Counter32
_BosPortCfgStateChangeCount_Object = MibTableColumn
bosPortCfgStateChangeCount = _BosPortCfgStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 1, 1, 3),
    _BosPortCfgStateChangeCount_Type()
)
bosPortCfgStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPortCfgStateChangeCount.setStatus("current")


class _BosPortCfgLearning_Type(Integer32):
    """Custom type bosPortCfgLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BosPortCfgLearning_Type.__name__ = "Integer32"
_BosPortCfgLearning_Object = MibTableColumn
bosPortCfgLearning = _BosPortCfgLearning_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 1, 1, 4),
    _BosPortCfgLearning_Type()
)
bosPortCfgLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPortCfgLearning.setStatus("current")


class _BosPortCfgFlooding_Type(Integer32):
    """Custom type bosPortCfgFlooding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BosPortCfgFlooding_Type.__name__ = "Integer32"
_BosPortCfgFlooding_Object = MibTableColumn
bosPortCfgFlooding = _BosPortCfgFlooding_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 1, 1, 5),
    _BosPortCfgFlooding_Type()
)
bosPortCfgFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPortCfgFlooding.setStatus("current")


class _BosPortCfgTagPvid_Type(Integer32):
    """Custom type bosPortCfgTagPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BosPortCfgTagPvid_Type.__name__ = "Integer32"
_BosPortCfgTagPvid_Object = MibTableColumn
bosPortCfgTagPvid = _BosPortCfgTagPvid_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 1, 1, 6),
    _BosPortCfgTagPvid_Type()
)
bosPortCfgTagPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPortCfgTagPvid.setStatus("current")


class _BosPortCfgMacNotif_Type(Integer32):
    """Custom type bosPortCfgMacNotif based on Integer32"""
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


_BosPortCfgMacNotif_Type.__name__ = "Integer32"
_BosPortCfgMacNotif_Object = MibTableColumn
bosPortCfgMacNotif = _BosPortCfgMacNotif_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 1, 1, 7),
    _BosPortCfgMacNotif_Type()
)
bosPortCfgMacNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPortCfgMacNotif.setStatus("current")
_BosPortStatsClearTable_Object = MibTable
bosPortStatsClearTable = _BosPortStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 2)
)
if mibBuilder.loadTexts:
    bosPortStatsClearTable.setStatus("current")
_BosPortStatsClearTableEntry_Object = MibTableRow
bosPortStatsClearTableEntry = _BosPortStatsClearTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 2, 1)
)
bosPortStatsClearTableEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosPortStatsIndx"),
)
if mibBuilder.loadTexts:
    bosPortStatsClearTableEntry.setStatus("current")
_BosPortStatsIndx_Type = InterfaceIndex
_BosPortStatsIndx_Object = MibTableColumn
bosPortStatsIndx = _BosPortStatsIndx_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 2, 1, 1),
    _BosPortStatsIndx_Type()
)
bosPortStatsIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosPortStatsIndx.setStatus("current")


class _BosPortStatsClear_Type(Integer32):
    """Custom type bosPortStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_BosPortStatsClear_Type.__name__ = "Integer32"
_BosPortStatsClear_Object = MibTableColumn
bosPortStatsClear = _BosPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 2, 1, 2),
    _BosPortStatsClear_Type()
)
bosPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosPortStatsClear.setStatus("current")


class _BosClearPortsStats_Type(Integer32):
    """Custom type bosClearPortsStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_BosClearPortsStats_Type.__name__ = "Integer32"
_BosClearPortsStats_Object = MibScalar
bosClearPortsStats = _BosClearPortsStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 2, 3),
    _BosClearPortsStats_Type()
)
bosClearPortsStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosClearPortsStats.setStatus("current")
_Igs_ObjectIdentity = ObjectIdentity
igs = _Igs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5)
)
_IgmpV3SnoopCfg_ObjectIdentity = ObjectIdentity
igmpV3SnoopCfg = _IgmpV3SnoopCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 2)
)
_IgmpV3SnoopNewCfgSources_Type = Integer32
_IgmpV3SnoopNewCfgSources_Object = MibScalar
igmpV3SnoopNewCfgSources = _IgmpV3SnoopNewCfgSources_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 2, 1),
    _IgmpV3SnoopNewCfgSources_Type()
)
igmpV3SnoopNewCfgSources.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpV3SnoopNewCfgSources.setStatus("current")


class _IgmpV3SnoopNewCfgEnaDis_Type(Integer32):
    """Custom type igmpV3SnoopNewCfgEnaDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IgmpV3SnoopNewCfgEnaDis_Type.__name__ = "Integer32"
_IgmpV3SnoopNewCfgEnaDis_Object = MibScalar
igmpV3SnoopNewCfgEnaDis = _IgmpV3SnoopNewCfgEnaDis_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 2, 2),
    _IgmpV3SnoopNewCfgEnaDis_Type()
)
igmpV3SnoopNewCfgEnaDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpV3SnoopNewCfgEnaDis.setStatus("current")


class _IgmpV3SnoopNewCfgExcludeEnaDis_Type(Integer32):
    """Custom type igmpV3SnoopNewCfgExcludeEnaDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IgmpV3SnoopNewCfgExcludeEnaDis_Type.__name__ = "Integer32"
_IgmpV3SnoopNewCfgExcludeEnaDis_Object = MibScalar
igmpV3SnoopNewCfgExcludeEnaDis = _IgmpV3SnoopNewCfgExcludeEnaDis_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 2, 3),
    _IgmpV3SnoopNewCfgExcludeEnaDis_Type()
)
igmpV3SnoopNewCfgExcludeEnaDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpV3SnoopNewCfgExcludeEnaDis.setStatus("current")


class _IgmpV3SnoopNewCfgV1V2EnaDis_Type(Integer32):
    """Custom type igmpV3SnoopNewCfgV1V2EnaDis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IgmpV3SnoopNewCfgV1V2EnaDis_Type.__name__ = "Integer32"
_IgmpV3SnoopNewCfgV1V2EnaDis_Object = MibScalar
igmpV3SnoopNewCfgV1V2EnaDis = _IgmpV3SnoopNewCfgV1V2EnaDis_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 2, 4),
    _IgmpV3SnoopNewCfgV1V2EnaDis_Type()
)
igmpV3SnoopNewCfgV1V2EnaDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpV3SnoopNewCfgV1V2EnaDis.setStatus("current")
_IgmpSnoopCfg_ObjectIdentity = ObjectIdentity
igmpSnoopCfg = _IgmpSnoopCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3)
)


class _IgmpSnoopStatsClear_Type(Integer32):
    """Custom type igmpSnoopStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_IgmpSnoopStatsClear_Type.__name__ = "Integer32"
_IgmpSnoopStatsClear_Object = MibScalar
igmpSnoopStatsClear = _IgmpSnoopStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 2),
    _IgmpSnoopStatsClear_Type()
)
igmpSnoopStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopStatsClear.setStatus("current")


class _IgmpSnoopGroupClear_Type(Integer32):
    """Custom type igmpSnoopGroupClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_IgmpSnoopGroupClear_Type.__name__ = "Integer32"
_IgmpSnoopGroupClear_Object = MibScalar
igmpSnoopGroupClear = _IgmpSnoopGroupClear_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 3),
    _IgmpSnoopGroupClear_Type()
)
igmpSnoopGroupClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopGroupClear.setStatus("current")


class _IgmpSnoopMrouterClear_Type(Integer32):
    """Custom type igmpSnoopMrouterClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_IgmpSnoopMrouterClear_Type.__name__ = "Integer32"
_IgmpSnoopMrouterClear_Object = MibScalar
igmpSnoopMrouterClear = _IgmpSnoopMrouterClear_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 4),
    _IgmpSnoopMrouterClear_Type()
)
igmpSnoopMrouterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopMrouterClear.setStatus("current")
_BosSnoopVlanStatsClearTable_Object = MibTable
bosSnoopVlanStatsClearTable = _BosSnoopVlanStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 5)
)
if mibBuilder.loadTexts:
    bosSnoopVlanStatsClearTable.setStatus("current")
_BosSnoopVlanStatsClearEntry_Object = MibTableRow
bosSnoopVlanStatsClearEntry = _BosSnoopVlanStatsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 5, 1)
)
bosSnoopVlanStatsClearEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanStatsClearVlanId"),
)
if mibBuilder.loadTexts:
    bosSnoopVlanStatsClearEntry.setStatus("current")
_BosSnoopVlanStatsClearVlanId_Type = Integer32
_BosSnoopVlanStatsClearVlanId_Object = MibTableColumn
bosSnoopVlanStatsClearVlanId = _BosSnoopVlanStatsClearVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 5, 1, 1),
    _BosSnoopVlanStatsClearVlanId_Type()
)
bosSnoopVlanStatsClearVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanStatsClearVlanId.setStatus("current")


class _BosSnoopVlanStatsClear_Type(Integer32):
    """Custom type bosSnoopVlanStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_BosSnoopVlanStatsClear_Type.__name__ = "Integer32"
_BosSnoopVlanStatsClear_Object = MibTableColumn
bosSnoopVlanStatsClear = _BosSnoopVlanStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 5, 1, 2),
    _BosSnoopVlanStatsClear_Type()
)
bosSnoopVlanStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopVlanStatsClear.setStatus("current")


class _IgmpSnoopFloodStatus_Type(Integer32):
    """Custom type igmpSnoopFloodStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_IgmpSnoopFloodStatus_Type.__name__ = "Integer32"
_IgmpSnoopFloodStatus_Object = MibScalar
igmpSnoopFloodStatus = _IgmpSnoopFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 6),
    _IgmpSnoopFloodStatus_Type()
)
igmpSnoopFloodStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopFloodStatus.setStatus("current")
_BosigmpSnoopVlanConfigTable_Object = MibTable
bosigmpSnoopVlanConfigTable = _BosigmpSnoopVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 7)
)
if mibBuilder.loadTexts:
    bosigmpSnoopVlanConfigTable.setStatus("current")
_BosigmpSnoopVlanConfigEntry_Object = MibTableRow
bosigmpSnoopVlanConfigEntry = _BosigmpSnoopVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 7, 1)
)
bosigmpSnoopVlanConfigEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanConfigVlanId"),
)
if mibBuilder.loadTexts:
    bosigmpSnoopVlanConfigEntry.setStatus("current")
_BosSnoopVlanConfigVlanId_Type = Integer32
_BosSnoopVlanConfigVlanId_Object = MibTableColumn
bosSnoopVlanConfigVlanId = _BosSnoopVlanConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 7, 1, 1),
    _BosSnoopVlanConfigVlanId_Type()
)
bosSnoopVlanConfigVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanConfigVlanId.setStatus("current")
_BosSnoopVlanConfigSrcIp_Type = IpAddress
_BosSnoopVlanConfigSrcIp_Object = MibTableColumn
bosSnoopVlanConfigSrcIp = _BosSnoopVlanConfigSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 3, 7, 1, 2),
    _BosSnoopVlanConfigSrcIp_Type()
)
bosSnoopVlanConfigSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopVlanConfigSrcIp.setStatus("current")
_BosSnoopInfo_ObjectIdentity = ObjectIdentity
bosSnoopInfo = _BosSnoopInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4)
)
_BosSnoopInfoTable_Object = MibTable
bosSnoopInfoTable = _BosSnoopInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1)
)
if mibBuilder.loadTexts:
    bosSnoopInfoTable.setStatus("current")
_BosSnoopInfoEntry_Object = MibTableRow
bosSnoopInfoEntry = _BosSnoopInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1, 1)
)
bosSnoopInfoEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnoopInfoAddressType"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopInfoVlanId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopInfoGroupAddress"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopInfoSourceAddress"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopInfoPortNum"),
)
if mibBuilder.loadTexts:
    bosSnoopInfoEntry.setStatus("current")
_BosSnoopInfoAddressType_Type = InetAddressType
_BosSnoopInfoAddressType_Object = MibTableColumn
bosSnoopInfoAddressType = _BosSnoopInfoAddressType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1, 1, 1),
    _BosSnoopInfoAddressType_Type()
)
bosSnoopInfoAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopInfoAddressType.setStatus("current")
_BosSnoopInfoVlanId_Type = Integer32
_BosSnoopInfoVlanId_Object = MibTableColumn
bosSnoopInfoVlanId = _BosSnoopInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1, 1, 2),
    _BosSnoopInfoVlanId_Type()
)
bosSnoopInfoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopInfoVlanId.setStatus("current")
_BosSnoopInfoGroupAddress_Type = InetAddress
_BosSnoopInfoGroupAddress_Object = MibTableColumn
bosSnoopInfoGroupAddress = _BosSnoopInfoGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1, 1, 3),
    _BosSnoopInfoGroupAddress_Type()
)
bosSnoopInfoGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopInfoGroupAddress.setStatus("current")
_BosSnoopInfoSourceAddress_Type = InetAddress
_BosSnoopInfoSourceAddress_Object = MibTableColumn
bosSnoopInfoSourceAddress = _BosSnoopInfoSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1, 1, 4),
    _BosSnoopInfoSourceAddress_Type()
)
bosSnoopInfoSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopInfoSourceAddress.setStatus("current")
_BosSnoopInfoPortNum_Type = Integer32
_BosSnoopInfoPortNum_Object = MibTableColumn
bosSnoopInfoPortNum = _BosSnoopInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1, 1, 5),
    _BosSnoopInfoPortNum_Type()
)
bosSnoopInfoPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopInfoPortNum.setStatus("current")


class _BosSnoopInfoVersion_Type(Integer32):
    """Custom type bosSnoopInfoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_BosSnoopInfoVersion_Type.__name__ = "Integer32"
_BosSnoopInfoVersion_Object = MibTableColumn
bosSnoopInfoVersion = _BosSnoopInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1, 1, 6),
    _BosSnoopInfoVersion_Type()
)
bosSnoopInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopInfoVersion.setStatus("current")
_BosSnoopInfoExpires_Type = DisplayString
_BosSnoopInfoExpires_Object = MibTableColumn
bosSnoopInfoExpires = _BosSnoopInfoExpires_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1, 1, 7),
    _BosSnoopInfoExpires_Type()
)
bosSnoopInfoExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopInfoExpires.setStatus("current")


class _BosSnoopInfoMode_Type(Integer32):
    """Custom type bosSnoopInfoMode based on Integer32"""
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
          ("exclude", 1),
          ("include", 2))
    )


_BosSnoopInfoMode_Type.__name__ = "Integer32"
_BosSnoopInfoMode_Object = MibTableColumn
bosSnoopInfoMode = _BosSnoopInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1, 1, 8),
    _BosSnoopInfoMode_Type()
)
bosSnoopInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopInfoMode.setStatus("current")


class _BosSnoopInfoFwd_Type(Integer32):
    """Custom type bosSnoopInfoFwd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BosSnoopInfoFwd_Type.__name__ = "Integer32"
_BosSnoopInfoFwd_Object = MibTableColumn
bosSnoopInfoFwd = _BosSnoopInfoFwd_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 1, 1, 9),
    _BosSnoopInfoFwd_Type()
)
bosSnoopInfoFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopInfoFwd.setStatus("current")
_BosSnoopMrouterInfoTable_Object = MibTable
bosSnoopMrouterInfoTable = _BosSnoopMrouterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 2)
)
if mibBuilder.loadTexts:
    bosSnoopMrouterInfoTable.setStatus("current")
_BosSnoopMrouterInfoEntry_Object = MibTableRow
bosSnoopMrouterInfoEntry = _BosSnoopMrouterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 2, 1)
)
bosSnoopMrouterInfoEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnoopMrouterInfoVlanId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopMrouterInfoPortNum"),
)
if mibBuilder.loadTexts:
    bosSnoopMrouterInfoEntry.setStatus("current")
_BosSnoopMrouterInfoVlanId_Type = Integer32
_BosSnoopMrouterInfoVlanId_Object = MibTableColumn
bosSnoopMrouterInfoVlanId = _BosSnoopMrouterInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 2, 1, 1),
    _BosSnoopMrouterInfoVlanId_Type()
)
bosSnoopMrouterInfoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopMrouterInfoVlanId.setStatus("current")
_BosSnoopMrouterInfoPortNum_Type = Integer32
_BosSnoopMrouterInfoPortNum_Object = MibTableColumn
bosSnoopMrouterInfoPortNum = _BosSnoopMrouterInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 2, 1, 2),
    _BosSnoopMrouterInfoPortNum_Type()
)
bosSnoopMrouterInfoPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopMrouterInfoPortNum.setStatus("current")
_BosSnoopMrouterInfoExpires_Type = DisplayString
_BosSnoopMrouterInfoExpires_Object = MibTableColumn
bosSnoopMrouterInfoExpires = _BosSnoopMrouterInfoExpires_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 2, 1, 3),
    _BosSnoopMrouterInfoExpires_Type()
)
bosSnoopMrouterInfoExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopMrouterInfoExpires.setStatus("current")
_BosSnoopMrouterInfoResponseTime_Type = Integer32
_BosSnoopMrouterInfoResponseTime_Object = MibTableColumn
bosSnoopMrouterInfoResponseTime = _BosSnoopMrouterInfoResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 2, 1, 4),
    _BosSnoopMrouterInfoResponseTime_Type()
)
bosSnoopMrouterInfoResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopMrouterInfoResponseTime.setStatus("current")
_BosSnoopMrouterInfoQRV_Type = Integer32
_BosSnoopMrouterInfoQRV_Object = MibTableColumn
bosSnoopMrouterInfoQRV = _BosSnoopMrouterInfoQRV_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 2, 1, 5),
    _BosSnoopMrouterInfoQRV_Type()
)
bosSnoopMrouterInfoQRV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopMrouterInfoQRV.setStatus("current")
_BosSnoopMrouterInfoQQIC_Type = Integer32
_BosSnoopMrouterInfoQQIC_Object = MibTableColumn
bosSnoopMrouterInfoQQIC = _BosSnoopMrouterInfoQQIC_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 5, 4, 2, 1, 6),
    _BosSnoopMrouterInfoQQIC_Type()
)
bosSnoopMrouterInfoQQIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopMrouterInfoQQIC.setStatus("current")
_Pnac_ObjectIdentity = ObjectIdentity
pnac = _Pnac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6)
)
_Dot1x_ObjectIdentity = ObjectIdentity
dot1x = _Dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1)
)


class _Dot1xNewStatus_Type(Integer32):
    """Custom type dot1xNewStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_Dot1xNewStatus_Type.__name__ = "Integer32"
_Dot1xNewStatus_Object = MibScalar
dot1xNewStatus = _Dot1xNewStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 1),
    _Dot1xNewStatus_Type()
)
dot1xNewStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewStatus.setStatus("current")
_Dot1xNewCfgGlobalTable_ObjectIdentity = ObjectIdentity
dot1xNewCfgGlobalTable = _Dot1xNewCfgGlobalTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 2)
)


class _Dot1xNewCfgGlobalMode_Type(Integer32):
    """Custom type dot1xNewCfgGlobalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceUnauth", 0),
          ("auto", 1),
          ("forceAuth", 2))
    )


_Dot1xNewCfgGlobalMode_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalMode_Object = MibScalar
dot1xNewCfgGlobalMode = _Dot1xNewCfgGlobalMode_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 2, 3),
    _Dot1xNewCfgGlobalMode_Type()
)
dot1xNewCfgGlobalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalMode.setStatus("current")


class _Dot1xNewCfgGlobalQtPeriod_Type(Integer32):
    """Custom type dot1xNewCfgGlobalQtPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1xNewCfgGlobalQtPeriod_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalQtPeriod_Object = MibScalar
dot1xNewCfgGlobalQtPeriod = _Dot1xNewCfgGlobalQtPeriod_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 2, 4),
    _Dot1xNewCfgGlobalQtPeriod_Type()
)
dot1xNewCfgGlobalQtPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalQtPeriod.setStatus("current")


class _Dot1xNewCfgGlobalTxPeriod_Type(Integer32):
    """Custom type dot1xNewCfgGlobalTxPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xNewCfgGlobalTxPeriod_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalTxPeriod_Object = MibScalar
dot1xNewCfgGlobalTxPeriod = _Dot1xNewCfgGlobalTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 2, 5),
    _Dot1xNewCfgGlobalTxPeriod_Type()
)
dot1xNewCfgGlobalTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalTxPeriod.setStatus("current")


class _Dot1xNewCfgGlobalSupTmout_Type(Integer32):
    """Custom type dot1xNewCfgGlobalSupTmout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xNewCfgGlobalSupTmout_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalSupTmout_Object = MibScalar
dot1xNewCfgGlobalSupTmout = _Dot1xNewCfgGlobalSupTmout_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 2, 6),
    _Dot1xNewCfgGlobalSupTmout_Type()
)
dot1xNewCfgGlobalSupTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalSupTmout.setStatus("current")


class _Dot1xNewCfgGlobalSrvTmout_Type(Integer32):
    """Custom type dot1xNewCfgGlobalSrvTmout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xNewCfgGlobalSrvTmout_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalSrvTmout_Object = MibScalar
dot1xNewCfgGlobalSrvTmout = _Dot1xNewCfgGlobalSrvTmout_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 2, 7),
    _Dot1xNewCfgGlobalSrvTmout_Type()
)
dot1xNewCfgGlobalSrvTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalSrvTmout.setStatus("current")


class _Dot1xNewCfgGlobalMaxRq_Type(Integer32):
    """Custom type dot1xNewCfgGlobalMaxRq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dot1xNewCfgGlobalMaxRq_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalMaxRq_Object = MibScalar
dot1xNewCfgGlobalMaxRq = _Dot1xNewCfgGlobalMaxRq_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 2, 8),
    _Dot1xNewCfgGlobalMaxRq_Type()
)
dot1xNewCfgGlobalMaxRq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalMaxRq.setStatus("current")


class _Dot1xNewCfgGlobalRaPeriod_Type(Integer32):
    """Custom type dot1xNewCfgGlobalRaPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_Dot1xNewCfgGlobalRaPeriod_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalRaPeriod_Object = MibScalar
dot1xNewCfgGlobalRaPeriod = _Dot1xNewCfgGlobalRaPeriod_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 2, 9),
    _Dot1xNewCfgGlobalRaPeriod_Type()
)
dot1xNewCfgGlobalRaPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalRaPeriod.setStatus("current")


class _Dot1xNewCfgGlobalReAuth_Type(Integer32):
    """Custom type dot1xNewCfgGlobalReAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Dot1xNewCfgGlobalReAuth_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalReAuth_Object = MibScalar
dot1xNewCfgGlobalReAuth = _Dot1xNewCfgGlobalReAuth_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 2, 10),
    _Dot1xNewCfgGlobalReAuth_Type()
)
dot1xNewCfgGlobalReAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalReAuth.setStatus("current")


class _Dot1xNewCfgGlobalDefault_Type(Integer32):
    """Custom type dot1xNewCfgGlobalDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("apply", 1))
    )


_Dot1xNewCfgGlobalDefault_Type.__name__ = "Integer32"
_Dot1xNewCfgGlobalDefault_Object = MibScalar
dot1xNewCfgGlobalDefault = _Dot1xNewCfgGlobalDefault_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 2, 11),
    _Dot1xNewCfgGlobalDefault_Type()
)
dot1xNewCfgGlobalDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xNewCfgGlobalDefault.setStatus("current")
_Dot1xClearStatsTable_Object = MibTable
dot1xClearStatsTable = _Dot1xClearStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 3)
)
if mibBuilder.loadTexts:
    dot1xClearStatsTable.setStatus("current")
_Dot1xClearStatsEntry_Object = MibTableRow
dot1xClearStatsEntry = _Dot1xClearStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 3, 1)
)
dot1xClearStatsEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "dot1xPortNumber"),
)
if mibBuilder.loadTexts:
    dot1xClearStatsEntry.setStatus("current")
_Dot1xPortNumber_Type = Integer32
_Dot1xPortNumber_Object = MibTableColumn
dot1xPortNumber = _Dot1xPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 3, 1, 1),
    _Dot1xPortNumber_Type()
)
dot1xPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1xPortNumber.setStatus("current")


class _Dot1xClearStats_Type(Integer32):
    """Custom type dot1xClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("clear", 1))
    )


_Dot1xClearStats_Type.__name__ = "Integer32"
_Dot1xClearStats_Object = MibTableColumn
dot1xClearStats = _Dot1xClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 6, 1, 3, 1, 2),
    _Dot1xClearStats_Type()
)
dot1xClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1xClearStats.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7)
)
_AgNewCfgIdleCLITimeout_Type = Integer32
_AgNewCfgIdleCLITimeout_Object = MibScalar
agNewCfgIdleCLITimeout = _AgNewCfgIdleCLITimeout_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 1),
    _AgNewCfgIdleCLITimeout_Type()
)
agNewCfgIdleCLITimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgIdleCLITimeout.setStatus("current")
_TacacsCmdAuthorAcctStatusTable_Object = MibTable
tacacsCmdAuthorAcctStatusTable = _TacacsCmdAuthorAcctStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 3)
)
if mibBuilder.loadTexts:
    tacacsCmdAuthorAcctStatusTable.setStatus("current")
_TacacsCmdAuthorAcctStatusEntry_Object = MibTableRow
tacacsCmdAuthorAcctStatusEntry = _TacacsCmdAuthorAcctStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 3, 1)
)
tacacsCmdAuthorAcctStatusEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "tacacsCmdPrivLevel"),
)
if mibBuilder.loadTexts:
    tacacsCmdAuthorAcctStatusEntry.setStatus("current")


class _TacacsCmdPrivLevel_Type(Integer32):
    """Custom type tacacsCmdPrivLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TacacsCmdPrivLevel_Type.__name__ = "Integer32"
_TacacsCmdPrivLevel_Object = MibTableColumn
tacacsCmdPrivLevel = _TacacsCmdPrivLevel_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 3, 1, 1),
    _TacacsCmdPrivLevel_Type()
)
tacacsCmdPrivLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsCmdPrivLevel.setStatus("current")
_TacacsCmdAuthorstatus_Type = TruthValue
_TacacsCmdAuthorstatus_Object = MibTableColumn
tacacsCmdAuthorstatus = _TacacsCmdAuthorstatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 3, 1, 2),
    _TacacsCmdAuthorstatus_Type()
)
tacacsCmdAuthorstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsCmdAuthorstatus.setStatus("current")
_TacacsCmdAcctStatus_Type = TruthValue
_TacacsCmdAcctStatus_Object = MibTableColumn
tacacsCmdAcctStatus = _TacacsCmdAcctStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 3, 1, 3),
    _TacacsCmdAcctStatus_Type()
)
tacacsCmdAcctStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsCmdAcctStatus.setStatus("current")


class _SystemNotice1_Type(DisplayString):
    """Custom type systemNotice1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemNotice1_Type.__name__ = "DisplayString"
_SystemNotice1_Object = MibScalar
systemNotice1 = _SystemNotice1_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 6),
    _SystemNotice1_Type()
)
systemNotice1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNotice1.setStatus("current")


class _SystemNotice2_Type(DisplayString):
    """Custom type systemNotice2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemNotice2_Type.__name__ = "DisplayString"
_SystemNotice2_Object = MibScalar
systemNotice2 = _SystemNotice2_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 7),
    _SystemNotice2_Type()
)
systemNotice2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNotice2.setStatus("current")


class _SystemNotice3_Type(DisplayString):
    """Custom type systemNotice3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemNotice3_Type.__name__ = "DisplayString"
_SystemNotice3_Object = MibScalar
systemNotice3 = _SystemNotice3_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 8),
    _SystemNotice3_Type()
)
systemNotice3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNotice3.setStatus("current")


class _SystemNotice4_Type(DisplayString):
    """Custom type systemNotice4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemNotice4_Type.__name__ = "DisplayString"
_SystemNotice4_Object = MibScalar
systemNotice4 = _SystemNotice4_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 9),
    _SystemNotice4_Type()
)
systemNotice4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNotice4.setStatus("current")


class _SystemNotice5_Type(DisplayString):
    """Custom type systemNotice5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemNotice5_Type.__name__ = "DisplayString"
_SystemNotice5_Object = MibScalar
systemNotice5 = _SystemNotice5_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 10),
    _SystemNotice5_Type()
)
systemNotice5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNotice5.setStatus("current")


class _SystemBanner_Type(DisplayString):
    """Custom type systemBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SystemBanner_Type.__name__ = "DisplayString"
_SystemBanner_Object = MibScalar
systemBanner = _SystemBanner_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 11),
    _SystemBanner_Type()
)
systemBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemBanner.setStatus("current")


class _SysAccessUserBbi_Type(Integer32):
    """Custom type sysAccessUserBbi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_SysAccessUserBbi_Type.__name__ = "Integer32"
_SysAccessUserBbi_Object = MibScalar
sysAccessUserBbi = _SysAccessUserBbi_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 12),
    _SysAccessUserBbi_Type()
)
sysAccessUserBbi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAccessUserBbi.setStatus("current")


class _SysCurCfgHprompt_Type(Integer32):
    """Custom type sysCurCfgHprompt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_SysCurCfgHprompt_Type.__name__ = "Integer32"
_SysCurCfgHprompt_Object = MibScalar
sysCurCfgHprompt = _SysCurCfgHprompt_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 7, 13),
    _SysCurCfgHprompt_Type()
)
sysCurCfgHprompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCurCfgHprompt.setStatus("current")
_Pmirr_ObjectIdentity = ObjectIdentity
pmirr = _Pmirr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 8)
)


class _PmNewCfgPortMirrState_Type(Integer32):
    """Custom type pmNewCfgPortMirrState based on Integer32"""
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


_PmNewCfgPortMirrState_Type.__name__ = "Integer32"
_PmNewCfgPortMirrState_Object = MibScalar
pmNewCfgPortMirrState = _PmNewCfgPortMirrState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 8, 1),
    _PmNewCfgPortMirrState_Type()
)
pmNewCfgPortMirrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmNewCfgPortMirrState.setStatus("current")
_PmNewCfgPortMonitorTable_Object = MibTable
pmNewCfgPortMonitorTable = _PmNewCfgPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 8, 2)
)
if mibBuilder.loadTexts:
    pmNewCfgPortMonitorTable.setStatus("current")
_PmNewCfgPortMonitorEntry_Object = MibTableRow
pmNewCfgPortMonitorEntry = _PmNewCfgPortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 8, 2, 1)
)
pmNewCfgPortMonitorEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "pmNewCfgPmirrMoniPortIndex"),
    (0, "BLADEOS-BASE-MIB", "pmNewCfgPmirrMirrPortIndex"),
)
if mibBuilder.loadTexts:
    pmNewCfgPortMonitorEntry.setStatus("current")


class _PmNewCfgPmirrMoniPortIndex_Type(Integer32):
    """Custom type pmNewCfgPmirrMoniPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmNewCfgPmirrMoniPortIndex_Type.__name__ = "Integer32"
_PmNewCfgPmirrMoniPortIndex_Object = MibTableColumn
pmNewCfgPmirrMoniPortIndex = _PmNewCfgPmirrMoniPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 8, 2, 1, 1),
    _PmNewCfgPmirrMoniPortIndex_Type()
)
pmNewCfgPmirrMoniPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmNewCfgPmirrMoniPortIndex.setStatus("current")


class _PmNewCfgPmirrMirrPortIndex_Type(Integer32):
    """Custom type pmNewCfgPmirrMirrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmNewCfgPmirrMirrPortIndex_Type.__name__ = "Integer32"
_PmNewCfgPmirrMirrPortIndex_Object = MibTableColumn
pmNewCfgPmirrMirrPortIndex = _PmNewCfgPmirrMirrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 8, 2, 1, 2),
    _PmNewCfgPmirrMirrPortIndex_Type()
)
pmNewCfgPmirrMirrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmNewCfgPmirrMirrPortIndex.setStatus("current")


class _PmNewCfgPmirrDirection_Type(Integer32):
    """Custom type pmNewCfgPmirrDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2),
          ("both", 3))
    )


_PmNewCfgPmirrDirection_Type.__name__ = "Integer32"
_PmNewCfgPmirrDirection_Object = MibTableColumn
pmNewCfgPmirrDirection = _PmNewCfgPmirrDirection_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 8, 2, 1, 3),
    _PmNewCfgPmirrDirection_Type()
)
pmNewCfgPmirrDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmNewCfgPmirrDirection.setStatus("current")


class _PmNewCfgPmirrDelete_Type(Integer32):
    """Custom type pmNewCfgPmirrDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_PmNewCfgPmirrDelete_Type.__name__ = "Integer32"
_PmNewCfgPmirrDelete_Object = MibTableColumn
pmNewCfgPmirrDelete = _PmNewCfgPmirrDelete_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 8, 2, 1, 4),
    _PmNewCfgPmirrDelete_Type()
)
pmNewCfgPmirrDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmNewCfgPmirrDelete.setStatus("current")
_Stp_ObjectIdentity = ObjectIdentity
stp = _Stp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9)
)
_BosMstMstiInstanceTable_Object = MibTable
bosMstMstiInstanceTable = _BosMstMstiInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 1)
)
if mibBuilder.loadTexts:
    bosMstMstiInstanceTable.setStatus("current")
_BosMstMstiInstanceEntry_Object = MibTableRow
bosMstMstiInstanceEntry = _BosMstMstiInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 1, 1)
)
bosMstMstiInstanceEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosMstMstiInstanceIndex"),
)
if mibBuilder.loadTexts:
    bosMstMstiInstanceEntry.setStatus("current")


class _BosMstMstiInstanceIndex_Type(Integer32):
    """Custom type bosMstMstiInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BosMstMstiInstanceIndex_Type.__name__ = "Integer32"
_BosMstMstiInstanceIndex_Object = MibTableColumn
bosMstMstiInstanceIndex = _BosMstMstiInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 1, 1, 1),
    _BosMstMstiInstanceIndex_Type()
)
bosMstMstiInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosMstMstiInstanceIndex.setStatus("current")


class _BosMstMstiForceState_Type(Integer32):
    """Custom type bosMstMstiForceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_BosMstMstiForceState_Type.__name__ = "Integer32"
_BosMstMstiForceState_Object = MibTableColumn
bosMstMstiForceState = _BosMstMstiForceState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 1, 1, 2),
    _BosMstMstiForceState_Type()
)
bosMstMstiForceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstMstiForceState.setStatus("current")
_BosMstMstiForcePortStateBmp_Type = OctetString
_BosMstMstiForcePortStateBmp_Object = MibTableColumn
bosMstMstiForcePortStateBmp = _BosMstMstiForcePortStateBmp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 1, 1, 3),
    _BosMstMstiForcePortStateBmp_Type()
)
bosMstMstiForcePortStateBmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosMstMstiForcePortStateBmp.setStatus("current")
_BosStgCfgTable_Object = MibTable
bosStgCfgTable = _BosStgCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 2)
)
if mibBuilder.loadTexts:
    bosStgCfgTable.setStatus("current")
_BosStgCfgTableEntry_Object = MibTableRow
bosStgCfgTableEntry = _BosStgCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 2, 1)
)
bosStgCfgTableEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosStgCfgIndex"),
)
if mibBuilder.loadTexts:
    bosStgCfgTableEntry.setStatus("current")
_BosStgCfgIndex_Type = Integer32
_BosStgCfgIndex_Object = MibTableColumn
bosStgCfgIndex = _BosStgCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 2, 1, 1),
    _BosStgCfgIndex_Type()
)
bosStgCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosStgCfgIndex.setStatus("current")


class _BosStgCfgDefaultCfg_Type(Integer32):
    """Custom type bosStgCfgDefaultCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("defaultConfig", 1)
    )


_BosStgCfgDefaultCfg_Type.__name__ = "Integer32"
_BosStgCfgDefaultCfg_Object = MibTableColumn
bosStgCfgDefaultCfg = _BosStgCfgDefaultCfg_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 2, 1, 2),
    _BosStgCfgDefaultCfg_Type()
)
bosStgCfgDefaultCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosStgCfgDefaultCfg.setStatus("current")


class _BosMstCistDefaultCfg_Type(Integer32):
    """Custom type bosMstCistDefaultCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("default", 1)
    )


_BosMstCistDefaultCfg_Type.__name__ = "Integer32"
_BosMstCistDefaultCfg_Object = MibScalar
bosMstCistDefaultCfg = _BosMstCistDefaultCfg_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 3),
    _BosMstCistDefaultCfg_Type()
)
bosMstCistDefaultCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosMstCistDefaultCfg.setStatus("current")


class _BosStpMode_Type(Integer32):
    """Custom type bosStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 1),
          ("mstp", 2),
          ("pvrst", 3))
    )


_BosStpMode_Type.__name__ = "Integer32"
_BosStpMode_Object = MibScalar
bosStpMode = _BosStpMode_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 9, 4),
    _BosStpMode_Type()
)
bosStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosStpMode.setStatus("current")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10)
)
_BosIpRouteStatsHiwat_Type = Counter32
_BosIpRouteStatsHiwat_Object = MibScalar
bosIpRouteStatsHiwat = _BosIpRouteStatsHiwat_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 1),
    _BosIpRouteStatsHiwat_Type()
)
bosIpRouteStatsHiwat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpRouteStatsHiwat.setStatus("current")
_BosIpDefaultGatewayTable_Object = MibTable
bosIpDefaultGatewayTable = _BosIpDefaultGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 2)
)
if mibBuilder.loadTexts:
    bosIpDefaultGatewayTable.setStatus("current")
_BosIpDefaultGatewayEntry_Object = MibTableRow
bosIpDefaultGatewayEntry = _BosIpDefaultGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 2, 1)
)
bosIpDefaultGatewayEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosIpDefaultGatewayIndex"),
)
if mibBuilder.loadTexts:
    bosIpDefaultGatewayEntry.setStatus("current")


class _BosIpDefaultGatewayIndex_Type(Integer32):
    """Custom type bosIpDefaultGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BosIpDefaultGatewayIndex_Type.__name__ = "Integer32"
_BosIpDefaultGatewayIndex_Object = MibTableColumn
bosIpDefaultGatewayIndex = _BosIpDefaultGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 2, 1, 1),
    _BosIpDefaultGatewayIndex_Type()
)
bosIpDefaultGatewayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosIpDefaultGatewayIndex.setStatus("current")
_BosIpDefaultGatewayIpAddr_Type = IpAddress
_BosIpDefaultGatewayIpAddr_Object = MibTableColumn
bosIpDefaultGatewayIpAddr = _BosIpDefaultGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 2, 1, 2),
    _BosIpDefaultGatewayIpAddr_Type()
)
bosIpDefaultGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpDefaultGatewayIpAddr.setStatus("current")


class _BosIpDefaultGatewayStatus_Type(Integer32):
    """Custom type bosIpDefaultGatewayStatus based on Integer32"""
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


_BosIpDefaultGatewayStatus_Type.__name__ = "Integer32"
_BosIpDefaultGatewayStatus_Object = MibTableColumn
bosIpDefaultGatewayStatus = _BosIpDefaultGatewayStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 2, 1, 3),
    _BosIpDefaultGatewayStatus_Type()
)
bosIpDefaultGatewayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpDefaultGatewayStatus.setStatus("current")


class _BosIpDefaultGatewayState_Type(Integer32):
    """Custom type bosIpDefaultGatewayState based on Integer32"""
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


_BosIpDefaultGatewayState_Type.__name__ = "Integer32"
_BosIpDefaultGatewayState_Object = MibTableColumn
bosIpDefaultGatewayState = _BosIpDefaultGatewayState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 2, 1, 4),
    _BosIpDefaultGatewayState_Type()
)
bosIpDefaultGatewayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosIpDefaultGatewayState.setStatus("current")
_BosIpDefaultGatewayRowStatus_Type = RowStatus
_BosIpDefaultGatewayRowStatus_Object = MibTableColumn
bosIpDefaultGatewayRowStatus = _BosIpDefaultGatewayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 2, 1, 5),
    _BosIpDefaultGatewayRowStatus_Type()
)
bosIpDefaultGatewayRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosIpDefaultGatewayRowStatus.setStatus("current")
_ClearStats_ObjectIdentity = ObjectIdentity
clearStats = _ClearStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 3)
)


class _IpClearStats_Type(Integer32):
    """Custom type ipClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_IpClearStats_Type.__name__ = "Integer32"
_IpClearStats_Object = MibScalar
ipClearStats = _IpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 3, 1),
    _IpClearStats_Type()
)
ipClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipClearStats.setStatus("current")


class _ArpClearStats_Type(Integer32):
    """Custom type arpClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_ArpClearStats_Type.__name__ = "Integer32"
_ArpClearStats_Object = MibScalar
arpClearStats = _ArpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 3, 2),
    _ArpClearStats_Type()
)
arpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpClearStats.setStatus("current")


class _DnsClearStats_Type(Integer32):
    """Custom type dnsClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_DnsClearStats_Type.__name__ = "Integer32"
_DnsClearStats_Object = MibScalar
dnsClearStats = _DnsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 3, 3),
    _DnsClearStats_Type()
)
dnsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsClearStats.setStatus("current")


class _IcmpClearStats_Type(Integer32):
    """Custom type icmpClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_IcmpClearStats_Type.__name__ = "Integer32"
_IcmpClearStats_Object = MibScalar
icmpClearStats = _IcmpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 3, 4),
    _IcmpClearStats_Type()
)
icmpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icmpClearStats.setStatus("current")


class _TcpClearStats_Type(Integer32):
    """Custom type tcpClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_TcpClearStats_Type.__name__ = "Integer32"
_TcpClearStats_Object = MibScalar
tcpClearStats = _TcpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 3, 5),
    _TcpClearStats_Type()
)
tcpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpClearStats.setStatus("current")


class _UdpClearStats_Type(Integer32):
    """Custom type udpClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_UdpClearStats_Type.__name__ = "Integer32"
_UdpClearStats_Object = MibScalar
udpClearStats = _UdpClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 3, 6),
    _UdpClearStats_Type()
)
udpClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpClearStats.setStatus("current")


class _RouteClearStats_Type(Integer32):
    """Custom type routeClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 2))
    )


_RouteClearStats_Type.__name__ = "Integer32"
_RouteClearStats_Object = MibScalar
routeClearStats = _RouteClearStats_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 3, 7),
    _RouteClearStats_Type()
)
routeClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeClearStats.setStatus("current")
_IpStaticArpCfg_ObjectIdentity = ObjectIdentity
ipStaticArpCfg = _IpStaticArpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4)
)
_IpStaticArpTableMaxSize_Type = Integer32
_IpStaticArpTableMaxSize_Object = MibScalar
ipStaticArpTableMaxSize = _IpStaticArpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 1),
    _IpStaticArpTableMaxSize_Type()
)
ipStaticArpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStaticArpTableMaxSize.setStatus("current")
_IpCurCfgStaticArpTable_Object = MibTable
ipCurCfgStaticArpTable = _IpCurCfgStaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 2)
)
if mibBuilder.loadTexts:
    ipCurCfgStaticArpTable.setStatus("current")
_IpCurCfgStaticArpEntry_Object = MibTableRow
ipCurCfgStaticArpEntry = _IpCurCfgStaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 2, 1)
)
ipCurCfgStaticArpEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "ipCurCfgStaticArpInterface"),
    (0, "BLADEOS-BASE-MIB", "ipCurCfgStaticArpIp"),
)
if mibBuilder.loadTexts:
    ipCurCfgStaticArpEntry.setStatus("current")
_IpCurCfgStaticArpInterface_Type = Integer32
_IpCurCfgStaticArpInterface_Object = MibTableColumn
ipCurCfgStaticArpInterface = _IpCurCfgStaticArpInterface_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 2, 1, 1),
    _IpCurCfgStaticArpInterface_Type()
)
ipCurCfgStaticArpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpInterface.setStatus("current")
_IpCurCfgStaticArpIp_Type = IpAddress
_IpCurCfgStaticArpIp_Object = MibTableColumn
ipCurCfgStaticArpIp = _IpCurCfgStaticArpIp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 2, 1, 2),
    _IpCurCfgStaticArpIp_Type()
)
ipCurCfgStaticArpIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpIp.setStatus("current")
_IpCurCfgStaticArpMAC_Type = DisplayString
_IpCurCfgStaticArpMAC_Object = MibTableColumn
ipCurCfgStaticArpMAC = _IpCurCfgStaticArpMAC_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 2, 1, 3),
    _IpCurCfgStaticArpMAC_Type()
)
ipCurCfgStaticArpMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpMAC.setStatus("current")


class _IpCurCfgStaticArpAction_Type(Integer32):
    """Custom type ipCurCfgStaticArpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_IpCurCfgStaticArpAction_Type.__name__ = "Integer32"
_IpCurCfgStaticArpAction_Object = MibTableColumn
ipCurCfgStaticArpAction = _IpCurCfgStaticArpAction_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 2, 1, 4),
    _IpCurCfgStaticArpAction_Type()
)
ipCurCfgStaticArpAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCurCfgStaticArpAction.setStatus("current")
_IpNewCfgStaticArpTable_Object = MibTable
ipNewCfgStaticArpTable = _IpNewCfgStaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 3)
)
if mibBuilder.loadTexts:
    ipNewCfgStaticArpTable.setStatus("current")
_IpNewCfgStaticArpEntry_Object = MibTableRow
ipNewCfgStaticArpEntry = _IpNewCfgStaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 3, 1)
)
ipNewCfgStaticArpEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "ipNewCfgStaticArpEntryIndex"),
)
if mibBuilder.loadTexts:
    ipNewCfgStaticArpEntry.setStatus("current")
_IpNewCfgStaticArpEntryIndex_Type = Integer32
_IpNewCfgStaticArpEntryIndex_Object = MibTableColumn
ipNewCfgStaticArpEntryIndex = _IpNewCfgStaticArpEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 3, 1, 1),
    _IpNewCfgStaticArpEntryIndex_Type()
)
ipNewCfgStaticArpEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpEntryIndex.setStatus("current")
_IpNewCfgStaticArpInterface_Type = Integer32
_IpNewCfgStaticArpInterface_Object = MibTableColumn
ipNewCfgStaticArpInterface = _IpNewCfgStaticArpInterface_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 3, 1, 2),
    _IpNewCfgStaticArpInterface_Type()
)
ipNewCfgStaticArpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpInterface.setStatus("current")
_IpNewCfgStaticArpIp_Type = IpAddress
_IpNewCfgStaticArpIp_Object = MibTableColumn
ipNewCfgStaticArpIp = _IpNewCfgStaticArpIp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 3, 1, 3),
    _IpNewCfgStaticArpIp_Type()
)
ipNewCfgStaticArpIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpIp.setStatus("current")
_IpNewCfgStaticArpMAC_Type = DisplayString
_IpNewCfgStaticArpMAC_Object = MibTableColumn
ipNewCfgStaticArpMAC = _IpNewCfgStaticArpMAC_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 3, 1, 4),
    _IpNewCfgStaticArpMAC_Type()
)
ipNewCfgStaticArpMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipNewCfgStaticArpMAC.setStatus("current")


class _IpStaticArpClearAll_Type(Integer32):
    """Custom type ipStaticArpClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_IpStaticArpClearAll_Type.__name__ = "Integer32"
_IpStaticArpClearAll_Object = MibScalar
ipStaticArpClearAll = _IpStaticArpClearAll_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 4, 4),
    _IpStaticArpClearAll_Type()
)
ipStaticArpClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStaticArpClearAll.setStatus("current")
_ArpCfg_ObjectIdentity = ObjectIdentity
arpCfg = _ArpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 5)
)


class _ArpCfgReARPPeriod_Type(Integer32):
    """Custom type arpCfgReARPPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_ArpCfgReARPPeriod_Type.__name__ = "Integer32"
_ArpCfgReARPPeriod_Object = MibScalar
arpCfgReARPPeriod = _ArpCfgReARPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 10, 5, 1),
    _ArpCfgReARPPeriod_Type()
)
arpCfgReARPPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpCfgReARPPeriod.setStatus("current")
_Snmpv3_ObjectIdentity = ObjectIdentity
snmpv3 = _Snmpv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11)
)
_BosUsmUser_ObjectIdentity = ObjectIdentity
bosUsmUser = _BosUsmUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1)
)
_BosUsmUserTable_Object = MibTable
bosUsmUserTable = _BosUsmUserTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1)
)
if mibBuilder.loadTexts:
    bosUsmUserTable.setStatus("current")
_BosUsmUserEntry_Object = MibTableRow
bosUsmUserEntry = _BosUsmUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1)
)
bosUsmUserEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosUsmUserTableIndex"),
)
if mibBuilder.loadTexts:
    bosUsmUserEntry.setStatus("current")
_BosUsmUserTableIndex_Type = Unsigned32
_BosUsmUserTableIndex_Object = MibTableColumn
bosUsmUserTableIndex = _BosUsmUserTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 1),
    _BosUsmUserTableIndex_Type()
)
bosUsmUserTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosUsmUserTableIndex.setStatus("current")


class _BosUsmUserName_Type(SnmpAdminString):
    """Custom type bosUsmUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BosUsmUserName_Type.__name__ = "SnmpAdminString"
_BosUsmUserName_Object = MibTableColumn
bosUsmUserName = _BosUsmUserName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 2),
    _BosUsmUserName_Type()
)
bosUsmUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosUsmUserName.setStatus("current")
_BosUsmUserSecurityName_Type = SnmpAdminString
_BosUsmUserSecurityName_Object = MibTableColumn
bosUsmUserSecurityName = _BosUsmUserSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 3),
    _BosUsmUserSecurityName_Type()
)
bosUsmUserSecurityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosUsmUserSecurityName.setStatus("current")
_BosUsmUserCloneFrom_Type = RowPointer
_BosUsmUserCloneFrom_Object = MibTableColumn
bosUsmUserCloneFrom = _BosUsmUserCloneFrom_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 4),
    _BosUsmUserCloneFrom_Type()
)
bosUsmUserCloneFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosUsmUserCloneFrom.setStatus("current")


class _BosUsmUserAuthProtocol_Type(AutonomousType):
    """Custom type bosUsmUserAuthProtocol based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 6, 3, 10, 1, 1, 1)


_BosUsmUserAuthProtocol_Type.__name__ = "AutonomousType"
_BosUsmUserAuthProtocol_Object = MibTableColumn
bosUsmUserAuthProtocol = _BosUsmUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 5),
    _BosUsmUserAuthProtocol_Type()
)
bosUsmUserAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosUsmUserAuthProtocol.setStatus("current")


class _BosUsmUserAuthKeyChange_Type(BosKeyChange):
    """Custom type bosUsmUserAuthKeyChange based on BosKeyChange"""
    defaultHexValue = ""


_BosUsmUserAuthKeyChange_Type.__name__ = "BosKeyChange"
_BosUsmUserAuthKeyChange_Object = MibTableColumn
bosUsmUserAuthKeyChange = _BosUsmUserAuthKeyChange_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 6),
    _BosUsmUserAuthKeyChange_Type()
)
bosUsmUserAuthKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosUsmUserAuthKeyChange.setStatus("current")


class _BosUsmUserOwnAuthKeyChange_Type(BosKeyChange):
    """Custom type bosUsmUserOwnAuthKeyChange based on BosKeyChange"""
    defaultHexValue = ""


_BosUsmUserOwnAuthKeyChange_Type.__name__ = "BosKeyChange"
_BosUsmUserOwnAuthKeyChange_Object = MibTableColumn
bosUsmUserOwnAuthKeyChange = _BosUsmUserOwnAuthKeyChange_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 7),
    _BosUsmUserOwnAuthKeyChange_Type()
)
bosUsmUserOwnAuthKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosUsmUserOwnAuthKeyChange.setStatus("current")


class _BosUsmUserPrivProtocol_Type(AutonomousType):
    """Custom type bosUsmUserPrivProtocol based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 6, 3, 10, 1, 2, 1)


_BosUsmUserPrivProtocol_Type.__name__ = "AutonomousType"
_BosUsmUserPrivProtocol_Object = MibTableColumn
bosUsmUserPrivProtocol = _BosUsmUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 8),
    _BosUsmUserPrivProtocol_Type()
)
bosUsmUserPrivProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosUsmUserPrivProtocol.setStatus("current")


class _BosUsmUserPrivKeyChange_Type(BosKeyChange):
    """Custom type bosUsmUserPrivKeyChange based on BosKeyChange"""
    defaultHexValue = ""


_BosUsmUserPrivKeyChange_Type.__name__ = "BosKeyChange"
_BosUsmUserPrivKeyChange_Object = MibTableColumn
bosUsmUserPrivKeyChange = _BosUsmUserPrivKeyChange_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 9),
    _BosUsmUserPrivKeyChange_Type()
)
bosUsmUserPrivKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosUsmUserPrivKeyChange.setStatus("current")


class _BosUsmUserOwnPrivKeyChange_Type(BosKeyChange):
    """Custom type bosUsmUserOwnPrivKeyChange based on BosKeyChange"""
    defaultHexValue = ""


_BosUsmUserOwnPrivKeyChange_Type.__name__ = "BosKeyChange"
_BosUsmUserOwnPrivKeyChange_Object = MibTableColumn
bosUsmUserOwnPrivKeyChange = _BosUsmUserOwnPrivKeyChange_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 10),
    _BosUsmUserOwnPrivKeyChange_Type()
)
bosUsmUserOwnPrivKeyChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosUsmUserOwnPrivKeyChange.setStatus("current")


class _BosUsmUserPublic_Type(OctetString):
    """Custom type bosUsmUserPublic based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BosUsmUserPublic_Type.__name__ = "OctetString"
_BosUsmUserPublic_Object = MibTableColumn
bosUsmUserPublic = _BosUsmUserPublic_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 11),
    _BosUsmUserPublic_Type()
)
bosUsmUserPublic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosUsmUserPublic.setStatus("current")


class _BosUsmUserStorageType_Type(StorageType):
    """Custom type bosUsmUserStorageType based on StorageType"""
    defaultValue = 3


_BosUsmUserStorageType_Type.__name__ = "StorageType"
_BosUsmUserStorageType_Object = MibTableColumn
bosUsmUserStorageType = _BosUsmUserStorageType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 12),
    _BosUsmUserStorageType_Type()
)
bosUsmUserStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosUsmUserStorageType.setStatus("current")
_BosUsmUserStatus_Type = RowStatus
_BosUsmUserStatus_Object = MibTableColumn
bosUsmUserStatus = _BosUsmUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 1, 1, 1, 13),
    _BosUsmUserStatus_Type()
)
bosUsmUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosUsmUserStatus.setStatus("current")
_BosVacmObjects_ObjectIdentity = ObjectIdentity
bosVacmObjects = _BosVacmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2)
)
_BosVacmSecurityToGroupTable_Object = MibTable
bosVacmSecurityToGroupTable = _BosVacmSecurityToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 1)
)
if mibBuilder.loadTexts:
    bosVacmSecurityToGroupTable.setStatus("current")
_BosVacmSecurityToGroupEntry_Object = MibTableRow
bosVacmSecurityToGroupEntry = _BosVacmSecurityToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 1, 1)
)
bosVacmSecurityToGroupEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosVacmSecurityToGroupTableIndex"),
)
if mibBuilder.loadTexts:
    bosVacmSecurityToGroupEntry.setStatus("current")
_BosVacmSecurityToGroupTableIndex_Type = Unsigned32
_BosVacmSecurityToGroupTableIndex_Object = MibTableColumn
bosVacmSecurityToGroupTableIndex = _BosVacmSecurityToGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 1, 1, 1),
    _BosVacmSecurityToGroupTableIndex_Type()
)
bosVacmSecurityToGroupTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosVacmSecurityToGroupTableIndex.setStatus("current")


class _BosVacmGroupName_Type(SnmpAdminString):
    """Custom type bosVacmGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BosVacmGroupName_Type.__name__ = "SnmpAdminString"
_BosVacmGroupName_Object = MibTableColumn
bosVacmGroupName = _BosVacmGroupName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 1, 1, 2),
    _BosVacmGroupName_Type()
)
bosVacmGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmGroupName.setStatus("current")


class _BosVacmSecurityToGroupStorageType_Type(StorageType):
    """Custom type bosVacmSecurityToGroupStorageType based on StorageType"""
    defaultValue = 3


_BosVacmSecurityToGroupStorageType_Type.__name__ = "StorageType"
_BosVacmSecurityToGroupStorageType_Object = MibTableColumn
bosVacmSecurityToGroupStorageType = _BosVacmSecurityToGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 1, 1, 3),
    _BosVacmSecurityToGroupStorageType_Type()
)
bosVacmSecurityToGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmSecurityToGroupStorageType.setStatus("current")
_BosVacmSecurityToGroupStatus_Type = RowStatus
_BosVacmSecurityToGroupStatus_Object = MibTableColumn
bosVacmSecurityToGroupStatus = _BosVacmSecurityToGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 1, 1, 4),
    _BosVacmSecurityToGroupStatus_Type()
)
bosVacmSecurityToGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmSecurityToGroupStatus.setStatus("current")
_BosVacmAccessTable_Object = MibTable
bosVacmAccessTable = _BosVacmAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 2)
)
if mibBuilder.loadTexts:
    bosVacmAccessTable.setStatus("current")
_BosVacmAccessEntry_Object = MibTableRow
bosVacmAccessEntry = _BosVacmAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 2, 1)
)
bosVacmAccessEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosVacmAccessTableIndex"),
)
if mibBuilder.loadTexts:
    bosVacmAccessEntry.setStatus("current")
_BosVacmAccessTableIndex_Type = Unsigned32
_BosVacmAccessTableIndex_Object = MibTableColumn
bosVacmAccessTableIndex = _BosVacmAccessTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 2, 1, 1),
    _BosVacmAccessTableIndex_Type()
)
bosVacmAccessTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosVacmAccessTableIndex.setStatus("current")


class _BosVacmAccessContextMatch_Type(Integer32):
    """Custom type bosVacmAccessContextMatch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exact", 1),
          ("prefix", 2))
    )


_BosVacmAccessContextMatch_Type.__name__ = "Integer32"
_BosVacmAccessContextMatch_Object = MibTableColumn
bosVacmAccessContextMatch = _BosVacmAccessContextMatch_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 2, 1, 2),
    _BosVacmAccessContextMatch_Type()
)
bosVacmAccessContextMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmAccessContextMatch.setStatus("current")


class _BosVacmAccessReadViewName_Type(SnmpAdminString):
    """Custom type bosVacmAccessReadViewName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BosVacmAccessReadViewName_Type.__name__ = "SnmpAdminString"
_BosVacmAccessReadViewName_Object = MibTableColumn
bosVacmAccessReadViewName = _BosVacmAccessReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 2, 1, 3),
    _BosVacmAccessReadViewName_Type()
)
bosVacmAccessReadViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmAccessReadViewName.setStatus("current")


class _BosVacmAccessWriteViewName_Type(SnmpAdminString):
    """Custom type bosVacmAccessWriteViewName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BosVacmAccessWriteViewName_Type.__name__ = "SnmpAdminString"
_BosVacmAccessWriteViewName_Object = MibTableColumn
bosVacmAccessWriteViewName = _BosVacmAccessWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 2, 1, 4),
    _BosVacmAccessWriteViewName_Type()
)
bosVacmAccessWriteViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmAccessWriteViewName.setStatus("current")


class _BosVacmAccessNotifyViewName_Type(SnmpAdminString):
    """Custom type bosVacmAccessNotifyViewName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BosVacmAccessNotifyViewName_Type.__name__ = "SnmpAdminString"
_BosVacmAccessNotifyViewName_Object = MibTableColumn
bosVacmAccessNotifyViewName = _BosVacmAccessNotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 2, 1, 5),
    _BosVacmAccessNotifyViewName_Type()
)
bosVacmAccessNotifyViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmAccessNotifyViewName.setStatus("current")


class _BosVacmAccessStorageType_Type(StorageType):
    """Custom type bosVacmAccessStorageType based on StorageType"""
    defaultValue = 3


_BosVacmAccessStorageType_Type.__name__ = "StorageType"
_BosVacmAccessStorageType_Object = MibTableColumn
bosVacmAccessStorageType = _BosVacmAccessStorageType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 2, 1, 6),
    _BosVacmAccessStorageType_Type()
)
bosVacmAccessStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmAccessStorageType.setStatus("current")
_BosVacmAccessStatus_Type = RowStatus
_BosVacmAccessStatus_Object = MibTableColumn
bosVacmAccessStatus = _BosVacmAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 2, 1, 7),
    _BosVacmAccessStatus_Type()
)
bosVacmAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmAccessStatus.setStatus("current")
_BosVacmViewTreeFamilyTable_Object = MibTable
bosVacmViewTreeFamilyTable = _BosVacmViewTreeFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 3)
)
if mibBuilder.loadTexts:
    bosVacmViewTreeFamilyTable.setStatus("current")
_BosVacmViewTreeFamilyEntry_Object = MibTableRow
bosVacmViewTreeFamilyEntry = _BosVacmViewTreeFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 3, 1)
)
bosVacmViewTreeFamilyEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosVacmViewTreeFamilyTableIndex"),
)
if mibBuilder.loadTexts:
    bosVacmViewTreeFamilyEntry.setStatus("current")
_BosVacmViewTreeFamilyTableIndex_Type = Unsigned32
_BosVacmViewTreeFamilyTableIndex_Object = MibTableColumn
bosVacmViewTreeFamilyTableIndex = _BosVacmViewTreeFamilyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 3, 1, 1),
    _BosVacmViewTreeFamilyTableIndex_Type()
)
bosVacmViewTreeFamilyTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosVacmViewTreeFamilyTableIndex.setStatus("current")


class _BosVacmViewTreeFamilyMask_Type(OctetString):
    """Custom type bosVacmViewTreeFamilyMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BosVacmViewTreeFamilyMask_Type.__name__ = "OctetString"
_BosVacmViewTreeFamilyMask_Object = MibTableColumn
bosVacmViewTreeFamilyMask = _BosVacmViewTreeFamilyMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 3, 1, 2),
    _BosVacmViewTreeFamilyMask_Type()
)
bosVacmViewTreeFamilyMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmViewTreeFamilyMask.setStatus("current")


class _BosVacmViewTreeFamilyType_Type(Integer32):
    """Custom type bosVacmViewTreeFamilyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("included", 1),
          ("excluded", 2))
    )


_BosVacmViewTreeFamilyType_Type.__name__ = "Integer32"
_BosVacmViewTreeFamilyType_Object = MibTableColumn
bosVacmViewTreeFamilyType = _BosVacmViewTreeFamilyType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 3, 1, 3),
    _BosVacmViewTreeFamilyType_Type()
)
bosVacmViewTreeFamilyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmViewTreeFamilyType.setStatus("current")


class _BosVacmViewTreeFamilyStorageType_Type(StorageType):
    """Custom type bosVacmViewTreeFamilyStorageType based on StorageType"""
    defaultValue = 3


_BosVacmViewTreeFamilyStorageType_Type.__name__ = "StorageType"
_BosVacmViewTreeFamilyStorageType_Object = MibTableColumn
bosVacmViewTreeFamilyStorageType = _BosVacmViewTreeFamilyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 3, 1, 4),
    _BosVacmViewTreeFamilyStorageType_Type()
)
bosVacmViewTreeFamilyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmViewTreeFamilyStorageType.setStatus("current")
_BosVacmViewTreeFamilyStatus_Type = RowStatus
_BosVacmViewTreeFamilyStatus_Object = MibTableColumn
bosVacmViewTreeFamilyStatus = _BosVacmViewTreeFamilyStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 2, 3, 1, 5),
    _BosVacmViewTreeFamilyStatus_Type()
)
bosVacmViewTreeFamilyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosVacmViewTreeFamilyStatus.setStatus("current")
_BosSnmpTargetObjects_ObjectIdentity = ObjectIdentity
bosSnmpTargetObjects = _BosSnmpTargetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3)
)
_BossnmpTargetAddrTable_Object = MibTable
bossnmpTargetAddrTable = _BossnmpTargetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1)
)
if mibBuilder.loadTexts:
    bossnmpTargetAddrTable.setStatus("current")
_BosSnmpTargetAddrEntry_Object = MibTableRow
bosSnmpTargetAddrEntry = _BosSnmpTargetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1, 1)
)
bosSnmpTargetAddrEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bossnmpTargetTableIndex"),
)
if mibBuilder.loadTexts:
    bosSnmpTargetAddrEntry.setStatus("current")
_BossnmpTargetTableIndex_Type = Unsigned32
_BossnmpTargetTableIndex_Object = MibTableColumn
bossnmpTargetTableIndex = _BossnmpTargetTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1, 1, 1),
    _BossnmpTargetTableIndex_Type()
)
bossnmpTargetTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bossnmpTargetTableIndex.setStatus("current")
_BossnmpTargetAddrTDomain_Type = TDomain
_BossnmpTargetAddrTDomain_Object = MibTableColumn
bossnmpTargetAddrTDomain = _BossnmpTargetAddrTDomain_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1, 1, 2),
    _BossnmpTargetAddrTDomain_Type()
)
bossnmpTargetAddrTDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bossnmpTargetAddrTDomain.setStatus("current")
_BossnmpTargetAddrTAddress_Type = TAddress
_BossnmpTargetAddrTAddress_Object = MibTableColumn
bossnmpTargetAddrTAddress = _BossnmpTargetAddrTAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1, 1, 3),
    _BossnmpTargetAddrTAddress_Type()
)
bossnmpTargetAddrTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bossnmpTargetAddrTAddress.setStatus("current")


class _BossnmpTargetAddrTimeout_Type(TimeInterval):
    """Custom type bossnmpTargetAddrTimeout based on TimeInterval"""
    defaultValue = 1500


_BossnmpTargetAddrTimeout_Type.__name__ = "TimeInterval"
_BossnmpTargetAddrTimeout_Object = MibTableColumn
bossnmpTargetAddrTimeout = _BossnmpTargetAddrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1, 1, 4),
    _BossnmpTargetAddrTimeout_Type()
)
bossnmpTargetAddrTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bossnmpTargetAddrTimeout.setStatus("current")


class _BossnmpTargetAddrRetryCount_Type(Integer32):
    """Custom type bossnmpTargetAddrRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BossnmpTargetAddrRetryCount_Type.__name__ = "Integer32"
_BossnmpTargetAddrRetryCount_Object = MibTableColumn
bossnmpTargetAddrRetryCount = _BossnmpTargetAddrRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1, 1, 5),
    _BossnmpTargetAddrRetryCount_Type()
)
bossnmpTargetAddrRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bossnmpTargetAddrRetryCount.setStatus("current")


class _BossnmpTargetAddrTagList_Type(SnmpTagList):
    """Custom type bossnmpTargetAddrTagList based on SnmpTagList"""
    defaultValue = OctetString("")


_BossnmpTargetAddrTagList_Type.__name__ = "SnmpTagList"
_BossnmpTargetAddrTagList_Object = MibTableColumn
bossnmpTargetAddrTagList = _BossnmpTargetAddrTagList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1, 1, 6),
    _BossnmpTargetAddrTagList_Type()
)
bossnmpTargetAddrTagList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bossnmpTargetAddrTagList.setStatus("current")


class _BossnmpTargetAddrParams_Type(SnmpAdminString):
    """Custom type bossnmpTargetAddrParams based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BossnmpTargetAddrParams_Type.__name__ = "SnmpAdminString"
_BossnmpTargetAddrParams_Object = MibTableColumn
bossnmpTargetAddrParams = _BossnmpTargetAddrParams_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1, 1, 7),
    _BossnmpTargetAddrParams_Type()
)
bossnmpTargetAddrParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bossnmpTargetAddrParams.setStatus("current")


class _BossnmpTargetAddrStorageType_Type(StorageType):
    """Custom type bossnmpTargetAddrStorageType based on StorageType"""
    defaultValue = 3


_BossnmpTargetAddrStorageType_Type.__name__ = "StorageType"
_BossnmpTargetAddrStorageType_Object = MibTableColumn
bossnmpTargetAddrStorageType = _BossnmpTargetAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1, 1, 8),
    _BossnmpTargetAddrStorageType_Type()
)
bossnmpTargetAddrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bossnmpTargetAddrStorageType.setStatus("current")
_BossnmpTargetAddrRowStatus_Type = RowStatus
_BossnmpTargetAddrRowStatus_Object = MibTableColumn
bossnmpTargetAddrRowStatus = _BossnmpTargetAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 1, 1, 9),
    _BossnmpTargetAddrRowStatus_Type()
)
bossnmpTargetAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bossnmpTargetAddrRowStatus.setStatus("current")
_BosSnmpTargetParamsTable_Object = MibTable
bosSnmpTargetParamsTable = _BosSnmpTargetParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 2)
)
if mibBuilder.loadTexts:
    bosSnmpTargetParamsTable.setStatus("current")
_BosSnmpTargetParamsEntry_Object = MibTableRow
bosSnmpTargetParamsEntry = _BosSnmpTargetParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 2, 1)
)
bosSnmpTargetParamsEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnmpTargetParamsTableIndex"),
)
if mibBuilder.loadTexts:
    bosSnmpTargetParamsEntry.setStatus("current")
_BosSnmpTargetParamsTableIndex_Type = Unsigned32
_BosSnmpTargetParamsTableIndex_Object = MibTableColumn
bosSnmpTargetParamsTableIndex = _BosSnmpTargetParamsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 2, 1, 1),
    _BosSnmpTargetParamsTableIndex_Type()
)
bosSnmpTargetParamsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnmpTargetParamsTableIndex.setStatus("current")
_BosSnmpTargetParamsMPModel_Type = SnmpMessageProcessingModel
_BosSnmpTargetParamsMPModel_Object = MibTableColumn
bosSnmpTargetParamsMPModel = _BosSnmpTargetParamsMPModel_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 2, 1, 2),
    _BosSnmpTargetParamsMPModel_Type()
)
bosSnmpTargetParamsMPModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpTargetParamsMPModel.setStatus("current")
_BosSnmpTargetParamsSecurityModel_Type = SnmpSecurityModel
_BosSnmpTargetParamsSecurityModel_Object = MibTableColumn
bosSnmpTargetParamsSecurityModel = _BosSnmpTargetParamsSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 2, 1, 3),
    _BosSnmpTargetParamsSecurityModel_Type()
)
bosSnmpTargetParamsSecurityModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpTargetParamsSecurityModel.setStatus("current")
_BosSnmpTargetParamsSecurityName_Type = SnmpAdminString
_BosSnmpTargetParamsSecurityName_Object = MibTableColumn
bosSnmpTargetParamsSecurityName = _BosSnmpTargetParamsSecurityName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 2, 1, 4),
    _BosSnmpTargetParamsSecurityName_Type()
)
bosSnmpTargetParamsSecurityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpTargetParamsSecurityName.setStatus("current")
_BosSnmpTargetParamsSecurityLevel_Type = SnmpSecurityLevel
_BosSnmpTargetParamsSecurityLevel_Object = MibTableColumn
bosSnmpTargetParamsSecurityLevel = _BosSnmpTargetParamsSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 2, 1, 5),
    _BosSnmpTargetParamsSecurityLevel_Type()
)
bosSnmpTargetParamsSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpTargetParamsSecurityLevel.setStatus("current")


class _BosSnmpTargetParamsStorageType_Type(StorageType):
    """Custom type bosSnmpTargetParamsStorageType based on StorageType"""
    defaultValue = 3


_BosSnmpTargetParamsStorageType_Type.__name__ = "StorageType"
_BosSnmpTargetParamsStorageType_Object = MibTableColumn
bosSnmpTargetParamsStorageType = _BosSnmpTargetParamsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 2, 1, 6),
    _BosSnmpTargetParamsStorageType_Type()
)
bosSnmpTargetParamsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpTargetParamsStorageType.setStatus("current")
_BosSnmpTargetParamsRowStatus_Type = RowStatus
_BosSnmpTargetParamsRowStatus_Object = MibTableColumn
bosSnmpTargetParamsRowStatus = _BosSnmpTargetParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 3, 2, 1, 7),
    _BosSnmpTargetParamsRowStatus_Type()
)
bosSnmpTargetParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpTargetParamsRowStatus.setStatus("current")
_BosSnmpNotifyObjects_ObjectIdentity = ObjectIdentity
bosSnmpNotifyObjects = _BosSnmpNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 4)
)
_BosSnmpNotifyTable_Object = MibTable
bosSnmpNotifyTable = _BosSnmpNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 4, 1)
)
if mibBuilder.loadTexts:
    bosSnmpNotifyTable.setStatus("current")
_BosSnmpNotifyEntry_Object = MibTableRow
bosSnmpNotifyEntry = _BosSnmpNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 4, 1, 1)
)
bosSnmpNotifyEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnmpNotifyTableIndex"),
)
if mibBuilder.loadTexts:
    bosSnmpNotifyEntry.setStatus("current")
_BosSnmpNotifyTableIndex_Type = Unsigned32
_BosSnmpNotifyTableIndex_Object = MibTableColumn
bosSnmpNotifyTableIndex = _BosSnmpNotifyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 4, 1, 1, 1),
    _BosSnmpNotifyTableIndex_Type()
)
bosSnmpNotifyTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnmpNotifyTableIndex.setStatus("current")


class _BosSnmpNotifyTag_Type(SnmpTagValue):
    """Custom type bosSnmpNotifyTag based on SnmpTagValue"""
    defaultValue = OctetString("")


_BosSnmpNotifyTag_Type.__name__ = "SnmpTagValue"
_BosSnmpNotifyTag_Object = MibTableColumn
bosSnmpNotifyTag = _BosSnmpNotifyTag_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 4, 1, 1, 2),
    _BosSnmpNotifyTag_Type()
)
bosSnmpNotifyTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpNotifyTag.setStatus("current")


class _BosSnmpNotifyType_Type(Integer32):
    """Custom type bosSnmpNotifyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trap", 1),
          ("inform", 2))
    )


_BosSnmpNotifyType_Type.__name__ = "Integer32"
_BosSnmpNotifyType_Object = MibTableColumn
bosSnmpNotifyType = _BosSnmpNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 4, 1, 1, 3),
    _BosSnmpNotifyType_Type()
)
bosSnmpNotifyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpNotifyType.setStatus("current")


class _BosSnmpNotifyStorageType_Type(StorageType):
    """Custom type bosSnmpNotifyStorageType based on StorageType"""
    defaultValue = 3


_BosSnmpNotifyStorageType_Type.__name__ = "StorageType"
_BosSnmpNotifyStorageType_Object = MibTableColumn
bosSnmpNotifyStorageType = _BosSnmpNotifyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 4, 1, 1, 4),
    _BosSnmpNotifyStorageType_Type()
)
bosSnmpNotifyStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpNotifyStorageType.setStatus("current")
_BosSnmpNotifyRowStatus_Type = RowStatus
_BosSnmpNotifyRowStatus_Object = MibTableColumn
bosSnmpNotifyRowStatus = _BosSnmpNotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 4, 1, 1, 5),
    _BosSnmpNotifyRowStatus_Type()
)
bosSnmpNotifyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpNotifyRowStatus.setStatus("current")
_BosSnmpCommunityObjects_ObjectIdentity = ObjectIdentity
bosSnmpCommunityObjects = _BosSnmpCommunityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5)
)
_BosSnmpCommunityTable_Object = MibTable
bosSnmpCommunityTable = _BosSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5, 1)
)
if mibBuilder.loadTexts:
    bosSnmpCommunityTable.setStatus("current")
_BosSnmpCommunityEntry_Object = MibTableRow
bosSnmpCommunityEntry = _BosSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5, 1, 1)
)
bosSnmpCommunityEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnmpCommunityTableIndex"),
)
if mibBuilder.loadTexts:
    bosSnmpCommunityEntry.setStatus("current")
_BosSnmpCommunityTableIndex_Type = Unsigned32
_BosSnmpCommunityTableIndex_Object = MibTableColumn
bosSnmpCommunityTableIndex = _BosSnmpCommunityTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5, 1, 1, 1),
    _BosSnmpCommunityTableIndex_Type()
)
bosSnmpCommunityTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnmpCommunityTableIndex.setStatus("current")
_BosSnmpCommunityName_Type = OctetString
_BosSnmpCommunityName_Object = MibTableColumn
bosSnmpCommunityName = _BosSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5, 1, 1, 2),
    _BosSnmpCommunityName_Type()
)
bosSnmpCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpCommunityName.setStatus("current")


class _BosSnmpCommunitySecurityName_Type(SnmpAdminString):
    """Custom type bosSnmpCommunitySecurityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BosSnmpCommunitySecurityName_Type.__name__ = "SnmpAdminString"
_BosSnmpCommunitySecurityName_Object = MibTableColumn
bosSnmpCommunitySecurityName = _BosSnmpCommunitySecurityName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5, 1, 1, 3),
    _BosSnmpCommunitySecurityName_Type()
)
bosSnmpCommunitySecurityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpCommunitySecurityName.setStatus("current")
_BosSnmpCommunityContextEngineID_Type = SnmpEngineID
_BosSnmpCommunityContextEngineID_Object = MibTableColumn
bosSnmpCommunityContextEngineID = _BosSnmpCommunityContextEngineID_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5, 1, 1, 4),
    _BosSnmpCommunityContextEngineID_Type()
)
bosSnmpCommunityContextEngineID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpCommunityContextEngineID.setStatus("current")


class _BosSnmpCommunityContextName_Type(SnmpAdminString):
    """Custom type bosSnmpCommunityContextName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BosSnmpCommunityContextName_Type.__name__ = "SnmpAdminString"
_BosSnmpCommunityContextName_Object = MibTableColumn
bosSnmpCommunityContextName = _BosSnmpCommunityContextName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5, 1, 1, 5),
    _BosSnmpCommunityContextName_Type()
)
bosSnmpCommunityContextName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpCommunityContextName.setStatus("current")


class _BosSnmpCommunityTransportTag_Type(SnmpTagValue):
    """Custom type bosSnmpCommunityTransportTag based on SnmpTagValue"""
    defaultHexValue = ""


_BosSnmpCommunityTransportTag_Type.__name__ = "SnmpTagValue"
_BosSnmpCommunityTransportTag_Object = MibTableColumn
bosSnmpCommunityTransportTag = _BosSnmpCommunityTransportTag_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5, 1, 1, 6),
    _BosSnmpCommunityTransportTag_Type()
)
bosSnmpCommunityTransportTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpCommunityTransportTag.setStatus("current")
_BosSnmpCommunityStorageType_Type = StorageType
_BosSnmpCommunityStorageType_Object = MibTableColumn
bosSnmpCommunityStorageType = _BosSnmpCommunityStorageType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5, 1, 1, 7),
    _BosSnmpCommunityStorageType_Type()
)
bosSnmpCommunityStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpCommunityStorageType.setStatus("current")
_BosSnmpCommunityStatus_Type = RowStatus
_BosSnmpCommunityStatus_Object = MibTableColumn
bosSnmpCommunityStatus = _BosSnmpCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 11, 5, 1, 1, 8),
    _BosSnmpCommunityStatus_Type()
)
bosSnmpCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosSnmpCommunityStatus.setStatus("current")
_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12)
)
_BosNewCfgPriorityCoSTable_Object = MibTable
bosNewCfgPriorityCoSTable = _BosNewCfgPriorityCoSTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 1)
)
if mibBuilder.loadTexts:
    bosNewCfgPriorityCoSTable.setStatus("current")
_BosNewCfgPriorityCoSEntry_Object = MibTableRow
bosNewCfgPriorityCoSEntry = _BosNewCfgPriorityCoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 1, 1)
)
bosNewCfgPriorityCoSEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosNewCfgPriorityIndex"),
)
if mibBuilder.loadTexts:
    bosNewCfgPriorityCoSEntry.setStatus("current")


class _BosNewCfgPriorityIndex_Type(Integer32):
    """Custom type bosNewCfgPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BosNewCfgPriorityIndex_Type.__name__ = "Integer32"
_BosNewCfgPriorityIndex_Object = MibTableColumn
bosNewCfgPriorityIndex = _BosNewCfgPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 1, 1, 1),
    _BosNewCfgPriorityIndex_Type()
)
bosNewCfgPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosNewCfgPriorityIndex.setStatus("current")


class _BosNewCfgPriorityCoSq_Type(Integer32):
    """Custom type bosNewCfgPriorityCoSq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BosNewCfgPriorityCoSq_Type.__name__ = "Integer32"
_BosNewCfgPriorityCoSq_Object = MibTableColumn
bosNewCfgPriorityCoSq = _BosNewCfgPriorityCoSq_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 1, 1, 2),
    _BosNewCfgPriorityCoSq_Type()
)
bosNewCfgPriorityCoSq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosNewCfgPriorityCoSq.setStatus("current")
_BosNewCfgCosWeightTable_Object = MibTable
bosNewCfgCosWeightTable = _BosNewCfgCosWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 2)
)
if mibBuilder.loadTexts:
    bosNewCfgCosWeightTable.setStatus("current")
_BosNewCfgCosWeightEntry_Object = MibTableRow
bosNewCfgCosWeightEntry = _BosNewCfgCosWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 2, 1)
)
bosNewCfgCosWeightEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosNewCfgCosIndex"),
)
if mibBuilder.loadTexts:
    bosNewCfgCosWeightEntry.setStatus("current")


class _BosNewCfgCosIndex_Type(Integer32):
    """Custom type bosNewCfgCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BosNewCfgCosIndex_Type.__name__ = "Integer32"
_BosNewCfgCosIndex_Object = MibTableColumn
bosNewCfgCosIndex = _BosNewCfgCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 2, 1, 1),
    _BosNewCfgCosIndex_Type()
)
bosNewCfgCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosNewCfgCosIndex.setStatus("current")


class _BosNewCfgCosWeight_Type(Integer32):
    """Custom type bosNewCfgCosWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_BosNewCfgCosWeight_Type.__name__ = "Integer32"
_BosNewCfgCosWeight_Object = MibTableColumn
bosNewCfgCosWeight = _BosNewCfgCosWeight_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 2, 1, 2),
    _BosNewCfgCosWeight_Type()
)
bosNewCfgCosWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosNewCfgCosWeight.setStatus("current")


class _BosNewCfgCosNum_Type(Integer32):
    """Custom type bosNewCfgCosNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("num2", 2),
          ("num8", 8))
    )


_BosNewCfgCosNum_Type.__name__ = "Integer32"
_BosNewCfgCosNum_Object = MibScalar
bosNewCfgCosNum = _BosNewCfgCosNum_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 3),
    _BosNewCfgCosNum_Type()
)
bosNewCfgCosNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosNewCfgCosNum.setStatus("current")
_BosNewCfgDscpTable_Object = MibTable
bosNewCfgDscpTable = _BosNewCfgDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 4)
)
if mibBuilder.loadTexts:
    bosNewCfgDscpTable.setStatus("current")
_BosNewCfgDscpEntry_Object = MibTableRow
bosNewCfgDscpEntry = _BosNewCfgDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 4, 1)
)
bosNewCfgDscpEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosNewCfgDscpIndex"),
)
if mibBuilder.loadTexts:
    bosNewCfgDscpEntry.setStatus("current")


class _BosNewCfgDscpIndex_Type(Integer32):
    """Custom type bosNewCfgDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_BosNewCfgDscpIndex_Type.__name__ = "Integer32"
_BosNewCfgDscpIndex_Object = MibTableColumn
bosNewCfgDscpIndex = _BosNewCfgDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 4, 1, 1),
    _BosNewCfgDscpIndex_Type()
)
bosNewCfgDscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosNewCfgDscpIndex.setStatus("current")


class _BosNewCfgMapDscp_Type(Integer32):
    """Custom type bosNewCfgMapDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_BosNewCfgMapDscp_Type.__name__ = "Integer32"
_BosNewCfgMapDscp_Object = MibTableColumn
bosNewCfgMapDscp = _BosNewCfgMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 4, 1, 2),
    _BosNewCfgMapDscp_Type()
)
bosNewCfgMapDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosNewCfgMapDscp.setStatus("current")


class _BosNewCfgMap8021p_Type(Integer32):
    """Custom type bosNewCfgMap8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BosNewCfgMap8021p_Type.__name__ = "Integer32"
_BosNewCfgMap8021p_Object = MibTableColumn
bosNewCfgMap8021p = _BosNewCfgMap8021p_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 4, 1, 3),
    _BosNewCfgMap8021p_Type()
)
bosNewCfgMap8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosNewCfgMap8021p.setStatus("current")


class _BosNewCfgDscpState_Type(Integer32):
    """Custom type bosNewCfgDscpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_BosNewCfgDscpState_Type.__name__ = "Integer32"
_BosNewCfgDscpState_Object = MibScalar
bosNewCfgDscpState = _BosNewCfgDscpState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 5),
    _BosNewCfgDscpState_Type()
)
bosNewCfgDscpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosNewCfgDscpState.setStatus("current")
_BosNewCfgPortDsStatusTable_Object = MibTable
bosNewCfgPortDsStatusTable = _BosNewCfgPortDsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 6)
)
if mibBuilder.loadTexts:
    bosNewCfgPortDsStatusTable.setStatus("current")
_BosNewCfgPortDsStatusEntry_Object = MibTableRow
bosNewCfgPortDsStatusEntry = _BosNewCfgPortDsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 6, 1)
)
bosNewCfgPortDsStatusEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosNewCfgPortDsIndex"),
)
if mibBuilder.loadTexts:
    bosNewCfgPortDsStatusEntry.setStatus("current")
_BosNewCfgPortDsIndex_Type = Integer32
_BosNewCfgPortDsIndex_Object = MibTableColumn
bosNewCfgPortDsIndex = _BosNewCfgPortDsIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 6, 1, 1),
    _BosNewCfgPortDsIndex_Type()
)
bosNewCfgPortDsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosNewCfgPortDsIndex.setStatus("current")


class _BosNewCfgPortDsState_Type(Integer32):
    """Custom type bosNewCfgPortDsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_BosNewCfgPortDsState_Type.__name__ = "Integer32"
_BosNewCfgPortDsState_Object = MibTableColumn
bosNewCfgPortDsState = _BosNewCfgPortDsState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 6, 1, 2),
    _BosNewCfgPortDsState_Type()
)
bosNewCfgPortDsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosNewCfgPortDsState.setStatus("current")
_BosDiffServMeterTable_Object = MibTable
bosDiffServMeterTable = _BosDiffServMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 7)
)
if mibBuilder.loadTexts:
    bosDiffServMeterTable.setStatus("current")
_BosDiffServMeterEntry_Object = MibTableRow
bosDiffServMeterEntry = _BosDiffServMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 7, 1)
)
bosDiffServMeterEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosDiffServMeterId"),
)
if mibBuilder.loadTexts:
    bosDiffServMeterEntry.setStatus("current")


class _BosDiffServMeterId_Type(Integer32):
    """Custom type bosDiffServMeterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BosDiffServMeterId_Type.__name__ = "Integer32"
_BosDiffServMeterId_Object = MibTableColumn
bosDiffServMeterId = _BosDiffServMeterId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 7, 1, 1),
    _BosDiffServMeterId_Type()
)
bosDiffServMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosDiffServMeterId.setStatus("current")
_BosDiffServMetertokenSize_Type = Unsigned32
_BosDiffServMetertokenSize_Object = MibTableColumn
bosDiffServMetertokenSize = _BosDiffServMetertokenSize_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 7, 1, 2),
    _BosDiffServMetertokenSize_Type()
)
bosDiffServMetertokenSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosDiffServMetertokenSize.setStatus("current")
_BosDiffServMeterRefreshCount_Type = Unsigned32
_BosDiffServMeterRefreshCount_Object = MibTableColumn
bosDiffServMeterRefreshCount = _BosDiffServMeterRefreshCount_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 7, 1, 3),
    _BosDiffServMeterRefreshCount_Type()
)
bosDiffServMeterRefreshCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosDiffServMeterRefreshCount.setStatus("current")
_BosDiffServMeterStatus_Type = RowStatus
_BosDiffServMeterStatus_Object = MibTableColumn
bosDiffServMeterStatus = _BosDiffServMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 12, 7, 1, 4),
    _BosDiffServMeterStatus_Type()
)
bosDiffServMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosDiffServMeterStatus.setStatus("current")
_Fdb_ObjectIdentity = ObjectIdentity
fdb = _Fdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13)
)


class _FdbClear_Type(Integer32):
    """Custom type fdbClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_FdbClear_Type.__name__ = "Integer32"
_FdbClear_Object = MibScalar
fdbClear = _FdbClear_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 1),
    _FdbClear_Type()
)
fdbClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbClear.setStatus("current")
_FdbStatsCurrent_Type = Gauge32
_FdbStatsCurrent_Object = MibScalar
fdbStatsCurrent = _FdbStatsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 2),
    _FdbStatsCurrent_Type()
)
fdbStatsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsCurrent.setStatus("current")
_FdbStatsHiwat_Type = Integer32
_FdbStatsHiwat_Object = MibScalar
fdbStatsHiwat = _FdbStatsHiwat_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 3),
    _FdbStatsHiwat_Type()
)
fdbStatsHiwat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatsHiwat.setStatus("current")


class _FdbStatsClear_Type(Integer32):
    """Custom type fdbStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_FdbStatsClear_Type.__name__ = "Integer32"
_FdbStatsClear_Object = MibScalar
fdbStatsClear = _FdbStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 4),
    _FdbStatsClear_Type()
)
fdbStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbStatsClear.setStatus("current")
_FdbTable_Object = MibTable
fdbTable = _FdbTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5)
)
if mibBuilder.loadTexts:
    fdbTable.setStatus("current")
_FdbEntry_Object = MibTableRow
fdbEntry = _FdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1)
)
fdbEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "fdbVlan"),
    (0, "BLADEOS-BASE-MIB", "fdbMacAddr"),
)
if mibBuilder.loadTexts:
    fdbEntry.setStatus("current")
_FdbVlan_Type = Integer32
_FdbVlan_Object = MibTableColumn
fdbVlan = _FdbVlan_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 1),
    _FdbVlan_Type()
)
fdbVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdbVlan.setStatus("current")
_FdbMacAddr_Type = PhysAddress
_FdbMacAddr_Object = MibTableColumn
fdbMacAddr = _FdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 2),
    _FdbMacAddr_Type()
)
fdbMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdbMacAddr.setStatus("current")


class _FdbMacAddrStr_Type(DisplayString):
    """Custom type fdbMacAddrStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FdbMacAddrStr_Type.__name__ = "DisplayString"
_FdbMacAddrStr_Object = MibTableColumn
fdbMacAddrStr = _FdbMacAddrStr_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 3),
    _FdbMacAddrStr_Type()
)
fdbMacAddrStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacAddrStr.setStatus("current")
_FdbVlanId_Type = Integer32
_FdbVlanId_Object = MibTableColumn
fdbVlanId = _FdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 4),
    _FdbVlanId_Type()
)
fdbVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbVlanId.setStatus("current")
_FdbSrcPort_Type = Integer32
_FdbSrcPort_Object = MibTableColumn
fdbSrcPort = _FdbSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 5),
    _FdbSrcPort_Type()
)
fdbSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSrcPort.setStatus("current")
_FdbSrcTrunk_Type = Integer32
_FdbSrcTrunk_Object = MibTableColumn
fdbSrcTrunk = _FdbSrcTrunk_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 6),
    _FdbSrcTrunk_Type()
)
fdbSrcTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbSrcTrunk.setStatus("current")


class _FdbState_Type(Integer32):
    """Custom type fdbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("forward", 2),
          ("trunk", 3))
    )


_FdbState_Type.__name__ = "Integer32"
_FdbState_Object = MibTableColumn
fdbState = _FdbState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 7),
    _FdbState_Type()
)
fdbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbState.setStatus("current")


class _FdbRefSps_Type(DisplayString):
    """Custom type fdbRefSps based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FdbRefSps_Type.__name__ = "DisplayString"
_FdbRefSps_Object = MibTableColumn
fdbRefSps = _FdbRefSps_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 8),
    _FdbRefSps_Type()
)
fdbRefSps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbRefSps.setStatus("current")
_FdbLearnedPort_Type = Integer32
_FdbLearnedPort_Object = MibTableColumn
fdbLearnedPort = _FdbLearnedPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 9),
    _FdbLearnedPort_Type()
)
fdbLearnedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbLearnedPort.setStatus("current")
_FdbStatus_Type = Integer32
_FdbStatus_Object = MibTableColumn
fdbStatus = _FdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 10),
    _FdbStatus_Type()
)
fdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbStatus.setStatus("current")


class _FdbClearMac_Type(Integer32):
    """Custom type fdbClearMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("clear", 2))
    )


_FdbClearMac_Type.__name__ = "Integer32"
_FdbClearMac_Object = MibTableColumn
fdbClearMac = _FdbClearMac_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 5, 1, 11),
    _FdbClearMac_Type()
)
fdbClearMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbClearMac.setStatus("current")


class _FdbDisableAging_Type(Integer32):
    """Custom type fdbDisableAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_FdbDisableAging_Type.__name__ = "Integer32"
_FdbDisableAging_Object = MibScalar
fdbDisableAging = _FdbDisableAging_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 6),
    _FdbDisableAging_Type()
)
fdbDisableAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbDisableAging.setStatus("current")
_FdbNewCfgStaticTable_Object = MibTable
fdbNewCfgStaticTable = _FdbNewCfgStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 7)
)
if mibBuilder.loadTexts:
    fdbNewCfgStaticTable.setStatus("current")
_FdbNewCfgStaticEntry_Object = MibTableRow
fdbNewCfgStaticEntry = _FdbNewCfgStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 7, 1)
)
fdbNewCfgStaticEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "fdbNewCfgEntryIndex"),
)
if mibBuilder.loadTexts:
    fdbNewCfgStaticEntry.setStatus("current")
_FdbNewCfgEntryIndex_Type = Integer32
_FdbNewCfgEntryIndex_Object = MibTableColumn
fdbNewCfgEntryIndex = _FdbNewCfgEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 7, 1, 1),
    _FdbNewCfgEntryIndex_Type()
)
fdbNewCfgEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbNewCfgEntryIndex.setStatus("current")
_FdbNewCfgAddVlan_Type = Integer32
_FdbNewCfgAddVlan_Object = MibTableColumn
fdbNewCfgAddVlan = _FdbNewCfgAddVlan_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 7, 1, 2),
    _FdbNewCfgAddVlan_Type()
)
fdbNewCfgAddVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbNewCfgAddVlan.setStatus("current")
_FdbNewCfgAddPort_Type = Integer32
_FdbNewCfgAddPort_Object = MibTableColumn
fdbNewCfgAddPort = _FdbNewCfgAddPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 7, 1, 3),
    _FdbNewCfgAddPort_Type()
)
fdbNewCfgAddPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbNewCfgAddPort.setStatus("current")
_FdbNewCfgAddPortChannel_Type = Integer32
_FdbNewCfgAddPortChannel_Object = MibTableColumn
fdbNewCfgAddPortChannel = _FdbNewCfgAddPortChannel_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 7, 1, 4),
    _FdbNewCfgAddPortChannel_Type()
)
fdbNewCfgAddPortChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbNewCfgAddPortChannel.setStatus("current")
_FdbNewCfgAddMac_Type = DisplayString
_FdbNewCfgAddMac_Object = MibTableColumn
fdbNewCfgAddMac = _FdbNewCfgAddMac_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 7, 1, 5),
    _FdbNewCfgAddMac_Type()
)
fdbNewCfgAddMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbNewCfgAddMac.setStatus("current")


class _FdbAgingTime_Type(Integer32):
    """Custom type fdbAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_FdbAgingTime_Type.__name__ = "Integer32"
_FdbAgingTime_Object = MibScalar
fdbAgingTime = _FdbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 13, 8),
    _FdbAgingTime_Type()
)
fdbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbAgingTime.setStatus("current")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14)
)


class _HwPartNumber_Type(DisplayString):
    """Custom type hwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwPartNumber_Type.__name__ = "DisplayString"
_HwPartNumber_Object = MibScalar
hwPartNumber = _HwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 1),
    _HwPartNumber_Type()
)
hwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPartNumber.setStatus("current")


class _HwRevision_Type(DisplayString):
    """Custom type hwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRevision_Type.__name__ = "DisplayString"
_HwRevision_Object = MibScalar
hwRevision = _HwRevision_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 2),
    _HwRevision_Type()
)
hwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRevision.setStatus("current")


class _HwLastBoot_Type(Integer32):
    """Custom type hwLastBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerCycle", 1),
          ("resetFromConsole", 2))
    )


_HwLastBoot_Type.__name__ = "Integer32"
_HwLastBoot_Object = MibScalar
hwLastBoot = _HwLastBoot_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 3),
    _HwLastBoot_Type()
)
hwLastBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLastBoot.setStatus("current")


class _HwMACAddress_Type(DisplayString):
    """Custom type hwMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwMACAddress_Type.__name__ = "DisplayString"
_HwMACAddress_Object = MibScalar
hwMACAddress = _HwMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 4),
    _HwMACAddress_Type()
)
hwMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACAddress.setStatus("current")


class _HwFlashConfiguration_Type(Integer32):
    """Custom type hwFlashConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factory", 0),
          ("active", 1),
          ("backup", 2))
    )


_HwFlashConfiguration_Type.__name__ = "Integer32"
_HwFlashConfiguration_Object = MibScalar
hwFlashConfiguration = _HwFlashConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 6),
    _HwFlashConfiguration_Type()
)
hwFlashConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlashConfiguration.setStatus("current")


class _HwPCBAPartNumber_Type(DisplayString):
    """Custom type hwPCBAPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwPCBAPartNumber_Type.__name__ = "DisplayString"
_HwPCBAPartNumber_Object = MibScalar
hwPCBAPartNumber = _HwPCBAPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 7),
    _HwPCBAPartNumber_Type()
)
hwPCBAPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPCBAPartNumber.setStatus("current")


class _HwFABNumber_Type(DisplayString):
    """Custom type hwFABNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwFABNumber_Type.__name__ = "DisplayString"
_HwFABNumber_Object = MibScalar
hwFABNumber = _HwFABNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 8),
    _HwFABNumber_Type()
)
hwFABNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFABNumber.setStatus("current")


class _HwTemperatureSensor1_Type(DisplayString):
    """Custom type hwTemperatureSensor1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwTemperatureSensor1_Type.__name__ = "DisplayString"
_HwTemperatureSensor1_Object = MibScalar
hwTemperatureSensor1 = _HwTemperatureSensor1_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 11),
    _HwTemperatureSensor1_Type()
)
hwTemperatureSensor1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTemperatureSensor1.setStatus("current")


class _HwTemperatureSensor2_Type(DisplayString):
    """Custom type hwTemperatureSensor2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwTemperatureSensor2_Type.__name__ = "DisplayString"
_HwTemperatureSensor2_Object = MibScalar
hwTemperatureSensor2 = _HwTemperatureSensor2_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 12),
    _HwTemperatureSensor2_Type()
)
hwTemperatureSensor2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTemperatureSensor2.setStatus("current")


class _HwFan1RPMValue_Type(DisplayString):
    """Custom type hwFan1RPMValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwFan1RPMValue_Type.__name__ = "DisplayString"
_HwFan1RPMValue_Object = MibScalar
hwFan1RPMValue = _HwFan1RPMValue_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 14),
    _HwFan1RPMValue_Type()
)
hwFan1RPMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFan1RPMValue.setStatus("current")


class _HwFan2RPMValue_Type(DisplayString):
    """Custom type hwFan2RPMValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwFan2RPMValue_Type.__name__ = "DisplayString"
_HwFan2RPMValue_Object = MibScalar
hwFan2RPMValue = _HwFan2RPMValue_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 15),
    _HwFan2RPMValue_Type()
)
hwFan2RPMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFan2RPMValue.setStatus("current")


class _HwFan3RPMValue_Type(DisplayString):
    """Custom type hwFan3RPMValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwFan3RPMValue_Type.__name__ = "DisplayString"
_HwFan3RPMValue_Object = MibScalar
hwFan3RPMValue = _HwFan3RPMValue_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 16),
    _HwFan3RPMValue_Type()
)
hwFan3RPMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFan3RPMValue.setStatus("current")


class _HwFan4RPMValue_Type(DisplayString):
    """Custom type hwFan4RPMValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwFan4RPMValue_Type.__name__ = "DisplayString"
_HwFan4RPMValue_Object = MibScalar
hwFan4RPMValue = _HwFan4RPMValue_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 17),
    _HwFan4RPMValue_Type()
)
hwFan4RPMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFan4RPMValue.setStatus("current")


class _HwBoardRevision_Type(DisplayString):
    """Custom type hwBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwBoardRevision_Type.__name__ = "DisplayString"
_HwBoardRevision_Object = MibScalar
hwBoardRevision = _HwBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 18),
    _HwBoardRevision_Type()
)
hwBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBoardRevision.setStatus("current")


class _HwPLDFirmwareVersion_Type(DisplayString):
    """Custom type hwPLDFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwPLDFirmwareVersion_Type.__name__ = "DisplayString"
_HwPLDFirmwareVersion_Object = MibScalar
hwPLDFirmwareVersion = _HwPLDFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 19),
    _HwPLDFirmwareVersion_Type()
)
hwPLDFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPLDFirmwareVersion.setStatus("current")


class _HwPowerSupply1State_Type(Integer32):
    """Custom type hwPowerSupply1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HwPowerSupply1State_Type.__name__ = "Integer32"
_HwPowerSupply1State_Object = MibScalar
hwPowerSupply1State = _HwPowerSupply1State_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 20),
    _HwPowerSupply1State_Type()
)
hwPowerSupply1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPowerSupply1State.setStatus("current")


class _HwPowerSupply2State_Type(Integer32):
    """Custom type hwPowerSupply2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HwPowerSupply2State_Type.__name__ = "Integer32"
_HwPowerSupply2State_Object = MibScalar
hwPowerSupply2State = _HwPowerSupply2State_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 21),
    _HwPowerSupply2State_Type()
)
hwPowerSupply2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPowerSupply2State.setStatus("current")
_SfpInfoTable_Object = MibTable
sfpInfoTable = _SfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 22)
)
if mibBuilder.loadTexts:
    sfpInfoTable.setStatus("current")
_SfpInfoTableEntry_Object = MibTableRow
sfpInfoTableEntry = _SfpInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 22, 1)
)
sfpInfoTableEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "sfpInfoIndx"),
)
if mibBuilder.loadTexts:
    sfpInfoTableEntry.setStatus("current")


class _SfpInfoIndx_Type(Integer32):
    """Custom type sfpInfoIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 52),
    )


_SfpInfoIndx_Type.__name__ = "Integer32"
_SfpInfoIndx_Object = MibTableColumn
sfpInfoIndx = _SfpInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 22, 1, 1),
    _SfpInfoIndx_Type()
)
sfpInfoIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoIndx.setStatus("current")


class _SfpInfoDescription_Type(Integer32):
    """Custom type sfpInfoDescription based on Integer32"""
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
          ("sfp", 1),
          ("cx4", 2),
          ("sfpplus", 3))
    )


_SfpInfoDescription_Type.__name__ = "Integer32"
_SfpInfoDescription_Object = MibTableColumn
sfpInfoDescription = _SfpInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 22, 1, 2),
    _SfpInfoDescription_Type()
)
sfpInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoDescription.setStatus("current")


class _SfpInfoSerialNumber_Type(DisplayString):
    """Custom type sfpInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SfpInfoSerialNumber_Type.__name__ = "DisplayString"
_SfpInfoSerialNumber_Object = MibTableColumn
sfpInfoSerialNumber = _SfpInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 22, 1, 3),
    _SfpInfoSerialNumber_Type()
)
sfpInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoSerialNumber.setStatus("current")


class _SfpInfoPartNumber_Type(DisplayString):
    """Custom type sfpInfoPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SfpInfoPartNumber_Type.__name__ = "DisplayString"
_SfpInfoPartNumber_Object = MibTableColumn
sfpInfoPartNumber = _SfpInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 22, 1, 4),
    _SfpInfoPartNumber_Type()
)
sfpInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoPartNumber.setStatus("current")


class _SfpInfoHWRevision_Type(DisplayString):
    """Custom type sfpInfoHWRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SfpInfoHWRevision_Type.__name__ = "DisplayString"
_SfpInfoHWRevision_Object = MibTableColumn
sfpInfoHWRevision = _SfpInfoHWRevision_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 22, 1, 5),
    _SfpInfoHWRevision_Type()
)
sfpInfoHWRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoHWRevision.setStatus("current")
_IomoduleInfoTable_Object = MibTable
iomoduleInfoTable = _IomoduleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 23)
)
if mibBuilder.loadTexts:
    iomoduleInfoTable.setStatus("current")
_IoModuleInfoTableEntry_Object = MibTableRow
ioModuleInfoTableEntry = _IoModuleInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 23, 1)
)
ioModuleInfoTableEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "ioModuleInfoIndx"),
)
if mibBuilder.loadTexts:
    ioModuleInfoTableEntry.setStatus("current")


class _IoModuleInfoIndx_Type(Integer32):
    """Custom type ioModuleInfoIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IoModuleInfoIndx_Type.__name__ = "Integer32"
_IoModuleInfoIndx_Object = MibTableColumn
ioModuleInfoIndx = _IoModuleInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 23, 1, 1),
    _IoModuleInfoIndx_Type()
)
ioModuleInfoIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ioModuleInfoIndx.setStatus("current")


class _IoModuleInfoDescription_Type(Integer32):
    """Custom type ioModuleInfoDescription based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sfp", 1),
          ("cx4", 2),
          ("sfpplus", 3),
          ("10g", 4),
          ("test", 5))
    )


_IoModuleInfoDescription_Type.__name__ = "Integer32"
_IoModuleInfoDescription_Object = MibTableColumn
ioModuleInfoDescription = _IoModuleInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 23, 1, 2),
    _IoModuleInfoDescription_Type()
)
ioModuleInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioModuleInfoDescription.setStatus("current")


class _IoModuleInfoSerialNumber_Type(DisplayString):
    """Custom type ioModuleInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_IoModuleInfoSerialNumber_Type.__name__ = "DisplayString"
_IoModuleInfoSerialNumber_Object = MibTableColumn
ioModuleInfoSerialNumber = _IoModuleInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 23, 1, 3),
    _IoModuleInfoSerialNumber_Type()
)
ioModuleInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioModuleInfoSerialNumber.setStatus("current")


class _IoModuleInfoPartNumber_Type(DisplayString):
    """Custom type ioModuleInfoPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_IoModuleInfoPartNumber_Type.__name__ = "DisplayString"
_IoModuleInfoPartNumber_Object = MibTableColumn
ioModuleInfoPartNumber = _IoModuleInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 23, 1, 4),
    _IoModuleInfoPartNumber_Type()
)
ioModuleInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioModuleInfoPartNumber.setStatus("current")


class _HwFan5RPMValue_Type(DisplayString):
    """Custom type hwFan5RPMValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwFan5RPMValue_Type.__name__ = "DisplayString"
_HwFan5RPMValue_Object = MibScalar
hwFan5RPMValue = _HwFan5RPMValue_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 27),
    _HwFan5RPMValue_Type()
)
hwFan5RPMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFan5RPMValue.setStatus("current")


class _HwTemperatureSensor1WarningThreshhold_Type(DisplayString):
    """Custom type hwTemperatureSensor1WarningThreshhold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwTemperatureSensor1WarningThreshhold_Type.__name__ = "DisplayString"
_HwTemperatureSensor1WarningThreshhold_Object = MibScalar
hwTemperatureSensor1WarningThreshhold = _HwTemperatureSensor1WarningThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 28),
    _HwTemperatureSensor1WarningThreshhold_Type()
)
hwTemperatureSensor1WarningThreshhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTemperatureSensor1WarningThreshhold.setStatus("current")


class _HwTemperatureSensor1RecoverThreshhold_Type(DisplayString):
    """Custom type hwTemperatureSensor1RecoverThreshhold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwTemperatureSensor1RecoverThreshhold_Type.__name__ = "DisplayString"
_HwTemperatureSensor1RecoverThreshhold_Object = MibScalar
hwTemperatureSensor1RecoverThreshhold = _HwTemperatureSensor1RecoverThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 29),
    _HwTemperatureSensor1RecoverThreshhold_Type()
)
hwTemperatureSensor1RecoverThreshhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTemperatureSensor1RecoverThreshhold.setStatus("current")


class _HwTemperatureSensor2WarningThreshhold_Type(DisplayString):
    """Custom type hwTemperatureSensor2WarningThreshhold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwTemperatureSensor2WarningThreshhold_Type.__name__ = "DisplayString"
_HwTemperatureSensor2WarningThreshhold_Object = MibScalar
hwTemperatureSensor2WarningThreshhold = _HwTemperatureSensor2WarningThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 30),
    _HwTemperatureSensor2WarningThreshhold_Type()
)
hwTemperatureSensor2WarningThreshhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTemperatureSensor2WarningThreshhold.setStatus("current")


class _HwTemperatureSensor2RecoverThreshhold_Type(DisplayString):
    """Custom type hwTemperatureSensor2RecoverThreshhold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwTemperatureSensor2RecoverThreshhold_Type.__name__ = "DisplayString"
_HwTemperatureSensor2RecoverThreshhold_Object = MibScalar
hwTemperatureSensor2RecoverThreshhold = _HwTemperatureSensor2RecoverThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 14, 31),
    _HwTemperatureSensor2RecoverThreshhold_Type()
)
hwTemperatureSensor2RecoverThreshhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTemperatureSensor2RecoverThreshhold.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 15)
)


class _SnmpCfgServerVersion_Type(Integer32):
    """Custom type snmpCfgServerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1v2v3", 1),
          ("v3only", 2))
    )


_SnmpCfgServerVersion_Type.__name__ = "Integer32"
_SnmpCfgServerVersion_Object = MibScalar
snmpCfgServerVersion = _SnmpCfgServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 15, 1),
    _SnmpCfgServerVersion_Type()
)
snmpCfgServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCfgServerVersion.setStatus("current")
_SnmpCfgTrapSrcIf_Type = Integer32
_SnmpCfgTrapSrcIf_Object = MibScalar
snmpCfgTrapSrcIf = _SnmpCfgTrapSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 15, 2),
    _SnmpCfgTrapSrcIf_Type()
)
snmpCfgTrapSrcIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCfgTrapSrcIf.setStatus("current")
_BosSnmpTraps_ObjectIdentity = ObjectIdentity
bosSnmpTraps = _BosSnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 16)
)
_BosBladeHarmony_ObjectIdentity = ObjectIdentity
bosBladeHarmony = _BosBladeHarmony_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17)
)
_DataCollection_ObjectIdentity = ObjectIdentity
dataCollection = _DataCollection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1)
)
_AgPortTableMaxEnt_Type = Integer32
_AgPortTableMaxEnt_Object = MibScalar
agPortTableMaxEnt = _AgPortTableMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 1),
    _AgPortTableMaxEnt_Type()
)
agPortTableMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agPortTableMaxEnt.setStatus("current")


class _AgImageForNxtReset_Type(Integer32):
    """Custom type agImageForNxtReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 2),
          ("image2", 3))
    )


_AgImageForNxtReset_Type.__name__ = "Integer32"
_AgImageForNxtReset_Object = MibScalar
agImageForNxtReset = _AgImageForNxtReset_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 2),
    _AgImageForNxtReset_Type()
)
agImageForNxtReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agImageForNxtReset.setStatus("current")


class _AgImage1Ver_Type(DisplayString):
    """Custom type agImage1Ver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgImage1Ver_Type.__name__ = "DisplayString"
_AgImage1Ver_Object = MibScalar
agImage1Ver = _AgImage1Ver_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 3),
    _AgImage1Ver_Type()
)
agImage1Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agImage1Ver.setStatus("current")


class _AgImage2Ver_Type(DisplayString):
    """Custom type agImage2Ver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgImage2Ver_Type.__name__ = "DisplayString"
_AgImage2Ver_Object = MibScalar
agImage2Ver = _AgImage2Ver_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 4),
    _AgImage2Ver_Type()
)
agImage2Ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agImage2Ver.setStatus("current")


class _HwSwitchSoftwareVersion_Type(DisplayString):
    """Custom type hwSwitchSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwSwitchSoftwareVersion_Type.__name__ = "DisplayString"
_HwSwitchSoftwareVersion_Object = MibScalar
hwSwitchSoftwareVersion = _HwSwitchSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 5),
    _HwSwitchSoftwareVersion_Type()
)
hwSwitchSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSwitchSoftwareVersion.setStatus("current")


class _HwSerialNumber_Type(DisplayString):
    """Custom type hwSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwSerialNumber_Type.__name__ = "DisplayString"
_HwSerialNumber_Object = MibScalar
hwSerialNumber = _HwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 6),
    _HwSerialNumber_Type()
)
hwSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSerialNumber.setStatus("current")


class _HwManufacturingDate_Type(DisplayString):
    """Custom type hwManufacturingDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HwManufacturingDate_Type.__name__ = "DisplayString"
_HwManufacturingDate_Object = MibScalar
hwManufacturingDate = _HwManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 7),
    _HwManufacturingDate_Type()
)
hwManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwManufacturingDate.setStatus("current")


class _AgReset_Type(Integer32):
    """Custom type agReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_AgReset_Type.__name__ = "Integer32"
_AgReset_Object = MibScalar
agReset = _AgReset_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 8),
    _AgReset_Type()
)
agReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agReset.setStatus("current")


class _AgBootVer_Type(DisplayString):
    """Custom type agBootVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgBootVer_Type.__name__ = "DisplayString"
_AgBootVer_Object = MibScalar
agBootVer = _AgBootVer_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 9),
    _AgBootVer_Type()
)
agBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agBootVer.setStatus("current")


class _AgConfigForNxtReset_Type(Integer32):
    """Custom type agConfigForNxtReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("backup", 3),
          ("default", 4))
    )


_AgConfigForNxtReset_Type.__name__ = "Integer32"
_AgConfigForNxtReset_Object = MibScalar
agConfigForNxtReset = _AgConfigForNxtReset_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 10),
    _AgConfigForNxtReset_Type()
)
agConfigForNxtReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agConfigForNxtReset.setStatus("current")


class _AgSoftwareVersion_Type(DisplayString):
    """Custom type agSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgSoftwareVersion_Type.__name__ = "DisplayString"
_AgSoftwareVersion_Object = MibScalar
agSoftwareVersion = _AgSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 1, 11),
    _AgSoftwareVersion_Type()
)
agSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agSoftwareVersion.setStatus("current")
_GeneralConfiguration_ObjectIdentity = ObjectIdentity
generalConfiguration = _GeneralConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 2)
)


class _AgSaveConfiguration_Type(Integer32):
    """Custom type agSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("saveActive", 2),
          ("notSaveActive", 3))
    )


_AgSaveConfiguration_Type.__name__ = "Integer32"
_AgSaveConfiguration_Object = MibScalar
agSaveConfiguration = _AgSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 2, 1),
    _AgSaveConfiguration_Type()
)
agSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agSaveConfiguration.setStatus("current")


class _AgNewCfgHttpServerPort_Type(Integer32):
    """Custom type agNewCfgHttpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgNewCfgHttpServerPort_Type.__name__ = "Integer32"
_AgNewCfgHttpServerPort_Object = MibScalar
agNewCfgHttpServerPort = _AgNewCfgHttpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 2, 2),
    _AgNewCfgHttpServerPort_Type()
)
agNewCfgHttpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgHttpServerPort.setStatus("current")


class _AgNewCfgTelnetServerPort_Type(Integer32):
    """Custom type agNewCfgTelnetServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgNewCfgTelnetServerPort_Type.__name__ = "Integer32"
_AgNewCfgTelnetServerPort_Object = MibScalar
agNewCfgTelnetServerPort = _AgNewCfgTelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 2, 3),
    _AgNewCfgTelnetServerPort_Type()
)
agNewCfgTelnetServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTelnetServerPort.setStatus("current")


class _AgNewCfgTftpServerPort_Type(Integer32):
    """Custom type agNewCfgTftpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgNewCfgTftpServerPort_Type.__name__ = "Integer32"
_AgNewCfgTftpServerPort_Object = MibScalar
agNewCfgTftpServerPort = _AgNewCfgTftpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 2, 4),
    _AgNewCfgTftpServerPort_Type()
)
agNewCfgTftpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agNewCfgTftpServerPort.setStatus("current")
_ImageConfigTransfer_ObjectIdentity = ObjectIdentity
imageConfigTransfer = _ImageConfigTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 3)
)


class _AgTftpServer_Type(DisplayString):
    """Custom type agTftpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpServer_Type.__name__ = "DisplayString"
_AgTftpServer_Object = MibScalar
agTftpServer = _AgTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 3, 1),
    _AgTftpServer_Type()
)
agTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpServer.setStatus("current")


class _AgTftpImage_Type(Integer32):
    """Custom type agTftpImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("image1", 2),
          ("image2", 3),
          ("boot", 4))
    )


_AgTftpImage_Type.__name__ = "Integer32"
_AgTftpImage_Object = MibScalar
agTftpImage = _AgTftpImage_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 3, 2),
    _AgTftpImage_Type()
)
agTftpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpImage.setStatus("current")


class _AgTftpImageFileName_Type(DisplayString):
    """Custom type agTftpImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpImageFileName_Type.__name__ = "DisplayString"
_AgTftpImageFileName_Object = MibScalar
agTftpImageFileName = _AgTftpImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 3, 3),
    _AgTftpImageFileName_Type()
)
agTftpImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpImageFileName.setStatus("current")


class _AgTftpCfgFileName_Type(DisplayString):
    """Custom type agTftpCfgFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpCfgFileName_Type.__name__ = "DisplayString"
_AgTftpCfgFileName_Object = MibScalar
agTftpCfgFileName = _AgTftpCfgFileName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 3, 4),
    _AgTftpCfgFileName_Type()
)
agTftpCfgFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpCfgFileName.setStatus("current")


class _AgTftpAction_Type(Integer32):
    """Custom type agTftpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              7,
              8,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("imgget", 2),
          ("cfgput", 4),
          ("imgput", 7),
          ("tsdump-put", 8),
          ("bkcfgget", 10),
          ("bkcfgput", 11),
          ("accfgget", 12),
          ("accfgput", 13))
    )


_AgTftpAction_Type.__name__ = "Integer32"
_AgTftpAction_Object = MibScalar
agTftpAction = _AgTftpAction_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 3, 5),
    _AgTftpAction_Type()
)
agTftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agTftpAction.setStatus("current")


class _AgTftpLastActionStatus_Type(DisplayString):
    """Custom type agTftpLastActionStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgTftpLastActionStatus_Type.__name__ = "DisplayString"
_AgTftpLastActionStatus_Object = MibScalar
agTftpLastActionStatus = _AgTftpLastActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 3, 6),
    _AgTftpLastActionStatus_Type()
)
agTftpLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agTftpLastActionStatus.setStatus("current")
_PortInformation_ObjectIdentity = ObjectIdentity
portInformation = _PortInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4)
)
_PortInfoTable_Object = MibTable
portInfoTable = _PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1)
)
if mibBuilder.loadTexts:
    portInfoTable.setStatus("current")
_PortInfoTableEntry_Object = MibTableRow
portInfoTableEntry = _PortInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1, 1)
)
portInfoTableEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "portInfoIndx"),
)
if mibBuilder.loadTexts:
    portInfoTableEntry.setStatus("current")
_PortInfoIndx_Type = Integer32
_PortInfoIndx_Object = MibTableColumn
portInfoIndx = _PortInfoIndx_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1, 1, 1),
    _PortInfoIndx_Type()
)
portInfoIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoIndx.setStatus("current")


class _PortInfoSpeed_Type(Integer32):
    """Custom type portInfoSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("mbs10", 2),
          ("mbs100", 3),
          ("mbs1000", 4),
          ("any", 5),
          ("mbs10000", 6))
    )


_PortInfoSpeed_Type.__name__ = "Integer32"
_PortInfoSpeed_Object = MibTableColumn
portInfoSpeed = _PortInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1, 1, 2),
    _PortInfoSpeed_Type()
)
portInfoSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoSpeed.setStatus("current")


class _PortInfoMode_Type(Integer32):
    """Custom type portInfoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 2),
          ("halfduplex", 3),
          ("any", 4))
    )


_PortInfoMode_Type.__name__ = "Integer32"
_PortInfoMode_Object = MibTableColumn
portInfoMode = _PortInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1, 1, 3),
    _PortInfoMode_Type()
)
portInfoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoMode.setStatus("current")


class _PortInfoFlowCtrl_Type(Integer32):
    """Custom type portInfoFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("transmit", 2),
          ("receive", 3),
          ("both", 4),
          ("none", 5))
    )


_PortInfoFlowCtrl_Type.__name__ = "Integer32"
_PortInfoFlowCtrl_Object = MibTableColumn
portInfoFlowCtrl = _PortInfoFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1, 1, 4),
    _PortInfoFlowCtrl_Type()
)
portInfoFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoFlowCtrl.setStatus("current")


class _PortInfoLink_Type(Integer32):
    """Custom type portInfoLink based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("disabled", 3),
          ("inoperative", 4))
    )


_PortInfoLink_Type.__name__ = "Integer32"
_PortInfoLink_Object = MibTableColumn
portInfoLink = _PortInfoLink_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1, 1, 5),
    _PortInfoLink_Type()
)
portInfoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoLink.setStatus("current")


class _AgPortNewCfgVlanTag_Type(Integer32):
    """Custom type agPortNewCfgVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_AgPortNewCfgVlanTag_Type.__name__ = "Integer32"
_AgPortNewCfgVlanTag_Object = MibTableColumn
agPortNewCfgVlanTag = _AgPortNewCfgVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1, 1, 6),
    _AgPortNewCfgVlanTag_Type()
)
agPortNewCfgVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgVlanTag.setStatus("current")


class _AgPortNewCfgTagPVID_Type(Integer32):
    """Custom type agPortNewCfgTagPVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 2),
          ("untagged", 3))
    )


_AgPortNewCfgTagPVID_Type.__name__ = "Integer32"
_AgPortNewCfgTagPVID_Object = MibTableColumn
agPortNewCfgTagPVID = _AgPortNewCfgTagPVID_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1, 1, 7),
    _AgPortNewCfgTagPVID_Type()
)
agPortNewCfgTagPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgTagPVID.setStatus("current")
_AgPortNewCfgPVID_Type = Integer32
_AgPortNewCfgPVID_Object = MibTableColumn
agPortNewCfgPVID = _AgPortNewCfgPVID_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1, 1, 8),
    _AgPortNewCfgPVID_Type()
)
agPortNewCfgPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPVID.setStatus("current")


class _AgPortNewCfgPortName_Type(DisplayString):
    """Custom type agPortNewCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgPortNewCfgPortName_Type.__name__ = "DisplayString"
_AgPortNewCfgPortName_Object = MibTableColumn
agPortNewCfgPortName = _AgPortNewCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 4, 1, 1, 9),
    _AgPortNewCfgPortName_Type()
)
agPortNewCfgPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agPortNewCfgPortName.setStatus("current")
_VlanConfiguration_ObjectIdentity = ObjectIdentity
vlanConfiguration = _VlanConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5)
)
_BosCfgVlanNewVlan_Type = Integer32
_BosCfgVlanNewVlan_Object = MibScalar
bosCfgVlanNewVlan = _BosCfgVlanNewVlan_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 1),
    _BosCfgVlanNewVlan_Type()
)
bosCfgVlanNewVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosCfgVlanNewVlan.setStatus("current")
_VlanNewCfgTable_Object = MibTable
vlanNewCfgTable = _VlanNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2)
)
if mibBuilder.loadTexts:
    vlanNewCfgTable.setStatus("current")
_VlanNewCfgTableEntry_Object = MibTableRow
vlanNewCfgTableEntry = _VlanNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1)
)
vlanNewCfgTableEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "vlanNewCfgVlanId"),
)
if mibBuilder.loadTexts:
    vlanNewCfgTableEntry.setStatus("current")
_VlanNewCfgVlanId_Type = Integer32
_VlanNewCfgVlanId_Object = MibTableColumn
vlanNewCfgVlanId = _VlanNewCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 1),
    _VlanNewCfgVlanId_Type()
)
vlanNewCfgVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNewCfgVlanId.setStatus("current")


class _VlanNewCfgVlanName_Type(DisplayString):
    """Custom type vlanNewCfgVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanNewCfgVlanName_Type.__name__ = "DisplayString"
_VlanNewCfgVlanName_Object = MibTableColumn
vlanNewCfgVlanName = _VlanNewCfgVlanName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 2),
    _VlanNewCfgVlanName_Type()
)
vlanNewCfgVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgVlanName.setStatus("current")
_VlanNewCfgPorts_Type = OctetString
_VlanNewCfgPorts_Object = MibTableColumn
vlanNewCfgPorts = _VlanNewCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 3),
    _VlanNewCfgPorts_Type()
)
vlanNewCfgPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNewCfgPorts.setStatus("current")


class _VlanNewCfgPortList_Type(DisplayString):
    """Custom type vlanNewCfgPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VlanNewCfgPortList_Type.__name__ = "DisplayString"
_VlanNewCfgPortList_Object = MibTableColumn
vlanNewCfgPortList = _VlanNewCfgPortList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 4),
    _VlanNewCfgPortList_Type()
)
vlanNewCfgPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgPortList.setStatus("current")


class _VlanNewCfgState_Type(Integer32):
    """Custom type vlanNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("disabled", 3))
    )


_VlanNewCfgState_Type.__name__ = "Integer32"
_VlanNewCfgState_Object = MibTableColumn
vlanNewCfgState = _VlanNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 5),
    _VlanNewCfgState_Type()
)
vlanNewCfgState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgState.setStatus("current")
_VlanNewCfgAddPort_Type = Integer32
_VlanNewCfgAddPort_Object = MibTableColumn
vlanNewCfgAddPort = _VlanNewCfgAddPort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 6),
    _VlanNewCfgAddPort_Type()
)
vlanNewCfgAddPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgAddPort.setStatus("current")
_VlanNewCfgRemovePort_Type = Integer32
_VlanNewCfgRemovePort_Object = MibTableColumn
vlanNewCfgRemovePort = _VlanNewCfgRemovePort_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 7),
    _VlanNewCfgRemovePort_Type()
)
vlanNewCfgRemovePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgRemovePort.setStatus("current")


class _VlanNewCfgDelete_Type(Integer32):
    """Custom type vlanNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_VlanNewCfgDelete_Type.__name__ = "Integer32"
_VlanNewCfgDelete_Object = MibTableColumn
vlanNewCfgDelete = _VlanNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 8),
    _VlanNewCfgDelete_Type()
)
vlanNewCfgDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgDelete.setStatus("current")
_VlanNewCfgStg_Type = Integer32
_VlanNewCfgStg_Object = MibTableColumn
vlanNewCfgStg = _VlanNewCfgStg_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 9),
    _VlanNewCfgStg_Type()
)
vlanNewCfgStg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanNewCfgStg.setStatus("current")


class _VlanNewCfgPrVlanType_Type(Integer32):
    """Custom type vlanNewCfgPrVlanType based on Integer32"""
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
          ("primary", 1),
          ("isolated", 2),
          ("community", 3))
    )


_VlanNewCfgPrVlanType_Type.__name__ = "Integer32"
_VlanNewCfgPrVlanType_Object = MibTableColumn
vlanNewCfgPrVlanType = _VlanNewCfgPrVlanType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 10),
    _VlanNewCfgPrVlanType_Type()
)
vlanNewCfgPrVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgPrVlanType.setStatus("current")
_VlanNewCfgPrVlanMapPriId_Type = Integer32
_VlanNewCfgPrVlanMapPriId_Object = MibTableColumn
vlanNewCfgPrVlanMapPriId = _VlanNewCfgPrVlanMapPriId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 11),
    _VlanNewCfgPrVlanMapPriId_Type()
)
vlanNewCfgPrVlanMapPriId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgPrVlanMapPriId.setStatus("current")


class _VlanNewCfgPrVlanState_Type(Integer32):
    """Custom type vlanNewCfgPrVlanState based on Integer32"""
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


_VlanNewCfgPrVlanState_Type.__name__ = "Integer32"
_VlanNewCfgPrVlanState_Object = MibTableColumn
vlanNewCfgPrVlanState = _VlanNewCfgPrVlanState_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 17, 5, 2, 1, 12),
    _VlanNewCfgPrVlanState_Type()
)
vlanNewCfgPrVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanNewCfgPrVlanState.setStatus("current")
_Bossnoop_ObjectIdentity = ObjectIdentity
bossnoop = _Bossnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105)
)
_BosSnoopSystem_ObjectIdentity = ObjectIdentity
bosSnoopSystem = _BosSnoopSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 1)
)
_BosSnoopInst_ObjectIdentity = ObjectIdentity
bosSnoopInst = _BosSnoopInst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2)
)
_BosSnoopInstanceGlobalTable_Object = MibTable
bosSnoopInstanceGlobalTable = _BosSnoopInstanceGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 1)
)
if mibBuilder.loadTexts:
    bosSnoopInstanceGlobalTable.setStatus("current")
_BosSnoopInstanceGlobalEntry_Object = MibTableRow
bosSnoopInstanceGlobalEntry = _BosSnoopInstanceGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 1, 1)
)
bosSnoopInstanceGlobalEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnoopInstanceGlobalInstId"),
)
if mibBuilder.loadTexts:
    bosSnoopInstanceGlobalEntry.setStatus("current")


class _BosSnoopInstanceGlobalInstId_Type(Integer32):
    """Custom type bosSnoopInstanceGlobalInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosSnoopInstanceGlobalInstId_Type.__name__ = "Integer32"
_BosSnoopInstanceGlobalInstId_Object = MibTableColumn
bosSnoopInstanceGlobalInstId = _BosSnoopInstanceGlobalInstId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 1, 1, 1),
    _BosSnoopInstanceGlobalInstId_Type()
)
bosSnoopInstanceGlobalInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopInstanceGlobalInstId.setStatus("current")
_BosSnoopInstanceConfigTable_Object = MibTable
bosSnoopInstanceConfigTable = _BosSnoopInstanceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 2)
)
if mibBuilder.loadTexts:
    bosSnoopInstanceConfigTable.setStatus("current")
_BosSnoopInstanceConfigEntry_Object = MibTableRow
bosSnoopInstanceConfigEntry = _BosSnoopInstanceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 2, 1)
)
bosSnoopInstanceConfigEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnoopInstanceConfigInstId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopInetAddressType"),
)
if mibBuilder.loadTexts:
    bosSnoopInstanceConfigEntry.setStatus("current")


class _BosSnoopInstanceConfigInstId_Type(Integer32):
    """Custom type bosSnoopInstanceConfigInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosSnoopInstanceConfigInstId_Type.__name__ = "Integer32"
_BosSnoopInstanceConfigInstId_Object = MibTableColumn
bosSnoopInstanceConfigInstId = _BosSnoopInstanceConfigInstId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 2, 1, 1),
    _BosSnoopInstanceConfigInstId_Type()
)
bosSnoopInstanceConfigInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopInstanceConfigInstId.setStatus("current")
_BosSnoopInetAddressType_Type = InetAddressType
_BosSnoopInetAddressType_Object = MibTableColumn
bosSnoopInetAddressType = _BosSnoopInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 2, 1, 2),
    _BosSnoopInetAddressType_Type()
)
bosSnoopInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopInetAddressType.setStatus("current")


class _BosSnoopStatus_Type(Integer32):
    """Custom type bosSnoopStatus based on Integer32"""
    defaultValue = 2

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


_BosSnoopStatus_Type.__name__ = "Integer32"
_BosSnoopStatus_Object = MibTableColumn
bosSnoopStatus = _BosSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 2, 1, 3),
    _BosSnoopStatus_Type()
)
bosSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopStatus.setStatus("current")


class _BosSnoopRouterPortPurgeInterval_Type(Integer32):
    """Custom type bosSnoopRouterPortPurgeInterval based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_BosSnoopRouterPortPurgeInterval_Type.__name__ = "Integer32"
_BosSnoopRouterPortPurgeInterval_Object = MibTableColumn
bosSnoopRouterPortPurgeInterval = _BosSnoopRouterPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 2, 1, 4),
    _BosSnoopRouterPortPurgeInterval_Type()
)
bosSnoopRouterPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopRouterPortPurgeInterval.setStatus("current")


class _BosSnoopPortPurgeInterval_Type(Integer32):
    """Custom type bosSnoopPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 1225),
    )


_BosSnoopPortPurgeInterval_Type.__name__ = "Integer32"
_BosSnoopPortPurgeInterval_Object = MibTableColumn
bosSnoopPortPurgeInterval = _BosSnoopPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 2, 1, 5),
    _BosSnoopPortPurgeInterval_Type()
)
bosSnoopPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopPortPurgeInterval.setStatus("current")


class _BosSnoopGrpQueryInterval_Type(Integer32):
    """Custom type bosSnoopGrpQueryInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_BosSnoopGrpQueryInterval_Type.__name__ = "Integer32"
_BosSnoopGrpQueryInterval_Object = MibTableColumn
bosSnoopGrpQueryInterval = _BosSnoopGrpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 2, 1, 6),
    _BosSnoopGrpQueryInterval_Type()
)
bosSnoopGrpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopGrpQueryInterval.setStatus("current")


class _BosSnoopOperStatus_Type(Integer32):
    """Custom type bosSnoopOperStatus based on Integer32"""
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


_BosSnoopOperStatus_Type.__name__ = "Integer32"
_BosSnoopOperStatus_Object = MibTableColumn
bosSnoopOperStatus = _BosSnoopOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 2, 2, 1, 7),
    _BosSnoopOperStatus_Type()
)
bosSnoopOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopOperStatus.setStatus("current")
_BosSnoopVlan_ObjectIdentity = ObjectIdentity
bosSnoopVlan = _BosSnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3)
)
_BosSnoopVlanMcastIpFwdTable_Object = MibTable
bosSnoopVlanMcastIpFwdTable = _BosSnoopVlanMcastIpFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 1)
)
if mibBuilder.loadTexts:
    bosSnoopVlanMcastIpFwdTable.setStatus("current")
_BosSnoopVlanMcastIpFwdEntry_Object = MibTableRow
bosSnoopVlanMcastIpFwdEntry = _BosSnoopVlanMcastIpFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 1, 1)
)
bosSnoopVlanMcastIpFwdEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanMcastIpFwdInstId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanMcastIpFwdVlanId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanMcastIpFwdAddressType"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanMcastIpFwdSourceAddress"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanMcastIpFwdGroupAddress"),
)
if mibBuilder.loadTexts:
    bosSnoopVlanMcastIpFwdEntry.setStatus("current")


class _BosSnoopVlanMcastIpFwdInstId_Type(Integer32):
    """Custom type bosSnoopVlanMcastIpFwdInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosSnoopVlanMcastIpFwdInstId_Type.__name__ = "Integer32"
_BosSnoopVlanMcastIpFwdInstId_Object = MibTableColumn
bosSnoopVlanMcastIpFwdInstId = _BosSnoopVlanMcastIpFwdInstId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 1, 1, 1),
    _BosSnoopVlanMcastIpFwdInstId_Type()
)
bosSnoopVlanMcastIpFwdInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanMcastIpFwdInstId.setStatus("current")


class _BosSnoopVlanMcastIpFwdVlanId_Type(Integer32):
    """Custom type bosSnoopVlanMcastIpFwdVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BosSnoopVlanMcastIpFwdVlanId_Type.__name__ = "Integer32"
_BosSnoopVlanMcastIpFwdVlanId_Object = MibTableColumn
bosSnoopVlanMcastIpFwdVlanId = _BosSnoopVlanMcastIpFwdVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 1, 1, 2),
    _BosSnoopVlanMcastIpFwdVlanId_Type()
)
bosSnoopVlanMcastIpFwdVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanMcastIpFwdVlanId.setStatus("current")
_BosSnoopVlanMcastIpFwdAddressType_Type = InetAddressType
_BosSnoopVlanMcastIpFwdAddressType_Object = MibTableColumn
bosSnoopVlanMcastIpFwdAddressType = _BosSnoopVlanMcastIpFwdAddressType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 1, 1, 3),
    _BosSnoopVlanMcastIpFwdAddressType_Type()
)
bosSnoopVlanMcastIpFwdAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanMcastIpFwdAddressType.setStatus("current")
_BosSnoopVlanMcastIpFwdSourceAddress_Type = InetAddress
_BosSnoopVlanMcastIpFwdSourceAddress_Object = MibTableColumn
bosSnoopVlanMcastIpFwdSourceAddress = _BosSnoopVlanMcastIpFwdSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 1, 1, 4),
    _BosSnoopVlanMcastIpFwdSourceAddress_Type()
)
bosSnoopVlanMcastIpFwdSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanMcastIpFwdSourceAddress.setStatus("current")
_BosSnoopVlanMcastIpFwdGroupAddress_Type = InetAddress
_BosSnoopVlanMcastIpFwdGroupAddress_Object = MibTableColumn
bosSnoopVlanMcastIpFwdGroupAddress = _BosSnoopVlanMcastIpFwdGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 1, 1, 5),
    _BosSnoopVlanMcastIpFwdGroupAddress_Type()
)
bosSnoopVlanMcastIpFwdGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanMcastIpFwdGroupAddress.setStatus("current")
_BosSnoopVlanMcastIpFwdPortList_Type = PortList
_BosSnoopVlanMcastIpFwdPortList_Object = MibTableColumn
bosSnoopVlanMcastIpFwdPortList = _BosSnoopVlanMcastIpFwdPortList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 1, 1, 6),
    _BosSnoopVlanMcastIpFwdPortList_Type()
)
bosSnoopVlanMcastIpFwdPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopVlanMcastIpFwdPortList.setStatus("current")
_BosSnoopVlanRouterTable_Object = MibTable
bosSnoopVlanRouterTable = _BosSnoopVlanRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 2)
)
if mibBuilder.loadTexts:
    bosSnoopVlanRouterTable.setStatus("current")
_BosSnoopVlanRouterEntry_Object = MibTableRow
bosSnoopVlanRouterEntry = _BosSnoopVlanRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 2, 1)
)
bosSnoopVlanRouterEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanRouterInstId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanRouterVlanId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanRouterInetAddressType"),
)
if mibBuilder.loadTexts:
    bosSnoopVlanRouterEntry.setStatus("current")


class _BosSnoopVlanRouterInstId_Type(Integer32):
    """Custom type bosSnoopVlanRouterInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosSnoopVlanRouterInstId_Type.__name__ = "Integer32"
_BosSnoopVlanRouterInstId_Object = MibTableColumn
bosSnoopVlanRouterInstId = _BosSnoopVlanRouterInstId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 2, 1, 1),
    _BosSnoopVlanRouterInstId_Type()
)
bosSnoopVlanRouterInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanRouterInstId.setStatus("current")


class _BosSnoopVlanRouterVlanId_Type(Integer32):
    """Custom type bosSnoopVlanRouterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BosSnoopVlanRouterVlanId_Type.__name__ = "Integer32"
_BosSnoopVlanRouterVlanId_Object = MibTableColumn
bosSnoopVlanRouterVlanId = _BosSnoopVlanRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 2, 1, 2),
    _BosSnoopVlanRouterVlanId_Type()
)
bosSnoopVlanRouterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanRouterVlanId.setStatus("current")
_BosSnoopVlanRouterInetAddressType_Type = InetAddressType
_BosSnoopVlanRouterInetAddressType_Object = MibTableColumn
bosSnoopVlanRouterInetAddressType = _BosSnoopVlanRouterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 2, 1, 3),
    _BosSnoopVlanRouterInetAddressType_Type()
)
bosSnoopVlanRouterInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanRouterInetAddressType.setStatus("current")
_BosSnoopVlanRouterPortList_Type = PortList
_BosSnoopVlanRouterPortList_Object = MibTableColumn
bosSnoopVlanRouterPortList = _BosSnoopVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 2, 1, 4),
    _BosSnoopVlanRouterPortList_Type()
)
bosSnoopVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopVlanRouterPortList.setStatus("current")
_BosSnoopVlanFilterTable_Object = MibTable
bosSnoopVlanFilterTable = _BosSnoopVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3)
)
if mibBuilder.loadTexts:
    bosSnoopVlanFilterTable.setStatus("current")
_BosSnoopVlanFilterEntry_Object = MibTableRow
bosSnoopVlanFilterEntry = _BosSnoopVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3, 1)
)
bosSnoopVlanFilterEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanFilterInstId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanFilterVlanId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopVlanFilterInetAddressType"),
)
if mibBuilder.loadTexts:
    bosSnoopVlanFilterEntry.setStatus("current")


class _BosSnoopVlanFilterInstId_Type(Integer32):
    """Custom type bosSnoopVlanFilterInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosSnoopVlanFilterInstId_Type.__name__ = "Integer32"
_BosSnoopVlanFilterInstId_Object = MibTableColumn
bosSnoopVlanFilterInstId = _BosSnoopVlanFilterInstId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3, 1, 1),
    _BosSnoopVlanFilterInstId_Type()
)
bosSnoopVlanFilterInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanFilterInstId.setStatus("current")


class _BosSnoopVlanFilterVlanId_Type(Integer32):
    """Custom type bosSnoopVlanFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BosSnoopVlanFilterVlanId_Type.__name__ = "Integer32"
_BosSnoopVlanFilterVlanId_Object = MibTableColumn
bosSnoopVlanFilterVlanId = _BosSnoopVlanFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3, 1, 2),
    _BosSnoopVlanFilterVlanId_Type()
)
bosSnoopVlanFilterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanFilterVlanId.setStatus("current")
_BosSnoopVlanFilterInetAddressType_Type = InetAddressType
_BosSnoopVlanFilterInetAddressType_Object = MibTableColumn
bosSnoopVlanFilterInetAddressType = _BosSnoopVlanFilterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3, 1, 3),
    _BosSnoopVlanFilterInetAddressType_Type()
)
bosSnoopVlanFilterInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopVlanFilterInetAddressType.setStatus("current")


class _BosSnoopVlanSnoopStatus_Type(Integer32):
    """Custom type bosSnoopVlanSnoopStatus based on Integer32"""
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


_BosSnoopVlanSnoopStatus_Type.__name__ = "Integer32"
_BosSnoopVlanSnoopStatus_Object = MibTableColumn
bosSnoopVlanSnoopStatus = _BosSnoopVlanSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3, 1, 4),
    _BosSnoopVlanSnoopStatus_Type()
)
bosSnoopVlanSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopVlanSnoopStatus.setStatus("current")


class _BosSnoopVlanOperatingVersion_Type(Integer32):
    """Custom type bosSnoopVlanOperatingVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_BosSnoopVlanOperatingVersion_Type.__name__ = "Integer32"
_BosSnoopVlanOperatingVersion_Object = MibTableColumn
bosSnoopVlanOperatingVersion = _BosSnoopVlanOperatingVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3, 1, 5),
    _BosSnoopVlanOperatingVersion_Type()
)
bosSnoopVlanOperatingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopVlanOperatingVersion.setStatus("current")


class _BosSnoopVlanCfgOperVersion_Type(Integer32):
    """Custom type bosSnoopVlanCfgOperVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_BosSnoopVlanCfgOperVersion_Type.__name__ = "Integer32"
_BosSnoopVlanCfgOperVersion_Object = MibTableColumn
bosSnoopVlanCfgOperVersion = _BosSnoopVlanCfgOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3, 1, 6),
    _BosSnoopVlanCfgOperVersion_Type()
)
bosSnoopVlanCfgOperVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopVlanCfgOperVersion.setStatus("current")


class _BosSnoopVlanFastLeave_Type(Integer32):
    """Custom type bosSnoopVlanFastLeave based on Integer32"""
    defaultValue = 2

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


_BosSnoopVlanFastLeave_Type.__name__ = "Integer32"
_BosSnoopVlanFastLeave_Object = MibTableColumn
bosSnoopVlanFastLeave = _BosSnoopVlanFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3, 1, 7),
    _BosSnoopVlanFastLeave_Type()
)
bosSnoopVlanFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopVlanFastLeave.setStatus("current")
_BosSnoopVlanRtrPortList_Type = PortList
_BosSnoopVlanRtrPortList_Object = MibTableColumn
bosSnoopVlanRtrPortList = _BosSnoopVlanRtrPortList_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3, 1, 8),
    _BosSnoopVlanRtrPortList_Type()
)
bosSnoopVlanRtrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopVlanRtrPortList.setStatus("current")
_BosSnoopVlanRowStatus_Type = RowStatus
_BosSnoopVlanRowStatus_Object = MibTableColumn
bosSnoopVlanRowStatus = _BosSnoopVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 3, 3, 1, 9),
    _BosSnoopVlanRowStatus_Type()
)
bosSnoopVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosSnoopVlanRowStatus.setStatus("current")
_BosSnoopStats_ObjectIdentity = ObjectIdentity
bosSnoopStats = _BosSnoopStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4)
)
_BosSnoopStatsTable_Object = MibTable
bosSnoopStatsTable = _BosSnoopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1)
)
if mibBuilder.loadTexts:
    bosSnoopStatsTable.setStatus("current")
_BosSnoopStatsEntry_Object = MibTableRow
bosSnoopStatsEntry = _BosSnoopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1)
)
bosSnoopStatsEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosSnoopStatsInstId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopStatsVlanId"),
    (0, "BLADEOS-BASE-MIB", "bosSnoopStatsInetAddressType"),
)
if mibBuilder.loadTexts:
    bosSnoopStatsEntry.setStatus("current")


class _BosSnoopStatsInstId_Type(Integer32):
    """Custom type bosSnoopStatsInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BosSnoopStatsInstId_Type.__name__ = "Integer32"
_BosSnoopStatsInstId_Object = MibTableColumn
bosSnoopStatsInstId = _BosSnoopStatsInstId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 1),
    _BosSnoopStatsInstId_Type()
)
bosSnoopStatsInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopStatsInstId.setStatus("current")


class _BosSnoopStatsVlanId_Type(Integer32):
    """Custom type bosSnoopStatsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BosSnoopStatsVlanId_Type.__name__ = "Integer32"
_BosSnoopStatsVlanId_Object = MibTableColumn
bosSnoopStatsVlanId = _BosSnoopStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 2),
    _BosSnoopStatsVlanId_Type()
)
bosSnoopStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopStatsVlanId.setStatus("current")
_BosSnoopStatsInetAddressType_Type = InetAddressType
_BosSnoopStatsInetAddressType_Object = MibTableColumn
bosSnoopStatsInetAddressType = _BosSnoopStatsInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 3),
    _BosSnoopStatsInetAddressType_Type()
)
bosSnoopStatsInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosSnoopStatsInetAddressType.setStatus("current")
_BosSnoopStatsRxGenQueries_Type = Counter32
_BosSnoopStatsRxGenQueries_Object = MibTableColumn
bosSnoopStatsRxGenQueries = _BosSnoopStatsRxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 4),
    _BosSnoopStatsRxGenQueries_Type()
)
bosSnoopStatsRxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxGenQueries.setStatus("current")
_BosSnoopStatsRxGrpQueries_Type = Counter32
_BosSnoopStatsRxGrpQueries_Object = MibTableColumn
bosSnoopStatsRxGrpQueries = _BosSnoopStatsRxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 5),
    _BosSnoopStatsRxGrpQueries_Type()
)
bosSnoopStatsRxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxGrpQueries.setStatus("current")
_BosSnoopStatsRxGrpAndSrcQueries_Type = Counter32
_BosSnoopStatsRxGrpAndSrcQueries_Object = MibTableColumn
bosSnoopStatsRxGrpAndSrcQueries = _BosSnoopStatsRxGrpAndSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 6),
    _BosSnoopStatsRxGrpAndSrcQueries_Type()
)
bosSnoopStatsRxGrpAndSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxGrpAndSrcQueries.setStatus("current")
_BosSnoopStatsRxAsmReports_Type = Counter32
_BosSnoopStatsRxAsmReports_Object = MibTableColumn
bosSnoopStatsRxAsmReports = _BosSnoopStatsRxAsmReports_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 7),
    _BosSnoopStatsRxAsmReports_Type()
)
bosSnoopStatsRxAsmReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxAsmReports.setStatus("current")
_BosSnoopStatsRxSsmReports_Type = Counter32
_BosSnoopStatsRxSsmReports_Object = MibTableColumn
bosSnoopStatsRxSsmReports = _BosSnoopStatsRxSsmReports_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 8),
    _BosSnoopStatsRxSsmReports_Type()
)
bosSnoopStatsRxSsmReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxSsmReports.setStatus("current")
_BosSnoopStatsRxSsmIsInMsgs_Type = Counter32
_BosSnoopStatsRxSsmIsInMsgs_Object = MibTableColumn
bosSnoopStatsRxSsmIsInMsgs = _BosSnoopStatsRxSsmIsInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 9),
    _BosSnoopStatsRxSsmIsInMsgs_Type()
)
bosSnoopStatsRxSsmIsInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxSsmIsInMsgs.setStatus("current")
_BosSnoopStatsRxSsmIsExMsgs_Type = Counter32
_BosSnoopStatsRxSsmIsExMsgs_Object = MibTableColumn
bosSnoopStatsRxSsmIsExMsgs = _BosSnoopStatsRxSsmIsExMsgs_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 10),
    _BosSnoopStatsRxSsmIsExMsgs_Type()
)
bosSnoopStatsRxSsmIsExMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxSsmIsExMsgs.setStatus("current")
_BosSnoopStatsRxSsmToInMsgs_Type = Counter32
_BosSnoopStatsRxSsmToInMsgs_Object = MibTableColumn
bosSnoopStatsRxSsmToInMsgs = _BosSnoopStatsRxSsmToInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 11),
    _BosSnoopStatsRxSsmToInMsgs_Type()
)
bosSnoopStatsRxSsmToInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxSsmToInMsgs.setStatus("current")
_BosSnoopStatsRxSsmToExMsgs_Type = Counter32
_BosSnoopStatsRxSsmToExMsgs_Object = MibTableColumn
bosSnoopStatsRxSsmToExMsgs = _BosSnoopStatsRxSsmToExMsgs_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 12),
    _BosSnoopStatsRxSsmToExMsgs_Type()
)
bosSnoopStatsRxSsmToExMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxSsmToExMsgs.setStatus("current")
_BosSnoopStatsRxSsmAllowMsgs_Type = Counter32
_BosSnoopStatsRxSsmAllowMsgs_Object = MibTableColumn
bosSnoopStatsRxSsmAllowMsgs = _BosSnoopStatsRxSsmAllowMsgs_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 13),
    _BosSnoopStatsRxSsmAllowMsgs_Type()
)
bosSnoopStatsRxSsmAllowMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxSsmAllowMsgs.setStatus("current")
_BosSnoopStatsRxSsmBlockMsgs_Type = Counter32
_BosSnoopStatsRxSsmBlockMsgs_Object = MibTableColumn
bosSnoopStatsRxSsmBlockMsgs = _BosSnoopStatsRxSsmBlockMsgs_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 14),
    _BosSnoopStatsRxSsmBlockMsgs_Type()
)
bosSnoopStatsRxSsmBlockMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxSsmBlockMsgs.setStatus("current")
_BosSnoopStatsRxAsmLeaves_Type = Counter32
_BosSnoopStatsRxAsmLeaves_Object = MibTableColumn
bosSnoopStatsRxAsmLeaves = _BosSnoopStatsRxAsmLeaves_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 15),
    _BosSnoopStatsRxAsmLeaves_Type()
)
bosSnoopStatsRxAsmLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsRxAsmLeaves.setStatus("current")
_BosSnoopStatsTxGenQueries_Type = Counter32
_BosSnoopStatsTxGenQueries_Object = MibTableColumn
bosSnoopStatsTxGenQueries = _BosSnoopStatsTxGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 16),
    _BosSnoopStatsTxGenQueries_Type()
)
bosSnoopStatsTxGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsTxGenQueries.setStatus("current")
_BosSnoopStatsTxGrpQueries_Type = Counter32
_BosSnoopStatsTxGrpQueries_Object = MibTableColumn
bosSnoopStatsTxGrpQueries = _BosSnoopStatsTxGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 17),
    _BosSnoopStatsTxGrpQueries_Type()
)
bosSnoopStatsTxGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsTxGrpQueries.setStatus("current")
_BosSnoopStatsTxAsmReports_Type = Counter32
_BosSnoopStatsTxAsmReports_Object = MibTableColumn
bosSnoopStatsTxAsmReports = _BosSnoopStatsTxAsmReports_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 18),
    _BosSnoopStatsTxAsmReports_Type()
)
bosSnoopStatsTxAsmReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsTxAsmReports.setStatus("current")
_BosSnoopStatsTxSsmReports_Type = Counter32
_BosSnoopStatsTxSsmReports_Object = MibTableColumn
bosSnoopStatsTxSsmReports = _BosSnoopStatsTxSsmReports_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 19),
    _BosSnoopStatsTxSsmReports_Type()
)
bosSnoopStatsTxSsmReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsTxSsmReports.setStatus("current")
_BosSnoopStatsTxAsmLeaves_Type = Counter32
_BosSnoopStatsTxAsmLeaves_Object = MibTableColumn
bosSnoopStatsTxAsmLeaves = _BosSnoopStatsTxAsmLeaves_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 20),
    _BosSnoopStatsTxAsmLeaves_Type()
)
bosSnoopStatsTxAsmLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsTxAsmLeaves.setStatus("current")
_BosSnoopStatsDroppedPkts_Type = Counter32
_BosSnoopStatsDroppedPkts_Object = MibTableColumn
bosSnoopStatsDroppedPkts = _BosSnoopStatsDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 21),
    _BosSnoopStatsDroppedPkts_Type()
)
bosSnoopStatsDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsDroppedPkts.setStatus("current")
_BosSnoopStatsValidPkts_Type = Counter32
_BosSnoopStatsValidPkts_Object = MibScalar
bosSnoopStatsValidPkts = _BosSnoopStatsValidPkts_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 105, 4, 1, 1, 22),
    _BosSnoopStatsValidPkts_Type()
)
bosSnoopStatsValidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosSnoopStatsValidPkts.setStatus("current")
_Bosrtm_ObjectIdentity = ObjectIdentity
bosrtm = _Bosrtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107)
)
_BosrrdScalar_ObjectIdentity = ObjectIdentity
bosrrdScalar = _BosrrdScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 1)
)
_BosRrdRouterId_Type = IpAddress
_BosRrdRouterId_Object = MibScalar
bosRrdRouterId = _BosRrdRouterId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 1, 1),
    _BosRrdRouterId_Type()
)
bosRrdRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdRouterId.setStatus("current")


class _BosRrdFilterByOspfTag_Type(Integer32):
    """Custom type bosRrdFilterByOspfTag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosRrdFilterByOspfTag_Type.__name__ = "Integer32"
_BosRrdFilterByOspfTag_Object = MibScalar
bosRrdFilterByOspfTag = _BosRrdFilterByOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 1, 2),
    _BosRrdFilterByOspfTag_Type()
)
bosRrdFilterByOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdFilterByOspfTag.setStatus("current")
_BosRrdFilterOspfTag_Type = Integer32
_BosRrdFilterOspfTag_Object = MibScalar
bosRrdFilterOspfTag = _BosRrdFilterOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 1, 3),
    _BosRrdFilterOspfTag_Type()
)
bosRrdFilterOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdFilterOspfTag.setStatus("current")


class _BosRrdFilterOspfTagMask_Type(Integer32):
    """Custom type bosRrdFilterOspfTagMask based on Integer32"""
    defaultValue = -1


_BosRrdFilterOspfTagMask_Type.__name__ = "Integer32"
_BosRrdFilterOspfTagMask_Object = MibScalar
bosRrdFilterOspfTagMask = _BosRrdFilterOspfTagMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 1, 4),
    _BosRrdFilterOspfTagMask_Type()
)
bosRrdFilterOspfTagMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdFilterOspfTagMask.setStatus("current")


class _BosRrdRouterASNumber_Type(Integer32):
    """Custom type bosRrdRouterASNumber based on Integer32"""
    defaultValue = 0


_BosRrdRouterASNumber_Type.__name__ = "Integer32"
_BosRrdRouterASNumber_Object = MibScalar
bosRrdRouterASNumber = _BosRrdRouterASNumber_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 1, 5),
    _BosRrdRouterASNumber_Type()
)
bosRrdRouterASNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdRouterASNumber.setStatus("current")


class _BosRrdAdminStatus_Type(Integer32):
    """Custom type bosRrdAdminStatus based on Integer32"""
    defaultValue = 2

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


_BosRrdAdminStatus_Type.__name__ = "Integer32"
_BosRrdAdminStatus_Object = MibScalar
bosRrdAdminStatus = _BosRrdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 1, 6),
    _BosRrdAdminStatus_Type()
)
bosRrdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdAdminStatus.setStatus("current")
_BosRrdControlTable_Object = MibTable
bosRrdControlTable = _BosRrdControlTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 2)
)
if mibBuilder.loadTexts:
    bosRrdControlTable.setStatus("current")
_BosRrdControlEntry_Object = MibTableRow
bosRrdControlEntry = _BosRrdControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 2, 1)
)
bosRrdControlEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosRrdControlDestIpAddress"),
    (0, "BLADEOS-BASE-MIB", "bosRrdControlNetMask"),
)
if mibBuilder.loadTexts:
    bosRrdControlEntry.setStatus("current")
_BosRrdControlDestIpAddress_Type = IpAddress
_BosRrdControlDestIpAddress_Object = MibTableColumn
bosRrdControlDestIpAddress = _BosRrdControlDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 2, 1, 1),
    _BosRrdControlDestIpAddress_Type()
)
bosRrdControlDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosRrdControlDestIpAddress.setStatus("current")
_BosRrdControlNetMask_Type = IpAddress
_BosRrdControlNetMask_Object = MibTableColumn
bosRrdControlNetMask = _BosRrdControlNetMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 2, 1, 2),
    _BosRrdControlNetMask_Type()
)
bosRrdControlNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosRrdControlNetMask.setStatus("current")


class _BosRrdControlSourceProto_Type(Integer32):
    """Custom type bosRrdControlSourceProto based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("any", 0),
          ("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16))
    )


_BosRrdControlSourceProto_Type.__name__ = "Integer32"
_BosRrdControlSourceProto_Object = MibTableColumn
bosRrdControlSourceProto = _BosRrdControlSourceProto_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 2, 1, 3),
    _BosRrdControlSourceProto_Type()
)
bosRrdControlSourceProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdControlSourceProto.setStatus("current")


class _BosRrdControlDestProto_Type(Integer32):
    """Custom type bosRrdControlDestProto based on Integer32"""
    defaultValue = 0


_BosRrdControlDestProto_Type.__name__ = "Integer32"
_BosRrdControlDestProto_Object = MibTableColumn
bosRrdControlDestProto = _BosRrdControlDestProto_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 2, 1, 4),
    _BosRrdControlDestProto_Type()
)
bosRrdControlDestProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdControlDestProto.setStatus("current")


class _BosRrdControlRouteExportFlag_Type(Integer32):
    """Custom type bosRrdControlRouteExportFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_BosRrdControlRouteExportFlag_Type.__name__ = "Integer32"
_BosRrdControlRouteExportFlag_Object = MibTableColumn
bosRrdControlRouteExportFlag = _BosRrdControlRouteExportFlag_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 2, 1, 5),
    _BosRrdControlRouteExportFlag_Type()
)
bosRrdControlRouteExportFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdControlRouteExportFlag.setStatus("current")
_BosRrdControlRowStatus_Type = RowStatus
_BosRrdControlRowStatus_Object = MibTableColumn
bosRrdControlRowStatus = _BosRrdControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 2, 1, 6),
    _BosRrdControlRowStatus_Type()
)
bosRrdControlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdControlRowStatus.setStatus("current")
_BosRrdRoutingProtoTable_Object = MibTable
bosRrdRoutingProtoTable = _BosRrdRoutingProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 3)
)
if mibBuilder.loadTexts:
    bosRrdRoutingProtoTable.setStatus("current")
_BosRrdRoutingProtoEntry_Object = MibTableRow
bosRrdRoutingProtoEntry = _BosRrdRoutingProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 3, 1)
)
bosRrdRoutingProtoEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosRrdRoutingProtoId"),
)
if mibBuilder.loadTexts:
    bosRrdRoutingProtoEntry.setStatus("current")


class _BosRrdRoutingProtoId_Type(Integer32):
    """Custom type bosRrdRoutingProtoId based on Integer32"""
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
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16))
    )


_BosRrdRoutingProtoId_Type.__name__ = "Integer32"
_BosRrdRoutingProtoId_Object = MibTableColumn
bosRrdRoutingProtoId = _BosRrdRoutingProtoId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 3, 1, 1),
    _BosRrdRoutingProtoId_Type()
)
bosRrdRoutingProtoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosRrdRoutingProtoId.setStatus("current")
_BosRrdRoutingRegnId_Type = Integer32
_BosRrdRoutingRegnId_Object = MibTableColumn
bosRrdRoutingRegnId = _BosRrdRoutingRegnId_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 3, 1, 2),
    _BosRrdRoutingRegnId_Type()
)
bosRrdRoutingRegnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRrdRoutingRegnId.setStatus("current")
_BosRrdRoutingProtoTaskIdent_Type = OctetString
_BosRrdRoutingProtoTaskIdent_Object = MibTableColumn
bosRrdRoutingProtoTaskIdent = _BosRrdRoutingProtoTaskIdent_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 3, 1, 3),
    _BosRrdRoutingProtoTaskIdent_Type()
)
bosRrdRoutingProtoTaskIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRrdRoutingProtoTaskIdent.setStatus("current")
_BosRrdRoutingProtoQueueIdent_Type = OctetString
_BosRrdRoutingProtoQueueIdent_Object = MibTableColumn
bosRrdRoutingProtoQueueIdent = _BosRrdRoutingProtoQueueIdent_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 3, 1, 4),
    _BosRrdRoutingProtoQueueIdent_Type()
)
bosRrdRoutingProtoQueueIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRrdRoutingProtoQueueIdent.setStatus("current")


class _BosRrdAllowOspfAreaRoutes_Type(Integer32):
    """Custom type bosRrdAllowOspfAreaRoutes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosRrdAllowOspfAreaRoutes_Type.__name__ = "Integer32"
_BosRrdAllowOspfAreaRoutes_Object = MibTableColumn
bosRrdAllowOspfAreaRoutes = _BosRrdAllowOspfAreaRoutes_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 3, 1, 5),
    _BosRrdAllowOspfAreaRoutes_Type()
)
bosRrdAllowOspfAreaRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdAllowOspfAreaRoutes.setStatus("current")


class _BosRrdAllowOspfExtRoutes_Type(Integer32):
    """Custom type bosRrdAllowOspfExtRoutes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BosRrdAllowOspfExtRoutes_Type.__name__ = "Integer32"
_BosRrdAllowOspfExtRoutes_Object = MibTableColumn
bosRrdAllowOspfExtRoutes = _BosRrdAllowOspfExtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 3, 1, 6),
    _BosRrdAllowOspfExtRoutes_Type()
)
bosRrdAllowOspfExtRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosRrdAllowOspfExtRoutes.setStatus("current")
_BosRtmCommonRouteTable_Object = MibTable
bosRtmCommonRouteTable = _BosRtmCommonRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4)
)
if mibBuilder.loadTexts:
    bosRtmCommonRouteTable.setStatus("current")
_BosRtmCommonRouteEntry_Object = MibTableRow
bosRtmCommonRouteEntry = _BosRtmCommonRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1)
)
bosRtmCommonRouteEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "bosRtmCommonRouteDest"),
    (0, "BLADEOS-BASE-MIB", "bosRtmCommonRouteMask"),
    (0, "BLADEOS-BASE-MIB", "bosRtmCommonRouteTos"),
    (0, "BLADEOS-BASE-MIB", "bosRtmCommonRouteNextHop"),
)
if mibBuilder.loadTexts:
    bosRtmCommonRouteEntry.setStatus("current")
_BosRtmCommonRouteDest_Type = IpAddress
_BosRtmCommonRouteDest_Object = MibTableColumn
bosRtmCommonRouteDest = _BosRtmCommonRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 1),
    _BosRtmCommonRouteDest_Type()
)
bosRtmCommonRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosRtmCommonRouteDest.setStatus("current")
_BosRtmCommonRouteMask_Type = IpAddress
_BosRtmCommonRouteMask_Object = MibTableColumn
bosRtmCommonRouteMask = _BosRtmCommonRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 2),
    _BosRtmCommonRouteMask_Type()
)
bosRtmCommonRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosRtmCommonRouteMask.setStatus("current")


class _BosRtmCommonRouteTos_Type(Integer32):
    """Custom type bosRtmCommonRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BosRtmCommonRouteTos_Type.__name__ = "Integer32"
_BosRtmCommonRouteTos_Object = MibTableColumn
bosRtmCommonRouteTos = _BosRtmCommonRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 3),
    _BosRtmCommonRouteTos_Type()
)
bosRtmCommonRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosRtmCommonRouteTos.setStatus("current")
_BosRtmCommonRouteNextHop_Type = IpAddress
_BosRtmCommonRouteNextHop_Object = MibTableColumn
bosRtmCommonRouteNextHop = _BosRtmCommonRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 4),
    _BosRtmCommonRouteNextHop_Type()
)
bosRtmCommonRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bosRtmCommonRouteNextHop.setStatus("current")


class _BosRtmCommonRouteIfIndex_Type(Integer32):
    """Custom type bosRtmCommonRouteIfIndex based on Integer32"""
    defaultValue = 0


_BosRtmCommonRouteIfIndex_Type.__name__ = "Integer32"
_BosRtmCommonRouteIfIndex_Object = MibTableColumn
bosRtmCommonRouteIfIndex = _BosRtmCommonRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 5),
    _BosRtmCommonRouteIfIndex_Type()
)
bosRtmCommonRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosRtmCommonRouteIfIndex.setStatus("current")


class _BosRtmCommonRouteType_Type(Integer32):
    """Custom type bosRtmCommonRouteType based on Integer32"""
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
          ("reject", 2),
          ("local", 3),
          ("remote", 4))
    )


_BosRtmCommonRouteType_Type.__name__ = "Integer32"
_BosRtmCommonRouteType_Object = MibTableColumn
bosRtmCommonRouteType = _BosRtmCommonRouteType_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 6),
    _BosRtmCommonRouteType_Type()
)
bosRtmCommonRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosRtmCommonRouteType.setStatus("current")


class _BosRtmCommonRouteProto_Type(Integer32):
    """Custom type bosRtmCommonRouteProto based on Integer32"""
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
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16))
    )


_BosRtmCommonRouteProto_Type.__name__ = "Integer32"
_BosRtmCommonRouteProto_Object = MibTableColumn
bosRtmCommonRouteProto = _BosRtmCommonRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 7),
    _BosRtmCommonRouteProto_Type()
)
bosRtmCommonRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRtmCommonRouteProto.setStatus("current")


class _BosRtmCommonRouteAge_Type(Integer32):
    """Custom type bosRtmCommonRouteAge based on Integer32"""
    defaultValue = 0


_BosRtmCommonRouteAge_Type.__name__ = "Integer32"
_BosRtmCommonRouteAge_Object = MibTableColumn
bosRtmCommonRouteAge = _BosRtmCommonRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 8),
    _BosRtmCommonRouteAge_Type()
)
bosRtmCommonRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bosRtmCommonRouteAge.setStatus("current")
_BosRtmCommonRouteInfo_Type = ObjectIdentifier
_BosRtmCommonRouteInfo_Object = MibTableColumn
bosRtmCommonRouteInfo = _BosRtmCommonRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 9),
    _BosRtmCommonRouteInfo_Type()
)
bosRtmCommonRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosRtmCommonRouteInfo.setStatus("current")


class _BosRtmCommonRouteNextHopAS_Type(Integer32):
    """Custom type bosRtmCommonRouteNextHopAS based on Integer32"""
    defaultValue = 0


_BosRtmCommonRouteNextHopAS_Type.__name__ = "Integer32"
_BosRtmCommonRouteNextHopAS_Object = MibTableColumn
bosRtmCommonRouteNextHopAS = _BosRtmCommonRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 10),
    _BosRtmCommonRouteNextHopAS_Type()
)
bosRtmCommonRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosRtmCommonRouteNextHopAS.setStatus("current")


class _BosRtmCommonRouteMetric1_Type(Integer32):
    """Custom type bosRtmCommonRouteMetric1 based on Integer32"""
    defaultValue = -1


_BosRtmCommonRouteMetric1_Type.__name__ = "Integer32"
_BosRtmCommonRouteMetric1_Object = MibTableColumn
bosRtmCommonRouteMetric1 = _BosRtmCommonRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 11),
    _BosRtmCommonRouteMetric1_Type()
)
bosRtmCommonRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosRtmCommonRouteMetric1.setStatus("current")
_BosRtmCommonRoutePrivateStatus_Type = TruthValue
_BosRtmCommonRoutePrivateStatus_Object = MibTableColumn
bosRtmCommonRoutePrivateStatus = _BosRtmCommonRoutePrivateStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 12),
    _BosRtmCommonRoutePrivateStatus_Type()
)
bosRtmCommonRoutePrivateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosRtmCommonRoutePrivateStatus.setStatus("current")
_BosRtmCommonRouteStatus_Type = RowStatus
_BosRtmCommonRouteStatus_Object = MibTableColumn
bosRtmCommonRouteStatus = _BosRtmCommonRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 107, 4, 1, 13),
    _BosRtmCommonRouteStatus_Type()
)
bosRtmCommonRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bosRtmCommonRouteStatus.setStatus("current")
_Bosarp_ObjectIdentity = ObjectIdentity
bosarp = _Bosarp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 109)
)
_Arp_ObjectIdentity = ObjectIdentity
arp = _Arp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 109, 1)
)


class _BosArpCacheTimeout_Type(Integer32):
    """Custom type bosArpCacheTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_BosArpCacheTimeout_Type.__name__ = "Integer32"
_BosArpCacheTimeout_Object = MibScalar
bosArpCacheTimeout = _BosArpCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 109, 1, 1),
    _BosArpCacheTimeout_Type()
)
bosArpCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosArpCacheTimeout.setStatus("current")


class _BosArpCachePendTime_Type(Integer32):
    """Custom type bosArpCachePendTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3000),
    )


_BosArpCachePendTime_Type.__name__ = "Integer32"
_BosArpCachePendTime_Object = MibScalar
bosArpCachePendTime = _BosArpCachePendTime_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 109, 1, 2),
    _BosArpCachePendTime_Type()
)
bosArpCachePendTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosArpCachePendTime.setStatus("current")


class _BosArpMaxRetries_Type(Integer32):
    """Custom type bosArpMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_BosArpMaxRetries_Type.__name__ = "Integer32"
_BosArpMaxRetries_Object = MibScalar
bosArpMaxRetries = _BosArpMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 109, 1, 3),
    _BosArpMaxRetries_Type()
)
bosArpMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bosArpMaxRetries.setStatus("current")
_Bossnmp3_ObjectIdentity = ObjectIdentity
bossnmp3 = _Bossnmp3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112)
)
_SnmpInInformResponses_Type = Counter32
_SnmpInInformResponses_Object = MibScalar
snmpInInformResponses = _SnmpInInformResponses_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 1),
    _SnmpInInformResponses_Type()
)
snmpInInformResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInInformResponses.setStatus("current")
_SnmpOutInformRequests_Type = Counter32
_SnmpOutInformRequests_Object = MibScalar
snmpOutInformRequests = _SnmpOutInformRequests_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 2),
    _SnmpOutInformRequests_Type()
)
snmpOutInformRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutInformRequests.setStatus("current")
_SnmpInformDrops_Type = Counter32
_SnmpInformDrops_Object = MibScalar
snmpInformDrops = _SnmpInformDrops_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 3),
    _SnmpInformDrops_Type()
)
snmpInformDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformDrops.setStatus("current")
_SnmpInformAwaitingAck_Type = Counter32
_SnmpInformAwaitingAck_Object = MibScalar
snmpInformAwaitingAck = _SnmpInformAwaitingAck_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 4),
    _SnmpInformAwaitingAck_Type()
)
snmpInformAwaitingAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformAwaitingAck.setStatus("current")
_SnmpInformCntTable_Object = MibTable
snmpInformCntTable = _SnmpInformCntTable_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 5)
)
if mibBuilder.loadTexts:
    snmpInformCntTable.setStatus("current")
_SnmpInformCntEntry_Object = MibTableRow
snmpInformCntEntry = _SnmpInformCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 5, 1)
)
snmpInformCntEntry.setIndexNames(
    (0, "BLADEOS-BASE-MIB", "snmpInformTgtAddrName"),
)
if mibBuilder.loadTexts:
    snmpInformCntEntry.setStatus("current")


class _SnmpInformTgtAddrName_Type(SnmpAdminString):
    """Custom type snmpInformTgtAddrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpInformTgtAddrName_Type.__name__ = "SnmpAdminString"
_SnmpInformTgtAddrName_Object = MibTableColumn
snmpInformTgtAddrName = _SnmpInformTgtAddrName_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 5, 1, 1),
    _SnmpInformTgtAddrName_Type()
)
snmpInformTgtAddrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpInformTgtAddrName.setStatus("current")
_SnmpInformSent_Type = Counter32
_SnmpInformSent_Object = MibTableColumn
snmpInformSent = _SnmpInformSent_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 5, 1, 2),
    _SnmpInformSent_Type()
)
snmpInformSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformSent.setStatus("current")
_SnmpInformAwaitAck_Type = Counter32
_SnmpInformAwaitAck_Object = MibTableColumn
snmpInformAwaitAck = _SnmpInformAwaitAck_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 5, 1, 3),
    _SnmpInformAwaitAck_Type()
)
snmpInformAwaitAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformAwaitAck.setStatus("current")
_SnmpInformRetried_Type = Counter32
_SnmpInformRetried_Object = MibTableColumn
snmpInformRetried = _SnmpInformRetried_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 5, 1, 4),
    _SnmpInformRetried_Type()
)
snmpInformRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformRetried.setStatus("current")
_SnmpInformDropped_Type = Counter32
_SnmpInformDropped_Object = MibTableColumn
snmpInformDropped = _SnmpInformDropped_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 5, 1, 5),
    _SnmpInformDropped_Type()
)
snmpInformDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformDropped.setStatus("current")
_SnmpInformFailed_Type = Counter32
_SnmpInformFailed_Object = MibTableColumn
snmpInformFailed = _SnmpInformFailed_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 5, 1, 6),
    _SnmpInformFailed_Type()
)
snmpInformFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformFailed.setStatus("current")
_SnmpInformResponses_Type = Counter32
_SnmpInformResponses_Object = MibTableColumn
snmpInformResponses = _SnmpInformResponses_Object(
    (1, 3, 6, 1, 4, 1, 26543, 100, 112, 5, 1, 7),
    _SnmpInformResponses_Type()
)
snmpInformResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformResponses.setStatus("current")
bosMstMstiInstanceIndex.registerAugmentions(
    ("BLADEOS-BASE-MIB",
     "bosMstMstiBridgeEntry")
)
bosMstMstiBridgeEntry.setIndexNames(*bosMstMstiInstanceIndex.getIndexNames())

# Managed Objects groups


# Notification objects

fmLowTimerResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 4, 0, 1)
)
fmLowTimerResource.setObjects(
    ("BLADEOS-BASE-MIB", "fmTimerReqFailCount")
)
if mibBuilder.loadTexts:
    fmLowTimerResource.setStatus(
        "deprecated"
    )

fmLowBufferResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 4, 0, 2)
)
fmLowBufferResource.setObjects(
    ("BLADEOS-BASE-MIB", "fmMemAllocFailCount")
)
if mibBuilder.loadTexts:
    fmLowBufferResource.setStatus(
        "deprecated"
    )

ffStaticEntryInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 27, 4, 0, 3)
)
ffStaticEntryInvalid.setObjects(
      *(("BLADEOS-BASE-MIB", "ffHostCacheIfIndex"),
        ("BLADEOS-BASE-MIB", "ffHostCacheEntryType"))
)
if mibBuilder.loadTexts:
    ffStaticEntryInvalid.setStatus(
        "deprecated"
    )

bosLaLacpParamMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 63, 4, 0, 1)
)
bosLaLacpParamMismatchTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosLaPortIndex"),
        ("BLADEOS-BASE-MIB", "bosLaPortIndex"))
)
if mibBuilder.loadTexts:
    bosLaLacpParamMismatchTrap.setStatus(
        "current"
    )

bosPvrstGlobalErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 3, 0, 1)
)
bosPvrstGlobalErrTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosPvrstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosPvrstGlobalErrTrapType"))
)
if mibBuilder.loadTexts:
    bosPvrstGlobalErrTrap.setStatus(
        "current"
    )

bosPvrstGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 3, 0, 2)
)
bosPvrstGenTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosPvrstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosPvrstGenTrapType"))
)
if mibBuilder.loadTexts:
    bosPvrstGenTrap.setStatus(
        "current"
    )

bosPvrstNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 3, 0, 3)
)
bosPvrstNewRootTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosPvrstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosPvrstInstDesignatedRoot"),
        ("BLADEOS-BASE-MIB", "bosPvrstInstInstanceIndex"))
)
if mibBuilder.loadTexts:
    bosPvrstNewRootTrap.setStatus(
        "current"
    )

bosPvrstTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 3, 0, 4)
)
bosPvrstTopologyChgTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosPvrstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosPvrstInstInstanceIndex"))
)
if mibBuilder.loadTexts:
    bosPvrstTopologyChgTrap.setStatus(
        "current"
    )

bosPvrstProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 3, 0, 5)
)
bosPvrstProtocolMigrationTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosPvrstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosPvrstPortTrapIndex"),
        ("BLADEOS-BASE-MIB", "bosPvrstPortMigrationType"),
        ("BLADEOS-BASE-MIB", "bosPvrstInstInstanceIndex"))
)
if mibBuilder.loadTexts:
    bosPvrstProtocolMigrationTrap.setStatus(
        "current"
    )

bosPvrstInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 78, 3, 0, 6)
)
bosPvrstInvalidBpduRxdTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosPvrstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosPvrstPortTrapIndex"),
        ("BLADEOS-BASE-MIB", "bosPvrstPktErrType"),
        ("BLADEOS-BASE-MIB", "bosPvrstPktErrVal"))
)
if mibBuilder.loadTexts:
    bosPvrstInvalidBpduRxdTrap.setStatus(
        "current"
    )

bosRstGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 3, 0, 1)
)
bosRstGenTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "dot1dBaseBridgeAddress"),
        ("BLADEOS-BASE-MIB", "bosRstGenTrapType"))
)
if mibBuilder.loadTexts:
    bosRstGenTrap.setStatus(
        "current"
    )

bosRstErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 3, 0, 2)
)
bosRstErrTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "dot1dBaseBridgeAddress"),
        ("BLADEOS-BASE-MIB", "bosRstErrTrapType"))
)
if mibBuilder.loadTexts:
    bosRstErrTrap.setStatus(
        "current"
    )

bosRstNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 3, 0, 3)
)
bosRstNewRootTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "dot1dBaseBridgeAddress"),
        ("BLADEOS-BASE-MIB", "bosRstOldDesignatedRoot"),
        ("BLADEOS-BASE-MIB", "dot1dStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    bosRstNewRootTrap.setStatus(
        "current"
    )

bosRstTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 3, 0, 4)
)
bosRstTopologyChgTrap.setObjects(
    ("BLADEOS-BASE-MIB", "dot1dBaseBridgeAddress")
)
if mibBuilder.loadTexts:
    bosRstTopologyChgTrap.setStatus(
        "current"
    )

bosRstProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 3, 0, 5)
)
bosRstProtocolMigrationTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "dot1dBaseBridgeAddress"),
        ("BLADEOS-BASE-MIB", "dot1dStpVersion"),
        ("BLADEOS-BASE-MIB", "bosRstPortMigrationType"))
)
if mibBuilder.loadTexts:
    bosRstProtocolMigrationTrap.setStatus(
        "current"
    )

bosRstInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 3, 0, 6)
)
bosRstInvalidBpduRxdTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "dot1dBaseBridgeAddress"),
        ("BLADEOS-BASE-MIB", "bosRstPktErrType"),
        ("BLADEOS-BASE-MIB", "bosRstPktErrVal"))
)
if mibBuilder.loadTexts:
    bosRstInvalidBpduRxdTrap.setStatus(
        "current"
    )

bosRstNewPortRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 79, 3, 0, 7)
)
bosRstNewPortRoleTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "dot1dBaseBridgeAddress"),
        ("BLADEOS-BASE-MIB", "bosRstPortRoleType"),
        ("BLADEOS-BASE-MIB", "bosRstOldRoleType"))
)
if mibBuilder.loadTexts:
    bosRstNewPortRoleTrap.setStatus(
        "current"
    )

bosMstGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 3, 0, 1)
)
bosMstGenTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosMstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosMstGenTrapType"))
)
if mibBuilder.loadTexts:
    bosMstGenTrap.setStatus(
        "current"
    )

bosMstErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 3, 0, 2)
)
bosMstErrTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosMstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosMstErrTrapType"))
)
if mibBuilder.loadTexts:
    bosMstErrTrap.setStatus(
        "current"
    )

bosMstNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 3, 0, 3)
)
bosMstNewRootTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosMstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosMstOldDesignatedRoot"),
        ("BLADEOS-BASE-MIB", "bosMstMstiBridgeRegionalRoot"),
        ("BLADEOS-BASE-MIB", "bosMstMstiInstanceIndex"))
)
if mibBuilder.loadTexts:
    bosMstNewRootTrap.setStatus(
        "current"
    )

bosMstTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 3, 0, 4)
)
bosMstTopologyChgTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosMstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosMstMstiInstanceIndex"))
)
if mibBuilder.loadTexts:
    bosMstTopologyChgTrap.setStatus(
        "current"
    )

bosMstProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 3, 0, 5)
)
bosMstProtocolMigrationTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosMstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosMstPortMigrationType"))
)
if mibBuilder.loadTexts:
    bosMstProtocolMigrationTrap.setStatus(
        "current"
    )

bosMstInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 3, 0, 6)
)
bosMstInvalidBpduRxdTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosMstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosMstPktErrType"),
        ("BLADEOS-BASE-MIB", "bosMstPktErrVal"))
)
if mibBuilder.loadTexts:
    bosMstInvalidBpduRxdTrap.setStatus(
        "current"
    )

bosMstRegionConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 3, 0, 7)
)
bosMstRegionConfigChangeTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosMstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosMstMstiRegionName"),
        ("BLADEOS-BASE-MIB", "bosMstMstiRegionVersion"),
        ("BLADEOS-BASE-MIB", "bosMstMstiConfigDigest"))
)
if mibBuilder.loadTexts:
    bosMstRegionConfigChangeTrap.setStatus(
        "current"
    )

bosMstNewPortRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 80, 3, 0, 8)
)
bosMstNewPortRoleTrap.setObjects(
      *(("BLADEOS-BASE-MIB", "bosMstBrgAddress"),
        ("BLADEOS-BASE-MIB", "bosMstPortRoleType"),
        ("BLADEOS-BASE-MIB", "bosMstOldRoleType"))
)
if mibBuilder.loadTexts:
    bosMstNewPortRoleTrap.setStatus(
        "current"
    )

bosSwTempExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 16, 1)
)
bosSwTempExceedThreshold.setObjects(
      *(("BLADEOS-BASE-MIB", "hwTemperatureSensor1"),
        ("BLADEOS-BASE-MIB", "hwTemperatureSensor2"))
)
if mibBuilder.loadTexts:
    bosSwTempExceedThreshold.setStatus(
        "current"
    )

bosSwFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 16, 2)
)
bosSwFanFailure.setObjects(
      *(("BLADEOS-BASE-MIB", "hwFan1RPMValue"),
        ("BLADEOS-BASE-MIB", "hwFan2RPMValue"),
        ("BLADEOS-BASE-MIB", "hwFan3RPMValue"),
        ("BLADEOS-BASE-MIB", "hwFan4RPMValue"))
)
if mibBuilder.loadTexts:
    bosSwFanFailure.setStatus(
        "current"
    )

bosSwPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 26543, 100, 100, 16, 3)
)
bosSwPowerSupplyFailure.setObjects(
      *(("BLADEOS-BASE-MIB", "hwPowerSupply1State"),
        ("BLADEOS-BASE-MIB", "hwPowerSupply2State"))
)
if mibBuilder.loadTexts:
    bosSwPowerSupplyFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLADEOS-BASE-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "PortLaMode": PortLaMode,
       "LacpKey": LacpKey,
       "LacpState": LacpState,
       "PaeControlledPortStatus": PaeControlledPortStatus,
       "AuthenticMethod": AuthenticMethod,
       "PermissionType": PermissionType,
       "VlanId": VlanId,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "EnabledStatus": EnabledStatus,
       "BosKeyChange": BosKeyChange,
       "SnmpTagValue": SnmpTagValue,
       "SnmpTagList": SnmpTagList,
       "blade": blade,
       "productID": productID,
       "bladeip": bladeip,
       "bosip": bosip,
       "bosIpInLengthErrors": bosIpInLengthErrors,
       "bosIpInCksumErrors": bosIpInCksumErrors,
       "bosIpInVersionErrors": bosIpInVersionErrors,
       "bosIpInTTLErrors": bosIpInTTLErrors,
       "bosIpInOptionErrors": bosIpInOptionErrors,
       "bosIpInBroadCasts": bosIpInBroadCasts,
       "bosIpOutGenErrors": bosIpOutGenErrors,
       "bosIpOptProcEnable": bosIpOptProcEnable,
       "bosIpNumMultipath": bosIpNumMultipath,
       "bosIpLoadShareEnable": bosIpLoadShareEnable,
       "bosIpEnablePMTUD": bosIpEnablePMTUD,
       "bosIpPmtuEntryAge": bosIpPmtuEntryAge,
       "bosIpPmtuTableSize": bosIpPmtuTableSize,
       "bosIpTraceConfigTable": bosIpTraceConfigTable,
       "bosIpTraceConfigEntry": bosIpTraceConfigEntry,
       "bosIpTraceConfigIndex": bosIpTraceConfigIndex,
       "bosIpTraceConfigDest": bosIpTraceConfigDest,
       "bosIpTraceConfigAdminStatus": bosIpTraceConfigAdminStatus,
       "bosIpTraceConfigMaxTTL": bosIpTraceConfigMaxTTL,
       "bosIpTraceConfigMinTTL": bosIpTraceConfigMinTTL,
       "bosIpTraceConfigOperStatus": bosIpTraceConfigOperStatus,
       "bosIpTraceConfigTimeout": bosIpTraceConfigTimeout,
       "bosIpTraceConfigMtu": bosIpTraceConfigMtu,
       "bosIpTraceConfigPort": bosIpTraceConfigPort,
       "bosIpTraceTable": bosIpTraceTable,
       "bosIpTraceEntry": bosIpTraceEntry,
       "bosIpTraceDest": bosIpTraceDest,
       "bosIpTraceHopCount": bosIpTraceHopCount,
       "bosIpTraceIntermHop": bosIpTraceIntermHop,
       "bosIpTraceReachTime1": bosIpTraceReachTime1,
       "bosIpTraceReachTime2": bosIpTraceReachTime2,
       "bosIpTraceReachTime3": bosIpTraceReachTime3,
       "bosIpAddressTable": bosIpAddressTable,
       "bosIpAddressEntry": bosIpAddressEntry,
       "bosIpAddrTabIfaceId": bosIpAddrTabIfaceId,
       "bosIpAddrTabAddress": bosIpAddrTabAddress,
       "bosIpAddrTabAdvertise": bosIpAddrTabAdvertise,
       "bosIpAddrTabPreflevel": bosIpAddrTabPreflevel,
       "bosIpAddrTabStatus": bosIpAddrTabStatus,
       "bosIpRtrLstTable": bosIpRtrLstTable,
       "bosIpRtrLstEntry": bosIpRtrLstEntry,
       "bosIpRtrLstIface": bosIpRtrLstIface,
       "bosIpRtrLstAddress": bosIpRtrLstAddress,
       "bosIpRtrLstPreflevel": bosIpRtrLstPreflevel,
       "bosIpRtrLstStatic": bosIpRtrLstStatic,
       "bosIpRtrLstStatus": bosIpRtrLstStatus,
       "bosIpPathMtuTable": bosIpPathMtuTable,
       "bosIpPathMtuEntry": bosIpPathMtuEntry,
       "bosIpPmtuDestination": bosIpPmtuDestination,
       "bosIpPmtuTos": bosIpPmtuTos,
       "bosIpPathMtu": bosIpPathMtu,
       "bosIpPmtuDisc": bosIpPmtuDisc,
       "bosIpPmtuEntryStatus": bosIpPmtuEntryStatus,
       "bosIpCommonRoutingTable": bosIpCommonRoutingTable,
       "bosIpCommonRoutingEntry": bosIpCommonRoutingEntry,
       "bosIpRouteDest": bosIpRouteDest,
       "bosIpRouteMask": bosIpRouteMask,
       "bosIpRouteTos": bosIpRouteTos,
       "bosIpRouteNextHop": bosIpRouteNextHop,
       "bosIpRouteProto": bosIpRouteProto,
       "bosIpRouteProtoInstanceId": bosIpRouteProtoInstanceId,
       "bosIpRouteIfIndex": bosIpRouteIfIndex,
       "bosIpRouteType": bosIpRouteType,
       "bosIpRouteAge": bosIpRouteAge,
       "bosIpRouteNextHopAS": bosIpRouteNextHopAS,
       "bosIpRouteMetric1": bosIpRouteMetric1,
       "bosIpRoutePreference": bosIpRoutePreference,
       "bosIpRouteStatus": bosIpRouteStatus,
       "bosIpifTable": bosIpifTable,
       "bosIpifEntry": bosIpifEntry,
       "bosIpifIndex": bosIpifIndex,
       "bosIpifMaxReasmSize": bosIpifMaxReasmSize,
       "bosIpifIcmpRedirectEnable": bosIpifIcmpRedirectEnable,
       "bosIpifDrtBcastFwdingEnable": bosIpifDrtBcastFwdingEnable,
       "bosicmp": bosicmp,
       "bosIcmpInDomainNameRequests": bosIcmpInDomainNameRequests,
       "bosIcmpInDomainNameReply": bosIcmpInDomainNameReply,
       "bosIcmpOutDomainNameRequests": bosIcmpOutDomainNameRequests,
       "bosIcmpOutDomainNameReply": bosIcmpOutDomainNameReply,
       "bosIcmpDirectQueryEnable": bosIcmpDirectQueryEnable,
       "bosIcmpInSecurityFailures": bosIcmpInSecurityFailures,
       "bosIcmpOutSecurityFailures": bosIcmpOutSecurityFailures,
       "bosudp": bosudp,
       "bosUdpInNoCksum": bosUdpInNoCksum,
       "bosUdpInIcmpErr": bosUdpInIcmpErr,
       "bosUdpInErrCksum": bosUdpInErrCksum,
       "bosUdpInBcast": bosUdpInBcast,
       "bossystemresize": bossystemresize,
       "bosNoOfReassemblyLists": bosNoOfReassemblyLists,
       "bosNoOfFragmentsPerList": bosNoOfFragmentsPerList,
       "boslogandtrace": boslogandtrace,
       "bosIpGlobalDebug": bosIpGlobalDebug,
       "bosntp": bosntp,
       "ntpCfg": ntpCfg,
       "ntpCfgAdminStatus": ntpCfgAdminStatus,
       "ntpCfgPollInterval": ntpCfgPollInterval,
       "ntpCfgPriServer": ntpCfgPriServer,
       "ntpCfgSecServer": ntpCfgSecServer,
       "ntpSysTime": ntpSysTime,
       "ntpLastUpdtTime": ntpLastUpdtTime,
       "ntpLastUpdtServer": ntpLastUpdtServer,
       "ntpServerStatsTable": ntpServerStatsTable,
       "ntpServerStatsEntry": ntpServerStatsEntry,
       "ntpIpAddress": ntpIpAddress,
       "ntpStatSerReq": ntpStatSerReq,
       "ntpStatSerRep": ntpStatSerRep,
       "ntpStatSerUpd": ntpStatSerUpd,
       "ntpSerClearStat": ntpSerClearStat,
       "ntpOps": ntpOps,
       "ntpOpsPollServer": ntpOpsPollServer,
       "bostcp": bostcp,
       "bosTcpTraceDebug": bosTcpTraceDebug,
       "bosTcpConnTable": bosTcpConnTable,
       "bosTcpConnEntry": bosTcpConnEntry,
       "bosTcpConnLocalAddress": bosTcpConnLocalAddress,
       "bosTcpConnLocalPort": bosTcpConnLocalPort,
       "bosTcpConnRemAddress": bosTcpConnRemAddress,
       "bosTcpConnRemPort": bosTcpConnRemPort,
       "bosTcpConnState": bosTcpConnState,
       "bosradius": bosradius,
       "radiusExtClient": radiusExtClient,
       "radiusExtDebugMask": radiusExtDebugMask,
       "radiusMaxNoOfUserEntries": radiusMaxNoOfUserEntries,
       "radiusSecureBackdoorStatus": radiusSecureBackdoorStatus,
       "radiusNewCfgPort": radiusNewCfgPort,
       "radiusExtServerTable": radiusExtServerTable,
       "radiusExtServerEntry": radiusExtServerEntry,
       "radiusExtServerIndex": radiusExtServerIndex,
       "radiusExtServerAddress": radiusExtServerAddress,
       "radiusExtServerType": radiusExtServerType,
       "radiusExtServerSharedSecret": radiusExtServerSharedSecret,
       "radiusExtServerEnabled": radiusExtServerEnabled,
       "radiusExtServerResponseTime": radiusExtServerResponseTime,
       "radiusExtServerMaximumRetransmission": radiusExtServerMaximumRetransmission,
       "radiusExtServerEntryStatus": radiusExtServerEntryStatus,
       "bosBridgeMIB": bosBridgeMIB,
       "dot1dBosBridge": dot1dBosBridge,
       "dot1dBosBase": dot1dBosBase,
       "dot1dBridgeSystemControl": dot1dBridgeSystemControl,
       "dot1dBaseBridgeStatus": dot1dBaseBridgeStatus,
       "dot1dBaseBridgeCRCStatus": dot1dBaseBridgeCRCStatus,
       "dot1dBaseBridgeDebug": dot1dBaseBridgeDebug,
       "dot1dBaseBridgeTrace": dot1dBaseBridgeTrace,
       "dot1dBaseBridgeMaxFwdDbEntries": dot1dBaseBridgeMaxFwdDbEntries,
       "dot1dBosBasePortTable": dot1dBosBasePortTable,
       "dot1dBosBasePortEntry": dot1dBosBasePortEntry,
       "dot1dBosBasePort": dot1dBosBasePort,
       "dot1dBasePortAdminStatus": dot1dBasePortAdminStatus,
       "dot1dBasePortOperStatus": dot1dBasePortOperStatus,
       "dot1dBasePortBcastStatus": dot1dBasePortBcastStatus,
       "dot1dBasePortFilterNumber": dot1dBasePortFilterNumber,
       "dot1dBasePortMcastNumber": dot1dBasePortMcastNumber,
       "dot1dBasePortBcastOutFrames": dot1dBasePortBcastOutFrames,
       "dot1dBasePortMcastOutFrames": dot1dBasePortMcastOutFrames,
       "dot1dBosTp": dot1dBosTp,
       "dot1dBosTpPortTable": dot1dBosTpPortTable,
       "dot1dBosTpPortEntry": dot1dBosTpPortEntry,
       "dot1dBosTpPort": dot1dBosTpPort,
       "dot1dTpPortInProtoDiscards": dot1dTpPortInProtoDiscards,
       "dot1dTpPortInFilterDiscards": dot1dTpPortInFilterDiscards,
       "dot1dTpPortProtocolFilterMask": dot1dTpPortProtocolFilterMask,
       "dot1dFilter": dot1dFilter,
       "dot1dFilterTable": dot1dFilterTable,
       "dot1dFilterEntry": dot1dFilterEntry,
       "dot1dFilterNumber": dot1dFilterNumber,
       "dot1dFilterSrcAddress": dot1dFilterSrcAddress,
       "dot1dFilterSrcMask": dot1dFilterSrcMask,
       "dot1dFilterDstAddress": dot1dFilterDstAddress,
       "dot1dFilterDstMask": dot1dFilterDstMask,
       "dot1dFilterPermiss": dot1dFilterPermiss,
       "dot1dMcast": dot1dMcast,
       "dot1dMcastTable": dot1dMcastTable,
       "dot1dMcastEntry": dot1dMcastEntry,
       "dot1dMlistNumber": dot1dMlistNumber,
       "dot1dMcastMacaddress": dot1dMcastMacaddress,
       "dot1dMcastPermiss": dot1dMcastPermiss,
       "boscfa": boscfa,
       "if": _pysmi_if,
       "ifMaxInterfaces": ifMaxInterfaces,
       "ifMaxPhysInterfaces": ifMaxPhysInterfaces,
       "ifMaxIpInterfaces": ifMaxIpInterfaces,
       "ifMaxMgmInterfaces": ifMaxMgmInterfaces,
       "ifMaxLogicalInterfaces": ifMaxLogicalInterfaces,
       "ifAvailableIndex": ifAvailableIndex,
       "ifMainTable": ifMainTable,
       "ifMainEntry": ifMainEntry,
       "ifMainIndex": ifMainIndex,
       "ifMainType": ifMainType,
       "ifMainMtu": ifMainMtu,
       "ifMainAdminStatus": ifMainAdminStatus,
       "ifMainOperStatus": ifMainOperStatus,
       "ifMainEncapType": ifMainEncapType,
       "ifMainBrgPortType": ifMainBrgPortType,
       "ifMainRowStatus": ifMainRowStatus,
       "ifMainPortName": ifMainPortName,
       "ifMainLinkStateChangeCount": ifMainLinkStateChangeCount,
       "ifMainVlanId": ifMainVlanId,
       "ifMainIntfIpNum": ifMainIntfIpNum,
       "ifIpTable": ifIpTable,
       "ifIpEntry": ifIpEntry,
       "ifIpAddrAllocMethod": ifIpAddrAllocMethod,
       "ifIpAddr": ifIpAddr,
       "ifIpSubnetMask": ifIpSubnetMask,
       "ifIpBroadcastAddr": ifIpBroadcastAddr,
       "ifIpForwardingEnable": ifIpForwardingEnable,
       "ifIpAddrAllocProtocol": ifIpAddrAllocProtocol,
       "ifIvrTable": ifIvrTable,
       "ifIvrEntry": ifIvrEntry,
       "ifIvrBridgedIface": ifIvrBridgedIface,
       "ff": ff,
       "ffFastForwardingEnable": ffFastForwardingEnable,
       "ffCacheSize": ffCacheSize,
       "ffIpChecksumValidationEnable": ffIpChecksumValidationEnable,
       "ffCachePurgeCount": ffCachePurgeCount,
       "ffCacheLastPurgeTime": ffCacheLastPurgeTime,
       "ffStaticEntryInvalidTrapEnable": ffStaticEntryInvalidTrapEnable,
       "ffCurrentStaticEntryInvalidCount": ffCurrentStaticEntryInvalidCount,
       "ffTotalEntryCount": ffTotalEntryCount,
       "ffStaticEntryCount": ffStaticEntryCount,
       "ffTotalPktsFastForwarded": ffTotalPktsFastForwarded,
       "ffHostCacheTable": ffHostCacheTable,
       "ffHostCacheEntry": ffHostCacheEntry,
       "ffHostCacheDestAddr": ffHostCacheDestAddr,
       "ffHostCacheNextHopAddr": ffHostCacheNextHopAddr,
       "ffHostCacheIfIndex": ffHostCacheIfIndex,
       "ffHostCacheNextHopMediaAddr": ffHostCacheNextHopMediaAddr,
       "ffHostCacheHits": ffHostCacheHits,
       "ffHostCacheLastHitTime": ffHostCacheLastHitTime,
       "ffHostCacheEntryType": ffHostCacheEntryType,
       "ffHostCacheRowStatus": ffHostCacheRowStatus,
       "fm": fm,
       "fmMemoryResourceTrapEnable": fmMemoryResourceTrapEnable,
       "fmTimersResourceTrapEnable": fmTimersResourceTrapEnable,
       "fmTracingEnable": fmTracingEnable,
       "fmMemAllocFailCount": fmMemAllocFailCount,
       "fmTimerReqFailCount": fmTimerReqFailCount,
       "traps": traps,
       "trapPrefix": trapPrefix,
       "fmLowTimerResource": fmLowTimerResource,
       "fmLowBufferResource": fmLowBufferResource,
       "ffStaticEntryInvalid": ffStaticEntryInvalid,
       "bosrmon": bosrmon,
       "rmonDebugType": rmonDebugType,
       "rmonEnableStatus": rmonEnableStatus,
       "rmonHwStatsSupp": rmonHwStatsSupp,
       "rmonHwHistorySupp": rmonHwHistorySupp,
       "rmonHwAlarmSupp": rmonHwAlarmSupp,
       "rmonHwHostSupp": rmonHwHostSupp,
       "rmonHwHostTopNSupp": rmonHwHostTopNSupp,
       "rmonHwMatrixSupp": rmonHwMatrixSupp,
       "rmonHwEventSupp": rmonHwEventSupp,
       "bosla": bosla,
       "bosLaSystem": bosLaSystem,
       "bosLaMaxPortsPerPortChannel": bosLaMaxPortsPerPortChannel,
       "bosLaMaxPortChannels": bosLaMaxPortChannels,
       "bosLaActorSystemID": bosLaActorSystemID,
       "bosLaGlobalTimeout": bosLaGlobalTimeout,
       "bosLaHashCfgSmacState": bosLaHashCfgSmacState,
       "bosLaHashCfgDmacState": bosLaHashCfgDmacState,
       "bosLaHashCfgSIpState": bosLaHashCfgSIpState,
       "bosLaHashCfgDIpState": bosLaHashCfgDIpState,
       "bosLaHashCfgSmacDmacState": bosLaHashCfgSmacDmacState,
       "bosLaHashCfgSIpDIpState": bosLaHashCfgSIpDIpState,
       "bosLaPortChannel": bosLaPortChannel,
       "bosLaPortChannelTable": bosLaPortChannelTable,
       "bosLaPortChannelEntry": bosLaPortChannelEntry,
       "bosLaPortChannelIfIndex": bosLaPortChannelIfIndex,
       "bosLaPortChannelGroup": bosLaPortChannelGroup,
       "bosLaPortChannelAdminMacAddress": bosLaPortChannelAdminMacAddress,
       "bosLaPortChannelMacSelection": bosLaPortChannelMacSelection,
       "bosLaPortChannelMode": bosLaPortChannelMode,
       "bosLaPortChannelPortCount": bosLaPortChannelPortCount,
       "bosLaPortChannelActivePortCount": bosLaPortChannelActivePortCount,
       "bosLaPortChannelDefaultPortIndex": bosLaPortChannelDefaultPortIndex,
       "bosLaPort": bosLaPort,
       "bosLaPortTable": bosLaPortTable,
       "bosLaPortEntry": bosLaPortEntry,
       "bosLaPortIndex": bosLaPortIndex,
       "bosLaPortMode": bosLaPortMode,
       "bosLaPortBundleState": bosLaPortBundleState,
       "bosLaPortActorResetAdminState": bosLaPortActorResetAdminState,
       "bosLaPortAggregateWaitTime": bosLaPortAggregateWaitTime,
       "bosLaPortPartnerResetAdminState": bosLaPortPartnerResetAdminState,
       "bosLaPortActorAdminPort": bosLaPortActorAdminPort,
       "bosLaPortRestoreMtu": bosLaPortRestoreMtu,
       "bosLaPortSelectAggregator": bosLaPortSelectAggregator,
       "bosLaTraps": bosLaTraps,
       "bosLaLacpTraps": bosLaLacpTraps,
       "bosLaLacpParamMismatchTrap": bosLaLacpParamMismatchTrap,
       "bospnac": bospnac,
       "bosPnacPaeSystem": bosPnacPaeSystem,
       "bosPnacSystemControl": bosPnacSystemControl,
       "bosPnacTraceOption": bosPnacTraceOption,
       "bosPnacAuthenticServer": bosPnacAuthenticServer,
       "bosPnacNasId": bosPnacNasId,
       "bosPnacPaePortTable": bosPnacPaePortTable,
       "bosPnacPaePortEntry": bosPnacPaePortEntry,
       "bosPnacPaePortNumber": bosPnacPaePortNumber,
       "bosPnacPaePortAuthMode": bosPnacPaePortAuthMode,
       "bosPnacPaePortSupplicantCount": bosPnacPaePortSupplicantCount,
       "bosPnacPaePortUserName": bosPnacPaePortUserName,
       "bosPnacPaePortPassword": bosPnacPaePortPassword,
       "bosPnacPaePortStatus": bosPnacPaePortStatus,
       "bosPnacModuleOperStatus": bosPnacModuleOperStatus,
       "bosPnacPaeAuthenticator": bosPnacPaeAuthenticator,
       "bosPnacAuthSessionTable": bosPnacAuthSessionTable,
       "bosPnacAuthSessionEntry": bosPnacAuthSessionEntry,
       "bosPnacAuthSessionSuppAddress": bosPnacAuthSessionSuppAddress,
       "bosPnacAuthSessionIdentifier": bosPnacAuthSessionIdentifier,
       "bosPnacAuthSessionAuthPaeState": bosPnacAuthSessionAuthPaeState,
       "bosPnacAuthSessionBackendAuthState": bosPnacAuthSessionBackendAuthState,
       "bosPnacAuthSessionPortStatus": bosPnacAuthSessionPortStatus,
       "bosPnacAuthSessionPortNumber": bosPnacAuthSessionPortNumber,
       "bosPnacAuthSessionInitialize": bosPnacAuthSessionInitialize,
       "bosPnacAuthSessionReauthenticate": bosPnacAuthSessionReauthenticate,
       "bosPnacAuthSessionStatsTable": bosPnacAuthSessionStatsTable,
       "bosPnacAuthSessionStatsEntry": bosPnacAuthSessionStatsEntry,
       "bosPnacAuthSessionOctetsRx": bosPnacAuthSessionOctetsRx,
       "bosPnacAuthSessionOctetsTx": bosPnacAuthSessionOctetsTx,
       "bosPnacAuthSessionFramesRx": bosPnacAuthSessionFramesRx,
       "bosPnacAuthSessionFramesTx": bosPnacAuthSessionFramesTx,
       "bosPnacAuthSessionId": bosPnacAuthSessionId,
       "bosPnacAuthSessionAuthenticMethod": bosPnacAuthSessionAuthenticMethod,
       "bosPnacAuthSessionTime": bosPnacAuthSessionTime,
       "bosPnacAuthSessionTerminateCause": bosPnacAuthSessionTerminateCause,
       "bosPnacAuthSessionUserName": bosPnacAuthSessionUserName,
       "bosPnacAuthServer": bosPnacAuthServer,
       "bosPnacASUserConfigTable": bosPnacASUserConfigTable,
       "bosPnacASUserConfigEntry": bosPnacASUserConfigEntry,
       "bosPnacASUserConfigUserName": bosPnacASUserConfigUserName,
       "bosPnacASUserConfigPassword": bosPnacASUserConfigPassword,
       "bosPnacASUserConfigAuthProtocol": bosPnacASUserConfigAuthProtocol,
       "bosPnacASUserConfigAuthTimeout": bosPnacASUserConfigAuthTimeout,
       "bosPnacASUserConfigPortList": bosPnacASUserConfigPortList,
       "bosPnacASUserConfigPermission": bosPnacASUserConfigPermission,
       "bosPnacASUserConfigRowStatus": bosPnacASUserConfigRowStatus,
       "bntufd": bntufd,
       "ufdGeneralCfg": ufdGeneralCfg,
       "ufdFdpCfgState": ufdFdpCfgState,
       "ufdCfgLtMPorts": ufdCfgLtMPorts,
       "ufdCfgLtMTrunks": ufdCfgLtMTrunks,
       "ufdCfgLtMAdminkey": ufdCfgLtMAdminkey,
       "ufdCfgLtDPorts": ufdCfgLtDPorts,
       "ufdCfgLtDTrunks": ufdCfgLtDTrunks,
       "ufdLtDAdminkeyMaxEnt": ufdLtDAdminkeyMaxEnt,
       "ufdLtDAdminkeyCfgTable": ufdLtDAdminkeyCfgTable,
       "ufdLtDAdminkeyCfgTableEntry": ufdLtDAdminkeyCfgTableEntry,
       "ufdLtDAdminkeyCfg": ufdLtDAdminkeyCfg,
       "ufdCfgAddLtMPort": ufdCfgAddLtMPort,
       "ufdCfgRemoveLtMPort": ufdCfgRemoveLtMPort,
       "ufdCfgAddLtMTrunk": ufdCfgAddLtMTrunk,
       "ufdCfgRemoveLtMTrunk": ufdCfgRemoveLtMTrunk,
       "ufdCfgAddLtMAdminkey": ufdCfgAddLtMAdminkey,
       "ufdCfgRemoveLtMAdminkey": ufdCfgRemoveLtMAdminkey,
       "ufdCfgAddLtDPort": ufdCfgAddLtDPort,
       "ufdCfgRemoveLtDPort": ufdCfgRemoveLtDPort,
       "ufdCfgAddLtDTrunk": ufdCfgAddLtDTrunk,
       "ufdCfgRemoveLtDTrunk": ufdCfgRemoveLtDTrunk,
       "ufdCfgAddLtDAdminkey": ufdCfgAddLtDAdminkey,
       "ufdCfgRemoveLtDAdminkey": ufdCfgRemoveLtDAdminkey,
       "ufdCfgGlobalState": ufdCfgGlobalState,
       "ufdStats": ufdStats,
       "ufdNoLtMLinkFailure": ufdNoLtMLinkFailure,
       "ufdNoLtMLinkBlockingState": ufdNoLtMLinkBlockingState,
       "ufdNoLtDAutoDisabled": ufdNoLtDAutoDisabled,
       "ufdClearStats": ufdClearStats,
       "bostacacs": bostacacs,
       "bosTacacsClientScalarGroup": bosTacacsClientScalarGroup,
       "bosTacClntActiveServer": bosTacClntActiveServer,
       "bosTacClntTraceLevel": bosTacClntTraceLevel,
       "bosTacClntRetransmit": bosTacClntRetransmit,
       "bosTacClntStatisticsGroup": bosTacClntStatisticsGroup,
       "bosTacClntAuthenStartRequests": bosTacClntAuthenStartRequests,
       "bosTacClntAuthenContinueRequests": bosTacClntAuthenContinueRequests,
       "bosTacClntAuthenEnableRequests": bosTacClntAuthenEnableRequests,
       "bosTacClntAuthenAbortRequests": bosTacClntAuthenAbortRequests,
       "bosTacClntAuthenPassReceived": bosTacClntAuthenPassReceived,
       "bosTacClntAuthenFailReceived": bosTacClntAuthenFailReceived,
       "bosTacClntAuthenGetUserReceived": bosTacClntAuthenGetUserReceived,
       "bosTacClntAuthenGetPassReceived": bosTacClntAuthenGetPassReceived,
       "bosTacClntAuthenGetDataReceived": bosTacClntAuthenGetDataReceived,
       "bosTacClntAuthenErrorReceived": bosTacClntAuthenErrorReceived,
       "bosTacClntAuthenFollowReceived": bosTacClntAuthenFollowReceived,
       "bosTacClntAuthenRestartReceived": bosTacClntAuthenRestartReceived,
       "bosTacClntAuthenSessionTimouts": bosTacClntAuthenSessionTimouts,
       "bosTacClntAuthorRequests": bosTacClntAuthorRequests,
       "bosTacClntAuthorPassAddReceived": bosTacClntAuthorPassAddReceived,
       "bosTacClntAuthorPassReplReceived": bosTacClntAuthorPassReplReceived,
       "bosTacClntAuthorFailReceived": bosTacClntAuthorFailReceived,
       "bosTacClntAuthorErrorReceived": bosTacClntAuthorErrorReceived,
       "bosTacClntAuthorFollowReceived": bosTacClntAuthorFollowReceived,
       "bosTacClntAuthorSessionTimeouts": bosTacClntAuthorSessionTimeouts,
       "bosTacClntAcctStartRequests": bosTacClntAcctStartRequests,
       "bosTacClntAcctWdRequests": bosTacClntAcctWdRequests,
       "bosTacClntAcctStopRequests": bosTacClntAcctStopRequests,
       "bosTacClntAcctSuccessReceived": bosTacClntAcctSuccessReceived,
       "bosTacClntAcctErrorReceived": bosTacClntAcctErrorReceived,
       "bosTacClntAcctFollowReceived": bosTacClntAcctFollowReceived,
       "bosTacClntAcctSessionTimeouts": bosTacClntAcctSessionTimeouts,
       "bosTacClntMalformedPktsReceived": bosTacClntMalformedPktsReceived,
       "bosTacClntSocketFailures": bosTacClntSocketFailures,
       "bosTacClntConnectionFailures": bosTacClntConnectionFailures,
       "bosTacClntPrivLevelMap": bosTacClntPrivLevelMap,
       "bosTacClntSecureBackdoorStatus": bosTacClntSecureBackdoorStatus,
       "bosTacacsClientTableGroup": bosTacacsClientTableGroup,
       "bosTacClntServerTable": bosTacClntServerTable,
       "bosTacClntServerEntry": bosTacClntServerEntry,
       "bosTacClntServerAddress": bosTacClntServerAddress,
       "bosTacClntServerStatus": bosTacClntServerStatus,
       "bosTacClntServerSingleConnect": bosTacClntServerSingleConnect,
       "bosTacClntServerPort": bosTacClntServerPort,
       "bosTacClntServerTimeout": bosTacClntServerTimeout,
       "bosTacClntServerKey": bosTacClntServerKey,
       "bosPvrstMIB": bosPvrstMIB,
       "bosPvrst": bosPvrst,
       "bosPvrstSystemControl": bosPvrstSystemControl,
       "bosPvrstModuleStatus": bosPvrstModuleStatus,
       "bosPvrstNoOfActiveInstances": bosPvrstNoOfActiveInstances,
       "bosPvrstBrgAddress": bosPvrstBrgAddress,
       "bosPvrstUpCount": bosPvrstUpCount,
       "bosPvrstDownCount": bosPvrstDownCount,
       "bosPvrstTrace": bosPvrstTrace,
       "bosPvrstDebug": bosPvrstDebug,
       "bosPvrstBufferOverFlowCount": bosPvrstBufferOverFlowCount,
       "bosPvrstMemAllocFailureCount": bosPvrstMemAllocFailureCount,
       "bosPvrstUplinkFastStatus": bosPvrstUplinkFastStatus,
       "bosPvrstUplinkFastMaxRate": bosPvrstUplinkFastMaxRate,
       "bosPvrstPortTable": bosPvrstPortTable,
       "bosPvrstPortEntry": bosPvrstPortEntry,
       "bosPvrstPort": bosPvrstPort,
       "bosPvrstPortAdminEdgeStatus": bosPvrstPortAdminEdgeStatus,
       "bosPvrstPortOperEdgePortStatus": bosPvrstPortOperEdgePortStatus,
       "bosPvrstBridgeDetectionSemState": bosPvrstBridgeDetectionSemState,
       "bosPvrstPortAdminPointToPoint": bosPvrstPortAdminPointToPoint,
       "bosPvrstPortOperPointToPoint": bosPvrstPortOperPointToPoint,
       "bosPvrstInstBridgeTable": bosPvrstInstBridgeTable,
       "bosPvrstInstBridgeEntry": bosPvrstInstBridgeEntry,
       "bosPvrstInstInstanceIndex": bosPvrstInstInstanceIndex,
       "bosPvrstInstBridgePriority": bosPvrstInstBridgePriority,
       "bosPvrstInstRootCost": bosPvrstInstRootCost,
       "bosPvrstInstRootPort": bosPvrstInstRootPort,
       "bosPvrstInstBridgeMaxAge": bosPvrstInstBridgeMaxAge,
       "bosPvrstInstBridgeHelloTime": bosPvrstInstBridgeHelloTime,
       "bosPvrstInstBridgeForwardDelay": bosPvrstInstBridgeForwardDelay,
       "bosPvrstInstHoldTime": bosPvrstInstHoldTime,
       "bosPvrstInstTimeSinceTopologyChange": bosPvrstInstTimeSinceTopologyChange,
       "bosPvrstInstTopChanges": bosPvrstInstTopChanges,
       "bosPvrstInstNewRootCount": bosPvrstInstNewRootCount,
       "bosPvrstInstInstanceUpCount": bosPvrstInstInstanceUpCount,
       "bosPvrstInstInstanceDownCount": bosPvrstInstInstanceDownCount,
       "bosPvrstInstPortRoleSelSemState": bosPvrstInstPortRoleSelSemState,
       "bosPvrstInstDesignatedRoot": bosPvrstInstDesignatedRoot,
       "bosPvrstInstRootMaxAge": bosPvrstInstRootMaxAge,
       "bosPvrstInstRootHelloTime": bosPvrstInstRootHelloTime,
       "bosPvrstInstRootForwardDelay": bosPvrstInstRootForwardDelay,
       "bosPvrstInstSetVlanList": bosPvrstInstSetVlanList,
       "bosPvrstInstResetVlanList": bosPvrstInstResetVlanList,
       "bosPvrstInstEnableStatus": bosPvrstInstEnableStatus,
       "bosPvrstInstPortTable": bosPvrstInstPortTable,
       "bosPvrstInstPortEntry": bosPvrstInstPortEntry,
       "bosPvrstInstPortIndex": bosPvrstInstPortIndex,
       "bosPvrstInstPortStatus": bosPvrstInstPortStatus,
       "bosPvrstInstPortPathCost": bosPvrstInstPortPathCost,
       "bosPvrstInstPortPriority": bosPvrstInstPortPriority,
       "bosPvrstInstPortDesignatedRoot": bosPvrstInstPortDesignatedRoot,
       "bosPvrstInstPortDesignatedBridge": bosPvrstInstPortDesignatedBridge,
       "bosPvrstInstPortDesignatedPort": bosPvrstInstPortDesignatedPort,
       "bosPvrstInstPortOperVersion": bosPvrstInstPortOperVersion,
       "bosPvrstInstPortProtocolMigration": bosPvrstInstPortProtocolMigration,
       "bosPvrstInstPortState": bosPvrstInstPortState,
       "bosPvrstInstPortForwardTransitions": bosPvrstInstPortForwardTransitions,
       "bosPvrstInstPortReceivedBpdus": bosPvrstInstPortReceivedBpdus,
       "bosPvrstInstPortRxConfigBpduCount": bosPvrstInstPortRxConfigBpduCount,
       "bosPvrstInstPortRxTcnBpduCount": bosPvrstInstPortRxTcnBpduCount,
       "bosPvrstInstPortTransmittedBpdus": bosPvrstInstPortTransmittedBpdus,
       "bosPvrstInstPortTxConfigBpduCount": bosPvrstInstPortTxConfigBpduCount,
       "bosPvrstInstPortTxTcnBpduCount": bosPvrstInstPortTxTcnBpduCount,
       "bosPvrstInstPortInvalidBpdusRcvd": bosPvrstInstPortInvalidBpdusRcvd,
       "bosPvrstInstPortInvalidConfigBpduRxCount": bosPvrstInstPortInvalidConfigBpduRxCount,
       "bosPvrstInstPortInvalidTcnBpduRxCount": bosPvrstInstPortInvalidTcnBpduRxCount,
       "bosPvrstInstPortTxSemState": bosPvrstInstPortTxSemState,
       "bosPvrstInstPortProtMigrationSemState": bosPvrstInstPortProtMigrationSemState,
       "bosPvrstInstProtocolMigrationCount": bosPvrstInstProtocolMigrationCount,
       "bosPvrstInstPortRole": bosPvrstInstPortRole,
       "bosPvrstInstCurrentPortRole": bosPvrstInstCurrentPortRole,
       "bosPvrstInstPortInfoSemState": bosPvrstInstPortInfoSemState,
       "bosPvrstInstPortRoleTransitionSemState": bosPvrstInstPortRoleTransitionSemState,
       "bosPvrstInstPortStateTransitionSemState": bosPvrstInstPortStateTransitionSemState,
       "bosPvrstInstPortTopologyChangeSemState": bosPvrstInstPortTopologyChangeSemState,
       "bosPvrstInstPortEffectivePortState": bosPvrstInstPortEffectivePortState,
       "bosPvrstInstPortHelloTime": bosPvrstInstPortHelloTime,
       "bosPvrstInstPortMaxAge": bosPvrstInstPortMaxAge,
       "bosPvrstInstPortForwardDelay": bosPvrstInstPortForwardDelay,
       "bosPvrstInstPortHoldTime": bosPvrstInstPortHoldTime,
       "bosPvrstTrapsControl": bosPvrstTrapsControl,
       "bosPvrstSetGlobalTrapOption": bosPvrstSetGlobalTrapOption,
       "bosPvrstGlobalErrTrapType": bosPvrstGlobalErrTrapType,
       "bosPvrstSetTraps": bosPvrstSetTraps,
       "bosPvrstGenTrapType": bosPvrstGenTrapType,
       "bosPvrstPortTrapNotificationTable": bosPvrstPortTrapNotificationTable,
       "bosPvrstPortTrapNotificationEntry": bosPvrstPortTrapNotificationEntry,
       "bosPvrstPortTrapIndex": bosPvrstPortTrapIndex,
       "bosPvrstPortMigrationType": bosPvrstPortMigrationType,
       "bosPvrstPktErrType": bosPvrstPktErrType,
       "bosPvrstPktErrVal": bosPvrstPktErrVal,
       "bosPvrstTraps": bosPvrstTraps,
       "bosPvrstNotifyTraps": bosPvrstNotifyTraps,
       "bosPvrstGlobalErrTrap": bosPvrstGlobalErrTrap,
       "bosPvrstGenTrap": bosPvrstGenTrap,
       "bosPvrstNewRootTrap": bosPvrstNewRootTrap,
       "bosPvrstTopologyChgTrap": bosPvrstTopologyChgTrap,
       "bosPvrstProtocolMigrationTrap": bosPvrstProtocolMigrationTrap,
       "bosPvrstInvalidBpduRxdTrap": bosPvrstInvalidBpduRxdTrap,
       "bosRstMIB": bosRstMIB,
       "dot1wBosRst": dot1wBosRst,
       "bosRstSystemControl": bosRstSystemControl,
       "bosRstModuleStatus": bosRstModuleStatus,
       "bosRstPortExtTable": bosRstPortExtTable,
       "bosRstPortExtEntry": bosRstPortExtEntry,
       "bosRstPort": bosRstPort,
       "bosRstPortRole": bosRstPortRole,
       "bosRstPortOperVersion": bosRstPortOperVersion,
       "bosRstPortRoleTransSmState": bosRstPortRoleTransSmState,
       "bosRstPortStateTransSmState": bosRstPortStateTransSmState,
       "bosRstPortRxRstBpduCount": bosRstPortRxRstBpduCount,
       "bosRstPortRxConfigBpduCount": bosRstPortRxConfigBpduCount,
       "bosRstPortRxTcnBpduCount": bosRstPortRxTcnBpduCount,
       "bosRstPortTxRstBpduCount": bosRstPortTxRstBpduCount,
       "bosRstPortTxConfigBpduCount": bosRstPortTxConfigBpduCount,
       "bosRstPortTxTcnBpduCount": bosRstPortTxTcnBpduCount,
       "bosRstPortInvalidRstBpduRxCount": bosRstPortInvalidRstBpduRxCount,
       "bosRstPortInvalidConfigBpduRxCount": bosRstPortInvalidConfigBpduRxCount,
       "bosRstPortInvalidTcnBpduRxCount": bosRstPortInvalidTcnBpduRxCount,
       "bosRstPortProtocolMigrationCount": bosRstPortProtocolMigrationCount,
       "bosRstPortAutoEdge": bosRstPortAutoEdge,
       "bosRstDynamicPathcostCalculation": bosRstDynamicPathcostCalculation,
       "bosRstOldDesignatedRoot": bosRstOldDesignatedRoot,
       "dot1wBosRstTrapsControl": dot1wBosRstTrapsControl,
       "bosRstSetTraps": bosRstSetTraps,
       "bosRstGenTrapType": bosRstGenTrapType,
       "bosRstErrTrapType": bosRstErrTrapType,
       "bosRstPortTrapNotificationTable": bosRstPortTrapNotificationTable,
       "bosRstPortTrapNotificationEntry": bosRstPortTrapNotificationEntry,
       "bosRstPortTrapIndex": bosRstPortTrapIndex,
       "bosRstPortMigrationType": bosRstPortMigrationType,
       "bosRstPktErrType": bosRstPktErrType,
       "bosRstPktErrVal": bosRstPktErrVal,
       "bosRstPortRoleType": bosRstPortRoleType,
       "bosRstOldRoleType": bosRstOldRoleType,
       "dot1wBosRstTraps": dot1wBosRstTraps,
       "bosRstTraps": bosRstTraps,
       "bosRstGenTrap": bosRstGenTrap,
       "bosRstErrTrap": bosRstErrTrap,
       "bosRstNewRootTrap": bosRstNewRootTrap,
       "bosRstTopologyChgTrap": bosRstTopologyChgTrap,
       "bosRstProtocolMigrationTrap": bosRstProtocolMigrationTrap,
       "bosRstInvalidBpduRxdTrap": bosRstInvalidBpduRxdTrap,
       "bosRstNewPortRoleTrap": bosRstNewPortRoleTrap,
       "bosMstMIB": bosMstMIB,
       "dot1sBosMst": dot1sBosMst,
       "bosMstSystemControl": bosMstSystemControl,
       "bosMstMaxHopCount": bosMstMaxHopCount,
       "bosMstBrgAddress": bosMstBrgAddress,
       "bosMstCistRoot": bosMstCistRoot,
       "bosMstCistRegionalRoot": bosMstCistRegionalRoot,
       "bosMstCistRootCost": bosMstCistRootCost,
       "bosMstCistRegionalRootCost": bosMstCistRegionalRootCost,
       "bosMstCistRootPort": bosMstCistRootPort,
       "bosMstCistBridgePriority": bosMstCistBridgePriority,
       "bosMstCistBridgeMaxAge": bosMstCistBridgeMaxAge,
       "bosMstCistBridgeForwardDelay": bosMstCistBridgeForwardDelay,
       "bosMstCistMaxAge": bosMstCistMaxAge,
       "bosMstCistForwardDelay": bosMstCistForwardDelay,
       "bosMstMstiRegionName": bosMstMstiRegionName,
       "bosMstMstiRegionVersion": bosMstMstiRegionVersion,
       "bosMstMstiConfigDigest": bosMstMstiConfigDigest,
       "bosMstBufferOverFlowCount": bosMstBufferOverFlowCount,
       "bosMstMemAllocFailureCount": bosMstMemAllocFailureCount,
       "bosMstRegionConfigChangeCount": bosMstRegionConfigChangeCount,
       "bosMstCistBridgeRoleSelectionSemState": bosMstCistBridgeRoleSelectionSemState,
       "bosMstCistTopChanges": bosMstCistTopChanges,
       "bosMstCistNewRootBridgeCount": bosMstCistNewRootBridgeCount,
       "bosMstCistHelloTime": bosMstCistHelloTime,
       "bosMstCistBridgeHelloTime": bosMstCistBridgeHelloTime,
       "bosMstMstiBridgeTable": bosMstMstiBridgeTable,
       "bosMstMstiBridgeEntry": bosMstMstiBridgeEntry,
       "bosMstMstiBridgeRegionalRoot": bosMstMstiBridgeRegionalRoot,
       "bosMstMstiBridgePriority": bosMstMstiBridgePriority,
       "bosMstMstiRootCost": bosMstMstiRootCost,
       "bosMstMstiRootPort": bosMstMstiRootPort,
       "bosMstMstiTopChanges": bosMstMstiTopChanges,
       "bosMstMstiNewRootBridgeCount": bosMstMstiNewRootBridgeCount,
       "bosMstMstiBridgeRoleSelectionSemState": bosMstMstiBridgeRoleSelectionSemState,
       "bosMstInstanceUpCount": bosMstInstanceUpCount,
       "bosMstInstanceDownCount": bosMstInstanceDownCount,
       "bosMstOldDesignatedRoot": bosMstOldDesignatedRoot,
       "bosMstVlanInstanceMappingTable": bosMstVlanInstanceMappingTable,
       "bosMstVlanInstanceMappingEntry": bosMstVlanInstanceMappingEntry,
       "bosMstInstanceIndex": bosMstInstanceIndex,
       "bosMstMapVlanIndex": bosMstMapVlanIndex,
       "bosMstUnMapVlanIndex": bosMstUnMapVlanIndex,
       "bosMstSetVlanList": bosMstSetVlanList,
       "bosMstResetVlanList": bosMstResetVlanList,
       "bosMstInstanceVlanMapped": bosMstInstanceVlanMapped,
       "bosMstInstanceVlanMapped2k": bosMstInstanceVlanMapped2k,
       "bosMstInstanceVlanMapped3k": bosMstInstanceVlanMapped3k,
       "bosMstInstanceVlanMapped4k": bosMstInstanceVlanMapped4k,
       "bosMstCistPortTable": bosMstCistPortTable,
       "bosMstCistPortEntry": bosMstCistPortEntry,
       "bosMstCistPort": bosMstCistPort,
       "bosMstCistPortPathCost": bosMstCistPortPathCost,
       "bosMstCistPortPriority": bosMstCistPortPriority,
       "bosMstCistPortDesignatedRoot": bosMstCistPortDesignatedRoot,
       "bosMstCistPortDesignatedBridge": bosMstCistPortDesignatedBridge,
       "bosMstCistPortDesignatedPort": bosMstCistPortDesignatedPort,
       "bosMstCistPortAdminP2P": bosMstCistPortAdminP2P,
       "bosMstCistPortOperP2P": bosMstCistPortOperP2P,
       "bosMstCistPortAdminEdgeStatus": bosMstCistPortAdminEdgeStatus,
       "bosMstCistPortOperEdgeStatus": bosMstCistPortOperEdgeStatus,
       "bosMstCistPortProtocolMigration": bosMstCistPortProtocolMigration,
       "bosMstCistPortState": bosMstCistPortState,
       "bosMstCistForcePortState": bosMstCistForcePortState,
       "bosMstCistPortDesignatedCost": bosMstCistPortDesignatedCost,
       "bosMstCistPortRegionalRoot": bosMstCistPortRegionalRoot,
       "bosMstCistPortRegionalPathCost": bosMstCistPortRegionalPathCost,
       "bosMstCistCurrentPortRole": bosMstCistCurrentPortRole,
       "bosMstCistPortHelloTime": bosMstCistPortHelloTime,
       "bosMstCistPortAutoEdgeStatus": bosMstCistPortAutoEdgeStatus,
       "bosMstCistPortPvstProtectionStatus": bosMstCistPortPvstProtectionStatus,
       "bosMstMstiPortTable": bosMstMstiPortTable,
       "bosMstMstiPortEntry": bosMstMstiPortEntry,
       "bosMstMstiPort": bosMstMstiPort,
       "bosMstMstiPortPathCost": bosMstMstiPortPathCost,
       "bosMstMstiPortPriority": bosMstMstiPortPriority,
       "bosMstMstiPortDesignatedRoot": bosMstMstiPortDesignatedRoot,
       "bosMstMstiPortDesignatedBridge": bosMstMstiPortDesignatedBridge,
       "bosMstMstiPortDesignatedPort": bosMstMstiPortDesignatedPort,
       "bosMstMstiPortState": bosMstMstiPortState,
       "bosMstMstiForcePortState": bosMstMstiForcePortState,
       "bosMstMstiPortDesignatedCost": bosMstMstiPortDesignatedCost,
       "bosMstMstiCurrentPortRole": bosMstMstiCurrentPortRole,
       "bosMstCistDynamicPathcostCalculation": bosMstCistDynamicPathcostCalculation,
       "dot1sBosMstTrapsControl": dot1sBosMstTrapsControl,
       "bosMstSetTraps": bosMstSetTraps,
       "bosMstGenTrapType": bosMstGenTrapType,
       "bosMstErrTrapType": bosMstErrTrapType,
       "bosMstPortTrapNotificationTable": bosMstPortTrapNotificationTable,
       "bosMstPortTrapNotificationEntry": bosMstPortTrapNotificationEntry,
       "bosMstPortTrapIndex": bosMstPortTrapIndex,
       "bosMstPortMigrationType": bosMstPortMigrationType,
       "bosMstPktErrType": bosMstPktErrType,
       "bosMstPktErrVal": bosMstPktErrVal,
       "bosMstPortRoleTrapNotificationTable": bosMstPortRoleTrapNotificationTable,
       "bosMstPortRoleTrapNotificationEntry": bosMstPortRoleTrapNotificationEntry,
       "bosMstPortRoleType": bosMstPortRoleType,
       "bosMstOldRoleType": bosMstOldRoleType,
       "dot1sBosMstTraps": dot1sBosMstTraps,
       "bosMstTraps": bosMstTraps,
       "bosMstGenTrap": bosMstGenTrap,
       "bosMstErrTrap": bosMstErrTrap,
       "bosMstNewRootTrap": bosMstNewRootTrap,
       "bosMstTopologyChgTrap": bosMstTopologyChgTrap,
       "bosMstProtocolMigrationTrap": bosMstProtocolMigrationTrap,
       "bosMstInvalidBpduRxdTrap": bosMstInvalidBpduRxdTrap,
       "bosMstRegionConfigChangeTrap": bosMstRegionConfigChangeTrap,
       "bosMstNewPortRoleTrap": bosMstNewPortRoleTrap,
       "bos": bos,
       "bosSystem": bosSystem,
       "bosHardwareVersion": bosHardwareVersion,
       "bosConfigSaveStatus": bosConfigSaveStatus,
       "bosLoginAuthentication": bosLoginAuthentication,
       "bosSwitchDate": bosSwitchDate,
       "bosHttpStatus": bosHttpStatus,
       "bosConfigRestoreFileVersion": bosConfigRestoreFileVersion,
       "bosTelnetStatus": bosTelnetStatus,
       "bosTimeZone": bosTimeZone,
       "bosDayLightSaving": bosDayLightSaving,
       "bosLastBootTime": bosLastBootTime,
       "bosAllocCount": bosAllocCount,
       "bosReleaseCount": bosReleaseCount,
       "bosAllocFailCount": bosAllocFailCount,
       "bosPeakUsageCount": bosPeakUsageCount,
       "bosConfigControl": bosConfigControl,
       "bosConfigCtrlTable": bosConfigCtrlTable,
       "bosConfigCtrlEntry": bosConfigCtrlEntry,
       "bosConfigCtrlIndex": bosConfigCtrlIndex,
       "bosConfigCtrlEgressStatus": bosConfigCtrlEgressStatus,
       "bosConfigCtrlStatsCollection": bosConfigCtrlStatsCollection,
       "bosConfigCtrlStatus": bosConfigCtrlStatus,
       "bosPortCtrlTable": bosPortCtrlTable,
       "bosPortCtrlEntry": bosPortCtrlEntry,
       "bosPortCtrlIndex": bosPortCtrlIndex,
       "bosPortCtrlMode": bosPortCtrlMode,
       "bosPortCtrlDuplex": bosPortCtrlDuplex,
       "bosPortCtrlSpeed": bosPortCtrlSpeed,
       "bosPortCtrlOperDuplex": bosPortCtrlOperDuplex,
       "bosPortCtrlOperSpeed": bosPortCtrlOperSpeed,
       "bosext": bosext,
       "bosRateControl": bosRateControl,
       "bosRateCtrlTable": bosRateCtrlTable,
       "bosRateCtrlEntry": bosRateCtrlEntry,
       "bosRateCtrlIndex": bosRateCtrlIndex,
       "bosRateCtrlDLFLimitValue": bosRateCtrlDLFLimitValue,
       "bosRateCtrlBCASTLimitValue": bosRateCtrlBCASTLimitValue,
       "bosRateCtrlMCASTLimitValue": bosRateCtrlMCASTLimitValue,
       "bosMacAcl": bosMacAcl,
       "bosMacAclTable": bosMacAclTable,
       "bosMacAclEntry": bosMacAclEntry,
       "bosMacAclNo": bosMacAclNo,
       "bosMacAclProtocolType": bosMacAclProtocolType,
       "bosMacAclDstMacAddr": bosMacAclDstMacAddr,
       "bosMacAclSrcMacAddr": bosMacAclSrcMacAddr,
       "bosMacAclVlanId": bosMacAclVlanId,
       "bosMacAclInPortList": bosMacAclInPortList,
       "bosMacAclOutPortList": bosMacAclOutPortList,
       "bosMacAclAction": bosMacAclAction,
       "bosMacAclMatchCount": bosMacAclMatchCount,
       "bosMacAclStatsStatus": bosMacAclStatsStatus,
       "bosMacAclStats": bosMacAclStats,
       "bosMacAclClearStats": bosMacAclClearStats,
       "bosMacAclUserPriority": bosMacAclUserPriority,
       "bosMacAclStatus": bosMacAclStatus,
       "bosIpAcl": bosIpAcl,
       "bosIpAclTable": bosIpAclTable,
       "bosIpAclEntry": bosIpAclEntry,
       "bosIpAclNo": bosIpAclNo,
       "bosIpAclProtocol": bosIpAclProtocol,
       "bosIpAclMessageType": bosIpAclMessageType,
       "bosIpAclMessageCode": bosIpAclMessageCode,
       "bosIpAclDstIpAddr": bosIpAclDstIpAddr,
       "bosIpAclSrcIpAddr": bosIpAclSrcIpAddr,
       "bosIpAclDstIpAddrMask": bosIpAclDstIpAddrMask,
       "bosIpAclSrcIpAddrMask": bosIpAclSrcIpAddrMask,
       "bosIpAclMinDstProtPort": bosIpAclMinDstProtPort,
       "bosIpAclMaxDstProtPort": bosIpAclMaxDstProtPort,
       "bosIpAclMinSrcProtPort": bosIpAclMinSrcProtPort,
       "bosIpAclMaxSrcProtPort": bosIpAclMaxSrcProtPort,
       "bosIpAclInPortList": bosIpAclInPortList,
       "bosIpAclOutPortList": bosIpAclOutPortList,
       "bosIpAclAckBit": bosIpAclAckBit,
       "bosIpAclRstBit": bosIpAclRstBit,
       "bosIpAclFinBit": bosIpAclFinBit,
       "bosIpAclSynBit": bosIpAclSynBit,
       "bosIpAclUrgBit": bosIpAclUrgBit,
       "bosIpAclPshBit": bosIpAclPshBit,
       "bosIpAclTos": bosIpAclTos,
       "bosIpAclDscp": bosIpAclDscp,
       "bosIpAclAction": bosIpAclAction,
       "bosIpAclMatchCount": bosIpAclMatchCount,
       "bosIpAclStatsStatus": bosIpAclStatsStatus,
       "bosIpAclStats": bosIpAclStats,
       "bosIpAclClearStats": bosIpAclClearStats,
       "bosIpAclUserPriority": bosIpAclUserPriority,
       "bosIpAclStatus": bosIpAclStatus,
       "bosDiffServMib": bosDiffServMib,
       "bosDhcpClientMIB": bosDhcpClientMIB,
       "dhcpClientConfig": dhcpClientConfig,
       "dhcpClientConfigTable": dhcpClientConfigTable,
       "dhcpClientConfigEntry": dhcpClientConfigEntry,
       "dhcpClientConfigIfIndex": dhcpClientConfigIfIndex,
       "dhcpClientRenew": dhcpClientRenew,
       "dhcpClientRelease": dhcpClientRelease,
       "dhcpClientCounters": dhcpClientCounters,
       "dhcpClientCounterTable": dhcpClientCounterTable,
       "dhcpClientCounterEntry": dhcpClientCounterEntry,
       "dhcpClientIfIndex": dhcpClientIfIndex,
       "dhcpClientCountDiscovers": dhcpClientCountDiscovers,
       "dhcpClientCountRequests": dhcpClientCountRequests,
       "dhcpClientCountReleases": dhcpClientCountReleases,
       "dhcpClientCountDeclines": dhcpClientCountDeclines,
       "dhcpClientLeaseTime": dhcpClientLeaseTime,
       "dhcpClientCounterReset": dhcpClientCounterReset,
       "dhcpClientRemainLeaseTime": dhcpClientRemainLeaseTime,
       "bosSyslog": bosSyslog,
       "bosSyslogGeneralGroup": bosSyslogGeneralGroup,
       "bosSyslogLogging": bosSyslogLogging,
       "bosSyslogTimeStamp": bosSyslogTimeStamp,
       "bosSyslogConsoleLog": bosSyslogConsoleLog,
       "bosSyslogSysBuffers": bosSyslogSysBuffers,
       "bosSyslogClearLog": bosSyslogClearLog,
       "bosSyslogFacility": bosSyslogFacility,
       "bosSyslogFacilitySec": bosSyslogFacilitySec,
       "bosSyslogSeverity": bosSyslogSeverity,
       "bosSyslogSeveritySec": bosSyslogSeveritySec,
       "bosSyslogLogs": bosSyslogLogs,
       "bosSyslogLogSrvAddr": bosSyslogLogSrvAddr,
       "bosSyslogLogNoLogServer": bosSyslogLogNoLogServer,
       "bosSyslogLogSrvAddrSec": bosSyslogLogSrvAddrSec,
       "bosSyslogLogNoLogServerSec": bosSyslogLogNoLogServerSec,
       "ssl": ssl,
       "sslGeneralGroup": sslGeneralGroup,
       "sslSecureHttpStatus": sslSecureHttpStatus,
       "sslPort": sslPort,
       "sslTrace": sslTrace,
       "sslCiphers": sslCiphers,
       "sslCipherList": sslCipherList,
       "sslDefaultCipherList": sslDefaultCipherList,
       "ssh": ssh,
       "g8000addon": g8000addon,
       "cfa": cfa,
       "bosPortCfgTable": bosPortCfgTable,
       "bosPortCfgTableEntry": bosPortCfgTableEntry,
       "bosPortCfgIndx": bosPortCfgIndx,
       "bosPortCfgVlanTag": bosPortCfgVlanTag,
       "bosPortCfgStateChangeCount": bosPortCfgStateChangeCount,
       "bosPortCfgLearning": bosPortCfgLearning,
       "bosPortCfgFlooding": bosPortCfgFlooding,
       "bosPortCfgTagPvid": bosPortCfgTagPvid,
       "bosPortCfgMacNotif": bosPortCfgMacNotif,
       "bosPortStatsClearTable": bosPortStatsClearTable,
       "bosPortStatsClearTableEntry": bosPortStatsClearTableEntry,
       "bosPortStatsIndx": bosPortStatsIndx,
       "bosPortStatsClear": bosPortStatsClear,
       "bosClearPortsStats": bosClearPortsStats,
       "igs": igs,
       "igmpV3SnoopCfg": igmpV3SnoopCfg,
       "igmpV3SnoopNewCfgSources": igmpV3SnoopNewCfgSources,
       "igmpV3SnoopNewCfgEnaDis": igmpV3SnoopNewCfgEnaDis,
       "igmpV3SnoopNewCfgExcludeEnaDis": igmpV3SnoopNewCfgExcludeEnaDis,
       "igmpV3SnoopNewCfgV1V2EnaDis": igmpV3SnoopNewCfgV1V2EnaDis,
       "igmpSnoopCfg": igmpSnoopCfg,
       "igmpSnoopStatsClear": igmpSnoopStatsClear,
       "igmpSnoopGroupClear": igmpSnoopGroupClear,
       "igmpSnoopMrouterClear": igmpSnoopMrouterClear,
       "bosSnoopVlanStatsClearTable": bosSnoopVlanStatsClearTable,
       "bosSnoopVlanStatsClearEntry": bosSnoopVlanStatsClearEntry,
       "bosSnoopVlanStatsClearVlanId": bosSnoopVlanStatsClearVlanId,
       "bosSnoopVlanStatsClear": bosSnoopVlanStatsClear,
       "igmpSnoopFloodStatus": igmpSnoopFloodStatus,
       "bosigmpSnoopVlanConfigTable": bosigmpSnoopVlanConfigTable,
       "bosigmpSnoopVlanConfigEntry": bosigmpSnoopVlanConfigEntry,
       "bosSnoopVlanConfigVlanId": bosSnoopVlanConfigVlanId,
       "bosSnoopVlanConfigSrcIp": bosSnoopVlanConfigSrcIp,
       "bosSnoopInfo": bosSnoopInfo,
       "bosSnoopInfoTable": bosSnoopInfoTable,
       "bosSnoopInfoEntry": bosSnoopInfoEntry,
       "bosSnoopInfoAddressType": bosSnoopInfoAddressType,
       "bosSnoopInfoVlanId": bosSnoopInfoVlanId,
       "bosSnoopInfoGroupAddress": bosSnoopInfoGroupAddress,
       "bosSnoopInfoSourceAddress": bosSnoopInfoSourceAddress,
       "bosSnoopInfoPortNum": bosSnoopInfoPortNum,
       "bosSnoopInfoVersion": bosSnoopInfoVersion,
       "bosSnoopInfoExpires": bosSnoopInfoExpires,
       "bosSnoopInfoMode": bosSnoopInfoMode,
       "bosSnoopInfoFwd": bosSnoopInfoFwd,
       "bosSnoopMrouterInfoTable": bosSnoopMrouterInfoTable,
       "bosSnoopMrouterInfoEntry": bosSnoopMrouterInfoEntry,
       "bosSnoopMrouterInfoVlanId": bosSnoopMrouterInfoVlanId,
       "bosSnoopMrouterInfoPortNum": bosSnoopMrouterInfoPortNum,
       "bosSnoopMrouterInfoExpires": bosSnoopMrouterInfoExpires,
       "bosSnoopMrouterInfoResponseTime": bosSnoopMrouterInfoResponseTime,
       "bosSnoopMrouterInfoQRV": bosSnoopMrouterInfoQRV,
       "bosSnoopMrouterInfoQQIC": bosSnoopMrouterInfoQQIC,
       "pnac": pnac,
       "dot1x": dot1x,
       "dot1xNewStatus": dot1xNewStatus,
       "dot1xNewCfgGlobalTable": dot1xNewCfgGlobalTable,
       "dot1xNewCfgGlobalMode": dot1xNewCfgGlobalMode,
       "dot1xNewCfgGlobalQtPeriod": dot1xNewCfgGlobalQtPeriod,
       "dot1xNewCfgGlobalTxPeriod": dot1xNewCfgGlobalTxPeriod,
       "dot1xNewCfgGlobalSupTmout": dot1xNewCfgGlobalSupTmout,
       "dot1xNewCfgGlobalSrvTmout": dot1xNewCfgGlobalSrvTmout,
       "dot1xNewCfgGlobalMaxRq": dot1xNewCfgGlobalMaxRq,
       "dot1xNewCfgGlobalRaPeriod": dot1xNewCfgGlobalRaPeriod,
       "dot1xNewCfgGlobalReAuth": dot1xNewCfgGlobalReAuth,
       "dot1xNewCfgGlobalDefault": dot1xNewCfgGlobalDefault,
       "dot1xClearStatsTable": dot1xClearStatsTable,
       "dot1xClearStatsEntry": dot1xClearStatsEntry,
       "dot1xPortNumber": dot1xPortNumber,
       "dot1xClearStats": dot1xClearStats,
       "sys": sys,
       "agNewCfgIdleCLITimeout": agNewCfgIdleCLITimeout,
       "tacacsCmdAuthorAcctStatusTable": tacacsCmdAuthorAcctStatusTable,
       "tacacsCmdAuthorAcctStatusEntry": tacacsCmdAuthorAcctStatusEntry,
       "tacacsCmdPrivLevel": tacacsCmdPrivLevel,
       "tacacsCmdAuthorstatus": tacacsCmdAuthorstatus,
       "tacacsCmdAcctStatus": tacacsCmdAcctStatus,
       "systemNotice1": systemNotice1,
       "systemNotice2": systemNotice2,
       "systemNotice3": systemNotice3,
       "systemNotice4": systemNotice4,
       "systemNotice5": systemNotice5,
       "systemBanner": systemBanner,
       "sysAccessUserBbi": sysAccessUserBbi,
       "sysCurCfgHprompt": sysCurCfgHprompt,
       "pmirr": pmirr,
       "pmNewCfgPortMirrState": pmNewCfgPortMirrState,
       "pmNewCfgPortMonitorTable": pmNewCfgPortMonitorTable,
       "pmNewCfgPortMonitorEntry": pmNewCfgPortMonitorEntry,
       "pmNewCfgPmirrMoniPortIndex": pmNewCfgPmirrMoniPortIndex,
       "pmNewCfgPmirrMirrPortIndex": pmNewCfgPmirrMirrPortIndex,
       "pmNewCfgPmirrDirection": pmNewCfgPmirrDirection,
       "pmNewCfgPmirrDelete": pmNewCfgPmirrDelete,
       "stp": stp,
       "bosMstMstiInstanceTable": bosMstMstiInstanceTable,
       "bosMstMstiInstanceEntry": bosMstMstiInstanceEntry,
       "bosMstMstiInstanceIndex": bosMstMstiInstanceIndex,
       "bosMstMstiForceState": bosMstMstiForceState,
       "bosMstMstiForcePortStateBmp": bosMstMstiForcePortStateBmp,
       "bosStgCfgTable": bosStgCfgTable,
       "bosStgCfgTableEntry": bosStgCfgTableEntry,
       "bosStgCfgIndex": bosStgCfgIndex,
       "bosStgCfgDefaultCfg": bosStgCfgDefaultCfg,
       "bosMstCistDefaultCfg": bosMstCistDefaultCfg,
       "bosStpMode": bosStpMode,
       "ip": ip,
       "bosIpRouteStatsHiwat": bosIpRouteStatsHiwat,
       "bosIpDefaultGatewayTable": bosIpDefaultGatewayTable,
       "bosIpDefaultGatewayEntry": bosIpDefaultGatewayEntry,
       "bosIpDefaultGatewayIndex": bosIpDefaultGatewayIndex,
       "bosIpDefaultGatewayIpAddr": bosIpDefaultGatewayIpAddr,
       "bosIpDefaultGatewayStatus": bosIpDefaultGatewayStatus,
       "bosIpDefaultGatewayState": bosIpDefaultGatewayState,
       "bosIpDefaultGatewayRowStatus": bosIpDefaultGatewayRowStatus,
       "clearStats": clearStats,
       "ipClearStats": ipClearStats,
       "arpClearStats": arpClearStats,
       "dnsClearStats": dnsClearStats,
       "icmpClearStats": icmpClearStats,
       "tcpClearStats": tcpClearStats,
       "udpClearStats": udpClearStats,
       "routeClearStats": routeClearStats,
       "ipStaticArpCfg": ipStaticArpCfg,
       "ipStaticArpTableMaxSize": ipStaticArpTableMaxSize,
       "ipCurCfgStaticArpTable": ipCurCfgStaticArpTable,
       "ipCurCfgStaticArpEntry": ipCurCfgStaticArpEntry,
       "ipCurCfgStaticArpInterface": ipCurCfgStaticArpInterface,
       "ipCurCfgStaticArpIp": ipCurCfgStaticArpIp,
       "ipCurCfgStaticArpMAC": ipCurCfgStaticArpMAC,
       "ipCurCfgStaticArpAction": ipCurCfgStaticArpAction,
       "ipNewCfgStaticArpTable": ipNewCfgStaticArpTable,
       "ipNewCfgStaticArpEntry": ipNewCfgStaticArpEntry,
       "ipNewCfgStaticArpEntryIndex": ipNewCfgStaticArpEntryIndex,
       "ipNewCfgStaticArpInterface": ipNewCfgStaticArpInterface,
       "ipNewCfgStaticArpIp": ipNewCfgStaticArpIp,
       "ipNewCfgStaticArpMAC": ipNewCfgStaticArpMAC,
       "ipStaticArpClearAll": ipStaticArpClearAll,
       "arpCfg": arpCfg,
       "arpCfgReARPPeriod": arpCfgReARPPeriod,
       "snmpv3": snmpv3,
       "bosUsmUser": bosUsmUser,
       "bosUsmUserTable": bosUsmUserTable,
       "bosUsmUserEntry": bosUsmUserEntry,
       "bosUsmUserTableIndex": bosUsmUserTableIndex,
       "bosUsmUserName": bosUsmUserName,
       "bosUsmUserSecurityName": bosUsmUserSecurityName,
       "bosUsmUserCloneFrom": bosUsmUserCloneFrom,
       "bosUsmUserAuthProtocol": bosUsmUserAuthProtocol,
       "bosUsmUserAuthKeyChange": bosUsmUserAuthKeyChange,
       "bosUsmUserOwnAuthKeyChange": bosUsmUserOwnAuthKeyChange,
       "bosUsmUserPrivProtocol": bosUsmUserPrivProtocol,
       "bosUsmUserPrivKeyChange": bosUsmUserPrivKeyChange,
       "bosUsmUserOwnPrivKeyChange": bosUsmUserOwnPrivKeyChange,
       "bosUsmUserPublic": bosUsmUserPublic,
       "bosUsmUserStorageType": bosUsmUserStorageType,
       "bosUsmUserStatus": bosUsmUserStatus,
       "bosVacmObjects": bosVacmObjects,
       "bosVacmSecurityToGroupTable": bosVacmSecurityToGroupTable,
       "bosVacmSecurityToGroupEntry": bosVacmSecurityToGroupEntry,
       "bosVacmSecurityToGroupTableIndex": bosVacmSecurityToGroupTableIndex,
       "bosVacmGroupName": bosVacmGroupName,
       "bosVacmSecurityToGroupStorageType": bosVacmSecurityToGroupStorageType,
       "bosVacmSecurityToGroupStatus": bosVacmSecurityToGroupStatus,
       "bosVacmAccessTable": bosVacmAccessTable,
       "bosVacmAccessEntry": bosVacmAccessEntry,
       "bosVacmAccessTableIndex": bosVacmAccessTableIndex,
       "bosVacmAccessContextMatch": bosVacmAccessContextMatch,
       "bosVacmAccessReadViewName": bosVacmAccessReadViewName,
       "bosVacmAccessWriteViewName": bosVacmAccessWriteViewName,
       "bosVacmAccessNotifyViewName": bosVacmAccessNotifyViewName,
       "bosVacmAccessStorageType": bosVacmAccessStorageType,
       "bosVacmAccessStatus": bosVacmAccessStatus,
       "bosVacmViewTreeFamilyTable": bosVacmViewTreeFamilyTable,
       "bosVacmViewTreeFamilyEntry": bosVacmViewTreeFamilyEntry,
       "bosVacmViewTreeFamilyTableIndex": bosVacmViewTreeFamilyTableIndex,
       "bosVacmViewTreeFamilyMask": bosVacmViewTreeFamilyMask,
       "bosVacmViewTreeFamilyType": bosVacmViewTreeFamilyType,
       "bosVacmViewTreeFamilyStorageType": bosVacmViewTreeFamilyStorageType,
       "bosVacmViewTreeFamilyStatus": bosVacmViewTreeFamilyStatus,
       "bosSnmpTargetObjects": bosSnmpTargetObjects,
       "bossnmpTargetAddrTable": bossnmpTargetAddrTable,
       "bosSnmpTargetAddrEntry": bosSnmpTargetAddrEntry,
       "bossnmpTargetTableIndex": bossnmpTargetTableIndex,
       "bossnmpTargetAddrTDomain": bossnmpTargetAddrTDomain,
       "bossnmpTargetAddrTAddress": bossnmpTargetAddrTAddress,
       "bossnmpTargetAddrTimeout": bossnmpTargetAddrTimeout,
       "bossnmpTargetAddrRetryCount": bossnmpTargetAddrRetryCount,
       "bossnmpTargetAddrTagList": bossnmpTargetAddrTagList,
       "bossnmpTargetAddrParams": bossnmpTargetAddrParams,
       "bossnmpTargetAddrStorageType": bossnmpTargetAddrStorageType,
       "bossnmpTargetAddrRowStatus": bossnmpTargetAddrRowStatus,
       "bosSnmpTargetParamsTable": bosSnmpTargetParamsTable,
       "bosSnmpTargetParamsEntry": bosSnmpTargetParamsEntry,
       "bosSnmpTargetParamsTableIndex": bosSnmpTargetParamsTableIndex,
       "bosSnmpTargetParamsMPModel": bosSnmpTargetParamsMPModel,
       "bosSnmpTargetParamsSecurityModel": bosSnmpTargetParamsSecurityModel,
       "bosSnmpTargetParamsSecurityName": bosSnmpTargetParamsSecurityName,
       "bosSnmpTargetParamsSecurityLevel": bosSnmpTargetParamsSecurityLevel,
       "bosSnmpTargetParamsStorageType": bosSnmpTargetParamsStorageType,
       "bosSnmpTargetParamsRowStatus": bosSnmpTargetParamsRowStatus,
       "bosSnmpNotifyObjects": bosSnmpNotifyObjects,
       "bosSnmpNotifyTable": bosSnmpNotifyTable,
       "bosSnmpNotifyEntry": bosSnmpNotifyEntry,
       "bosSnmpNotifyTableIndex": bosSnmpNotifyTableIndex,
       "bosSnmpNotifyTag": bosSnmpNotifyTag,
       "bosSnmpNotifyType": bosSnmpNotifyType,
       "bosSnmpNotifyStorageType": bosSnmpNotifyStorageType,
       "bosSnmpNotifyRowStatus": bosSnmpNotifyRowStatus,
       "bosSnmpCommunityObjects": bosSnmpCommunityObjects,
       "bosSnmpCommunityTable": bosSnmpCommunityTable,
       "bosSnmpCommunityEntry": bosSnmpCommunityEntry,
       "bosSnmpCommunityTableIndex": bosSnmpCommunityTableIndex,
       "bosSnmpCommunityName": bosSnmpCommunityName,
       "bosSnmpCommunitySecurityName": bosSnmpCommunitySecurityName,
       "bosSnmpCommunityContextEngineID": bosSnmpCommunityContextEngineID,
       "bosSnmpCommunityContextName": bosSnmpCommunityContextName,
       "bosSnmpCommunityTransportTag": bosSnmpCommunityTransportTag,
       "bosSnmpCommunityStorageType": bosSnmpCommunityStorageType,
       "bosSnmpCommunityStatus": bosSnmpCommunityStatus,
       "qos": qos,
       "bosNewCfgPriorityCoSTable": bosNewCfgPriorityCoSTable,
       "bosNewCfgPriorityCoSEntry": bosNewCfgPriorityCoSEntry,
       "bosNewCfgPriorityIndex": bosNewCfgPriorityIndex,
       "bosNewCfgPriorityCoSq": bosNewCfgPriorityCoSq,
       "bosNewCfgCosWeightTable": bosNewCfgCosWeightTable,
       "bosNewCfgCosWeightEntry": bosNewCfgCosWeightEntry,
       "bosNewCfgCosIndex": bosNewCfgCosIndex,
       "bosNewCfgCosWeight": bosNewCfgCosWeight,
       "bosNewCfgCosNum": bosNewCfgCosNum,
       "bosNewCfgDscpTable": bosNewCfgDscpTable,
       "bosNewCfgDscpEntry": bosNewCfgDscpEntry,
       "bosNewCfgDscpIndex": bosNewCfgDscpIndex,
       "bosNewCfgMapDscp": bosNewCfgMapDscp,
       "bosNewCfgMap8021p": bosNewCfgMap8021p,
       "bosNewCfgDscpState": bosNewCfgDscpState,
       "bosNewCfgPortDsStatusTable": bosNewCfgPortDsStatusTable,
       "bosNewCfgPortDsStatusEntry": bosNewCfgPortDsStatusEntry,
       "bosNewCfgPortDsIndex": bosNewCfgPortDsIndex,
       "bosNewCfgPortDsState": bosNewCfgPortDsState,
       "bosDiffServMeterTable": bosDiffServMeterTable,
       "bosDiffServMeterEntry": bosDiffServMeterEntry,
       "bosDiffServMeterId": bosDiffServMeterId,
       "bosDiffServMetertokenSize": bosDiffServMetertokenSize,
       "bosDiffServMeterRefreshCount": bosDiffServMeterRefreshCount,
       "bosDiffServMeterStatus": bosDiffServMeterStatus,
       "fdb": fdb,
       "fdbClear": fdbClear,
       "fdbStatsCurrent": fdbStatsCurrent,
       "fdbStatsHiwat": fdbStatsHiwat,
       "fdbStatsClear": fdbStatsClear,
       "fdbTable": fdbTable,
       "fdbEntry": fdbEntry,
       "fdbVlan": fdbVlan,
       "fdbMacAddr": fdbMacAddr,
       "fdbMacAddrStr": fdbMacAddrStr,
       "fdbVlanId": fdbVlanId,
       "fdbSrcPort": fdbSrcPort,
       "fdbSrcTrunk": fdbSrcTrunk,
       "fdbState": fdbState,
       "fdbRefSps": fdbRefSps,
       "fdbLearnedPort": fdbLearnedPort,
       "fdbStatus": fdbStatus,
       "fdbClearMac": fdbClearMac,
       "fdbDisableAging": fdbDisableAging,
       "fdbNewCfgStaticTable": fdbNewCfgStaticTable,
       "fdbNewCfgStaticEntry": fdbNewCfgStaticEntry,
       "fdbNewCfgEntryIndex": fdbNewCfgEntryIndex,
       "fdbNewCfgAddVlan": fdbNewCfgAddVlan,
       "fdbNewCfgAddPort": fdbNewCfgAddPort,
       "fdbNewCfgAddPortChannel": fdbNewCfgAddPortChannel,
       "fdbNewCfgAddMac": fdbNewCfgAddMac,
       "fdbAgingTime": fdbAgingTime,
       "switch": switch,
       "hwPartNumber": hwPartNumber,
       "hwRevision": hwRevision,
       "hwLastBoot": hwLastBoot,
       "hwMACAddress": hwMACAddress,
       "hwFlashConfiguration": hwFlashConfiguration,
       "hwPCBAPartNumber": hwPCBAPartNumber,
       "hwFABNumber": hwFABNumber,
       "hwTemperatureSensor1": hwTemperatureSensor1,
       "hwTemperatureSensor2": hwTemperatureSensor2,
       "hwFan1RPMValue": hwFan1RPMValue,
       "hwFan2RPMValue": hwFan2RPMValue,
       "hwFan3RPMValue": hwFan3RPMValue,
       "hwFan4RPMValue": hwFan4RPMValue,
       "hwBoardRevision": hwBoardRevision,
       "hwPLDFirmwareVersion": hwPLDFirmwareVersion,
       "hwPowerSupply1State": hwPowerSupply1State,
       "hwPowerSupply2State": hwPowerSupply2State,
       "sfpInfoTable": sfpInfoTable,
       "sfpInfoTableEntry": sfpInfoTableEntry,
       "sfpInfoIndx": sfpInfoIndx,
       "sfpInfoDescription": sfpInfoDescription,
       "sfpInfoSerialNumber": sfpInfoSerialNumber,
       "sfpInfoPartNumber": sfpInfoPartNumber,
       "sfpInfoHWRevision": sfpInfoHWRevision,
       "iomoduleInfoTable": iomoduleInfoTable,
       "ioModuleInfoTableEntry": ioModuleInfoTableEntry,
       "ioModuleInfoIndx": ioModuleInfoIndx,
       "ioModuleInfoDescription": ioModuleInfoDescription,
       "ioModuleInfoSerialNumber": ioModuleInfoSerialNumber,
       "ioModuleInfoPartNumber": ioModuleInfoPartNumber,
       "hwFan5RPMValue": hwFan5RPMValue,
       "hwTemperatureSensor1WarningThreshhold": hwTemperatureSensor1WarningThreshhold,
       "hwTemperatureSensor1RecoverThreshhold": hwTemperatureSensor1RecoverThreshhold,
       "hwTemperatureSensor2WarningThreshhold": hwTemperatureSensor2WarningThreshhold,
       "hwTemperatureSensor2RecoverThreshhold": hwTemperatureSensor2RecoverThreshhold,
       "snmp": snmp,
       "snmpCfgServerVersion": snmpCfgServerVersion,
       "snmpCfgTrapSrcIf": snmpCfgTrapSrcIf,
       "bosSnmpTraps": bosSnmpTraps,
       "bosSwTempExceedThreshold": bosSwTempExceedThreshold,
       "bosSwFanFailure": bosSwFanFailure,
       "bosSwPowerSupplyFailure": bosSwPowerSupplyFailure,
       "bosBladeHarmony": bosBladeHarmony,
       "dataCollection": dataCollection,
       "agPortTableMaxEnt": agPortTableMaxEnt,
       "agImageForNxtReset": agImageForNxtReset,
       "agImage1Ver": agImage1Ver,
       "agImage2Ver": agImage2Ver,
       "hwSwitchSoftwareVersion": hwSwitchSoftwareVersion,
       "hwSerialNumber": hwSerialNumber,
       "hwManufacturingDate": hwManufacturingDate,
       "agReset": agReset,
       "agBootVer": agBootVer,
       "agConfigForNxtReset": agConfigForNxtReset,
       "agSoftwareVersion": agSoftwareVersion,
       "generalConfiguration": generalConfiguration,
       "agSaveConfiguration": agSaveConfiguration,
       "agNewCfgHttpServerPort": agNewCfgHttpServerPort,
       "agNewCfgTelnetServerPort": agNewCfgTelnetServerPort,
       "agNewCfgTftpServerPort": agNewCfgTftpServerPort,
       "imageConfigTransfer": imageConfigTransfer,
       "agTftpServer": agTftpServer,
       "agTftpImage": agTftpImage,
       "agTftpImageFileName": agTftpImageFileName,
       "agTftpCfgFileName": agTftpCfgFileName,
       "agTftpAction": agTftpAction,
       "agTftpLastActionStatus": agTftpLastActionStatus,
       "portInformation": portInformation,
       "portInfoTable": portInfoTable,
       "portInfoTableEntry": portInfoTableEntry,
       "portInfoIndx": portInfoIndx,
       "portInfoSpeed": portInfoSpeed,
       "portInfoMode": portInfoMode,
       "portInfoFlowCtrl": portInfoFlowCtrl,
       "portInfoLink": portInfoLink,
       "agPortNewCfgVlanTag": agPortNewCfgVlanTag,
       "agPortNewCfgTagPVID": agPortNewCfgTagPVID,
       "agPortNewCfgPVID": agPortNewCfgPVID,
       "agPortNewCfgPortName": agPortNewCfgPortName,
       "vlanConfiguration": vlanConfiguration,
       "bosCfgVlanNewVlan": bosCfgVlanNewVlan,
       "vlanNewCfgTable": vlanNewCfgTable,
       "vlanNewCfgTableEntry": vlanNewCfgTableEntry,
       "vlanNewCfgVlanId": vlanNewCfgVlanId,
       "vlanNewCfgVlanName": vlanNewCfgVlanName,
       "vlanNewCfgPorts": vlanNewCfgPorts,
       "vlanNewCfgPortList": vlanNewCfgPortList,
       "vlanNewCfgState": vlanNewCfgState,
       "vlanNewCfgAddPort": vlanNewCfgAddPort,
       "vlanNewCfgRemovePort": vlanNewCfgRemovePort,
       "vlanNewCfgDelete": vlanNewCfgDelete,
       "vlanNewCfgStg": vlanNewCfgStg,
       "vlanNewCfgPrVlanType": vlanNewCfgPrVlanType,
       "vlanNewCfgPrVlanMapPriId": vlanNewCfgPrVlanMapPriId,
       "vlanNewCfgPrVlanState": vlanNewCfgPrVlanState,
       "bossnoop": bossnoop,
       "bosSnoopSystem": bosSnoopSystem,
       "bosSnoopInst": bosSnoopInst,
       "bosSnoopInstanceGlobalTable": bosSnoopInstanceGlobalTable,
       "bosSnoopInstanceGlobalEntry": bosSnoopInstanceGlobalEntry,
       "bosSnoopInstanceGlobalInstId": bosSnoopInstanceGlobalInstId,
       "bosSnoopInstanceConfigTable": bosSnoopInstanceConfigTable,
       "bosSnoopInstanceConfigEntry": bosSnoopInstanceConfigEntry,
       "bosSnoopInstanceConfigInstId": bosSnoopInstanceConfigInstId,
       "bosSnoopInetAddressType": bosSnoopInetAddressType,
       "bosSnoopStatus": bosSnoopStatus,
       "bosSnoopRouterPortPurgeInterval": bosSnoopRouterPortPurgeInterval,
       "bosSnoopPortPurgeInterval": bosSnoopPortPurgeInterval,
       "bosSnoopGrpQueryInterval": bosSnoopGrpQueryInterval,
       "bosSnoopOperStatus": bosSnoopOperStatus,
       "bosSnoopVlan": bosSnoopVlan,
       "bosSnoopVlanMcastIpFwdTable": bosSnoopVlanMcastIpFwdTable,
       "bosSnoopVlanMcastIpFwdEntry": bosSnoopVlanMcastIpFwdEntry,
       "bosSnoopVlanMcastIpFwdInstId": bosSnoopVlanMcastIpFwdInstId,
       "bosSnoopVlanMcastIpFwdVlanId": bosSnoopVlanMcastIpFwdVlanId,
       "bosSnoopVlanMcastIpFwdAddressType": bosSnoopVlanMcastIpFwdAddressType,
       "bosSnoopVlanMcastIpFwdSourceAddress": bosSnoopVlanMcastIpFwdSourceAddress,
       "bosSnoopVlanMcastIpFwdGroupAddress": bosSnoopVlanMcastIpFwdGroupAddress,
       "bosSnoopVlanMcastIpFwdPortList": bosSnoopVlanMcastIpFwdPortList,
       "bosSnoopVlanRouterTable": bosSnoopVlanRouterTable,
       "bosSnoopVlanRouterEntry": bosSnoopVlanRouterEntry,
       "bosSnoopVlanRouterInstId": bosSnoopVlanRouterInstId,
       "bosSnoopVlanRouterVlanId": bosSnoopVlanRouterVlanId,
       "bosSnoopVlanRouterInetAddressType": bosSnoopVlanRouterInetAddressType,
       "bosSnoopVlanRouterPortList": bosSnoopVlanRouterPortList,
       "bosSnoopVlanFilterTable": bosSnoopVlanFilterTable,
       "bosSnoopVlanFilterEntry": bosSnoopVlanFilterEntry,
       "bosSnoopVlanFilterInstId": bosSnoopVlanFilterInstId,
       "bosSnoopVlanFilterVlanId": bosSnoopVlanFilterVlanId,
       "bosSnoopVlanFilterInetAddressType": bosSnoopVlanFilterInetAddressType,
       "bosSnoopVlanSnoopStatus": bosSnoopVlanSnoopStatus,
       "bosSnoopVlanOperatingVersion": bosSnoopVlanOperatingVersion,
       "bosSnoopVlanCfgOperVersion": bosSnoopVlanCfgOperVersion,
       "bosSnoopVlanFastLeave": bosSnoopVlanFastLeave,
       "bosSnoopVlanRtrPortList": bosSnoopVlanRtrPortList,
       "bosSnoopVlanRowStatus": bosSnoopVlanRowStatus,
       "bosSnoopStats": bosSnoopStats,
       "bosSnoopStatsTable": bosSnoopStatsTable,
       "bosSnoopStatsEntry": bosSnoopStatsEntry,
       "bosSnoopStatsInstId": bosSnoopStatsInstId,
       "bosSnoopStatsVlanId": bosSnoopStatsVlanId,
       "bosSnoopStatsInetAddressType": bosSnoopStatsInetAddressType,
       "bosSnoopStatsRxGenQueries": bosSnoopStatsRxGenQueries,
       "bosSnoopStatsRxGrpQueries": bosSnoopStatsRxGrpQueries,
       "bosSnoopStatsRxGrpAndSrcQueries": bosSnoopStatsRxGrpAndSrcQueries,
       "bosSnoopStatsRxAsmReports": bosSnoopStatsRxAsmReports,
       "bosSnoopStatsRxSsmReports": bosSnoopStatsRxSsmReports,
       "bosSnoopStatsRxSsmIsInMsgs": bosSnoopStatsRxSsmIsInMsgs,
       "bosSnoopStatsRxSsmIsExMsgs": bosSnoopStatsRxSsmIsExMsgs,
       "bosSnoopStatsRxSsmToInMsgs": bosSnoopStatsRxSsmToInMsgs,
       "bosSnoopStatsRxSsmToExMsgs": bosSnoopStatsRxSsmToExMsgs,
       "bosSnoopStatsRxSsmAllowMsgs": bosSnoopStatsRxSsmAllowMsgs,
       "bosSnoopStatsRxSsmBlockMsgs": bosSnoopStatsRxSsmBlockMsgs,
       "bosSnoopStatsRxAsmLeaves": bosSnoopStatsRxAsmLeaves,
       "bosSnoopStatsTxGenQueries": bosSnoopStatsTxGenQueries,
       "bosSnoopStatsTxGrpQueries": bosSnoopStatsTxGrpQueries,
       "bosSnoopStatsTxAsmReports": bosSnoopStatsTxAsmReports,
       "bosSnoopStatsTxSsmReports": bosSnoopStatsTxSsmReports,
       "bosSnoopStatsTxAsmLeaves": bosSnoopStatsTxAsmLeaves,
       "bosSnoopStatsDroppedPkts": bosSnoopStatsDroppedPkts,
       "bosSnoopStatsValidPkts": bosSnoopStatsValidPkts,
       "bosrtm": bosrtm,
       "bosrrdScalar": bosrrdScalar,
       "bosRrdRouterId": bosRrdRouterId,
       "bosRrdFilterByOspfTag": bosRrdFilterByOspfTag,
       "bosRrdFilterOspfTag": bosRrdFilterOspfTag,
       "bosRrdFilterOspfTagMask": bosRrdFilterOspfTagMask,
       "bosRrdRouterASNumber": bosRrdRouterASNumber,
       "bosRrdAdminStatus": bosRrdAdminStatus,
       "bosRrdControlTable": bosRrdControlTable,
       "bosRrdControlEntry": bosRrdControlEntry,
       "bosRrdControlDestIpAddress": bosRrdControlDestIpAddress,
       "bosRrdControlNetMask": bosRrdControlNetMask,
       "bosRrdControlSourceProto": bosRrdControlSourceProto,
       "bosRrdControlDestProto": bosRrdControlDestProto,
       "bosRrdControlRouteExportFlag": bosRrdControlRouteExportFlag,
       "bosRrdControlRowStatus": bosRrdControlRowStatus,
       "bosRrdRoutingProtoTable": bosRrdRoutingProtoTable,
       "bosRrdRoutingProtoEntry": bosRrdRoutingProtoEntry,
       "bosRrdRoutingProtoId": bosRrdRoutingProtoId,
       "bosRrdRoutingRegnId": bosRrdRoutingRegnId,
       "bosRrdRoutingProtoTaskIdent": bosRrdRoutingProtoTaskIdent,
       "bosRrdRoutingProtoQueueIdent": bosRrdRoutingProtoQueueIdent,
       "bosRrdAllowOspfAreaRoutes": bosRrdAllowOspfAreaRoutes,
       "bosRrdAllowOspfExtRoutes": bosRrdAllowOspfExtRoutes,
       "bosRtmCommonRouteTable": bosRtmCommonRouteTable,
       "bosRtmCommonRouteEntry": bosRtmCommonRouteEntry,
       "bosRtmCommonRouteDest": bosRtmCommonRouteDest,
       "bosRtmCommonRouteMask": bosRtmCommonRouteMask,
       "bosRtmCommonRouteTos": bosRtmCommonRouteTos,
       "bosRtmCommonRouteNextHop": bosRtmCommonRouteNextHop,
       "bosRtmCommonRouteIfIndex": bosRtmCommonRouteIfIndex,
       "bosRtmCommonRouteType": bosRtmCommonRouteType,
       "bosRtmCommonRouteProto": bosRtmCommonRouteProto,
       "bosRtmCommonRouteAge": bosRtmCommonRouteAge,
       "bosRtmCommonRouteInfo": bosRtmCommonRouteInfo,
       "bosRtmCommonRouteNextHopAS": bosRtmCommonRouteNextHopAS,
       "bosRtmCommonRouteMetric1": bosRtmCommonRouteMetric1,
       "bosRtmCommonRoutePrivateStatus": bosRtmCommonRoutePrivateStatus,
       "bosRtmCommonRouteStatus": bosRtmCommonRouteStatus,
       "bosarp": bosarp,
       "arp": arp,
       "bosArpCacheTimeout": bosArpCacheTimeout,
       "bosArpCachePendTime": bosArpCachePendTime,
       "bosArpMaxRetries": bosArpMaxRetries,
       "bossnmp3": bossnmp3,
       "snmpInInformResponses": snmpInInformResponses,
       "snmpOutInformRequests": snmpOutInformRequests,
       "snmpInformDrops": snmpInformDrops,
       "snmpInformAwaitingAck": snmpInformAwaitingAck,
       "snmpInformCntTable": snmpInformCntTable,
       "snmpInformCntEntry": snmpInformCntEntry,
       "snmpInformTgtAddrName": snmpInformTgtAddrName,
       "snmpInformSent": snmpInformSent,
       "snmpInformAwaitAck": snmpInformAwaitAck,
       "snmpInformRetried": snmpInformRetried,
       "snmpInformDropped": snmpInformDropped,
       "snmpInformFailed": snmpInformFailed,
       "snmpInformResponses": snmpInformResponses}
)
