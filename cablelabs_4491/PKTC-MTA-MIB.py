# SNMP MIB module (PKTC-MTA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/PKTC-MTA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:41:44 2025
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

(clabProjPacketCable,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjPacketCable")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

(Bits,
 Bits,
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

pktcMtaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pktcMtaMib.setRevisions(
        ("2007-11-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class X509Certificate(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )



# MIB Managed Objects in the order of their OIDs

_PktcMtaMibObjects_ObjectIdentity = ObjectIdentity
pktcMtaMibObjects = _PktcMtaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1)
)
_PktcMtaDevBase_ObjectIdentity = ObjectIdentity
pktcMtaDevBase = _PktcMtaDevBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1)
)
_PktcMtaDevResetNow_Type = TruthValue
_PktcMtaDevResetNow_Object = MibScalar
pktcMtaDevResetNow = _PktcMtaDevResetNow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 1),
    _PktcMtaDevResetNow_Type()
)
pktcMtaDevResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevResetNow.setStatus("current")


class _PktcMtaDevSerialNumber_Type(SnmpAdminString):
    """Custom type pktcMtaDevSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PktcMtaDevSerialNumber_Type.__name__ = "SnmpAdminString"
_PktcMtaDevSerialNumber_Object = MibScalar
pktcMtaDevSerialNumber = _PktcMtaDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 2),
    _PktcMtaDevSerialNumber_Type()
)
pktcMtaDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevSerialNumber.setStatus("current")


class _PktcMtaDevHardwareVersion_Type(SnmpAdminString):
    """Custom type pktcMtaDevHardwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_PktcMtaDevHardwareVersion_Type.__name__ = "SnmpAdminString"
_PktcMtaDevHardwareVersion_Object = MibScalar
pktcMtaDevHardwareVersion = _PktcMtaDevHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 3),
    _PktcMtaDevHardwareVersion_Type()
)
pktcMtaDevHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevHardwareVersion.setStatus("obsolete")
_PktcMtaDevMacAddress_Type = MacAddress
_PktcMtaDevMacAddress_Object = MibScalar
pktcMtaDevMacAddress = _PktcMtaDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 4),
    _PktcMtaDevMacAddress_Type()
)
pktcMtaDevMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevMacAddress.setStatus("current")
_PktcMtaDevFQDN_Type = SnmpAdminString
_PktcMtaDevFQDN_Object = MibScalar
pktcMtaDevFQDN = _PktcMtaDevFQDN_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 5),
    _PktcMtaDevFQDN_Type()
)
pktcMtaDevFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevFQDN.setStatus("current")


class _PktcMtaDevEndPntCount_Type(Integer32):
    """Custom type pktcMtaDevEndPntCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PktcMtaDevEndPntCount_Type.__name__ = "Integer32"
_PktcMtaDevEndPntCount_Object = MibScalar
pktcMtaDevEndPntCount = _PktcMtaDevEndPntCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 6),
    _PktcMtaDevEndPntCount_Type()
)
pktcMtaDevEndPntCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevEndPntCount.setStatus("current")
_PktcMtaDevEnabled_Type = TruthValue
_PktcMtaDevEnabled_Object = MibScalar
pktcMtaDevEnabled = _PktcMtaDevEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 7),
    _PktcMtaDevEnabled_Type()
)
pktcMtaDevEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevEnabled.setStatus("current")
_PktcMtaDevTypeIdentifier_Type = SnmpAdminString
_PktcMtaDevTypeIdentifier_Object = MibScalar
pktcMtaDevTypeIdentifier = _PktcMtaDevTypeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 8),
    _PktcMtaDevTypeIdentifier_Type()
)
pktcMtaDevTypeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevTypeIdentifier.setStatus("current")


class _PktcMtaDevProvisioningState_Type(Integer32):
    """Custom type pktcMtaDevProvisioningState based on Integer32"""
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
        *(("pass", 1),
          ("inProgress", 2),
          ("failConfigFileError", 3),
          ("passWithWarnings", 4),
          ("passWithIncompleteParsing", 5),
          ("failureInternalError", 6),
          ("failOtherReason", 7))
    )


_PktcMtaDevProvisioningState_Type.__name__ = "Integer32"
_PktcMtaDevProvisioningState_Object = MibScalar
pktcMtaDevProvisioningState = _PktcMtaDevProvisioningState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 9),
    _PktcMtaDevProvisioningState_Type()
)
pktcMtaDevProvisioningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningState.setStatus("current")
_PktcMtaDevHttpAccess_Type = TruthValue
_PktcMtaDevHttpAccess_Object = MibScalar
pktcMtaDevHttpAccess = _PktcMtaDevHttpAccess_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 10),
    _PktcMtaDevHttpAccess_Type()
)
pktcMtaDevHttpAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevHttpAccess.setStatus("current")


class _PktcMtaDevProvisioningTimer_Type(Integer32):
    """Custom type pktcMtaDevProvisioningTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_PktcMtaDevProvisioningTimer_Type.__name__ = "Integer32"
_PktcMtaDevProvisioningTimer_Object = MibScalar
pktcMtaDevProvisioningTimer = _PktcMtaDevProvisioningTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 11),
    _PktcMtaDevProvisioningTimer_Type()
)
pktcMtaDevProvisioningTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningTimer.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningTimer.setUnits("minutes")
_PktcMtaDevProvisioningCounter_Type = Counter32
_PktcMtaDevProvisioningCounter_Object = MibScalar
pktcMtaDevProvisioningCounter = _PktcMtaDevProvisioningCounter_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 12),
    _PktcMtaDevProvisioningCounter_Type()
)
pktcMtaDevProvisioningCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningCounter.setStatus("current")
_PktcMtaDevErrorOidsTable_Object = MibTable
pktcMtaDevErrorOidsTable = _PktcMtaDevErrorOidsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    pktcMtaDevErrorOidsTable.setStatus("current")
_PktcMtaDevErrorOidsEntry_Object = MibTableRow
pktcMtaDevErrorOidsEntry = _PktcMtaDevErrorOidsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 13, 1)
)
pktcMtaDevErrorOidsEntry.setIndexNames(
    (0, "PKTC-MTA-MIB", "pktcMtaDevErrorOidIndex"),
)
if mibBuilder.loadTexts:
    pktcMtaDevErrorOidsEntry.setStatus("current")


class _PktcMtaDevErrorOidIndex_Type(Integer32):
    """Custom type pktcMtaDevErrorOidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PktcMtaDevErrorOidIndex_Type.__name__ = "Integer32"
_PktcMtaDevErrorOidIndex_Object = MibTableColumn
pktcMtaDevErrorOidIndex = _PktcMtaDevErrorOidIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 13, 1, 1),
    _PktcMtaDevErrorOidIndex_Type()
)
pktcMtaDevErrorOidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaDevErrorOidIndex.setStatus("current")
_PktcMtaDevErrorOid_Type = SnmpAdminString
_PktcMtaDevErrorOid_Object = MibTableColumn
pktcMtaDevErrorOid = _PktcMtaDevErrorOid_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 13, 1, 2),
    _PktcMtaDevErrorOid_Type()
)
pktcMtaDevErrorOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevErrorOid.setStatus("current")
_PktcMtaDevErrorGiven_Type = SnmpAdminString
_PktcMtaDevErrorGiven_Object = MibTableColumn
pktcMtaDevErrorGiven = _PktcMtaDevErrorGiven_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 13, 1, 3),
    _PktcMtaDevErrorGiven_Type()
)
pktcMtaDevErrorGiven.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevErrorGiven.setStatus("current")
_PktcMtaDevErrorReason_Type = SnmpAdminString
_PktcMtaDevErrorReason_Object = MibTableColumn
pktcMtaDevErrorReason = _PktcMtaDevErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 13, 1, 4),
    _PktcMtaDevErrorReason_Type()
)
pktcMtaDevErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevErrorReason.setStatus("current")
_PktcMtaDevSwCurrentVers_Type = SnmpAdminString
_PktcMtaDevSwCurrentVers_Object = MibScalar
pktcMtaDevSwCurrentVers = _PktcMtaDevSwCurrentVers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 14),
    _PktcMtaDevSwCurrentVers_Type()
)
pktcMtaDevSwCurrentVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevSwCurrentVers.setStatus("current")
_PktcMtaDevServer_ObjectIdentity = ObjectIdentity
pktcMtaDevServer = _PktcMtaDevServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2)
)


class _PktcMtaDevServerBootState_Type(Integer32):
    """Custom type pktcMtaDevServerBootState based on Integer32"""
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
        *(("operational", 1),
          ("disabled", 2),
          ("waitingForDhcpOffer", 3),
          ("waitingForDhcpResponse", 4),
          ("waitingForConfig", 5),
          ("refusedByCmts", 6),
          ("other", 7),
          ("unknown", 8))
    )


_PktcMtaDevServerBootState_Type.__name__ = "Integer32"
_PktcMtaDevServerBootState_Object = MibScalar
pktcMtaDevServerBootState = _PktcMtaDevServerBootState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 1),
    _PktcMtaDevServerBootState_Type()
)
pktcMtaDevServerBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevServerBootState.setStatus("obsolete")
_PktcMtaDevServerDhcp_Type = IpAddress
_PktcMtaDevServerDhcp_Object = MibScalar
pktcMtaDevServerDhcp = _PktcMtaDevServerDhcp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 2),
    _PktcMtaDevServerDhcp_Type()
)
pktcMtaDevServerDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevServerDhcp.setStatus("obsolete")
_PktcMtaDevServerDns1_Type = IpAddress
_PktcMtaDevServerDns1_Object = MibScalar
pktcMtaDevServerDns1 = _PktcMtaDevServerDns1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 3),
    _PktcMtaDevServerDns1_Type()
)
pktcMtaDevServerDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServerDns1.setStatus("current")
_PktcMtaDevServerDns2_Type = IpAddress
_PktcMtaDevServerDns2_Object = MibScalar
pktcMtaDevServerDns2 = _PktcMtaDevServerDns2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 4),
    _PktcMtaDevServerDns2_Type()
)
pktcMtaDevServerDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServerDns2.setStatus("current")
_PktcMtaDevConfigFile_Type = SnmpAdminString
_PktcMtaDevConfigFile_Object = MibScalar
pktcMtaDevConfigFile = _PktcMtaDevConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 5),
    _PktcMtaDevConfigFile_Type()
)
pktcMtaDevConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevConfigFile.setStatus("current")
_PktcMtaDevSnmpEntity_Type = SnmpAdminString
_PktcMtaDevSnmpEntity_Object = MibScalar
pktcMtaDevSnmpEntity = _PktcMtaDevSnmpEntity_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 6),
    _PktcMtaDevSnmpEntity_Type()
)
pktcMtaDevSnmpEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevSnmpEntity.setStatus("current")


class _PktcMtaDevProvConfigHash_Type(OctetString):
    """Custom type pktcMtaDevProvConfigHash based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PktcMtaDevProvConfigHash_Type.__name__ = "OctetString"
_PktcMtaDevProvConfigHash_Object = MibScalar
pktcMtaDevProvConfigHash = _PktcMtaDevProvConfigHash_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 7),
    _PktcMtaDevProvConfigHash_Type()
)
pktcMtaDevProvConfigHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevProvConfigHash.setStatus("current")


class _PktcMtaDevProvConfigKey_Type(OctetString):
    """Custom type pktcMtaDevProvConfigKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_PktcMtaDevProvConfigKey_Type.__name__ = "OctetString"
_PktcMtaDevProvConfigKey_Object = MibScalar
pktcMtaDevProvConfigKey = _PktcMtaDevProvConfigKey_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 8),
    _PktcMtaDevProvConfigKey_Type()
)
pktcMtaDevProvConfigKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevProvConfigKey.setStatus("current")


class _PktcMtaDevProvSolicitedKeyTimeout_Type(Integer32):
    """Custom type pktcMtaDevProvSolicitedKeyTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevProvSolicitedKeyTimeout_Type.__name__ = "Integer32"
_PktcMtaDevProvSolicitedKeyTimeout_Object = MibScalar
pktcMtaDevProvSolicitedKeyTimeout = _PktcMtaDevProvSolicitedKeyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 9),
    _PktcMtaDevProvSolicitedKeyTimeout_Type()
)
pktcMtaDevProvSolicitedKeyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevProvSolicitedKeyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevProvSolicitedKeyTimeout.setUnits("seconds")


class _PktcMtaDevProvUnsolicitedKeyMaxTimeout_Type(Integer32):
    """Custom type pktcMtaDevProvUnsolicitedKeyMaxTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevProvUnsolicitedKeyMaxTimeout_Type.__name__ = "Integer32"
_PktcMtaDevProvUnsolicitedKeyMaxTimeout_Object = MibScalar
pktcMtaDevProvUnsolicitedKeyMaxTimeout = _PktcMtaDevProvUnsolicitedKeyMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 10),
    _PktcMtaDevProvUnsolicitedKeyMaxTimeout_Type()
)
pktcMtaDevProvUnsolicitedKeyMaxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyMaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyMaxTimeout.setUnits("seconds")


class _PktcMtaDevProvUnsolicitedKeyNomTimeout_Type(Integer32):
    """Custom type pktcMtaDevProvUnsolicitedKeyNomTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevProvUnsolicitedKeyNomTimeout_Type.__name__ = "Integer32"
_PktcMtaDevProvUnsolicitedKeyNomTimeout_Object = MibScalar
pktcMtaDevProvUnsolicitedKeyNomTimeout = _PktcMtaDevProvUnsolicitedKeyNomTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 11),
    _PktcMtaDevProvUnsolicitedKeyNomTimeout_Type()
)
pktcMtaDevProvUnsolicitedKeyNomTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyNomTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyNomTimeout.setUnits("seconds")


class _PktcMtaDevProvUnsolicitedKeyMeanDev_Type(Integer32):
    """Custom type pktcMtaDevProvUnsolicitedKeyMeanDev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevProvUnsolicitedKeyMeanDev_Type.__name__ = "Integer32"
_PktcMtaDevProvUnsolicitedKeyMeanDev_Object = MibScalar
pktcMtaDevProvUnsolicitedKeyMeanDev = _PktcMtaDevProvUnsolicitedKeyMeanDev_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 12),
    _PktcMtaDevProvUnsolicitedKeyMeanDev_Type()
)
pktcMtaDevProvUnsolicitedKeyMeanDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyMeanDev.setStatus("obsolete")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyMeanDev.setUnits("seconds")


class _PktcMtaDevProvUnsolicitedKeyMaxRetries_Type(Integer32):
    """Custom type pktcMtaDevProvUnsolicitedKeyMaxRetries based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PktcMtaDevProvUnsolicitedKeyMaxRetries_Type.__name__ = "Integer32"
_PktcMtaDevProvUnsolicitedKeyMaxRetries_Object = MibScalar
pktcMtaDevProvUnsolicitedKeyMaxRetries = _PktcMtaDevProvUnsolicitedKeyMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 13),
    _PktcMtaDevProvUnsolicitedKeyMaxRetries_Type()
)
pktcMtaDevProvUnsolicitedKeyMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyMaxRetries.setStatus("current")


class _PktcMtaDevProvKerbRealmName_Type(SnmpAdminString):
    """Custom type pktcMtaDevProvKerbRealmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PktcMtaDevProvKerbRealmName_Type.__name__ = "SnmpAdminString"
_PktcMtaDevProvKerbRealmName_Object = MibScalar
pktcMtaDevProvKerbRealmName = _PktcMtaDevProvKerbRealmName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 14),
    _PktcMtaDevProvKerbRealmName_Type()
)
pktcMtaDevProvKerbRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvKerbRealmName.setStatus("current")


class _PktcMtaDevProvState_Type(Integer32):
    """Custom type pktcMtaDevProvState based on Integer32"""
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
        *(("operational", 1),
          ("waitingForSnmpSetInfo", 2),
          ("waitingForTftpAddrResponse", 3),
          ("waitingForConfigFile", 4))
    )


_PktcMtaDevProvState_Type.__name__ = "Integer32"
_PktcMtaDevProvState_Object = MibScalar
pktcMtaDevProvState = _PktcMtaDevProvState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 15),
    _PktcMtaDevProvState_Type()
)
pktcMtaDevProvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvState.setStatus("current")
_PktcMtaDevServerDhcp1_Type = IpAddress
_PktcMtaDevServerDhcp1_Object = MibScalar
pktcMtaDevServerDhcp1 = _PktcMtaDevServerDhcp1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 16),
    _PktcMtaDevServerDhcp1_Type()
)
pktcMtaDevServerDhcp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevServerDhcp1.setStatus("current")
_PktcMtaDevServerDhcp2_Type = IpAddress
_PktcMtaDevServerDhcp2_Object = MibScalar
pktcMtaDevServerDhcp2 = _PktcMtaDevServerDhcp2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 17),
    _PktcMtaDevServerDhcp2_Type()
)
pktcMtaDevServerDhcp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevServerDhcp2.setStatus("current")
_PktcMtaDevTimeServer_Type = IpAddress
_PktcMtaDevTimeServer_Object = MibScalar
pktcMtaDevTimeServer = _PktcMtaDevTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 18),
    _PktcMtaDevTimeServer_Type()
)
pktcMtaDevTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevTimeServer.setStatus("current")
_PktcMtaDevSecurity_ObjectIdentity = ObjectIdentity
pktcMtaDevSecurity = _PktcMtaDevSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3)
)
_PktcMtaDevManufacturerCertificate_Type = X509Certificate
_PktcMtaDevManufacturerCertificate_Object = MibScalar
pktcMtaDevManufacturerCertificate = _PktcMtaDevManufacturerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 1),
    _PktcMtaDevManufacturerCertificate_Type()
)
pktcMtaDevManufacturerCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevManufacturerCertificate.setStatus("current")
_PktcMtaDevCertificate_Type = X509Certificate
_PktcMtaDevCertificate_Object = MibScalar
pktcMtaDevCertificate = _PktcMtaDevCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 2),
    _PktcMtaDevCertificate_Type()
)
pktcMtaDevCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevCertificate.setStatus("current")


class _PktcMtaDevSignature_Type(OctetString):
    """Custom type pktcMtaDevSignature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PktcMtaDevSignature_Type.__name__ = "OctetString"
_PktcMtaDevSignature_Object = MibScalar
pktcMtaDevSignature = _PktcMtaDevSignature_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 3),
    _PktcMtaDevSignature_Type()
)
pktcMtaDevSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevSignature.setStatus("obsolete")
_PktcMtaDevCorrelationId_Type = Integer32
_PktcMtaDevCorrelationId_Object = MibScalar
pktcMtaDevCorrelationId = _PktcMtaDevCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 4),
    _PktcMtaDevCorrelationId_Type()
)
pktcMtaDevCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevCorrelationId.setStatus("current")
_PktcMtaDevSecurityTable_Object = MibTable
pktcMtaDevSecurityTable = _PktcMtaDevSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    pktcMtaDevSecurityTable.setStatus("obsolete")
_PktcMtaDevSecurityEntry_Object = MibTableRow
pktcMtaDevSecurityEntry = _PktcMtaDevSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1)
)
pktcMtaDevSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcMtaDevSecurityEntry.setStatus("obsolete")
_PktcMtaDevServProviderCertificate_Type = X509Certificate
_PktcMtaDevServProviderCertificate_Object = MibTableColumn
pktcMtaDevServProviderCertificate = _PktcMtaDevServProviderCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 1),
    _PktcMtaDevServProviderCertificate_Type()
)
pktcMtaDevServProviderCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServProviderCertificate.setStatus("obsolete")
_PktcMtaDevTelephonyCertificate_Type = X509Certificate
_PktcMtaDevTelephonyCertificate_Object = MibTableColumn
pktcMtaDevTelephonyCertificate = _PktcMtaDevTelephonyCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 2),
    _PktcMtaDevTelephonyCertificate_Type()
)
pktcMtaDevTelephonyCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevTelephonyCertificate.setStatus("obsolete")


class _PktcMtaDevKerberosRealm_Type(OctetString):
    """Custom type pktcMtaDevKerberosRealm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1280),
    )


_PktcMtaDevKerberosRealm_Type.__name__ = "OctetString"
_PktcMtaDevKerberosRealm_Object = MibTableColumn
pktcMtaDevKerberosRealm = _PktcMtaDevKerberosRealm_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 3),
    _PktcMtaDevKerberosRealm_Type()
)
pktcMtaDevKerberosRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevKerberosRealm.setStatus("obsolete")


class _PktcMtaDevKerbPrincipalName_Type(DisplayString):
    """Custom type pktcMtaDevKerbPrincipalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_PktcMtaDevKerbPrincipalName_Type.__name__ = "DisplayString"
_PktcMtaDevKerbPrincipalName_Object = MibTableColumn
pktcMtaDevKerbPrincipalName = _PktcMtaDevKerbPrincipalName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 4),
    _PktcMtaDevKerbPrincipalName_Type()
)
pktcMtaDevKerbPrincipalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevKerbPrincipalName.setStatus("obsolete")


class _PktcMtaDevServGracePeriod_Type(Integer32):
    """Custom type pktcMtaDevServGracePeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevServGracePeriod_Type.__name__ = "Integer32"
_PktcMtaDevServGracePeriod_Object = MibTableColumn
pktcMtaDevServGracePeriod = _PktcMtaDevServGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 5),
    _PktcMtaDevServGracePeriod_Type()
)
pktcMtaDevServGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServGracePeriod.setStatus("obsolete")
if mibBuilder.loadTexts:
    pktcMtaDevServGracePeriod.setUnits("minutes")
_PktcMtaDevLocalSystemCertificate_Type = X509Certificate
_PktcMtaDevLocalSystemCertificate_Object = MibTableColumn
pktcMtaDevLocalSystemCertificate = _PktcMtaDevLocalSystemCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 6),
    _PktcMtaDevLocalSystemCertificate_Type()
)
pktcMtaDevLocalSystemCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevLocalSystemCertificate.setStatus("obsolete")


class _PktcMtaDevKeyMgmtTimeout1_Type(Integer32):
    """Custom type pktcMtaDevKeyMgmtTimeout1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevKeyMgmtTimeout1_Type.__name__ = "Integer32"
_PktcMtaDevKeyMgmtTimeout1_Object = MibTableColumn
pktcMtaDevKeyMgmtTimeout1 = _PktcMtaDevKeyMgmtTimeout1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 7),
    _PktcMtaDevKeyMgmtTimeout1_Type()
)
pktcMtaDevKeyMgmtTimeout1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevKeyMgmtTimeout1.setStatus("obsolete")
if mibBuilder.loadTexts:
    pktcMtaDevKeyMgmtTimeout1.setUnits("seconds")


class _PktcMtaDevKeyMgmtTimeout2_Type(Integer32):
    """Custom type pktcMtaDevKeyMgmtTimeout2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevKeyMgmtTimeout2_Type.__name__ = "Integer32"
_PktcMtaDevKeyMgmtTimeout2_Object = MibTableColumn
pktcMtaDevKeyMgmtTimeout2 = _PktcMtaDevKeyMgmtTimeout2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 8),
    _PktcMtaDevKeyMgmtTimeout2_Type()
)
pktcMtaDevKeyMgmtTimeout2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevKeyMgmtTimeout2.setStatus("obsolete")
if mibBuilder.loadTexts:
    pktcMtaDevKeyMgmtTimeout2.setUnits("seconds")
_PktcMtaDevTgsTable_Object = MibTable
pktcMtaDevTgsTable = _PktcMtaDevTgsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    pktcMtaDevTgsTable.setStatus("obsolete")
_PktcMtaDevTgsEntry_Object = MibTableRow
pktcMtaDevTgsEntry = _PktcMtaDevTgsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 8, 1)
)
pktcMtaDevTgsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PKTC-MTA-MIB", "pktcMtaDevTgsIndex"),
)
if mibBuilder.loadTexts:
    pktcMtaDevTgsEntry.setStatus("obsolete")


class _PktcMtaDevTgsIndex_Type(Integer32):
    """Custom type pktcMtaDevTgsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PktcMtaDevTgsIndex_Type.__name__ = "Integer32"
_PktcMtaDevTgsIndex_Object = MibTableColumn
pktcMtaDevTgsIndex = _PktcMtaDevTgsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 8, 1, 1),
    _PktcMtaDevTgsIndex_Type()
)
pktcMtaDevTgsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaDevTgsIndex.setStatus("obsolete")


class _PktcMtaDevTgsLocation_Type(DisplayString):
    """Custom type pktcMtaDevTgsLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PktcMtaDevTgsLocation_Type.__name__ = "DisplayString"
_PktcMtaDevTgsLocation_Object = MibTableColumn
pktcMtaDevTgsLocation = _PktcMtaDevTgsLocation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 8, 1, 2),
    _PktcMtaDevTgsLocation_Type()
)
pktcMtaDevTgsLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevTgsLocation.setStatus("obsolete")
_PktcMtaDevTgsStatus_Type = RowStatus
_PktcMtaDevTgsStatus_Object = MibTableColumn
pktcMtaDevTgsStatus = _PktcMtaDevTgsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 8, 1, 3),
    _PktcMtaDevTgsStatus_Type()
)
pktcMtaDevTgsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevTgsStatus.setStatus("obsolete")
_PktcMtaDevTelephonyRootCertificate_Type = X509Certificate
_PktcMtaDevTelephonyRootCertificate_Object = MibScalar
pktcMtaDevTelephonyRootCertificate = _PktcMtaDevTelephonyRootCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 9),
    _PktcMtaDevTelephonyRootCertificate_Type()
)
pktcMtaDevTelephonyRootCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevTelephonyRootCertificate.setStatus("current")
_PktcMtaDevRealmTable_Object = MibTable
pktcMtaDevRealmTable = _PktcMtaDevRealmTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16)
)
if mibBuilder.loadTexts:
    pktcMtaDevRealmTable.setStatus("current")
_PktcMtaDevRealmEntry_Object = MibTableRow
pktcMtaDevRealmEntry = _PktcMtaDevRealmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16, 1)
)
pktcMtaDevRealmEntry.setIndexNames(
    (1, "PKTC-MTA-MIB", "pktcMtaDevRealmName"),
)
if mibBuilder.loadTexts:
    pktcMtaDevRealmEntry.setStatus("current")


class _PktcMtaDevRealmName_Type(SnmpAdminString):
    """Custom type pktcMtaDevRealmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PktcMtaDevRealmName_Type.__name__ = "SnmpAdminString"
_PktcMtaDevRealmName_Object = MibTableColumn
pktcMtaDevRealmName = _PktcMtaDevRealmName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16, 1, 1),
    _PktcMtaDevRealmName_Type()
)
pktcMtaDevRealmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaDevRealmName.setStatus("current")


class _PktcMtaDevRealmPkinitGracePeriod_Type(Integer32):
    """Custom type pktcMtaDevRealmPkinitGracePeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevRealmPkinitGracePeriod_Type.__name__ = "Integer32"
_PktcMtaDevRealmPkinitGracePeriod_Object = MibTableColumn
pktcMtaDevRealmPkinitGracePeriod = _PktcMtaDevRealmPkinitGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16, 1, 2),
    _PktcMtaDevRealmPkinitGracePeriod_Type()
)
pktcMtaDevRealmPkinitGracePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmPkinitGracePeriod.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevRealmPkinitGracePeriod.setUnits("minutes")


class _PktcMtaDevRealmTgsGracePeriod_Type(Integer32):
    """Custom type pktcMtaDevRealmTgsGracePeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PktcMtaDevRealmTgsGracePeriod_Type.__name__ = "Integer32"
_PktcMtaDevRealmTgsGracePeriod_Object = MibTableColumn
pktcMtaDevRealmTgsGracePeriod = _PktcMtaDevRealmTgsGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16, 1, 3),
    _PktcMtaDevRealmTgsGracePeriod_Type()
)
pktcMtaDevRealmTgsGracePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmTgsGracePeriod.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevRealmTgsGracePeriod.setUnits("minutes")


class _PktcMtaDevRealmOrgName_Type(OctetString):
    """Custom type pktcMtaDevRealmOrgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PktcMtaDevRealmOrgName_Type.__name__ = "OctetString"
_PktcMtaDevRealmOrgName_Object = MibTableColumn
pktcMtaDevRealmOrgName = _PktcMtaDevRealmOrgName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16, 1, 4),
    _PktcMtaDevRealmOrgName_Type()
)
pktcMtaDevRealmOrgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmOrgName.setStatus("current")


class _PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Type(Integer32):
    """Custom type pktcMtaDevRealmUnsolicitedKeyMaxTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Type.__name__ = "Integer32"
_PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Object = MibTableColumn
pktcMtaDevRealmUnsolicitedKeyMaxTimeout = _PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16, 1, 5),
    _PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Type()
)
pktcMtaDevRealmUnsolicitedKeyMaxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyMaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyMaxTimeout.setUnits("seconds")


class _PktcMtaDevRealmUnsolicitedKeyNomTimeout_Type(Integer32):
    """Custom type pktcMtaDevRealmUnsolicitedKeyNomTimeout based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 600000),
    )


_PktcMtaDevRealmUnsolicitedKeyNomTimeout_Type.__name__ = "Integer32"
_PktcMtaDevRealmUnsolicitedKeyNomTimeout_Object = MibTableColumn
pktcMtaDevRealmUnsolicitedKeyNomTimeout = _PktcMtaDevRealmUnsolicitedKeyNomTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16, 1, 6),
    _PktcMtaDevRealmUnsolicitedKeyNomTimeout_Type()
)
pktcMtaDevRealmUnsolicitedKeyNomTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyNomTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyNomTimeout.setUnits("milliseconds")


class _PktcMtaDevRealmUnsolicitedKeyMeanDev_Type(Integer32):
    """Custom type pktcMtaDevRealmUnsolicitedKeyMeanDev based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PktcMtaDevRealmUnsolicitedKeyMeanDev_Type.__name__ = "Integer32"
_PktcMtaDevRealmUnsolicitedKeyMeanDev_Object = MibTableColumn
pktcMtaDevRealmUnsolicitedKeyMeanDev = _PktcMtaDevRealmUnsolicitedKeyMeanDev_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16, 1, 7),
    _PktcMtaDevRealmUnsolicitedKeyMeanDev_Type()
)
pktcMtaDevRealmUnsolicitedKeyMeanDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyMeanDev.setStatus("obsolete")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyMeanDev.setUnits("seconds")


class _PktcMtaDevRealmUnsolicitedKeyMaxRetries_Type(Integer32):
    """Custom type pktcMtaDevRealmUnsolicitedKeyMaxRetries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_PktcMtaDevRealmUnsolicitedKeyMaxRetries_Type.__name__ = "Integer32"
_PktcMtaDevRealmUnsolicitedKeyMaxRetries_Object = MibTableColumn
pktcMtaDevRealmUnsolicitedKeyMaxRetries = _PktcMtaDevRealmUnsolicitedKeyMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16, 1, 8),
    _PktcMtaDevRealmUnsolicitedKeyMaxRetries_Type()
)
pktcMtaDevRealmUnsolicitedKeyMaxRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyMaxRetries.setStatus("current")
_PktcMtaDevRealmStatus_Type = RowStatus
_PktcMtaDevRealmStatus_Object = MibTableColumn
pktcMtaDevRealmStatus = _PktcMtaDevRealmStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 16, 1, 9),
    _PktcMtaDevRealmStatus_Type()
)
pktcMtaDevRealmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmStatus.setStatus("current")
_PktcMtaDevCmsTable_Object = MibTable
pktcMtaDevCmsTable = _PktcMtaDevCmsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17)
)
if mibBuilder.loadTexts:
    pktcMtaDevCmsTable.setStatus("current")
_PktcMtaDevCmsEntry_Object = MibTableRow
pktcMtaDevCmsEntry = _PktcMtaDevCmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1)
)
pktcMtaDevCmsEntry.setIndexNames(
    (1, "PKTC-MTA-MIB", "pktcMtaDevCmsFqdn"),
)
if mibBuilder.loadTexts:
    pktcMtaDevCmsEntry.setStatus("current")


class _PktcMtaDevCmsFqdn_Type(SnmpAdminString):
    """Custom type pktcMtaDevCmsFqdn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PktcMtaDevCmsFqdn_Type.__name__ = "SnmpAdminString"
_PktcMtaDevCmsFqdn_Object = MibTableColumn
pktcMtaDevCmsFqdn = _PktcMtaDevCmsFqdn_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1, 1),
    _PktcMtaDevCmsFqdn_Type()
)
pktcMtaDevCmsFqdn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaDevCmsFqdn.setStatus("current")


class _PktcMtaDevCmsKerbRealmName_Type(SnmpAdminString):
    """Custom type pktcMtaDevCmsKerbRealmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PktcMtaDevCmsKerbRealmName_Type.__name__ = "SnmpAdminString"
_PktcMtaDevCmsKerbRealmName_Object = MibTableColumn
pktcMtaDevCmsKerbRealmName = _PktcMtaDevCmsKerbRealmName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1, 2),
    _PktcMtaDevCmsKerbRealmName_Type()
)
pktcMtaDevCmsKerbRealmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsKerbRealmName.setStatus("current")


class _PktcMtaDevCmsMaxClockSkew_Type(Integer32):
    """Custom type pktcMtaDevCmsMaxClockSkew based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_PktcMtaDevCmsMaxClockSkew_Type.__name__ = "Integer32"
_PktcMtaDevCmsMaxClockSkew_Object = MibTableColumn
pktcMtaDevCmsMaxClockSkew = _PktcMtaDevCmsMaxClockSkew_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1, 3),
    _PktcMtaDevCmsMaxClockSkew_Type()
)
pktcMtaDevCmsMaxClockSkew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsMaxClockSkew.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevCmsMaxClockSkew.setUnits("seconds")


class _PktcMtaDevCmsSolicitedKeyTimeout_Type(Integer32):
    """Custom type pktcMtaDevCmsSolicitedKeyTimeout based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_PktcMtaDevCmsSolicitedKeyTimeout_Type.__name__ = "Integer32"
_PktcMtaDevCmsSolicitedKeyTimeout_Object = MibTableColumn
pktcMtaDevCmsSolicitedKeyTimeout = _PktcMtaDevCmsSolicitedKeyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1, 4),
    _PktcMtaDevCmsSolicitedKeyTimeout_Type()
)
pktcMtaDevCmsSolicitedKeyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsSolicitedKeyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevCmsSolicitedKeyTimeout.setUnits("milliseconds")


class _PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Type(Integer32):
    """Custom type pktcMtaDevCmsUnsolicitedKeyMaxTimeout based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Type.__name__ = "Integer32"
_PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Object = MibTableColumn
pktcMtaDevCmsUnsolicitedKeyMaxTimeout = _PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1, 5),
    _PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Type()
)
pktcMtaDevCmsUnsolicitedKeyMaxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyMaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyMaxTimeout.setUnits("seconds")


class _PktcMtaDevCmsUnsolicitedKeyNomTimeout_Type(Integer32):
    """Custom type pktcMtaDevCmsUnsolicitedKeyNomTimeout based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_PktcMtaDevCmsUnsolicitedKeyNomTimeout_Type.__name__ = "Integer32"
_PktcMtaDevCmsUnsolicitedKeyNomTimeout_Object = MibTableColumn
pktcMtaDevCmsUnsolicitedKeyNomTimeout = _PktcMtaDevCmsUnsolicitedKeyNomTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1, 6),
    _PktcMtaDevCmsUnsolicitedKeyNomTimeout_Type()
)
pktcMtaDevCmsUnsolicitedKeyNomTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyNomTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyNomTimeout.setUnits("milliseconds")


class _PktcMtaDevCmsUnsolicitedKeyMeanDev_Type(Integer32):
    """Custom type pktcMtaDevCmsUnsolicitedKeyMeanDev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PktcMtaDevCmsUnsolicitedKeyMeanDev_Type.__name__ = "Integer32"
_PktcMtaDevCmsUnsolicitedKeyMeanDev_Object = MibTableColumn
pktcMtaDevCmsUnsolicitedKeyMeanDev = _PktcMtaDevCmsUnsolicitedKeyMeanDev_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1, 7),
    _PktcMtaDevCmsUnsolicitedKeyMeanDev_Type()
)
pktcMtaDevCmsUnsolicitedKeyMeanDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyMeanDev.setStatus("obsolete")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyMeanDev.setUnits("seconds")


class _PktcMtaDevCmsUnsolicitedKeyMaxRetries_Type(Integer32):
    """Custom type pktcMtaDevCmsUnsolicitedKeyMaxRetries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_PktcMtaDevCmsUnsolicitedKeyMaxRetries_Type.__name__ = "Integer32"
_PktcMtaDevCmsUnsolicitedKeyMaxRetries_Object = MibTableColumn
pktcMtaDevCmsUnsolicitedKeyMaxRetries = _PktcMtaDevCmsUnsolicitedKeyMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1, 8),
    _PktcMtaDevCmsUnsolicitedKeyMaxRetries_Type()
)
pktcMtaDevCmsUnsolicitedKeyMaxRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyMaxRetries.setStatus("current")
_PktcMtaDevCmsStatus_Type = RowStatus
_PktcMtaDevCmsStatus_Object = MibTableColumn
pktcMtaDevCmsStatus = _PktcMtaDevCmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1, 9),
    _PktcMtaDevCmsStatus_Type()
)
pktcMtaDevCmsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsStatus.setStatus("current")


class _PktcMtaDevCmsIpsecCtrl_Type(TruthValue):
    """Custom type pktcMtaDevCmsIpsecCtrl based on TruthValue"""
    defaultValue = 1


_PktcMtaDevCmsIpsecCtrl_Type.__name__ = "TruthValue"
_PktcMtaDevCmsIpsecCtrl_Object = MibTableColumn
pktcMtaDevCmsIpsecCtrl = _PktcMtaDevCmsIpsecCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 17, 1, 10),
    _PktcMtaDevCmsIpsecCtrl_Type()
)
pktcMtaDevCmsIpsecCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevCmsIpsecCtrl.setStatus("current")
_PktcMtaCmsMapTable_Object = MibTable
pktcMtaCmsMapTable = _PktcMtaCmsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 18)
)
if mibBuilder.loadTexts:
    pktcMtaCmsMapTable.setStatus("obsolete")
_PktcMtaCmsMapEntry_Object = MibTableRow
pktcMtaCmsMapEntry = _PktcMtaCmsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 18, 1)
)
pktcMtaCmsMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PKTC-MTA-MIB", "pktcMtaCmsMapCmsFqdn"),
)
if mibBuilder.loadTexts:
    pktcMtaCmsMapEntry.setStatus("obsolete")


class _PktcMtaCmsMapCmsFqdn_Type(DisplayString):
    """Custom type pktcMtaCmsMapCmsFqdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PktcMtaCmsMapCmsFqdn_Type.__name__ = "DisplayString"
_PktcMtaCmsMapCmsFqdn_Object = MibTableColumn
pktcMtaCmsMapCmsFqdn = _PktcMtaCmsMapCmsFqdn_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 18, 1, 1),
    _PktcMtaCmsMapCmsFqdn_Type()
)
pktcMtaCmsMapCmsFqdn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaCmsMapCmsFqdn.setStatus("obsolete")


class _PktcMtaCmsMapOperStatus_Type(Integer32):
    """Custom type pktcMtaCmsMapOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_PktcMtaCmsMapOperStatus_Type.__name__ = "Integer32"
_PktcMtaCmsMapOperStatus_Object = MibTableColumn
pktcMtaCmsMapOperStatus = _PktcMtaCmsMapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 18, 1, 2),
    _PktcMtaCmsMapOperStatus_Type()
)
pktcMtaCmsMapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaCmsMapOperStatus.setStatus("obsolete")


class _PktcMtaCmsMapAdminStatus_Type(Integer32):
    """Custom type pktcMtaCmsMapAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 1),
          ("allow", 2))
    )


_PktcMtaCmsMapAdminStatus_Type.__name__ = "Integer32"
_PktcMtaCmsMapAdminStatus_Object = MibTableColumn
pktcMtaCmsMapAdminStatus = _PktcMtaCmsMapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 18, 1, 3),
    _PktcMtaCmsMapAdminStatus_Type()
)
pktcMtaCmsMapAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaCmsMapAdminStatus.setStatus("obsolete")
_PktcMtaCmsMapRowStatus_Type = RowStatus
_PktcMtaCmsMapRowStatus_Object = MibTableColumn
pktcMtaCmsMapRowStatus = _PktcMtaCmsMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 18, 1, 4),
    _PktcMtaCmsMapRowStatus_Type()
)
pktcMtaCmsMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaCmsMapRowStatus.setStatus("obsolete")


class _PktcMtaDevResetKrbTickets_Type(Bits):
    """Custom type pktcMtaDevResetKrbTickets based on Bits"""
    namedValues = NamedValues(
        *(("invalidateProvOnReboot", 0),
          ("invalidateAllCmsOnReboot", 1))
    )

_PktcMtaDevResetKrbTickets_Type.__name__ = "Bits"
_PktcMtaDevResetKrbTickets_Object = MibScalar
pktcMtaDevResetKrbTickets = _PktcMtaDevResetKrbTickets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 19),
    _PktcMtaDevResetKrbTickets_Type()
)
pktcMtaDevResetKrbTickets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevResetKrbTickets.setStatus("current")
_PktcMtaNotificationPrefix_ObjectIdentity = ObjectIdentity
pktcMtaNotificationPrefix = _PktcMtaNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 2)
)
_PktcMtaNotification_ObjectIdentity = ObjectIdentity
pktcMtaNotification = _PktcMtaNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 2, 0)
)
_PktcMtaConformance_ObjectIdentity = ObjectIdentity
pktcMtaConformance = _PktcMtaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3)
)
_PktcMtaCompliances_ObjectIdentity = ObjectIdentity
pktcMtaCompliances = _PktcMtaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3, 1)
)
_PktcMtaGroups_ObjectIdentity = ObjectIdentity
pktcMtaGroups = _PktcMtaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3, 2)
)

# Managed Objects groups

pktcMtaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3, 2, 1)
)
pktcMtaGroup.setObjects(
      *(("PKTC-MTA-MIB", "pktcMtaDevResetNow"),
        ("PKTC-MTA-MIB", "pktcMtaDevSerialNumber"),
        ("PKTC-MTA-MIB", "pktcMtaDevMacAddress"),
        ("PKTC-MTA-MIB", "pktcMtaDevFQDN"),
        ("PKTC-MTA-MIB", "pktcMtaDevEndPntCount"),
        ("PKTC-MTA-MIB", "pktcMtaDevEnabled"),
        ("PKTC-MTA-MIB", "pktcMtaDevTypeIdentifier"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvisioningState"),
        ("PKTC-MTA-MIB", "pktcMtaDevHttpAccess"),
        ("PKTC-MTA-MIB", "pktcMtaDevCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevCorrelationId"),
        ("PKTC-MTA-MIB", "pktcMtaDevManufacturerCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevServerDhcp1"),
        ("PKTC-MTA-MIB", "pktcMtaDevServerDhcp2"),
        ("PKTC-MTA-MIB", "pktcMtaDevServerDns1"),
        ("PKTC-MTA-MIB", "pktcMtaDevServerDns2"),
        ("PKTC-MTA-MIB", "pktcMtaDevTimeServer"),
        ("PKTC-MTA-MIB", "pktcMtaDevConfigFile"),
        ("PKTC-MTA-MIB", "pktcMtaDevSnmpEntity"),
        ("PKTC-MTA-MIB", "pktcMtaDevRealmPkinitGracePeriod"),
        ("PKTC-MTA-MIB", "pktcMtaDevRealmTgsGracePeriod"),
        ("PKTC-MTA-MIB", "pktcMtaDevRealmOrgName"),
        ("PKTC-MTA-MIB", "pktcMtaDevRealmUnsolicitedKeyMaxTimeout"),
        ("PKTC-MTA-MIB", "pktcMtaDevRealmUnsolicitedKeyNomTimeout"),
        ("PKTC-MTA-MIB", "pktcMtaDevRealmUnsolicitedKeyMaxRetries"),
        ("PKTC-MTA-MIB", "pktcMtaDevRealmStatus"),
        ("PKTC-MTA-MIB", "pktcMtaDevCmsKerbRealmName"),
        ("PKTC-MTA-MIB", "pktcMtaDevCmsUnsolicitedKeyMaxTimeout"),
        ("PKTC-MTA-MIB", "pktcMtaDevCmsUnsolicitedKeyNomTimeout"),
        ("PKTC-MTA-MIB", "pktcMtaDevCmsUnsolicitedKeyMaxRetries"),
        ("PKTC-MTA-MIB", "pktcMtaDevCmsSolicitedKeyTimeout"),
        ("PKTC-MTA-MIB", "pktcMtaDevCmsMaxClockSkew"),
        ("PKTC-MTA-MIB", "pktcMtaDevCmsStatus"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvUnsolicitedKeyMaxTimeout"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvUnsolicitedKeyNomTimeout"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvUnsolicitedKeyMaxRetries"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvKerbRealmName"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvSolicitedKeyTimeout"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvConfigHash"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvConfigKey"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvState"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvisioningTimer"),
        ("PKTC-MTA-MIB", "pktcMtaDevTelephonyRootCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevErrorOid"),
        ("PKTC-MTA-MIB", "pktcMtaDevErrorGiven"),
        ("PKTC-MTA-MIB", "pktcMtaDevErrorReason"),
        ("PKTC-MTA-MIB", "pktcMtaDevSwCurrentVers"),
        ("PKTC-MTA-MIB", "pktcMtaDevResetKrbTickets"),
        ("PKTC-MTA-MIB", "pktcMtaDevCmsIpsecCtrl"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvisioningCounter"))
)
if mibBuilder.loadTexts:
    pktcMtaGroup.setStatus("current")

pktcMtaObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3, 2, 3)
)
pktcMtaObsoleteGroup.setObjects(
      *(("PKTC-MTA-MIB", "pktcMtaDevHardwareVersion"),
        ("PKTC-MTA-MIB", "pktcMtaDevSignature"),
        ("PKTC-MTA-MIB", "pktcMtaDevServProviderCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevTelephonyCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevKerberosRealm"),
        ("PKTC-MTA-MIB", "pktcMtaDevKerbPrincipalName"),
        ("PKTC-MTA-MIB", "pktcMtaDevServGracePeriod"),
        ("PKTC-MTA-MIB", "pktcMtaDevLocalSystemCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevKeyMgmtTimeout1"),
        ("PKTC-MTA-MIB", "pktcMtaDevTgsLocation"),
        ("PKTC-MTA-MIB", "pktcMtaDevTgsStatus"),
        ("PKTC-MTA-MIB", "pktcMtaDevServerBootState"),
        ("PKTC-MTA-MIB", "pktcMtaCmsMapOperStatus"),
        ("PKTC-MTA-MIB", "pktcMtaCmsMapAdminStatus"),
        ("PKTC-MTA-MIB", "pktcMtaCmsMapRowStatus"),
        ("PKTC-MTA-MIB", "pktcMtaDevRealmUnsolicitedKeyMeanDev"),
        ("PKTC-MTA-MIB", "pktcMtaDevCmsUnsolicitedKeyMeanDev"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvUnsolicitedKeyMeanDev"),
        ("PKTC-MTA-MIB", "pktcMtaDevServerDhcp"),
        ("PKTC-MTA-MIB", "pktcMtaDevKeyMgmtTimeout2"))
)
if mibBuilder.loadTexts:
    pktcMtaObsoleteGroup.setStatus("obsolete")


# Notification objects

pktcMtaDevProvisioningEnrollment = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 2, 0, 1)
)
pktcMtaDevProvisioningEnrollment.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("PKTC-MTA-MIB", "pktcMtaDevSwCurrentVers"),
        ("PKTC-MTA-MIB", "pktcMtaDevTypeIdentifier"),
        ("PKTC-MTA-MIB", "pktcMtaDevMacAddress"),
        ("PKTC-MTA-MIB", "pktcMtaDevCorrelationId"))
)
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningEnrollment.setStatus(
        "current"
    )

pktcMtaDevProvisioningStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 2, 0, 2)
)
pktcMtaDevProvisioningStatus.setObjects(
      *(("PKTC-MTA-MIB", "pktcMtaDevMacAddress"),
        ("PKTC-MTA-MIB", "pktcMtaDevCorrelationId"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvisioningState"))
)
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningStatus.setStatus(
        "current"
    )


# Notifications groups

pktcMtaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3, 2, 2)
)
pktcMtaNotificationGroup.setObjects(
      *(("PKTC-MTA-MIB", "pktcMtaDevProvisioningStatus"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvisioningEnrollment"))
)
if mibBuilder.loadTexts:
    pktcMtaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pktcMtaBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3, 1, 3)
)
pktcMtaBasicCompliance.setObjects(
      *(("PKTC-MTA-MIB", "pktcMtaGroup"),
        ("PKTC-MTA-MIB", "pktcMtaNotificationGroup"))
)
if mibBuilder.loadTexts:
    pktcMtaBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-MTA-MIB",
    **{"X509Certificate": X509Certificate,
       "pktcMtaMib": pktcMtaMib,
       "pktcMtaMibObjects": pktcMtaMibObjects,
       "pktcMtaDevBase": pktcMtaDevBase,
       "pktcMtaDevResetNow": pktcMtaDevResetNow,
       "pktcMtaDevSerialNumber": pktcMtaDevSerialNumber,
       "pktcMtaDevHardwareVersion": pktcMtaDevHardwareVersion,
       "pktcMtaDevMacAddress": pktcMtaDevMacAddress,
       "pktcMtaDevFQDN": pktcMtaDevFQDN,
       "pktcMtaDevEndPntCount": pktcMtaDevEndPntCount,
       "pktcMtaDevEnabled": pktcMtaDevEnabled,
       "pktcMtaDevTypeIdentifier": pktcMtaDevTypeIdentifier,
       "pktcMtaDevProvisioningState": pktcMtaDevProvisioningState,
       "pktcMtaDevHttpAccess": pktcMtaDevHttpAccess,
       "pktcMtaDevProvisioningTimer": pktcMtaDevProvisioningTimer,
       "pktcMtaDevProvisioningCounter": pktcMtaDevProvisioningCounter,
       "pktcMtaDevErrorOidsTable": pktcMtaDevErrorOidsTable,
       "pktcMtaDevErrorOidsEntry": pktcMtaDevErrorOidsEntry,
       "pktcMtaDevErrorOidIndex": pktcMtaDevErrorOidIndex,
       "pktcMtaDevErrorOid": pktcMtaDevErrorOid,
       "pktcMtaDevErrorGiven": pktcMtaDevErrorGiven,
       "pktcMtaDevErrorReason": pktcMtaDevErrorReason,
       "pktcMtaDevSwCurrentVers": pktcMtaDevSwCurrentVers,
       "pktcMtaDevServer": pktcMtaDevServer,
       "pktcMtaDevServerBootState": pktcMtaDevServerBootState,
       "pktcMtaDevServerDhcp": pktcMtaDevServerDhcp,
       "pktcMtaDevServerDns1": pktcMtaDevServerDns1,
       "pktcMtaDevServerDns2": pktcMtaDevServerDns2,
       "pktcMtaDevConfigFile": pktcMtaDevConfigFile,
       "pktcMtaDevSnmpEntity": pktcMtaDevSnmpEntity,
       "pktcMtaDevProvConfigHash": pktcMtaDevProvConfigHash,
       "pktcMtaDevProvConfigKey": pktcMtaDevProvConfigKey,
       "pktcMtaDevProvSolicitedKeyTimeout": pktcMtaDevProvSolicitedKeyTimeout,
       "pktcMtaDevProvUnsolicitedKeyMaxTimeout": pktcMtaDevProvUnsolicitedKeyMaxTimeout,
       "pktcMtaDevProvUnsolicitedKeyNomTimeout": pktcMtaDevProvUnsolicitedKeyNomTimeout,
       "pktcMtaDevProvUnsolicitedKeyMeanDev": pktcMtaDevProvUnsolicitedKeyMeanDev,
       "pktcMtaDevProvUnsolicitedKeyMaxRetries": pktcMtaDevProvUnsolicitedKeyMaxRetries,
       "pktcMtaDevProvKerbRealmName": pktcMtaDevProvKerbRealmName,
       "pktcMtaDevProvState": pktcMtaDevProvState,
       "pktcMtaDevServerDhcp1": pktcMtaDevServerDhcp1,
       "pktcMtaDevServerDhcp2": pktcMtaDevServerDhcp2,
       "pktcMtaDevTimeServer": pktcMtaDevTimeServer,
       "pktcMtaDevSecurity": pktcMtaDevSecurity,
       "pktcMtaDevManufacturerCertificate": pktcMtaDevManufacturerCertificate,
       "pktcMtaDevCertificate": pktcMtaDevCertificate,
       "pktcMtaDevSignature": pktcMtaDevSignature,
       "pktcMtaDevCorrelationId": pktcMtaDevCorrelationId,
       "pktcMtaDevSecurityTable": pktcMtaDevSecurityTable,
       "pktcMtaDevSecurityEntry": pktcMtaDevSecurityEntry,
       "pktcMtaDevServProviderCertificate": pktcMtaDevServProviderCertificate,
       "pktcMtaDevTelephonyCertificate": pktcMtaDevTelephonyCertificate,
       "pktcMtaDevKerberosRealm": pktcMtaDevKerberosRealm,
       "pktcMtaDevKerbPrincipalName": pktcMtaDevKerbPrincipalName,
       "pktcMtaDevServGracePeriod": pktcMtaDevServGracePeriod,
       "pktcMtaDevLocalSystemCertificate": pktcMtaDevLocalSystemCertificate,
       "pktcMtaDevKeyMgmtTimeout1": pktcMtaDevKeyMgmtTimeout1,
       "pktcMtaDevKeyMgmtTimeout2": pktcMtaDevKeyMgmtTimeout2,
       "pktcMtaDevTgsTable": pktcMtaDevTgsTable,
       "pktcMtaDevTgsEntry": pktcMtaDevTgsEntry,
       "pktcMtaDevTgsIndex": pktcMtaDevTgsIndex,
       "pktcMtaDevTgsLocation": pktcMtaDevTgsLocation,
       "pktcMtaDevTgsStatus": pktcMtaDevTgsStatus,
       "pktcMtaDevTelephonyRootCertificate": pktcMtaDevTelephonyRootCertificate,
       "pktcMtaDevRealmTable": pktcMtaDevRealmTable,
       "pktcMtaDevRealmEntry": pktcMtaDevRealmEntry,
       "pktcMtaDevRealmName": pktcMtaDevRealmName,
       "pktcMtaDevRealmPkinitGracePeriod": pktcMtaDevRealmPkinitGracePeriod,
       "pktcMtaDevRealmTgsGracePeriod": pktcMtaDevRealmTgsGracePeriod,
       "pktcMtaDevRealmOrgName": pktcMtaDevRealmOrgName,
       "pktcMtaDevRealmUnsolicitedKeyMaxTimeout": pktcMtaDevRealmUnsolicitedKeyMaxTimeout,
       "pktcMtaDevRealmUnsolicitedKeyNomTimeout": pktcMtaDevRealmUnsolicitedKeyNomTimeout,
       "pktcMtaDevRealmUnsolicitedKeyMeanDev": pktcMtaDevRealmUnsolicitedKeyMeanDev,
       "pktcMtaDevRealmUnsolicitedKeyMaxRetries": pktcMtaDevRealmUnsolicitedKeyMaxRetries,
       "pktcMtaDevRealmStatus": pktcMtaDevRealmStatus,
       "pktcMtaDevCmsTable": pktcMtaDevCmsTable,
       "pktcMtaDevCmsEntry": pktcMtaDevCmsEntry,
       "pktcMtaDevCmsFqdn": pktcMtaDevCmsFqdn,
       "pktcMtaDevCmsKerbRealmName": pktcMtaDevCmsKerbRealmName,
       "pktcMtaDevCmsMaxClockSkew": pktcMtaDevCmsMaxClockSkew,
       "pktcMtaDevCmsSolicitedKeyTimeout": pktcMtaDevCmsSolicitedKeyTimeout,
       "pktcMtaDevCmsUnsolicitedKeyMaxTimeout": pktcMtaDevCmsUnsolicitedKeyMaxTimeout,
       "pktcMtaDevCmsUnsolicitedKeyNomTimeout": pktcMtaDevCmsUnsolicitedKeyNomTimeout,
       "pktcMtaDevCmsUnsolicitedKeyMeanDev": pktcMtaDevCmsUnsolicitedKeyMeanDev,
       "pktcMtaDevCmsUnsolicitedKeyMaxRetries": pktcMtaDevCmsUnsolicitedKeyMaxRetries,
       "pktcMtaDevCmsStatus": pktcMtaDevCmsStatus,
       "pktcMtaDevCmsIpsecCtrl": pktcMtaDevCmsIpsecCtrl,
       "pktcMtaCmsMapTable": pktcMtaCmsMapTable,
       "pktcMtaCmsMapEntry": pktcMtaCmsMapEntry,
       "pktcMtaCmsMapCmsFqdn": pktcMtaCmsMapCmsFqdn,
       "pktcMtaCmsMapOperStatus": pktcMtaCmsMapOperStatus,
       "pktcMtaCmsMapAdminStatus": pktcMtaCmsMapAdminStatus,
       "pktcMtaCmsMapRowStatus": pktcMtaCmsMapRowStatus,
       "pktcMtaDevResetKrbTickets": pktcMtaDevResetKrbTickets,
       "pktcMtaNotificationPrefix": pktcMtaNotificationPrefix,
       "pktcMtaNotification": pktcMtaNotification,
       "pktcMtaDevProvisioningEnrollment": pktcMtaDevProvisioningEnrollment,
       "pktcMtaDevProvisioningStatus": pktcMtaDevProvisioningStatus,
       "pktcMtaConformance": pktcMtaConformance,
       "pktcMtaCompliances": pktcMtaCompliances,
       "pktcMtaBasicCompliance": pktcMtaBasicCompliance,
       "pktcMtaGroups": pktcMtaGroups,
       "pktcMtaGroup": pktcMtaGroup,
       "pktcMtaNotificationGroup": pktcMtaNotificationGroup,
       "pktcMtaObsoleteGroup": pktcMtaObsoleteGroup}
)
