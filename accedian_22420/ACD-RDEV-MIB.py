# SNMP MIB module (ACD-RDEV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/accedian_22420/ACD-RDEV-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:07:59 2025
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

acdRDev = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22)
)
if mibBuilder.loadTexts:
    acdRDev.setRevisions(
        ("2016-09-23 01:00",
         "2016-05-06 01:00",
         "2016-01-27 01:00",
         "2015-11-11 01:00",
         "2015-03-23 01:00",
         "2014-12-12 01:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AcdRDevDiscoveryMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("iPad", 2))
    )



class AcdRDevDiscoveryRate(TextualConvention, Integer32):
    status = "current"
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
        *(("rateOneShot", 0),
          ("rate3sec", 1),
          ("rate60sec", 2),
          ("rate5min", 3),
          ("rate10min", 4),
          ("rate60min", 5))
    )



class AcdRDevDiscoveryIPType(TextualConvention, Integer32):
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
        *(("unicast", 1),
          ("unicast-directed", 2),
          ("subnet", 3))
    )



class AcdRDevConfigAdminStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oos", 0),
          ("is", 1))
    )



class AcdRDevDeviceTypeType(TextualConvention, Integer32):
    status = "current"
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
        *(("ant-Nano", 0),
          ("nano2Copper", 1),
          ("nano2Optical", 2),
          ("ant2Combo", 3),
          ("ant2Copper", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AcdRDevNotifications_ObjectIdentity = ObjectIdentity
acdRDevNotifications = _AcdRDevNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 0)
)
_AcdRDevMIBObjects_ObjectIdentity = ObjectIdentity
acdRDevMIBObjects = _AcdRDevMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1)
)
_AcdRDevConfig_ObjectIdentity = ObjectIdentity
acdRDevConfig = _AcdRDevConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1)
)
_AcdRDevConfigTable_Object = MibTable
acdRDevConfigTable = _AcdRDevConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdRDevConfigTable.setStatus("current")
_AcdRDevConfigEntry_Object = MibTableRow
acdRDevConfigEntry = _AcdRDevConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1)
)
acdRDevConfigEntry.setIndexNames(
    (0, "ACD-RDEV-MIB", "acdRDevConfigIndex"),
)
if mibBuilder.loadTexts:
    acdRDevConfigEntry.setStatus("current")
_AcdRDevConfigIndex_Type = Unsigned32
_AcdRDevConfigIndex_Object = MibTableColumn
acdRDevConfigIndex = _AcdRDevConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 1),
    _AcdRDevConfigIndex_Type()
)
acdRDevConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdRDevConfigIndex.setStatus("current")
_AcdRDevConfigRowStatus_Type = RowStatus
_AcdRDevConfigRowStatus_Object = MibTableColumn
acdRDevConfigRowStatus = _AcdRDevConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 2),
    _AcdRDevConfigRowStatus_Type()
)
acdRDevConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigRowStatus.setStatus("current")


class _AcdRDevConfigName_Type(DisplayString):
    """Custom type acdRDevConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdRDevConfigName_Type.__name__ = "DisplayString"
_AcdRDevConfigName_Object = MibTableColumn
acdRDevConfigName = _AcdRDevConfigName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 3),
    _AcdRDevConfigName_Type()
)
acdRDevConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigName.setStatus("current")


class _AcdRDevConfigMacAddr_Type(MacAddress):
    """Custom type acdRDevConfigMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_AcdRDevConfigMacAddr_Type.__name__ = "MacAddress"
_AcdRDevConfigMacAddr_Object = MibTableColumn
acdRDevConfigMacAddr = _AcdRDevConfigMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 4),
    _AcdRDevConfigMacAddr_Type()
)
acdRDevConfigMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigMacAddr.setStatus("current")


class _AcdRDevConfigSecurityKey_Type(DisplayString):
    """Custom type acdRDevConfigSecurityKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_AcdRDevConfigSecurityKey_Type.__name__ = "DisplayString"
_AcdRDevConfigSecurityKey_Object = MibTableColumn
acdRDevConfigSecurityKey = _AcdRDevConfigSecurityKey_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 5),
    _AcdRDevConfigSecurityKey_Type()
)
acdRDevConfigSecurityKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigSecurityKey.setStatus("current")


class _AcdRDevConfigAuthorized_Type(TruthValue):
    """Custom type acdRDevConfigAuthorized based on TruthValue"""
    defaultValue = 1


_AcdRDevConfigAuthorized_Type.__name__ = "TruthValue"
_AcdRDevConfigAuthorized_Object = MibTableColumn
acdRDevConfigAuthorized = _AcdRDevConfigAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 6),
    _AcdRDevConfigAuthorized_Type()
)
acdRDevConfigAuthorized.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigAuthorized.setStatus("current")


class _AcdRDevConfigLinked_Type(TruthValue):
    """Custom type acdRDevConfigLinked based on TruthValue"""
    defaultValue = 2


_AcdRDevConfigLinked_Type.__name__ = "TruthValue"
_AcdRDevConfigLinked_Object = MibTableColumn
acdRDevConfigLinked = _AcdRDevConfigLinked_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 7),
    _AcdRDevConfigLinked_Type()
)
acdRDevConfigLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRDevConfigLinked.setStatus("current")


class _AcdRDevConfigActiveFeature_Type(DisplayString):
    """Custom type acdRDevConfigActiveFeature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdRDevConfigActiveFeature_Type.__name__ = "DisplayString"
_AcdRDevConfigActiveFeature_Object = MibTableColumn
acdRDevConfigActiveFeature = _AcdRDevConfigActiveFeature_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 8),
    _AcdRDevConfigActiveFeature_Type()
)
acdRDevConfigActiveFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRDevConfigActiveFeature.setStatus("current")


class _AcdRDevConfigCurrentFeatureSuite_Type(DisplayString):
    """Custom type acdRDevConfigCurrentFeatureSuite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdRDevConfigCurrentFeatureSuite_Type.__name__ = "DisplayString"
_AcdRDevConfigCurrentFeatureSuite_Object = MibTableColumn
acdRDevConfigCurrentFeatureSuite = _AcdRDevConfigCurrentFeatureSuite_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 9),
    _AcdRDevConfigCurrentFeatureSuite_Type()
)
acdRDevConfigCurrentFeatureSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRDevConfigCurrentFeatureSuite.setStatus("current")


class _AcdRDevConfigAdminState_Type(AcdRDevConfigAdminStateType):
    """Custom type acdRDevConfigAdminState based on AcdRDevConfigAdminStateType"""
    defaultValue = 0


_AcdRDevConfigAdminState_Type.__name__ = "AcdRDevConfigAdminStateType"
_AcdRDevConfigAdminState_Object = MibTableColumn
acdRDevConfigAdminState = _AcdRDevConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 10),
    _AcdRDevConfigAdminState_Type()
)
acdRDevConfigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRDevConfigAdminState.setStatus("current")


class _AcdRDevConfigType_Type(AcdRDevDeviceTypeType):
    """Custom type acdRDevConfigType based on AcdRDevDeviceTypeType"""
    defaultValue = 0


_AcdRDevConfigType_Type.__name__ = "AcdRDevDeviceTypeType"
_AcdRDevConfigType_Object = MibTableColumn
acdRDevConfigType = _AcdRDevConfigType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 11),
    _AcdRDevConfigType_Type()
)
acdRDevConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigType.setStatus("current")


class _AcdRDevConfigL2Interface_Type(Unsigned32):
    """Custom type acdRDevConfigL2Interface based on Unsigned32"""
    defaultValue = 0


_AcdRDevConfigL2Interface_Type.__name__ = "Unsigned32"
_AcdRDevConfigL2Interface_Object = MibTableColumn
acdRDevConfigL2Interface = _AcdRDevConfigL2Interface_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 12),
    _AcdRDevConfigL2Interface_Type()
)
acdRDevConfigL2Interface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigL2Interface.setStatus("current")


class _AcdRDevConfigDestinationIP_Type(DisplayString):
    """Custom type acdRDevConfigDestinationIP based on DisplayString"""
    defaultValue = OctetString("")


_AcdRDevConfigDestinationIP_Type.__name__ = "DisplayString"
_AcdRDevConfigDestinationIP_Object = MibTableColumn
acdRDevConfigDestinationIP = _AcdRDevConfigDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 13),
    _AcdRDevConfigDestinationIP_Type()
)
acdRDevConfigDestinationIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigDestinationIP.setStatus("current")


class _AcdRDevConfigTunnelTCPPort_Type(Unsigned32):
    """Custom type acdRDevConfigTunnelTCPPort based on Unsigned32"""
    defaultValue = 44240


_AcdRDevConfigTunnelTCPPort_Type.__name__ = "Unsigned32"
_AcdRDevConfigTunnelTCPPort_Object = MibTableColumn
acdRDevConfigTunnelTCPPort = _AcdRDevConfigTunnelTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 14),
    _AcdRDevConfigTunnelTCPPort_Type()
)
acdRDevConfigTunnelTCPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigTunnelTCPPort.setStatus("current")


class _AcdRDevConfigTunnelTCPDSCP_Type(Unsigned32):
    """Custom type acdRDevConfigTunnelTCPDSCP based on Unsigned32"""
    defaultValue = 0


_AcdRDevConfigTunnelTCPDSCP_Type.__name__ = "Unsigned32"
_AcdRDevConfigTunnelTCPDSCP_Object = MibTableColumn
acdRDevConfigTunnelTCPDSCP = _AcdRDevConfigTunnelTCPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 15),
    _AcdRDevConfigTunnelTCPDSCP_Type()
)
acdRDevConfigTunnelTCPDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigTunnelTCPDSCP.setStatus("current")


class _AcdRDevConfigFlexMonitor_Type(TruthValue):
    """Custom type acdRDevConfigFlexMonitor based on TruthValue"""
    defaultValue = 2


_AcdRDevConfigFlexMonitor_Type.__name__ = "TruthValue"
_AcdRDevConfigFlexMonitor_Object = MibTableColumn
acdRDevConfigFlexMonitor = _AcdRDevConfigFlexMonitor_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 1, 1, 1, 16),
    _AcdRDevConfigFlexMonitor_Type()
)
acdRDevConfigFlexMonitor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevConfigFlexMonitor.setStatus("current")
_AcdRDevSecurityKeyMgmt_ObjectIdentity = ObjectIdentity
acdRDevSecurityKeyMgmt = _AcdRDevSecurityKeyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 2)
)


class _AcdRDevSecurityKeyMgmtBackupPeriod_Type(Unsigned32):
    """Custom type acdRDevSecurityKeyMgmtBackupPeriod based on Unsigned32"""
    defaultValue = 1440


_AcdRDevSecurityKeyMgmtBackupPeriod_Type.__name__ = "Unsigned32"
_AcdRDevSecurityKeyMgmtBackupPeriod_Object = MibScalar
acdRDevSecurityKeyMgmtBackupPeriod = _AcdRDevSecurityKeyMgmtBackupPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 2, 1),
    _AcdRDevSecurityKeyMgmtBackupPeriod_Type()
)
acdRDevSecurityKeyMgmtBackupPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdRDevSecurityKeyMgmtBackupPeriod.setStatus("current")


class _AcdRDevSecurityKeyMgmtServerURL_Type(DisplayString):
    """Custom type acdRDevSecurityKeyMgmtServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AcdRDevSecurityKeyMgmtServerURL_Type.__name__ = "DisplayString"
_AcdRDevSecurityKeyMgmtServerURL_Object = MibScalar
acdRDevSecurityKeyMgmtServerURL = _AcdRDevSecurityKeyMgmtServerURL_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 2, 2),
    _AcdRDevSecurityKeyMgmtServerURL_Type()
)
acdRDevSecurityKeyMgmtServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdRDevSecurityKeyMgmtServerURL.setStatus("current")


class _AcdRDevSecurityKeyMgmtSCPPassword_Type(DisplayString):
    """Custom type acdRDevSecurityKeyMgmtSCPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdRDevSecurityKeyMgmtSCPPassword_Type.__name__ = "DisplayString"
_AcdRDevSecurityKeyMgmtSCPPassword_Object = MibScalar
acdRDevSecurityKeyMgmtSCPPassword = _AcdRDevSecurityKeyMgmtSCPPassword_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 2, 3),
    _AcdRDevSecurityKeyMgmtSCPPassword_Type()
)
acdRDevSecurityKeyMgmtSCPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdRDevSecurityKeyMgmtSCPPassword.setStatus("current")
_AcdRDevDiscoveryCfg_ObjectIdentity = ObjectIdentity
acdRDevDiscoveryCfg = _AcdRDevDiscoveryCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3)
)
_AcdRDevDiscoveryCfgTable_Object = MibTable
acdRDevDiscoveryCfgTable = _AcdRDevDiscoveryCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgTable.setStatus("current")
_AcdRDevDiscoveryCfgEntry_Object = MibTableRow
acdRDevDiscoveryCfgEntry = _AcdRDevDiscoveryCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1)
)
acdRDevDiscoveryCfgEntry.setIndexNames(
    (0, "ACD-RDEV-MIB", "acdRDevDiscoveryCfgIndex"),
)
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgEntry.setStatus("current")
_AcdRDevDiscoveryCfgIndex_Type = Unsigned32
_AcdRDevDiscoveryCfgIndex_Object = MibTableColumn
acdRDevDiscoveryCfgIndex = _AcdRDevDiscoveryCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 1),
    _AcdRDevDiscoveryCfgIndex_Type()
)
acdRDevDiscoveryCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgIndex.setStatus("current")
_AcdRDevDiscoveryCfgRowStatus_Type = RowStatus
_AcdRDevDiscoveryCfgRowStatus_Object = MibTableColumn
acdRDevDiscoveryCfgRowStatus = _AcdRDevDiscoveryCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 2),
    _AcdRDevDiscoveryCfgRowStatus_Type()
)
acdRDevDiscoveryCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgRowStatus.setStatus("current")


class _AcdRDevDiscoveryCfgName_Type(DisplayString):
    """Custom type acdRDevDiscoveryCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdRDevDiscoveryCfgName_Type.__name__ = "DisplayString"
_AcdRDevDiscoveryCfgName_Object = MibTableColumn
acdRDevDiscoveryCfgName = _AcdRDevDiscoveryCfgName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 3),
    _AcdRDevDiscoveryCfgName_Type()
)
acdRDevDiscoveryCfgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgName.setStatus("current")


class _AcdRDevDiscoveryCfgEnable_Type(TruthValue):
    """Custom type acdRDevDiscoveryCfgEnable based on TruthValue"""
    defaultValue = 2


_AcdRDevDiscoveryCfgEnable_Type.__name__ = "TruthValue"
_AcdRDevDiscoveryCfgEnable_Object = MibTableColumn
acdRDevDiscoveryCfgEnable = _AcdRDevDiscoveryCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 4),
    _AcdRDevDiscoveryCfgEnable_Type()
)
acdRDevDiscoveryCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgEnable.setStatus("current")


class _AcdRDevDiscoveryCfgMethod_Type(AcdRDevDiscoveryMethod):
    """Custom type acdRDevDiscoveryCfgMethod based on AcdRDevDiscoveryMethod"""
    defaultValue = 1


_AcdRDevDiscoveryCfgMethod_Type.__name__ = "AcdRDevDiscoveryMethod"
_AcdRDevDiscoveryCfgMethod_Object = MibTableColumn
acdRDevDiscoveryCfgMethod = _AcdRDevDiscoveryCfgMethod_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 5),
    _AcdRDevDiscoveryCfgMethod_Type()
)
acdRDevDiscoveryCfgMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgMethod.setStatus("current")


class _AcdRDevDiscoveryCfgRate_Type(AcdRDevDiscoveryRate):
    """Custom type acdRDevDiscoveryCfgRate based on AcdRDevDiscoveryRate"""
    defaultValue = 2


_AcdRDevDiscoveryCfgRate_Type.__name__ = "AcdRDevDiscoveryRate"
_AcdRDevDiscoveryCfgRate_Object = MibTableColumn
acdRDevDiscoveryCfgRate = _AcdRDevDiscoveryCfgRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 6),
    _AcdRDevDiscoveryCfgRate_Type()
)
acdRDevDiscoveryCfgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgRate.setStatus("current")


class _AcdRDevDiscoveryCfgInterface_Type(DisplayString):
    """Custom type acdRDevDiscoveryCfgInterface based on DisplayString"""
    defaultValue = OctetString("Management")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_AcdRDevDiscoveryCfgInterface_Type.__name__ = "DisplayString"
_AcdRDevDiscoveryCfgInterface_Object = MibTableColumn
acdRDevDiscoveryCfgInterface = _AcdRDevDiscoveryCfgInterface_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 7),
    _AcdRDevDiscoveryCfgInterface_Type()
)
acdRDevDiscoveryCfgInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgInterface.setStatus("current")


class _AcdRDevDiscoveryCfgHopLimit_Type(Unsigned32):
    """Custom type acdRDevDiscoveryCfgHopLimit based on Unsigned32"""
    defaultValue = 255


_AcdRDevDiscoveryCfgHopLimit_Type.__name__ = "Unsigned32"
_AcdRDevDiscoveryCfgHopLimit_Object = MibTableColumn
acdRDevDiscoveryCfgHopLimit = _AcdRDevDiscoveryCfgHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 8),
    _AcdRDevDiscoveryCfgHopLimit_Type()
)
acdRDevDiscoveryCfgHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgHopLimit.setStatus("current")


class _AcdRDevDiscoveryCfgTimeout_Type(Unsigned32):
    """Custom type acdRDevDiscoveryCfgTimeout based on Unsigned32"""
    defaultValue = 10


_AcdRDevDiscoveryCfgTimeout_Type.__name__ = "Unsigned32"
_AcdRDevDiscoveryCfgTimeout_Object = MibTableColumn
acdRDevDiscoveryCfgTimeout = _AcdRDevDiscoveryCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 9),
    _AcdRDevDiscoveryCfgTimeout_Type()
)
acdRDevDiscoveryCfgTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgTimeout.setStatus("current")


class _AcdRDevDiscoveryCfgDestinationIP_Type(DisplayString):
    """Custom type acdRDevDiscoveryCfgDestinationIP based on DisplayString"""
    defaultHexValue = "00000000"

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )


_AcdRDevDiscoveryCfgDestinationIP_Type.__name__ = "DisplayString"
_AcdRDevDiscoveryCfgDestinationIP_Object = MibTableColumn
acdRDevDiscoveryCfgDestinationIP = _AcdRDevDiscoveryCfgDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 10),
    _AcdRDevDiscoveryCfgDestinationIP_Type()
)
acdRDevDiscoveryCfgDestinationIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgDestinationIP.setStatus("current")


class _AcdRDevDiscoveryCfgIPType_Type(AcdRDevDiscoveryIPType):
    """Custom type acdRDevDiscoveryCfgIPType based on AcdRDevDiscoveryIPType"""
    defaultValue = 1


_AcdRDevDiscoveryCfgIPType_Type.__name__ = "AcdRDevDiscoveryIPType"
_AcdRDevDiscoveryCfgIPType_Object = MibTableColumn
acdRDevDiscoveryCfgIPType = _AcdRDevDiscoveryCfgIPType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 11),
    _AcdRDevDiscoveryCfgIPType_Type()
)
acdRDevDiscoveryCfgIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgIPType.setStatus("current")


class _AcdRDevDiscoveryCfgSerialNumber_Type(DisplayString):
    """Custom type acdRDevDiscoveryCfgSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdRDevDiscoveryCfgSerialNumber_Type.__name__ = "DisplayString"
_AcdRDevDiscoveryCfgSerialNumber_Object = MibTableColumn
acdRDevDiscoveryCfgSerialNumber = _AcdRDevDiscoveryCfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 12),
    _AcdRDevDiscoveryCfgSerialNumber_Type()
)
acdRDevDiscoveryCfgSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgSerialNumber.setStatus("current")
_AcdRDevDiscoveryCfgSubnet_Type = IpAddress
_AcdRDevDiscoveryCfgSubnet_Object = MibTableColumn
acdRDevDiscoveryCfgSubnet = _AcdRDevDiscoveryCfgSubnet_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 1, 3, 1, 1, 13),
    _AcdRDevDiscoveryCfgSubnet_Type()
)
acdRDevDiscoveryCfgSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgSubnet.setStatus("current")
_AcdRDevConformance_ObjectIdentity = ObjectIdentity
acdRDevConformance = _AcdRDevConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 2)
)
_AcdRDevCompliances_ObjectIdentity = ObjectIdentity
acdRDevCompliances = _AcdRDevCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 2, 1)
)
_AcdRDevGroups_ObjectIdentity = ObjectIdentity
acdRDevGroups = _AcdRDevGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 2, 2)
)

# Managed Objects groups

acdRDevConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 2, 2, 1)
)
acdRDevConfigGroup.setObjects(
      *(("ACD-RDEV-MIB", "acdRDevConfigRowStatus"),
        ("ACD-RDEV-MIB", "acdRDevConfigName"),
        ("ACD-RDEV-MIB", "acdRDevConfigMacAddr"),
        ("ACD-RDEV-MIB", "acdRDevConfigSecurityKey"),
        ("ACD-RDEV-MIB", "acdRDevConfigAuthorized"),
        ("ACD-RDEV-MIB", "acdRDevConfigLinked"),
        ("ACD-RDEV-MIB", "acdRDevConfigActiveFeature"),
        ("ACD-RDEV-MIB", "acdRDevConfigCurrentFeatureSuite"),
        ("ACD-RDEV-MIB", "acdRDevConfigAdminState"),
        ("ACD-RDEV-MIB", "acdRDevConfigType"),
        ("ACD-RDEV-MIB", "acdRDevConfigL2Interface"),
        ("ACD-RDEV-MIB", "acdRDevConfigDestinationIP"),
        ("ACD-RDEV-MIB", "acdRDevConfigTunnelTCPPort"),
        ("ACD-RDEV-MIB", "acdRDevConfigTunnelTCPDSCP"),
        ("ACD-RDEV-MIB", "acdRDevConfigFlexMonitor"))
)
if mibBuilder.loadTexts:
    acdRDevConfigGroup.setStatus("current")

acdRDevSecurityKeyMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 2, 2, 2)
)
acdRDevSecurityKeyMgmtGroup.setObjects(
      *(("ACD-RDEV-MIB", "acdRDevSecurityKeyMgmtBackupPeriod"),
        ("ACD-RDEV-MIB", "acdRDevSecurityKeyMgmtServerURL"),
        ("ACD-RDEV-MIB", "acdRDevSecurityKeyMgmtSCPPassword"))
)
if mibBuilder.loadTexts:
    acdRDevSecurityKeyMgmtGroup.setStatus("current")

acdRDevDiscoveryCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 2, 2, 3)
)
acdRDevDiscoveryCfgGroup.setObjects(
      *(("ACD-RDEV-MIB", "acdRDevDiscoveryCfgRowStatus"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgName"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgEnable"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgMethod"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgRate"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgInterface"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgHopLimit"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgTimeout"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgDestinationIP"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgIPType"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgSerialNumber"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgSubnet"))
)
if mibBuilder.loadTexts:
    acdRDevDiscoveryCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdRDevCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 22, 2, 1, 1)
)
acdRDevCompliance.setObjects(
      *(("ACD-RDEV-MIB", "acdRDevConfigGroup"),
        ("ACD-RDEV-MIB", "acdRDevSecurityKeyMgmtGroup"),
        ("ACD-RDEV-MIB", "acdRDevDiscoveryCfgGroup"))
)
if mibBuilder.loadTexts:
    acdRDevCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-RDEV-MIB",
    **{"AcdRDevDiscoveryMethod": AcdRDevDiscoveryMethod,
       "AcdRDevDiscoveryRate": AcdRDevDiscoveryRate,
       "AcdRDevDiscoveryIPType": AcdRDevDiscoveryIPType,
       "AcdRDevConfigAdminStateType": AcdRDevConfigAdminStateType,
       "AcdRDevDeviceTypeType": AcdRDevDeviceTypeType,
       "acdRDev": acdRDev,
       "acdRDevNotifications": acdRDevNotifications,
       "acdRDevMIBObjects": acdRDevMIBObjects,
       "acdRDevConfig": acdRDevConfig,
       "acdRDevConfigTable": acdRDevConfigTable,
       "acdRDevConfigEntry": acdRDevConfigEntry,
       "acdRDevConfigIndex": acdRDevConfigIndex,
       "acdRDevConfigRowStatus": acdRDevConfigRowStatus,
       "acdRDevConfigName": acdRDevConfigName,
       "acdRDevConfigMacAddr": acdRDevConfigMacAddr,
       "acdRDevConfigSecurityKey": acdRDevConfigSecurityKey,
       "acdRDevConfigAuthorized": acdRDevConfigAuthorized,
       "acdRDevConfigLinked": acdRDevConfigLinked,
       "acdRDevConfigActiveFeature": acdRDevConfigActiveFeature,
       "acdRDevConfigCurrentFeatureSuite": acdRDevConfigCurrentFeatureSuite,
       "acdRDevConfigAdminState": acdRDevConfigAdminState,
       "acdRDevConfigType": acdRDevConfigType,
       "acdRDevConfigL2Interface": acdRDevConfigL2Interface,
       "acdRDevConfigDestinationIP": acdRDevConfigDestinationIP,
       "acdRDevConfigTunnelTCPPort": acdRDevConfigTunnelTCPPort,
       "acdRDevConfigTunnelTCPDSCP": acdRDevConfigTunnelTCPDSCP,
       "acdRDevConfigFlexMonitor": acdRDevConfigFlexMonitor,
       "acdRDevSecurityKeyMgmt": acdRDevSecurityKeyMgmt,
       "acdRDevSecurityKeyMgmtBackupPeriod": acdRDevSecurityKeyMgmtBackupPeriod,
       "acdRDevSecurityKeyMgmtServerURL": acdRDevSecurityKeyMgmtServerURL,
       "acdRDevSecurityKeyMgmtSCPPassword": acdRDevSecurityKeyMgmtSCPPassword,
       "acdRDevDiscoveryCfg": acdRDevDiscoveryCfg,
       "acdRDevDiscoveryCfgTable": acdRDevDiscoveryCfgTable,
       "acdRDevDiscoveryCfgEntry": acdRDevDiscoveryCfgEntry,
       "acdRDevDiscoveryCfgIndex": acdRDevDiscoveryCfgIndex,
       "acdRDevDiscoveryCfgRowStatus": acdRDevDiscoveryCfgRowStatus,
       "acdRDevDiscoveryCfgName": acdRDevDiscoveryCfgName,
       "acdRDevDiscoveryCfgEnable": acdRDevDiscoveryCfgEnable,
       "acdRDevDiscoveryCfgMethod": acdRDevDiscoveryCfgMethod,
       "acdRDevDiscoveryCfgRate": acdRDevDiscoveryCfgRate,
       "acdRDevDiscoveryCfgInterface": acdRDevDiscoveryCfgInterface,
       "acdRDevDiscoveryCfgHopLimit": acdRDevDiscoveryCfgHopLimit,
       "acdRDevDiscoveryCfgTimeout": acdRDevDiscoveryCfgTimeout,
       "acdRDevDiscoveryCfgDestinationIP": acdRDevDiscoveryCfgDestinationIP,
       "acdRDevDiscoveryCfgIPType": acdRDevDiscoveryCfgIPType,
       "acdRDevDiscoveryCfgSerialNumber": acdRDevDiscoveryCfgSerialNumber,
       "acdRDevDiscoveryCfgSubnet": acdRDevDiscoveryCfgSubnet,
       "acdRDevConformance": acdRDevConformance,
       "acdRDevCompliances": acdRDevCompliances,
       "acdRDevCompliance": acdRDevCompliance,
       "acdRDevGroups": acdRDevGroups,
       "acdRDevConfigGroup": acdRDevConfigGroup,
       "acdRDevSecurityKeyMgmtGroup": acdRDevSecurityKeyMgmtGroup,
       "acdRDevDiscoveryCfgGroup": acdRDevDiscoveryCfgGroup}
)
