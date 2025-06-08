# SNMP MIB module (RARITANSX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/raritan_13742/RARITANSX-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 21:26:10 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sxMIBIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 2, 15)
)
if mibBuilder.loadTexts:
    sxMIBIdentity.setRevisions(
        ("2007-04-30 15:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Raritan_ObjectIdentity = ObjectIdentity
raritan = _Raritan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742)
)
_Raritansx_ObjectIdentity = ObjectIdentity
raritansx = _Raritansx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 2)
)
_Raritansxnotifications_ObjectIdentity = ObjectIdentity
raritansxnotifications = _Raritansxnotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0)
)
_SxObjectImageCurrentVersion_Type = DisplayString
_SxObjectImageCurrentVersion_Object = MibScalar
sxObjectImageCurrentVersion = _SxObjectImageCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 1),
    _SxObjectImageCurrentVersion_Type()
)
sxObjectImageCurrentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sxObjectImageCurrentVersion.setStatus("current")
_SxActiveUsersTable_Object = MibTable
sxActiveUsersTable = _SxActiveUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 2)
)
if mibBuilder.loadTexts:
    sxActiveUsersTable.setStatus("current")
_SxActiveUsersEntry_Object = MibTableRow
sxActiveUsersEntry = _SxActiveUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 2, 1)
)
sxActiveUsersEntry.setIndexNames(
    (0, "RARITANSX-MIB", "sxActiveUserName"),
)
if mibBuilder.loadTexts:
    sxActiveUsersEntry.setStatus("current")
_SxActiveUserName_Type = DisplayString
_SxActiveUserName_Object = MibTableColumn
sxActiveUserName = _SxActiveUserName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 2, 1, 1),
    _SxActiveUserName_Type()
)
sxActiveUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxActiveUserName.setStatus("current")
_SxLoginTime_Type = TimeTicks
_SxLoginTime_Object = MibTableColumn
sxLoginTime = _SxLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 2, 1, 2),
    _SxLoginTime_Type()
)
sxLoginTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxLoginTime.setStatus("current")
_SxPortConnected_Type = DisplayString
_SxPortConnected_Object = MibTableColumn
sxPortConnected = _SxPortConnected_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 2, 1, 3),
    _SxPortConnected_Type()
)
sxPortConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxPortConnected.setStatus("current")
_SxPortName_Type = DisplayString
_SxPortName_Object = MibTableColumn
sxPortName = _SxPortName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 2, 1, 4),
    _SxPortName_Type()
)
sxPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxPortName.setStatus("current")
_SxUserLoggingFromIP_Type = IpAddress
_SxUserLoggingFromIP_Object = MibTableColumn
sxUserLoggingFromIP = _SxUserLoggingFromIP_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 2, 1, 5),
    _SxUserLoggingFromIP_Type()
)
sxUserLoggingFromIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxUserLoggingFromIP.setStatus("current")


class _SxApplicationType_Type(Integer32):
    """Custom type sxApplicationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("raritanConsole", 1),
          ("powerBoard", 2),
          ("ipmi", 3))
    )


_SxApplicationType_Type.__name__ = "Integer32"
_SxApplicationType_Object = MibTableColumn
sxApplicationType = _SxApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 2, 1, 6),
    _SxApplicationType_Type()
)
sxApplicationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxApplicationType.setStatus("current")


class _SxAuthenticationType_Type(Integer32):
    """Custom type sxAuthenticationType based on Integer32"""
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
        *(("radius", 1),
          ("ldap", 2),
          ("activeDirectory", 3),
          ("local", 4),
          ("tacacs", 5),
          ("kerberos", 6),
          ("other", 7))
    )


_SxAuthenticationType_Type.__name__ = "Integer32"
_SxAuthenticationType_Object = MibTableColumn
sxAuthenticationType = _SxAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 2, 1, 7),
    _SxAuthenticationType_Type()
)
sxAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxAuthenticationType.setStatus("current")


class _SxInterfaceType_Type(Integer32):
    """Custom type sxInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("modem", 2))
    )


_SxInterfaceType_Type.__name__ = "Integer32"
_SxInterfaceType_Object = MibTableColumn
sxInterfaceType = _SxInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 2, 1, 8),
    _SxInterfaceType_Type()
)
sxInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxInterfaceType.setStatus("current")
_SxObjectName_Type = DisplayString
_SxObjectName_Object = MibScalar
sxObjectName = _SxObjectName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 3),
    _SxObjectName_Type()
)
sxObjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxObjectName.setStatus("current")
_SxObjectInstance_Type = DisplayString
_SxObjectInstance_Object = MibScalar
sxObjectInstance = _SxObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 4),
    _SxObjectInstance_Type()
)
sxObjectInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxObjectInstance.setStatus("current")
_SxUserName_Type = DisplayString
_SxUserName_Object = MibScalar
sxUserName = _SxUserName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 5),
    _SxUserName_Type()
)
sxUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxUserName.setStatus("current")
_SxUserSessionID_Type = DisplayString
_SxUserSessionID_Object = MibScalar
sxUserSessionID = _SxUserSessionID_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 6),
    _SxUserSessionID_Type()
)
sxUserSessionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxUserSessionID.setStatus("current")
_SxUserNameInitiated_Type = DisplayString
_SxUserNameInitiated_Object = MibScalar
sxUserNameInitiated = _SxUserNameInitiated_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 7),
    _SxUserNameInitiated_Type()
)
sxUserNameInitiated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxUserNameInitiated.setStatus("current")
_SxUserNameTerminated_Type = DisplayString
_SxUserNameTerminated_Object = MibScalar
sxUserNameTerminated = _SxUserNameTerminated_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 8),
    _SxUserNameTerminated_Type()
)
sxUserNameTerminated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxUserNameTerminated.setStatus("current")
_SxImageType_Type = DisplayString
_SxImageType_Object = MibScalar
sxImageType = _SxImageType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 9),
    _SxImageType_Type()
)
sxImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxImageType.setStatus("current")
_SxImageVersion_Type = DisplayString
_SxImageVersion_Object = MibScalar
sxImageVersion = _SxImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 10),
    _SxImageVersion_Type()
)
sxImageVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxImageVersion.setStatus("current")


class _SxImageVersionStatus_Type(Integer32):
    """Custom type sxImageVersionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_SxImageVersionStatus_Type.__name__ = "Integer32"
_SxImageVersionStatus_Object = MibScalar
sxImageVersionStatus = _SxImageVersionStatus_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 11),
    _SxImageVersionStatus_Type()
)
sxImageVersionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxImageVersionStatus.setStatus("current")
_SxUserWhoAdded_Type = DisplayString
_SxUserWhoAdded_Object = MibScalar
sxUserWhoAdded = _SxUserWhoAdded_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 12),
    _SxUserWhoAdded_Type()
)
sxUserWhoAdded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxUserWhoAdded.setStatus("current")
_SxUserWhoDeleted_Type = DisplayString
_SxUserWhoDeleted_Object = MibScalar
sxUserWhoDeleted = _SxUserWhoDeleted_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 13),
    _SxUserWhoDeleted_Type()
)
sxUserWhoDeleted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxUserWhoDeleted.setStatus("current")
_SxUserWhoModified_Type = DisplayString
_SxUserWhoModified_Object = MibScalar
sxUserWhoModified = _SxUserWhoModified_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 14),
    _SxUserWhoModified_Type()
)
sxUserWhoModified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxUserWhoModified.setStatus("current")
_SxPortNumber_Type = DisplayString
_SxPortNumber_Object = MibScalar
sxPortNumber = _SxPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 16),
    _SxPortNumber_Type()
)
sxPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxPortNumber.setStatus("current")
_SxAlertString_Type = DisplayString
_SxAlertString_Object = MibScalar
sxAlertString = _SxAlertString_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 17),
    _SxAlertString_Type()
)
sxAlertString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxAlertString.setStatus("current")
_SxIPaddress_Type = DisplayString
_SxIPaddress_Object = MibScalar
sxIPaddress = _SxIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 19),
    _SxIPaddress_Type()
)
sxIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxIPaddress.setStatus("current")


class _SxInterface_Type(Integer32):
    """Custom type sxInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("modem", 2))
    )


_SxInterface_Type.__name__ = "Integer32"
_SxInterface_Object = MibScalar
sxInterface = _SxInterface_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 20),
    _SxInterface_Type()
)
sxInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxInterface.setStatus("current")


class _SxAppType_Type(Integer32):
    """Custom type sxAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("raritanConsole", 1),
          ("powerBoard", 2),
          ("ipmi", 3))
    )


_SxAppType_Type.__name__ = "Integer32"
_SxAppType_Object = MibScalar
sxAppType = _SxAppType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 21),
    _SxAppType_Type()
)
sxAppType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxAppType.setStatus("current")


class _SxAuthType_Type(Integer32):
    """Custom type sxAuthType based on Integer32"""
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
        *(("radius", 1),
          ("ldap", 2),
          ("activeDirectory", 3),
          ("local", 4),
          ("tacacs", 5),
          ("kerberos", 6),
          ("other", 7))
    )


_SxAuthType_Type.__name__ = "Integer32"
_SxAuthType_Object = MibScalar
sxAuthType = _SxAuthType_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 22),
    _SxAuthType_Type()
)
sxAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxAuthType.setStatus("current")


class _SxEthernetInterface_Type(Integer32):
    """Custom type sxEthernetInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lan0", 0),
          ("lan1", 1))
    )


_SxEthernetInterface_Type.__name__ = "Integer32"
_SxEthernetInterface_Object = MibScalar
sxEthernetInterface = _SxEthernetInterface_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 23),
    _SxEthernetInterface_Type()
)
sxEthernetInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxEthernetInterface.setStatus("current")


class _SxPowerPort_Type(Integer32):
    """Custom type sxPowerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("psu0", 0),
          ("psu1", 1))
    )


_SxPowerPort_Type.__name__ = "Integer32"
_SxPowerPort_Object = MibScalar
sxPowerPort = _SxPowerPort_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 24),
    _SxPowerPort_Type()
)
sxPowerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxPowerPort.setStatus("current")


class _SxDirectAccessAction_Type(Integer32):
    """Custom type sxDirectAccessAction based on Integer32"""
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


_SxDirectAccessAction_Type.__name__ = "Integer32"
_SxDirectAccessAction_Object = MibScalar
sxDirectAccessAction = _SxDirectAccessAction_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 25),
    _SxDirectAccessAction_Type()
)
sxDirectAccessAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxDirectAccessAction.setStatus("current")


class _SxBackUpRestoreAction_Type(Integer32):
    """Custom type sxBackUpRestoreAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("backup", 0),
          ("restore", 1))
    )


_SxBackUpRestoreAction_Type.__name__ = "Integer32"
_SxBackUpRestoreAction_Object = MibScalar
sxBackUpRestoreAction = _SxBackUpRestoreAction_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 26),
    _SxBackUpRestoreAction_Type()
)
sxBackUpRestoreAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxBackUpRestoreAction.setStatus("current")


class _SxTargetConnectionStatus_Type(Integer32):
    """Custom type sxTargetConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_SxTargetConnectionStatus_Type.__name__ = "Integer32"
_SxTargetConnectionStatus_Object = MibScalar
sxTargetConnectionStatus = _SxTargetConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 27),
    _SxTargetConnectionStatus_Type()
)
sxTargetConnectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxTargetConnectionStatus.setStatus("current")
_SxCertificateAuthorityName_Type = DisplayString
_SxCertificateAuthorityName_Object = MibScalar
sxCertificateAuthorityName = _SxCertificateAuthorityName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 28),
    _SxCertificateAuthorityName_Type()
)
sxCertificateAuthorityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxCertificateAuthorityName.setStatus("current")


class _SxStatus_Type(Integer32):
    """Custom type sxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2))
    )


_SxStatus_Type.__name__ = "Integer32"
_SxStatus_Object = MibScalar
sxStatus = _SxStatus_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 29),
    _SxStatus_Type()
)
sxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxStatus.setStatus("current")


class _SxAction_Type(Integer32):
    """Custom type sxAction based on Integer32"""
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


_SxAction_Type.__name__ = "Integer32"
_SxAction_Object = MibScalar
sxAction = _SxAction_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 30),
    _SxAction_Type()
)
sxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxAction.setStatus("current")


class _SxBannerAction_Type(Integer32):
    """Custom type sxBannerAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("declined", 0),
          ("accepted", 1))
    )


_SxBannerAction_Type.__name__ = "Integer32"
_SxBannerAction_Object = MibScalar
sxBannerAction = _SxBannerAction_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 31),
    _SxBannerAction_Type()
)
sxBannerAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxBannerAction.setStatus("current")


class _SxPowerAction_Type(Integer32):
    """Custom type sxPowerAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cycle", 0),
          ("on", 1),
          ("off", 2))
    )


_SxPowerAction_Type.__name__ = "Integer32"
_SxPowerAction_Object = MibScalar
sxPowerAction = _SxPowerAction_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 32),
    _SxPowerAction_Type()
)
sxPowerAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxPowerAction.setStatus("current")
_SxDeviceName_Type = DisplayString
_SxDeviceName_Object = MibScalar
sxDeviceName = _SxDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 13742, 2, 33),
    _SxDeviceName_Type()
)
sxDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sxDeviceName.setStatus("current")
_SxMibConformance_ObjectIdentity = ObjectIdentity
sxMibConformance = _SxMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9)
)
_SxMibCompliances_ObjectIdentity = ObjectIdentity
sxMibCompliances = _SxMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1)
)
_SxMibGroups_ObjectIdentity = ObjectIdentity
sxMibGroups = _SxMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2)
)

# Managed Objects groups

sxMibBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2, 1)
)
sxMibBasicGroup.setObjects(
      *(("RARITANSX-MIB", "sxObjectImageCurrentVersion"),
        ("RARITANSX-MIB", "sxActiveUserName"),
        ("RARITANSX-MIB", "sxLoginTime"),
        ("RARITANSX-MIB", "sxPortConnected"),
        ("RARITANSX-MIB", "sxPortName"),
        ("RARITANSX-MIB", "sxUserLoggingFromIP"),
        ("RARITANSX-MIB", "sxApplicationType"),
        ("RARITANSX-MIB", "sxAuthenticationType"),
        ("RARITANSX-MIB", "sxInterfaceType"),
        ("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxUserSessionID"),
        ("RARITANSX-MIB", "sxUserNameInitiated"),
        ("RARITANSX-MIB", "sxUserNameTerminated"),
        ("RARITANSX-MIB", "sxImageType"),
        ("RARITANSX-MIB", "sxImageVersion"),
        ("RARITANSX-MIB", "sxImageVersionStatus"),
        ("RARITANSX-MIB", "sxUserWhoAdded"),
        ("RARITANSX-MIB", "sxUserWhoDeleted"),
        ("RARITANSX-MIB", "sxUserWhoModified"),
        ("RARITANSX-MIB", "sxPortNumber"),
        ("RARITANSX-MIB", "sxAlertString"),
        ("RARITANSX-MIB", "sxIPaddress"),
        ("RARITANSX-MIB", "sxInterface"),
        ("RARITANSX-MIB", "sxAppType"),
        ("RARITANSX-MIB", "sxAuthType"),
        ("RARITANSX-MIB", "sxEthernetInterface"),
        ("RARITANSX-MIB", "sxPowerPort"),
        ("RARITANSX-MIB", "sxDirectAccessAction"),
        ("RARITANSX-MIB", "sxBackUpRestoreAction"),
        ("RARITANSX-MIB", "sxTargetConnectionStatus"),
        ("RARITANSX-MIB", "sxCertificateAuthorityName"),
        ("RARITANSX-MIB", "sxStatus"),
        ("RARITANSX-MIB", "sxAction"),
        ("RARITANSX-MIB", "sxBannerAction"),
        ("RARITANSX-MIB", "sxPowerAction"),
        ("RARITANSX-MIB", "sxDeviceName"))
)
if mibBuilder.loadTexts:
    sxMibBasicGroup.setStatus("current")


# Notification objects

sxRebootStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 1)
)
sxRebootStarted.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"))
)
if mibBuilder.loadTexts:
    sxRebootStarted.setStatus(
        "current"
    )

sxRebootCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 2)
)
sxRebootCompleted.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"))
)
if mibBuilder.loadTexts:
    sxRebootCompleted.setStatus(
        "current"
    )

sxUserLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 3)
)
sxUserLogin.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxIPaddress"),
        ("RARITANSX-MIB", "sxInterface"))
)
if mibBuilder.loadTexts:
    sxUserLogin.setStatus(
        "current"
    )

sxUserLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 4)
)
sxUserLogout.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxIPaddress"),
        ("RARITANSX-MIB", "sxInterface"))
)
if mibBuilder.loadTexts:
    sxUserLogout.setStatus(
        "current"
    )

sxSerialSessionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 5)
)
sxSerialSessionStarted.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxUserSessionID"),
        ("RARITANSX-MIB", "sxPortName"),
        ("RARITANSX-MIB", "sxPortConnected"),
        ("RARITANSX-MIB", "sxAuthType"),
        ("RARITANSX-MIB", "sxAppType"))
)
if mibBuilder.loadTexts:
    sxSerialSessionStarted.setStatus(
        "current"
    )

sxSerialSessionStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 6)
)
sxSerialSessionStopped.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxUserSessionID"),
        ("RARITANSX-MIB", "sxPortName"),
        ("RARITANSX-MIB", "sxPortConnected"),
        ("RARITANSX-MIB", "sxAuthType"),
        ("RARITANSX-MIB", "sxAppType"))
)
if mibBuilder.loadTexts:
    sxSerialSessionStopped.setStatus(
        "current"
    )

sxSerialSessionTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 7)
)
sxSerialSessionTerminated.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserNameInitiated"),
        ("RARITANSX-MIB", "sxUserNameTerminated"),
        ("RARITANSX-MIB", "sxUserSessionID"))
)
if mibBuilder.loadTexts:
    sxSerialSessionTerminated.setStatus(
        "current"
    )

sxImageUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 8)
)
sxImageUpgradeStarted.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxImageType"),
        ("RARITANSX-MIB", "sxImageVersion"))
)
if mibBuilder.loadTexts:
    sxImageUpgradeStarted.setStatus(
        "current"
    )

sxImageUpgradeResults = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 9)
)
sxImageUpgradeResults.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxImageType"),
        ("RARITANSX-MIB", "sxImageVersion"),
        ("RARITANSX-MIB", "sxImageVersionStatus"))
)
if mibBuilder.loadTexts:
    sxImageUpgradeResults.setStatus(
        "current"
    )

sxUserAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 10)
)
sxUserAdded.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxUserWhoAdded"))
)
if mibBuilder.loadTexts:
    sxUserAdded.setStatus(
        "current"
    )

sxUserDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 11)
)
sxUserDeleted.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxUserWhoDeleted"))
)
if mibBuilder.loadTexts:
    sxUserDeleted.setStatus(
        "current"
    )

sxUserModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 12)
)
sxUserModified.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxUserWhoModified"))
)
if mibBuilder.loadTexts:
    sxUserModified.setStatus(
        "current"
    )

sxUserAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 13)
)
sxUserAuthenticationFailure.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"))
)
if mibBuilder.loadTexts:
    sxUserAuthenticationFailure.setStatus(
        "current"
    )

sxPortAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 14)
)
sxPortAlert.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxPortNumber"),
        ("RARITANSX-MIB", "sxAlertString"))
)
if mibBuilder.loadTexts:
    sxPortAlert.setStatus(
        "current"
    )

sxPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 15)
)
sxPowerSupplyFailure.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxPowerPort"))
)
if mibBuilder.loadTexts:
    sxPowerSupplyFailure.setStatus(
        "current"
    )

sxFailOverEthernet = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 16)
)
sxFailOverEthernet.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxEthernetInterface"))
)
if mibBuilder.loadTexts:
    sxFailOverEthernet.setStatus(
        "current"
    )

sxDirectAccessLockOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 17)
)
sxDirectAccessLockOut.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxDirectAccessAction"),
        ("RARITANSX-MIB", "sxUserName"))
)
if mibBuilder.loadTexts:
    sxDirectAccessLockOut.setStatus(
        "current"
    )

sxBackUpRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 18)
)
sxBackUpRestore.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxBackUpRestoreAction"),
        ("RARITANSX-MIB", "sxUserName"))
)
if mibBuilder.loadTexts:
    sxBackUpRestore.setStatus(
        "current"
    )

sxTargetConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 19)
)
sxTargetConnection.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxPortNumber"),
        ("RARITANSX-MIB", "sxTargetConnectionStatus"))
)
if mibBuilder.loadTexts:
    sxTargetConnection.setStatus(
        "current"
    )

sxForcedLogOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 20)
)
sxForcedLogOut.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserNameInitiated"),
        ("RARITANSX-MIB", "sxUserNameTerminated"))
)
if mibBuilder.loadTexts:
    sxForcedLogOut.setStatus(
        "current"
    )

sxStrongPasswordConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 21)
)
sxStrongPasswordConfig.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"))
)
if mibBuilder.loadTexts:
    sxStrongPasswordConfig.setStatus(
        "current"
    )

sxStrongPasswordExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 22)
)
sxStrongPasswordExpired.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"))
)
if mibBuilder.loadTexts:
    sxStrongPasswordExpired.setStatus(
        "current"
    )

sxStrongPasswordLoginExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 23)
)
sxStrongPasswordLoginExpired.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"))
)
if mibBuilder.loadTexts:
    sxStrongPasswordLoginExpired.setStatus(
        "current"
    )

sxStrongPasswordLoginDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 24)
)
sxStrongPasswordLoginDeactivated.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"))
)
if mibBuilder.loadTexts:
    sxStrongPasswordLoginDeactivated.setStatus(
        "current"
    )

sxSecurityBanner = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 25)
)
sxSecurityBanner.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"),
        ("RARITANSX-MIB", "sxBannerAction"))
)
if mibBuilder.loadTexts:
    sxSecurityBanner.setStatus(
        "current"
    )

sxStrongPasswordAccountLockedout = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 26)
)
sxStrongPasswordAccountLockedout.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxUserName"))
)
if mibBuilder.loadTexts:
    sxStrongPasswordAccountLockedout.setStatus(
        "current"
    )

sxFirewall = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 27)
)
sxFirewall.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxAction"))
)
if mibBuilder.loadTexts:
    sxFirewall.setStatus(
        "current"
    )

sxIPTables = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 29)
)
sxIPTables.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"))
)
if mibBuilder.loadTexts:
    sxIPTables.setStatus(
        "current"
    )

sxClientCertCAAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 30)
)
sxClientCertCAAdded.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxCertificateAuthorityName"))
)
if mibBuilder.loadTexts:
    sxClientCertCAAdded.setStatus(
        "current"
    )

sxClientCertCADeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 31)
)
sxClientCertCADeleted.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxCertificateAuthorityName"))
)
if mibBuilder.loadTexts:
    sxClientCertCADeleted.setStatus(
        "current"
    )

sxClientAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 32)
)
sxClientAuth.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxAction"))
)
if mibBuilder.loadTexts:
    sxClientAuth.setStatus(
        "current"
    )

sxClientCertCRLExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 33)
)
sxClientCertCRLExpired.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxCertificateAuthorityName"))
)
if mibBuilder.loadTexts:
    sxClientCertCRLExpired.setStatus(
        "current"
    )

sxClientCertCRLUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 34)
)
sxClientCertCRLUpdated.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxCertificateAuthorityName"),
        ("RARITANSX-MIB", "sxStatus"))
)
if mibBuilder.loadTexts:
    sxClientCertCRLUpdated.setStatus(
        "current"
    )

sxPowerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 13742, 2, 0, 35)
)
sxPowerChange.setObjects(
      *(("RARITANSX-MIB", "sxObjectName"),
        ("RARITANSX-MIB", "sxObjectInstance"),
        ("RARITANSX-MIB", "sxDeviceName"),
        ("RARITANSX-MIB", "sxPortConnected"),
        ("RARITANSX-MIB", "sxPowerAction"))
)
if mibBuilder.loadTexts:
    sxPowerChange.setStatus(
        "current"
    )


# Notifications groups

sxMibTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13742, 9, 2, 2)
)
sxMibTrapGroup.setObjects(
      *(("RARITANSX-MIB", "sxRebootStarted"),
        ("RARITANSX-MIB", "sxRebootCompleted"),
        ("RARITANSX-MIB", "sxUserLogin"),
        ("RARITANSX-MIB", "sxUserLogout"),
        ("RARITANSX-MIB", "sxSerialSessionStarted"),
        ("RARITANSX-MIB", "sxSerialSessionStopped"),
        ("RARITANSX-MIB", "sxSerialSessionTerminated"),
        ("RARITANSX-MIB", "sxImageUpgradeStarted"),
        ("RARITANSX-MIB", "sxImageUpgradeResults"),
        ("RARITANSX-MIB", "sxUserAdded"),
        ("RARITANSX-MIB", "sxUserDeleted"),
        ("RARITANSX-MIB", "sxUserModified"),
        ("RARITANSX-MIB", "sxUserAuthenticationFailure"),
        ("RARITANSX-MIB", "sxPortAlert"),
        ("RARITANSX-MIB", "sxPowerSupplyFailure"),
        ("RARITANSX-MIB", "sxFailOverEthernet"),
        ("RARITANSX-MIB", "sxDirectAccessLockOut"),
        ("RARITANSX-MIB", "sxBackUpRestore"),
        ("RARITANSX-MIB", "sxTargetConnection"),
        ("RARITANSX-MIB", "sxForcedLogOut"),
        ("RARITANSX-MIB", "sxStrongPasswordConfig"),
        ("RARITANSX-MIB", "sxStrongPasswordExpired"),
        ("RARITANSX-MIB", "sxStrongPasswordLoginExpired"),
        ("RARITANSX-MIB", "sxStrongPasswordLoginDeactivated"),
        ("RARITANSX-MIB", "sxSecurityBanner"),
        ("RARITANSX-MIB", "sxStrongPasswordAccountLockedout"),
        ("RARITANSX-MIB", "sxFirewall"),
        ("RARITANSX-MIB", "sxIPTables"),
        ("RARITANSX-MIB", "sxClientCertCAAdded"),
        ("RARITANSX-MIB", "sxClientCertCADeleted"),
        ("RARITANSX-MIB", "sxClientAuth"),
        ("RARITANSX-MIB", "sxClientCertCRLExpired"),
        ("RARITANSX-MIB", "sxClientCertCRLUpdated"),
        ("RARITANSX-MIB", "sxPowerChange"))
)
if mibBuilder.loadTexts:
    sxMibTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

sxMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13742, 9, 1, 1)
)
sxMibCompliance.setObjects(
      *(("RARITANSX-MIB", "sxMibBasicGroup"),
        ("RARITANSX-MIB", "sxMibTrapGroup"))
)
if mibBuilder.loadTexts:
    sxMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RARITANSX-MIB",
    **{"raritan": raritan,
       "raritansx": raritansx,
       "raritansxnotifications": raritansxnotifications,
       "sxRebootStarted": sxRebootStarted,
       "sxRebootCompleted": sxRebootCompleted,
       "sxUserLogin": sxUserLogin,
       "sxUserLogout": sxUserLogout,
       "sxSerialSessionStarted": sxSerialSessionStarted,
       "sxSerialSessionStopped": sxSerialSessionStopped,
       "sxSerialSessionTerminated": sxSerialSessionTerminated,
       "sxImageUpgradeStarted": sxImageUpgradeStarted,
       "sxImageUpgradeResults": sxImageUpgradeResults,
       "sxUserAdded": sxUserAdded,
       "sxUserDeleted": sxUserDeleted,
       "sxUserModified": sxUserModified,
       "sxUserAuthenticationFailure": sxUserAuthenticationFailure,
       "sxPortAlert": sxPortAlert,
       "sxPowerSupplyFailure": sxPowerSupplyFailure,
       "sxFailOverEthernet": sxFailOverEthernet,
       "sxDirectAccessLockOut": sxDirectAccessLockOut,
       "sxBackUpRestore": sxBackUpRestore,
       "sxTargetConnection": sxTargetConnection,
       "sxForcedLogOut": sxForcedLogOut,
       "sxStrongPasswordConfig": sxStrongPasswordConfig,
       "sxStrongPasswordExpired": sxStrongPasswordExpired,
       "sxStrongPasswordLoginExpired": sxStrongPasswordLoginExpired,
       "sxStrongPasswordLoginDeactivated": sxStrongPasswordLoginDeactivated,
       "sxSecurityBanner": sxSecurityBanner,
       "sxStrongPasswordAccountLockedout": sxStrongPasswordAccountLockedout,
       "sxFirewall": sxFirewall,
       "sxIPTables": sxIPTables,
       "sxClientCertCAAdded": sxClientCertCAAdded,
       "sxClientCertCADeleted": sxClientCertCADeleted,
       "sxClientAuth": sxClientAuth,
       "sxClientCertCRLExpired": sxClientCertCRLExpired,
       "sxClientCertCRLUpdated": sxClientCertCRLUpdated,
       "sxPowerChange": sxPowerChange,
       "sxObjectImageCurrentVersion": sxObjectImageCurrentVersion,
       "sxActiveUsersTable": sxActiveUsersTable,
       "sxActiveUsersEntry": sxActiveUsersEntry,
       "sxActiveUserName": sxActiveUserName,
       "sxLoginTime": sxLoginTime,
       "sxPortConnected": sxPortConnected,
       "sxPortName": sxPortName,
       "sxUserLoggingFromIP": sxUserLoggingFromIP,
       "sxApplicationType": sxApplicationType,
       "sxAuthenticationType": sxAuthenticationType,
       "sxInterfaceType": sxInterfaceType,
       "sxObjectName": sxObjectName,
       "sxObjectInstance": sxObjectInstance,
       "sxUserName": sxUserName,
       "sxUserSessionID": sxUserSessionID,
       "sxUserNameInitiated": sxUserNameInitiated,
       "sxUserNameTerminated": sxUserNameTerminated,
       "sxImageType": sxImageType,
       "sxImageVersion": sxImageVersion,
       "sxImageVersionStatus": sxImageVersionStatus,
       "sxUserWhoAdded": sxUserWhoAdded,
       "sxUserWhoDeleted": sxUserWhoDeleted,
       "sxUserWhoModified": sxUserWhoModified,
       "sxMIBIdentity": sxMIBIdentity,
       "sxPortNumber": sxPortNumber,
       "sxAlertString": sxAlertString,
       "sxIPaddress": sxIPaddress,
       "sxInterface": sxInterface,
       "sxAppType": sxAppType,
       "sxAuthType": sxAuthType,
       "sxEthernetInterface": sxEthernetInterface,
       "sxPowerPort": sxPowerPort,
       "sxDirectAccessAction": sxDirectAccessAction,
       "sxBackUpRestoreAction": sxBackUpRestoreAction,
       "sxTargetConnectionStatus": sxTargetConnectionStatus,
       "sxCertificateAuthorityName": sxCertificateAuthorityName,
       "sxStatus": sxStatus,
       "sxAction": sxAction,
       "sxBannerAction": sxBannerAction,
       "sxPowerAction": sxPowerAction,
       "sxDeviceName": sxDeviceName,
       "sxMibConformance": sxMibConformance,
       "sxMibCompliances": sxMibCompliances,
       "sxMibCompliance": sxMibCompliance,
       "sxMibGroups": sxMibGroups,
       "sxMibBasicGroup": sxMibBasicGroup,
       "sxMibTrapGroup": sxMibTrapGroup}
)
