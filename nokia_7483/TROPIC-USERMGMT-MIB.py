# SNMP MIB module (TROPIC-USERMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-USERMGMT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:59:16 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(tnSystemModules,
 tnUserMgmtMIB) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSystemModules",
    "tnUserMgmtMIB")


# MODULE-IDENTITY

tnUserMgmtMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tnUserMgmtMibModule.setRevisions(
        ("2008-04-11 12:00",
         "2009-04-07 12:00",
         "2009-04-30 12:00",
         "2009-05-05 12:00",
         "2009-05-06 12:00",
         "2009-05-27 12:00",
         "2009-05-30 12:00",
         "2009-06-04 12:00",
         "2009-06-07 12:00",
         "2009-06-09 12:00",
         "2009-06-11 12:00",
         "2009-06-12 12:00",
         "2009-07-03 12:00",
         "2009-07-07 12:00",
         "2010-10-28 12:00",
         "2011-06-15 12:00",
         "2011-08-12 12:00",
         "2013-04-19 12:00",
         "2013-05-21 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnUserMgmtConf_ObjectIdentity = ObjectIdentity
tnUserMgmtConf = _TnUserMgmtConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 1)
)
_TnUserMgmtGroups_ObjectIdentity = ObjectIdentity
tnUserMgmtGroups = _TnUserMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 1, 1)
)
_TnUserMgmtCompliances_ObjectIdentity = ObjectIdentity
tnUserMgmtCompliances = _TnUserMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 1, 2)
)
_TnUserMgmtObjs_ObjectIdentity = ObjectIdentity
tnUserMgmtObjs = _TnUserMgmtObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2)
)
_TnUserMgmtBasics_ObjectIdentity = ObjectIdentity
tnUserMgmtBasics = _TnUserMgmtBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1)
)
_TnUserTable_Object = MibTable
tnUserTable = _TnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tnUserTable.setStatus("current")
_TnUserEntry_Object = MibTableRow
tnUserEntry = _TnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1)
)
tnUserEntry.setIndexNames(
    (0, "TROPIC-USERMGMT-MIB", "tnUserName"),
)
if mibBuilder.loadTexts:
    tnUserEntry.setStatus("current")


class _TnUserName_Type(SnmpAdminString):
    """Custom type tnUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TnUserName_Type.__name__ = "SnmpAdminString"
_TnUserName_Object = MibTableColumn
tnUserName = _TnUserName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 1),
    _TnUserName_Type()
)
tnUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnUserName.setStatus("current")
_TnUserRowStatus_Type = RowStatus
_TnUserRowStatus_Object = MibTableColumn
tnUserRowStatus = _TnUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 2),
    _TnUserRowStatus_Type()
)
tnUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserRowStatus.setStatus("current")


class _TnUserAccessLevel_Type(Integer32):
    """Custom type tnUserAccessLevel based on Integer32"""
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
        *(("unknown", 1),
          ("administrator", 2),
          ("provisioner", 3),
          ("observer", 4),
          ("service", 5),
          ("crypto", 6))
    )


_TnUserAccessLevel_Type.__name__ = "Integer32"
_TnUserAccessLevel_Object = MibTableColumn
tnUserAccessLevel = _TnUserAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 3),
    _TnUserAccessLevel_Type()
)
tnUserAccessLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserAccessLevel.setStatus("current")


class _TnUserPassword_Type(SnmpAdminString):
    """Custom type tnUserPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TnUserPassword_Type.__name__ = "SnmpAdminString"
_TnUserPassword_Object = MibTableColumn
tnUserPassword = _TnUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 4),
    _TnUserPassword_Type()
)
tnUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserPassword.setStatus("current")
_TnUserLastLoginDateAndTime_Type = Unsigned32
_TnUserLastLoginDateAndTime_Object = MibTableColumn
tnUserLastLoginDateAndTime = _TnUserLastLoginDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 5),
    _TnUserLastLoginDateAndTime_Type()
)
tnUserLastLoginDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserLastLoginDateAndTime.setStatus("current")
_TnUserLastLoginTerminalIP_Type = SnmpAdminString
_TnUserLastLoginTerminalIP_Object = MibTableColumn
tnUserLastLoginTerminalIP = _TnUserLastLoginTerminalIP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 6),
    _TnUserLastLoginTerminalIP_Type()
)
tnUserLastLoginTerminalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserLastLoginTerminalIP.setStatus("current")
_TnUserNumberOfFailedLogins_Type = Unsigned32
_TnUserNumberOfFailedLogins_Object = MibTableColumn
tnUserNumberOfFailedLogins = _TnUserNumberOfFailedLogins_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 7),
    _TnUserNumberOfFailedLogins_Type()
)
tnUserNumberOfFailedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserNumberOfFailedLogins.setStatus("current")


class _TnUserSessionTimeout_Type(Unsigned32):
    """Custom type tnUserSessionTimeout based on Unsigned32"""
    defaultValue = 15


_TnUserSessionTimeout_Type.__name__ = "Unsigned32"
_TnUserSessionTimeout_Object = MibTableColumn
tnUserSessionTimeout = _TnUserSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 8),
    _TnUserSessionTimeout_Type()
)
tnUserSessionTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnUserSessionTimeout.setStatus("current")
_TnUserLastPasswordChangeDateAndTime_Type = Unsigned32
_TnUserLastPasswordChangeDateAndTime_Object = MibTableColumn
tnUserLastPasswordChangeDateAndTime = _TnUserLastPasswordChangeDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 9),
    _TnUserLastPasswordChangeDateAndTime_Type()
)
tnUserLastPasswordChangeDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserLastPasswordChangeDateAndTime.setStatus("current")
_TnUserPasswordAge_Type = Unsigned32
_TnUserPasswordAge_Object = MibTableColumn
tnUserPasswordAge = _TnUserPasswordAge_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 10),
    _TnUserPasswordAge_Type()
)
tnUserPasswordAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserPasswordAge.setStatus("current")
_TnUserPasswordGraceInterval_Type = Unsigned32
_TnUserPasswordGraceInterval_Object = MibTableColumn
tnUserPasswordGraceInterval = _TnUserPasswordGraceInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 11),
    _TnUserPasswordGraceInterval_Type()
)
tnUserPasswordGraceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserPasswordGraceInterval.setStatus("current")
_TnUserPasswordGraceLogins_Type = Unsigned32
_TnUserPasswordGraceLogins_Object = MibTableColumn
tnUserPasswordGraceLogins = _TnUserPasswordGraceLogins_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 1, 1, 12),
    _TnUserPasswordGraceLogins_Type()
)
tnUserPasswordGraceLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserPasswordGraceLogins.setStatus("current")
_TnUserSessionTable_Object = MibTable
tnUserSessionTable = _TnUserSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tnUserSessionTable.setStatus("current")
_TnUserSessionEntry_Object = MibTableRow
tnUserSessionEntry = _TnUserSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 2, 1)
)
tnUserSessionEntry.setIndexNames(
    (0, "TROPIC-USERMGMT-MIB", "tnUserSessionId"),
)
if mibBuilder.loadTexts:
    tnUserSessionEntry.setStatus("current")
_TnUserSessionId_Type = Unsigned32
_TnUserSessionId_Object = MibTableColumn
tnUserSessionId = _TnUserSessionId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 2, 1, 1),
    _TnUserSessionId_Type()
)
tnUserSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnUserSessionId.setStatus("current")


class _TnUserSessionUserType_Type(Integer32):
    """Custom type tnUserSessionUserType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("cliTelnet", 2),
          ("cliSsh", 3),
          ("cliConsloe", 4),
          ("webui", 5),
          ("webuiSecure", 6),
          ("tl1Raw", 7),
          ("tl1Telnet", 8),
          ("tl1Ssh", 9),
          ("snmp", 10))
    )


_TnUserSessionUserType_Type.__name__ = "Integer32"
_TnUserSessionUserType_Object = MibTableColumn
tnUserSessionUserType = _TnUserSessionUserType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 2, 1, 2),
    _TnUserSessionUserType_Type()
)
tnUserSessionUserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserSessionUserType.setStatus("current")
_TnUserSessionUserName_Type = SnmpAdminString
_TnUserSessionUserName_Object = MibTableColumn
tnUserSessionUserName = _TnUserSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 2, 1, 3),
    _TnUserSessionUserName_Type()
)
tnUserSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserSessionUserName.setStatus("current")
_TnUserSessionTerminal_Type = SnmpAdminString
_TnUserSessionTerminal_Object = MibTableColumn
tnUserSessionTerminal = _TnUserSessionTerminal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 2, 1, 4),
    _TnUserSessionTerminal_Type()
)
tnUserSessionTerminal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserSessionTerminal.setStatus("current")
_TnUserSessionLoginTime_Type = Unsigned32
_TnUserSessionLoginTime_Object = MibTableColumn
tnUserSessionLoginTime = _TnUserSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 1, 2, 1, 5),
    _TnUserSessionLoginTime_Type()
)
tnUserSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserSessionLoginTime.setStatus("current")
_TnUserMgmtGlobal_ObjectIdentity = ObjectIdentity
tnUserMgmtGlobal = _TnUserMgmtGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2)
)


class _TnUserMgmtSysMinPasswordLength_Type(Unsigned32):
    """Custom type tnUserMgmtSysMinPasswordLength based on Unsigned32"""
    defaultValue = 8


_TnUserMgmtSysMinPasswordLength_Type.__name__ = "Unsigned32"
_TnUserMgmtSysMinPasswordLength_Object = MibScalar
tnUserMgmtSysMinPasswordLength = _TnUserMgmtSysMinPasswordLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 1),
    _TnUserMgmtSysMinPasswordLength_Type()
)
tnUserMgmtSysMinPasswordLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysMinPasswordLength.setStatus("current")


class _TnUserMgmtSysMaxPasswordLength_Type(Unsigned32):
    """Custom type tnUserMgmtSysMaxPasswordLength based on Unsigned32"""
    defaultValue = 32


_TnUserMgmtSysMaxPasswordLength_Type.__name__ = "Unsigned32"
_TnUserMgmtSysMaxPasswordLength_Object = MibScalar
tnUserMgmtSysMaxPasswordLength = _TnUserMgmtSysMaxPasswordLength_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 2),
    _TnUserMgmtSysMaxPasswordLength_Type()
)
tnUserMgmtSysMaxPasswordLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysMaxPasswordLength.setStatus("current")


class _TnUserMgmtSysSessionTimeOut_Type(Unsigned32):
    """Custom type tnUserMgmtSysSessionTimeOut based on Unsigned32"""
    defaultValue = 60


_TnUserMgmtSysSessionTimeOut_Type.__name__ = "Unsigned32"
_TnUserMgmtSysSessionTimeOut_Object = MibScalar
tnUserMgmtSysSessionTimeOut = _TnUserMgmtSysSessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 3),
    _TnUserMgmtSysSessionTimeOut_Type()
)
tnUserMgmtSysSessionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysSessionTimeOut.setStatus("current")


class _TnUserMgmtSysSessionFailedMaxLogins_Type(Unsigned32):
    """Custom type tnUserMgmtSysSessionFailedMaxLogins based on Unsigned32"""
    defaultValue = 3


_TnUserMgmtSysSessionFailedMaxLogins_Type.__name__ = "Unsigned32"
_TnUserMgmtSysSessionFailedMaxLogins_Object = MibScalar
tnUserMgmtSysSessionFailedMaxLogins = _TnUserMgmtSysSessionFailedMaxLogins_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 4),
    _TnUserMgmtSysSessionFailedMaxLogins_Type()
)
tnUserMgmtSysSessionFailedMaxLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysSessionFailedMaxLogins.setStatus("current")


class _TnUserMgmtSysLoginInactivityTimeOut_Type(Unsigned32):
    """Custom type tnUserMgmtSysLoginInactivityTimeOut based on Unsigned32"""
    defaultValue = 60


_TnUserMgmtSysLoginInactivityTimeOut_Type.__name__ = "Unsigned32"
_TnUserMgmtSysLoginInactivityTimeOut_Object = MibScalar
tnUserMgmtSysLoginInactivityTimeOut = _TnUserMgmtSysLoginInactivityTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 5),
    _TnUserMgmtSysLoginInactivityTimeOut_Type()
)
tnUserMgmtSysLoginInactivityTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysLoginInactivityTimeOut.setStatus("current")


class _TnUserMgmtSysMinIntervalInvalidLogin_Type(Unsigned32):
    """Custom type tnUserMgmtSysMinIntervalInvalidLogin based on Unsigned32"""
    defaultValue = 4


_TnUserMgmtSysMinIntervalInvalidLogin_Type.__name__ = "Unsigned32"
_TnUserMgmtSysMinIntervalInvalidLogin_Object = MibScalar
tnUserMgmtSysMinIntervalInvalidLogin = _TnUserMgmtSysMinIntervalInvalidLogin_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 6),
    _TnUserMgmtSysMinIntervalInvalidLogin_Type()
)
tnUserMgmtSysMinIntervalInvalidLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysMinIntervalInvalidLogin.setStatus("current")
_TnUserMgmtSysSessionLogoff_Type = Unsigned32
_TnUserMgmtSysSessionLogoff_Object = MibScalar
tnUserMgmtSysSessionLogoff = _TnUserMgmtSysSessionLogoff_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 7),
    _TnUserMgmtSysSessionLogoff_Type()
)
tnUserMgmtSysSessionLogoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysSessionLogoff.setStatus("current")


class _TnUserMgmtSysPasswordAging_Type(Unsigned32):
    """Custom type tnUserMgmtSysPasswordAging based on Unsigned32"""
    defaultValue = 30


_TnUserMgmtSysPasswordAging_Type.__name__ = "Unsigned32"
_TnUserMgmtSysPasswordAging_Object = MibScalar
tnUserMgmtSysPasswordAging = _TnUserMgmtSysPasswordAging_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 8),
    _TnUserMgmtSysPasswordAging_Type()
)
tnUserMgmtSysPasswordAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysPasswordAging.setStatus("current")


class _TnUserMgmtSysPasswordAgingGraceInterval_Type(Unsigned32):
    """Custom type tnUserMgmtSysPasswordAgingGraceInterval based on Unsigned32"""
    defaultValue = 7


_TnUserMgmtSysPasswordAgingGraceInterval_Type.__name__ = "Unsigned32"
_TnUserMgmtSysPasswordAgingGraceInterval_Object = MibScalar
tnUserMgmtSysPasswordAgingGraceInterval = _TnUserMgmtSysPasswordAgingGraceInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 9),
    _TnUserMgmtSysPasswordAgingGraceInterval_Type()
)
tnUserMgmtSysPasswordAgingGraceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysPasswordAgingGraceInterval.setStatus("current")


class _TnUserMgmtSysPasswordAgingGraceLogins_Type(Unsigned32):
    """Custom type tnUserMgmtSysPasswordAgingGraceLogins based on Unsigned32"""
    defaultValue = 3


_TnUserMgmtSysPasswordAgingGraceLogins_Type.__name__ = "Unsigned32"
_TnUserMgmtSysPasswordAgingGraceLogins_Object = MibScalar
tnUserMgmtSysPasswordAgingGraceLogins = _TnUserMgmtSysPasswordAgingGraceLogins_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 10),
    _TnUserMgmtSysPasswordAgingGraceLogins_Type()
)
tnUserMgmtSysPasswordAgingGraceLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysPasswordAgingGraceLogins.setStatus("current")


class _TnUserMgmtSysPasswordObsolescenceInterval_Type(Unsigned32):
    """Custom type tnUserMgmtSysPasswordObsolescenceInterval based on Unsigned32"""
    defaultValue = 180


_TnUserMgmtSysPasswordObsolescenceInterval_Type.__name__ = "Unsigned32"
_TnUserMgmtSysPasswordObsolescenceInterval_Object = MibScalar
tnUserMgmtSysPasswordObsolescenceInterval = _TnUserMgmtSysPasswordObsolescenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 2, 2, 11),
    _TnUserMgmtSysPasswordObsolescenceInterval_Type()
)
tnUserMgmtSysPasswordObsolescenceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnUserMgmtSysPasswordObsolescenceInterval.setStatus("current")

# Managed Objects groups

tnUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 1, 1, 1)
)
tnUserGroup.setObjects(
      *(("TROPIC-USERMGMT-MIB", "tnUserRowStatus"),
        ("TROPIC-USERMGMT-MIB", "tnUserAccessLevel"),
        ("TROPIC-USERMGMT-MIB", "tnUserPassword"),
        ("TROPIC-USERMGMT-MIB", "tnUserLastLoginDateAndTime"),
        ("TROPIC-USERMGMT-MIB", "tnUserLastLoginTerminalIP"),
        ("TROPIC-USERMGMT-MIB", "tnUserNumberOfFailedLogins"),
        ("TROPIC-USERMGMT-MIB", "tnUserSessionTimeout"),
        ("TROPIC-USERMGMT-MIB", "tnUserLastPasswordChangeDateAndTime"),
        ("TROPIC-USERMGMT-MIB", "tnUserPasswordAge"),
        ("TROPIC-USERMGMT-MIB", "tnUserPasswordGraceInterval"),
        ("TROPIC-USERMGMT-MIB", "tnUserPasswordGraceLogins"))
)
if mibBuilder.loadTexts:
    tnUserGroup.setStatus("current")

tnUserSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 1, 1, 2)
)
tnUserSessionGroup.setObjects(
      *(("TROPIC-USERMGMT-MIB", "tnUserSessionUserType"),
        ("TROPIC-USERMGMT-MIB", "tnUserSessionUserName"),
        ("TROPIC-USERMGMT-MIB", "tnUserSessionTerminal"),
        ("TROPIC-USERMGMT-MIB", "tnUserSessionLoginTime"))
)
if mibBuilder.loadTexts:
    tnUserSessionGroup.setStatus("current")

tnUserMgmtGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 1, 1, 3)
)
tnUserMgmtGlobalGroup.setObjects(
      *(("TROPIC-USERMGMT-MIB", "tnUserMgmtSysMinPasswordLength"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtSysMaxPasswordLength"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtSysSessionTimeOut"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtSysSessionFailedMaxLogins"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtSysLoginInactivityTimeOut"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtSysMinIntervalInvalidLogin"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtSysSessionLogoff"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtSysPasswordAging"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtSysPasswordAgingGraceInterval"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtSysPasswordAgingGraceLogins"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtSysPasswordObsolescenceInterval"))
)
if mibBuilder.loadTexts:
    tnUserMgmtGlobalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnUserMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 7, 1, 2, 1)
)
tnUserMgmtCompliance.setObjects(
      *(("TROPIC-USERMGMT-MIB", "tnUserGroup"),
        ("TROPIC-USERMGMT-MIB", "tnUserSessionGroup"),
        ("TROPIC-USERMGMT-MIB", "tnUserMgmtGlobalGroup"))
)
if mibBuilder.loadTexts:
    tnUserMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-USERMGMT-MIB",
    **{"tnUserMgmtMibModule": tnUserMgmtMibModule,
       "tnUserMgmtConf": tnUserMgmtConf,
       "tnUserMgmtGroups": tnUserMgmtGroups,
       "tnUserGroup": tnUserGroup,
       "tnUserSessionGroup": tnUserSessionGroup,
       "tnUserMgmtGlobalGroup": tnUserMgmtGlobalGroup,
       "tnUserMgmtCompliances": tnUserMgmtCompliances,
       "tnUserMgmtCompliance": tnUserMgmtCompliance,
       "tnUserMgmtObjs": tnUserMgmtObjs,
       "tnUserMgmtBasics": tnUserMgmtBasics,
       "tnUserTable": tnUserTable,
       "tnUserEntry": tnUserEntry,
       "tnUserName": tnUserName,
       "tnUserRowStatus": tnUserRowStatus,
       "tnUserAccessLevel": tnUserAccessLevel,
       "tnUserPassword": tnUserPassword,
       "tnUserLastLoginDateAndTime": tnUserLastLoginDateAndTime,
       "tnUserLastLoginTerminalIP": tnUserLastLoginTerminalIP,
       "tnUserNumberOfFailedLogins": tnUserNumberOfFailedLogins,
       "tnUserSessionTimeout": tnUserSessionTimeout,
       "tnUserLastPasswordChangeDateAndTime": tnUserLastPasswordChangeDateAndTime,
       "tnUserPasswordAge": tnUserPasswordAge,
       "tnUserPasswordGraceInterval": tnUserPasswordGraceInterval,
       "tnUserPasswordGraceLogins": tnUserPasswordGraceLogins,
       "tnUserSessionTable": tnUserSessionTable,
       "tnUserSessionEntry": tnUserSessionEntry,
       "tnUserSessionId": tnUserSessionId,
       "tnUserSessionUserType": tnUserSessionUserType,
       "tnUserSessionUserName": tnUserSessionUserName,
       "tnUserSessionTerminal": tnUserSessionTerminal,
       "tnUserSessionLoginTime": tnUserSessionLoginTime,
       "tnUserMgmtGlobal": tnUserMgmtGlobal,
       "tnUserMgmtSysMinPasswordLength": tnUserMgmtSysMinPasswordLength,
       "tnUserMgmtSysMaxPasswordLength": tnUserMgmtSysMaxPasswordLength,
       "tnUserMgmtSysSessionTimeOut": tnUserMgmtSysSessionTimeOut,
       "tnUserMgmtSysSessionFailedMaxLogins": tnUserMgmtSysSessionFailedMaxLogins,
       "tnUserMgmtSysLoginInactivityTimeOut": tnUserMgmtSysLoginInactivityTimeOut,
       "tnUserMgmtSysMinIntervalInvalidLogin": tnUserMgmtSysMinIntervalInvalidLogin,
       "tnUserMgmtSysSessionLogoff": tnUserMgmtSysSessionLogoff,
       "tnUserMgmtSysPasswordAging": tnUserMgmtSysPasswordAging,
       "tnUserMgmtSysPasswordAgingGraceInterval": tnUserMgmtSysPasswordAgingGraceInterval,
       "tnUserMgmtSysPasswordAgingGraceLogins": tnUserMgmtSysPasswordAgingGraceLogins,
       "tnUserMgmtSysPasswordObsolescenceInterval": tnUserMgmtSysPasswordObsolescenceInterval}
)
