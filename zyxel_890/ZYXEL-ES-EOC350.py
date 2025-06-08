# SNMP MIB module (ZYXEL-ES-EOC350) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-ES-EOC350.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:25:25 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(esPartnerProducts,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esPartnerProducts")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eoc350BrMib_ObjectIdentity = ObjectIdentity
eoc350BrMib = _Eoc350BrMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1)
)
_EocBrSystemGroup_ObjectIdentity = ObjectIdentity
eocBrSystemGroup = _EocBrSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1)
)


class _EocBrModel_Type(Integer32):
    """Custom type eocBrModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            39029
        )
    )
    namedValues = NamedValues(
        ("eOC350-TS", 39029)
    )


_EocBrModel_Type.__name__ = "Integer32"
_EocBrModel_Object = MibScalar
eocBrModel = _EocBrModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 1),
    _EocBrModel_Type()
)
eocBrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrModel.setStatus("current")


class _EocBrProductName_Type(DisplayString):
    """Custom type eocBrProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrProductName_Type.__name__ = "DisplayString"
_EocBrProductName_Object = MibScalar
eocBrProductName = _EocBrProductName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 2),
    _EocBrProductName_Type()
)
eocBrProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrProductName.setStatus("current")
_EocBrSystemMac_Type = MacAddress
_EocBrSystemMac_Object = MibScalar
eocBrSystemMac = _EocBrSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 3),
    _EocBrSystemMac_Type()
)
eocBrSystemMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSystemMac.setStatus("current")
_EocBrEoCMac_Type = MacAddress
_EocBrEoCMac_Object = MibScalar
eocBrEoCMac = _EocBrEoCMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 4),
    _EocBrEoCMac_Type()
)
eocBrEoCMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEoCMac.setStatus("current")


class _EocBrHardwareVersion_Type(DisplayString):
    """Custom type eocBrHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_EocBrHardwareVersion_Type.__name__ = "DisplayString"
_EocBrHardwareVersion_Object = MibScalar
eocBrHardwareVersion = _EocBrHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 5),
    _EocBrHardwareVersion_Type()
)
eocBrHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrHardwareVersion.setStatus("current")


class _EocBrBootVersion_Type(DisplayString):
    """Custom type eocBrBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrBootVersion_Type.__name__ = "DisplayString"
_EocBrBootVersion_Object = MibScalar
eocBrBootVersion = _EocBrBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 6),
    _EocBrBootVersion_Type()
)
eocBrBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrBootVersion.setStatus("current")


class _EocBrSystemFwWorkingVersion_Type(DisplayString):
    """Custom type eocBrSystemFwWorkingVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrSystemFwWorkingVersion_Type.__name__ = "DisplayString"
_EocBrSystemFwWorkingVersion_Object = MibScalar
eocBrSystemFwWorkingVersion = _EocBrSystemFwWorkingVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 7),
    _EocBrSystemFwWorkingVersion_Type()
)
eocBrSystemFwWorkingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSystemFwWorkingVersion.setStatus("current")


class _EocBrSystemFwUploadVersion_Type(DisplayString):
    """Custom type eocBrSystemFwUploadVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrSystemFwUploadVersion_Type.__name__ = "DisplayString"
_EocBrSystemFwUploadVersion_Object = MibScalar
eocBrSystemFwUploadVersion = _EocBrSystemFwUploadVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 8),
    _EocBrSystemFwUploadVersion_Type()
)
eocBrSystemFwUploadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSystemFwUploadVersion.setStatus("current")


class _EocBrSystemFwUpgradeAction_Type(Integer32):
    """Custom type eocBrSystemFwUpgradeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activateThenReboot", 1))
    )


_EocBrSystemFwUpgradeAction_Type.__name__ = "Integer32"
_EocBrSystemFwUpgradeAction_Object = MibScalar
eocBrSystemFwUpgradeAction = _EocBrSystemFwUpgradeAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 9),
    _EocBrSystemFwUpgradeAction_Type()
)
eocBrSystemFwUpgradeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSystemFwUpgradeAction.setStatus("current")


class _EocBrSystemFwUpgradeStatus_Type(Integer32):
    """Custom type eocBrSystemFwUpgradeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOrComplete", 0),
          ("inProgress", 1),
          ("failed", 2))
    )


_EocBrSystemFwUpgradeStatus_Type.__name__ = "Integer32"
_EocBrSystemFwUpgradeStatus_Object = MibScalar
eocBrSystemFwUpgradeStatus = _EocBrSystemFwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 10),
    _EocBrSystemFwUpgradeStatus_Type()
)
eocBrSystemFwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSystemFwUpgradeStatus.setStatus("current")


class _EocBrSystemReboot_Type(Integer32):
    """Custom type eocBrSystemReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activateThenReboot", 1))
    )


_EocBrSystemReboot_Type.__name__ = "Integer32"
_EocBrSystemReboot_Object = MibScalar
eocBrSystemReboot = _EocBrSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 11),
    _EocBrSystemReboot_Type()
)
eocBrSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSystemReboot.setStatus("current")


class _EocBrAutoEPDrvUpgrade_Type(Integer32):
    """Custom type eocBrAutoEPDrvUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrAutoEPDrvUpgrade_Type.__name__ = "Integer32"
_EocBrAutoEPDrvUpgrade_Object = MibScalar
eocBrAutoEPDrvUpgrade = _EocBrAutoEPDrvUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 1, 15),
    _EocBrAutoEPDrvUpgrade_Type()
)
eocBrAutoEPDrvUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAutoEPDrvUpgrade.setStatus("current")
_EocBrIPGroup_ObjectIdentity = ObjectIdentity
eocBrIPGroup = _EocBrIPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2)
)
_EocBrIPAddress_Type = IpAddress
_EocBrIPAddress_Object = MibScalar
eocBrIPAddress = _EocBrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 1),
    _EocBrIPAddress_Type()
)
eocBrIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrIPAddress.setStatus("current")
_EocBrSubnetMask_Type = IpAddress
_EocBrSubnetMask_Object = MibScalar
eocBrSubnetMask = _EocBrSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 2),
    _EocBrSubnetMask_Type()
)
eocBrSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSubnetMask.setStatus("current")
_EocBrDefaultGatewayIPAddress_Type = IpAddress
_EocBrDefaultGatewayIPAddress_Object = MibScalar
eocBrDefaultGatewayIPAddress = _EocBrDefaultGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 3),
    _EocBrDefaultGatewayIPAddress_Type()
)
eocBrDefaultGatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrDefaultGatewayIPAddress.setStatus("current")
_EocBrPrimaryDnsIPAddress_Type = IpAddress
_EocBrPrimaryDnsIPAddress_Object = MibScalar
eocBrPrimaryDnsIPAddress = _EocBrPrimaryDnsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 4),
    _EocBrPrimaryDnsIPAddress_Type()
)
eocBrPrimaryDnsIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrPrimaryDnsIPAddress.setStatus("current")
_EocBrSecondaryDnsIPAddress_Type = IpAddress
_EocBrSecondaryDnsIPAddress_Object = MibScalar
eocBrSecondaryDnsIPAddress = _EocBrSecondaryDnsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 5),
    _EocBrSecondaryDnsIPAddress_Type()
)
eocBrSecondaryDnsIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSecondaryDnsIPAddress.setStatus("current")


class _EocBrIPAddressAssign_Type(Integer32):
    """Custom type eocBrIPAddressAssign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic-dhcp", 1))
    )


_EocBrIPAddressAssign_Type.__name__ = "Integer32"
_EocBrIPAddressAssign_Object = MibScalar
eocBrIPAddressAssign = _EocBrIPAddressAssign_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 6),
    _EocBrIPAddressAssign_Type()
)
eocBrIPAddressAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrIPAddressAssign.setStatus("current")
_EocBrDHCPLease_Type = Integer32
_EocBrDHCPLease_Object = MibScalar
eocBrDHCPLease = _EocBrDHCPLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 8),
    _EocBrDHCPLease_Type()
)
eocBrDHCPLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrDHCPLease.setStatus("current")


class _EocBrHostDHCPPadOpt82EnableCtrl_Type(Integer32):
    """Custom type eocBrHostDHCPPadOpt82EnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrHostDHCPPadOpt82EnableCtrl_Type.__name__ = "Integer32"
_EocBrHostDHCPPadOpt82EnableCtrl_Object = MibScalar
eocBrHostDHCPPadOpt82EnableCtrl = _EocBrHostDHCPPadOpt82EnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 10),
    _EocBrHostDHCPPadOpt82EnableCtrl_Type()
)
eocBrHostDHCPPadOpt82EnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrHostDHCPPadOpt82EnableCtrl.setStatus("current")


class _EocBrHostIPSourceGuardCtrl_Type(Integer32):
    """Custom type eocBrHostIPSourceGuardCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrHostIPSourceGuardCtrl_Type.__name__ = "Integer32"
_EocBrHostIPSourceGuardCtrl_Object = MibScalar
eocBrHostIPSourceGuardCtrl = _EocBrHostIPSourceGuardCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 12),
    _EocBrHostIPSourceGuardCtrl_Type()
)
eocBrHostIPSourceGuardCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrHostIPSourceGuardCtrl.setStatus("current")
_EocBrHostDHCPTable_Object = MibTable
eocBrHostDHCPTable = _EocBrHostDHCPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 13)
)
if mibBuilder.loadTexts:
    eocBrHostDHCPTable.setStatus("current")
_EocBrHostDHCPEntry_Object = MibTableRow
eocBrHostDHCPEntry = _EocBrHostDHCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 13, 1)
)
eocBrHostDHCPEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrHostDHCPIndex"),
)
if mibBuilder.loadTexts:
    eocBrHostDHCPEntry.setStatus("current")
_EocBrHostDHCPIndex_Type = Integer32
_EocBrHostDHCPIndex_Object = MibTableColumn
eocBrHostDHCPIndex = _EocBrHostDHCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 13, 1, 1),
    _EocBrHostDHCPIndex_Type()
)
eocBrHostDHCPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrHostDHCPIndex.setStatus("current")
_EocBrHostDHCPEPMac_Type = MacAddress
_EocBrHostDHCPEPMac_Object = MibTableColumn
eocBrHostDHCPEPMac = _EocBrHostDHCPEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 13, 1, 3),
    _EocBrHostDHCPEPMac_Type()
)
eocBrHostDHCPEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrHostDHCPEPMac.setStatus("current")
_EocBrHostDHCPHostMac_Type = MacAddress
_EocBrHostDHCPHostMac_Object = MibTableColumn
eocBrHostDHCPHostMac = _EocBrHostDHCPHostMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 13, 1, 4),
    _EocBrHostDHCPHostMac_Type()
)
eocBrHostDHCPHostMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrHostDHCPHostMac.setStatus("current")
_EocBrHostDHCPIPAddress_Type = IpAddress
_EocBrHostDHCPIPAddress_Object = MibTableColumn
eocBrHostDHCPIPAddress = _EocBrHostDHCPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 13, 1, 5),
    _EocBrHostDHCPIPAddress_Type()
)
eocBrHostDHCPIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrHostDHCPIPAddress.setStatus("current")
_EocBrHostDHCPLease_Type = Integer32
_EocBrHostDHCPLease_Object = MibTableColumn
eocBrHostDHCPLease = _EocBrHostDHCPLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 13, 1, 6),
    _EocBrHostDHCPLease_Type()
)
eocBrHostDHCPLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrHostDHCPLease.setStatus("current")


class _EocBrAutoConfig_Type(Integer32):
    """Custom type eocBrAutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrAutoConfig_Type.__name__ = "Integer32"
_EocBrAutoConfig_Object = MibScalar
eocBrAutoConfig = _EocBrAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 15),
    _EocBrAutoConfig_Type()
)
eocBrAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAutoConfig.setStatus("current")
_EocBrAutoConfigTFTPServerIPAddress_Type = IpAddress
_EocBrAutoConfigTFTPServerIPAddress_Object = MibScalar
eocBrAutoConfigTFTPServerIPAddress = _EocBrAutoConfigTFTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 16),
    _EocBrAutoConfigTFTPServerIPAddress_Type()
)
eocBrAutoConfigTFTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAutoConfigTFTPServerIPAddress.setStatus("current")


class _EocBrAutoConfigTFTPExtensionPath_Type(DisplayString):
    """Custom type eocBrAutoConfigTFTPExtensionPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EocBrAutoConfigTFTPExtensionPath_Type.__name__ = "DisplayString"
_EocBrAutoConfigTFTPExtensionPath_Object = MibScalar
eocBrAutoConfigTFTPExtensionPath = _EocBrAutoConfigTFTPExtensionPath_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 17),
    _EocBrAutoConfigTFTPExtensionPath_Type()
)
eocBrAutoConfigTFTPExtensionPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAutoConfigTFTPExtensionPath.setStatus("current")


class _EocBrAutoConfigTFTPServer_Type(DisplayString):
    """Custom type eocBrAutoConfigTFTPServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrAutoConfigTFTPServer_Type.__name__ = "DisplayString"
_EocBrAutoConfigTFTPServer_Object = MibScalar
eocBrAutoConfigTFTPServer = _EocBrAutoConfigTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 2, 18),
    _EocBrAutoConfigTFTPServer_Type()
)
eocBrAutoConfigTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAutoConfigTFTPServer.setStatus("current")
_EocBrAdminGroup_ObjectIdentity = ObjectIdentity
eocBrAdminGroup = _EocBrAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4)
)
_EocBrAccountTable_Object = MibTable
eocBrAccountTable = _EocBrAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eocBrAccountTable.setStatus("current")
_EocBrAccountEntry_Object = MibTableRow
eocBrAccountEntry = _EocBrAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 1, 1)
)
eocBrAccountEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrAccountIndex"),
)
if mibBuilder.loadTexts:
    eocBrAccountEntry.setStatus("current")
_EocBrAccountIndex_Type = Integer32
_EocBrAccountIndex_Object = MibTableColumn
eocBrAccountIndex = _EocBrAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 1, 1, 1),
    _EocBrAccountIndex_Type()
)
eocBrAccountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrAccountIndex.setStatus("current")


class _EocBrAccountName_Type(DisplayString):
    """Custom type eocBrAccountName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EocBrAccountName_Type.__name__ = "DisplayString"
_EocBrAccountName_Object = MibTableColumn
eocBrAccountName = _EocBrAccountName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 1, 1, 2),
    _EocBrAccountName_Type()
)
eocBrAccountName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAccountName.setStatus("current")


class _EocBrAccountPasswd_Type(DisplayString):
    """Custom type eocBrAccountPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EocBrAccountPasswd_Type.__name__ = "DisplayString"
_EocBrAccountPasswd_Object = MibTableColumn
eocBrAccountPasswd = _EocBrAccountPasswd_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 1, 1, 3),
    _EocBrAccountPasswd_Type()
)
eocBrAccountPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAccountPasswd.setStatus("current")


class _EocBrAccountPrivilege_Type(Integer32):
    """Custom type eocBrAccountPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("superuser", 0),
          ("readWrite", 1),
          ("readOnly", 2))
    )


_EocBrAccountPrivilege_Type.__name__ = "Integer32"
_EocBrAccountPrivilege_Object = MibTableColumn
eocBrAccountPrivilege = _EocBrAccountPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 1, 1, 4),
    _EocBrAccountPrivilege_Type()
)
eocBrAccountPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAccountPrivilege.setStatus("current")
_EocBrAccountRowStatus_Type = RowStatus
_EocBrAccountRowStatus_Object = MibTableColumn
eocBrAccountRowStatus = _EocBrAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 1, 1, 5),
    _EocBrAccountRowStatus_Type()
)
eocBrAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eocBrAccountRowStatus.setStatus("current")
_EocBrAllowIPProtocolTable_Object = MibTable
eocBrAllowIPProtocolTable = _EocBrAllowIPProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    eocBrAllowIPProtocolTable.setStatus("current")
_EocBrAllowIPProtocolEntry_Object = MibTableRow
eocBrAllowIPProtocolEntry = _EocBrAllowIPProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 2, 1)
)
eocBrAllowIPProtocolEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrAllowIndex"),
)
if mibBuilder.loadTexts:
    eocBrAllowIPProtocolEntry.setStatus("current")
_EocBrAllowIndex_Type = Integer32
_EocBrAllowIndex_Object = MibTableColumn
eocBrAllowIndex = _EocBrAllowIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 2, 1, 1),
    _EocBrAllowIndex_Type()
)
eocBrAllowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrAllowIndex.setStatus("current")
_EocBrAllowIPAddress_Type = IpAddress
_EocBrAllowIPAddress_Object = MibTableColumn
eocBrAllowIPAddress = _EocBrAllowIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 2, 1, 2),
    _EocBrAllowIPAddress_Type()
)
eocBrAllowIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAllowIPAddress.setStatus("current")
_EocBrAllowSubnetMask_Type = IpAddress
_EocBrAllowSubnetMask_Object = MibTableColumn
eocBrAllowSubnetMask = _EocBrAllowSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 2, 1, 3),
    _EocBrAllowSubnetMask_Type()
)
eocBrAllowSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAllowSubnetMask.setStatus("current")


class _EocBrAllowTelnet_Type(Integer32):
    """Custom type eocBrAllowTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_EocBrAllowTelnet_Type.__name__ = "Integer32"
_EocBrAllowTelnet_Object = MibTableColumn
eocBrAllowTelnet = _EocBrAllowTelnet_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 2, 1, 4),
    _EocBrAllowTelnet_Type()
)
eocBrAllowTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAllowTelnet.setStatus("current")


class _EocBrAllowHttp_Type(Integer32):
    """Custom type eocBrAllowHttp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_EocBrAllowHttp_Type.__name__ = "Integer32"
_EocBrAllowHttp_Object = MibTableColumn
eocBrAllowHttp = _EocBrAllowHttp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 2, 1, 5),
    _EocBrAllowHttp_Type()
)
eocBrAllowHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAllowHttp.setStatus("current")


class _EocBrAllowSnmp_Type(Integer32):
    """Custom type eocBrAllowSnmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_EocBrAllowSnmp_Type.__name__ = "Integer32"
_EocBrAllowSnmp_Object = MibTableColumn
eocBrAllowSnmp = _EocBrAllowSnmp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 2, 1, 6),
    _EocBrAllowSnmp_Type()
)
eocBrAllowSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAllowSnmp.setStatus("current")


class _EocBrAllowIcmpPing_Type(Integer32):
    """Custom type eocBrAllowIcmpPing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_EocBrAllowIcmpPing_Type.__name__ = "Integer32"
_EocBrAllowIcmpPing_Object = MibTableColumn
eocBrAllowIcmpPing = _EocBrAllowIcmpPing_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 2, 1, 7),
    _EocBrAllowIcmpPing_Type()
)
eocBrAllowIcmpPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrAllowIcmpPing.setStatus("current")
_EocBrAllowRowStatus_Type = RowStatus
_EocBrAllowRowStatus_Object = MibTableColumn
eocBrAllowRowStatus = _EocBrAllowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 2, 1, 8),
    _EocBrAllowRowStatus_Type()
)
eocBrAllowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eocBrAllowRowStatus.setStatus("current")
_EocBrStaticMacTable_Object = MibTable
eocBrStaticMacTable = _EocBrStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 3)
)
if mibBuilder.loadTexts:
    eocBrStaticMacTable.setStatus("current")
_EocBrStaticMacEntry_Object = MibTableRow
eocBrStaticMacEntry = _EocBrStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 3, 1)
)
eocBrStaticMacEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrStaticMacIndex"),
)
if mibBuilder.loadTexts:
    eocBrStaticMacEntry.setStatus("current")
_EocBrStaticMacIndex_Type = Integer32
_EocBrStaticMacIndex_Object = MibTableColumn
eocBrStaticMacIndex = _EocBrStaticMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 3, 1, 1),
    _EocBrStaticMacIndex_Type()
)
eocBrStaticMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrStaticMacIndex.setStatus("current")
_EocBrStaticMacAddress_Type = MacAddress
_EocBrStaticMacAddress_Object = MibTableColumn
eocBrStaticMacAddress = _EocBrStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 3, 1, 2),
    _EocBrStaticMacAddress_Type()
)
eocBrStaticMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrStaticMacAddress.setStatus("current")


class _EocBrStaticMacBindingPort_Type(Integer32):
    """Custom type eocBrStaticMacBindingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan1", 1),
          ("lan2", 2))
    )


_EocBrStaticMacBindingPort_Type.__name__ = "Integer32"
_EocBrStaticMacBindingPort_Object = MibTableColumn
eocBrStaticMacBindingPort = _EocBrStaticMacBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 3, 1, 3),
    _EocBrStaticMacBindingPort_Type()
)
eocBrStaticMacBindingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrStaticMacBindingPort.setStatus("current")
_EocBrStaticMacRowStatus_Type = RowStatus
_EocBrStaticMacRowStatus_Object = MibTableColumn
eocBrStaticMacRowStatus = _EocBrStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 4, 3, 1, 4),
    _EocBrStaticMacRowStatus_Type()
)
eocBrStaticMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eocBrStaticMacRowStatus.setStatus("current")
_EocBrServiceGroup_ObjectIdentity = ObjectIdentity
eocBrServiceGroup = _EocBrServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5)
)
_EocBrTelnet_ObjectIdentity = ObjectIdentity
eocBrTelnet = _EocBrTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 1)
)


class _EocBrTelnetEnableCtrl_Type(Integer32):
    """Custom type eocBrTelnetEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrTelnetEnableCtrl_Type.__name__ = "Integer32"
_EocBrTelnetEnableCtrl_Object = MibScalar
eocBrTelnetEnableCtrl = _EocBrTelnetEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 1, 1),
    _EocBrTelnetEnableCtrl_Type()
)
eocBrTelnetEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTelnetEnableCtrl.setStatus("current")


class _EocBrTelnetPortNum_Type(Integer32):
    """Custom type eocBrTelnetPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrTelnetPortNum_Type.__name__ = "Integer32"
_EocBrTelnetPortNum_Object = MibScalar
eocBrTelnetPortNum = _EocBrTelnetPortNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 1, 2),
    _EocBrTelnetPortNum_Type()
)
eocBrTelnetPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTelnetPortNum.setStatus("current")


class _EocBrTelnetExpiryInSeconds_Type(Integer32):
    """Custom type eocBrTelnetExpiryInSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrTelnetExpiryInSeconds_Type.__name__ = "Integer32"
_EocBrTelnetExpiryInSeconds_Object = MibScalar
eocBrTelnetExpiryInSeconds = _EocBrTelnetExpiryInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 1, 3),
    _EocBrTelnetExpiryInSeconds_Type()
)
eocBrTelnetExpiryInSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTelnetExpiryInSeconds.setStatus("current")
_EocBrHttp_ObjectIdentity = ObjectIdentity
eocBrHttp = _EocBrHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 2)
)


class _EocBrHttpEnableCtrl_Type(Integer32):
    """Custom type eocBrHttpEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrHttpEnableCtrl_Type.__name__ = "Integer32"
_EocBrHttpEnableCtrl_Object = MibScalar
eocBrHttpEnableCtrl = _EocBrHttpEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 2, 1),
    _EocBrHttpEnableCtrl_Type()
)
eocBrHttpEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrHttpEnableCtrl.setStatus("current")


class _EocBrHttpPortNum_Type(Integer32):
    """Custom type eocBrHttpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrHttpPortNum_Type.__name__ = "Integer32"
_EocBrHttpPortNum_Object = MibScalar
eocBrHttpPortNum = _EocBrHttpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 2, 2),
    _EocBrHttpPortNum_Type()
)
eocBrHttpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrHttpPortNum.setStatus("current")
_EocBrSnmp_ObjectIdentity = ObjectIdentity
eocBrSnmp = _EocBrSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3)
)


class _EocBrSnmpEnableCtrl_Type(Integer32):
    """Custom type eocBrSnmpEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrSnmpEnableCtrl_Type.__name__ = "Integer32"
_EocBrSnmpEnableCtrl_Object = MibScalar
eocBrSnmpEnableCtrl = _EocBrSnmpEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 1),
    _EocBrSnmpEnableCtrl_Type()
)
eocBrSnmpEnableCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSnmpEnableCtrl.setStatus("current")


class _EocBrSnmpPortNum_Type(Integer32):
    """Custom type eocBrSnmpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrSnmpPortNum_Type.__name__ = "Integer32"
_EocBrSnmpPortNum_Object = MibScalar
eocBrSnmpPortNum = _EocBrSnmpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 2),
    _EocBrSnmpPortNum_Type()
)
eocBrSnmpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSnmpPortNum.setStatus("current")


class _EocBrSnmpName_Type(DisplayString):
    """Custom type eocBrSnmpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrSnmpName_Type.__name__ = "DisplayString"
_EocBrSnmpName_Object = MibScalar
eocBrSnmpName = _EocBrSnmpName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 3),
    _EocBrSnmpName_Type()
)
eocBrSnmpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSnmpName.setStatus("current")


class _EocBrSnmpContact_Type(DisplayString):
    """Custom type eocBrSnmpContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrSnmpContact_Type.__name__ = "DisplayString"
_EocBrSnmpContact_Object = MibScalar
eocBrSnmpContact = _EocBrSnmpContact_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 4),
    _EocBrSnmpContact_Type()
)
eocBrSnmpContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSnmpContact.setStatus("current")


class _EocBrSnmpLocation_Type(DisplayString):
    """Custom type eocBrSnmpLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrSnmpLocation_Type.__name__ = "DisplayString"
_EocBrSnmpLocation_Object = MibScalar
eocBrSnmpLocation = _EocBrSnmpLocation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 5),
    _EocBrSnmpLocation_Type()
)
eocBrSnmpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSnmpLocation.setStatus("current")


class _EocBrSnmpReadWriteCommunity_Type(DisplayString):
    """Custom type eocBrSnmpReadWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrSnmpReadWriteCommunity_Type.__name__ = "DisplayString"
_EocBrSnmpReadWriteCommunity_Object = MibScalar
eocBrSnmpReadWriteCommunity = _EocBrSnmpReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 6),
    _EocBrSnmpReadWriteCommunity_Type()
)
eocBrSnmpReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSnmpReadWriteCommunity.setStatus("current")


class _EocBrSnmpReadOnlyCommunity_Type(DisplayString):
    """Custom type eocBrSnmpReadOnlyCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrSnmpReadOnlyCommunity_Type.__name__ = "DisplayString"
_EocBrSnmpReadOnlyCommunity_Object = MibScalar
eocBrSnmpReadOnlyCommunity = _EocBrSnmpReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 7),
    _EocBrSnmpReadOnlyCommunity_Type()
)
eocBrSnmpReadOnlyCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSnmpReadOnlyCommunity.setStatus("current")
_EocBrSnmpTrapEnableTable_Object = MibTable
eocBrSnmpTrapEnableTable = _EocBrSnmpTrapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 8)
)
if mibBuilder.loadTexts:
    eocBrSnmpTrapEnableTable.setStatus("current")
_EocBrSnmpTrapEnableEntry_Object = MibTableRow
eocBrSnmpTrapEnableEntry = _EocBrSnmpTrapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 8, 1)
)
eocBrSnmpTrapEnableEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrSnmpTrapEnableIndex"),
)
if mibBuilder.loadTexts:
    eocBrSnmpTrapEnableEntry.setStatus("current")
_EocBrSnmpTrapEnableIndex_Type = Integer32
_EocBrSnmpTrapEnableIndex_Object = MibTableColumn
eocBrSnmpTrapEnableIndex = _EocBrSnmpTrapEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 8, 1, 1),
    _EocBrSnmpTrapEnableIndex_Type()
)
eocBrSnmpTrapEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSnmpTrapEnableIndex.setStatus("current")


class _EocBrSnmpTrapEnableType_Type(Integer32):
    """Custom type eocBrSnmpTrapEnableType based on Integer32"""
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
        *(("logInOut", 0),
          ("upgrade", 1),
          ("epStatus", 2),
          ("epDiagnosis", 3),
          ("dhcp", 4),
          ("autoConfig", 5))
    )


_EocBrSnmpTrapEnableType_Type.__name__ = "Integer32"
_EocBrSnmpTrapEnableType_Object = MibTableColumn
eocBrSnmpTrapEnableType = _EocBrSnmpTrapEnableType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 8, 1, 2),
    _EocBrSnmpTrapEnableType_Type()
)
eocBrSnmpTrapEnableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSnmpTrapEnableType.setStatus("current")


class _EocBrSnmpTrapEnableCtrl_Type(Integer32):
    """Custom type eocBrSnmpTrapEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrSnmpTrapEnableCtrl_Type.__name__ = "Integer32"
_EocBrSnmpTrapEnableCtrl_Object = MibTableColumn
eocBrSnmpTrapEnableCtrl = _EocBrSnmpTrapEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 8, 1, 3),
    _EocBrSnmpTrapEnableCtrl_Type()
)
eocBrSnmpTrapEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSnmpTrapEnableCtrl.setStatus("current")
_EocBrSnmpTrapTable_Object = MibTable
eocBrSnmpTrapTable = _EocBrSnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 9)
)
if mibBuilder.loadTexts:
    eocBrSnmpTrapTable.setStatus("current")
_EocBrSnmpTrapEntry_Object = MibTableRow
eocBrSnmpTrapEntry = _EocBrSnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 9, 1)
)
eocBrSnmpTrapEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrSnmpTrapIndex"),
)
if mibBuilder.loadTexts:
    eocBrSnmpTrapEntry.setStatus("current")
_EocBrSnmpTrapIndex_Type = Integer32
_EocBrSnmpTrapIndex_Object = MibTableColumn
eocBrSnmpTrapIndex = _EocBrSnmpTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 9, 1, 1),
    _EocBrSnmpTrapIndex_Type()
)
eocBrSnmpTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSnmpTrapIndex.setStatus("current")


class _EocBrSnmpTrapServer_Type(DisplayString):
    """Custom type eocBrSnmpTrapServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrSnmpTrapServer_Type.__name__ = "DisplayString"
_EocBrSnmpTrapServer_Object = MibTableColumn
eocBrSnmpTrapServer = _EocBrSnmpTrapServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 9, 1, 2),
    _EocBrSnmpTrapServer_Type()
)
eocBrSnmpTrapServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSnmpTrapServer.setStatus("current")


class _EocBrSnmpTrapPortNum_Type(Integer32):
    """Custom type eocBrSnmpTrapPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrSnmpTrapPortNum_Type.__name__ = "Integer32"
_EocBrSnmpTrapPortNum_Object = MibTableColumn
eocBrSnmpTrapPortNum = _EocBrSnmpTrapPortNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 9, 1, 4),
    _EocBrSnmpTrapPortNum_Type()
)
eocBrSnmpTrapPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSnmpTrapPortNum.setStatus("current")


class _EocBrSnmpTrapCommunity_Type(DisplayString):
    """Custom type eocBrSnmpTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrSnmpTrapCommunity_Type.__name__ = "DisplayString"
_EocBrSnmpTrapCommunity_Object = MibTableColumn
eocBrSnmpTrapCommunity = _EocBrSnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 9, 1, 5),
    _EocBrSnmpTrapCommunity_Type()
)
eocBrSnmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSnmpTrapCommunity.setStatus("current")
_EocBrSnmpTrapRowStatus_Type = RowStatus
_EocBrSnmpTrapRowStatus_Object = MibTableColumn
eocBrSnmpTrapRowStatus = _EocBrSnmpTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 3, 9, 1, 6),
    _EocBrSnmpTrapRowStatus_Type()
)
eocBrSnmpTrapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eocBrSnmpTrapRowStatus.setStatus("current")
_EocBrSyslogTable_Object = MibTable
eocBrSyslogTable = _EocBrSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 4)
)
if mibBuilder.loadTexts:
    eocBrSyslogTable.setStatus("current")
_EocBrSyslogEntry_Object = MibTableRow
eocBrSyslogEntry = _EocBrSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 4, 1)
)
eocBrSyslogEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrSyslogIndex"),
)
if mibBuilder.loadTexts:
    eocBrSyslogEntry.setStatus("current")
_EocBrSyslogIndex_Type = Integer32
_EocBrSyslogIndex_Object = MibTableColumn
eocBrSyslogIndex = _EocBrSyslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 4, 1, 1),
    _EocBrSyslogIndex_Type()
)
eocBrSyslogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSyslogIndex.setStatus("current")


class _EocBrSyslogServer_Type(DisplayString):
    """Custom type eocBrSyslogServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrSyslogServer_Type.__name__ = "DisplayString"
_EocBrSyslogServer_Object = MibTableColumn
eocBrSyslogServer = _EocBrSyslogServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 4, 1, 2),
    _EocBrSyslogServer_Type()
)
eocBrSyslogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSyslogServer.setStatus("current")
_EocBrSyslogIPAddress_Type = IpAddress
_EocBrSyslogIPAddress_Object = MibTableColumn
eocBrSyslogIPAddress = _EocBrSyslogIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 4, 1, 3),
    _EocBrSyslogIPAddress_Type()
)
eocBrSyslogIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSyslogIPAddress.setStatus("current")


class _EocBrSyslogSeverity_Type(Integer32):
    """Custom type eocBrSyslogSeverity based on Integer32"""
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


_EocBrSyslogSeverity_Type.__name__ = "Integer32"
_EocBrSyslogSeverity_Object = MibTableColumn
eocBrSyslogSeverity = _EocBrSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 4, 1, 4),
    _EocBrSyslogSeverity_Type()
)
eocBrSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSyslogSeverity.setStatus("current")
_EocBrSyslogRowStatus_Type = RowStatus
_EocBrSyslogRowStatus_Object = MibTableColumn
eocBrSyslogRowStatus = _EocBrSyslogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 4, 1, 5),
    _EocBrSyslogRowStatus_Type()
)
eocBrSyslogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eocBrSyslogRowStatus.setStatus("current")
_EocBrSntp_ObjectIdentity = ObjectIdentity
eocBrSntp = _EocBrSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 5)
)


class _EocBrSntpEnableCtrl_Type(Integer32):
    """Custom type eocBrSntpEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrSntpEnableCtrl_Type.__name__ = "Integer32"
_EocBrSntpEnableCtrl_Object = MibScalar
eocBrSntpEnableCtrl = _EocBrSntpEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 5, 1),
    _EocBrSntpEnableCtrl_Type()
)
eocBrSntpEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSntpEnableCtrl.setStatus("current")


class _EocBrSntpPrimaryServer_Type(DisplayString):
    """Custom type eocBrSntpPrimaryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrSntpPrimaryServer_Type.__name__ = "DisplayString"
_EocBrSntpPrimaryServer_Object = MibScalar
eocBrSntpPrimaryServer = _EocBrSntpPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 5, 2),
    _EocBrSntpPrimaryServer_Type()
)
eocBrSntpPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSntpPrimaryServer.setStatus("current")


class _EocBrSntpSecondaryServer_Type(DisplayString):
    """Custom type eocBrSntpSecondaryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrSntpSecondaryServer_Type.__name__ = "DisplayString"
_EocBrSntpSecondaryServer_Object = MibScalar
eocBrSntpSecondaryServer = _EocBrSntpSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 5, 3),
    _EocBrSntpSecondaryServer_Type()
)
eocBrSntpSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSntpSecondaryServer.setStatus("current")


class _EocBrSntpTimeZone_Type(Integer32):
    """Custom type eocBrSntpTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              8,
              12,
              14,
              16,
              18,
              20,
              23,
              24,
              26,
              28,
              32,
              36,
              38,
              40,
              44,
              48,
              208,
              212,
              216,
              220,
              224,
              228,
              232,
              236,
              240,
              242,
              244,
              248,
              252)
        )
    )
    namedValues = NamedValues(
        *(("gmt", 0),
          ("gmt-plus-0100", 4),
          ("gmt-plus-0200", 8),
          ("gmt-plus-0300", 12),
          ("gmt-plus-0330", 14),
          ("gmt-plus-0400", 16),
          ("gmt-plus-0430", 18),
          ("gmt-plus-0500", 20),
          ("gmt-plus-0545", 23),
          ("gmt-plus-0600", 24),
          ("gmt-plus-0630", 26),
          ("gmt-plus-0700", 28),
          ("gmt-plus-0800", 32),
          ("gmt-plus-0900", 36),
          ("gmt-plus-0930", 38),
          ("gmt-plus-1000", 40),
          ("gmt-plus-1100", 44),
          ("gmt-plus-1200", 48),
          ("gmt-minus-1200", 208),
          ("gmt-minus-1100", 212),
          ("gmt-minus-1000", 216),
          ("gmt-minus-0900", 220),
          ("gmt-minus-0800", 224),
          ("gmt-minus-0700", 228),
          ("gmt-minus-0600", 232),
          ("gmt-minus-0500", 236),
          ("gmt-minus-0400", 240),
          ("gmt-minus-0330", 242),
          ("gmt-minus-0300", 244),
          ("gmt-minus-0200", 248),
          ("gmt-minus-0100", 252))
    )


_EocBrSntpTimeZone_Type.__name__ = "Integer32"
_EocBrSntpTimeZone_Object = MibScalar
eocBrSntpTimeZone = _EocBrSntpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 5, 4),
    _EocBrSntpTimeZone_Type()
)
eocBrSntpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSntpTimeZone.setStatus("current")


class _EocBrSntpQueryPeriodInMinutes_Type(Integer32):
    """Custom type eocBrSntpQueryPeriodInMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrSntpQueryPeriodInMinutes_Type.__name__ = "Integer32"
_EocBrSntpQueryPeriodInMinutes_Object = MibScalar
eocBrSntpQueryPeriodInMinutes = _EocBrSntpQueryPeriodInMinutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 5, 5),
    _EocBrSntpQueryPeriodInMinutes_Type()
)
eocBrSntpQueryPeriodInMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSntpQueryPeriodInMinutes.setStatus("current")


class _EocBrSntpCurrentTime_Type(DisplayString):
    """Custom type eocBrSntpCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrSntpCurrentTime_Type.__name__ = "DisplayString"
_EocBrSntpCurrentTime_Object = MibScalar
eocBrSntpCurrentTime = _EocBrSntpCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 5, 6),
    _EocBrSntpCurrentTime_Type()
)
eocBrSntpCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrSntpCurrentTime.setStatus("current")
_EocBrSyslogCtrl_ObjectIdentity = ObjectIdentity
eocBrSyslogCtrl = _EocBrSyslogCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 6)
)


class _EocBrSyslogOverTcpUdp_Type(Integer32):
    """Custom type eocBrSyslogOverTcpUdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("tcp", 1))
    )


_EocBrSyslogOverTcpUdp_Type.__name__ = "Integer32"
_EocBrSyslogOverTcpUdp_Object = MibScalar
eocBrSyslogOverTcpUdp = _EocBrSyslogOverTcpUdp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 6, 1),
    _EocBrSyslogOverTcpUdp_Type()
)
eocBrSyslogOverTcpUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSyslogOverTcpUdp.setStatus("current")


class _EocBrSyslogPortNum_Type(Integer32):
    """Custom type eocBrSyslogPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrSyslogPortNum_Type.__name__ = "Integer32"
_EocBrSyslogPortNum_Object = MibScalar
eocBrSyslogPortNum = _EocBrSyslogPortNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 5, 6, 2),
    _EocBrSyslogPortNum_Type()
)
eocBrSyslogPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrSyslogPortNum.setStatus("current")
_EocBrMasterEoCGroup_ObjectIdentity = ObjectIdentity
eocBrMasterEoCGroup = _EocBrMasterEoCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7)
)
_EocBrMasterMac_Type = MacAddress
_EocBrMasterMac_Object = MibScalar
eocBrMasterMac = _EocBrMasterMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 1),
    _EocBrMasterMac_Type()
)
eocBrMasterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrMasterMac.setStatus("current")


class _EocBrMasterNote_Type(DisplayString):
    """Custom type eocBrMasterNote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrMasterNote_Type.__name__ = "DisplayString"
_EocBrMasterNote_Object = MibScalar
eocBrMasterNote = _EocBrMasterNote_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 2),
    _EocBrMasterNote_Type()
)
eocBrMasterNote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrMasterNote.setStatus("current")


class _EocBrMasterModel_Type(Integer32):
    """Custom type eocBrMasterModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            39029
        )
    )
    namedValues = NamedValues(
        ("eOC350-TS", 39029)
    )


_EocBrMasterModel_Type.__name__ = "Integer32"
_EocBrMasterModel_Object = MibScalar
eocBrMasterModel = _EocBrMasterModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 3),
    _EocBrMasterModel_Type()
)
eocBrMasterModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrMasterModel.setStatus("current")


class _EocBrMasterProductName_Type(DisplayString):
    """Custom type eocBrMasterProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrMasterProductName_Type.__name__ = "DisplayString"
_EocBrMasterProductName_Object = MibScalar
eocBrMasterProductName = _EocBrMasterProductName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 4),
    _EocBrMasterProductName_Type()
)
eocBrMasterProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrMasterProductName.setStatus("current")


class _EocBrMasterWorkingPrivacyMode_Type(Integer32):
    """Custom type eocBrMasterWorkingPrivacyMode based on Integer32"""
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


_EocBrMasterWorkingPrivacyMode_Type.__name__ = "Integer32"
_EocBrMasterWorkingPrivacyMode_Object = MibScalar
eocBrMasterWorkingPrivacyMode = _EocBrMasterWorkingPrivacyMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 5),
    _EocBrMasterWorkingPrivacyMode_Type()
)
eocBrMasterWorkingPrivacyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrMasterWorkingPrivacyMode.setStatus("current")


class _EocBrMasterSettingPrivacyMode_Type(Integer32):
    """Custom type eocBrMasterSettingPrivacyMode based on Integer32"""
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


_EocBrMasterSettingPrivacyMode_Type.__name__ = "Integer32"
_EocBrMasterSettingPrivacyMode_Object = MibScalar
eocBrMasterSettingPrivacyMode = _EocBrMasterSettingPrivacyMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 6),
    _EocBrMasterSettingPrivacyMode_Type()
)
eocBrMasterSettingPrivacyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrMasterSettingPrivacyMode.setStatus("current")


class _EocBrMasterWorkingPrivacyKey_Type(Integer32):
    """Custom type eocBrMasterWorkingPrivacyKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrMasterWorkingPrivacyKey_Type.__name__ = "Integer32"
_EocBrMasterWorkingPrivacyKey_Object = MibScalar
eocBrMasterWorkingPrivacyKey = _EocBrMasterWorkingPrivacyKey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 7),
    _EocBrMasterWorkingPrivacyKey_Type()
)
eocBrMasterWorkingPrivacyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrMasterWorkingPrivacyKey.setStatus("current")


class _EocBrMasterSettingPrivacyKey_Type(Integer32):
    """Custom type eocBrMasterSettingPrivacyKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrMasterSettingPrivacyKey_Type.__name__ = "Integer32"
_EocBrMasterSettingPrivacyKey_Object = MibScalar
eocBrMasterSettingPrivacyKey = _EocBrMasterSettingPrivacyKey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 8),
    _EocBrMasterSettingPrivacyKey_Type()
)
eocBrMasterSettingPrivacyKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrMasterSettingPrivacyKey.setStatus("current")


class _EocBrMasterDrvWorkingVersion_Type(DisplayString):
    """Custom type eocBrMasterDrvWorkingVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrMasterDrvWorkingVersion_Type.__name__ = "DisplayString"
_EocBrMasterDrvWorkingVersion_Object = MibScalar
eocBrMasterDrvWorkingVersion = _EocBrMasterDrvWorkingVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 9),
    _EocBrMasterDrvWorkingVersion_Type()
)
eocBrMasterDrvWorkingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrMasterDrvWorkingVersion.setStatus("current")


class _EocBrMasterDrvUploadVersion_Type(DisplayString):
    """Custom type eocBrMasterDrvUploadVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrMasterDrvUploadVersion_Type.__name__ = "DisplayString"
_EocBrMasterDrvUploadVersion_Object = MibScalar
eocBrMasterDrvUploadVersion = _EocBrMasterDrvUploadVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 10),
    _EocBrMasterDrvUploadVersion_Type()
)
eocBrMasterDrvUploadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrMasterDrvUploadVersion.setStatus("current")


class _EocBrMasterDrvUpgradeAction_Type(Integer32):
    """Custom type eocBrMasterDrvUpgradeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrMasterDrvUpgradeAction_Type.__name__ = "Integer32"
_EocBrMasterDrvUpgradeAction_Object = MibScalar
eocBrMasterDrvUpgradeAction = _EocBrMasterDrvUpgradeAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 11),
    _EocBrMasterDrvUpgradeAction_Type()
)
eocBrMasterDrvUpgradeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrMasterDrvUpgradeAction.setStatus("current")


class _EocBrMasterDrvUpgradeStatus_Type(Integer32):
    """Custom type eocBrMasterDrvUpgradeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOrComplete", 0),
          ("inProgress", 1),
          ("failed", 2))
    )


_EocBrMasterDrvUpgradeStatus_Type.__name__ = "Integer32"
_EocBrMasterDrvUpgradeStatus_Object = MibScalar
eocBrMasterDrvUpgradeStatus = _EocBrMasterDrvUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 12),
    _EocBrMasterDrvUpgradeStatus_Type()
)
eocBrMasterDrvUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrMasterDrvUpgradeStatus.setStatus("current")


class _EocBrMasterScanEPAction_Type(Integer32):
    """Custom type eocBrMasterScanEPAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrMasterScanEPAction_Type.__name__ = "Integer32"
_EocBrMasterScanEPAction_Object = MibScalar
eocBrMasterScanEPAction = _EocBrMasterScanEPAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 13),
    _EocBrMasterScanEPAction_Type()
)
eocBrMasterScanEPAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrMasterScanEPAction.setStatus("current")


class _EocBrMasterScanEPStatus_Type(Integer32):
    """Custom type eocBrMasterScanEPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOrComplete", 0),
          ("inProgress", 1),
          ("failed", 2))
    )


_EocBrMasterScanEPStatus_Type.__name__ = "Integer32"
_EocBrMasterScanEPStatus_Object = MibScalar
eocBrMasterScanEPStatus = _EocBrMasterScanEPStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 14),
    _EocBrMasterScanEPStatus_Type()
)
eocBrMasterScanEPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrMasterScanEPStatus.setStatus("current")


class _EocBrMasterReboot_Type(Integer32):
    """Custom type eocBrMasterReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activateThenReboot", 1))
    )


_EocBrMasterReboot_Type.__name__ = "Integer32"
_EocBrMasterReboot_Object = MibScalar
eocBrMasterReboot = _EocBrMasterReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 7, 15),
    _EocBrMasterReboot_Type()
)
eocBrMasterReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrMasterReboot.setStatus("current")
_EocBrEPEoCGroup_ObjectIdentity = ObjectIdentity
eocBrEPEoCGroup = _EocBrEPEoCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8)
)
_EocBrEPTable_Object = MibTable
eocBrEPTable = _EocBrEPTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1)
)
if mibBuilder.loadTexts:
    eocBrEPTable.setStatus("current")
_EocBrEPEntry_Object = MibTableRow
eocBrEPEntry = _EocBrEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1)
)
eocBrEPEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPIndex"),
)
if mibBuilder.loadTexts:
    eocBrEPEntry.setStatus("current")
_EocBrEPIndex_Type = Integer32
_EocBrEPIndex_Object = MibTableColumn
eocBrEPIndex = _EocBrEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 1),
    _EocBrEPIndex_Type()
)
eocBrEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPIndex.setStatus("current")
_EocBrEPMac_Type = MacAddress
_EocBrEPMac_Object = MibTableColumn
eocBrEPMac = _EocBrEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 2),
    _EocBrEPMac_Type()
)
eocBrEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPMac.setStatus("current")


class _EocBrEPNote_Type(DisplayString):
    """Custom type eocBrEPNote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrEPNote_Type.__name__ = "DisplayString"
_EocBrEPNote_Object = MibTableColumn
eocBrEPNote = _EocBrEPNote_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 3),
    _EocBrEPNote_Type()
)
eocBrEPNote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPNote.setStatus("current")


class _EocBrEPModel_Type(Integer32):
    """Custom type eocBrEPModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4852
        )
    )
    namedValues = NamedValues(
        ("eOC350-TA", 4852)
    )


_EocBrEPModel_Type.__name__ = "Integer32"
_EocBrEPModel_Object = MibTableColumn
eocBrEPModel = _EocBrEPModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 4),
    _EocBrEPModel_Type()
)
eocBrEPModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPModel.setStatus("current")


class _EocBrEPProductName_Type(DisplayString):
    """Custom type eocBrEPProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrEPProductName_Type.__name__ = "DisplayString"
_EocBrEPProductName_Object = MibTableColumn
eocBrEPProductName = _EocBrEPProductName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 5),
    _EocBrEPProductName_Type()
)
eocBrEPProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPProductName.setStatus("current")


class _EocBrEPOnlineStatus_Type(Integer32):
    """Custom type eocBrEPOnlineStatus based on Integer32"""
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


_EocBrEPOnlineStatus_Type.__name__ = "Integer32"
_EocBrEPOnlineStatus_Object = MibTableColumn
eocBrEPOnlineStatus = _EocBrEPOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 6),
    _EocBrEPOnlineStatus_Type()
)
eocBrEPOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPOnlineStatus.setStatus("current")


class _EocBrEPHostCountLimit_Type(Integer32):
    """Custom type eocBrEPHostCountLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_EocBrEPHostCountLimit_Type.__name__ = "Integer32"
_EocBrEPHostCountLimit_Object = MibTableColumn
eocBrEPHostCountLimit = _EocBrEPHostCountLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 8),
    _EocBrEPHostCountLimit_Type()
)
eocBrEPHostCountLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPHostCountLimit.setStatus("current")


class _EocBrEPWorkingPrivacyKeyMatched_Type(Integer32):
    """Custom type eocBrEPWorkingPrivacyKeyMatched based on Integer32"""
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


_EocBrEPWorkingPrivacyKeyMatched_Type.__name__ = "Integer32"
_EocBrEPWorkingPrivacyKeyMatched_Object = MibTableColumn
eocBrEPWorkingPrivacyKeyMatched = _EocBrEPWorkingPrivacyKeyMatched_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 12),
    _EocBrEPWorkingPrivacyKeyMatched_Type()
)
eocBrEPWorkingPrivacyKeyMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPWorkingPrivacyKeyMatched.setStatus("current")


class _EocBrEPDrvWorkingVersion_Type(DisplayString):
    """Custom type eocBrEPDrvWorkingVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrEPDrvWorkingVersion_Type.__name__ = "DisplayString"
_EocBrEPDrvWorkingVersion_Object = MibTableColumn
eocBrEPDrvWorkingVersion = _EocBrEPDrvWorkingVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 13),
    _EocBrEPDrvWorkingVersion_Type()
)
eocBrEPDrvWorkingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPDrvWorkingVersion.setStatus("current")


class _EocBrEPDrvUploadVersion_Type(DisplayString):
    """Custom type eocBrEPDrvUploadVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocBrEPDrvUploadVersion_Type.__name__ = "DisplayString"
_EocBrEPDrvUploadVersion_Object = MibTableColumn
eocBrEPDrvUploadVersion = _EocBrEPDrvUploadVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 14),
    _EocBrEPDrvUploadVersion_Type()
)
eocBrEPDrvUploadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPDrvUploadVersion.setStatus("current")


class _EocBrEPDrvUpgradeAction_Type(Integer32):
    """Custom type eocBrEPDrvUpgradeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrEPDrvUpgradeAction_Type.__name__ = "Integer32"
_EocBrEPDrvUpgradeAction_Object = MibTableColumn
eocBrEPDrvUpgradeAction = _EocBrEPDrvUpgradeAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 15),
    _EocBrEPDrvUpgradeAction_Type()
)
eocBrEPDrvUpgradeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPDrvUpgradeAction.setStatus("current")


class _EocBrEPDrvUpgradeStatus_Type(Integer32):
    """Custom type eocBrEPDrvUpgradeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOrComplete", 0),
          ("inProgress", 1),
          ("failed", 2))
    )


_EocBrEPDrvUpgradeStatus_Type.__name__ = "Integer32"
_EocBrEPDrvUpgradeStatus_Object = MibTableColumn
eocBrEPDrvUpgradeStatus = _EocBrEPDrvUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 16),
    _EocBrEPDrvUpgradeStatus_Type()
)
eocBrEPDrvUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPDrvUpgradeStatus.setStatus("current")


class _EocBrEPPhyDiagAction_Type(Integer32):
    """Custom type eocBrEPPhyDiagAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrEPPhyDiagAction_Type.__name__ = "Integer32"
_EocBrEPPhyDiagAction_Object = MibTableColumn
eocBrEPPhyDiagAction = _EocBrEPPhyDiagAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 17),
    _EocBrEPPhyDiagAction_Type()
)
eocBrEPPhyDiagAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPPhyDiagAction.setStatus("current")


class _EocBrEPPhyDiagStatus_Type(Integer32):
    """Custom type eocBrEPPhyDiagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOrComplete", 0),
          ("inProgress", 1),
          ("failed", 2))
    )


_EocBrEPPhyDiagStatus_Type.__name__ = "Integer32"
_EocBrEPPhyDiagStatus_Object = MibTableColumn
eocBrEPPhyDiagStatus = _EocBrEPPhyDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 18),
    _EocBrEPPhyDiagStatus_Type()
)
eocBrEPPhyDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPhyDiagStatus.setStatus("current")


class _EocBrEPDiagDnLinkResult_Type(DisplayString):
    """Custom type eocBrEPDiagDnLinkResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EocBrEPDiagDnLinkResult_Type.__name__ = "DisplayString"
_EocBrEPDiagDnLinkResult_Object = MibTableColumn
eocBrEPDiagDnLinkResult = _EocBrEPDiagDnLinkResult_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 19),
    _EocBrEPDiagDnLinkResult_Type()
)
eocBrEPDiagDnLinkResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPDiagDnLinkResult.setStatus("current")


class _EocBrEPDiagUpLinkResult_Type(DisplayString):
    """Custom type eocBrEPDiagUpLinkResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EocBrEPDiagUpLinkResult_Type.__name__ = "DisplayString"
_EocBrEPDiagUpLinkResult_Object = MibTableColumn
eocBrEPDiagUpLinkResult = _EocBrEPDiagUpLinkResult_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 20),
    _EocBrEPDiagUpLinkResult_Type()
)
eocBrEPDiagUpLinkResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPDiagUpLinkResult.setStatus("current")


class _EocBrEPOnlineDiagAction_Type(Integer32):
    """Custom type eocBrEPOnlineDiagAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrEPOnlineDiagAction_Type.__name__ = "Integer32"
_EocBrEPOnlineDiagAction_Object = MibTableColumn
eocBrEPOnlineDiagAction = _EocBrEPOnlineDiagAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 21),
    _EocBrEPOnlineDiagAction_Type()
)
eocBrEPOnlineDiagAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPOnlineDiagAction.setStatus("current")


class _EocBrEPOnlineDiagStatus_Type(Integer32):
    """Custom type eocBrEPOnlineDiagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOrComplete", 0),
          ("inProgress", 1),
          ("failed", 2))
    )


_EocBrEPOnlineDiagStatus_Type.__name__ = "Integer32"
_EocBrEPOnlineDiagStatus_Object = MibTableColumn
eocBrEPOnlineDiagStatus = _EocBrEPOnlineDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 22),
    _EocBrEPOnlineDiagStatus_Type()
)
eocBrEPOnlineDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPOnlineDiagStatus.setStatus("current")


class _EocBrEPRowStatus_Type(Integer32):
    """Custom type eocBrEPRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_EocBrEPRowStatus_Type.__name__ = "Integer32"
_EocBrEPRowStatus_Object = MibTableColumn
eocBrEPRowStatus = _EocBrEPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 1, 1, 27),
    _EocBrEPRowStatus_Type()
)
eocBrEPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPRowStatus.setStatus("current")
_EocBrEPMacInfoTable_Object = MibTable
eocBrEPMacInfoTable = _EocBrEPMacInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 2)
)
if mibBuilder.loadTexts:
    eocBrEPMacInfoTable.setStatus("current")
_EocBrEPMacInfoEntry_Object = MibTableRow
eocBrEPMacInfoEntry = _EocBrEPMacInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 2, 1)
)
eocBrEPMacInfoEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEP-Index"),
)
if mibBuilder.loadTexts:
    eocBrEPMacInfoEntry.setStatus("current")
_EocBrEP_Index_Type = Integer32
_EocBrEP_Index_Object = MibTableColumn
eocBrEP_Index = _EocBrEP_Index_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 2, 1, 1),
    _EocBrEP_Index_Type()
)
eocBrEP_Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEP_Index.setStatus("current")


class _EocBrEP_MacType_Type(Integer32):
    """Custom type eocBrEP_MacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ep", 0),
          ("master", 1),
          ("host", 2))
    )


_EocBrEP_MacType_Type.__name__ = "Integer32"
_EocBrEP_MacType_Object = MibTableColumn
eocBrEP_MacType = _EocBrEP_MacType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 2, 1, 2),
    _EocBrEP_MacType_Type()
)
eocBrEP_MacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEP_MacType.setStatus("current")
_EocBrEP_EPMac_Type = MacAddress
_EocBrEP_EPMac_Object = MibTableColumn
eocBrEP_EPMac = _EocBrEP_EPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 2, 1, 3),
    _EocBrEP_EPMac_Type()
)
eocBrEP_EPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEP_EPMac.setStatus("current")
_EocBrEP_HostMac_Type = MacAddress
_EocBrEP_HostMac_Object = MibTableColumn
eocBrEP_HostMac = _EocBrEP_HostMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 2, 1, 4),
    _EocBrEP_HostMac_Type()
)
eocBrEP_HostMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEP_HostMac.setStatus("current")
_EocBrEPNetPerTable_Object = MibTable
eocBrEPNetPerTable = _EocBrEPNetPerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 3)
)
if mibBuilder.loadTexts:
    eocBrEPNetPerTable.setStatus("current")
_EocBrEPNetPerEntry_Object = MibTableRow
eocBrEPNetPerEntry = _EocBrEPNetPerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 3, 1)
)
eocBrEPNetPerEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPNetPerIndex"),
)
if mibBuilder.loadTexts:
    eocBrEPNetPerEntry.setStatus("current")
_EocBrEPNetPerIndex_Type = Integer32
_EocBrEPNetPerIndex_Object = MibTableColumn
eocBrEPNetPerIndex = _EocBrEPNetPerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 3, 1, 1),
    _EocBrEPNetPerIndex_Type()
)
eocBrEPNetPerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPNetPerIndex.setStatus("current")
_EocBrEPNetPerEPMac_Type = MacAddress
_EocBrEPNetPerEPMac_Object = MibTableColumn
eocBrEPNetPerEPMac = _EocBrEPNetPerEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 3, 1, 2),
    _EocBrEPNetPerEPMac_Type()
)
eocBrEPNetPerEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPNetPerEPMac.setStatus("current")
_EocBrEPNetPerDnLinkSNR_Type = Integer32
_EocBrEPNetPerDnLinkSNR_Object = MibTableColumn
eocBrEPNetPerDnLinkSNR = _EocBrEPNetPerDnLinkSNR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 3, 1, 3),
    _EocBrEPNetPerDnLinkSNR_Type()
)
eocBrEPNetPerDnLinkSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPNetPerDnLinkSNR.setStatus("current")
_EocBrEPNetPerUpLinkSNR_Type = Integer32
_EocBrEPNetPerUpLinkSNR_Object = MibTableColumn
eocBrEPNetPerUpLinkSNR = _EocBrEPNetPerUpLinkSNR_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 3, 1, 4),
    _EocBrEPNetPerUpLinkSNR_Type()
)
eocBrEPNetPerUpLinkSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPNetPerUpLinkSNR.setStatus("current")
_EocBrEPNetPerDnLinkRate_Type = Integer32
_EocBrEPNetPerDnLinkRate_Object = MibTableColumn
eocBrEPNetPerDnLinkRate = _EocBrEPNetPerDnLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 3, 1, 5),
    _EocBrEPNetPerDnLinkRate_Type()
)
eocBrEPNetPerDnLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPNetPerDnLinkRate.setStatus("current")
_EocBrEPNetPerUpLinkRate_Type = Integer32
_EocBrEPNetPerUpLinkRate_Object = MibTableColumn
eocBrEPNetPerUpLinkRate = _EocBrEPNetPerUpLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 3, 1, 6),
    _EocBrEPNetPerUpLinkRate_Type()
)
eocBrEPNetPerUpLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPNetPerUpLinkRate.setStatus("current")


class _EocBrEPNetPerDnLinkRxPwr_Type(Integer32):
    """Custom type eocBrEPNetPerDnLinkRxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_EocBrEPNetPerDnLinkRxPwr_Type.__name__ = "Integer32"
_EocBrEPNetPerDnLinkRxPwr_Object = MibTableColumn
eocBrEPNetPerDnLinkRxPwr = _EocBrEPNetPerDnLinkRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 3, 1, 7),
    _EocBrEPNetPerDnLinkRxPwr_Type()
)
eocBrEPNetPerDnLinkRxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPNetPerDnLinkRxPwr.setStatus("current")


class _EocBrEPNetPerUpLinkRxPwr_Type(Integer32):
    """Custom type eocBrEPNetPerUpLinkRxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_EocBrEPNetPerUpLinkRxPwr_Type.__name__ = "Integer32"
_EocBrEPNetPerUpLinkRxPwr_Object = MibTableColumn
eocBrEPNetPerUpLinkRxPwr = _EocBrEPNetPerUpLinkRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 3, 1, 8),
    _EocBrEPNetPerUpLinkRxPwr_Type()
)
eocBrEPNetPerUpLinkRxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPNetPerUpLinkRxPwr.setStatus("current")
_EocBrEPScanMacInfo_ObjectIdentity = ObjectIdentity
eocBrEPScanMacInfo = _EocBrEPScanMacInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 4)
)


class _EocBrEPScanMacInfoAction_Type(Integer32):
    """Custom type eocBrEPScanMacInfoAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrEPScanMacInfoAction_Type.__name__ = "Integer32"
_EocBrEPScanMacInfoAction_Object = MibScalar
eocBrEPScanMacInfoAction = _EocBrEPScanMacInfoAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 4, 1),
    _EocBrEPScanMacInfoAction_Type()
)
eocBrEPScanMacInfoAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPScanMacInfoAction.setStatus("current")


class _EocBrEPScanMacInfoStatus_Type(Integer32):
    """Custom type eocBrEPScanMacInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOrComplete", 0),
          ("inProgress", 1),
          ("failed", 2))
    )


_EocBrEPScanMacInfoStatus_Type.__name__ = "Integer32"
_EocBrEPScanMacInfoStatus_Object = MibScalar
eocBrEPScanMacInfoStatus = _EocBrEPScanMacInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 4, 2),
    _EocBrEPScanMacInfoStatus_Type()
)
eocBrEPScanMacInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPScanMacInfoStatus.setStatus("current")
_EocBrEPPayloadEncodeTable_Object = MibTable
eocBrEPPayloadEncodeTable = _EocBrEPPayloadEncodeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 5)
)
if mibBuilder.loadTexts:
    eocBrEPPayloadEncodeTable.setStatus("current")
_EocBrEPPayloadEncodeEntry_Object = MibTableRow
eocBrEPPayloadEncodeEntry = _EocBrEPPayloadEncodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 5, 1)
)
eocBrEPPayloadEncodeEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPPayloadEncodeIndex"),
)
if mibBuilder.loadTexts:
    eocBrEPPayloadEncodeEntry.setStatus("current")
_EocBrEPPayloadEncodeIndex_Type = Integer32
_EocBrEPPayloadEncodeIndex_Object = MibTableColumn
eocBrEPPayloadEncodeIndex = _EocBrEPPayloadEncodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 5, 1, 1),
    _EocBrEPPayloadEncodeIndex_Type()
)
eocBrEPPayloadEncodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPayloadEncodeIndex.setStatus("current")
_EocBrEPPayloadEncodeEPMac_Type = MacAddress
_EocBrEPPayloadEncodeEPMac_Object = MibTableColumn
eocBrEPPayloadEncodeEPMac = _EocBrEPPayloadEncodeEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 5, 1, 2),
    _EocBrEPPayloadEncodeEPMac_Type()
)
eocBrEPPayloadEncodeEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPayloadEncodeEPMac.setStatus("current")
_EocBrEPPayloadEncodeDnRate_Type = Integer32
_EocBrEPPayloadEncodeDnRate_Object = MibTableColumn
eocBrEPPayloadEncodeDnRate = _EocBrEPPayloadEncodeDnRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 5, 1, 3),
    _EocBrEPPayloadEncodeDnRate_Type()
)
eocBrEPPayloadEncodeDnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPayloadEncodeDnRate.setStatus("current")
_EocBrEPPayloadEncodeUpRate_Type = Integer32
_EocBrEPPayloadEncodeUpRate_Object = MibTableColumn
eocBrEPPayloadEncodeUpRate = _EocBrEPPayloadEncodeUpRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 8, 5, 1, 4),
    _EocBrEPPayloadEncodeUpRate_Type()
)
eocBrEPPayloadEncodeUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPayloadEncodeUpRate.setStatus("current")
_EocBrTFTPGroup_ObjectIdentity = ObjectIdentity
eocBrTFTPGroup = _EocBrTFTPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 9)
)
_EocBrTFTPServerIPAddress_Type = IpAddress
_EocBrTFTPServerIPAddress_Object = MibScalar
eocBrTFTPServerIPAddress = _EocBrTFTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 9, 1),
    _EocBrTFTPServerIPAddress_Type()
)
eocBrTFTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTFTPServerIPAddress.setStatus("current")


class _EocBrTFTPFilename_Type(DisplayString):
    """Custom type eocBrTFTPFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrTFTPFilename_Type.__name__ = "DisplayString"
_EocBrTFTPFilename_Object = MibScalar
eocBrTFTPFilename = _EocBrTFTPFilename_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 9, 2),
    _EocBrTFTPFilename_Type()
)
eocBrTFTPFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTFTPFilename.setStatus("current")


class _EocBrTFTPGetAction_Type(Integer32):
    """Custom type eocBrTFTPGetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrTFTPGetAction_Type.__name__ = "Integer32"
_EocBrTFTPGetAction_Object = MibScalar
eocBrTFTPGetAction = _EocBrTFTPGetAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 9, 3),
    _EocBrTFTPGetAction_Type()
)
eocBrTFTPGetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTFTPGetAction.setStatus("current")


class _EocBrTFTPGetStatus_Type(Integer32):
    """Custom type eocBrTFTPGetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOrComplete", 0),
          ("inProgress", 1),
          ("failed", 2))
    )


_EocBrTFTPGetStatus_Type.__name__ = "Integer32"
_EocBrTFTPGetStatus_Object = MibScalar
eocBrTFTPGetStatus = _EocBrTFTPGetStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 9, 4),
    _EocBrTFTPGetStatus_Type()
)
eocBrTFTPGetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrTFTPGetStatus.setStatus("current")


class _EocBrTFTPExtensionPath_Type(DisplayString):
    """Custom type eocBrTFTPExtensionPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EocBrTFTPExtensionPath_Type.__name__ = "DisplayString"
_EocBrTFTPExtensionPath_Object = MibScalar
eocBrTFTPExtensionPath = _EocBrTFTPExtensionPath_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 9, 5),
    _EocBrTFTPExtensionPath_Type()
)
eocBrTFTPExtensionPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTFTPExtensionPath.setStatus("current")


class _EocBrTFTPServer_Type(DisplayString):
    """Custom type eocBrTFTPServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EocBrTFTPServer_Type.__name__ = "DisplayString"
_EocBrTFTPServer_Object = MibScalar
eocBrTFTPServer = _EocBrTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 9, 6),
    _EocBrTFTPServer_Type()
)
eocBrTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTFTPServer.setStatus("current")
_EocBrEtherGroup_ObjectIdentity = ObjectIdentity
eocBrEtherGroup = _EocBrEtherGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10)
)
_EocBrEtherPort_ObjectIdentity = ObjectIdentity
eocBrEtherPort = _EocBrEtherPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1)
)
_EocBrPortPropTable_Object = MibTable
eocBrPortPropTable = _EocBrPortPropTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    eocBrPortPropTable.setStatus("current")
_EocBrPortPropEntry_Object = MibTableRow
eocBrPortPropEntry = _EocBrPortPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 1, 1)
)
eocBrPortPropEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrPortPropPID"),
)
if mibBuilder.loadTexts:
    eocBrPortPropEntry.setStatus("current")
_EocBrPortPropPID_Type = Integer32
_EocBrPortPropPID_Object = MibTableColumn
eocBrPortPropPID = _EocBrPortPropPID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 1, 1, 1),
    _EocBrPortPropPID_Type()
)
eocBrPortPropPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortPropPID.setStatus("current")


class _EocBrPortPropType_Type(Integer32):
    """Custom type eocBrPortPropType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("coax", 1),
          ("phoneLine", 2))
    )


_EocBrPortPropType_Type.__name__ = "Integer32"
_EocBrPortPropType_Object = MibTableColumn
eocBrPortPropType = _EocBrPortPropType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 1, 1, 2),
    _EocBrPortPropType_Type()
)
eocBrPortPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortPropType.setStatus("current")


class _EocBrPortPropConfig_Type(Integer32):
    """Custom type eocBrPortPropConfig based on Integer32"""
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
        *(("autoNegotiation", 0),
          ("fullDuplex100Mbps", 1),
          ("halfDuplex100Mbps", 2),
          ("fullDuplex10Mbps", 3),
          ("halfDuplex10Mbps", 4))
    )


_EocBrPortPropConfig_Type.__name__ = "Integer32"
_EocBrPortPropConfig_Object = MibTableColumn
eocBrPortPropConfig = _EocBrPortPropConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 1, 1, 3),
    _EocBrPortPropConfig_Type()
)
eocBrPortPropConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrPortPropConfig.setStatus("current")


class _EocBrPortPropLinkStatus_Type(Integer32):
    """Custom type eocBrPortPropLinkStatus based on Integer32"""
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
        *(("off", 0),
          ("fullDuplex100Mbps", 1),
          ("halfDuplex100Mbps", 2),
          ("fullDuplex10Mbps", 3),
          ("halfDuplex10Mbps", 4),
          ("fullDuplex1000Mbps", 5))
    )


_EocBrPortPropLinkStatus_Type.__name__ = "Integer32"
_EocBrPortPropLinkStatus_Object = MibTableColumn
eocBrPortPropLinkStatus = _EocBrPortPropLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 1, 1, 4),
    _EocBrPortPropLinkStatus_Type()
)
eocBrPortPropLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortPropLinkStatus.setStatus("current")


class _EocBrPortPropInRateCtrl_Type(Integer32):
    """Custom type eocBrPortPropInRateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrPortPropInRateCtrl_Type.__name__ = "Integer32"
_EocBrPortPropInRateCtrl_Object = MibTableColumn
eocBrPortPropInRateCtrl = _EocBrPortPropInRateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 1, 1, 6),
    _EocBrPortPropInRateCtrl_Type()
)
eocBrPortPropInRateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrPortPropInRateCtrl.setStatus("current")


class _EocBrPortPropInRate_Type(Integer32):
    """Custom type eocBrPortPropInRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3125),
    )


_EocBrPortPropInRate_Type.__name__ = "Integer32"
_EocBrPortPropInRate_Object = MibTableColumn
eocBrPortPropInRate = _EocBrPortPropInRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 1, 1, 7),
    _EocBrPortPropInRate_Type()
)
eocBrPortPropInRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrPortPropInRate.setStatus("current")


class _EocBrPortPropOutRateCtrl_Type(Integer32):
    """Custom type eocBrPortPropOutRateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrPortPropOutRateCtrl_Type.__name__ = "Integer32"
_EocBrPortPropOutRateCtrl_Object = MibTableColumn
eocBrPortPropOutRateCtrl = _EocBrPortPropOutRateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 1, 1, 8),
    _EocBrPortPropOutRateCtrl_Type()
)
eocBrPortPropOutRateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrPortPropOutRateCtrl.setStatus("current")


class _EocBrPortPropOutRate_Type(Integer32):
    """Custom type eocBrPortPropOutRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3125),
    )


_EocBrPortPropOutRate_Type.__name__ = "Integer32"
_EocBrPortPropOutRate_Object = MibTableColumn
eocBrPortPropOutRate = _EocBrPortPropOutRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 1, 1, 9),
    _EocBrPortPropOutRate_Type()
)
eocBrPortPropOutRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrPortPropOutRate.setStatus("current")
_EocBrPortStatsTable_Object = MibTable
eocBrPortStatsTable = _EocBrPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 2)
)
if mibBuilder.loadTexts:
    eocBrPortStatsTable.setStatus("current")
_EocBrPortStatsEntry_Object = MibTableRow
eocBrPortStatsEntry = _EocBrPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 2, 1)
)
eocBrPortStatsEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrPortStatsPID"),
)
if mibBuilder.loadTexts:
    eocBrPortStatsEntry.setStatus("current")
_EocBrPortStatsPID_Type = Integer32
_EocBrPortStatsPID_Object = MibTableColumn
eocBrPortStatsPID = _EocBrPortStatsPID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 2, 1, 1),
    _EocBrPortStatsPID_Type()
)
eocBrPortStatsPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortStatsPID.setStatus("current")


class _EocBrPortStatsType_Type(Integer32):
    """Custom type eocBrPortStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("coax", 1),
          ("phoneLine", 2))
    )


_EocBrPortStatsType_Type.__name__ = "Integer32"
_EocBrPortStatsType_Object = MibTableColumn
eocBrPortStatsType = _EocBrPortStatsType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 2, 1, 2),
    _EocBrPortStatsType_Type()
)
eocBrPortStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortStatsType.setStatus("current")
_EocBrPortStatsRxPkts_Type = Counter64
_EocBrPortStatsRxPkts_Object = MibTableColumn
eocBrPortStatsRxPkts = _EocBrPortStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 2, 1, 3),
    _EocBrPortStatsRxPkts_Type()
)
eocBrPortStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortStatsRxPkts.setStatus("current")
_EocBrPortStatsRxBytes_Type = Counter64
_EocBrPortStatsRxBytes_Object = MibTableColumn
eocBrPortStatsRxBytes = _EocBrPortStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 2, 1, 4),
    _EocBrPortStatsRxBytes_Type()
)
eocBrPortStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortStatsRxBytes.setStatus("current")
_EocBrPortStatsTxPkts_Type = Counter64
_EocBrPortStatsTxPkts_Object = MibTableColumn
eocBrPortStatsTxPkts = _EocBrPortStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 2, 1, 5),
    _EocBrPortStatsTxPkts_Type()
)
eocBrPortStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortStatsTxPkts.setStatus("current")
_EocBrPortStatsTxBytes_Type = Counter64
_EocBrPortStatsTxBytes_Object = MibTableColumn
eocBrPortStatsTxBytes = _EocBrPortStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 2, 1, 6),
    _EocBrPortStatsTxBytes_Type()
)
eocBrPortStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortStatsTxBytes.setStatus("current")
_EocBrPortStatsCollisions_Type = Counter64
_EocBrPortStatsCollisions_Object = MibTableColumn
eocBrPortStatsCollisions = _EocBrPortStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 2, 1, 7),
    _EocBrPortStatsCollisions_Type()
)
eocBrPortStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortStatsCollisions.setStatus("current")
_EocBrPortStatsErrors_Type = Counter64
_EocBrPortStatsErrors_Object = MibTableColumn
eocBrPortStatsErrors = _EocBrPortStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 2, 1, 8),
    _EocBrPortStatsErrors_Type()
)
eocBrPortStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrPortStatsErrors.setStatus("current")
_EocBrStatsCtrl_ObjectIdentity = ObjectIdentity
eocBrStatsCtrl = _EocBrStatsCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 3)
)


class _EocBrStatsCtrlReset_Type(Integer32):
    """Custom type eocBrStatsCtrlReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrStatsCtrlReset_Type.__name__ = "Integer32"
_EocBrStatsCtrlReset_Object = MibScalar
eocBrStatsCtrlReset = _EocBrStatsCtrlReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 3, 1),
    _EocBrStatsCtrlReset_Type()
)
eocBrStatsCtrlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrStatsCtrlReset.setStatus("current")


class _EocBrStatsCtrlRefresh_Type(Integer32):
    """Custom type eocBrStatsCtrlRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrStatsCtrlRefresh_Type.__name__ = "Integer32"
_EocBrStatsCtrlRefresh_Object = MibScalar
eocBrStatsCtrlRefresh = _EocBrStatsCtrlRefresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 1, 3, 2),
    _EocBrStatsCtrlRefresh_Type()
)
eocBrStatsCtrlRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrStatsCtrlRefresh.setStatus("current")
_EocBrEtherQoS_ObjectIdentity = ObjectIdentity
eocBrEtherQoS = _EocBrEtherQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 2)
)
_EocBrTcpUdpPriTable_Object = MibTable
eocBrTcpUdpPriTable = _EocBrTcpUdpPriTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    eocBrTcpUdpPriTable.setStatus("current")
_EocBrTcpUdpPriEntry_Object = MibTableRow
eocBrTcpUdpPriEntry = _EocBrTcpUdpPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 2, 2, 1)
)
eocBrTcpUdpPriEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrTcpUdpRuleNum"),
)
if mibBuilder.loadTexts:
    eocBrTcpUdpPriEntry.setStatus("current")
_EocBrTcpUdpRuleNum_Type = Integer32
_EocBrTcpUdpRuleNum_Object = MibTableColumn
eocBrTcpUdpRuleNum = _EocBrTcpUdpRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 2, 2, 1, 1),
    _EocBrTcpUdpRuleNum_Type()
)
eocBrTcpUdpRuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrTcpUdpRuleNum.setStatus("current")


class _EocBrTcpUdpEnableCtrl_Type(Integer32):
    """Custom type eocBrTcpUdpEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrTcpUdpEnableCtrl_Type.__name__ = "Integer32"
_EocBrTcpUdpEnableCtrl_Object = MibTableColumn
eocBrTcpUdpEnableCtrl = _EocBrTcpUdpEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 2, 2, 1, 2),
    _EocBrTcpUdpEnableCtrl_Type()
)
eocBrTcpUdpEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTcpUdpEnableCtrl.setStatus("current")


class _EocBrTcpUdpPortNum_Type(Integer32):
    """Custom type eocBrTcpUdpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrTcpUdpPortNum_Type.__name__ = "Integer32"
_EocBrTcpUdpPortNum_Object = MibTableColumn
eocBrTcpUdpPortNum = _EocBrTcpUdpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 2, 2, 1, 3),
    _EocBrTcpUdpPortNum_Type()
)
eocBrTcpUdpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTcpUdpPortNum.setStatus("current")


class _EocBrTcpUdpMappedQueue_Type(Integer32):
    """Custom type eocBrTcpUdpMappedQueue based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3))
    )


_EocBrTcpUdpMappedQueue_Type.__name__ = "Integer32"
_EocBrTcpUdpMappedQueue_Object = MibTableColumn
eocBrTcpUdpMappedQueue = _EocBrTcpUdpMappedQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 2, 2, 1, 4),
    _EocBrTcpUdpMappedQueue_Type()
)
eocBrTcpUdpMappedQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTcpUdpMappedQueue.setStatus("current")


class _EocBrQueueSchType_Type(Integer32):
    """Custom type eocBrQueueSchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 0),
          ("wfq", 1),
          ("mix", 2))
    )


_EocBrQueueSchType_Type.__name__ = "Integer32"
_EocBrQueueSchType_Object = MibScalar
eocBrQueueSchType = _EocBrQueueSchType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 2, 3),
    _EocBrQueueSchType_Type()
)
eocBrQueueSchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrQueueSchType.setStatus("current")


class _EocBrPriSchemeSelect_Type(Integer32):
    """Custom type eocBrPriSchemeSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("use8021p", 0),
          ("useIP", 1))
    )


_EocBrPriSchemeSelect_Type.__name__ = "Integer32"
_EocBrPriSchemeSelect_Object = MibScalar
eocBrPriSchemeSelect = _EocBrPriSchemeSelect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 2, 4),
    _EocBrPriSchemeSelect_Type()
)
eocBrPriSchemeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrPriSchemeSelect.setStatus("current")
_EocBrEtherIGMPSnoop_ObjectIdentity = ObjectIdentity
eocBrEtherIGMPSnoop = _EocBrEtherIGMPSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 3)
)


class _EocBrIGMPSnoopEnableCtrl_Type(Integer32):
    """Custom type eocBrIGMPSnoopEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrIGMPSnoopEnableCtrl_Type.__name__ = "Integer32"
_EocBrIGMPSnoopEnableCtrl_Object = MibScalar
eocBrIGMPSnoopEnableCtrl = _EocBrIGMPSnoopEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 3, 1),
    _EocBrIGMPSnoopEnableCtrl_Type()
)
eocBrIGMPSnoopEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrIGMPSnoopEnableCtrl.setStatus("current")
_EocBrEtherTagVLAN_ObjectIdentity = ObjectIdentity
eocBrEtherTagVLAN = _EocBrEtherTagVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 4)
)


class _EocBrTagVLANEnableCtrl_Type(Integer32):
    """Custom type eocBrTagVLANEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrTagVLANEnableCtrl_Type.__name__ = "Integer32"
_EocBrTagVLANEnableCtrl_Object = MibScalar
eocBrTagVLANEnableCtrl = _EocBrTagVLANEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 4, 1),
    _EocBrTagVLANEnableCtrl_Type()
)
eocBrTagVLANEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTagVLANEnableCtrl.setStatus("current")
_EocBrTagPortTable_Object = MibTable
eocBrTagPortTable = _EocBrTagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 4, 2)
)
if mibBuilder.loadTexts:
    eocBrTagPortTable.setStatus("current")
_EocBrTagPortEntry_Object = MibTableRow
eocBrTagPortEntry = _EocBrTagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 4, 2, 1)
)
eocBrTagPortEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrTagPortPID"),
)
if mibBuilder.loadTexts:
    eocBrTagPortEntry.setStatus("current")
_EocBrTagPortPID_Type = Integer32
_EocBrTagPortPID_Object = MibTableColumn
eocBrTagPortPID = _EocBrTagPortPID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 4, 2, 1, 1),
    _EocBrTagPortPID_Type()
)
eocBrTagPortPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrTagPortPID.setStatus("current")


class _EocBrTagPortType_Type(Integer32):
    """Custom type eocBrTagPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("coax", 1),
          ("phoneLine", 2))
    )


_EocBrTagPortType_Type.__name__ = "Integer32"
_EocBrTagPortType_Object = MibTableColumn
eocBrTagPortType = _EocBrTagPortType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 4, 2, 1, 2),
    _EocBrTagPortType_Type()
)
eocBrTagPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrTagPortType.setStatus("current")


class _EocBrTagPortPriority_Type(Integer32):
    """Custom type eocBrTagPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EocBrTagPortPriority_Type.__name__ = "Integer32"
_EocBrTagPortPriority_Object = MibTableColumn
eocBrTagPortPriority = _EocBrTagPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 4, 2, 1, 3),
    _EocBrTagPortPriority_Type()
)
eocBrTagPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTagPortPriority.setStatus("current")


class _EocBrTagPortVID_Type(Integer32):
    """Custom type eocBrTagPortVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_EocBrTagPortVID_Type.__name__ = "Integer32"
_EocBrTagPortVID_Object = MibTableColumn
eocBrTagPortVID = _EocBrTagPortVID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 4, 2, 1, 4),
    _EocBrTagPortVID_Type()
)
eocBrTagPortVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTagPortVID.setStatus("current")


class _EocBrTagPortInRule_Type(Integer32):
    """Custom type eocBrTagPortInRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("tag", 1))
    )


_EocBrTagPortInRule_Type.__name__ = "Integer32"
_EocBrTagPortInRule_Object = MibTableColumn
eocBrTagPortInRule = _EocBrTagPortInRule_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 4, 2, 1, 5),
    _EocBrTagPortInRule_Type()
)
eocBrTagPortInRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTagPortInRule.setStatus("current")


class _EocBrTagPortOutRule_Type(Integer32):
    """Custom type eocBrTagPortOutRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untag", 0),
          ("tag", 1),
          ("bypass", 2))
    )


_EocBrTagPortOutRule_Type.__name__ = "Integer32"
_EocBrTagPortOutRule_Object = MibTableColumn
eocBrTagPortOutRule = _EocBrTagPortOutRule_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 4, 2, 1, 6),
    _EocBrTagPortOutRule_Type()
)
eocBrTagPortOutRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrTagPortOutRule.setStatus("current")
_EocBrEtherCascadeLan_ObjectIdentity = ObjectIdentity
eocBrEtherCascadeLan = _EocBrEtherCascadeLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 5)
)


class _EocBrCascadeMode_Type(Integer32):
    """Custom type eocBrCascadeMode based on Integer32"""
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
        *(("disable", 0),
          ("downLinkLAN1-upLinkLAN2", 1),
          ("downLinkLAN2-upLinkLAN1", 2),
          ("autoBySTP", 3))
    )


_EocBrCascadeMode_Type.__name__ = "Integer32"
_EocBrCascadeMode_Object = MibScalar
eocBrCascadeMode = _EocBrCascadeMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 10, 5, 1),
    _EocBrCascadeMode_Type()
)
eocBrCascadeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrCascadeMode.setStatus("current")
_EocBrEPEtherGroup_ObjectIdentity = ObjectIdentity
eocBrEPEtherGroup = _EocBrEPEtherGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11)
)
_EocBrEPDesignate_ObjectIdentity = ObjectIdentity
eocBrEPDesignate = _EocBrEPDesignate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 1)
)
_EocBrEPDesignateTable_Object = MibTable
eocBrEPDesignateTable = _EocBrEPDesignateTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    eocBrEPDesignateTable.setStatus("current")
_EocBrEPDesignateEntry_Object = MibTableRow
eocBrEPDesignateEntry = _EocBrEPDesignateEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 1, 1, 1)
)
eocBrEPDesignateEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPDesignateEPIndex"),
)
if mibBuilder.loadTexts:
    eocBrEPDesignateEntry.setStatus("current")
_EocBrEPDesignateEPIndex_Type = Integer32
_EocBrEPDesignateEPIndex_Object = MibTableColumn
eocBrEPDesignateEPIndex = _EocBrEPDesignateEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 1, 1, 1, 1),
    _EocBrEPDesignateEPIndex_Type()
)
eocBrEPDesignateEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPDesignateEPIndex.setStatus("current")
_EocBrEPDesignateEPMac_Type = MacAddress
_EocBrEPDesignateEPMac_Object = MibTableColumn
eocBrEPDesignateEPMac = _EocBrEPDesignateEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 1, 1, 1, 2),
    _EocBrEPDesignateEPMac_Type()
)
eocBrEPDesignateEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPDesignateEPMac.setStatus("current")


class _EocBrEPDesignateOnlineStatus_Type(Integer32):
    """Custom type eocBrEPDesignateOnlineStatus based on Integer32"""
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


_EocBrEPDesignateOnlineStatus_Type.__name__ = "Integer32"
_EocBrEPDesignateOnlineStatus_Object = MibTableColumn
eocBrEPDesignateOnlineStatus = _EocBrEPDesignateOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 1, 1, 1, 3),
    _EocBrEPDesignateOnlineStatus_Type()
)
eocBrEPDesignateOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPDesignateOnlineStatus.setStatus("current")


class _EocBrEPDesignateDeviceVersion_Type(Integer32):
    """Custom type eocBrEPDesignateDeviceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrEPDesignateDeviceVersion_Type.__name__ = "Integer32"
_EocBrEPDesignateDeviceVersion_Object = MibTableColumn
eocBrEPDesignateDeviceVersion = _EocBrEPDesignateDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 1, 1, 1, 4),
    _EocBrEPDesignateDeviceVersion_Type()
)
eocBrEPDesignateDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPDesignateDeviceVersion.setStatus("current")


class _EocBrEPDesignateIsSmart_Type(Integer32):
    """Custom type eocBrEPDesignateIsSmart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1),
          ("unknown", 255))
    )


_EocBrEPDesignateIsSmart_Type.__name__ = "Integer32"
_EocBrEPDesignateIsSmart_Object = MibTableColumn
eocBrEPDesignateIsSmart = _EocBrEPDesignateIsSmart_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 1, 1, 1, 6),
    _EocBrEPDesignateIsSmart_Type()
)
eocBrEPDesignateIsSmart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPDesignateIsSmart.setStatus("current")


class _EocBrEPDesignateIsTarget_Type(Integer32):
    """Custom type eocBrEPDesignateIsTarget based on Integer32"""
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


_EocBrEPDesignateIsTarget_Type.__name__ = "Integer32"
_EocBrEPDesignateIsTarget_Object = MibTableColumn
eocBrEPDesignateIsTarget = _EocBrEPDesignateIsTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 1, 1, 1, 7),
    _EocBrEPDesignateIsTarget_Type()
)
eocBrEPDesignateIsTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPDesignateIsTarget.setStatus("current")
_EocBrEPEtherPort_ObjectIdentity = ObjectIdentity
eocBrEPEtherPort = _EocBrEPEtherPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2)
)
_EocBrEPPortPropTable_Object = MibTable
eocBrEPPortPropTable = _EocBrEPPortPropTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    eocBrEPPortPropTable.setStatus("current")
_EocBrEPPortPropEntry_Object = MibTableRow
eocBrEPPortPropEntry = _EocBrEPPortPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1)
)
eocBrEPPortPropEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPPortPropEPIndex"),
    (0, "ZYXEL-ES-EOC350", "eocBrEPPortPropPID"),
)
if mibBuilder.loadTexts:
    eocBrEPPortPropEntry.setStatus("current")
_EocBrEPPortPropEPIndex_Type = Integer32
_EocBrEPPortPropEPIndex_Object = MibTableColumn
eocBrEPPortPropEPIndex = _EocBrEPPortPropEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 1),
    _EocBrEPPortPropEPIndex_Type()
)
eocBrEPPortPropEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortPropEPIndex.setStatus("current")
_EocBrEPPortPropPID_Type = Integer32
_EocBrEPPortPropPID_Object = MibTableColumn
eocBrEPPortPropPID = _EocBrEPPortPropPID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 2),
    _EocBrEPPortPropPID_Type()
)
eocBrEPPortPropPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortPropPID.setStatus("current")
_EocBrEPPortPropEPMac_Type = MacAddress
_EocBrEPPortPropEPMac_Object = MibTableColumn
eocBrEPPortPropEPMac = _EocBrEPPortPropEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 3),
    _EocBrEPPortPropEPMac_Type()
)
eocBrEPPortPropEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortPropEPMac.setStatus("current")


class _EocBrEPPortPropType_Type(Integer32):
    """Custom type eocBrEPPortPropType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("coax", 1),
          ("phoneLine", 2))
    )


_EocBrEPPortPropType_Type.__name__ = "Integer32"
_EocBrEPPortPropType_Object = MibTableColumn
eocBrEPPortPropType = _EocBrEPPortPropType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 4),
    _EocBrEPPortPropType_Type()
)
eocBrEPPortPropType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortPropType.setStatus("current")


class _EocBrEPPortPropConfig_Type(Integer32):
    """Custom type eocBrEPPortPropConfig based on Integer32"""
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
        *(("autoNegotiation", 0),
          ("fullDuplex100Mbps", 1),
          ("halfDuplex100Mbps", 2),
          ("fullDuplex10Mbps", 3),
          ("halfDuplex10Mbps", 4))
    )


_EocBrEPPortPropConfig_Type.__name__ = "Integer32"
_EocBrEPPortPropConfig_Object = MibTableColumn
eocBrEPPortPropConfig = _EocBrEPPortPropConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 5),
    _EocBrEPPortPropConfig_Type()
)
eocBrEPPortPropConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPPortPropConfig.setStatus("current")


class _EocBrEPPortPropLinkStatus_Type(Integer32):
    """Custom type eocBrEPPortPropLinkStatus based on Integer32"""
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
        *(("off", 0),
          ("fullDuplex100Mbps", 1),
          ("halfDuplex100Mbps", 2),
          ("fullDuplex10Mbps", 3),
          ("halfDuplex10Mbps", 4))
    )


_EocBrEPPortPropLinkStatus_Type.__name__ = "Integer32"
_EocBrEPPortPropLinkStatus_Object = MibTableColumn
eocBrEPPortPropLinkStatus = _EocBrEPPortPropLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 6),
    _EocBrEPPortPropLinkStatus_Type()
)
eocBrEPPortPropLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortPropLinkStatus.setStatus("current")


class _EocBrEPPortPropFlowCtrl_Type(Integer32):
    """Custom type eocBrEPPortPropFlowCtrl based on Integer32"""
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


_EocBrEPPortPropFlowCtrl_Type.__name__ = "Integer32"
_EocBrEPPortPropFlowCtrl_Object = MibTableColumn
eocBrEPPortPropFlowCtrl = _EocBrEPPortPropFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 7),
    _EocBrEPPortPropFlowCtrl_Type()
)
eocBrEPPortPropFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPPortPropFlowCtrl.setStatus("current")


class _EocBrEPPortPropInRateCtrl_Type(Integer32):
    """Custom type eocBrEPPortPropInRateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrEPPortPropInRateCtrl_Type.__name__ = "Integer32"
_EocBrEPPortPropInRateCtrl_Object = MibTableColumn
eocBrEPPortPropInRateCtrl = _EocBrEPPortPropInRateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 8),
    _EocBrEPPortPropInRateCtrl_Type()
)
eocBrEPPortPropInRateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPPortPropInRateCtrl.setStatus("current")


class _EocBrEPPortPropInRate_Type(Integer32):
    """Custom type eocBrEPPortPropInRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1563),
    )


_EocBrEPPortPropInRate_Type.__name__ = "Integer32"
_EocBrEPPortPropInRate_Object = MibTableColumn
eocBrEPPortPropInRate = _EocBrEPPortPropInRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 9),
    _EocBrEPPortPropInRate_Type()
)
eocBrEPPortPropInRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPPortPropInRate.setStatus("current")


class _EocBrEPPortPropOutRateCtrl_Type(Integer32):
    """Custom type eocBrEPPortPropOutRateCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrEPPortPropOutRateCtrl_Type.__name__ = "Integer32"
_EocBrEPPortPropOutRateCtrl_Object = MibTableColumn
eocBrEPPortPropOutRateCtrl = _EocBrEPPortPropOutRateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 10),
    _EocBrEPPortPropOutRateCtrl_Type()
)
eocBrEPPortPropOutRateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPPortPropOutRateCtrl.setStatus("current")


class _EocBrEPPortPropOutRate_Type(Integer32):
    """Custom type eocBrEPPortPropOutRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1563),
    )


_EocBrEPPortPropOutRate_Type.__name__ = "Integer32"
_EocBrEPPortPropOutRate_Object = MibTableColumn
eocBrEPPortPropOutRate = _EocBrEPPortPropOutRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 11),
    _EocBrEPPortPropOutRate_Type()
)
eocBrEPPortPropOutRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPPortPropOutRate.setStatus("current")


class _EocBrEPPortPropEnableCtrl_Type(Integer32):
    """Custom type eocBrEPPortPropEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrEPPortPropEnableCtrl_Type.__name__ = "Integer32"
_EocBrEPPortPropEnableCtrl_Object = MibTableColumn
eocBrEPPortPropEnableCtrl = _EocBrEPPortPropEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 1, 1, 12),
    _EocBrEPPortPropEnableCtrl_Type()
)
eocBrEPPortPropEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPPortPropEnableCtrl.setStatus("current")
_EocBrEPPortStatsTable_Object = MibTable
eocBrEPPortStatsTable = _EocBrEPPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    eocBrEPPortStatsTable.setStatus("current")
_EocBrEPPortStatsEntry_Object = MibTableRow
eocBrEPPortStatsEntry = _EocBrEPPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1)
)
eocBrEPPortStatsEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPPortStatsEPIndex"),
    (0, "ZYXEL-ES-EOC350", "eocBrEPPortStatsPID"),
)
if mibBuilder.loadTexts:
    eocBrEPPortStatsEntry.setStatus("current")
_EocBrEPPortStatsEPIndex_Type = Integer32
_EocBrEPPortStatsEPIndex_Object = MibTableColumn
eocBrEPPortStatsEPIndex = _EocBrEPPortStatsEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1, 1),
    _EocBrEPPortStatsEPIndex_Type()
)
eocBrEPPortStatsEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortStatsEPIndex.setStatus("current")
_EocBrEPPortStatsPID_Type = Integer32
_EocBrEPPortStatsPID_Object = MibTableColumn
eocBrEPPortStatsPID = _EocBrEPPortStatsPID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1, 2),
    _EocBrEPPortStatsPID_Type()
)
eocBrEPPortStatsPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortStatsPID.setStatus("current")
_EocBrEPPortStatsEPMac_Type = MacAddress
_EocBrEPPortStatsEPMac_Object = MibTableColumn
eocBrEPPortStatsEPMac = _EocBrEPPortStatsEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1, 3),
    _EocBrEPPortStatsEPMac_Type()
)
eocBrEPPortStatsEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortStatsEPMac.setStatus("current")


class _EocBrEPPortStatsType_Type(Integer32):
    """Custom type eocBrEPPortStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("coax", 1),
          ("phoneLine", 2))
    )


_EocBrEPPortStatsType_Type.__name__ = "Integer32"
_EocBrEPPortStatsType_Object = MibTableColumn
eocBrEPPortStatsType = _EocBrEPPortStatsType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1, 4),
    _EocBrEPPortStatsType_Type()
)
eocBrEPPortStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortStatsType.setStatus("current")
_EocBrEPPortStatsRxPkts_Type = Counter32
_EocBrEPPortStatsRxPkts_Object = MibTableColumn
eocBrEPPortStatsRxPkts = _EocBrEPPortStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1, 5),
    _EocBrEPPortStatsRxPkts_Type()
)
eocBrEPPortStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortStatsRxPkts.setStatus("current")
_EocBrEPPortStatsRxBytes_Type = Counter32
_EocBrEPPortStatsRxBytes_Object = MibTableColumn
eocBrEPPortStatsRxBytes = _EocBrEPPortStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1, 6),
    _EocBrEPPortStatsRxBytes_Type()
)
eocBrEPPortStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortStatsRxBytes.setStatus("current")
_EocBrEPPortStatsTxPkts_Type = Counter32
_EocBrEPPortStatsTxPkts_Object = MibTableColumn
eocBrEPPortStatsTxPkts = _EocBrEPPortStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1, 7),
    _EocBrEPPortStatsTxPkts_Type()
)
eocBrEPPortStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortStatsTxPkts.setStatus("current")
_EocBrEPPortStatsTxBytes_Type = Counter32
_EocBrEPPortStatsTxBytes_Object = MibTableColumn
eocBrEPPortStatsTxBytes = _EocBrEPPortStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1, 8),
    _EocBrEPPortStatsTxBytes_Type()
)
eocBrEPPortStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortStatsTxBytes.setStatus("current")
_EocBrEPPortStatsCollisions_Type = Counter32
_EocBrEPPortStatsCollisions_Object = MibTableColumn
eocBrEPPortStatsCollisions = _EocBrEPPortStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1, 9),
    _EocBrEPPortStatsCollisions_Type()
)
eocBrEPPortStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortStatsCollisions.setStatus("current")
_EocBrEPPortStatsErrors_Type = Counter32
_EocBrEPPortStatsErrors_Object = MibTableColumn
eocBrEPPortStatsErrors = _EocBrEPPortStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 2, 1, 10),
    _EocBrEPPortStatsErrors_Type()
)
eocBrEPPortStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPortStatsErrors.setStatus("current")
_EocBrEPStatsCtrlTable_Object = MibTable
eocBrEPStatsCtrlTable = _EocBrEPStatsCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 3)
)
if mibBuilder.loadTexts:
    eocBrEPStatsCtrlTable.setStatus("current")
_EocBrEPStatsCtrlEntry_Object = MibTableRow
eocBrEPStatsCtrlEntry = _EocBrEPStatsCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 3, 1)
)
eocBrEPStatsCtrlEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPStatsCtrlEPIndex"),
)
if mibBuilder.loadTexts:
    eocBrEPStatsCtrlEntry.setStatus("current")
_EocBrEPStatsCtrlEPIndex_Type = Integer32
_EocBrEPStatsCtrlEPIndex_Object = MibTableColumn
eocBrEPStatsCtrlEPIndex = _EocBrEPStatsCtrlEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 3, 1, 1),
    _EocBrEPStatsCtrlEPIndex_Type()
)
eocBrEPStatsCtrlEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPStatsCtrlEPIndex.setStatus("current")
_EocBrEPStatsCtrlEPMac_Type = MacAddress
_EocBrEPStatsCtrlEPMac_Object = MibTableColumn
eocBrEPStatsCtrlEPMac = _EocBrEPStatsCtrlEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 3, 1, 2),
    _EocBrEPStatsCtrlEPMac_Type()
)
eocBrEPStatsCtrlEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPStatsCtrlEPMac.setStatus("current")


class _EocBrEPStatsCtrlReset_Type(Integer32):
    """Custom type eocBrEPStatsCtrlReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrEPStatsCtrlReset_Type.__name__ = "Integer32"
_EocBrEPStatsCtrlReset_Object = MibTableColumn
eocBrEPStatsCtrlReset = _EocBrEPStatsCtrlReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 3, 1, 3),
    _EocBrEPStatsCtrlReset_Type()
)
eocBrEPStatsCtrlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPStatsCtrlReset.setStatus("current")


class _EocBrEPStatsCtrlRefresh_Type(Integer32):
    """Custom type eocBrEPStatsCtrlRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrEPStatsCtrlRefresh_Type.__name__ = "Integer32"
_EocBrEPStatsCtrlRefresh_Object = MibTableColumn
eocBrEPStatsCtrlRefresh = _EocBrEPStatsCtrlRefresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 2, 3, 1, 4),
    _EocBrEPStatsCtrlRefresh_Type()
)
eocBrEPStatsCtrlRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPStatsCtrlRefresh.setStatus("current")
_EocBrEPEtherQoS_ObjectIdentity = ObjectIdentity
eocBrEPEtherQoS = _EocBrEPEtherQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3)
)
_EocBrEPTcpUdpPriTable_Object = MibTable
eocBrEPTcpUdpPriTable = _EocBrEPTcpUdpPriTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 2)
)
if mibBuilder.loadTexts:
    eocBrEPTcpUdpPriTable.setStatus("current")
_EocBrEPTcpUdpPriEntry_Object = MibTableRow
eocBrEPTcpUdpPriEntry = _EocBrEPTcpUdpPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 2, 1)
)
eocBrEPTcpUdpPriEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPTcpUdpEPIndex"),
    (0, "ZYXEL-ES-EOC350", "eocBrEPTcpUdpRuleNum"),
)
if mibBuilder.loadTexts:
    eocBrEPTcpUdpPriEntry.setStatus("current")
_EocBrEPTcpUdpEPIndex_Type = Integer32
_EocBrEPTcpUdpEPIndex_Object = MibTableColumn
eocBrEPTcpUdpEPIndex = _EocBrEPTcpUdpEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 2, 1, 1),
    _EocBrEPTcpUdpEPIndex_Type()
)
eocBrEPTcpUdpEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPTcpUdpEPIndex.setStatus("current")
_EocBrEPTcpUdpRuleNum_Type = Integer32
_EocBrEPTcpUdpRuleNum_Object = MibTableColumn
eocBrEPTcpUdpRuleNum = _EocBrEPTcpUdpRuleNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 2, 1, 2),
    _EocBrEPTcpUdpRuleNum_Type()
)
eocBrEPTcpUdpRuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPTcpUdpRuleNum.setStatus("current")
_EocBrEPTcpUdpEPMac_Type = MacAddress
_EocBrEPTcpUdpEPMac_Object = MibTableColumn
eocBrEPTcpUdpEPMac = _EocBrEPTcpUdpEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 2, 1, 3),
    _EocBrEPTcpUdpEPMac_Type()
)
eocBrEPTcpUdpEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPTcpUdpEPMac.setStatus("current")


class _EocBrEPTcpUdpEnableCtrl_Type(Integer32):
    """Custom type eocBrEPTcpUdpEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrEPTcpUdpEnableCtrl_Type.__name__ = "Integer32"
_EocBrEPTcpUdpEnableCtrl_Object = MibTableColumn
eocBrEPTcpUdpEnableCtrl = _EocBrEPTcpUdpEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 2, 1, 4),
    _EocBrEPTcpUdpEnableCtrl_Type()
)
eocBrEPTcpUdpEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPTcpUdpEnableCtrl.setStatus("current")


class _EocBrEPTcpUdpPortNum_Type(Integer32):
    """Custom type eocBrEPTcpUdpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EocBrEPTcpUdpPortNum_Type.__name__ = "Integer32"
_EocBrEPTcpUdpPortNum_Object = MibTableColumn
eocBrEPTcpUdpPortNum = _EocBrEPTcpUdpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 2, 1, 5),
    _EocBrEPTcpUdpPortNum_Type()
)
eocBrEPTcpUdpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPTcpUdpPortNum.setStatus("current")


class _EocBrEPTcpUdpMappedQueue_Type(Integer32):
    """Custom type eocBrEPTcpUdpMappedQueue based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3))
    )


_EocBrEPTcpUdpMappedQueue_Type.__name__ = "Integer32"
_EocBrEPTcpUdpMappedQueue_Object = MibTableColumn
eocBrEPTcpUdpMappedQueue = _EocBrEPTcpUdpMappedQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 2, 1, 6),
    _EocBrEPTcpUdpMappedQueue_Type()
)
eocBrEPTcpUdpMappedQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPTcpUdpMappedQueue.setStatus("current")
_EocBrEPQueueSchTable_Object = MibTable
eocBrEPQueueSchTable = _EocBrEPQueueSchTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    eocBrEPQueueSchTable.setStatus("current")
_EocBrEPQueueSchEntry_Object = MibTableRow
eocBrEPQueueSchEntry = _EocBrEPQueueSchEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 3, 1)
)
eocBrEPQueueSchEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPQueueSchEPIndex"),
)
if mibBuilder.loadTexts:
    eocBrEPQueueSchEntry.setStatus("current")
_EocBrEPQueueSchEPIndex_Type = Integer32
_EocBrEPQueueSchEPIndex_Object = MibTableColumn
eocBrEPQueueSchEPIndex = _EocBrEPQueueSchEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 3, 1, 1),
    _EocBrEPQueueSchEPIndex_Type()
)
eocBrEPQueueSchEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPQueueSchEPIndex.setStatus("current")
_EocBrEPQueueSchEPMac_Type = MacAddress
_EocBrEPQueueSchEPMac_Object = MibTableColumn
eocBrEPQueueSchEPMac = _EocBrEPQueueSchEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 3, 1, 2),
    _EocBrEPQueueSchEPMac_Type()
)
eocBrEPQueueSchEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPQueueSchEPMac.setStatus("current")


class _EocBrEPQueueSchType_Type(Integer32):
    """Custom type eocBrEPQueueSchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 0),
          ("wfq", 1),
          ("mix", 2))
    )


_EocBrEPQueueSchType_Type.__name__ = "Integer32"
_EocBrEPQueueSchType_Object = MibTableColumn
eocBrEPQueueSchType = _EocBrEPQueueSchType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 3, 1, 3),
    _EocBrEPQueueSchType_Type()
)
eocBrEPQueueSchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPQueueSchType.setStatus("current")
_EocBrEPPriSchemeTable_Object = MibTable
eocBrEPPriSchemeTable = _EocBrEPPriSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 4)
)
if mibBuilder.loadTexts:
    eocBrEPPriSchemeTable.setStatus("current")
_EocBrEPPriSchemeEntry_Object = MibTableRow
eocBrEPPriSchemeEntry = _EocBrEPPriSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 4, 1)
)
eocBrEPPriSchemeEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPPriSchemeEPIndex"),
)
if mibBuilder.loadTexts:
    eocBrEPPriSchemeEntry.setStatus("current")
_EocBrEPPriSchemeEPIndex_Type = Integer32
_EocBrEPPriSchemeEPIndex_Object = MibTableColumn
eocBrEPPriSchemeEPIndex = _EocBrEPPriSchemeEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 4, 1, 1),
    _EocBrEPPriSchemeEPIndex_Type()
)
eocBrEPPriSchemeEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPriSchemeEPIndex.setStatus("current")
_EocBrEPPriSchemeEPMac_Type = MacAddress
_EocBrEPPriSchemeEPMac_Object = MibTableColumn
eocBrEPPriSchemeEPMac = _EocBrEPPriSchemeEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 4, 1, 2),
    _EocBrEPPriSchemeEPMac_Type()
)
eocBrEPPriSchemeEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPPriSchemeEPMac.setStatus("current")


class _EocBrEPPriSchemeSelect_Type(Integer32):
    """Custom type eocBrEPPriSchemeSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("use8021p", 0),
          ("useIP", 1))
    )


_EocBrEPPriSchemeSelect_Type.__name__ = "Integer32"
_EocBrEPPriSchemeSelect_Object = MibTableColumn
eocBrEPPriSchemeSelect = _EocBrEPPriSchemeSelect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 3, 4, 1, 3),
    _EocBrEPPriSchemeSelect_Type()
)
eocBrEPPriSchemeSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPPriSchemeSelect.setStatus("current")
_EocBrEPEtherIGMPSnoop_ObjectIdentity = ObjectIdentity
eocBrEPEtherIGMPSnoop = _EocBrEPEtherIGMPSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 4)
)
_EocBrEPIGMPSnoopTable_Object = MibTable
eocBrEPIGMPSnoopTable = _EocBrEPIGMPSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 4, 1)
)
if mibBuilder.loadTexts:
    eocBrEPIGMPSnoopTable.setStatus("current")
_EocBrEPIGMPSnoopEntry_Object = MibTableRow
eocBrEPIGMPSnoopEntry = _EocBrEPIGMPSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 4, 1, 1)
)
eocBrEPIGMPSnoopEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPIGMPSnoopEPIndex"),
)
if mibBuilder.loadTexts:
    eocBrEPIGMPSnoopEntry.setStatus("current")
_EocBrEPIGMPSnoopEPIndex_Type = Integer32
_EocBrEPIGMPSnoopEPIndex_Object = MibTableColumn
eocBrEPIGMPSnoopEPIndex = _EocBrEPIGMPSnoopEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 4, 1, 1, 1),
    _EocBrEPIGMPSnoopEPIndex_Type()
)
eocBrEPIGMPSnoopEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPIGMPSnoopEPIndex.setStatus("current")
_EocBrEPIGMPSnoopEPMac_Type = MacAddress
_EocBrEPIGMPSnoopEPMac_Object = MibTableColumn
eocBrEPIGMPSnoopEPMac = _EocBrEPIGMPSnoopEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 4, 1, 1, 2),
    _EocBrEPIGMPSnoopEPMac_Type()
)
eocBrEPIGMPSnoopEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPIGMPSnoopEPMac.setStatus("current")


class _EocBrEPIGMPSnoopEnableCtrl_Type(Integer32):
    """Custom type eocBrEPIGMPSnoopEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrEPIGMPSnoopEnableCtrl_Type.__name__ = "Integer32"
_EocBrEPIGMPSnoopEnableCtrl_Object = MibTableColumn
eocBrEPIGMPSnoopEnableCtrl = _EocBrEPIGMPSnoopEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 4, 1, 1, 3),
    _EocBrEPIGMPSnoopEnableCtrl_Type()
)
eocBrEPIGMPSnoopEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPIGMPSnoopEnableCtrl.setStatus("current")
_EocBrEPEtherTagVLAN_ObjectIdentity = ObjectIdentity
eocBrEPEtherTagVLAN = _EocBrEPEtherTagVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5)
)
_EocBrEPTagVLANCtrlTable_Object = MibTable
eocBrEPTagVLANCtrlTable = _EocBrEPTagVLANCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 1)
)
if mibBuilder.loadTexts:
    eocBrEPTagVLANCtrlTable.setStatus("current")
_EocBrEPTagVLANCtrlEntry_Object = MibTableRow
eocBrEPTagVLANCtrlEntry = _EocBrEPTagVLANCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 1, 1)
)
eocBrEPTagVLANCtrlEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPTagVLANEPIndex"),
)
if mibBuilder.loadTexts:
    eocBrEPTagVLANCtrlEntry.setStatus("current")
_EocBrEPTagVLANEPIndex_Type = Integer32
_EocBrEPTagVLANEPIndex_Object = MibTableColumn
eocBrEPTagVLANEPIndex = _EocBrEPTagVLANEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 1, 1, 1),
    _EocBrEPTagVLANEPIndex_Type()
)
eocBrEPTagVLANEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPTagVLANEPIndex.setStatus("current")
_EocBrEPTagVLANEPMac_Type = MacAddress
_EocBrEPTagVLANEPMac_Object = MibTableColumn
eocBrEPTagVLANEPMac = _EocBrEPTagVLANEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 1, 1, 2),
    _EocBrEPTagVLANEPMac_Type()
)
eocBrEPTagVLANEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPTagVLANEPMac.setStatus("current")


class _EocBrEPTagVLANEnableCtrl_Type(Integer32):
    """Custom type eocBrEPTagVLANEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrEPTagVLANEnableCtrl_Type.__name__ = "Integer32"
_EocBrEPTagVLANEnableCtrl_Object = MibTableColumn
eocBrEPTagVLANEnableCtrl = _EocBrEPTagVLANEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 1, 1, 3),
    _EocBrEPTagVLANEnableCtrl_Type()
)
eocBrEPTagVLANEnableCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPTagVLANEnableCtrl.setStatus("current")
_EocBrEPTagPortTable_Object = MibTable
eocBrEPTagPortTable = _EocBrEPTagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 2)
)
if mibBuilder.loadTexts:
    eocBrEPTagPortTable.setStatus("current")
_EocBrEPTagPortEntry_Object = MibTableRow
eocBrEPTagPortEntry = _EocBrEPTagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 2, 1)
)
eocBrEPTagPortEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPTagPortEPIndex"),
    (0, "ZYXEL-ES-EOC350", "eocBrEPTagPortPID"),
)
if mibBuilder.loadTexts:
    eocBrEPTagPortEntry.setStatus("current")
_EocBrEPTagPortEPIndex_Type = Integer32
_EocBrEPTagPortEPIndex_Object = MibTableColumn
eocBrEPTagPortEPIndex = _EocBrEPTagPortEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 2, 1, 1),
    _EocBrEPTagPortEPIndex_Type()
)
eocBrEPTagPortEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPTagPortEPIndex.setStatus("current")
_EocBrEPTagPortPID_Type = Integer32
_EocBrEPTagPortPID_Object = MibTableColumn
eocBrEPTagPortPID = _EocBrEPTagPortPID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 2, 1, 2),
    _EocBrEPTagPortPID_Type()
)
eocBrEPTagPortPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPTagPortPID.setStatus("current")
_EocBrEPTagPortEPMac_Type = MacAddress
_EocBrEPTagPortEPMac_Object = MibTableColumn
eocBrEPTagPortEPMac = _EocBrEPTagPortEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 2, 1, 3),
    _EocBrEPTagPortEPMac_Type()
)
eocBrEPTagPortEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPTagPortEPMac.setStatus("current")


class _EocBrEPTagPortType_Type(Integer32):
    """Custom type eocBrEPTagPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("coax", 1),
          ("phoneLine", 2))
    )


_EocBrEPTagPortType_Type.__name__ = "Integer32"
_EocBrEPTagPortType_Object = MibTableColumn
eocBrEPTagPortType = _EocBrEPTagPortType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 2, 1, 4),
    _EocBrEPTagPortType_Type()
)
eocBrEPTagPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPTagPortType.setStatus("current")


class _EocBrEPTagPortPriority_Type(Integer32):
    """Custom type eocBrEPTagPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EocBrEPTagPortPriority_Type.__name__ = "Integer32"
_EocBrEPTagPortPriority_Object = MibTableColumn
eocBrEPTagPortPriority = _EocBrEPTagPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 2, 1, 5),
    _EocBrEPTagPortPriority_Type()
)
eocBrEPTagPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPTagPortPriority.setStatus("current")


class _EocBrEPTagPortVID_Type(Integer32):
    """Custom type eocBrEPTagPortVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_EocBrEPTagPortVID_Type.__name__ = "Integer32"
_EocBrEPTagPortVID_Object = MibTableColumn
eocBrEPTagPortVID = _EocBrEPTagPortVID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 2, 1, 6),
    _EocBrEPTagPortVID_Type()
)
eocBrEPTagPortVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPTagPortVID.setStatus("current")


class _EocBrEPTagPortInRule_Type(Integer32):
    """Custom type eocBrEPTagPortInRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("tag", 1))
    )


_EocBrEPTagPortInRule_Type.__name__ = "Integer32"
_EocBrEPTagPortInRule_Object = MibTableColumn
eocBrEPTagPortInRule = _EocBrEPTagPortInRule_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 2, 1, 7),
    _EocBrEPTagPortInRule_Type()
)
eocBrEPTagPortInRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPTagPortInRule.setStatus("current")


class _EocBrEPTagPortOutRule_Type(Integer32):
    """Custom type eocBrEPTagPortOutRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untag", 0),
          ("tag", 1),
          ("bypass", 2))
    )


_EocBrEPTagPortOutRule_Type.__name__ = "Integer32"
_EocBrEPTagPortOutRule_Object = MibTableColumn
eocBrEPTagPortOutRule = _EocBrEPTagPortOutRule_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 5, 2, 1, 8),
    _EocBrEPTagPortOutRule_Type()
)
eocBrEPTagPortOutRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPTagPortOutRule.setStatus("current")
_EocBrEPCtrl_ObjectIdentity = ObjectIdentity
eocBrEPCtrl = _EocBrEPCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 6)
)
_EocBrEPCtrlTable_Object = MibTable
eocBrEPCtrlTable = _EocBrEPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 6, 1)
)
if mibBuilder.loadTexts:
    eocBrEPCtrlTable.setStatus("current")
_EocBrEPCtrlEntry_Object = MibTableRow
eocBrEPCtrlEntry = _EocBrEPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 6, 1, 1)
)
eocBrEPCtrlEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPCtrlEPIndex"),
)
if mibBuilder.loadTexts:
    eocBrEPCtrlEntry.setStatus("current")
_EocBrEPCtrlEPIndex_Type = Integer32
_EocBrEPCtrlEPIndex_Object = MibTableColumn
eocBrEPCtrlEPIndex = _EocBrEPCtrlEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 6, 1, 1, 1),
    _EocBrEPCtrlEPIndex_Type()
)
eocBrEPCtrlEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPCtrlEPIndex.setStatus("current")
_EocBrEPCtrlEPMac_Type = MacAddress
_EocBrEPCtrlEPMac_Object = MibTableColumn
eocBrEPCtrlEPMac = _EocBrEPCtrlEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 6, 1, 1, 2),
    _EocBrEPCtrlEPMac_Type()
)
eocBrEPCtrlEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPCtrlEPMac.setStatus("current")


class _EocBrEPCtrlEtherDefault_Type(Integer32):
    """Custom type eocBrEPCtrlEtherDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activate", 1))
    )


_EocBrEPCtrlEtherDefault_Type.__name__ = "Integer32"
_EocBrEPCtrlEtherDefault_Object = MibTableColumn
eocBrEPCtrlEtherDefault = _EocBrEPCtrlEtherDefault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 6, 1, 1, 3),
    _EocBrEPCtrlEtherDefault_Type()
)
eocBrEPCtrlEtherDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPCtrlEtherDefault.setStatus("current")


class _EocBrEPCtrlReboot_Type(Integer32):
    """Custom type eocBrEPCtrlReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activateThenReboot", 1))
    )


_EocBrEPCtrlReboot_Type.__name__ = "Integer32"
_EocBrEPCtrlReboot_Object = MibTableColumn
eocBrEPCtrlReboot = _EocBrEPCtrlReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 6, 1, 1, 4),
    _EocBrEPCtrlReboot_Type()
)
eocBrEPCtrlReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPCtrlReboot.setStatus("current")
_EocBrEPHostMacFilter_ObjectIdentity = ObjectIdentity
eocBrEPHostMacFilter = _EocBrEPHostMacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 7)
)
_EocBrEPHostMacFilterTable_Object = MibTable
eocBrEPHostMacFilterTable = _EocBrEPHostMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 7, 1)
)
if mibBuilder.loadTexts:
    eocBrEPHostMacFilterTable.setStatus("current")
_EocBrEPHostMacFilterEntry_Object = MibTableRow
eocBrEPHostMacFilterEntry = _EocBrEPHostMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 7, 1, 1)
)
eocBrEPHostMacFilterEntry.setIndexNames(
    (0, "ZYXEL-ES-EOC350", "eocBrEPHostMacFilterEPIndex"),
    (0, "ZYXEL-ES-EOC350", "eocBrEPHostMacFilterSetNum"),
)
if mibBuilder.loadTexts:
    eocBrEPHostMacFilterEntry.setStatus("current")
_EocBrEPHostMacFilterEPIndex_Type = Integer32
_EocBrEPHostMacFilterEPIndex_Object = MibTableColumn
eocBrEPHostMacFilterEPIndex = _EocBrEPHostMacFilterEPIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 7, 1, 1, 1),
    _EocBrEPHostMacFilterEPIndex_Type()
)
eocBrEPHostMacFilterEPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPHostMacFilterEPIndex.setStatus("current")
_EocBrEPHostMacFilterSetNum_Type = Integer32
_EocBrEPHostMacFilterSetNum_Object = MibTableColumn
eocBrEPHostMacFilterSetNum = _EocBrEPHostMacFilterSetNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 7, 1, 1, 2),
    _EocBrEPHostMacFilterSetNum_Type()
)
eocBrEPHostMacFilterSetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPHostMacFilterSetNum.setStatus("current")
_EocBrEPHostMacFilterEPMac_Type = MacAddress
_EocBrEPHostMacFilterEPMac_Object = MibTableColumn
eocBrEPHostMacFilterEPMac = _EocBrEPHostMacFilterEPMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 7, 1, 1, 3),
    _EocBrEPHostMacFilterEPMac_Type()
)
eocBrEPHostMacFilterEPMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPHostMacFilterEPMac.setStatus("current")


class _EocBrEPHostMacFilterEnableCtrl_Type(Integer32):
    """Custom type eocBrEPHostMacFilterEnableCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EocBrEPHostMacFilterEnableCtrl_Type.__name__ = "Integer32"
_EocBrEPHostMacFilterEnableCtrl_Object = MibTableColumn
eocBrEPHostMacFilterEnableCtrl = _EocBrEPHostMacFilterEnableCtrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 7, 1, 1, 4),
    _EocBrEPHostMacFilterEnableCtrl_Type()
)
eocBrEPHostMacFilterEnableCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocBrEPHostMacFilterEnableCtrl.setStatus("current")
_EocBrEPHostMacFilterHostMac_Type = MacAddress
_EocBrEPHostMacFilterHostMac_Object = MibTableColumn
eocBrEPHostMacFilterHostMac = _EocBrEPHostMacFilterHostMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 1, 11, 7, 1, 1, 5),
    _EocBrEPHostMacFilterHostMac_Type()
)
eocBrEPHostMacFilterHostMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocBrEPHostMacFilterHostMac.setStatus("current")
_Eoc350BrNotification_ObjectIdentity = ObjectIdentity
eoc350BrNotification = _Eoc350BrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3)
)

# Managed Objects groups


# Notification objects

eocBrHttpLoginNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 1)
)
eocBrHttpLoginNotification.setObjects(
    ("ZYXEL-ES-EOC350", "eocBrAccountName")
)
if mibBuilder.loadTexts:
    eocBrHttpLoginNotification.setStatus(
        "current"
    )

eocBrHttpLogoutNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 2)
)
eocBrHttpLogoutNotification.setObjects(
    ("ZYXEL-ES-EOC350", "eocBrAccountName")
)
if mibBuilder.loadTexts:
    eocBrHttpLogoutNotification.setStatus(
        "current"
    )

eocBrHttpLoginAuthFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 3)
)
eocBrHttpLoginAuthFailedNotification.setObjects(
    ("ZYXEL-ES-EOC350", "eocBrAccountName")
)
if mibBuilder.loadTexts:
    eocBrHttpLoginAuthFailedNotification.setStatus(
        "current"
    )

eocBrTelnetLoginNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 4)
)
eocBrTelnetLoginNotification.setObjects(
    ("ZYXEL-ES-EOC350", "eocBrAccountName")
)
if mibBuilder.loadTexts:
    eocBrTelnetLoginNotification.setStatus(
        "current"
    )

eocBrTelnetLogoutNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 5)
)
eocBrTelnetLogoutNotification.setObjects(
    ("ZYXEL-ES-EOC350", "eocBrAccountName")
)
if mibBuilder.loadTexts:
    eocBrTelnetLogoutNotification.setStatus(
        "current"
    )

eocBrTelnetLoginAuthFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 6)
)
eocBrTelnetLoginAuthFailedNotification.setObjects(
    ("ZYXEL-ES-EOC350", "eocBrAccountName")
)
if mibBuilder.loadTexts:
    eocBrTelnetLoginAuthFailedNotification.setStatus(
        "current"
    )

eocBrSystemFwUpgradeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 11)
)
eocBrSystemFwUpgradeNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrSystemFwWorkingVersion"),
        ("ZYXEL-ES-EOC350", "eocBrSystemFwUploadVersion"))
)
if mibBuilder.loadTexts:
    eocBrSystemFwUpgradeNotification.setStatus(
        "current"
    )

eocBrDhcpClientAckNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 21)
)
eocBrDhcpClientAckNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrSystemMac"),
        ("ZYXEL-ES-EOC350", "eocBrIPAddress"),
        ("ZYXEL-ES-EOC350", "eocBrDHCPLease"),
        ("ZYXEL-ES-EOC350", "eocBrIPAddress"))
)
if mibBuilder.loadTexts:
    eocBrDhcpClientAckNotification.setStatus(
        "current"
    )

eocBrHostDhcpClientAckNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 23)
)
eocBrHostDhcpClientAckNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrHostDHCPEPMac"),
        ("ZYXEL-ES-EOC350", "eocBrHostDHCPHostMac"),
        ("ZYXEL-ES-EOC350", "eocBrHostDHCPIPAddress"),
        ("ZYXEL-ES-EOC350", "eocBrHostDHCPLease"))
)
if mibBuilder.loadTexts:
    eocBrHostDhcpClientAckNotification.setStatus(
        "current"
    )

eocBrAutoConfigTFTPGetOkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 27)
)
eocBrAutoConfigTFTPGetOkNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrTFTPServerIPAddress"),
        ("ZYXEL-ES-EOC350", "eocBrTFTPFilename"))
)
if mibBuilder.loadTexts:
    eocBrAutoConfigTFTPGetOkNotification.setStatus(
        "current"
    )

eocBrAutoConfigTFTPGetErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 28)
)
eocBrAutoConfigTFTPGetErrorNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrTFTPServerIPAddress"),
        ("ZYXEL-ES-EOC350", "eocBrTFTPFilename"))
)
if mibBuilder.loadTexts:
    eocBrAutoConfigTFTPGetErrorNotification.setStatus(
        "current"
    )

eocBrHTTPGetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 51)
)
eocBrHTTPGetNotification.setObjects(
    ("ZYXEL-ES-EOC350", "eocBrTFTPServerIPAddress")
)
if mibBuilder.loadTexts:
    eocBrHTTPGetNotification.setStatus(
        "current"
    )

eocBrMasterDrvUpgradeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 71)
)
eocBrMasterDrvUpgradeNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrMasterMac"),
        ("ZYXEL-ES-EOC350", "eocBrMasterDrvWorkingVersion"),
        ("ZYXEL-ES-EOC350", "eocBrMasterDrvUploadVersion"))
)
if mibBuilder.loadTexts:
    eocBrMasterDrvUpgradeNotification.setStatus(
        "current"
    )

eocBrEPDrvUpgradeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 81)
)
eocBrEPDrvUpgradeNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrEPMac"),
        ("ZYXEL-ES-EOC350", "eocBrEPDrvWorkingVersion"),
        ("ZYXEL-ES-EOC350", "eocBrEPDrvUploadVersion"))
)
if mibBuilder.loadTexts:
    eocBrEPDrvUpgradeNotification.setStatus(
        "current"
    )

eocBrEPOnlineStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 82)
)
eocBrEPOnlineStatusNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrEPMac"),
        ("ZYXEL-ES-EOC350", "eocBrEPOnlineStatus"),
        ("ZYXEL-ES-EOC350", "eocBrSystemMac"))
)
if mibBuilder.loadTexts:
    eocBrEPOnlineStatusNotification.setStatus(
        "current"
    )

eocBrEPDiagResultNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 83)
)
eocBrEPDiagResultNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrEPMac"),
        ("ZYXEL-ES-EOC350", "eocBrEPDiagDnLinkResult"),
        ("ZYXEL-ES-EOC350", "eocBrEPDiagUpLinkResult"))
)
if mibBuilder.loadTexts:
    eocBrEPDiagResultNotification.setStatus(
        "current"
    )

eocBrTFTPGetOkNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 91)
)
eocBrTFTPGetOkNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrTFTPServerIPAddress"),
        ("ZYXEL-ES-EOC350", "eocBrTFTPFilename"))
)
if mibBuilder.loadTexts:
    eocBrTFTPGetOkNotification.setStatus(
        "current"
    )

eocBrTFTPGetErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 5, 3, 92)
)
eocBrTFTPGetErrorNotification.setObjects(
      *(("ZYXEL-ES-EOC350", "eocBrTFTPServerIPAddress"),
        ("ZYXEL-ES-EOC350", "eocBrTFTPFilename"))
)
if mibBuilder.loadTexts:
    eocBrTFTPGetErrorNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES-EOC350",
    **{"eoc350BrMib": eoc350BrMib,
       "eocBrSystemGroup": eocBrSystemGroup,
       "eocBrModel": eocBrModel,
       "eocBrProductName": eocBrProductName,
       "eocBrSystemMac": eocBrSystemMac,
       "eocBrEoCMac": eocBrEoCMac,
       "eocBrHardwareVersion": eocBrHardwareVersion,
       "eocBrBootVersion": eocBrBootVersion,
       "eocBrSystemFwWorkingVersion": eocBrSystemFwWorkingVersion,
       "eocBrSystemFwUploadVersion": eocBrSystemFwUploadVersion,
       "eocBrSystemFwUpgradeAction": eocBrSystemFwUpgradeAction,
       "eocBrSystemFwUpgradeStatus": eocBrSystemFwUpgradeStatus,
       "eocBrSystemReboot": eocBrSystemReboot,
       "eocBrAutoEPDrvUpgrade": eocBrAutoEPDrvUpgrade,
       "eocBrIPGroup": eocBrIPGroup,
       "eocBrIPAddress": eocBrIPAddress,
       "eocBrSubnetMask": eocBrSubnetMask,
       "eocBrDefaultGatewayIPAddress": eocBrDefaultGatewayIPAddress,
       "eocBrPrimaryDnsIPAddress": eocBrPrimaryDnsIPAddress,
       "eocBrSecondaryDnsIPAddress": eocBrSecondaryDnsIPAddress,
       "eocBrIPAddressAssign": eocBrIPAddressAssign,
       "eocBrDHCPLease": eocBrDHCPLease,
       "eocBrHostDHCPPadOpt82EnableCtrl": eocBrHostDHCPPadOpt82EnableCtrl,
       "eocBrHostIPSourceGuardCtrl": eocBrHostIPSourceGuardCtrl,
       "eocBrHostDHCPTable": eocBrHostDHCPTable,
       "eocBrHostDHCPEntry": eocBrHostDHCPEntry,
       "eocBrHostDHCPIndex": eocBrHostDHCPIndex,
       "eocBrHostDHCPEPMac": eocBrHostDHCPEPMac,
       "eocBrHostDHCPHostMac": eocBrHostDHCPHostMac,
       "eocBrHostDHCPIPAddress": eocBrHostDHCPIPAddress,
       "eocBrHostDHCPLease": eocBrHostDHCPLease,
       "eocBrAutoConfig": eocBrAutoConfig,
       "eocBrAutoConfigTFTPServerIPAddress": eocBrAutoConfigTFTPServerIPAddress,
       "eocBrAutoConfigTFTPExtensionPath": eocBrAutoConfigTFTPExtensionPath,
       "eocBrAutoConfigTFTPServer": eocBrAutoConfigTFTPServer,
       "eocBrAdminGroup": eocBrAdminGroup,
       "eocBrAccountTable": eocBrAccountTable,
       "eocBrAccountEntry": eocBrAccountEntry,
       "eocBrAccountIndex": eocBrAccountIndex,
       "eocBrAccountName": eocBrAccountName,
       "eocBrAccountPasswd": eocBrAccountPasswd,
       "eocBrAccountPrivilege": eocBrAccountPrivilege,
       "eocBrAccountRowStatus": eocBrAccountRowStatus,
       "eocBrAllowIPProtocolTable": eocBrAllowIPProtocolTable,
       "eocBrAllowIPProtocolEntry": eocBrAllowIPProtocolEntry,
       "eocBrAllowIndex": eocBrAllowIndex,
       "eocBrAllowIPAddress": eocBrAllowIPAddress,
       "eocBrAllowSubnetMask": eocBrAllowSubnetMask,
       "eocBrAllowTelnet": eocBrAllowTelnet,
       "eocBrAllowHttp": eocBrAllowHttp,
       "eocBrAllowSnmp": eocBrAllowSnmp,
       "eocBrAllowIcmpPing": eocBrAllowIcmpPing,
       "eocBrAllowRowStatus": eocBrAllowRowStatus,
       "eocBrStaticMacTable": eocBrStaticMacTable,
       "eocBrStaticMacEntry": eocBrStaticMacEntry,
       "eocBrStaticMacIndex": eocBrStaticMacIndex,
       "eocBrStaticMacAddress": eocBrStaticMacAddress,
       "eocBrStaticMacBindingPort": eocBrStaticMacBindingPort,
       "eocBrStaticMacRowStatus": eocBrStaticMacRowStatus,
       "eocBrServiceGroup": eocBrServiceGroup,
       "eocBrTelnet": eocBrTelnet,
       "eocBrTelnetEnableCtrl": eocBrTelnetEnableCtrl,
       "eocBrTelnetPortNum": eocBrTelnetPortNum,
       "eocBrTelnetExpiryInSeconds": eocBrTelnetExpiryInSeconds,
       "eocBrHttp": eocBrHttp,
       "eocBrHttpEnableCtrl": eocBrHttpEnableCtrl,
       "eocBrHttpPortNum": eocBrHttpPortNum,
       "eocBrSnmp": eocBrSnmp,
       "eocBrSnmpEnableCtrl": eocBrSnmpEnableCtrl,
       "eocBrSnmpPortNum": eocBrSnmpPortNum,
       "eocBrSnmpName": eocBrSnmpName,
       "eocBrSnmpContact": eocBrSnmpContact,
       "eocBrSnmpLocation": eocBrSnmpLocation,
       "eocBrSnmpReadWriteCommunity": eocBrSnmpReadWriteCommunity,
       "eocBrSnmpReadOnlyCommunity": eocBrSnmpReadOnlyCommunity,
       "eocBrSnmpTrapEnableTable": eocBrSnmpTrapEnableTable,
       "eocBrSnmpTrapEnableEntry": eocBrSnmpTrapEnableEntry,
       "eocBrSnmpTrapEnableIndex": eocBrSnmpTrapEnableIndex,
       "eocBrSnmpTrapEnableType": eocBrSnmpTrapEnableType,
       "eocBrSnmpTrapEnableCtrl": eocBrSnmpTrapEnableCtrl,
       "eocBrSnmpTrapTable": eocBrSnmpTrapTable,
       "eocBrSnmpTrapEntry": eocBrSnmpTrapEntry,
       "eocBrSnmpTrapIndex": eocBrSnmpTrapIndex,
       "eocBrSnmpTrapServer": eocBrSnmpTrapServer,
       "eocBrSnmpTrapPortNum": eocBrSnmpTrapPortNum,
       "eocBrSnmpTrapCommunity": eocBrSnmpTrapCommunity,
       "eocBrSnmpTrapRowStatus": eocBrSnmpTrapRowStatus,
       "eocBrSyslogTable": eocBrSyslogTable,
       "eocBrSyslogEntry": eocBrSyslogEntry,
       "eocBrSyslogIndex": eocBrSyslogIndex,
       "eocBrSyslogServer": eocBrSyslogServer,
       "eocBrSyslogIPAddress": eocBrSyslogIPAddress,
       "eocBrSyslogSeverity": eocBrSyslogSeverity,
       "eocBrSyslogRowStatus": eocBrSyslogRowStatus,
       "eocBrSntp": eocBrSntp,
       "eocBrSntpEnableCtrl": eocBrSntpEnableCtrl,
       "eocBrSntpPrimaryServer": eocBrSntpPrimaryServer,
       "eocBrSntpSecondaryServer": eocBrSntpSecondaryServer,
       "eocBrSntpTimeZone": eocBrSntpTimeZone,
       "eocBrSntpQueryPeriodInMinutes": eocBrSntpQueryPeriodInMinutes,
       "eocBrSntpCurrentTime": eocBrSntpCurrentTime,
       "eocBrSyslogCtrl": eocBrSyslogCtrl,
       "eocBrSyslogOverTcpUdp": eocBrSyslogOverTcpUdp,
       "eocBrSyslogPortNum": eocBrSyslogPortNum,
       "eocBrMasterEoCGroup": eocBrMasterEoCGroup,
       "eocBrMasterMac": eocBrMasterMac,
       "eocBrMasterNote": eocBrMasterNote,
       "eocBrMasterModel": eocBrMasterModel,
       "eocBrMasterProductName": eocBrMasterProductName,
       "eocBrMasterWorkingPrivacyMode": eocBrMasterWorkingPrivacyMode,
       "eocBrMasterSettingPrivacyMode": eocBrMasterSettingPrivacyMode,
       "eocBrMasterWorkingPrivacyKey": eocBrMasterWorkingPrivacyKey,
       "eocBrMasterSettingPrivacyKey": eocBrMasterSettingPrivacyKey,
       "eocBrMasterDrvWorkingVersion": eocBrMasterDrvWorkingVersion,
       "eocBrMasterDrvUploadVersion": eocBrMasterDrvUploadVersion,
       "eocBrMasterDrvUpgradeAction": eocBrMasterDrvUpgradeAction,
       "eocBrMasterDrvUpgradeStatus": eocBrMasterDrvUpgradeStatus,
       "eocBrMasterScanEPAction": eocBrMasterScanEPAction,
       "eocBrMasterScanEPStatus": eocBrMasterScanEPStatus,
       "eocBrMasterReboot": eocBrMasterReboot,
       "eocBrEPEoCGroup": eocBrEPEoCGroup,
       "eocBrEPTable": eocBrEPTable,
       "eocBrEPEntry": eocBrEPEntry,
       "eocBrEPIndex": eocBrEPIndex,
       "eocBrEPMac": eocBrEPMac,
       "eocBrEPNote": eocBrEPNote,
       "eocBrEPModel": eocBrEPModel,
       "eocBrEPProductName": eocBrEPProductName,
       "eocBrEPOnlineStatus": eocBrEPOnlineStatus,
       "eocBrEPHostCountLimit": eocBrEPHostCountLimit,
       "eocBrEPWorkingPrivacyKeyMatched": eocBrEPWorkingPrivacyKeyMatched,
       "eocBrEPDrvWorkingVersion": eocBrEPDrvWorkingVersion,
       "eocBrEPDrvUploadVersion": eocBrEPDrvUploadVersion,
       "eocBrEPDrvUpgradeAction": eocBrEPDrvUpgradeAction,
       "eocBrEPDrvUpgradeStatus": eocBrEPDrvUpgradeStatus,
       "eocBrEPPhyDiagAction": eocBrEPPhyDiagAction,
       "eocBrEPPhyDiagStatus": eocBrEPPhyDiagStatus,
       "eocBrEPDiagDnLinkResult": eocBrEPDiagDnLinkResult,
       "eocBrEPDiagUpLinkResult": eocBrEPDiagUpLinkResult,
       "eocBrEPOnlineDiagAction": eocBrEPOnlineDiagAction,
       "eocBrEPOnlineDiagStatus": eocBrEPOnlineDiagStatus,
       "eocBrEPRowStatus": eocBrEPRowStatus,
       "eocBrEPMacInfoTable": eocBrEPMacInfoTable,
       "eocBrEPMacInfoEntry": eocBrEPMacInfoEntry,
       "eocBrEP-Index": eocBrEP_Index,
       "eocBrEP-MacType": eocBrEP_MacType,
       "eocBrEP-EPMac": eocBrEP_EPMac,
       "eocBrEP-HostMac": eocBrEP_HostMac,
       "eocBrEPNetPerTable": eocBrEPNetPerTable,
       "eocBrEPNetPerEntry": eocBrEPNetPerEntry,
       "eocBrEPNetPerIndex": eocBrEPNetPerIndex,
       "eocBrEPNetPerEPMac": eocBrEPNetPerEPMac,
       "eocBrEPNetPerDnLinkSNR": eocBrEPNetPerDnLinkSNR,
       "eocBrEPNetPerUpLinkSNR": eocBrEPNetPerUpLinkSNR,
       "eocBrEPNetPerDnLinkRate": eocBrEPNetPerDnLinkRate,
       "eocBrEPNetPerUpLinkRate": eocBrEPNetPerUpLinkRate,
       "eocBrEPNetPerDnLinkRxPwr": eocBrEPNetPerDnLinkRxPwr,
       "eocBrEPNetPerUpLinkRxPwr": eocBrEPNetPerUpLinkRxPwr,
       "eocBrEPScanMacInfo": eocBrEPScanMacInfo,
       "eocBrEPScanMacInfoAction": eocBrEPScanMacInfoAction,
       "eocBrEPScanMacInfoStatus": eocBrEPScanMacInfoStatus,
       "eocBrEPPayloadEncodeTable": eocBrEPPayloadEncodeTable,
       "eocBrEPPayloadEncodeEntry": eocBrEPPayloadEncodeEntry,
       "eocBrEPPayloadEncodeIndex": eocBrEPPayloadEncodeIndex,
       "eocBrEPPayloadEncodeEPMac": eocBrEPPayloadEncodeEPMac,
       "eocBrEPPayloadEncodeDnRate": eocBrEPPayloadEncodeDnRate,
       "eocBrEPPayloadEncodeUpRate": eocBrEPPayloadEncodeUpRate,
       "eocBrTFTPGroup": eocBrTFTPGroup,
       "eocBrTFTPServerIPAddress": eocBrTFTPServerIPAddress,
       "eocBrTFTPFilename": eocBrTFTPFilename,
       "eocBrTFTPGetAction": eocBrTFTPGetAction,
       "eocBrTFTPGetStatus": eocBrTFTPGetStatus,
       "eocBrTFTPExtensionPath": eocBrTFTPExtensionPath,
       "eocBrTFTPServer": eocBrTFTPServer,
       "eocBrEtherGroup": eocBrEtherGroup,
       "eocBrEtherPort": eocBrEtherPort,
       "eocBrPortPropTable": eocBrPortPropTable,
       "eocBrPortPropEntry": eocBrPortPropEntry,
       "eocBrPortPropPID": eocBrPortPropPID,
       "eocBrPortPropType": eocBrPortPropType,
       "eocBrPortPropConfig": eocBrPortPropConfig,
       "eocBrPortPropLinkStatus": eocBrPortPropLinkStatus,
       "eocBrPortPropInRateCtrl": eocBrPortPropInRateCtrl,
       "eocBrPortPropInRate": eocBrPortPropInRate,
       "eocBrPortPropOutRateCtrl": eocBrPortPropOutRateCtrl,
       "eocBrPortPropOutRate": eocBrPortPropOutRate,
       "eocBrPortStatsTable": eocBrPortStatsTable,
       "eocBrPortStatsEntry": eocBrPortStatsEntry,
       "eocBrPortStatsPID": eocBrPortStatsPID,
       "eocBrPortStatsType": eocBrPortStatsType,
       "eocBrPortStatsRxPkts": eocBrPortStatsRxPkts,
       "eocBrPortStatsRxBytes": eocBrPortStatsRxBytes,
       "eocBrPortStatsTxPkts": eocBrPortStatsTxPkts,
       "eocBrPortStatsTxBytes": eocBrPortStatsTxBytes,
       "eocBrPortStatsCollisions": eocBrPortStatsCollisions,
       "eocBrPortStatsErrors": eocBrPortStatsErrors,
       "eocBrStatsCtrl": eocBrStatsCtrl,
       "eocBrStatsCtrlReset": eocBrStatsCtrlReset,
       "eocBrStatsCtrlRefresh": eocBrStatsCtrlRefresh,
       "eocBrEtherQoS": eocBrEtherQoS,
       "eocBrTcpUdpPriTable": eocBrTcpUdpPriTable,
       "eocBrTcpUdpPriEntry": eocBrTcpUdpPriEntry,
       "eocBrTcpUdpRuleNum": eocBrTcpUdpRuleNum,
       "eocBrTcpUdpEnableCtrl": eocBrTcpUdpEnableCtrl,
       "eocBrTcpUdpPortNum": eocBrTcpUdpPortNum,
       "eocBrTcpUdpMappedQueue": eocBrTcpUdpMappedQueue,
       "eocBrQueueSchType": eocBrQueueSchType,
       "eocBrPriSchemeSelect": eocBrPriSchemeSelect,
       "eocBrEtherIGMPSnoop": eocBrEtherIGMPSnoop,
       "eocBrIGMPSnoopEnableCtrl": eocBrIGMPSnoopEnableCtrl,
       "eocBrEtherTagVLAN": eocBrEtherTagVLAN,
       "eocBrTagVLANEnableCtrl": eocBrTagVLANEnableCtrl,
       "eocBrTagPortTable": eocBrTagPortTable,
       "eocBrTagPortEntry": eocBrTagPortEntry,
       "eocBrTagPortPID": eocBrTagPortPID,
       "eocBrTagPortType": eocBrTagPortType,
       "eocBrTagPortPriority": eocBrTagPortPriority,
       "eocBrTagPortVID": eocBrTagPortVID,
       "eocBrTagPortInRule": eocBrTagPortInRule,
       "eocBrTagPortOutRule": eocBrTagPortOutRule,
       "eocBrEtherCascadeLan": eocBrEtherCascadeLan,
       "eocBrCascadeMode": eocBrCascadeMode,
       "eocBrEPEtherGroup": eocBrEPEtherGroup,
       "eocBrEPDesignate": eocBrEPDesignate,
       "eocBrEPDesignateTable": eocBrEPDesignateTable,
       "eocBrEPDesignateEntry": eocBrEPDesignateEntry,
       "eocBrEPDesignateEPIndex": eocBrEPDesignateEPIndex,
       "eocBrEPDesignateEPMac": eocBrEPDesignateEPMac,
       "eocBrEPDesignateOnlineStatus": eocBrEPDesignateOnlineStatus,
       "eocBrEPDesignateDeviceVersion": eocBrEPDesignateDeviceVersion,
       "eocBrEPDesignateIsSmart": eocBrEPDesignateIsSmart,
       "eocBrEPDesignateIsTarget": eocBrEPDesignateIsTarget,
       "eocBrEPEtherPort": eocBrEPEtherPort,
       "eocBrEPPortPropTable": eocBrEPPortPropTable,
       "eocBrEPPortPropEntry": eocBrEPPortPropEntry,
       "eocBrEPPortPropEPIndex": eocBrEPPortPropEPIndex,
       "eocBrEPPortPropPID": eocBrEPPortPropPID,
       "eocBrEPPortPropEPMac": eocBrEPPortPropEPMac,
       "eocBrEPPortPropType": eocBrEPPortPropType,
       "eocBrEPPortPropConfig": eocBrEPPortPropConfig,
       "eocBrEPPortPropLinkStatus": eocBrEPPortPropLinkStatus,
       "eocBrEPPortPropFlowCtrl": eocBrEPPortPropFlowCtrl,
       "eocBrEPPortPropInRateCtrl": eocBrEPPortPropInRateCtrl,
       "eocBrEPPortPropInRate": eocBrEPPortPropInRate,
       "eocBrEPPortPropOutRateCtrl": eocBrEPPortPropOutRateCtrl,
       "eocBrEPPortPropOutRate": eocBrEPPortPropOutRate,
       "eocBrEPPortPropEnableCtrl": eocBrEPPortPropEnableCtrl,
       "eocBrEPPortStatsTable": eocBrEPPortStatsTable,
       "eocBrEPPortStatsEntry": eocBrEPPortStatsEntry,
       "eocBrEPPortStatsEPIndex": eocBrEPPortStatsEPIndex,
       "eocBrEPPortStatsPID": eocBrEPPortStatsPID,
       "eocBrEPPortStatsEPMac": eocBrEPPortStatsEPMac,
       "eocBrEPPortStatsType": eocBrEPPortStatsType,
       "eocBrEPPortStatsRxPkts": eocBrEPPortStatsRxPkts,
       "eocBrEPPortStatsRxBytes": eocBrEPPortStatsRxBytes,
       "eocBrEPPortStatsTxPkts": eocBrEPPortStatsTxPkts,
       "eocBrEPPortStatsTxBytes": eocBrEPPortStatsTxBytes,
       "eocBrEPPortStatsCollisions": eocBrEPPortStatsCollisions,
       "eocBrEPPortStatsErrors": eocBrEPPortStatsErrors,
       "eocBrEPStatsCtrlTable": eocBrEPStatsCtrlTable,
       "eocBrEPStatsCtrlEntry": eocBrEPStatsCtrlEntry,
       "eocBrEPStatsCtrlEPIndex": eocBrEPStatsCtrlEPIndex,
       "eocBrEPStatsCtrlEPMac": eocBrEPStatsCtrlEPMac,
       "eocBrEPStatsCtrlReset": eocBrEPStatsCtrlReset,
       "eocBrEPStatsCtrlRefresh": eocBrEPStatsCtrlRefresh,
       "eocBrEPEtherQoS": eocBrEPEtherQoS,
       "eocBrEPTcpUdpPriTable": eocBrEPTcpUdpPriTable,
       "eocBrEPTcpUdpPriEntry": eocBrEPTcpUdpPriEntry,
       "eocBrEPTcpUdpEPIndex": eocBrEPTcpUdpEPIndex,
       "eocBrEPTcpUdpRuleNum": eocBrEPTcpUdpRuleNum,
       "eocBrEPTcpUdpEPMac": eocBrEPTcpUdpEPMac,
       "eocBrEPTcpUdpEnableCtrl": eocBrEPTcpUdpEnableCtrl,
       "eocBrEPTcpUdpPortNum": eocBrEPTcpUdpPortNum,
       "eocBrEPTcpUdpMappedQueue": eocBrEPTcpUdpMappedQueue,
       "eocBrEPQueueSchTable": eocBrEPQueueSchTable,
       "eocBrEPQueueSchEntry": eocBrEPQueueSchEntry,
       "eocBrEPQueueSchEPIndex": eocBrEPQueueSchEPIndex,
       "eocBrEPQueueSchEPMac": eocBrEPQueueSchEPMac,
       "eocBrEPQueueSchType": eocBrEPQueueSchType,
       "eocBrEPPriSchemeTable": eocBrEPPriSchemeTable,
       "eocBrEPPriSchemeEntry": eocBrEPPriSchemeEntry,
       "eocBrEPPriSchemeEPIndex": eocBrEPPriSchemeEPIndex,
       "eocBrEPPriSchemeEPMac": eocBrEPPriSchemeEPMac,
       "eocBrEPPriSchemeSelect": eocBrEPPriSchemeSelect,
       "eocBrEPEtherIGMPSnoop": eocBrEPEtherIGMPSnoop,
       "eocBrEPIGMPSnoopTable": eocBrEPIGMPSnoopTable,
       "eocBrEPIGMPSnoopEntry": eocBrEPIGMPSnoopEntry,
       "eocBrEPIGMPSnoopEPIndex": eocBrEPIGMPSnoopEPIndex,
       "eocBrEPIGMPSnoopEPMac": eocBrEPIGMPSnoopEPMac,
       "eocBrEPIGMPSnoopEnableCtrl": eocBrEPIGMPSnoopEnableCtrl,
       "eocBrEPEtherTagVLAN": eocBrEPEtherTagVLAN,
       "eocBrEPTagVLANCtrlTable": eocBrEPTagVLANCtrlTable,
       "eocBrEPTagVLANCtrlEntry": eocBrEPTagVLANCtrlEntry,
       "eocBrEPTagVLANEPIndex": eocBrEPTagVLANEPIndex,
       "eocBrEPTagVLANEPMac": eocBrEPTagVLANEPMac,
       "eocBrEPTagVLANEnableCtrl": eocBrEPTagVLANEnableCtrl,
       "eocBrEPTagPortTable": eocBrEPTagPortTable,
       "eocBrEPTagPortEntry": eocBrEPTagPortEntry,
       "eocBrEPTagPortEPIndex": eocBrEPTagPortEPIndex,
       "eocBrEPTagPortPID": eocBrEPTagPortPID,
       "eocBrEPTagPortEPMac": eocBrEPTagPortEPMac,
       "eocBrEPTagPortType": eocBrEPTagPortType,
       "eocBrEPTagPortPriority": eocBrEPTagPortPriority,
       "eocBrEPTagPortVID": eocBrEPTagPortVID,
       "eocBrEPTagPortInRule": eocBrEPTagPortInRule,
       "eocBrEPTagPortOutRule": eocBrEPTagPortOutRule,
       "eocBrEPCtrl": eocBrEPCtrl,
       "eocBrEPCtrlTable": eocBrEPCtrlTable,
       "eocBrEPCtrlEntry": eocBrEPCtrlEntry,
       "eocBrEPCtrlEPIndex": eocBrEPCtrlEPIndex,
       "eocBrEPCtrlEPMac": eocBrEPCtrlEPMac,
       "eocBrEPCtrlEtherDefault": eocBrEPCtrlEtherDefault,
       "eocBrEPCtrlReboot": eocBrEPCtrlReboot,
       "eocBrEPHostMacFilter": eocBrEPHostMacFilter,
       "eocBrEPHostMacFilterTable": eocBrEPHostMacFilterTable,
       "eocBrEPHostMacFilterEntry": eocBrEPHostMacFilterEntry,
       "eocBrEPHostMacFilterEPIndex": eocBrEPHostMacFilterEPIndex,
       "eocBrEPHostMacFilterSetNum": eocBrEPHostMacFilterSetNum,
       "eocBrEPHostMacFilterEPMac": eocBrEPHostMacFilterEPMac,
       "eocBrEPHostMacFilterEnableCtrl": eocBrEPHostMacFilterEnableCtrl,
       "eocBrEPHostMacFilterHostMac": eocBrEPHostMacFilterHostMac,
       "eoc350BrNotification": eoc350BrNotification,
       "eocBrHttpLoginNotification": eocBrHttpLoginNotification,
       "eocBrHttpLogoutNotification": eocBrHttpLogoutNotification,
       "eocBrHttpLoginAuthFailedNotification": eocBrHttpLoginAuthFailedNotification,
       "eocBrTelnetLoginNotification": eocBrTelnetLoginNotification,
       "eocBrTelnetLogoutNotification": eocBrTelnetLogoutNotification,
       "eocBrTelnetLoginAuthFailedNotification": eocBrTelnetLoginAuthFailedNotification,
       "eocBrSystemFwUpgradeNotification": eocBrSystemFwUpgradeNotification,
       "eocBrDhcpClientAckNotification": eocBrDhcpClientAckNotification,
       "eocBrHostDhcpClientAckNotification": eocBrHostDhcpClientAckNotification,
       "eocBrAutoConfigTFTPGetOkNotification": eocBrAutoConfigTFTPGetOkNotification,
       "eocBrAutoConfigTFTPGetErrorNotification": eocBrAutoConfigTFTPGetErrorNotification,
       "eocBrHTTPGetNotification": eocBrHTTPGetNotification,
       "eocBrMasterDrvUpgradeNotification": eocBrMasterDrvUpgradeNotification,
       "eocBrEPDrvUpgradeNotification": eocBrEPDrvUpgradeNotification,
       "eocBrEPOnlineStatusNotification": eocBrEPOnlineStatusNotification,
       "eocBrEPDiagResultNotification": eocBrEPDiagResultNotification,
       "eocBrTFTPGetOkNotification": eocBrTFTPGetOkNotification,
       "eocBrTFTPGetErrorNotification": eocBrTFTPGetErrorNotification}
)
