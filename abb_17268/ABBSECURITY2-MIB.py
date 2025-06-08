# SNMP MIB module (ABBSECURITY2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/abb_17268/ABBSECURITY2-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:23:57 2025
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

(hmLastIpAddr,
 hmLastLoginUserName) = mibBuilder.importSymbols(
    "ABB-PRIVATE-MIB",
    "hmLastIpAddr",
    "hmLastLoginUserName")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(SnmpTagList,
 SnmpTagValue) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagList",
    "SnmpTagValue")

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
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

hmSecurity2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52)
)
if mibBuilder.loadTexts:
    hmSecurity2.setRevisions(
        ("2008-12-08 12:00",
         "2008-09-30 12:00",
         "2010-05-20 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Abb_ObjectIdentity = ObjectIdentity
abb = _Abb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268)
)
_UtilityCommProducts_ObjectIdentity = ObjectIdentity
utilityCommProducts = _UtilityCommProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818)
)
_ArFamilyCommProducts_ObjectIdentity = ObjectIdentity
arFamilyCommProducts = _ArFamilyCommProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6)
)
_HmSecurity2Event_ObjectIdentity = ObjectIdentity
hmSecurity2Event = _HmSecurity2Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0)
)
if mibBuilder.loadTexts:
    hmSecurity2Event.setStatus("current")
_HmSecurity2Objects_ObjectIdentity = ObjectIdentity
hmSecurity2Objects = _HmSecurity2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1)
)
_HmSec2Device_ObjectIdentity = ObjectIdentity
hmSec2Device = _HmSec2Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 1)
)
_HmSec2Agent_ObjectIdentity = ObjectIdentity
hmSec2Agent = _HmSec2Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2)
)
_HmSec2WebGroup_ObjectIdentity = ObjectIdentity
hmSec2WebGroup = _HmSec2WebGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 3)
)


class _HmSec2WebLoginAccessWeb_Type(Integer32):
    """Custom type hmSec2WebLoginAccessWeb based on Integer32"""
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


_HmSec2WebLoginAccessWeb_Type.__name__ = "Integer32"
_HmSec2WebLoginAccessWeb_Object = MibScalar
hmSec2WebLoginAccessWeb = _HmSec2WebLoginAccessWeb_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 3, 1),
    _HmSec2WebLoginAccessWeb_Type()
)
hmSec2WebLoginAccessWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2WebLoginAccessWeb.setStatus("current")


class _HmSec2WebLoginTimeoutWeb_Type(Integer32):
    """Custom type hmSec2WebLoginTimeoutWeb based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HmSec2WebLoginTimeoutWeb_Type.__name__ = "Integer32"
_HmSec2WebLoginTimeoutWeb_Object = MibScalar
hmSec2WebLoginTimeoutWeb = _HmSec2WebLoginTimeoutWeb_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 3, 2),
    _HmSec2WebLoginTimeoutWeb_Type()
)
hmSec2WebLoginTimeoutWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2WebLoginTimeoutWeb.setStatus("current")


class _HmSec2WebHttpsPortNumber_Type(Integer32):
    """Custom type hmSec2WebHttpsPortNumber based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HmSec2WebHttpsPortNumber_Type.__name__ = "Integer32"
_HmSec2WebHttpsPortNumber_Object = MibScalar
hmSec2WebHttpsPortNumber = _HmSec2WebHttpsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 3, 6),
    _HmSec2WebHttpsPortNumber_Type()
)
hmSec2WebHttpsPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2WebHttpsPortNumber.setStatus("current")
_HmSec2CliGroup_ObjectIdentity = ObjectIdentity
hmSec2CliGroup = _HmSec2CliGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4)
)


class _HmSec2CliLoginPrompt_Type(DisplayString):
    """Custom type hmSec2CliLoginPrompt based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmSec2CliLoginPrompt_Type.__name__ = "DisplayString"
_HmSec2CliLoginPrompt_Object = MibScalar
hmSec2CliLoginPrompt = _HmSec2CliLoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4, 1),
    _HmSec2CliLoginPrompt_Type()
)
hmSec2CliLoginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2CliLoginPrompt.setStatus("current")


class _HmSec2CliLoginTimeoutSerial_Type(Integer32):
    """Custom type hmSec2CliLoginTimeoutSerial based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HmSec2CliLoginTimeoutSerial_Type.__name__ = "Integer32"
_HmSec2CliLoginTimeoutSerial_Object = MibScalar
hmSec2CliLoginTimeoutSerial = _HmSec2CliLoginTimeoutSerial_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4, 2),
    _HmSec2CliLoginTimeoutSerial_Type()
)
hmSec2CliLoginTimeoutSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2CliLoginTimeoutSerial.setStatus("current")


class _HmSec2CliLoginTimeoutSSH_Type(Integer32):
    """Custom type hmSec2CliLoginTimeoutSSH based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HmSec2CliLoginTimeoutSSH_Type.__name__ = "Integer32"
_HmSec2CliLoginTimeoutSSH_Object = MibScalar
hmSec2CliLoginTimeoutSSH = _HmSec2CliLoginTimeoutSSH_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4, 3),
    _HmSec2CliLoginTimeoutSSH_Type()
)
hmSec2CliLoginTimeoutSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2CliLoginTimeoutSSH.setStatus("current")


class _HmSec2CliLoginTimeoutTelnet_Type(Integer32):
    """Custom type hmSec2CliLoginTimeoutTelnet based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HmSec2CliLoginTimeoutTelnet_Type.__name__ = "Integer32"
_HmSec2CliLoginTimeoutTelnet_Object = MibScalar
hmSec2CliLoginTimeoutTelnet = _HmSec2CliLoginTimeoutTelnet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4, 4),
    _HmSec2CliLoginTimeoutTelnet_Type()
)
hmSec2CliLoginTimeoutTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2CliLoginTimeoutTelnet.setStatus("current")


class _HmSec2CliLoginAccessSSH_Type(Integer32):
    """Custom type hmSec2CliLoginAccessSSH based on Integer32"""
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


_HmSec2CliLoginAccessSSH_Type.__name__ = "Integer32"
_HmSec2CliLoginAccessSSH_Object = MibScalar
hmSec2CliLoginAccessSSH = _HmSec2CliLoginAccessSSH_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4, 6),
    _HmSec2CliLoginAccessSSH_Type()
)
hmSec2CliLoginAccessSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2CliLoginAccessSSH.setStatus("current")


class _HmSec2CliLoginAccessTelnet_Type(Integer32):
    """Custom type hmSec2CliLoginAccessTelnet based on Integer32"""
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


_HmSec2CliLoginAccessTelnet_Type.__name__ = "Integer32"
_HmSec2CliLoginAccessTelnet_Object = MibScalar
hmSec2CliLoginAccessTelnet = _HmSec2CliLoginAccessTelnet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4, 7),
    _HmSec2CliLoginAccessTelnet_Type()
)
hmSec2CliLoginAccessTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2CliLoginAccessTelnet.setStatus("current")


class _HmSec2CliLoginSshPortNumber_Type(Integer32):
    """Custom type hmSec2CliLoginSshPortNumber based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HmSec2CliLoginSshPortNumber_Type.__name__ = "Integer32"
_HmSec2CliLoginSshPortNumber_Object = MibScalar
hmSec2CliLoginSshPortNumber = _HmSec2CliLoginSshPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4, 8),
    _HmSec2CliLoginSshPortNumber_Type()
)
hmSec2CliLoginSshPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2CliLoginSshPortNumber.setStatus("current")


class _HmSec2CliLoginFingerPrintDSA_Type(DisplayString):
    """Custom type hmSec2CliLoginFingerPrintDSA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2CliLoginFingerPrintDSA_Type.__name__ = "DisplayString"
_HmSec2CliLoginFingerPrintDSA_Object = MibScalar
hmSec2CliLoginFingerPrintDSA = _HmSec2CliLoginFingerPrintDSA_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4, 9),
    _HmSec2CliLoginFingerPrintDSA_Type()
)
hmSec2CliLoginFingerPrintDSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2CliLoginFingerPrintDSA.setStatus("current")


class _HmSec2CliLoginFingerPrintRSA_Type(DisplayString):
    """Custom type hmSec2CliLoginFingerPrintRSA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2CliLoginFingerPrintRSA_Type.__name__ = "DisplayString"
_HmSec2CliLoginFingerPrintRSA_Object = MibScalar
hmSec2CliLoginFingerPrintRSA = _HmSec2CliLoginFingerPrintRSA_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4, 10),
    _HmSec2CliLoginFingerPrintRSA_Type()
)
hmSec2CliLoginFingerPrintRSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2CliLoginFingerPrintRSA.setStatus("current")


class _HmSec2CliLoginDefaultPasswordActive_Type(Integer32):
    """Custom type hmSec2CliLoginDefaultPasswordActive based on Integer32"""
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


_HmSec2CliLoginDefaultPasswordActive_Type.__name__ = "Integer32"
_HmSec2CliLoginDefaultPasswordActive_Object = MibScalar
hmSec2CliLoginDefaultPasswordActive = _HmSec2CliLoginDefaultPasswordActive_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 4, 11),
    _HmSec2CliLoginDefaultPasswordActive_Type()
)
hmSec2CliLoginDefaultPasswordActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2CliLoginDefaultPasswordActive.setStatus("current")
_HmSec2FileManagementGroup_ObjectIdentity = ObjectIdentity
hmSec2FileManagementGroup = _HmSec2FileManagementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5)
)
_HmSec2FileManagementActionGroup_ObjectIdentity = ObjectIdentity
hmSec2FileManagementActionGroup = _HmSec2FileManagementActionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1)
)


class _HmSec2FMActionType_Type(Integer32):
    """Custom type hmSec2FMActionType based on Integer32"""
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
        *(("other", 1),
          ("copy", 2),
          ("clear", 3))
    )


_HmSec2FMActionType_Type.__name__ = "Integer32"
_HmSec2FMActionType_Object = MibScalar
hmSec2FMActionType = _HmSec2FMActionType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 1),
    _HmSec2FMActionType_Type()
)
hmSec2FMActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMActionType.setStatus("current")


class _HmSec2FMActionItemType_Type(Integer32):
    """Custom type hmSec2FMActionItemType based on Integer32"""
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
        *(("config", 1),
          ("firmware", 2),
          ("eventlog", 3),
          ("certs", 4),
          ("sysinfo", 5))
    )


_HmSec2FMActionItemType_Type.__name__ = "Integer32"
_HmSec2FMActionItemType_Object = MibScalar
hmSec2FMActionItemType = _HmSec2FMActionItemType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 2),
    _HmSec2FMActionItemType_Type()
)
hmSec2FMActionItemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMActionItemType.setStatus("current")


class _HmSec2FMActionSourceType_Type(Integer32):
    """Custom type hmSec2FMActionSourceType based on Integer32"""
    defaultValue = 3

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
        *(("nv", 1),
          ("aca", 2),
          ("running-config", 3),
          ("system", 4))
    )


_HmSec2FMActionSourceType_Type.__name__ = "Integer32"
_HmSec2FMActionSourceType_Object = MibScalar
hmSec2FMActionSourceType = _HmSec2FMActionSourceType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 3),
    _HmSec2FMActionSourceType_Type()
)
hmSec2FMActionSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMActionSourceType.setStatus("current")


class _HmSec2FMActionSourceData_Type(DisplayString):
    """Custom type hmSec2FMActionSourceData based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FMActionSourceData_Type.__name__ = "DisplayString"
_HmSec2FMActionSourceData_Object = MibScalar
hmSec2FMActionSourceData = _HmSec2FMActionSourceData_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 4),
    _HmSec2FMActionSourceData_Type()
)
hmSec2FMActionSourceData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMActionSourceData.setStatus("current")


class _HmSec2FMActionDestinationType_Type(Integer32):
    """Custom type hmSec2FMActionDestinationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nv", 1),
          ("aca", 2),
          ("running-config", 3))
    )


_HmSec2FMActionDestinationType_Type.__name__ = "Integer32"
_HmSec2FMActionDestinationType_Object = MibScalar
hmSec2FMActionDestinationType = _HmSec2FMActionDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 5),
    _HmSec2FMActionDestinationType_Type()
)
hmSec2FMActionDestinationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMActionDestinationType.setStatus("current")


class _HmSec2FMActionDestinationData_Type(DisplayString):
    """Custom type hmSec2FMActionDestinationData based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FMActionDestinationData_Type.__name__ = "DisplayString"
_HmSec2FMActionDestinationData_Object = MibScalar
hmSec2FMActionDestinationData = _HmSec2FMActionDestinationData_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 6),
    _HmSec2FMActionDestinationData_Type()
)
hmSec2FMActionDestinationData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMActionDestinationData.setStatus("current")


class _HmSec2FMActionActivate_Type(Integer32):
    """Custom type hmSec2FMActionActivate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("activate", 2))
    )


_HmSec2FMActionActivate_Type.__name__ = "Integer32"
_HmSec2FMActionActivate_Object = MibScalar
hmSec2FMActionActivate = _HmSec2FMActionActivate_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 7),
    _HmSec2FMActionActivate_Type()
)
hmSec2FMActionActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMActionActivate.setStatus("current")


class _HmSec2FMActionActivateResult_Type(Integer32):
    """Custom type hmSec2FMActionActivateResult based on Integer32"""
    defaultValue = 1

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
          ("param-error", 2),
          ("busy", 3))
    )


_HmSec2FMActionActivateResult_Type.__name__ = "Integer32"
_HmSec2FMActionActivateResult_Object = MibScalar
hmSec2FMActionActivateResult = _HmSec2FMActionActivateResult_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 8),
    _HmSec2FMActionActivateResult_Type()
)
hmSec2FMActionActivateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMActionActivateResult.setStatus("current")
_HmSec2FMActionActivateResultText_Type = DisplayString
_HmSec2FMActionActivateResultText_Object = MibScalar
hmSec2FMActionActivateResultText = _HmSec2FMActionActivateResultText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 9),
    _HmSec2FMActionActivateResultText_Type()
)
hmSec2FMActionActivateResultText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMActionActivateResultText.setStatus("current")


class _HmSec2FMActionStatus_Type(Integer32):
    """Custom type hmSec2FMActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("running", 2))
    )


_HmSec2FMActionStatus_Type.__name__ = "Integer32"
_HmSec2FMActionStatus_Object = MibScalar
hmSec2FMActionStatus = _HmSec2FMActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 10),
    _HmSec2FMActionStatus_Type()
)
hmSec2FMActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMActionStatus.setStatus("current")


class _HmSec2FMActionPercentReady_Type(Integer32):
    """Custom type hmSec2FMActionPercentReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HmSec2FMActionPercentReady_Type.__name__ = "Integer32"
_HmSec2FMActionPercentReady_Object = MibScalar
hmSec2FMActionPercentReady = _HmSec2FMActionPercentReady_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 11),
    _HmSec2FMActionPercentReady_Type()
)
hmSec2FMActionPercentReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMActionPercentReady.setStatus("current")


class _HmSec2FMActionResult_Type(Integer32):
    """Custom type hmSec2FMActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("error", 2))
    )


_HmSec2FMActionResult_Type.__name__ = "Integer32"
_HmSec2FMActionResult_Object = MibScalar
hmSec2FMActionResult = _HmSec2FMActionResult_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 12),
    _HmSec2FMActionResult_Type()
)
hmSec2FMActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMActionResult.setStatus("current")
_HmSec2FMActionResultText_Type = DisplayString
_HmSec2FMActionResultText_Object = MibScalar
hmSec2FMActionResultText = _HmSec2FMActionResultText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 1, 13),
    _HmSec2FMActionResultText_Type()
)
hmSec2FMActionResultText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMActionResultText.setStatus("current")
_HmSec2FileManagementProfileGroup_ObjectIdentity = ObjectIdentity
hmSec2FileManagementProfileGroup = _HmSec2FileManagementProfileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2)
)
_HmSec2FMNvProfileTable_Object = MibTable
hmSec2FMNvProfileTable = _HmSec2FMNvProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hmSec2FMNvProfileTable.setStatus("current")
_HmSec2FMNvProfileEntry_Object = MibTableRow
hmSec2FMNvProfileEntry = _HmSec2FMNvProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 1, 1)
)
hmSec2FMNvProfileEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FMNvProfileIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FMNvProfileEntry.setStatus("current")


class _HmSec2FMNvProfileIndex_Type(Integer32):
    """Custom type hmSec2FMNvProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSec2FMNvProfileIndex_Type.__name__ = "Integer32"
_HmSec2FMNvProfileIndex_Object = MibTableColumn
hmSec2FMNvProfileIndex = _HmSec2FMNvProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 1, 1, 1),
    _HmSec2FMNvProfileIndex_Type()
)
hmSec2FMNvProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMNvProfileIndex.setStatus("current")


class _HmSec2FMNvProfileName_Type(DisplayString):
    """Custom type hmSec2FMNvProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmSec2FMNvProfileName_Type.__name__ = "DisplayString"
_HmSec2FMNvProfileName_Object = MibTableColumn
hmSec2FMNvProfileName = _HmSec2FMNvProfileName_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 1, 1, 2),
    _HmSec2FMNvProfileName_Type()
)
hmSec2FMNvProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMNvProfileName.setStatus("current")
_HmSec2FMNvProfileDateTime_Type = TimeTicks
_HmSec2FMNvProfileDateTime_Object = MibTableColumn
hmSec2FMNvProfileDateTime = _HmSec2FMNvProfileDateTime_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 1, 1, 3),
    _HmSec2FMNvProfileDateTime_Type()
)
hmSec2FMNvProfileDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMNvProfileDateTime.setStatus("current")


class _HmSec2FMNvProfileActive_Type(Integer32):
    """Custom type hmSec2FMNvProfileActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HmSec2FMNvProfileActive_Type.__name__ = "Integer32"
_HmSec2FMNvProfileActive_Object = MibTableColumn
hmSec2FMNvProfileActive = _HmSec2FMNvProfileActive_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 1, 1, 4),
    _HmSec2FMNvProfileActive_Type()
)
hmSec2FMNvProfileActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMNvProfileActive.setStatus("current")


class _HmSec2FMNvProfileAction_Type(Integer32):
    """Custom type hmSec2FMNvProfileAction based on Integer32"""
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


_HmSec2FMNvProfileAction_Type.__name__ = "Integer32"
_HmSec2FMNvProfileAction_Object = MibTableColumn
hmSec2FMNvProfileAction = _HmSec2FMNvProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 1, 1, 5),
    _HmSec2FMNvProfileAction_Type()
)
hmSec2FMNvProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMNvProfileAction.setStatus("current")
_HmSec2FMAcaProfileTable_Object = MibTable
hmSec2FMAcaProfileTable = _HmSec2FMAcaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    hmSec2FMAcaProfileTable.setStatus("current")
_HmSec2FMAcaProfileEntry_Object = MibTableRow
hmSec2FMAcaProfileEntry = _HmSec2FMAcaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 2, 1)
)
hmSec2FMAcaProfileEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FMAcaProfileIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FMAcaProfileEntry.setStatus("current")


class _HmSec2FMAcaProfileIndex_Type(Integer32):
    """Custom type hmSec2FMAcaProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HmSec2FMAcaProfileIndex_Type.__name__ = "Integer32"
_HmSec2FMAcaProfileIndex_Object = MibTableColumn
hmSec2FMAcaProfileIndex = _HmSec2FMAcaProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 2, 1, 1),
    _HmSec2FMAcaProfileIndex_Type()
)
hmSec2FMAcaProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMAcaProfileIndex.setStatus("current")


class _HmSec2FMAcaProfileName_Type(DisplayString):
    """Custom type hmSec2FMAcaProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmSec2FMAcaProfileName_Type.__name__ = "DisplayString"
_HmSec2FMAcaProfileName_Object = MibTableColumn
hmSec2FMAcaProfileName = _HmSec2FMAcaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 2, 1, 2),
    _HmSec2FMAcaProfileName_Type()
)
hmSec2FMAcaProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMAcaProfileName.setStatus("current")
_HmSec2FMAcaProfileDateTime_Type = TimeTicks
_HmSec2FMAcaProfileDateTime_Object = MibTableColumn
hmSec2FMAcaProfileDateTime = _HmSec2FMAcaProfileDateTime_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 2, 1, 3),
    _HmSec2FMAcaProfileDateTime_Type()
)
hmSec2FMAcaProfileDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMAcaProfileDateTime.setStatus("current")


class _HmSec2FMAcaProfileActive_Type(Integer32):
    """Custom type hmSec2FMAcaProfileActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HmSec2FMAcaProfileActive_Type.__name__ = "Integer32"
_HmSec2FMAcaProfileActive_Object = MibTableColumn
hmSec2FMAcaProfileActive = _HmSec2FMAcaProfileActive_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 2, 1, 4),
    _HmSec2FMAcaProfileActive_Type()
)
hmSec2FMAcaProfileActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMAcaProfileActive.setStatus("current")


class _HmSec2FMAcaProfileAction_Type(Integer32):
    """Custom type hmSec2FMAcaProfileAction based on Integer32"""
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


_HmSec2FMAcaProfileAction_Type.__name__ = "Integer32"
_HmSec2FMAcaProfileAction_Object = MibTableColumn
hmSec2FMAcaProfileAction = _HmSec2FMAcaProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 2, 2, 1, 5),
    _HmSec2FMAcaProfileAction_Type()
)
hmSec2FMAcaProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FMAcaProfileAction.setStatus("current")
_HmSec2FileManagementStatusGroup_ObjectIdentity = ObjectIdentity
hmSec2FileManagementStatusGroup = _HmSec2FileManagementStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 3)
)


class _HmSec2FMNvState_Type(Integer32):
    """Custom type hmSec2FMNvState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("out-of-sync", 2))
    )


_HmSec2FMNvState_Type.__name__ = "Integer32"
_HmSec2FMNvState_Object = MibScalar
hmSec2FMNvState = _HmSec2FMNvState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 3, 1),
    _HmSec2FMNvState_Type()
)
hmSec2FMNvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMNvState.setStatus("current")


class _HmSec2FMAcaState_Type(Integer32):
    """Custom type hmSec2FMAcaState based on Integer32"""
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
        *(("ok", 1),
          ("out-of-sync", 2),
          ("absent", 3),
          ("autodisabled", 4))
    )


_HmSec2FMAcaState_Type.__name__ = "Integer32"
_HmSec2FMAcaState_Object = MibScalar
hmSec2FMAcaState = _HmSec2FMAcaState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 5, 3, 2),
    _HmSec2FMAcaState_Type()
)
hmSec2FMAcaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FMAcaState.setStatus("current")
_HmSec2LoggingGroup_ObjectIdentity = ObjectIdentity
hmSec2LoggingGroup = _HmSec2LoggingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10)
)
_HmSec2LoggingGeneral_ObjectIdentity = ObjectIdentity
hmSec2LoggingGeneral = _HmSec2LoggingGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 1)
)


class _HmSec2SyslogServerIPAddr_Type(IpAddress):
    """Custom type hmSec2SyslogServerIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_HmSec2SyslogServerIPAddr_Type.__name__ = "IpAddress"
_HmSec2SyslogServerIPAddr_Object = MibScalar
hmSec2SyslogServerIPAddr = _HmSec2SyslogServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 1, 1),
    _HmSec2SyslogServerIPAddr_Type()
)
hmSec2SyslogServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2SyslogServerIPAddr.setStatus("current")


class _HmSec2SyslogServerUdpPort_Type(InetPortNumber):
    """Custom type hmSec2SyslogServerUdpPort based on InetPortNumber"""
    defaultValue = 514


_HmSec2SyslogServerUdpPort_Type.__name__ = "InetPortNumber"
_HmSec2SyslogServerUdpPort_Object = MibScalar
hmSec2SyslogServerUdpPort = _HmSec2SyslogServerUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 1, 2),
    _HmSec2SyslogServerUdpPort_Type()
)
hmSec2SyslogServerUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2SyslogServerUdpPort.setStatus("current")


class _HmSec2LogPermFileSize_Type(Integer32):
    """Custom type hmSec2LogPermFileSize based on Integer32"""
    defaultValue = 0


_HmSec2LogPermFileSize_Type.__name__ = "Integer32"
_HmSec2LogPermFileSize_Object = MibScalar
hmSec2LogPermFileSize = _HmSec2LogPermFileSize_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 1, 3),
    _HmSec2LogPermFileSize_Type()
)
hmSec2LogPermFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2LogPermFileSize.setStatus("current")


class _HmSec2LogPermFilesMax_Type(Integer32):
    """Custom type hmSec2LogPermFilesMax based on Integer32"""
    defaultValue = 0


_HmSec2LogPermFilesMax_Type.__name__ = "Integer32"
_HmSec2LogPermFilesMax_Object = MibScalar
hmSec2LogPermFilesMax = _HmSec2LogPermFilesMax_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 1, 4),
    _HmSec2LogPermFilesMax_Type()
)
hmSec2LogPermFilesMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2LogPermFilesMax.setStatus("current")


class _HmSec2LogPermFilesLock_Type(Integer32):
    """Custom type hmSec2LogPermFilesLock based on Integer32"""
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


_HmSec2LogPermFilesLock_Type.__name__ = "Integer32"
_HmSec2LogPermFilesLock_Object = MibScalar
hmSec2LogPermFilesLock = _HmSec2LogPermFilesLock_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 1, 5),
    _HmSec2LogPermFilesLock_Type()
)
hmSec2LogPermFilesLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2LogPermFilesLock.setStatus("current")
_HmSec2LogLevelTable_Object = MibTable
hmSec2LogLevelTable = _HmSec2LogLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    hmSec2LogLevelTable.setStatus("current")
_HmSec2LogLevelEntry_Object = MibTableRow
hmSec2LogLevelEntry = _HmSec2LogLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 2, 1)
)
hmSec2LogLevelEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2LogLevelIndex"),
)
if mibBuilder.loadTexts:
    hmSec2LogLevelEntry.setStatus("current")
_HmSec2LogLevelIndex_Type = Integer32
_HmSec2LogLevelIndex_Object = MibTableColumn
hmSec2LogLevelIndex = _HmSec2LogLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 2, 1, 1),
    _HmSec2LogLevelIndex_Type()
)
hmSec2LogLevelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2LogLevelIndex.setStatus("current")


class _HmSec2LogLevelUpto_Type(Integer32):
    """Custom type hmSec2LogLevelUpto based on Integer32"""
    defaultValue = 5

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
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )


_HmSec2LogLevelUpto_Type.__name__ = "Integer32"
_HmSec2LogLevelUpto_Object = MibTableColumn
hmSec2LogLevelUpto = _HmSec2LogLevelUpto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 2, 1, 2),
    _HmSec2LogLevelUpto_Type()
)
hmSec2LogLevelUpto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2LogLevelUpto.setStatus("current")


class _HmSec2LogLevelName_Type(DisplayString):
    """Custom type hmSec2LogLevelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HmSec2LogLevelName_Type.__name__ = "DisplayString"
_HmSec2LogLevelName_Object = MibTableColumn
hmSec2LogLevelName = _HmSec2LogLevelName_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 2, 1, 3),
    _HmSec2LogLevelName_Type()
)
hmSec2LogLevelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2LogLevelName.setStatus("current")


class _HmSec2LogLevelDesc_Type(DisplayString):
    """Custom type hmSec2LogLevelDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HmSec2LogLevelDesc_Type.__name__ = "DisplayString"
_HmSec2LogLevelDesc_Object = MibTableColumn
hmSec2LogLevelDesc = _HmSec2LogLevelDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 2, 1, 4),
    _HmSec2LogLevelDesc_Type()
)
hmSec2LogLevelDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2LogLevelDesc.setStatus("current")


class _HmSec2LogLevelPerm_Type(Integer32):
    """Custom type hmSec2LogLevelPerm based on Integer32"""
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


_HmSec2LogLevelPerm_Type.__name__ = "Integer32"
_HmSec2LogLevelPerm_Object = MibTableColumn
hmSec2LogLevelPerm = _HmSec2LogLevelPerm_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 10, 2, 1, 5),
    _HmSec2LogLevelPerm_Type()
)
hmSec2LogLevelPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2LogLevelPerm.setStatus("current")
_HmSec2UserConfigGroup_ObjectIdentity = ObjectIdentity
hmSec2UserConfigGroup = _HmSec2UserConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 20)
)
_HmSec2UserConfigTable_Object = MibTable
hmSec2UserConfigTable = _HmSec2UserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 20, 1)
)
if mibBuilder.loadTexts:
    hmSec2UserConfigTable.setStatus("current")
_HmSec2UserConfigEntry_Object = MibTableRow
hmSec2UserConfigEntry = _HmSec2UserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 20, 1, 1)
)
hmSec2UserConfigEntry.setIndexNames(
    (1, "ABBSECURITY2-MIB", "hmSec2UserName"),
)
if mibBuilder.loadTexts:
    hmSec2UserConfigEntry.setStatus("current")


class _HmSec2UserName_Type(SnmpAdminString):
    """Custom type hmSec2UserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HmSec2UserName_Type.__name__ = "SnmpAdminString"
_HmSec2UserName_Object = MibTableColumn
hmSec2UserName = _HmSec2UserName_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 20, 1, 1, 1),
    _HmSec2UserName_Type()
)
hmSec2UserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSec2UserName.setStatus("current")


class _HmSec2UserPassword_Type(DisplayString):
    """Custom type hmSec2UserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_HmSec2UserPassword_Type.__name__ = "DisplayString"
_HmSec2UserPassword_Object = MibTableColumn
hmSec2UserPassword = _HmSec2UserPassword_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 20, 1, 1, 2),
    _HmSec2UserPassword_Type()
)
hmSec2UserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserPassword.setStatus("current")


class _HmSec2UserAccessMode_Type(Integer32):
    """Custom type hmSec2UserAccessMode based on Integer32"""
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
        *(("no-access", 0),
          ("read-access", 1),
          ("read-write-access", 2))
    )


_HmSec2UserAccessMode_Type.__name__ = "Integer32"
_HmSec2UserAccessMode_Object = MibTableColumn
hmSec2UserAccessMode = _HmSec2UserAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 20, 1, 1, 3),
    _HmSec2UserAccessMode_Type()
)
hmSec2UserAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserAccessMode.setStatus("current")


class _HmSec2UserSnmpAuthenticationType_Type(Integer32):
    """Custom type hmSec2UserSnmpAuthenticationType based on Integer32"""
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
          ("hmacmd5", 1),
          ("hmacsha", 2))
    )


_HmSec2UserSnmpAuthenticationType_Type.__name__ = "Integer32"
_HmSec2UserSnmpAuthenticationType_Object = MibTableColumn
hmSec2UserSnmpAuthenticationType = _HmSec2UserSnmpAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 20, 1, 1, 4),
    _HmSec2UserSnmpAuthenticationType_Type()
)
hmSec2UserSnmpAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserSnmpAuthenticationType.setStatus("current")


class _HmSec2UserSnmpEncryptionType_Type(Integer32):
    """Custom type hmSec2UserSnmpEncryptionType based on Integer32"""
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
          ("des", 1),
          ("aes-cfb-128", 2))
    )


_HmSec2UserSnmpEncryptionType_Type.__name__ = "Integer32"
_HmSec2UserSnmpEncryptionType_Object = MibTableColumn
hmSec2UserSnmpEncryptionType = _HmSec2UserSnmpEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 20, 1, 1, 5),
    _HmSec2UserSnmpEncryptionType_Type()
)
hmSec2UserSnmpEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserSnmpEncryptionType.setStatus("current")


class _HmSec2UserAuthenticationList_Type(SnmpTagList):
    """Custom type hmSec2UserAuthenticationList based on SnmpTagList"""
    defaultValue = OctetString("systemLoginDefaultList")

    subtypeSpec = SnmpTagList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HmSec2UserAuthenticationList_Type.__name__ = "SnmpTagList"
_HmSec2UserAuthenticationList_Object = MibTableColumn
hmSec2UserAuthenticationList = _HmSec2UserAuthenticationList_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 20, 1, 1, 6),
    _HmSec2UserAuthenticationList_Type()
)
hmSec2UserAuthenticationList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserAuthenticationList.setStatus("current")
_HmSec2UserStatus_Type = RowStatus
_HmSec2UserStatus_Object = MibTableColumn
hmSec2UserStatus = _HmSec2UserStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 20, 1, 1, 7),
    _HmSec2UserStatus_Type()
)
hmSec2UserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserStatus.setStatus("current")
_HmSec2UserAuthListGroup_ObjectIdentity = ObjectIdentity
hmSec2UserAuthListGroup = _HmSec2UserAuthListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 30)
)
_HmSec2UserAuthListTable_Object = MibTable
hmSec2UserAuthListTable = _HmSec2UserAuthListTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 30, 1)
)
if mibBuilder.loadTexts:
    hmSec2UserAuthListTable.setStatus("current")
_HmSec2UserAuthListEntry_Object = MibTableRow
hmSec2UserAuthListEntry = _HmSec2UserAuthListEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 30, 1, 1)
)
hmSec2UserAuthListEntry.setIndexNames(
    (1, "ABBSECURITY2-MIB", "hmSec2UserAuthListName"),
)
if mibBuilder.loadTexts:
    hmSec2UserAuthListEntry.setStatus("current")


class _HmSec2UserAuthListName_Type(SnmpTagValue):
    """Custom type hmSec2UserAuthListName based on SnmpTagValue"""
    subtypeSpec = SnmpTagValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HmSec2UserAuthListName_Type.__name__ = "SnmpTagValue"
_HmSec2UserAuthListName_Object = MibTableColumn
hmSec2UserAuthListName = _HmSec2UserAuthListName_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 30, 1, 1, 1),
    _HmSec2UserAuthListName_Type()
)
hmSec2UserAuthListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSec2UserAuthListName.setStatus("current")


class _HmSec2UserAuthListPolicy1_Type(Integer32):
    """Custom type hmSec2UserAuthListPolicy1 based on Integer32"""
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
          ("local", 2),
          ("radius", 3),
          ("deny", 4))
    )


_HmSec2UserAuthListPolicy1_Type.__name__ = "Integer32"
_HmSec2UserAuthListPolicy1_Object = MibTableColumn
hmSec2UserAuthListPolicy1 = _HmSec2UserAuthListPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 30, 1, 1, 2),
    _HmSec2UserAuthListPolicy1_Type()
)
hmSec2UserAuthListPolicy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserAuthListPolicy1.setStatus("current")


class _HmSec2UserAuthListPolicy2_Type(Integer32):
    """Custom type hmSec2UserAuthListPolicy2 based on Integer32"""
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
          ("local", 2),
          ("radius", 3),
          ("deny", 4))
    )


_HmSec2UserAuthListPolicy2_Type.__name__ = "Integer32"
_HmSec2UserAuthListPolicy2_Object = MibTableColumn
hmSec2UserAuthListPolicy2 = _HmSec2UserAuthListPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 30, 1, 1, 3),
    _HmSec2UserAuthListPolicy2_Type()
)
hmSec2UserAuthListPolicy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserAuthListPolicy2.setStatus("current")


class _HmSec2UserAuthListPolicy3_Type(Integer32):
    """Custom type hmSec2UserAuthListPolicy3 based on Integer32"""
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
          ("local", 2),
          ("radius", 3),
          ("deny", 4))
    )


_HmSec2UserAuthListPolicy3_Type.__name__ = "Integer32"
_HmSec2UserAuthListPolicy3_Object = MibTableColumn
hmSec2UserAuthListPolicy3 = _HmSec2UserAuthListPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 30, 1, 1, 4),
    _HmSec2UserAuthListPolicy3_Type()
)
hmSec2UserAuthListPolicy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserAuthListPolicy3.setStatus("current")
_HmSec2UserAuthListStatus_Type = RowStatus
_HmSec2UserAuthListStatus_Object = MibTableColumn
hmSec2UserAuthListStatus = _HmSec2UserAuthListStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 30, 1, 1, 5),
    _HmSec2UserAuthListStatus_Type()
)
hmSec2UserAuthListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserAuthListStatus.setStatus("current")


class _HmSec2UserAuthListDefault_Type(SnmpTagValue):
    """Custom type hmSec2UserAuthListDefault based on SnmpTagValue"""
    subtypeSpec = SnmpTagValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2UserAuthListDefault_Type.__name__ = "SnmpTagValue"
_HmSec2UserAuthListDefault_Object = MibScalar
hmSec2UserAuthListDefault = _HmSec2UserAuthListDefault_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 30, 2),
    _HmSec2UserAuthListDefault_Type()
)
hmSec2UserAuthListDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserAuthListDefault.setStatus("current")


class _HmSec2UserFirewallAuthListDefault_Type(SnmpTagValue):
    """Custom type hmSec2UserFirewallAuthListDefault based on SnmpTagValue"""
    subtypeSpec = SnmpTagValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2UserFirewallAuthListDefault_Type.__name__ = "SnmpTagValue"
_HmSec2UserFirewallAuthListDefault_Object = MibScalar
hmSec2UserFirewallAuthListDefault = _HmSec2UserFirewallAuthListDefault_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 30, 3),
    _HmSec2UserFirewallAuthListDefault_Type()
)
hmSec2UserFirewallAuthListDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UserFirewallAuthListDefault.setStatus("current")
_HmSec2UsrFwUserGroup_ObjectIdentity = ObjectIdentity
hmSec2UsrFwUserGroup = _HmSec2UsrFwUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 40)
)


class _HmSec2UsrFwUserGroupAuth_Type(Integer32):
    """Custom type hmSec2UsrFwUserGroupAuth based on Integer32"""
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


_HmSec2UsrFwUserGroupAuth_Type.__name__ = "Integer32"
_HmSec2UsrFwUserGroupAuth_Object = MibScalar
hmSec2UsrFwUserGroupAuth = _HmSec2UsrFwUserGroupAuth_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 40, 1),
    _HmSec2UsrFwUserGroupAuth_Type()
)
hmSec2UsrFwUserGroupAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwUserGroupAuth.setStatus("current")
_HmSec2UsrFwUserTable_Object = MibTable
hmSec2UsrFwUserTable = _HmSec2UsrFwUserTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 40, 2)
)
if mibBuilder.loadTexts:
    hmSec2UsrFwUserTable.setStatus("current")
_HmSec2UsrFwUserEntry_Object = MibTableRow
hmSec2UsrFwUserEntry = _HmSec2UsrFwUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 40, 2, 1)
)
hmSec2UsrFwUserEntry.setIndexNames(
    (1, "ABBSECURITY2-MIB", "hmSec2UsrFwUserName"),
)
if mibBuilder.loadTexts:
    hmSec2UsrFwUserEntry.setStatus("current")


class _HmSec2UsrFwUserName_Type(SnmpAdminString):
    """Custom type hmSec2UsrFwUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HmSec2UsrFwUserName_Type.__name__ = "SnmpAdminString"
_HmSec2UsrFwUserName_Object = MibTableColumn
hmSec2UsrFwUserName = _HmSec2UsrFwUserName_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 40, 2, 1, 1),
    _HmSec2UsrFwUserName_Type()
)
hmSec2UsrFwUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2UsrFwUserName.setStatus("current")


class _HmSec2UsrFwUserPassword_Type(DisplayString):
    """Custom type hmSec2UsrFwUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_HmSec2UsrFwUserPassword_Type.__name__ = "DisplayString"
_HmSec2UsrFwUserPassword_Object = MibTableColumn
hmSec2UsrFwUserPassword = _HmSec2UsrFwUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 40, 2, 1, 2),
    _HmSec2UsrFwUserPassword_Type()
)
hmSec2UsrFwUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwUserPassword.setStatus("current")


class _HmSec2UsrFwUserAuthList_Type(SnmpTagValue):
    """Custom type hmSec2UsrFwUserAuthList based on SnmpTagValue"""
    defaultValue = OctetString("systemLoginDefaultList")

    subtypeSpec = SnmpTagValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HmSec2UsrFwUserAuthList_Type.__name__ = "SnmpTagValue"
_HmSec2UsrFwUserAuthList_Object = MibTableColumn
hmSec2UsrFwUserAuthList = _HmSec2UsrFwUserAuthList_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 40, 2, 1, 3),
    _HmSec2UsrFwUserAuthList_Type()
)
hmSec2UsrFwUserAuthList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwUserAuthList.setStatus("current")


class _HmSec2UsrFwUserLoginStatus_Type(Integer32):
    """Custom type hmSec2UsrFwUserLoginStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("logout", 1),
          ("login", 2))
    )


_HmSec2UsrFwUserLoginStatus_Type.__name__ = "Integer32"
_HmSec2UsrFwUserLoginStatus_Object = MibTableColumn
hmSec2UsrFwUserLoginStatus = _HmSec2UsrFwUserLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 40, 2, 1, 4),
    _HmSec2UsrFwUserLoginStatus_Type()
)
hmSec2UsrFwUserLoginStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwUserLoginStatus.setStatus("current")


class _HmSec2UsrFwUserLoginAddr_Type(DisplayString):
    """Custom type hmSec2UsrFwUserLoginAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2UsrFwUserLoginAddr_Type.__name__ = "DisplayString"
_HmSec2UsrFwUserLoginAddr_Object = MibTableColumn
hmSec2UsrFwUserLoginAddr = _HmSec2UsrFwUserLoginAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 40, 2, 1, 5),
    _HmSec2UsrFwUserLoginAddr_Type()
)
hmSec2UsrFwUserLoginAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2UsrFwUserLoginAddr.setStatus("current")
_HmSec2UsrFwUserStatus_Type = RowStatus
_HmSec2UsrFwUserStatus_Object = MibTableColumn
hmSec2UsrFwUserStatus = _HmSec2UsrFwUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 2, 40, 2, 1, 6),
    _HmSec2UsrFwUserStatus_Type()
)
hmSec2UsrFwUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwUserStatus.setStatus("current")
_HmSec2Security_ObjectIdentity = ObjectIdentity
hmSec2Security = _HmSec2Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3)
)
_HmSec2Radius_ObjectIdentity = ObjectIdentity
hmSec2Radius = _HmSec2Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1)
)
_HmSec2RadiusClient_ObjectIdentity = ObjectIdentity
hmSec2RadiusClient = _HmSec2RadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1, 1)
)


class _HmSec2RadiusMaxRetries_Type(Integer32):
    """Custom type hmSec2RadiusMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HmSec2RadiusMaxRetries_Type.__name__ = "Integer32"
_HmSec2RadiusMaxRetries_Object = MibScalar
hmSec2RadiusMaxRetries = _HmSec2RadiusMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1, 1, 1),
    _HmSec2RadiusMaxRetries_Type()
)
hmSec2RadiusMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RadiusMaxRetries.setStatus("current")


class _HmSec2RadiusTimeout_Type(Integer32):
    """Custom type hmSec2RadiusTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HmSec2RadiusTimeout_Type.__name__ = "Integer32"
_HmSec2RadiusTimeout_Object = MibScalar
hmSec2RadiusTimeout = _HmSec2RadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1, 1, 2),
    _HmSec2RadiusTimeout_Type()
)
hmSec2RadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RadiusTimeout.setStatus("current")
_HmSec2RadiusAuthServerTable_Object = MibTable
hmSec2RadiusAuthServerTable = _HmSec2RadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hmSec2RadiusAuthServerTable.setStatus("current")
_HmSec2RadiusAuthServerEntry_Object = MibTableRow
hmSec2RadiusAuthServerEntry = _HmSec2RadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1, 1, 10, 1)
)
hmSec2RadiusAuthServerEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2RadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    hmSec2RadiusAuthServerEntry.setStatus("current")


class _HmSec2RadiusAuthServerIndex_Type(Integer32):
    """Custom type hmSec2RadiusAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HmSec2RadiusAuthServerIndex_Type.__name__ = "Integer32"
_HmSec2RadiusAuthServerIndex_Object = MibTableColumn
hmSec2RadiusAuthServerIndex = _HmSec2RadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1, 1, 10, 1, 1),
    _HmSec2RadiusAuthServerIndex_Type()
)
hmSec2RadiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmSec2RadiusAuthServerIndex.setStatus("current")
_HmSec2RadiusAuthServerAddress_Type = IpAddress
_HmSec2RadiusAuthServerAddress_Object = MibTableColumn
hmSec2RadiusAuthServerAddress = _HmSec2RadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1, 1, 10, 1, 2),
    _HmSec2RadiusAuthServerAddress_Type()
)
hmSec2RadiusAuthServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RadiusAuthServerAddress.setStatus("current")


class _HmSec2RadiusAuthServerPort_Type(Integer32):
    """Custom type hmSec2RadiusAuthServerPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HmSec2RadiusAuthServerPort_Type.__name__ = "Integer32"
_HmSec2RadiusAuthServerPort_Object = MibTableColumn
hmSec2RadiusAuthServerPort = _HmSec2RadiusAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1, 1, 10, 1, 3),
    _HmSec2RadiusAuthServerPort_Type()
)
hmSec2RadiusAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RadiusAuthServerPort.setStatus("current")


class _HmSec2RadiusAuthServerSecret_Type(DisplayString):
    """Custom type hmSec2RadiusAuthServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2RadiusAuthServerSecret_Type.__name__ = "DisplayString"
_HmSec2RadiusAuthServerSecret_Object = MibTableColumn
hmSec2RadiusAuthServerSecret = _HmSec2RadiusAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1, 1, 10, 1, 4),
    _HmSec2RadiusAuthServerSecret_Type()
)
hmSec2RadiusAuthServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RadiusAuthServerSecret.setStatus("current")
_HmSec2RadiusAuthServerStatus_Type = RowStatus
_HmSec2RadiusAuthServerStatus_Object = MibTableColumn
hmSec2RadiusAuthServerStatus = _HmSec2RadiusAuthServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 3, 1, 1, 10, 1, 5),
    _HmSec2RadiusAuthServerStatus_Type()
)
hmSec2RadiusAuthServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RadiusAuthServerStatus.setStatus("current")
_HmSec2Firewall_ObjectIdentity = ObjectIdentity
hmSec2Firewall = _HmSec2Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11)
)
_HmSec2FirewallDenialOfServiceGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallDenialOfServiceGroup = _HmSec2FirewallDenialOfServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1)
)
_HmSec2FirewallDenialOfServiceVars_ObjectIdentity = ObjectIdentity
hmSec2FirewallDenialOfServiceVars = _HmSec2FirewallDenialOfServiceVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1)
)


class _HmSec2FwDosInSynLimit_Type(Integer32):
    """Custom type hmSec2FwDosInSynLimit based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_HmSec2FwDosInSynLimit_Type.__name__ = "Integer32"
_HmSec2FwDosInSynLimit_Object = MibScalar
hmSec2FwDosInSynLimit = _HmSec2FwDosInSynLimit_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 1),
    _HmSec2FwDosInSynLimit_Type()
)
hmSec2FwDosInSynLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosInSynLimit.setStatus("current")


class _HmSec2FwDosOutSynLimit_Type(Integer32):
    """Custom type hmSec2FwDosOutSynLimit based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_HmSec2FwDosOutSynLimit_Type.__name__ = "Integer32"
_HmSec2FwDosOutSynLimit_Object = MibScalar
hmSec2FwDosOutSynLimit = _HmSec2FwDosOutSynLimit_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 2),
    _HmSec2FwDosOutSynLimit_Type()
)
hmSec2FwDosOutSynLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosOutSynLimit.setStatus("current")


class _HmSec2FwDosInPingLimit_Type(Integer32):
    """Custom type hmSec2FwDosInPingLimit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_HmSec2FwDosInPingLimit_Type.__name__ = "Integer32"
_HmSec2FwDosInPingLimit_Object = MibScalar
hmSec2FwDosInPingLimit = _HmSec2FwDosInPingLimit_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 3),
    _HmSec2FwDosInPingLimit_Type()
)
hmSec2FwDosInPingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosInPingLimit.setStatus("current")


class _HmSec2FwDosOutPingLimit_Type(Integer32):
    """Custom type hmSec2FwDosOutPingLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_HmSec2FwDosOutPingLimit_Type.__name__ = "Integer32"
_HmSec2FwDosOutPingLimit_Object = MibScalar
hmSec2FwDosOutPingLimit = _HmSec2FwDosOutPingLimit_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 4),
    _HmSec2FwDosOutPingLimit_Type()
)
hmSec2FwDosOutPingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosOutPingLimit.setStatus("current")


class _HmSec2FwDosInArpLimit_Type(Integer32):
    """Custom type hmSec2FwDosInArpLimit based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_HmSec2FwDosInArpLimit_Type.__name__ = "Integer32"
_HmSec2FwDosInArpLimit_Object = MibScalar
hmSec2FwDosInArpLimit = _HmSec2FwDosInArpLimit_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 5),
    _HmSec2FwDosInArpLimit_Type()
)
hmSec2FwDosInArpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosInArpLimit.setStatus("current")


class _HmSec2FwDosOutArpLimit_Type(Integer32):
    """Custom type hmSec2FwDosOutArpLimit based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_HmSec2FwDosOutArpLimit_Type.__name__ = "Integer32"
_HmSec2FwDosOutArpLimit_Object = MibScalar
hmSec2FwDosOutArpLimit = _HmSec2FwDosOutArpLimit_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 6),
    _HmSec2FwDosOutArpLimit_Type()
)
hmSec2FwDosOutArpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosOutArpLimit.setStatus("current")


class _HmSec2FwDosInSynLimitLog_Type(Integer32):
    """Custom type hmSec2FwDosInSynLimitLog based on Integer32"""
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


_HmSec2FwDosInSynLimitLog_Type.__name__ = "Integer32"
_HmSec2FwDosInSynLimitLog_Object = MibScalar
hmSec2FwDosInSynLimitLog = _HmSec2FwDosInSynLimitLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 7),
    _HmSec2FwDosInSynLimitLog_Type()
)
hmSec2FwDosInSynLimitLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosInSynLimitLog.setStatus("current")


class _HmSec2FwDosOutSynLimitLog_Type(Integer32):
    """Custom type hmSec2FwDosOutSynLimitLog based on Integer32"""
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


_HmSec2FwDosOutSynLimitLog_Type.__name__ = "Integer32"
_HmSec2FwDosOutSynLimitLog_Object = MibScalar
hmSec2FwDosOutSynLimitLog = _HmSec2FwDosOutSynLimitLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 8),
    _HmSec2FwDosOutSynLimitLog_Type()
)
hmSec2FwDosOutSynLimitLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosOutSynLimitLog.setStatus("current")


class _HmSec2FwDosInPingLimitLog_Type(Integer32):
    """Custom type hmSec2FwDosInPingLimitLog based on Integer32"""
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


_HmSec2FwDosInPingLimitLog_Type.__name__ = "Integer32"
_HmSec2FwDosInPingLimitLog_Object = MibScalar
hmSec2FwDosInPingLimitLog = _HmSec2FwDosInPingLimitLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 9),
    _HmSec2FwDosInPingLimitLog_Type()
)
hmSec2FwDosInPingLimitLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosInPingLimitLog.setStatus("current")


class _HmSec2FwDosOutPingLimitLog_Type(Integer32):
    """Custom type hmSec2FwDosOutPingLimitLog based on Integer32"""
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


_HmSec2FwDosOutPingLimitLog_Type.__name__ = "Integer32"
_HmSec2FwDosOutPingLimitLog_Object = MibScalar
hmSec2FwDosOutPingLimitLog = _HmSec2FwDosOutPingLimitLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 10),
    _HmSec2FwDosOutPingLimitLog_Type()
)
hmSec2FwDosOutPingLimitLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosOutPingLimitLog.setStatus("current")


class _HmSec2FwDosInArpLimitLog_Type(Integer32):
    """Custom type hmSec2FwDosInArpLimitLog based on Integer32"""
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


_HmSec2FwDosInArpLimitLog_Type.__name__ = "Integer32"
_HmSec2FwDosInArpLimitLog_Object = MibScalar
hmSec2FwDosInArpLimitLog = _HmSec2FwDosInArpLimitLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 11),
    _HmSec2FwDosInArpLimitLog_Type()
)
hmSec2FwDosInArpLimitLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosInArpLimitLog.setStatus("current")


class _HmSec2FwDosOutArpLimitLog_Type(Integer32):
    """Custom type hmSec2FwDosOutArpLimitLog based on Integer32"""
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


_HmSec2FwDosOutArpLimitLog_Type.__name__ = "Integer32"
_HmSec2FwDosOutArpLimitLog_Object = MibScalar
hmSec2FwDosOutArpLimitLog = _HmSec2FwDosOutArpLimitLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 1, 1, 12),
    _HmSec2FwDosOutArpLimitLog_Type()
)
hmSec2FwDosOutArpLimitLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwDosOutArpLimitLog.setStatus("current")
_HmSec2FirewallL2PacketFilterGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallL2PacketFilterGroup = _HmSec2FirewallL2PacketFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2)
)
_HmSec2FirewallL2PfIncomingGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallL2PfIncomingGroup = _HmSec2FirewallL2PfIncomingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1)
)
_HmSec2FwL2PfInTable_Object = MibTable
hmSec2FwL2PfInTable = _HmSec2FwL2PfInTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hmSec2FwL2PfInTable.setStatus("current")
_HmSec2FwL2PfInEntry_Object = MibTableRow
hmSec2FwL2PfInEntry = _HmSec2FwL2PfInEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1, 1)
)
hmSec2FwL2PfInEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwL2PfInIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FwL2PfInEntry.setStatus("current")
_HmSec2FwL2PfInIndex_Type = Integer32
_HmSec2FwL2PfInIndex_Object = MibTableColumn
hmSec2FwL2PfInIndex = _HmSec2FwL2PfInIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1, 1, 1),
    _HmSec2FwL2PfInIndex_Type()
)
hmSec2FwL2PfInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL2PfInIndex.setStatus("current")


class _HmSec2FwL2PfInSrcAddr_Type(DisplayString):
    """Custom type hmSec2FwL2PfInSrcAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL2PfInSrcAddr_Type.__name__ = "DisplayString"
_HmSec2FwL2PfInSrcAddr_Object = MibTableColumn
hmSec2FwL2PfInSrcAddr = _HmSec2FwL2PfInSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1, 1, 2),
    _HmSec2FwL2PfInSrcAddr_Type()
)
hmSec2FwL2PfInSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfInSrcAddr.setStatus("current")


class _HmSec2FwL2PfInDstAddr_Type(DisplayString):
    """Custom type hmSec2FwL2PfInDstAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL2PfInDstAddr_Type.__name__ = "DisplayString"
_HmSec2FwL2PfInDstAddr_Object = MibTableColumn
hmSec2FwL2PfInDstAddr = _HmSec2FwL2PfInDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1, 1, 4),
    _HmSec2FwL2PfInDstAddr_Type()
)
hmSec2FwL2PfInDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfInDstAddr.setStatus("current")


class _HmSec2FwL2PfInProto_Type(DisplayString):
    """Custom type hmSec2FwL2PfInProto based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmSec2FwL2PfInProto_Type.__name__ = "DisplayString"
_HmSec2FwL2PfInProto_Object = MibTableColumn
hmSec2FwL2PfInProto = _HmSec2FwL2PfInProto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1, 1, 6),
    _HmSec2FwL2PfInProto_Type()
)
hmSec2FwL2PfInProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfInProto.setStatus("current")


class _HmSec2FwL2PfInAction_Type(Integer32):
    """Custom type hmSec2FwL2PfInAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2))
    )


_HmSec2FwL2PfInAction_Type.__name__ = "Integer32"
_HmSec2FwL2PfInAction_Object = MibTableColumn
hmSec2FwL2PfInAction = _HmSec2FwL2PfInAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1, 1, 7),
    _HmSec2FwL2PfInAction_Type()
)
hmSec2FwL2PfInAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfInAction.setStatus("current")


class _HmSec2FwL2PfInLog_Type(Integer32):
    """Custom type hmSec2FwL2PfInLog based on Integer32"""
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
          ("logAndTrap", 3))
    )


_HmSec2FwL2PfInLog_Type.__name__ = "Integer32"
_HmSec2FwL2PfInLog_Object = MibTableColumn
hmSec2FwL2PfInLog = _HmSec2FwL2PfInLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1, 1, 8),
    _HmSec2FwL2PfInLog_Type()
)
hmSec2FwL2PfInLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfInLog.setStatus("current")


class _HmSec2FwL2PfInDesc_Type(DisplayString):
    """Custom type hmSec2FwL2PfInDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwL2PfInDesc_Type.__name__ = "DisplayString"
_HmSec2FwL2PfInDesc_Object = MibTableColumn
hmSec2FwL2PfInDesc = _HmSec2FwL2PfInDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1, 1, 9),
    _HmSec2FwL2PfInDesc_Type()
)
hmSec2FwL2PfInDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfInDesc.setStatus("current")


class _HmSec2FwL2PfInErrorText_Type(DisplayString):
    """Custom type hmSec2FwL2PfInErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwL2PfInErrorText_Type.__name__ = "DisplayString"
_HmSec2FwL2PfInErrorText_Object = MibTableColumn
hmSec2FwL2PfInErrorText = _HmSec2FwL2PfInErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1, 1, 10),
    _HmSec2FwL2PfInErrorText_Type()
)
hmSec2FwL2PfInErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL2PfInErrorText.setStatus("current")
_HmSec2FwL2PfInRowStatus_Type = RowStatus
_HmSec2FwL2PfInRowStatus_Object = MibTableColumn
hmSec2FwL2PfInRowStatus = _HmSec2FwL2PfInRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 1, 1, 1, 11),
    _HmSec2FwL2PfInRowStatus_Type()
)
hmSec2FwL2PfInRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfInRowStatus.setStatus("current")
_HmSec2FirewallL2PfOutgoingGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallL2PfOutgoingGroup = _HmSec2FirewallL2PfOutgoingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2)
)
_HmSec2FwL2PfOutTable_Object = MibTable
hmSec2FwL2PfOutTable = _HmSec2FwL2PfOutTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutTable.setStatus("current")
_HmSec2FwL2PfOutEntry_Object = MibTableRow
hmSec2FwL2PfOutEntry = _HmSec2FwL2PfOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1, 1)
)
hmSec2FwL2PfOutEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwL2PfOutIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutEntry.setStatus("current")
_HmSec2FwL2PfOutIndex_Type = Integer32
_HmSec2FwL2PfOutIndex_Object = MibTableColumn
hmSec2FwL2PfOutIndex = _HmSec2FwL2PfOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1, 1, 1),
    _HmSec2FwL2PfOutIndex_Type()
)
hmSec2FwL2PfOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutIndex.setStatus("current")


class _HmSec2FwL2PfOutSrcAddr_Type(DisplayString):
    """Custom type hmSec2FwL2PfOutSrcAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL2PfOutSrcAddr_Type.__name__ = "DisplayString"
_HmSec2FwL2PfOutSrcAddr_Object = MibTableColumn
hmSec2FwL2PfOutSrcAddr = _HmSec2FwL2PfOutSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1, 1, 2),
    _HmSec2FwL2PfOutSrcAddr_Type()
)
hmSec2FwL2PfOutSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutSrcAddr.setStatus("current")


class _HmSec2FwL2PfOutDstAddr_Type(DisplayString):
    """Custom type hmSec2FwL2PfOutDstAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL2PfOutDstAddr_Type.__name__ = "DisplayString"
_HmSec2FwL2PfOutDstAddr_Object = MibTableColumn
hmSec2FwL2PfOutDstAddr = _HmSec2FwL2PfOutDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1, 1, 4),
    _HmSec2FwL2PfOutDstAddr_Type()
)
hmSec2FwL2PfOutDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutDstAddr.setStatus("current")


class _HmSec2FwL2PfOutProto_Type(DisplayString):
    """Custom type hmSec2FwL2PfOutProto based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmSec2FwL2PfOutProto_Type.__name__ = "DisplayString"
_HmSec2FwL2PfOutProto_Object = MibTableColumn
hmSec2FwL2PfOutProto = _HmSec2FwL2PfOutProto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1, 1, 6),
    _HmSec2FwL2PfOutProto_Type()
)
hmSec2FwL2PfOutProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutProto.setStatus("current")


class _HmSec2FwL2PfOutAction_Type(Integer32):
    """Custom type hmSec2FwL2PfOutAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2))
    )


_HmSec2FwL2PfOutAction_Type.__name__ = "Integer32"
_HmSec2FwL2PfOutAction_Object = MibTableColumn
hmSec2FwL2PfOutAction = _HmSec2FwL2PfOutAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1, 1, 7),
    _HmSec2FwL2PfOutAction_Type()
)
hmSec2FwL2PfOutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutAction.setStatus("current")


class _HmSec2FwL2PfOutLog_Type(Integer32):
    """Custom type hmSec2FwL2PfOutLog based on Integer32"""
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
          ("logAndTrap", 3))
    )


_HmSec2FwL2PfOutLog_Type.__name__ = "Integer32"
_HmSec2FwL2PfOutLog_Object = MibTableColumn
hmSec2FwL2PfOutLog = _HmSec2FwL2PfOutLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1, 1, 8),
    _HmSec2FwL2PfOutLog_Type()
)
hmSec2FwL2PfOutLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutLog.setStatus("current")


class _HmSec2FwL2PfOutDesc_Type(DisplayString):
    """Custom type hmSec2FwL2PfOutDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwL2PfOutDesc_Type.__name__ = "DisplayString"
_HmSec2FwL2PfOutDesc_Object = MibTableColumn
hmSec2FwL2PfOutDesc = _HmSec2FwL2PfOutDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1, 1, 9),
    _HmSec2FwL2PfOutDesc_Type()
)
hmSec2FwL2PfOutDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutDesc.setStatus("current")


class _HmSec2FwL2PfOutErrorText_Type(DisplayString):
    """Custom type hmSec2FwL2PfOutErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwL2PfOutErrorText_Type.__name__ = "DisplayString"
_HmSec2FwL2PfOutErrorText_Object = MibTableColumn
hmSec2FwL2PfOutErrorText = _HmSec2FwL2PfOutErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1, 1, 10),
    _HmSec2FwL2PfOutErrorText_Type()
)
hmSec2FwL2PfOutErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutErrorText.setStatus("current")
_HmSec2FwL2PfOutRowStatus_Type = RowStatus
_HmSec2FwL2PfOutRowStatus_Object = MibTableColumn
hmSec2FwL2PfOutRowStatus = _HmSec2FwL2PfOutRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 2, 2, 1, 1, 11),
    _HmSec2FwL2PfOutRowStatus_Type()
)
hmSec2FwL2PfOutRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL2PfOutRowStatus.setStatus("current")
_HmSec2FirewallL3PacketFilterGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallL3PacketFilterGroup = _HmSec2FirewallL3PacketFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3)
)
_HmSec2FirewallL3PfIncomingGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallL3PfIncomingGroup = _HmSec2FirewallL3PfIncomingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1)
)
_HmSec2FwL3PfInTable_Object = MibTable
hmSec2FwL3PfInTable = _HmSec2FwL3PfInTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hmSec2FwL3PfInTable.setStatus("current")
_HmSec2FwL3PfInEntry_Object = MibTableRow
hmSec2FwL3PfInEntry = _HmSec2FwL3PfInEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1)
)
hmSec2FwL3PfInEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwL3PfInIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FwL3PfInEntry.setStatus("current")
_HmSec2FwL3PfInIndex_Type = Integer32
_HmSec2FwL3PfInIndex_Object = MibTableColumn
hmSec2FwL3PfInIndex = _HmSec2FwL3PfInIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 1),
    _HmSec2FwL3PfInIndex_Type()
)
hmSec2FwL3PfInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInIndex.setStatus("current")


class _HmSec2FwL3PfInSrcNet_Type(DisplayString):
    """Custom type hmSec2FwL3PfInSrcNet based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL3PfInSrcNet_Type.__name__ = "DisplayString"
_HmSec2FwL3PfInSrcNet_Object = MibTableColumn
hmSec2FwL3PfInSrcNet = _HmSec2FwL3PfInSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 2),
    _HmSec2FwL3PfInSrcNet_Type()
)
hmSec2FwL3PfInSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInSrcNet.setStatus("current")


class _HmSec2FwL3PfInSrcPort_Type(DisplayString):
    """Custom type hmSec2FwL3PfInSrcPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL3PfInSrcPort_Type.__name__ = "DisplayString"
_HmSec2FwL3PfInSrcPort_Object = MibTableColumn
hmSec2FwL3PfInSrcPort = _HmSec2FwL3PfInSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 3),
    _HmSec2FwL3PfInSrcPort_Type()
)
hmSec2FwL3PfInSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInSrcPort.setStatus("current")


class _HmSec2FwL3PfInDstNet_Type(DisplayString):
    """Custom type hmSec2FwL3PfInDstNet based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL3PfInDstNet_Type.__name__ = "DisplayString"
_HmSec2FwL3PfInDstNet_Object = MibTableColumn
hmSec2FwL3PfInDstNet = _HmSec2FwL3PfInDstNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 4),
    _HmSec2FwL3PfInDstNet_Type()
)
hmSec2FwL3PfInDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInDstNet.setStatus("current")


class _HmSec2FwL3PfInDstPort_Type(DisplayString):
    """Custom type hmSec2FwL3PfInDstPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL3PfInDstPort_Type.__name__ = "DisplayString"
_HmSec2FwL3PfInDstPort_Object = MibTableColumn
hmSec2FwL3PfInDstPort = _HmSec2FwL3PfInDstPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 5),
    _HmSec2FwL3PfInDstPort_Type()
)
hmSec2FwL3PfInDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInDstPort.setStatus("current")


class _HmSec2FwL3PfInProto_Type(DisplayString):
    """Custom type hmSec2FwL3PfInProto based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmSec2FwL3PfInProto_Type.__name__ = "DisplayString"
_HmSec2FwL3PfInProto_Object = MibTableColumn
hmSec2FwL3PfInProto = _HmSec2FwL3PfInProto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 6),
    _HmSec2FwL3PfInProto_Type()
)
hmSec2FwL3PfInProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInProto.setStatus("current")


class _HmSec2FwL3PfInAction_Type(Integer32):
    """Custom type hmSec2FwL3PfInAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3))
    )


_HmSec2FwL3PfInAction_Type.__name__ = "Integer32"
_HmSec2FwL3PfInAction_Object = MibTableColumn
hmSec2FwL3PfInAction = _HmSec2FwL3PfInAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 7),
    _HmSec2FwL3PfInAction_Type()
)
hmSec2FwL3PfInAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInAction.setStatus("current")


class _HmSec2FwL3PfInLog_Type(Integer32):
    """Custom type hmSec2FwL3PfInLog based on Integer32"""
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
          ("logAndTrap", 3))
    )


_HmSec2FwL3PfInLog_Type.__name__ = "Integer32"
_HmSec2FwL3PfInLog_Object = MibTableColumn
hmSec2FwL3PfInLog = _HmSec2FwL3PfInLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 8),
    _HmSec2FwL3PfInLog_Type()
)
hmSec2FwL3PfInLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInLog.setStatus("current")


class _HmSec2FwL3PfInDesc_Type(DisplayString):
    """Custom type hmSec2FwL3PfInDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwL3PfInDesc_Type.__name__ = "DisplayString"
_HmSec2FwL3PfInDesc_Object = MibTableColumn
hmSec2FwL3PfInDesc = _HmSec2FwL3PfInDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 9),
    _HmSec2FwL3PfInDesc_Type()
)
hmSec2FwL3PfInDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInDesc.setStatus("current")


class _HmSec2FwL3PfInErrorText_Type(DisplayString):
    """Custom type hmSec2FwL3PfInErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwL3PfInErrorText_Type.__name__ = "DisplayString"
_HmSec2FwL3PfInErrorText_Object = MibTableColumn
hmSec2FwL3PfInErrorText = _HmSec2FwL3PfInErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 10),
    _HmSec2FwL3PfInErrorText_Type()
)
hmSec2FwL3PfInErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInErrorText.setStatus("current")
_HmSec2FwL3PfInRowStatus_Type = RowStatus
_HmSec2FwL3PfInRowStatus_Object = MibTableColumn
hmSec2FwL3PfInRowStatus = _HmSec2FwL3PfInRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 1, 1, 11),
    _HmSec2FwL3PfInRowStatus_Type()
)
hmSec2FwL3PfInRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInRowStatus.setStatus("current")


class _HmSec2FwL3PfInLogNonMatching_Type(Integer32):
    """Custom type hmSec2FwL3PfInLogNonMatching based on Integer32"""
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


_HmSec2FwL3PfInLogNonMatching_Type.__name__ = "Integer32"
_HmSec2FwL3PfInLogNonMatching_Object = MibScalar
hmSec2FwL3PfInLogNonMatching = _HmSec2FwL3PfInLogNonMatching_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 1, 2),
    _HmSec2FwL3PfInLogNonMatching_Type()
)
hmSec2FwL3PfInLogNonMatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfInLogNonMatching.setStatus("current")
_HmSec2FirewallL3PfOutgoingGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallL3PfOutgoingGroup = _HmSec2FirewallL3PfOutgoingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2)
)
_HmSec2FwL3PfOutTable_Object = MibTable
hmSec2FwL3PfOutTable = _HmSec2FwL3PfOutTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutTable.setStatus("current")
_HmSec2FwL3PfOutEntry_Object = MibTableRow
hmSec2FwL3PfOutEntry = _HmSec2FwL3PfOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1)
)
hmSec2FwL3PfOutEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwL3PfOutIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutEntry.setStatus("current")
_HmSec2FwL3PfOutIndex_Type = Integer32
_HmSec2FwL3PfOutIndex_Object = MibTableColumn
hmSec2FwL3PfOutIndex = _HmSec2FwL3PfOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 1),
    _HmSec2FwL3PfOutIndex_Type()
)
hmSec2FwL3PfOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutIndex.setStatus("current")


class _HmSec2FwL3PfOutSrcNet_Type(DisplayString):
    """Custom type hmSec2FwL3PfOutSrcNet based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL3PfOutSrcNet_Type.__name__ = "DisplayString"
_HmSec2FwL3PfOutSrcNet_Object = MibTableColumn
hmSec2FwL3PfOutSrcNet = _HmSec2FwL3PfOutSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 2),
    _HmSec2FwL3PfOutSrcNet_Type()
)
hmSec2FwL3PfOutSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutSrcNet.setStatus("current")


class _HmSec2FwL3PfOutSrcPort_Type(DisplayString):
    """Custom type hmSec2FwL3PfOutSrcPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL3PfOutSrcPort_Type.__name__ = "DisplayString"
_HmSec2FwL3PfOutSrcPort_Object = MibTableColumn
hmSec2FwL3PfOutSrcPort = _HmSec2FwL3PfOutSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 3),
    _HmSec2FwL3PfOutSrcPort_Type()
)
hmSec2FwL3PfOutSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutSrcPort.setStatus("current")


class _HmSec2FwL3PfOutDstNet_Type(DisplayString):
    """Custom type hmSec2FwL3PfOutDstNet based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL3PfOutDstNet_Type.__name__ = "DisplayString"
_HmSec2FwL3PfOutDstNet_Object = MibTableColumn
hmSec2FwL3PfOutDstNet = _HmSec2FwL3PfOutDstNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 4),
    _HmSec2FwL3PfOutDstNet_Type()
)
hmSec2FwL3PfOutDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutDstNet.setStatus("current")


class _HmSec2FwL3PfOutDstPort_Type(DisplayString):
    """Custom type hmSec2FwL3PfOutDstPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL3PfOutDstPort_Type.__name__ = "DisplayString"
_HmSec2FwL3PfOutDstPort_Object = MibTableColumn
hmSec2FwL3PfOutDstPort = _HmSec2FwL3PfOutDstPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 5),
    _HmSec2FwL3PfOutDstPort_Type()
)
hmSec2FwL3PfOutDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutDstPort.setStatus("current")


class _HmSec2FwL3PfOutProto_Type(DisplayString):
    """Custom type hmSec2FwL3PfOutProto based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmSec2FwL3PfOutProto_Type.__name__ = "DisplayString"
_HmSec2FwL3PfOutProto_Object = MibTableColumn
hmSec2FwL3PfOutProto = _HmSec2FwL3PfOutProto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 6),
    _HmSec2FwL3PfOutProto_Type()
)
hmSec2FwL3PfOutProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutProto.setStatus("current")


class _HmSec2FwL3PfOutAction_Type(Integer32):
    """Custom type hmSec2FwL3PfOutAction based on Integer32"""
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
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3))
    )


_HmSec2FwL3PfOutAction_Type.__name__ = "Integer32"
_HmSec2FwL3PfOutAction_Object = MibTableColumn
hmSec2FwL3PfOutAction = _HmSec2FwL3PfOutAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 7),
    _HmSec2FwL3PfOutAction_Type()
)
hmSec2FwL3PfOutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutAction.setStatus("current")


class _HmSec2FwL3PfOutLog_Type(Integer32):
    """Custom type hmSec2FwL3PfOutLog based on Integer32"""
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
          ("logAndTrap", 3))
    )


_HmSec2FwL3PfOutLog_Type.__name__ = "Integer32"
_HmSec2FwL3PfOutLog_Object = MibTableColumn
hmSec2FwL3PfOutLog = _HmSec2FwL3PfOutLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 8),
    _HmSec2FwL3PfOutLog_Type()
)
hmSec2FwL3PfOutLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutLog.setStatus("current")


class _HmSec2FwL3PfOutDesc_Type(DisplayString):
    """Custom type hmSec2FwL3PfOutDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwL3PfOutDesc_Type.__name__ = "DisplayString"
_HmSec2FwL3PfOutDesc_Object = MibTableColumn
hmSec2FwL3PfOutDesc = _HmSec2FwL3PfOutDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 9),
    _HmSec2FwL3PfOutDesc_Type()
)
hmSec2FwL3PfOutDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutDesc.setStatus("current")


class _HmSec2FwL3PfOutErrorText_Type(DisplayString):
    """Custom type hmSec2FwL3PfOutErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwL3PfOutErrorText_Type.__name__ = "DisplayString"
_HmSec2FwL3PfOutErrorText_Object = MibTableColumn
hmSec2FwL3PfOutErrorText = _HmSec2FwL3PfOutErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 10),
    _HmSec2FwL3PfOutErrorText_Type()
)
hmSec2FwL3PfOutErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutErrorText.setStatus("current")
_HmSec2FwL3PfOutRowStatus_Type = RowStatus
_HmSec2FwL3PfOutRowStatus_Object = MibTableColumn
hmSec2FwL3PfOutRowStatus = _HmSec2FwL3PfOutRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 1, 1, 11),
    _HmSec2FwL3PfOutRowStatus_Type()
)
hmSec2FwL3PfOutRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutRowStatus.setStatus("current")


class _HmSec2FwL3PfOutLogNonMatching_Type(Integer32):
    """Custom type hmSec2FwL3PfOutLogNonMatching based on Integer32"""
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


_HmSec2FwL3PfOutLogNonMatching_Type.__name__ = "Integer32"
_HmSec2FwL3PfOutLogNonMatching_Object = MibScalar
hmSec2FwL3PfOutLogNonMatching = _HmSec2FwL3PfOutLogNonMatching_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 2, 2),
    _HmSec2FwL3PfOutLogNonMatching_Type()
)
hmSec2FwL3PfOutLogNonMatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3PfOutLogNonMatching.setStatus("current")
_HmSec2FirewallL3TemplateGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallL3TemplateGroup = _HmSec2FirewallL3TemplateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3)
)
_HmSec2FwL3TplIdTable_Object = MibTable
hmSec2FwL3TplIdTable = _HmSec2FwL3TplIdTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hmSec2FwL3TplIdTable.setStatus("current")
_HmSec2FwL3TplIdEntry_Object = MibTableRow
hmSec2FwL3TplIdEntry = _HmSec2FwL3TplIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 1, 1)
)
hmSec2FwL3TplIdEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwL3TplIdIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FwL3TplIdEntry.setStatus("current")
_HmSec2FwL3TplIdIndex_Type = Integer32
_HmSec2FwL3TplIdIndex_Object = MibTableColumn
hmSec2FwL3TplIdIndex = _HmSec2FwL3TplIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 1, 1, 1),
    _HmSec2FwL3TplIdIndex_Type()
)
hmSec2FwL3TplIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL3TplIdIndex.setStatus("current")


class _HmSec2FwL3TplIdName_Type(DisplayString):
    """Custom type hmSec2FwL3TplIdName based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_HmSec2FwL3TplIdName_Type.__name__ = "DisplayString"
_HmSec2FwL3TplIdName_Object = MibTableColumn
hmSec2FwL3TplIdName = _HmSec2FwL3TplIdName_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 1, 1, 2),
    _HmSec2FwL3TplIdName_Type()
)
hmSec2FwL3TplIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3TplIdName.setStatus("current")
_HmSec2FwL3TplIdRowStatus_Type = RowStatus
_HmSec2FwL3TplIdRowStatus_Object = MibTableColumn
hmSec2FwL3TplIdRowStatus = _HmSec2FwL3TplIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 1, 1, 3),
    _HmSec2FwL3TplIdRowStatus_Type()
)
hmSec2FwL3TplIdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3TplIdRowStatus.setStatus("current")
_HmSec2FwL3TplNetTable_Object = MibTable
hmSec2FwL3TplNetTable = _HmSec2FwL3TplNetTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hmSec2FwL3TplNetTable.setStatus("current")
_HmSec2FwL3TplNetEntry_Object = MibTableRow
hmSec2FwL3TplNetEntry = _HmSec2FwL3TplNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 2, 1)
)
hmSec2FwL3TplNetEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwL3TplNetIdIndex"),
    (0, "ABBSECURITY2-MIB", "hmSec2FwL3TplNetIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FwL3TplNetEntry.setStatus("current")
_HmSec2FwL3TplNetIdIndex_Type = Integer32
_HmSec2FwL3TplNetIdIndex_Object = MibTableColumn
hmSec2FwL3TplNetIdIndex = _HmSec2FwL3TplNetIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 2, 1, 1),
    _HmSec2FwL3TplNetIdIndex_Type()
)
hmSec2FwL3TplNetIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL3TplNetIdIndex.setStatus("current")
_HmSec2FwL3TplNetIndex_Type = Integer32
_HmSec2FwL3TplNetIndex_Object = MibTableColumn
hmSec2FwL3TplNetIndex = _HmSec2FwL3TplNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 2, 1, 2),
    _HmSec2FwL3TplNetIndex_Type()
)
hmSec2FwL3TplNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwL3TplNetIndex.setStatus("current")


class _HmSec2FwL3TplNetAddr_Type(DisplayString):
    """Custom type hmSec2FwL3TplNetAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwL3TplNetAddr_Type.__name__ = "DisplayString"
_HmSec2FwL3TplNetAddr_Object = MibTableColumn
hmSec2FwL3TplNetAddr = _HmSec2FwL3TplNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 2, 1, 3),
    _HmSec2FwL3TplNetAddr_Type()
)
hmSec2FwL3TplNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3TplNetAddr.setStatus("current")
_HmSec2FwL3TplNetRowStatus_Type = RowStatus
_HmSec2FwL3TplNetRowStatus_Object = MibTableColumn
hmSec2FwL3TplNetRowStatus = _HmSec2FwL3TplNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 3, 3, 2, 1, 4),
    _HmSec2FwL3TplNetRowStatus_Type()
)
hmSec2FwL3TplNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwL3TplNetRowStatus.setStatus("current")
_HmSec2FirewallPppFilterGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallPppFilterGroup = _HmSec2FirewallPppFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4)
)
_HmSec2FirewallPppIncomingGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallPppIncomingGroup = _HmSec2FirewallPppIncomingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1)
)
_HmSec2FwPppInTable_Object = MibTable
hmSec2FwPppInTable = _HmSec2FwPppInTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hmSec2FwPppInTable.setStatus("current")
_HmSec2FwPppInEntry_Object = MibTableRow
hmSec2FwPppInEntry = _HmSec2FwPppInEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1)
)
hmSec2FwPppInEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwPppInIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FwPppInEntry.setStatus("current")
_HmSec2FwPppInIndex_Type = Integer32
_HmSec2FwPppInIndex_Object = MibTableColumn
hmSec2FwPppInIndex = _HmSec2FwPppInIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 1),
    _HmSec2FwPppInIndex_Type()
)
hmSec2FwPppInIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwPppInIndex.setStatus("current")


class _HmSec2FwPppInSrcNet_Type(DisplayString):
    """Custom type hmSec2FwPppInSrcNet based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwPppInSrcNet_Type.__name__ = "DisplayString"
_HmSec2FwPppInSrcNet_Object = MibTableColumn
hmSec2FwPppInSrcNet = _HmSec2FwPppInSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 2),
    _HmSec2FwPppInSrcNet_Type()
)
hmSec2FwPppInSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwPppInSrcNet.setStatus("current")


class _HmSec2FwPppInSrcPort_Type(DisplayString):
    """Custom type hmSec2FwPppInSrcPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwPppInSrcPort_Type.__name__ = "DisplayString"
_HmSec2FwPppInSrcPort_Object = MibTableColumn
hmSec2FwPppInSrcPort = _HmSec2FwPppInSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 3),
    _HmSec2FwPppInSrcPort_Type()
)
hmSec2FwPppInSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwPppInSrcPort.setStatus("current")


class _HmSec2FwPppInDstNet_Type(DisplayString):
    """Custom type hmSec2FwPppInDstNet based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwPppInDstNet_Type.__name__ = "DisplayString"
_HmSec2FwPppInDstNet_Object = MibTableColumn
hmSec2FwPppInDstNet = _HmSec2FwPppInDstNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 4),
    _HmSec2FwPppInDstNet_Type()
)
hmSec2FwPppInDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwPppInDstNet.setStatus("current")


class _HmSec2FwPppInDstPort_Type(DisplayString):
    """Custom type hmSec2FwPppInDstPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwPppInDstPort_Type.__name__ = "DisplayString"
_HmSec2FwPppInDstPort_Object = MibTableColumn
hmSec2FwPppInDstPort = _HmSec2FwPppInDstPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 5),
    _HmSec2FwPppInDstPort_Type()
)
hmSec2FwPppInDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwPppInDstPort.setStatus("current")


class _HmSec2FwPppInProto_Type(DisplayString):
    """Custom type hmSec2FwPppInProto based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmSec2FwPppInProto_Type.__name__ = "DisplayString"
_HmSec2FwPppInProto_Object = MibTableColumn
hmSec2FwPppInProto = _HmSec2FwPppInProto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 6),
    _HmSec2FwPppInProto_Type()
)
hmSec2FwPppInProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwPppInProto.setStatus("current")


class _HmSec2FwPppInAction_Type(Integer32):
    """Custom type hmSec2FwPppInAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3))
    )


_HmSec2FwPppInAction_Type.__name__ = "Integer32"
_HmSec2FwPppInAction_Object = MibTableColumn
hmSec2FwPppInAction = _HmSec2FwPppInAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 7),
    _HmSec2FwPppInAction_Type()
)
hmSec2FwPppInAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwPppInAction.setStatus("current")


class _HmSec2FwPppInLog_Type(Integer32):
    """Custom type hmSec2FwPppInLog based on Integer32"""
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
          ("logAndTrap", 3))
    )


_HmSec2FwPppInLog_Type.__name__ = "Integer32"
_HmSec2FwPppInLog_Object = MibTableColumn
hmSec2FwPppInLog = _HmSec2FwPppInLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 8),
    _HmSec2FwPppInLog_Type()
)
hmSec2FwPppInLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwPppInLog.setStatus("current")


class _HmSec2FwPppInDesc_Type(DisplayString):
    """Custom type hmSec2FwPppInDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwPppInDesc_Type.__name__ = "DisplayString"
_HmSec2FwPppInDesc_Object = MibTableColumn
hmSec2FwPppInDesc = _HmSec2FwPppInDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 9),
    _HmSec2FwPppInDesc_Type()
)
hmSec2FwPppInDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwPppInDesc.setStatus("current")


class _HmSec2FwPppInErrorText_Type(DisplayString):
    """Custom type hmSec2FwPppInErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwPppInErrorText_Type.__name__ = "DisplayString"
_HmSec2FwPppInErrorText_Object = MibTableColumn
hmSec2FwPppInErrorText = _HmSec2FwPppInErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 10),
    _HmSec2FwPppInErrorText_Type()
)
hmSec2FwPppInErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwPppInErrorText.setStatus("current")
_HmSec2FwPppInRowStatus_Type = RowStatus
_HmSec2FwPppInRowStatus_Object = MibTableColumn
hmSec2FwPppInRowStatus = _HmSec2FwPppInRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 1, 1, 11),
    _HmSec2FwPppInRowStatus_Type()
)
hmSec2FwPppInRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwPppInRowStatus.setStatus("current")


class _HmSec2FwPppInLogNonMatching_Type(Integer32):
    """Custom type hmSec2FwPppInLogNonMatching based on Integer32"""
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


_HmSec2FwPppInLogNonMatching_Type.__name__ = "Integer32"
_HmSec2FwPppInLogNonMatching_Object = MibScalar
hmSec2FwPppInLogNonMatching = _HmSec2FwPppInLogNonMatching_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 4, 1, 2),
    _HmSec2FwPppInLogNonMatching_Type()
)
hmSec2FwPppInLogNonMatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwPppInLogNonMatching.setStatus("current")
_HmSec2FirewallSnmpFilterGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallSnmpFilterGroup = _HmSec2FirewallSnmpFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5)
)
_HmSec2FwSnmpTable_Object = MibTable
hmSec2FwSnmpTable = _HmSec2FwSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5, 1)
)
if mibBuilder.loadTexts:
    hmSec2FwSnmpTable.setStatus("current")
_HmSec2FwSnmpEntry_Object = MibTableRow
hmSec2FwSnmpEntry = _HmSec2FwSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5, 1, 1)
)
hmSec2FwSnmpEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwSnmpIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FwSnmpEntry.setStatus("current")
_HmSec2FwSnmpIndex_Type = Integer32
_HmSec2FwSnmpIndex_Object = MibTableColumn
hmSec2FwSnmpIndex = _HmSec2FwSnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5, 1, 1, 1),
    _HmSec2FwSnmpIndex_Type()
)
hmSec2FwSnmpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwSnmpIndex.setStatus("current")


class _HmSec2FwSnmpInterface_Type(Integer32):
    """Custom type hmSec2FwSnmpInterface based on Integer32"""
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
        *(("int", 1),
          ("ext", 2),
          ("ppp", 3))
    )


_HmSec2FwSnmpInterface_Type.__name__ = "Integer32"
_HmSec2FwSnmpInterface_Object = MibTableColumn
hmSec2FwSnmpInterface = _HmSec2FwSnmpInterface_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5, 1, 1, 2),
    _HmSec2FwSnmpInterface_Type()
)
hmSec2FwSnmpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSnmpInterface.setStatus("current")


class _HmSec2FwSnmpSrcNet_Type(DisplayString):
    """Custom type hmSec2FwSnmpSrcNet based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwSnmpSrcNet_Type.__name__ = "DisplayString"
_HmSec2FwSnmpSrcNet_Object = MibTableColumn
hmSec2FwSnmpSrcNet = _HmSec2FwSnmpSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5, 1, 1, 3),
    _HmSec2FwSnmpSrcNet_Type()
)
hmSec2FwSnmpSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSnmpSrcNet.setStatus("current")


class _HmSec2FwSnmpAction_Type(Integer32):
    """Custom type hmSec2FwSnmpAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3))
    )


_HmSec2FwSnmpAction_Type.__name__ = "Integer32"
_HmSec2FwSnmpAction_Object = MibTableColumn
hmSec2FwSnmpAction = _HmSec2FwSnmpAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5, 1, 1, 4),
    _HmSec2FwSnmpAction_Type()
)
hmSec2FwSnmpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSnmpAction.setStatus("current")


class _HmSec2FwSnmpLog_Type(Integer32):
    """Custom type hmSec2FwSnmpLog based on Integer32"""
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
          ("logAndTrap", 3))
    )


_HmSec2FwSnmpLog_Type.__name__ = "Integer32"
_HmSec2FwSnmpLog_Object = MibTableColumn
hmSec2FwSnmpLog = _HmSec2FwSnmpLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5, 1, 1, 5),
    _HmSec2FwSnmpLog_Type()
)
hmSec2FwSnmpLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSnmpLog.setStatus("current")


class _HmSec2FwSnmpDesc_Type(DisplayString):
    """Custom type hmSec2FwSnmpDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwSnmpDesc_Type.__name__ = "DisplayString"
_HmSec2FwSnmpDesc_Object = MibTableColumn
hmSec2FwSnmpDesc = _HmSec2FwSnmpDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5, 1, 1, 6),
    _HmSec2FwSnmpDesc_Type()
)
hmSec2FwSnmpDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSnmpDesc.setStatus("current")


class _HmSec2FwSnmpErrorText_Type(DisplayString):
    """Custom type hmSec2FwSnmpErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwSnmpErrorText_Type.__name__ = "DisplayString"
_HmSec2FwSnmpErrorText_Object = MibTableColumn
hmSec2FwSnmpErrorText = _HmSec2FwSnmpErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5, 1, 1, 7),
    _HmSec2FwSnmpErrorText_Type()
)
hmSec2FwSnmpErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwSnmpErrorText.setStatus("current")
_HmSec2FwSnmpRowStatus_Type = RowStatus
_HmSec2FwSnmpRowStatus_Object = MibTableColumn
hmSec2FwSnmpRowStatus = _HmSec2FwSnmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 5, 1, 1, 8),
    _HmSec2FwSnmpRowStatus_Type()
)
hmSec2FwSnmpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSnmpRowStatus.setStatus("current")
_HmSec2FirewallSshFilterGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallSshFilterGroup = _HmSec2FirewallSshFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6)
)
_HmSec2FwSshTable_Object = MibTable
hmSec2FwSshTable = _HmSec2FwSshTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6, 1)
)
if mibBuilder.loadTexts:
    hmSec2FwSshTable.setStatus("current")
_HmSec2FwSshEntry_Object = MibTableRow
hmSec2FwSshEntry = _HmSec2FwSshEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6, 1, 1)
)
hmSec2FwSshEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwSshIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FwSshEntry.setStatus("current")
_HmSec2FwSshIndex_Type = Integer32
_HmSec2FwSshIndex_Object = MibTableColumn
hmSec2FwSshIndex = _HmSec2FwSshIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6, 1, 1, 1),
    _HmSec2FwSshIndex_Type()
)
hmSec2FwSshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwSshIndex.setStatus("current")


class _HmSec2FwSshInterface_Type(Integer32):
    """Custom type hmSec2FwSshInterface based on Integer32"""
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
        *(("int", 1),
          ("ext", 2),
          ("ppp", 3))
    )


_HmSec2FwSshInterface_Type.__name__ = "Integer32"
_HmSec2FwSshInterface_Object = MibTableColumn
hmSec2FwSshInterface = _HmSec2FwSshInterface_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6, 1, 1, 2),
    _HmSec2FwSshInterface_Type()
)
hmSec2FwSshInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSshInterface.setStatus("current")


class _HmSec2FwSshSrcNet_Type(DisplayString):
    """Custom type hmSec2FwSshSrcNet based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwSshSrcNet_Type.__name__ = "DisplayString"
_HmSec2FwSshSrcNet_Object = MibTableColumn
hmSec2FwSshSrcNet = _HmSec2FwSshSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6, 1, 1, 3),
    _HmSec2FwSshSrcNet_Type()
)
hmSec2FwSshSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSshSrcNet.setStatus("current")


class _HmSec2FwSshAction_Type(Integer32):
    """Custom type hmSec2FwSshAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3))
    )


_HmSec2FwSshAction_Type.__name__ = "Integer32"
_HmSec2FwSshAction_Object = MibTableColumn
hmSec2FwSshAction = _HmSec2FwSshAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6, 1, 1, 4),
    _HmSec2FwSshAction_Type()
)
hmSec2FwSshAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSshAction.setStatus("current")


class _HmSec2FwSshLog_Type(Integer32):
    """Custom type hmSec2FwSshLog based on Integer32"""
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
          ("logAndTrap", 3))
    )


_HmSec2FwSshLog_Type.__name__ = "Integer32"
_HmSec2FwSshLog_Object = MibTableColumn
hmSec2FwSshLog = _HmSec2FwSshLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6, 1, 1, 5),
    _HmSec2FwSshLog_Type()
)
hmSec2FwSshLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSshLog.setStatus("current")


class _HmSec2FwSshDesc_Type(DisplayString):
    """Custom type hmSec2FwSshDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwSshDesc_Type.__name__ = "DisplayString"
_HmSec2FwSshDesc_Object = MibTableColumn
hmSec2FwSshDesc = _HmSec2FwSshDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6, 1, 1, 6),
    _HmSec2FwSshDesc_Type()
)
hmSec2FwSshDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSshDesc.setStatus("current")


class _HmSec2FwSshErrorText_Type(DisplayString):
    """Custom type hmSec2FwSshErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwSshErrorText_Type.__name__ = "DisplayString"
_HmSec2FwSshErrorText_Object = MibTableColumn
hmSec2FwSshErrorText = _HmSec2FwSshErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6, 1, 1, 7),
    _HmSec2FwSshErrorText_Type()
)
hmSec2FwSshErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwSshErrorText.setStatus("current")
_HmSec2FwSshRowStatus_Type = RowStatus
_HmSec2FwSshRowStatus_Object = MibTableColumn
hmSec2FwSshRowStatus = _HmSec2FwSshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 6, 1, 1, 8),
    _HmSec2FwSshRowStatus_Type()
)
hmSec2FwSshRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwSshRowStatus.setStatus("current")
_HmSec2FirewallHttpsFilterGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallHttpsFilterGroup = _HmSec2FirewallHttpsFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7)
)
_HmSec2FwHttpsTable_Object = MibTable
hmSec2FwHttpsTable = _HmSec2FwHttpsTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7, 1)
)
if mibBuilder.loadTexts:
    hmSec2FwHttpsTable.setStatus("current")
_HmSec2FwHttpsEntry_Object = MibTableRow
hmSec2FwHttpsEntry = _HmSec2FwHttpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7, 1, 1)
)
hmSec2FwHttpsEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwHttpsIndex"),
)
if mibBuilder.loadTexts:
    hmSec2FwHttpsEntry.setStatus("current")
_HmSec2FwHttpsIndex_Type = Integer32
_HmSec2FwHttpsIndex_Object = MibTableColumn
hmSec2FwHttpsIndex = _HmSec2FwHttpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7, 1, 1, 1),
    _HmSec2FwHttpsIndex_Type()
)
hmSec2FwHttpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwHttpsIndex.setStatus("current")


class _HmSec2FwHttpsInterface_Type(Integer32):
    """Custom type hmSec2FwHttpsInterface based on Integer32"""
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
        *(("int", 1),
          ("ext", 2),
          ("ppp", 3))
    )


_HmSec2FwHttpsInterface_Type.__name__ = "Integer32"
_HmSec2FwHttpsInterface_Object = MibTableColumn
hmSec2FwHttpsInterface = _HmSec2FwHttpsInterface_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7, 1, 1, 2),
    _HmSec2FwHttpsInterface_Type()
)
hmSec2FwHttpsInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwHttpsInterface.setStatus("current")


class _HmSec2FwHttpsSrcNet_Type(DisplayString):
    """Custom type hmSec2FwHttpsSrcNet based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwHttpsSrcNet_Type.__name__ = "DisplayString"
_HmSec2FwHttpsSrcNet_Object = MibTableColumn
hmSec2FwHttpsSrcNet = _HmSec2FwHttpsSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7, 1, 1, 3),
    _HmSec2FwHttpsSrcNet_Type()
)
hmSec2FwHttpsSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwHttpsSrcNet.setStatus("current")


class _HmSec2FwHttpsAction_Type(Integer32):
    """Custom type hmSec2FwHttpsAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3))
    )


_HmSec2FwHttpsAction_Type.__name__ = "Integer32"
_HmSec2FwHttpsAction_Object = MibTableColumn
hmSec2FwHttpsAction = _HmSec2FwHttpsAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7, 1, 1, 4),
    _HmSec2FwHttpsAction_Type()
)
hmSec2FwHttpsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwHttpsAction.setStatus("current")


class _HmSec2FwHttpsLog_Type(Integer32):
    """Custom type hmSec2FwHttpsLog based on Integer32"""
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
          ("logAndTrap", 3))
    )


_HmSec2FwHttpsLog_Type.__name__ = "Integer32"
_HmSec2FwHttpsLog_Object = MibTableColumn
hmSec2FwHttpsLog = _HmSec2FwHttpsLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7, 1, 1, 5),
    _HmSec2FwHttpsLog_Type()
)
hmSec2FwHttpsLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwHttpsLog.setStatus("current")


class _HmSec2FwHttpsDesc_Type(DisplayString):
    """Custom type hmSec2FwHttpsDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwHttpsDesc_Type.__name__ = "DisplayString"
_HmSec2FwHttpsDesc_Object = MibTableColumn
hmSec2FwHttpsDesc = _HmSec2FwHttpsDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7, 1, 1, 6),
    _HmSec2FwHttpsDesc_Type()
)
hmSec2FwHttpsDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwHttpsDesc.setStatus("current")


class _HmSec2FwHttpsErrorText_Type(DisplayString):
    """Custom type hmSec2FwHttpsErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2FwHttpsErrorText_Type.__name__ = "DisplayString"
_HmSec2FwHttpsErrorText_Object = MibTableColumn
hmSec2FwHttpsErrorText = _HmSec2FwHttpsErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7, 1, 1, 7),
    _HmSec2FwHttpsErrorText_Type()
)
hmSec2FwHttpsErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwHttpsErrorText.setStatus("current")
_HmSec2FwHttpsRowStatus_Type = RowStatus
_HmSec2FwHttpsRowStatus_Object = MibTableColumn
hmSec2FwHttpsRowStatus = _HmSec2FwHttpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 7, 1, 1, 8),
    _HmSec2FwHttpsRowStatus_Type()
)
hmSec2FwHttpsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwHttpsRowStatus.setStatus("current")
_HmSec2UsrFwConfigGroup_ObjectIdentity = ObjectIdentity
hmSec2UsrFwConfigGroup = _HmSec2UsrFwConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8)
)


class _HmSec2UsrFwStatus_Type(Integer32):
    """Custom type hmSec2UsrFwStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("enable", 1),
          ("disable", 2))
    )


_HmSec2UsrFwStatus_Type.__name__ = "Integer32"
_HmSec2UsrFwStatus_Object = MibScalar
hmSec2UsrFwStatus = _HmSec2UsrFwStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 1),
    _HmSec2UsrFwStatus_Type()
)
hmSec2UsrFwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwStatus.setStatus("current")
_HmSec2UsrFwTemplateTable_Object = MibTable
hmSec2UsrFwTemplateTable = _HmSec2UsrFwTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 2)
)
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateTable.setStatus("current")
_HmSec2UsrFwTemplateEntry_Object = MibTableRow
hmSec2UsrFwTemplateEntry = _HmSec2UsrFwTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 2, 1)
)
hmSec2UsrFwTemplateEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2UsrFwTemplateIndex"),
)
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateEntry.setStatus("current")
_HmSec2UsrFwTemplateIndex_Type = Integer32
_HmSec2UsrFwTemplateIndex_Object = MibTableColumn
hmSec2UsrFwTemplateIndex = _HmSec2UsrFwTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 2, 1, 1),
    _HmSec2UsrFwTemplateIndex_Type()
)
hmSec2UsrFwTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateIndex.setStatus("current")


class _HmSec2UsrFwTemplateName_Type(SnmpAdminString):
    """Custom type hmSec2UsrFwTemplateName based on SnmpAdminString"""
    defaultValue = OctetString("(unnamed)")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HmSec2UsrFwTemplateName_Type.__name__ = "SnmpAdminString"
_HmSec2UsrFwTemplateName_Object = MibTableColumn
hmSec2UsrFwTemplateName = _HmSec2UsrFwTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 2, 1, 2),
    _HmSec2UsrFwTemplateName_Type()
)
hmSec2UsrFwTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateName.setStatus("current")


class _HmSec2UsrFwTemplateTimeout_Type(Integer32):
    """Custom type hmSec2UsrFwTemplateTimeout based on Integer32"""
    defaultValue = 28800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 604800),
    )


_HmSec2UsrFwTemplateTimeout_Type.__name__ = "Integer32"
_HmSec2UsrFwTemplateTimeout_Object = MibTableColumn
hmSec2UsrFwTemplateTimeout = _HmSec2UsrFwTemplateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 2, 1, 3),
    _HmSec2UsrFwTemplateTimeout_Type()
)
hmSec2UsrFwTemplateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateTimeout.setStatus("current")


class _HmSec2UsrFwTemplateTimeoutType_Type(Integer32):
    """Custom type hmSec2UsrFwTemplateTimeoutType based on Integer32"""
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


_HmSec2UsrFwTemplateTimeoutType_Type.__name__ = "Integer32"
_HmSec2UsrFwTemplateTimeoutType_Object = MibTableColumn
hmSec2UsrFwTemplateTimeoutType = _HmSec2UsrFwTemplateTimeoutType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 2, 1, 4),
    _HmSec2UsrFwTemplateTimeoutType_Type()
)
hmSec2UsrFwTemplateTimeoutType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateTimeoutType.setStatus("current")


class _HmSec2UsrFwTemplateComment_Type(DisplayString):
    """Custom type hmSec2UsrFwTemplateComment based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2UsrFwTemplateComment_Type.__name__ = "DisplayString"
_HmSec2UsrFwTemplateComment_Object = MibTableColumn
hmSec2UsrFwTemplateComment = _HmSec2UsrFwTemplateComment_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 2, 1, 5),
    _HmSec2UsrFwTemplateComment_Type()
)
hmSec2UsrFwTemplateComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateComment.setStatus("current")


class _HmSec2UsrFwTemplateSrcAddr_Type(DisplayString):
    """Custom type hmSec2UsrFwTemplateSrcAddr based on DisplayString"""
    defaultValue = OctetString("%authorized_ip")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 20),
    )


_HmSec2UsrFwTemplateSrcAddr_Type.__name__ = "DisplayString"
_HmSec2UsrFwTemplateSrcAddr_Object = MibTableColumn
hmSec2UsrFwTemplateSrcAddr = _HmSec2UsrFwTemplateSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 2, 1, 6),
    _HmSec2UsrFwTemplateSrcAddr_Type()
)
hmSec2UsrFwTemplateSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateSrcAddr.setStatus("current")
_HmSec2UsrFwTemplateStatus_Type = RowStatus
_HmSec2UsrFwTemplateStatus_Object = MibTableColumn
hmSec2UsrFwTemplateStatus = _HmSec2UsrFwTemplateStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 2, 1, 7),
    _HmSec2UsrFwTemplateStatus_Type()
)
hmSec2UsrFwTemplateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateStatus.setStatus("current")
_HmSec2UsrFwTemplateUserTable_Object = MibTable
hmSec2UsrFwTemplateUserTable = _HmSec2UsrFwTemplateUserTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 3)
)
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateUserTable.setStatus("current")
_HmSec2UsrFwTemplateUserEntry_Object = MibTableRow
hmSec2UsrFwTemplateUserEntry = _HmSec2UsrFwTemplateUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 3, 1)
)
hmSec2UsrFwTemplateUserEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2UsrFwTemplateIndex"),
    (1, "ABBSECURITY2-MIB", "hmSec2UsrFwTemplateUserName"),
)
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateUserEntry.setStatus("current")
_HmSec2UsrFwTemplateUserTemplateIndex_Type = Integer32
_HmSec2UsrFwTemplateUserTemplateIndex_Object = MibTableColumn
hmSec2UsrFwTemplateUserTemplateIndex = _HmSec2UsrFwTemplateUserTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 3, 1, 1),
    _HmSec2UsrFwTemplateUserTemplateIndex_Type()
)
hmSec2UsrFwTemplateUserTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateUserTemplateIndex.setStatus("current")


class _HmSec2UsrFwTemplateUserName_Type(SnmpAdminString):
    """Custom type hmSec2UsrFwTemplateUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HmSec2UsrFwTemplateUserName_Type.__name__ = "SnmpAdminString"
_HmSec2UsrFwTemplateUserName_Object = MibTableColumn
hmSec2UsrFwTemplateUserName = _HmSec2UsrFwTemplateUserName_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 3, 1, 2),
    _HmSec2UsrFwTemplateUserName_Type()
)
hmSec2UsrFwTemplateUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateUserName.setStatus("current")
_HmSec2UsrFwTemplateUserStatus_Type = RowStatus
_HmSec2UsrFwTemplateUserStatus_Object = MibTableColumn
hmSec2UsrFwTemplateUserStatus = _HmSec2UsrFwTemplateUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 3, 1, 3),
    _HmSec2UsrFwTemplateUserStatus_Type()
)
hmSec2UsrFwTemplateUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateUserStatus.setStatus("current")
_HmSec2UsrFwTemplateRuleTable_Object = MibTable
hmSec2UsrFwTemplateRuleTable = _HmSec2UsrFwTemplateRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4)
)
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleTable.setStatus("current")
_HmSec2UsrFwTemplateRuleEntry_Object = MibTableRow
hmSec2UsrFwTemplateRuleEntry = _HmSec2UsrFwTemplateRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4, 1)
)
hmSec2UsrFwTemplateRuleEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2UsrFwTemplateRuleTemplateIndex"),
    (0, "ABBSECURITY2-MIB", "hmSec2UsrFwTemplateRuleIndex"),
)
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleEntry.setStatus("current")
_HmSec2UsrFwTemplateRuleTemplateIndex_Type = Integer32
_HmSec2UsrFwTemplateRuleTemplateIndex_Object = MibTableColumn
hmSec2UsrFwTemplateRuleTemplateIndex = _HmSec2UsrFwTemplateRuleTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4, 1, 1),
    _HmSec2UsrFwTemplateRuleTemplateIndex_Type()
)
hmSec2UsrFwTemplateRuleTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleTemplateIndex.setStatus("current")
_HmSec2UsrFwTemplateRuleIndex_Type = Integer32
_HmSec2UsrFwTemplateRuleIndex_Object = MibTableColumn
hmSec2UsrFwTemplateRuleIndex = _HmSec2UsrFwTemplateRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4, 1, 2),
    _HmSec2UsrFwTemplateRuleIndex_Type()
)
hmSec2UsrFwTemplateRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleIndex.setStatus("current")


class _HmSec2UsrFwTemplateRuleProto_Type(DisplayString):
    """Custom type hmSec2UsrFwTemplateRuleProto based on DisplayString"""
    defaultValue = OctetString("tcp")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmSec2UsrFwTemplateRuleProto_Type.__name__ = "DisplayString"
_HmSec2UsrFwTemplateRuleProto_Object = MibTableColumn
hmSec2UsrFwTemplateRuleProto = _HmSec2UsrFwTemplateRuleProto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4, 1, 3),
    _HmSec2UsrFwTemplateRuleProto_Type()
)
hmSec2UsrFwTemplateRuleProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleProto.setStatus("current")


class _HmSec2UsrFwTemplateRuleSrcPort_Type(DisplayString):
    """Custom type hmSec2UsrFwTemplateRuleSrcPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2UsrFwTemplateRuleSrcPort_Type.__name__ = "DisplayString"
_HmSec2UsrFwTemplateRuleSrcPort_Object = MibTableColumn
hmSec2UsrFwTemplateRuleSrcPort = _HmSec2UsrFwTemplateRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4, 1, 4),
    _HmSec2UsrFwTemplateRuleSrcPort_Type()
)
hmSec2UsrFwTemplateRuleSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleSrcPort.setStatus("current")


class _HmSec2UsrFwTemplateRuleDstNet_Type(DisplayString):
    """Custom type hmSec2UsrFwTemplateRuleDstNet based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2UsrFwTemplateRuleDstNet_Type.__name__ = "DisplayString"
_HmSec2UsrFwTemplateRuleDstNet_Object = MibTableColumn
hmSec2UsrFwTemplateRuleDstNet = _HmSec2UsrFwTemplateRuleDstNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4, 1, 5),
    _HmSec2UsrFwTemplateRuleDstNet_Type()
)
hmSec2UsrFwTemplateRuleDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleDstNet.setStatus("current")


class _HmSec2UsrFwTemplateRuleDstPort_Type(DisplayString):
    """Custom type hmSec2UsrFwTemplateRuleDstPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2UsrFwTemplateRuleDstPort_Type.__name__ = "DisplayString"
_HmSec2UsrFwTemplateRuleDstPort_Object = MibTableColumn
hmSec2UsrFwTemplateRuleDstPort = _HmSec2UsrFwTemplateRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4, 1, 6),
    _HmSec2UsrFwTemplateRuleDstPort_Type()
)
hmSec2UsrFwTemplateRuleDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleDstPort.setStatus("current")


class _HmSec2UsrFwTemplateRuleComment_Type(DisplayString):
    """Custom type hmSec2UsrFwTemplateRuleComment based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2UsrFwTemplateRuleComment_Type.__name__ = "DisplayString"
_HmSec2UsrFwTemplateRuleComment_Object = MibTableColumn
hmSec2UsrFwTemplateRuleComment = _HmSec2UsrFwTemplateRuleComment_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4, 1, 7),
    _HmSec2UsrFwTemplateRuleComment_Type()
)
hmSec2UsrFwTemplateRuleComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleComment.setStatus("current")


class _HmSec2UsrFwTemplateRuleLog_Type(Integer32):
    """Custom type hmSec2UsrFwTemplateRuleLog based on Integer32"""
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


_HmSec2UsrFwTemplateRuleLog_Type.__name__ = "Integer32"
_HmSec2UsrFwTemplateRuleLog_Object = MibTableColumn
hmSec2UsrFwTemplateRuleLog = _HmSec2UsrFwTemplateRuleLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4, 1, 8),
    _HmSec2UsrFwTemplateRuleLog_Type()
)
hmSec2UsrFwTemplateRuleLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleLog.setStatus("current")
_HmSec2UsrFwTemplateRuleStatus_Type = RowStatus
_HmSec2UsrFwTemplateRuleStatus_Object = MibTableColumn
hmSec2UsrFwTemplateRuleStatus = _HmSec2UsrFwTemplateRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 8, 4, 1, 9),
    _HmSec2UsrFwTemplateRuleStatus_Type()
)
hmSec2UsrFwTemplateRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UsrFwTemplateRuleStatus.setStatus("current")
_HmSec2FirewallDiagnosticsGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallDiagnosticsGroup = _HmSec2FirewallDiagnosticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9)
)
_HmSec2FwDiagL3Table_Object = MibTable
hmSec2FwDiagL3Table = _HmSec2FwDiagL3Table_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1)
)
if mibBuilder.loadTexts:
    hmSec2FwDiagL3Table.setStatus("current")
_HmSec2FwDiagL3Entry_Object = MibTableRow
hmSec2FwDiagL3Entry = _HmSec2FwDiagL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1)
)
hmSec2FwDiagL3Entry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwDiagL3Index"),
)
if mibBuilder.loadTexts:
    hmSec2FwDiagL3Entry.setStatus("current")
_HmSec2FwDiagL3Index_Type = Integer32
_HmSec2FwDiagL3Index_Object = MibTableColumn
hmSec2FwDiagL3Index = _HmSec2FwDiagL3Index_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 1),
    _HmSec2FwDiagL3Index_Type()
)
hmSec2FwDiagL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3Index.setStatus("current")


class _HmSec2FwDiagL3Group_Type(DisplayString):
    """Custom type hmSec2FwDiagL3Group based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmSec2FwDiagL3Group_Type.__name__ = "DisplayString"
_HmSec2FwDiagL3Group_Object = MibTableColumn
hmSec2FwDiagL3Group = _HmSec2FwDiagL3Group_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 2),
    _HmSec2FwDiagL3Group_Type()
)
hmSec2FwDiagL3Group.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3Group.setStatus("current")
_HmSec2FwDiagL3Ref_Type = Integer32
_HmSec2FwDiagL3Ref_Object = MibTableColumn
hmSec2FwDiagL3Ref = _HmSec2FwDiagL3Ref_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 3),
    _HmSec2FwDiagL3Ref_Type()
)
hmSec2FwDiagL3Ref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3Ref.setStatus("current")


class _HmSec2FwDiagL3Interface_Type(DisplayString):
    """Custom type hmSec2FwDiagL3Interface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HmSec2FwDiagL3Interface_Type.__name__ = "DisplayString"
_HmSec2FwDiagL3Interface_Object = MibTableColumn
hmSec2FwDiagL3Interface = _HmSec2FwDiagL3Interface_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 4),
    _HmSec2FwDiagL3Interface_Type()
)
hmSec2FwDiagL3Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3Interface.setStatus("current")


class _HmSec2FwDiagL3SrcNet_Type(DisplayString):
    """Custom type hmSec2FwDiagL3SrcNet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwDiagL3SrcNet_Type.__name__ = "DisplayString"
_HmSec2FwDiagL3SrcNet_Object = MibTableColumn
hmSec2FwDiagL3SrcNet = _HmSec2FwDiagL3SrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 5),
    _HmSec2FwDiagL3SrcNet_Type()
)
hmSec2FwDiagL3SrcNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3SrcNet.setStatus("current")


class _HmSec2FwDiagL3SrcPort_Type(DisplayString):
    """Custom type hmSec2FwDiagL3SrcPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwDiagL3SrcPort_Type.__name__ = "DisplayString"
_HmSec2FwDiagL3SrcPort_Object = MibTableColumn
hmSec2FwDiagL3SrcPort = _HmSec2FwDiagL3SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 6),
    _HmSec2FwDiagL3SrcPort_Type()
)
hmSec2FwDiagL3SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3SrcPort.setStatus("current")


class _HmSec2FwDiagL3DstNet_Type(DisplayString):
    """Custom type hmSec2FwDiagL3DstNet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwDiagL3DstNet_Type.__name__ = "DisplayString"
_HmSec2FwDiagL3DstNet_Object = MibTableColumn
hmSec2FwDiagL3DstNet = _HmSec2FwDiagL3DstNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 7),
    _HmSec2FwDiagL3DstNet_Type()
)
hmSec2FwDiagL3DstNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3DstNet.setStatus("current")


class _HmSec2FwDiagL3DstPort_Type(DisplayString):
    """Custom type hmSec2FwDiagL3DstPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwDiagL3DstPort_Type.__name__ = "DisplayString"
_HmSec2FwDiagL3DstPort_Object = MibTableColumn
hmSec2FwDiagL3DstPort = _HmSec2FwDiagL3DstPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 8),
    _HmSec2FwDiagL3DstPort_Type()
)
hmSec2FwDiagL3DstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3DstPort.setStatus("current")


class _HmSec2FwDiagL3Proto_Type(DisplayString):
    """Custom type hmSec2FwDiagL3Proto based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmSec2FwDiagL3Proto_Type.__name__ = "DisplayString"
_HmSec2FwDiagL3Proto_Object = MibTableColumn
hmSec2FwDiagL3Proto = _HmSec2FwDiagL3Proto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 9),
    _HmSec2FwDiagL3Proto_Type()
)
hmSec2FwDiagL3Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3Proto.setStatus("current")


class _HmSec2FwDiagL3Action_Type(Integer32):
    """Custom type hmSec2FwDiagL3Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("reject", 3))
    )


_HmSec2FwDiagL3Action_Type.__name__ = "Integer32"
_HmSec2FwDiagL3Action_Object = MibTableColumn
hmSec2FwDiagL3Action = _HmSec2FwDiagL3Action_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 10),
    _HmSec2FwDiagL3Action_Type()
)
hmSec2FwDiagL3Action.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3Action.setStatus("current")


class _HmSec2FwDiagL3Log_Type(Integer32):
    """Custom type hmSec2FwDiagL3Log based on Integer32"""
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
          ("logAndTrap", 3))
    )


_HmSec2FwDiagL3Log_Type.__name__ = "Integer32"
_HmSec2FwDiagL3Log_Object = MibTableColumn
hmSec2FwDiagL3Log = _HmSec2FwDiagL3Log_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 11),
    _HmSec2FwDiagL3Log_Type()
)
hmSec2FwDiagL3Log.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3Log.setStatus("current")
_HmSec2FwDiagL3MatchCnt_Type = Counter32
_HmSec2FwDiagL3MatchCnt_Object = MibTableColumn
hmSec2FwDiagL3MatchCnt = _HmSec2FwDiagL3MatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 1, 1, 12),
    _HmSec2FwDiagL3MatchCnt_Type()
)
hmSec2FwDiagL3MatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL3MatchCnt.setStatus("current")
_HmSec2FwDiagL2Table_Object = MibTable
hmSec2FwDiagL2Table = _HmSec2FwDiagL2Table_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2)
)
if mibBuilder.loadTexts:
    hmSec2FwDiagL2Table.setStatus("current")
_HmSec2FwDiagL2Entry_Object = MibTableRow
hmSec2FwDiagL2Entry = _HmSec2FwDiagL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1)
)
hmSec2FwDiagL2Entry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2FwDiagL2Index"),
)
if mibBuilder.loadTexts:
    hmSec2FwDiagL2Entry.setStatus("current")
_HmSec2FwDiagL2Index_Type = Integer32
_HmSec2FwDiagL2Index_Object = MibTableColumn
hmSec2FwDiagL2Index = _HmSec2FwDiagL2Index_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1, 1),
    _HmSec2FwDiagL2Index_Type()
)
hmSec2FwDiagL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL2Index.setStatus("current")


class _HmSec2FwDiagL2Group_Type(DisplayString):
    """Custom type hmSec2FwDiagL2Group based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmSec2FwDiagL2Group_Type.__name__ = "DisplayString"
_HmSec2FwDiagL2Group_Object = MibTableColumn
hmSec2FwDiagL2Group = _HmSec2FwDiagL2Group_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1, 2),
    _HmSec2FwDiagL2Group_Type()
)
hmSec2FwDiagL2Group.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL2Group.setStatus("current")
_HmSec2FwDiagL2Ref_Type = Integer32
_HmSec2FwDiagL2Ref_Object = MibTableColumn
hmSec2FwDiagL2Ref = _HmSec2FwDiagL2Ref_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1, 3),
    _HmSec2FwDiagL2Ref_Type()
)
hmSec2FwDiagL2Ref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL2Ref.setStatus("current")


class _HmSec2FwDiagL2Interface_Type(DisplayString):
    """Custom type hmSec2FwDiagL2Interface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HmSec2FwDiagL2Interface_Type.__name__ = "DisplayString"
_HmSec2FwDiagL2Interface_Object = MibTableColumn
hmSec2FwDiagL2Interface = _HmSec2FwDiagL2Interface_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1, 4),
    _HmSec2FwDiagL2Interface_Type()
)
hmSec2FwDiagL2Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL2Interface.setStatus("current")


class _HmSec2FwDiagL2SrcNet_Type(DisplayString):
    """Custom type hmSec2FwDiagL2SrcNet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwDiagL2SrcNet_Type.__name__ = "DisplayString"
_HmSec2FwDiagL2SrcNet_Object = MibTableColumn
hmSec2FwDiagL2SrcNet = _HmSec2FwDiagL2SrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1, 5),
    _HmSec2FwDiagL2SrcNet_Type()
)
hmSec2FwDiagL2SrcNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL2SrcNet.setStatus("current")


class _HmSec2FwDiagL2DstNet_Type(DisplayString):
    """Custom type hmSec2FwDiagL2DstNet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2FwDiagL2DstNet_Type.__name__ = "DisplayString"
_HmSec2FwDiagL2DstNet_Object = MibTableColumn
hmSec2FwDiagL2DstNet = _HmSec2FwDiagL2DstNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1, 6),
    _HmSec2FwDiagL2DstNet_Type()
)
hmSec2FwDiagL2DstNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL2DstNet.setStatus("current")


class _HmSec2FwDiagL2Proto_Type(DisplayString):
    """Custom type hmSec2FwDiagL2Proto based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmSec2FwDiagL2Proto_Type.__name__ = "DisplayString"
_HmSec2FwDiagL2Proto_Object = MibTableColumn
hmSec2FwDiagL2Proto = _HmSec2FwDiagL2Proto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1, 7),
    _HmSec2FwDiagL2Proto_Type()
)
hmSec2FwDiagL2Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL2Proto.setStatus("current")


class _HmSec2FwDiagL2Action_Type(Integer32):
    """Custom type hmSec2FwDiagL2Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2))
    )


_HmSec2FwDiagL2Action_Type.__name__ = "Integer32"
_HmSec2FwDiagL2Action_Object = MibTableColumn
hmSec2FwDiagL2Action = _HmSec2FwDiagL2Action_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1, 8),
    _HmSec2FwDiagL2Action_Type()
)
hmSec2FwDiagL2Action.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL2Action.setStatus("current")


class _HmSec2FwDiagL2Log_Type(Integer32):
    """Custom type hmSec2FwDiagL2Log based on Integer32"""
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
          ("logAndTrap", 3))
    )


_HmSec2FwDiagL2Log_Type.__name__ = "Integer32"
_HmSec2FwDiagL2Log_Object = MibTableColumn
hmSec2FwDiagL2Log = _HmSec2FwDiagL2Log_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1, 9),
    _HmSec2FwDiagL2Log_Type()
)
hmSec2FwDiagL2Log.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL2Log.setStatus("current")
_HmSec2FwDiagL2MatchCnt_Type = Counter32
_HmSec2FwDiagL2MatchCnt_Object = MibTableColumn
hmSec2FwDiagL2MatchCnt = _HmSec2FwDiagL2MatchCnt_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 9, 2, 1, 10),
    _HmSec2FwDiagL2MatchCnt_Type()
)
hmSec2FwDiagL2MatchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwDiagL2MatchCnt.setStatus("current")
_HmSec2FirewallLearningModeGroup_ObjectIdentity = ObjectIdentity
hmSec2FirewallLearningModeGroup = _HmSec2FirewallLearningModeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10)
)
_HmSec2FirewallLearningModeVars_ObjectIdentity = ObjectIdentity
hmSec2FirewallLearningModeVars = _HmSec2FirewallLearningModeVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1)
)


class _HmSec2FLMAdminState_Type(Integer32):
    """Custom type hmSec2FLMAdminState based on Integer32"""
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


_HmSec2FLMAdminState_Type.__name__ = "Integer32"
_HmSec2FLMAdminState_Object = MibScalar
hmSec2FLMAdminState = _HmSec2FLMAdminState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1, 1),
    _HmSec2FLMAdminState_Type()
)
hmSec2FLMAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FLMAdminState.setStatus("current")


class _HmSec2FLMAction_Type(Integer32):
    """Custom type hmSec2FLMAction based on Integer32"""
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
        *(("other", 1),
          ("start", 2),
          ("stop", 3),
          ("clear", 4))
    )


_HmSec2FLMAction_Type.__name__ = "Integer32"
_HmSec2FLMAction_Object = MibScalar
hmSec2FLMAction = _HmSec2FLMAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1, 2),
    _HmSec2FLMAction_Type()
)
hmSec2FLMAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FLMAction.setStatus("current")


class _HmSec2FLMInterfaces_Type(Integer32):
    """Custom type hmSec2FLMInterfaces based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("int", 2),
          ("ext", 3))
    )


_HmSec2FLMInterfaces_Type.__name__ = "Integer32"
_HmSec2FLMInterfaces_Object = MibScalar
hmSec2FLMInterfaces = _HmSec2FLMInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1, 3),
    _HmSec2FLMInterfaces_Type()
)
hmSec2FLMInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FLMInterfaces.setStatus("current")


class _HmSec2FLMType_Type(Integer32):
    """Custom type hmSec2FLMType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learn", 1),
          ("test", 2))
    )


_HmSec2FLMType_Type.__name__ = "Integer32"
_HmSec2FLMType_Object = MibScalar
hmSec2FLMType = _HmSec2FLMType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1, 4),
    _HmSec2FLMType_Type()
)
hmSec2FLMType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FLMType.setStatus("current")


class _HmSec2FLMAppState_Type(Integer32):
    """Custom type hmSec2FLMAppState based on Integer32"""
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
        *(("off", 1),
          ("stoppeddatanotpresent", 2),
          ("stoppeddatapresent", 3),
          ("learning", 4),
          ("testing", 5),
          ("pending", 6))
    )


_HmSec2FLMAppState_Type.__name__ = "Integer32"
_HmSec2FLMAppState_Object = MibScalar
hmSec2FLMAppState = _HmSec2FLMAppState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1, 5),
    _HmSec2FLMAppState_Type()
)
hmSec2FLMAppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FLMAppState.setStatus("current")


class _HmSec2FLMAppInfoEnum_Type(Integer32):
    """Custom type hmSec2FLMAppInfoEnum based on Integer32"""
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
        *(("other", 1),
          ("normal", 2),
          ("ramlow", 3),
          ("ramempty", 4),
          ("conndrop", 5))
    )


_HmSec2FLMAppInfoEnum_Type.__name__ = "Integer32"
_HmSec2FLMAppInfoEnum_Object = MibScalar
hmSec2FLMAppInfoEnum = _HmSec2FLMAppInfoEnum_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1, 6),
    _HmSec2FLMAppInfoEnum_Type()
)
hmSec2FLMAppInfoEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FLMAppInfoEnum.setStatus("current")


class _HmSec2FLMAppInfoString_Type(DisplayString):
    """Custom type hmSec2FLMAppInfoString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HmSec2FLMAppInfoString_Type.__name__ = "DisplayString"
_HmSec2FLMAppInfoString_Object = MibScalar
hmSec2FLMAppInfoString = _HmSec2FLMAppInfoString_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1, 7),
    _HmSec2FLMAppInfoString_Type()
)
hmSec2FLMAppInfoString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FLMAppInfoString.setStatus("current")
_HmSec2FLML3Entries_Type = Integer32
_HmSec2FLML3Entries_Object = MibScalar
hmSec2FLML3Entries = _HmSec2FLML3Entries_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1, 8),
    _HmSec2FLML3Entries_Type()
)
hmSec2FLML3Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FLML3Entries.setStatus("current")
_HmSec2FLMFreeMem_Type = Integer32
_HmSec2FLMFreeMem_Object = MibScalar
hmSec2FLMFreeMem = _HmSec2FLMFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1, 9),
    _HmSec2FLMFreeMem_Type()
)
hmSec2FLMFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FLMFreeMem.setStatus("current")


class _HmSec2FLMAnyRuleChange_Type(Integer32):
    """Custom type hmSec2FLMAnyRuleChange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_HmSec2FLMAnyRuleChange_Type.__name__ = "Integer32"
_HmSec2FLMAnyRuleChange_Object = MibScalar
hmSec2FLMAnyRuleChange = _HmSec2FLMAnyRuleChange_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 10, 1, 10),
    _HmSec2FLMAnyRuleChange_Type()
)
hmSec2FLMAnyRuleChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FLMAnyRuleChange.setStatus("current")
_HmSec2FwConfigGroup_ObjectIdentity = ObjectIdentity
hmSec2FwConfigGroup = _HmSec2FwConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 11)
)


class _HmSec2FwStaticPacketCheck_Type(Integer32):
    """Custom type hmSec2FwStaticPacketCheck based on Integer32"""
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


_HmSec2FwStaticPacketCheck_Type.__name__ = "Integer32"
_HmSec2FwStaticPacketCheck_Object = MibScalar
hmSec2FwStaticPacketCheck = _HmSec2FwStaticPacketCheck_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 11, 1),
    _HmSec2FwStaticPacketCheck_Type()
)
hmSec2FwStaticPacketCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2FwStaticPacketCheck.setStatus("current")
_HmSec2FwInternRemNumIPRules_Type = Counter32
_HmSec2FwInternRemNumIPRules_Object = MibScalar
hmSec2FwInternRemNumIPRules = _HmSec2FwInternRemNumIPRules_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 11, 11, 2),
    _HmSec2FwInternRemNumIPRules_Type()
)
hmSec2FwInternRemNumIPRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2FwInternRemNumIPRules.setStatus("current")
_HmSec2Network_ObjectIdentity = ObjectIdentity
hmSec2Network = _HmSec2Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12)
)
_HmSec2NetGeneralGroup_ObjectIdentity = ObjectIdentity
hmSec2NetGeneralGroup = _HmSec2NetGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 1)
)


class _HmSec2NetworkMode_Type(Integer32):
    """Custom type hmSec2NetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("router", 2),
          ("pppoe", 3))
    )


_HmSec2NetworkMode_Type.__name__ = "Integer32"
_HmSec2NetworkMode_Object = MibScalar
hmSec2NetworkMode = _HmSec2NetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 1, 1),
    _HmSec2NetworkMode_Type()
)
hmSec2NetworkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetworkMode.setStatus("current")


class _HmSec2NetAction_Type(Integer32):
    """Custom type hmSec2NetAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("activate", 2),
          ("flushstates", 3))
    )


_HmSec2NetAction_Type.__name__ = "Integer32"
_HmSec2NetAction_Object = MibScalar
hmSec2NetAction = _HmSec2NetAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 1, 2),
    _HmSec2NetAction_Type()
)
hmSec2NetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetAction.setStatus("current")


class _HmSec2NetDirectedBroadcasts_Type(Integer32):
    """Custom type hmSec2NetDirectedBroadcasts based on Integer32"""
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


_HmSec2NetDirectedBroadcasts_Type.__name__ = "Integer32"
_HmSec2NetDirectedBroadcasts_Object = MibScalar
hmSec2NetDirectedBroadcasts = _HmSec2NetDirectedBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 1, 3),
    _HmSec2NetDirectedBroadcasts_Type()
)
hmSec2NetDirectedBroadcasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetDirectedBroadcasts.setStatus("current")


class _HmSec2NetIPFragmentsAllowed_Type(Integer32):
    """Custom type hmSec2NetIPFragmentsAllowed based on Integer32"""
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


_HmSec2NetIPFragmentsAllowed_Type.__name__ = "Integer32"
_HmSec2NetIPFragmentsAllowed_Object = MibScalar
hmSec2NetIPFragmentsAllowed = _HmSec2NetIPFragmentsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 1, 4),
    _HmSec2NetIPFragmentsAllowed_Type()
)
hmSec2NetIPFragmentsAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPFragmentsAllowed.setStatus("current")


class _HmSec2NetICMPSendRedirects_Type(Integer32):
    """Custom type hmSec2NetICMPSendRedirects based on Integer32"""
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


_HmSec2NetICMPSendRedirects_Type.__name__ = "Integer32"
_HmSec2NetICMPSendRedirects_Object = MibScalar
hmSec2NetICMPSendRedirects = _HmSec2NetICMPSendRedirects_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 1, 5),
    _HmSec2NetICMPSendRedirects_Type()
)
hmSec2NetICMPSendRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetICMPSendRedirects.setStatus("current")
_HmSec2NetTransparentGroup_ObjectIdentity = ObjectIdentity
hmSec2NetTransparentGroup = _HmSec2NetTransparentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2)
)


class _HmSec2LocalIPAddr_Type(IpAddress):
    """Custom type hmSec2LocalIPAddr based on IpAddress"""
    defaultHexValue = "C0A80101"


_HmSec2LocalIPAddr_Type.__name__ = "IpAddress"
_HmSec2LocalIPAddr_Object = MibScalar
hmSec2LocalIPAddr = _HmSec2LocalIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2, 1),
    _HmSec2LocalIPAddr_Type()
)
hmSec2LocalIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2LocalIPAddr.setStatus("current")
_HmSec2LocalPhysAddr_Type = PhysAddress
_HmSec2LocalPhysAddr_Object = MibScalar
hmSec2LocalPhysAddr = _HmSec2LocalPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2, 2),
    _HmSec2LocalPhysAddr_Type()
)
hmSec2LocalPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2LocalPhysAddr.setStatus("current")


class _HmSec2GatewayIPAddr_Type(IpAddress):
    """Custom type hmSec2GatewayIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_HmSec2GatewayIPAddr_Type.__name__ = "IpAddress"
_HmSec2GatewayIPAddr_Object = MibScalar
hmSec2GatewayIPAddr = _HmSec2GatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2, 3),
    _HmSec2GatewayIPAddr_Type()
)
hmSec2GatewayIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2GatewayIPAddr.setStatus("current")


class _HmSec2NetMask_Type(IpAddress):
    """Custom type hmSec2NetMask based on IpAddress"""
    defaultHexValue = "FFFFFF00"


_HmSec2NetMask_Type.__name__ = "IpAddress"
_HmSec2NetMask_Object = MibScalar
hmSec2NetMask = _HmSec2NetMask_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2, 4),
    _HmSec2NetMask_Type()
)
hmSec2NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetMask.setStatus("current")


class _HmSec2UseVLAN_Type(Integer32):
    """Custom type hmSec2UseVLAN based on Integer32"""
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


_HmSec2UseVLAN_Type.__name__ = "Integer32"
_HmSec2UseVLAN_Object = MibScalar
hmSec2UseVLAN = _HmSec2UseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2, 5),
    _HmSec2UseVLAN_Type()
)
hmSec2UseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2UseVLAN.setStatus("current")


class _HmSec2MgmtVLANID_Type(Integer32):
    """Custom type hmSec2MgmtVLANID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HmSec2MgmtVLANID_Type.__name__ = "Integer32"
_HmSec2MgmtVLANID_Object = MibScalar
hmSec2MgmtVLANID = _HmSec2MgmtVLANID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2, 6),
    _HmSec2MgmtVLANID_Type()
)
hmSec2MgmtVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2MgmtVLANID.setStatus("current")


class _HmSec2NetProto_Type(Integer32):
    """Custom type hmSec2NetProto based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dhcp", 2))
    )


_HmSec2NetProto_Type.__name__ = "Integer32"
_HmSec2NetProto_Object = MibScalar
hmSec2NetProto = _HmSec2NetProto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2, 7),
    _HmSec2NetProto_Type()
)
hmSec2NetProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetProto.setStatus("current")


class _HmSec2NetPassThroughSTP_Type(Integer32):
    """Custom type hmSec2NetPassThroughSTP based on Integer32"""
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


_HmSec2NetPassThroughSTP_Type.__name__ = "Integer32"
_HmSec2NetPassThroughSTP_Object = MibScalar
hmSec2NetPassThroughSTP = _HmSec2NetPassThroughSTP_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2, 8),
    _HmSec2NetPassThroughSTP_Type()
)
hmSec2NetPassThroughSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetPassThroughSTP.setStatus("current")


class _HmSec2NetPassThroughGMRP_Type(Integer32):
    """Custom type hmSec2NetPassThroughGMRP based on Integer32"""
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


_HmSec2NetPassThroughGMRP_Type.__name__ = "Integer32"
_HmSec2NetPassThroughGMRP_Object = MibScalar
hmSec2NetPassThroughGMRP = _HmSec2NetPassThroughGMRP_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2, 9),
    _HmSec2NetPassThroughGMRP_Type()
)
hmSec2NetPassThroughGMRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetPassThroughGMRP.setStatus("current")


class _HmSec2NetPassThroughDHCP_Type(Integer32):
    """Custom type hmSec2NetPassThroughDHCP based on Integer32"""
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


_HmSec2NetPassThroughDHCP_Type.__name__ = "Integer32"
_HmSec2NetPassThroughDHCP_Object = MibScalar
hmSec2NetPassThroughDHCP = _HmSec2NetPassThroughDHCP_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 2, 10),
    _HmSec2NetPassThroughDHCP_Type()
)
hmSec2NetPassThroughDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetPassThroughDHCP.setStatus("current")
_HmSec2NetRouterGroup_ObjectIdentity = ObjectIdentity
hmSec2NetRouterGroup = _HmSec2NetRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3)
)
_HmSec2NetIPInterfaceTable_Object = MibTable
hmSec2NetIPInterfaceTable = _HmSec2NetIPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    hmSec2NetIPInterfaceTable.setStatus("current")
_HmSec2NetIPInterfaceEntry_Object = MibTableRow
hmSec2NetIPInterfaceEntry = _HmSec2NetIPInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 1, 1)
)
hmSec2NetIPInterfaceEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2NetIPIfIndex"),
)
if mibBuilder.loadTexts:
    hmSec2NetIPInterfaceEntry.setStatus("current")
_HmSec2NetIPIfIndex_Type = Integer32
_HmSec2NetIPIfIndex_Object = MibTableColumn
hmSec2NetIPIfIndex = _HmSec2NetIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 1, 1, 1),
    _HmSec2NetIPIfIndex_Type()
)
hmSec2NetIPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2NetIPIfIndex.setStatus("current")
_HmSec2NetIPIfAddr_Type = IpAddress
_HmSec2NetIPIfAddr_Object = MibTableColumn
hmSec2NetIPIfAddr = _HmSec2NetIPIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 1, 1, 2),
    _HmSec2NetIPIfAddr_Type()
)
hmSec2NetIPIfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPIfAddr.setStatus("current")
_HmSec2NetIPIfMask_Type = IpAddress
_HmSec2NetIPIfMask_Object = MibTableColumn
hmSec2NetIPIfMask = _HmSec2NetIPIfMask_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 1, 1, 3),
    _HmSec2NetIPIfMask_Type()
)
hmSec2NetIPIfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPIfMask.setStatus("current")


class _HmSec2NetIPIfUseVLAN_Type(Integer32):
    """Custom type hmSec2NetIPIfUseVLAN based on Integer32"""
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


_HmSec2NetIPIfUseVLAN_Type.__name__ = "Integer32"
_HmSec2NetIPIfUseVLAN_Object = MibTableColumn
hmSec2NetIPIfUseVLAN = _HmSec2NetIPIfUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 1, 1, 4),
    _HmSec2NetIPIfUseVLAN_Type()
)
hmSec2NetIPIfUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPIfUseVLAN.setStatus("current")


class _HmSec2NetIPIfVLANID_Type(Integer32):
    """Custom type hmSec2NetIPIfVLANID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HmSec2NetIPIfVLANID_Type.__name__ = "Integer32"
_HmSec2NetIPIfVLANID_Object = MibTableColumn
hmSec2NetIPIfVLANID = _HmSec2NetIPIfVLANID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 1, 1, 5),
    _HmSec2NetIPIfVLANID_Type()
)
hmSec2NetIPIfVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPIfVLANID.setStatus("current")


class _HmSec2NetIPIfNetProto_Type(Integer32):
    """Custom type hmSec2NetIPIfNetProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dhcp", 2))
    )


_HmSec2NetIPIfNetProto_Type.__name__ = "Integer32"
_HmSec2NetIPIfNetProto_Object = MibTableColumn
hmSec2NetIPIfNetProto = _HmSec2NetIPIfNetProto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 1, 1, 6),
    _HmSec2NetIPIfNetProto_Type()
)
hmSec2NetIPIfNetProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPIfNetProto.setStatus("current")
_HmSec2NetIPAliasesTable_Object = MibTable
hmSec2NetIPAliasesTable = _HmSec2NetIPAliasesTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 2)
)
if mibBuilder.loadTexts:
    hmSec2NetIPAliasesTable.setStatus("current")
_HmSec2NetIPAliasesEntry_Object = MibTableRow
hmSec2NetIPAliasesEntry = _HmSec2NetIPAliasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 2, 1)
)
hmSec2NetIPAliasesEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2NetIPAliasIfIndex"),
    (0, "ABBSECURITY2-MIB", "hmSec2NetIPAliasAddr"),
)
if mibBuilder.loadTexts:
    hmSec2NetIPAliasesEntry.setStatus("current")
_HmSec2NetIPAliasIfIndex_Type = Integer32
_HmSec2NetIPAliasIfIndex_Object = MibTableColumn
hmSec2NetIPAliasIfIndex = _HmSec2NetIPAliasIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 2, 1, 1),
    _HmSec2NetIPAliasIfIndex_Type()
)
hmSec2NetIPAliasIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2NetIPAliasIfIndex.setStatus("current")
_HmSec2NetIPAliasAddr_Type = IpAddress
_HmSec2NetIPAliasAddr_Object = MibTableColumn
hmSec2NetIPAliasAddr = _HmSec2NetIPAliasAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 2, 1, 2),
    _HmSec2NetIPAliasAddr_Type()
)
hmSec2NetIPAliasAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPAliasAddr.setStatus("current")
_HmSec2NetIPAliasMask_Type = IpAddress
_HmSec2NetIPAliasMask_Object = MibTableColumn
hmSec2NetIPAliasMask = _HmSec2NetIPAliasMask_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 2, 1, 3),
    _HmSec2NetIPAliasMask_Type()
)
hmSec2NetIPAliasMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPAliasMask.setStatus("current")


class _HmSec2NetIPAliasUseVLAN_Type(Integer32):
    """Custom type hmSec2NetIPAliasUseVLAN based on Integer32"""
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


_HmSec2NetIPAliasUseVLAN_Type.__name__ = "Integer32"
_HmSec2NetIPAliasUseVLAN_Object = MibTableColumn
hmSec2NetIPAliasUseVLAN = _HmSec2NetIPAliasUseVLAN_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 2, 1, 4),
    _HmSec2NetIPAliasUseVLAN_Type()
)
hmSec2NetIPAliasUseVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPAliasUseVLAN.setStatus("current")


class _HmSec2NetIPAliasVLANID_Type(Integer32):
    """Custom type hmSec2NetIPAliasVLANID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HmSec2NetIPAliasVLANID_Type.__name__ = "Integer32"
_HmSec2NetIPAliasVLANID_Object = MibTableColumn
hmSec2NetIPAliasVLANID = _HmSec2NetIPAliasVLANID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 2, 1, 5),
    _HmSec2NetIPAliasVLANID_Type()
)
hmSec2NetIPAliasVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPAliasVLANID.setStatus("current")
_HmSec2NetIPAliasRowStatus_Type = RowStatus
_HmSec2NetIPAliasRowStatus_Object = MibTableColumn
hmSec2NetIPAliasRowStatus = _HmSec2NetIPAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 2, 1, 6),
    _HmSec2NetIPAliasRowStatus_Type()
)
hmSec2NetIPAliasRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPAliasRowStatus.setStatus("current")
_HmSec2NetRouterExternalGroup_ObjectIdentity = ObjectIdentity
hmSec2NetRouterExternalGroup = _HmSec2NetRouterExternalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 3)
)


class _HmSec2NetRtrExternalGateway_Type(IpAddress):
    """Custom type hmSec2NetRtrExternalGateway based on IpAddress"""
    defaultHexValue = "00000000"


_HmSec2NetRtrExternalGateway_Type.__name__ = "IpAddress"
_HmSec2NetRtrExternalGateway_Object = MibScalar
hmSec2NetRtrExternalGateway = _HmSec2NetRtrExternalGateway_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 3, 1),
    _HmSec2NetRtrExternalGateway_Type()
)
hmSec2NetRtrExternalGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetRtrExternalGateway.setStatus("current")
_HmSec2NetIPRouteTable_Object = MibTable
hmSec2NetIPRouteTable = _HmSec2NetIPRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 4)
)
if mibBuilder.loadTexts:
    hmSec2NetIPRouteTable.setStatus("current")
_HmSec2NetIPRouteEntry_Object = MibTableRow
hmSec2NetIPRouteEntry = _HmSec2NetIPRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 4, 1)
)
hmSec2NetIPRouteEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2NetIPRouteIfIndex"),
    (0, "ABBSECURITY2-MIB", "hmSec2NetIPRouteAddr"),
    (0, "ABBSECURITY2-MIB", "hmSec2NetIPRouteMask"),
)
if mibBuilder.loadTexts:
    hmSec2NetIPRouteEntry.setStatus("current")
_HmSec2NetIPRouteIfIndex_Type = Integer32
_HmSec2NetIPRouteIfIndex_Object = MibTableColumn
hmSec2NetIPRouteIfIndex = _HmSec2NetIPRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 4, 1, 1),
    _HmSec2NetIPRouteIfIndex_Type()
)
hmSec2NetIPRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2NetIPRouteIfIndex.setStatus("current")
_HmSec2NetIPRouteAddr_Type = IpAddress
_HmSec2NetIPRouteAddr_Object = MibTableColumn
hmSec2NetIPRouteAddr = _HmSec2NetIPRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 4, 1, 2),
    _HmSec2NetIPRouteAddr_Type()
)
hmSec2NetIPRouteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPRouteAddr.setStatus("current")
_HmSec2NetIPRouteMask_Type = IpAddress
_HmSec2NetIPRouteMask_Object = MibTableColumn
hmSec2NetIPRouteMask = _HmSec2NetIPRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 4, 1, 3),
    _HmSec2NetIPRouteMask_Type()
)
hmSec2NetIPRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPRouteMask.setStatus("current")
_HmSec2NetIPRouteGateway_Type = IpAddress
_HmSec2NetIPRouteGateway_Object = MibTableColumn
hmSec2NetIPRouteGateway = _HmSec2NetIPRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 4, 1, 4),
    _HmSec2NetIPRouteGateway_Type()
)
hmSec2NetIPRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPRouteGateway.setStatus("current")
_HmSec2NetIPRouteRowStatus_Type = RowStatus
_HmSec2NetIPRouteRowStatus_Object = MibTableColumn
hmSec2NetIPRouteRowStatus = _HmSec2NetIPRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 3, 4, 1, 5),
    _HmSec2NetIPRouteRowStatus_Type()
)
hmSec2NetIPRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetIPRouteRowStatus.setStatus("current")
_HmSec2NetPPPoEGroup_ObjectIdentity = ObjectIdentity
hmSec2NetPPPoEGroup = _HmSec2NetPPPoEGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 4)
)


class _HmSec2PPPoEUsername_Type(DisplayString):
    """Custom type hmSec2PPPoEUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2PPPoEUsername_Type.__name__ = "DisplayString"
_HmSec2PPPoEUsername_Object = MibScalar
hmSec2PPPoEUsername = _HmSec2PPPoEUsername_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 4, 1),
    _HmSec2PPPoEUsername_Type()
)
hmSec2PPPoEUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPoEUsername.setStatus("current")


class _HmSec2PPPoEPassword_Type(DisplayString):
    """Custom type hmSec2PPPoEPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmSec2PPPoEPassword_Type.__name__ = "DisplayString"
_HmSec2PPPoEPassword_Object = MibScalar
hmSec2PPPoEPassword = _HmSec2PPPoEPassword_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 4, 2),
    _HmSec2PPPoEPassword_Type()
)
hmSec2PPPoEPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPoEPassword.setStatus("current")


class _HmSec2PPPoEMTU_Type(Integer32):
    """Custom type hmSec2PPPoEMTU based on Integer32"""
    defaultValue = 1492

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1500),
    )


_HmSec2PPPoEMTU_Type.__name__ = "Integer32"
_HmSec2PPPoEMTU_Object = MibScalar
hmSec2PPPoEMTU = _HmSec2PPPoEMTU_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 4, 3),
    _HmSec2PPPoEMTU_Type()
)
hmSec2PPPoEMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPoEMTU.setStatus("current")
_HmSec2PPPoEIfAddr_Type = IpAddress
_HmSec2PPPoEIfAddr_Object = MibScalar
hmSec2PPPoEIfAddr = _HmSec2PPPoEIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 4, 4),
    _HmSec2PPPoEIfAddr_Type()
)
hmSec2PPPoEIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2PPPoEIfAddr.setStatus("current")
_HmSec2PPPoEIfMask_Type = IpAddress
_HmSec2PPPoEIfMask_Object = MibScalar
hmSec2PPPoEIfMask = _HmSec2PPPoEIfMask_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 4, 5),
    _HmSec2PPPoEIfMask_Type()
)
hmSec2PPPoEIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2PPPoEIfMask.setStatus("current")
_HmSec2PPPoEGateway_Type = IpAddress
_HmSec2PPPoEGateway_Object = MibScalar
hmSec2PPPoEGateway = _HmSec2PPPoEGateway_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 4, 6),
    _HmSec2PPPoEGateway_Type()
)
hmSec2PPPoEGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2PPPoEGateway.setStatus("current")


class _HmSec2PPPoEStatus_Type(DisplayString):
    """Custom type hmSec2PPPoEStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2PPPoEStatus_Type.__name__ = "DisplayString"
_HmSec2PPPoEStatus_Object = MibScalar
hmSec2PPPoEStatus = _HmSec2PPPoEStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 4, 7),
    _HmSec2PPPoEStatus_Type()
)
hmSec2PPPoEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2PPPoEStatus.setStatus("current")


class _HmSec2PPPoEDisconAdminState_Type(Integer32):
    """Custom type hmSec2PPPoEDisconAdminState based on Integer32"""
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


_HmSec2PPPoEDisconAdminState_Type.__name__ = "Integer32"
_HmSec2PPPoEDisconAdminState_Object = MibScalar
hmSec2PPPoEDisconAdminState = _HmSec2PPPoEDisconAdminState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 4, 8),
    _HmSec2PPPoEDisconAdminState_Type()
)
hmSec2PPPoEDisconAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPoEDisconAdminState.setStatus("current")


class _HmSec2PPPoEDisconHour_Type(Integer32):
    """Custom type hmSec2PPPoEDisconHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_HmSec2PPPoEDisconHour_Type.__name__ = "Integer32"
_HmSec2PPPoEDisconHour_Object = MibScalar
hmSec2PPPoEDisconHour = _HmSec2PPPoEDisconHour_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 4, 9),
    _HmSec2PPPoEDisconHour_Type()
)
hmSec2PPPoEDisconHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPoEDisconHour.setStatus("current")
_HmSec2NetPPPGroup_ObjectIdentity = ObjectIdentity
hmSec2NetPPPGroup = _HmSec2NetPPPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 5)
)


class _HmSec2PPPUsername_Type(DisplayString):
    """Custom type hmSec2PPPUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2PPPUsername_Type.__name__ = "DisplayString"
_HmSec2PPPUsername_Object = MibScalar
hmSec2PPPUsername = _HmSec2PPPUsername_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 5, 1),
    _HmSec2PPPUsername_Type()
)
hmSec2PPPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPUsername.setStatus("current")


class _HmSec2PPPPassword_Type(DisplayString):
    """Custom type hmSec2PPPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmSec2PPPPassword_Type.__name__ = "DisplayString"
_HmSec2PPPPassword_Object = MibScalar
hmSec2PPPPassword = _HmSec2PPPPassword_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 5, 2),
    _HmSec2PPPPassword_Type()
)
hmSec2PPPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPPassword.setStatus("current")


class _HmSec2PPPLocalIPAddress_Type(IpAddress):
    """Custom type hmSec2PPPLocalIPAddress based on IpAddress"""
    defaultHexValue = "C0A80201"


_HmSec2PPPLocalIPAddress_Type.__name__ = "IpAddress"
_HmSec2PPPLocalIPAddress_Object = MibScalar
hmSec2PPPLocalIPAddress = _HmSec2PPPLocalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 5, 3),
    _HmSec2PPPLocalIPAddress_Type()
)
hmSec2PPPLocalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPLocalIPAddress.setStatus("current")


class _HmSec2PPPRemoteIPAddress_Type(IpAddress):
    """Custom type hmSec2PPPRemoteIPAddress based on IpAddress"""
    defaultHexValue = "C0A80202"


_HmSec2PPPRemoteIPAddress_Type.__name__ = "IpAddress"
_HmSec2PPPRemoteIPAddress_Object = MibScalar
hmSec2PPPRemoteIPAddress = _HmSec2PPPRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 5, 4),
    _HmSec2PPPRemoteIPAddress_Type()
)
hmSec2PPPRemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPRemoteIPAddress.setStatus("current")


class _HmSec2PPPModemAdminState_Type(Integer32):
    """Custom type hmSec2PPPModemAdminState based on Integer32"""
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


_HmSec2PPPModemAdminState_Type.__name__ = "Integer32"
_HmSec2PPPModemAdminState_Object = MibScalar
hmSec2PPPModemAdminState = _HmSec2PPPModemAdminState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 5, 5),
    _HmSec2PPPModemAdminState_Type()
)
hmSec2PPPModemAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPModemAdminState.setStatus("current")


class _HmSec2PPPModemBaudRate_Type(Integer32):
    """Custom type hmSec2PPPModemBaudRate based on Integer32"""
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
        *(("b19200", 1),
          ("b38400", 2),
          ("b57600", 3))
    )


_HmSec2PPPModemBaudRate_Type.__name__ = "Integer32"
_HmSec2PPPModemBaudRate_Object = MibScalar
hmSec2PPPModemBaudRate = _HmSec2PPPModemBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 5, 6),
    _HmSec2PPPModemBaudRate_Type()
)
hmSec2PPPModemBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPModemBaudRate.setStatus("current")


class _HmSec2PPPMTU_Type(Integer32):
    """Custom type hmSec2PPPMTU based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1500),
    )


_HmSec2PPPMTU_Type.__name__ = "Integer32"
_HmSec2PPPMTU_Object = MibScalar
hmSec2PPPMTU = _HmSec2PPPMTU_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 5, 7),
    _HmSec2PPPMTU_Type()
)
hmSec2PPPMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPMTU.setStatus("current")


class _HmSec2PPPStatus_Type(DisplayString):
    """Custom type hmSec2PPPStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2PPPStatus_Type.__name__ = "DisplayString"
_HmSec2PPPStatus_Object = MibScalar
hmSec2PPPStatus = _HmSec2PPPStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 5, 8),
    _HmSec2PPPStatus_Type()
)
hmSec2PPPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2PPPStatus.setStatus("current")


class _HmSec2PPPModemFlowControl_Type(Integer32):
    """Custom type hmSec2PPPModemFlowControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("rtscts", 2))
    )


_HmSec2PPPModemFlowControl_Type.__name__ = "Integer32"
_HmSec2PPPModemFlowControl_Object = MibScalar
hmSec2PPPModemFlowControl = _HmSec2PPPModemFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 5, 9),
    _HmSec2PPPModemFlowControl_Type()
)
hmSec2PPPModemFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2PPPModemFlowControl.setStatus("current")
_HmSec2NetDNSClientGroup_ObjectIdentity = ObjectIdentity
hmSec2NetDNSClientGroup = _HmSec2NetDNSClientGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 6)
)


class _HmSec2DNSClientServer1_Type(IpAddress):
    """Custom type hmSec2DNSClientServer1 based on IpAddress"""
    defaultHexValue = "00000000"


_HmSec2DNSClientServer1_Type.__name__ = "IpAddress"
_HmSec2DNSClientServer1_Object = MibScalar
hmSec2DNSClientServer1 = _HmSec2DNSClientServer1_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 6, 1),
    _HmSec2DNSClientServer1_Type()
)
hmSec2DNSClientServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DNSClientServer1.setStatus("current")


class _HmSec2DNSClientServer2_Type(IpAddress):
    """Custom type hmSec2DNSClientServer2 based on IpAddress"""
    defaultHexValue = "00000000"


_HmSec2DNSClientServer2_Type.__name__ = "IpAddress"
_HmSec2DNSClientServer2_Object = MibScalar
hmSec2DNSClientServer2 = _HmSec2DNSClientServer2_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 6, 2),
    _HmSec2DNSClientServer2_Type()
)
hmSec2DNSClientServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DNSClientServer2.setStatus("current")


class _HmSec2DNSClientServer3_Type(IpAddress):
    """Custom type hmSec2DNSClientServer3 based on IpAddress"""
    defaultHexValue = "00000000"


_HmSec2DNSClientServer3_Type.__name__ = "IpAddress"
_HmSec2DNSClientServer3_Object = MibScalar
hmSec2DNSClientServer3 = _HmSec2DNSClientServer3_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 6, 3),
    _HmSec2DNSClientServer3_Type()
)
hmSec2DNSClientServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DNSClientServer3.setStatus("current")


class _HmSec2DNSClientServer4_Type(IpAddress):
    """Custom type hmSec2DNSClientServer4 based on IpAddress"""
    defaultHexValue = "00000000"


_HmSec2DNSClientServer4_Type.__name__ = "IpAddress"
_HmSec2DNSClientServer4_Object = MibScalar
hmSec2DNSClientServer4 = _HmSec2DNSClientServer4_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 6, 4),
    _HmSec2DNSClientServer4_Type()
)
hmSec2DNSClientServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DNSClientServer4.setStatus("current")


class _HmSec2DNSClientConfigSource_Type(Integer32):
    """Custom type hmSec2DNSClientConfigSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("user", 1),
          ("provider", 2))
    )


_HmSec2DNSClientConfigSource_Type.__name__ = "Integer32"
_HmSec2DNSClientConfigSource_Object = MibScalar
hmSec2DNSClientConfigSource = _HmSec2DNSClientConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 6, 5),
    _HmSec2DNSClientConfigSource_Type()
)
hmSec2DNSClientConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DNSClientConfigSource.setStatus("current")
_HmSec2NetDynDNSGroup_ObjectIdentity = ObjectIdentity
hmSec2NetDynDNSGroup = _HmSec2NetDynDNSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 7)
)


class _HmSec2DynDNSProvider_Type(Integer32):
    """Custom type hmSec2DynDNSProvider based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dyndns-org", 1),
          ("other", 2))
    )


_HmSec2DynDNSProvider_Type.__name__ = "Integer32"
_HmSec2DynDNSProvider_Object = MibScalar
hmSec2DynDNSProvider = _HmSec2DynDNSProvider_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 7, 1),
    _HmSec2DynDNSProvider_Type()
)
hmSec2DynDNSProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DynDNSProvider.setStatus("current")


class _HmSec2DynDNSRegister_Type(Integer32):
    """Custom type hmSec2DynDNSRegister based on Integer32"""
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


_HmSec2DynDNSRegister_Type.__name__ = "Integer32"
_HmSec2DynDNSRegister_Object = MibScalar
hmSec2DynDNSRegister = _HmSec2DynDNSRegister_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 7, 2),
    _HmSec2DynDNSRegister_Type()
)
hmSec2DynDNSRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DynDNSRegister.setStatus("current")


class _HmSec2DynDNSServer_Type(DisplayString):
    """Custom type hmSec2DynDNSServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2DynDNSServer_Type.__name__ = "DisplayString"
_HmSec2DynDNSServer_Object = MibScalar
hmSec2DynDNSServer = _HmSec2DynDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 7, 3),
    _HmSec2DynDNSServer_Type()
)
hmSec2DynDNSServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DynDNSServer.setStatus("current")


class _HmSec2DynDNSLogin_Type(DisplayString):
    """Custom type hmSec2DynDNSLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2DynDNSLogin_Type.__name__ = "DisplayString"
_HmSec2DynDNSLogin_Object = MibScalar
hmSec2DynDNSLogin = _HmSec2DynDNSLogin_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 7, 4),
    _HmSec2DynDNSLogin_Type()
)
hmSec2DynDNSLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DynDNSLogin.setStatus("current")


class _HmSec2DynDNSPassword_Type(DisplayString):
    """Custom type hmSec2DynDNSPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2DynDNSPassword_Type.__name__ = "DisplayString"
_HmSec2DynDNSPassword_Object = MibScalar
hmSec2DynDNSPassword = _HmSec2DynDNSPassword_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 7, 5),
    _HmSec2DynDNSPassword_Type()
)
hmSec2DynDNSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DynDNSPassword.setStatus("current")


class _HmSec2DynDNSHostname_Type(DisplayString):
    """Custom type hmSec2DynDNSHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2DynDNSHostname_Type.__name__ = "DisplayString"
_HmSec2DynDNSHostname_Object = MibScalar
hmSec2DynDNSHostname = _HmSec2DynDNSHostname_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 7, 6),
    _HmSec2DynDNSHostname_Type()
)
hmSec2DynDNSHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DynDNSHostname.setStatus("current")


class _HmSec2DynDNSRefresh_Type(Integer32):
    """Custom type hmSec2DynDNSRefresh based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_HmSec2DynDNSRefresh_Type.__name__ = "Integer32"
_HmSec2DynDNSRefresh_Object = MibScalar
hmSec2DynDNSRefresh = _HmSec2DynDNSRefresh_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 7, 7),
    _HmSec2DynDNSRefresh_Type()
)
hmSec2DynDNSRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DynDNSRefresh.setStatus("current")


class _HmSec2DynDNSStatus_Type(DisplayString):
    """Custom type hmSec2DynDNSStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2DynDNSStatus_Type.__name__ = "DisplayString"
_HmSec2DynDNSStatus_Object = MibScalar
hmSec2DynDNSStatus = _HmSec2DynDNSStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 7, 8),
    _HmSec2DynDNSStatus_Type()
)
hmSec2DynDNSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2DynDNSStatus.setStatus("current")


class _HmSec2DynDNSCheckIPServer_Type(DisplayString):
    """Custom type hmSec2DynDNSCheckIPServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2DynDNSCheckIPServer_Type.__name__ = "DisplayString"
_HmSec2DynDNSCheckIPServer_Object = MibScalar
hmSec2DynDNSCheckIPServer = _HmSec2DynDNSCheckIPServer_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 7, 9),
    _HmSec2DynDNSCheckIPServer_Type()
)
hmSec2DynDNSCheckIPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2DynDNSCheckIPServer.setStatus("current")
_HmSec2NetPingGroup_ObjectIdentity = ObjectIdentity
hmSec2NetPingGroup = _HmSec2NetPingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 8)
)


class _HmSec2NetPingSourceAddr_Type(IpAddress):
    """Custom type hmSec2NetPingSourceAddr based on IpAddress"""
    defaultHexValue = "00000000"


_HmSec2NetPingSourceAddr_Type.__name__ = "IpAddress"
_HmSec2NetPingSourceAddr_Object = MibScalar
hmSec2NetPingSourceAddr = _HmSec2NetPingSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 8, 1),
    _HmSec2NetPingSourceAddr_Type()
)
hmSec2NetPingSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetPingSourceAddr.setStatus("current")


class _HmSec2NetPingDestAddr_Type(IpAddress):
    """Custom type hmSec2NetPingDestAddr based on IpAddress"""
    defaultHexValue = "00000000"


_HmSec2NetPingDestAddr_Type.__name__ = "IpAddress"
_HmSec2NetPingDestAddr_Object = MibScalar
hmSec2NetPingDestAddr = _HmSec2NetPingDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 8, 2),
    _HmSec2NetPingDestAddr_Type()
)
hmSec2NetPingDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetPingDestAddr.setStatus("current")


class _HmSec2NetPingAction_Type(Integer32):
    """Custom type hmSec2NetPingAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("activate", 2))
    )


_HmSec2NetPingAction_Type.__name__ = "Integer32"
_HmSec2NetPingAction_Object = MibScalar
hmSec2NetPingAction = _HmSec2NetPingAction_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 8, 3),
    _HmSec2NetPingAction_Type()
)
hmSec2NetPingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NetPingAction.setStatus("current")


class _HmSec2NetPingActionStatus_Type(Integer32):
    """Custom type hmSec2NetPingActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("pinging", 2))
    )


_HmSec2NetPingActionStatus_Type.__name__ = "Integer32"
_HmSec2NetPingActionStatus_Object = MibScalar
hmSec2NetPingActionStatus = _HmSec2NetPingActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 8, 4),
    _HmSec2NetPingActionStatus_Type()
)
hmSec2NetPingActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2NetPingActionStatus.setStatus("current")


class _HmSec2NetPingResult_Type(Integer32):
    """Custom type hmSec2NetPingResult based on Integer32"""
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
        *(("init", 1),
          ("reachable", 2),
          ("unreachable", 3),
          ("pinging", 4))
    )


_HmSec2NetPingResult_Type.__name__ = "Integer32"
_HmSec2NetPingResult_Object = MibScalar
hmSec2NetPingResult = _HmSec2NetPingResult_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 8, 5),
    _HmSec2NetPingResult_Type()
)
hmSec2NetPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2NetPingResult.setStatus("current")


class _HmSec2NetPingResultText_Type(DisplayString):
    """Custom type hmSec2NetPingResultText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2NetPingResultText_Type.__name__ = "DisplayString"
_HmSec2NetPingResultText_Object = MibScalar
hmSec2NetPingResultText = _HmSec2NetPingResultText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 12, 8, 6),
    _HmSec2NetPingResultText_Type()
)
hmSec2NetPingResultText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2NetPingResultText.setStatus("current")
_HmSec2Vpn_ObjectIdentity = ObjectIdentity
hmSec2Vpn = _HmSec2Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13)
)
_HmSec2VpnGroup_ObjectIdentity = ObjectIdentity
hmSec2VpnGroup = _HmSec2VpnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1)
)
_HmSec2VpnGeneralGroup_ObjectIdentity = ObjectIdentity
hmSec2VpnGeneralGroup = _HmSec2VpnGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 1)
)


class _HmSec2VpnRemoteCtlPwd_Type(DisplayString):
    """Custom type hmSec2VpnRemoteCtlPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HmSec2VpnRemoteCtlPwd_Type.__name__ = "DisplayString"
_HmSec2VpnRemoteCtlPwd_Object = MibScalar
hmSec2VpnRemoteCtlPwd = _HmSec2VpnRemoteCtlPwd_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 1, 1),
    _HmSec2VpnRemoteCtlPwd_Type()
)
hmSec2VpnRemoteCtlPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnRemoteCtlPwd.setStatus("current")


class _HmSec2VpnLEDIndication_Type(Integer32):
    """Custom type hmSec2VpnLEDIndication based on Integer32"""
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


_HmSec2VpnLEDIndication_Type.__name__ = "Integer32"
_HmSec2VpnLEDIndication_Object = MibScalar
hmSec2VpnLEDIndication = _HmSec2VpnLEDIndication_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 1, 2),
    _HmSec2VpnLEDIndication_Type()
)
hmSec2VpnLEDIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnLEDIndication.setStatus("current")


class _HmSec2VpnModeConfigPool_Type(DisplayString):
    """Custom type hmSec2VpnModeConfigPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2VpnModeConfigPool_Type.__name__ = "DisplayString"
_HmSec2VpnModeConfigPool_Object = MibScalar
hmSec2VpnModeConfigPool = _HmSec2VpnModeConfigPool_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 1, 3),
    _HmSec2VpnModeConfigPool_Type()
)
hmSec2VpnModeConfigPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnModeConfigPool.setStatus("current")
_HmSec2VpnConnGroup_ObjectIdentity = ObjectIdentity
hmSec2VpnConnGroup = _HmSec2VpnConnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2)
)


class _HmSec2VpnConnMax_Type(Integer32):
    """Custom type hmSec2VpnConnMax based on Integer32"""
    defaultValue = 256


_HmSec2VpnConnMax_Type.__name__ = "Integer32"
_HmSec2VpnConnMax_Object = MibScalar
hmSec2VpnConnMax = _HmSec2VpnConnMax_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 1),
    _HmSec2VpnConnMax_Type()
)
hmSec2VpnConnMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2VpnConnMax.setStatus("current")


class _HmSec2VpnConnNext_Type(Integer32):
    """Custom type hmSec2VpnConnNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HmSec2VpnConnNext_Type.__name__ = "Integer32"
_HmSec2VpnConnNext_Object = MibScalar
hmSec2VpnConnNext = _HmSec2VpnConnNext_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 2),
    _HmSec2VpnConnNext_Type()
)
hmSec2VpnConnNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2VpnConnNext.setStatus("current")
_HmSec2VpnConnTable_Object = MibTable
hmSec2VpnConnTable = _HmSec2VpnConnTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hmSec2VpnConnTable.setStatus("current")
_HmSec2VpnConnEntry_Object = MibTableRow
hmSec2VpnConnEntry = _HmSec2VpnConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1)
)
hmSec2VpnConnEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2VpnConnIndex"),
)
if mibBuilder.loadTexts:
    hmSec2VpnConnEntry.setStatus("current")


class _HmSec2VpnConnIndex_Type(Integer32):
    """Custom type hmSec2VpnConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HmSec2VpnConnIndex_Type.__name__ = "Integer32"
_HmSec2VpnConnIndex_Object = MibTableColumn
hmSec2VpnConnIndex = _HmSec2VpnConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 1),
    _HmSec2VpnConnIndex_Type()
)
hmSec2VpnConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2VpnConnIndex.setStatus("current")


class _HmSec2VpnConnIkeVersion_Type(Integer32):
    """Custom type hmSec2VpnConnIkeVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("v1", 2),
          ("v2", 3))
    )


_HmSec2VpnConnIkeVersion_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeVersion_Object = MibTableColumn
hmSec2VpnConnIkeVersion = _HmSec2VpnConnIkeVersion_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 2),
    _HmSec2VpnConnIkeVersion_Type()
)
hmSec2VpnConnIkeVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeVersion.setStatus("current")


class _HmSec2VpnConnIkeStartup_Type(Integer32):
    """Custom type hmSec2VpnConnIkeStartup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 1),
          ("responder", 2))
    )


_HmSec2VpnConnIkeStartup_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeStartup_Object = MibTableColumn
hmSec2VpnConnIkeStartup = _HmSec2VpnConnIkeStartup_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 3),
    _HmSec2VpnConnIkeStartup_Type()
)
hmSec2VpnConnIkeStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeStartup.setStatus("current")


class _HmSec2VpnConnIkeCompat_Type(Integer32):
    """Custom type hmSec2VpnConnIkeCompat based on Integer32"""
    defaultValue = 2

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


_HmSec2VpnConnIkeCompat_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeCompat_Object = MibTableColumn
hmSec2VpnConnIkeCompat = _HmSec2VpnConnIkeCompat_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 4),
    _HmSec2VpnConnIkeCompat_Type()
)
hmSec2VpnConnIkeCompat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeCompat.setStatus("current")


class _HmSec2VpnConnIkeLifetime_Type(Integer32):
    """Custom type hmSec2VpnConnIkeLifetime based on Integer32"""
    defaultValue = 28800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_HmSec2VpnConnIkeLifetime_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeLifetime_Object = MibTableColumn
hmSec2VpnConnIkeLifetime = _HmSec2VpnConnIkeLifetime_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 5),
    _HmSec2VpnConnIkeLifetime_Type()
)
hmSec2VpnConnIkeLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeLifetime.setStatus("current")


class _HmSec2VpnConnIkeDpdTimeout_Type(Integer32):
    """Custom type hmSec2VpnConnIkeDpdTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_HmSec2VpnConnIkeDpdTimeout_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeDpdTimeout_Object = MibTableColumn
hmSec2VpnConnIkeDpdTimeout = _HmSec2VpnConnIkeDpdTimeout_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 6),
    _HmSec2VpnConnIkeDpdTimeout_Type()
)
hmSec2VpnConnIkeDpdTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeDpdTimeout.setStatus("current")


class _HmSec2VpnConnIkeLocalAddr_Type(DisplayString):
    """Custom type hmSec2VpnConnIkeLocalAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmSec2VpnConnIkeLocalAddr_Type.__name__ = "DisplayString"
_HmSec2VpnConnIkeLocalAddr_Object = MibTableColumn
hmSec2VpnConnIkeLocalAddr = _HmSec2VpnConnIkeLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 7),
    _HmSec2VpnConnIkeLocalAddr_Type()
)
hmSec2VpnConnIkeLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeLocalAddr.setStatus("current")


class _HmSec2VpnConnIkeRemoteAddr_Type(DisplayString):
    """Custom type hmSec2VpnConnIkeRemoteAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmSec2VpnConnIkeRemoteAddr_Type.__name__ = "DisplayString"
_HmSec2VpnConnIkeRemoteAddr_Object = MibTableColumn
hmSec2VpnConnIkeRemoteAddr = _HmSec2VpnConnIkeRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 8),
    _HmSec2VpnConnIkeRemoteAddr_Type()
)
hmSec2VpnConnIkeRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeRemoteAddr.setStatus("current")


class _HmSec2VpnConnIkeAuthType_Type(Integer32):
    """Custom type hmSec2VpnConnIkeAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("psk", 1),
          ("x509rsa", 2))
    )


_HmSec2VpnConnIkeAuthType_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeAuthType_Object = MibTableColumn
hmSec2VpnConnIkeAuthType = _HmSec2VpnConnIkeAuthType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 9),
    _HmSec2VpnConnIkeAuthType_Type()
)
hmSec2VpnConnIkeAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthType.setStatus("current")


class _HmSec2VpnConnIkeAuthMode_Type(Integer32):
    """Custom type hmSec2VpnConnIkeAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mainaggressive", 1),
          ("main", 2),
          ("aggressive", 3))
    )


_HmSec2VpnConnIkeAuthMode_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeAuthMode_Object = MibTableColumn
hmSec2VpnConnIkeAuthMode = _HmSec2VpnConnIkeAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 10),
    _HmSec2VpnConnIkeAuthMode_Type()
)
hmSec2VpnConnIkeAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthMode.setStatus("current")


class _HmSec2VpnConnIkeAuthCertCA_Type(OctetString):
    """Custom type hmSec2VpnConnIkeAuthCertCA based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6144),
    )


_HmSec2VpnConnIkeAuthCertCA_Type.__name__ = "OctetString"
_HmSec2VpnConnIkeAuthCertCA_Object = MibTableColumn
hmSec2VpnConnIkeAuthCertCA = _HmSec2VpnConnIkeAuthCertCA_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 11),
    _HmSec2VpnConnIkeAuthCertCA_Type()
)
hmSec2VpnConnIkeAuthCertCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthCertCA.setStatus("current")


class _HmSec2VpnConnIkeAuthCertRemote_Type(OctetString):
    """Custom type hmSec2VpnConnIkeAuthCertRemote based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6144),
    )


_HmSec2VpnConnIkeAuthCertRemote_Type.__name__ = "OctetString"
_HmSec2VpnConnIkeAuthCertRemote_Object = MibTableColumn
hmSec2VpnConnIkeAuthCertRemote = _HmSec2VpnConnIkeAuthCertRemote_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 12),
    _HmSec2VpnConnIkeAuthCertRemote_Type()
)
hmSec2VpnConnIkeAuthCertRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthCertRemote.setStatus("current")


class _HmSec2VpnConnIkeAuthCertLocal_Type(OctetString):
    """Custom type hmSec2VpnConnIkeAuthCertLocal based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6144),
    )


_HmSec2VpnConnIkeAuthCertLocal_Type.__name__ = "OctetString"
_HmSec2VpnConnIkeAuthCertLocal_Object = MibTableColumn
hmSec2VpnConnIkeAuthCertLocal = _HmSec2VpnConnIkeAuthCertLocal_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 13),
    _HmSec2VpnConnIkeAuthCertLocal_Type()
)
hmSec2VpnConnIkeAuthCertLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthCertLocal.setStatus("current")


class _HmSec2VpnConnIkeAuthPrivKey_Type(OctetString):
    """Custom type hmSec2VpnConnIkeAuthPrivKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6144),
    )


_HmSec2VpnConnIkeAuthPrivKey_Type.__name__ = "OctetString"
_HmSec2VpnConnIkeAuthPrivKey_Object = MibTableColumn
hmSec2VpnConnIkeAuthPrivKey = _HmSec2VpnConnIkeAuthPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 14),
    _HmSec2VpnConnIkeAuthPrivKey_Type()
)
hmSec2VpnConnIkeAuthPrivKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthPrivKey.setStatus("current")


class _HmSec2VpnConnIkeAuthPasswd_Type(DisplayString):
    """Custom type hmSec2VpnConnIkeAuthPasswd based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2VpnConnIkeAuthPasswd_Type.__name__ = "DisplayString"
_HmSec2VpnConnIkeAuthPasswd_Object = MibTableColumn
hmSec2VpnConnIkeAuthPasswd = _HmSec2VpnConnIkeAuthPasswd_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 15),
    _HmSec2VpnConnIkeAuthPasswd_Type()
)
hmSec2VpnConnIkeAuthPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthPasswd.setStatus("current")


class _HmSec2VpnConnIkeAuthPsk_Type(DisplayString):
    """Custom type hmSec2VpnConnIkeAuthPsk based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2VpnConnIkeAuthPsk_Type.__name__ = "DisplayString"
_HmSec2VpnConnIkeAuthPsk_Object = MibTableColumn
hmSec2VpnConnIkeAuthPsk = _HmSec2VpnConnIkeAuthPsk_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 16),
    _HmSec2VpnConnIkeAuthPsk_Type()
)
hmSec2VpnConnIkeAuthPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthPsk.setStatus("current")


class _HmSec2VpnConnIkeAuthLocId_Type(DisplayString):
    """Custom type hmSec2VpnConnIkeAuthLocId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmSec2VpnConnIkeAuthLocId_Type.__name__ = "DisplayString"
_HmSec2VpnConnIkeAuthLocId_Object = MibTableColumn
hmSec2VpnConnIkeAuthLocId = _HmSec2VpnConnIkeAuthLocId_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 17),
    _HmSec2VpnConnIkeAuthLocId_Type()
)
hmSec2VpnConnIkeAuthLocId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthLocId.setStatus("current")


class _HmSec2VpnConnIkeAuthLocType_Type(Integer32):
    """Custom type hmSec2VpnConnIkeAuthLocType based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("ipaddr", 2),
          ("keyid", 3),
          ("fqdn", 4),
          ("email", 5),
          ("asn1dn", 6))
    )


_HmSec2VpnConnIkeAuthLocType_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeAuthLocType_Object = MibTableColumn
hmSec2VpnConnIkeAuthLocType = _HmSec2VpnConnIkeAuthLocType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 18),
    _HmSec2VpnConnIkeAuthLocType_Type()
)
hmSec2VpnConnIkeAuthLocType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthLocType.setStatus("current")


class _HmSec2VpnConnIkeAuthRemId_Type(DisplayString):
    """Custom type hmSec2VpnConnIkeAuthRemId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmSec2VpnConnIkeAuthRemId_Type.__name__ = "DisplayString"
_HmSec2VpnConnIkeAuthRemId_Object = MibTableColumn
hmSec2VpnConnIkeAuthRemId = _HmSec2VpnConnIkeAuthRemId_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 19),
    _HmSec2VpnConnIkeAuthRemId_Type()
)
hmSec2VpnConnIkeAuthRemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthRemId.setStatus("current")


class _HmSec2VpnConnIkeAuthRemType_Type(Integer32):
    """Custom type hmSec2VpnConnIkeAuthRemType based on Integer32"""
    defaultValue = 1

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
        *(("any", 1),
          ("ipaddr", 2),
          ("keyid", 3),
          ("fqdn", 4),
          ("email", 5),
          ("asn1dn", 6))
    )


_HmSec2VpnConnIkeAuthRemType_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeAuthRemType_Object = MibTableColumn
hmSec2VpnConnIkeAuthRemType = _HmSec2VpnConnIkeAuthRemType_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 20),
    _HmSec2VpnConnIkeAuthRemType_Type()
)
hmSec2VpnConnIkeAuthRemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAuthRemType.setStatus("current")


class _HmSec2VpnConnIkeAlgDh_Type(Integer32):
    """Custom type hmSec2VpnConnIkeAlgDh based on Integer32"""
    defaultValue = 3

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
        *(("any", 1),
          ("modp768", 2),
          ("modp1024", 3),
          ("modp1536", 4),
          ("modp2048", 5),
          ("modp3072", 6),
          ("modp4096", 7))
    )


_HmSec2VpnConnIkeAlgDh_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeAlgDh_Object = MibTableColumn
hmSec2VpnConnIkeAlgDh = _HmSec2VpnConnIkeAlgDh_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 21),
    _HmSec2VpnConnIkeAlgDh_Type()
)
hmSec2VpnConnIkeAlgDh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAlgDh.setStatus("current")


class _HmSec2VpnConnIkeAlgHash_Type(Integer32):
    """Custom type hmSec2VpnConnIkeAlgHash based on Integer32"""
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
        *(("any", 1),
          ("md5", 2),
          ("sha1", 3))
    )


_HmSec2VpnConnIkeAlgHash_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeAlgHash_Object = MibTableColumn
hmSec2VpnConnIkeAlgHash = _HmSec2VpnConnIkeAlgHash_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 22),
    _HmSec2VpnConnIkeAlgHash_Type()
)
hmSec2VpnConnIkeAlgHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAlgHash.setStatus("current")


class _HmSec2VpnConnIkeAlgMac_Type(Integer32):
    """Custom type hmSec2VpnConnIkeAlgMac based on Integer32"""
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
        *(("any", 1),
          ("hmacmd5", 2),
          ("hmacsha1", 3))
    )


_HmSec2VpnConnIkeAlgMac_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeAlgMac_Object = MibTableColumn
hmSec2VpnConnIkeAlgMac = _HmSec2VpnConnIkeAlgMac_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 23),
    _HmSec2VpnConnIkeAlgMac_Type()
)
hmSec2VpnConnIkeAlgMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAlgMac.setStatus("current")


class _HmSec2VpnConnIkeAlgEncr_Type(Integer32):
    """Custom type hmSec2VpnConnIkeAlgEncr based on Integer32"""
    defaultValue = 3

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
        *(("any", 1),
          ("des", 2),
          ("des3", 3),
          ("aes128", 4),
          ("aes192", 5),
          ("aes256", 6))
    )


_HmSec2VpnConnIkeAlgEncr_Type.__name__ = "Integer32"
_HmSec2VpnConnIkeAlgEncr_Object = MibTableColumn
hmSec2VpnConnIkeAlgEncr = _HmSec2VpnConnIkeAlgEncr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 24),
    _HmSec2VpnConnIkeAlgEncr_Type()
)
hmSec2VpnConnIkeAlgEncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIkeAlgEncr.setStatus("current")


class _HmSec2VpnConnIpsecMode_Type(Integer32):
    """Custom type hmSec2VpnConnIpsecMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 1),
          ("tunnel", 2))
    )


_HmSec2VpnConnIpsecMode_Type.__name__ = "Integer32"
_HmSec2VpnConnIpsecMode_Object = MibTableColumn
hmSec2VpnConnIpsecMode = _HmSec2VpnConnIpsecMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 25),
    _HmSec2VpnConnIpsecMode_Type()
)
hmSec2VpnConnIpsecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIpsecMode.setStatus("current")


class _HmSec2VpnConnIpsecNatTraversal_Type(Integer32):
    """Custom type hmSec2VpnConnIpsecNatTraversal based on Integer32"""
    defaultValue = 2

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


_HmSec2VpnConnIpsecNatTraversal_Type.__name__ = "Integer32"
_HmSec2VpnConnIpsecNatTraversal_Object = MibTableColumn
hmSec2VpnConnIpsecNatTraversal = _HmSec2VpnConnIpsecNatTraversal_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 26),
    _HmSec2VpnConnIpsecNatTraversal_Type()
)
hmSec2VpnConnIpsecNatTraversal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIpsecNatTraversal.setStatus("current")


class _HmSec2VpnConnIpsecLifetime_Type(Integer32):
    """Custom type hmSec2VpnConnIpsecLifetime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28800),
    )


_HmSec2VpnConnIpsecLifetime_Type.__name__ = "Integer32"
_HmSec2VpnConnIpsecLifetime_Object = MibTableColumn
hmSec2VpnConnIpsecLifetime = _HmSec2VpnConnIpsecLifetime_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 27),
    _HmSec2VpnConnIpsecLifetime_Type()
)
hmSec2VpnConnIpsecLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIpsecLifetime.setStatus("current")


class _HmSec2VpnConnIpsecAlgDh_Type(Integer32):
    """Custom type hmSec2VpnConnIpsecAlgDh based on Integer32"""
    defaultValue = 3

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
        *(("any", 1),
          ("modp768", 2),
          ("modp1024", 3),
          ("modp1536", 4),
          ("modp2048", 5),
          ("modp3072", 6),
          ("modp4096", 7),
          ("none", 8))
    )


_HmSec2VpnConnIpsecAlgDh_Type.__name__ = "Integer32"
_HmSec2VpnConnIpsecAlgDh_Object = MibTableColumn
hmSec2VpnConnIpsecAlgDh = _HmSec2VpnConnIpsecAlgDh_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 28),
    _HmSec2VpnConnIpsecAlgDh_Type()
)
hmSec2VpnConnIpsecAlgDh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIpsecAlgDh.setStatus("current")


class _HmSec2VpnConnIpsecAlgMac_Type(Integer32):
    """Custom type hmSec2VpnConnIpsecAlgMac based on Integer32"""
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
        *(("any", 1),
          ("hmacmd5", 2),
          ("hmacsha1", 3))
    )


_HmSec2VpnConnIpsecAlgMac_Type.__name__ = "Integer32"
_HmSec2VpnConnIpsecAlgMac_Object = MibTableColumn
hmSec2VpnConnIpsecAlgMac = _HmSec2VpnConnIpsecAlgMac_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 29),
    _HmSec2VpnConnIpsecAlgMac_Type()
)
hmSec2VpnConnIpsecAlgMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIpsecAlgMac.setStatus("current")


class _HmSec2VpnConnIpsecAlgEncr_Type(Integer32):
    """Custom type hmSec2VpnConnIpsecAlgEncr based on Integer32"""
    defaultValue = 3

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
        *(("any", 1),
          ("des", 2),
          ("des3", 3),
          ("aes128", 4),
          ("aes192", 5),
          ("aes256", 6))
    )


_HmSec2VpnConnIpsecAlgEncr_Type.__name__ = "Integer32"
_HmSec2VpnConnIpsecAlgEncr_Object = MibTableColumn
hmSec2VpnConnIpsecAlgEncr = _HmSec2VpnConnIpsecAlgEncr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 30),
    _HmSec2VpnConnIpsecAlgEncr_Type()
)
hmSec2VpnConnIpsecAlgEncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnIpsecAlgEncr.setStatus("current")


class _HmSec2VpnConnOperStatus_Type(Integer32):
    """Custom type hmSec2VpnConnOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("negotiation", 3),
          ("constructing", 4),
          ("dormant", 5),
          ("servicemode-up", 6))
    )


_HmSec2VpnConnOperStatus_Type.__name__ = "Integer32"
_HmSec2VpnConnOperStatus_Object = MibTableColumn
hmSec2VpnConnOperStatus = _HmSec2VpnConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 31),
    _HmSec2VpnConnOperStatus_Type()
)
hmSec2VpnConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2VpnConnOperStatus.setStatus("current")


class _HmSec2VpnConnDesc_Type(DisplayString):
    """Custom type hmSec2VpnConnDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2VpnConnDesc_Type.__name__ = "DisplayString"
_HmSec2VpnConnDesc_Object = MibTableColumn
hmSec2VpnConnDesc = _HmSec2VpnConnDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 32),
    _HmSec2VpnConnDesc_Type()
)
hmSec2VpnConnDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnDesc.setStatus("current")
_HmSec2VpnConnRowStatus_Type = RowStatus
_HmSec2VpnConnRowStatus_Object = MibTableColumn
hmSec2VpnConnRowStatus = _HmSec2VpnConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 33),
    _HmSec2VpnConnRowStatus_Type()
)
hmSec2VpnConnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnRowStatus.setStatus("current")


class _HmSec2VpnConnServiceMode_Type(Integer32):
    """Custom type hmSec2VpnConnServiceMode based on Integer32"""
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


_HmSec2VpnConnServiceMode_Type.__name__ = "Integer32"
_HmSec2VpnConnServiceMode_Object = MibTableColumn
hmSec2VpnConnServiceMode = _HmSec2VpnConnServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 2, 3, 1, 34),
    _HmSec2VpnConnServiceMode_Type()
)
hmSec2VpnConnServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnConnServiceMode.setStatus("current")
_HmSec2VpnTrafficSelGroup_ObjectIdentity = ObjectIdentity
hmSec2VpnTrafficSelGroup = _HmSec2VpnTrafficSelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3)
)
_HmSec2VpnTrafficSelTable_Object = MibTable
hmSec2VpnTrafficSelTable = _HmSec2VpnTrafficSelTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelTable.setStatus("current")
_HmSec2VpnTrafficSelEntry_Object = MibTableRow
hmSec2VpnTrafficSelEntry = _HmSec2VpnTrafficSelEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1)
)
hmSec2VpnTrafficSelEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2VpnConnIndex"),
    (0, "ABBSECURITY2-MIB", "hmSec2VpnTrafficSelIndex"),
)
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelEntry.setStatus("current")
_HmSec2VpnTrafficSelIndex_Type = Integer32
_HmSec2VpnTrafficSelIndex_Object = MibTableColumn
hmSec2VpnTrafficSelIndex = _HmSec2VpnTrafficSelIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 1),
    _HmSec2VpnTrafficSelIndex_Type()
)
hmSec2VpnTrafficSelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelIndex.setStatus("current")


class _HmSec2VpnTrafficSelSrcAddr_Type(DisplayString):
    """Custom type hmSec2VpnTrafficSelSrcAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2VpnTrafficSelSrcAddr_Type.__name__ = "DisplayString"
_HmSec2VpnTrafficSelSrcAddr_Object = MibTableColumn
hmSec2VpnTrafficSelSrcAddr = _HmSec2VpnTrafficSelSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 3),
    _HmSec2VpnTrafficSelSrcAddr_Type()
)
hmSec2VpnTrafficSelSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelSrcAddr.setStatus("current")


class _HmSec2VpnTrafficSelDstAddr_Type(DisplayString):
    """Custom type hmSec2VpnTrafficSelDstAddr based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2VpnTrafficSelDstAddr_Type.__name__ = "DisplayString"
_HmSec2VpnTrafficSelDstAddr_Object = MibTableColumn
hmSec2VpnTrafficSelDstAddr = _HmSec2VpnTrafficSelDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 4),
    _HmSec2VpnTrafficSelDstAddr_Type()
)
hmSec2VpnTrafficSelDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelDstAddr.setStatus("current")


class _HmSec2VpnTrafficSelSrcPort_Type(DisplayString):
    """Custom type hmSec2VpnTrafficSelSrcPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2VpnTrafficSelSrcPort_Type.__name__ = "DisplayString"
_HmSec2VpnTrafficSelSrcPort_Object = MibTableColumn
hmSec2VpnTrafficSelSrcPort = _HmSec2VpnTrafficSelSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 5),
    _HmSec2VpnTrafficSelSrcPort_Type()
)
hmSec2VpnTrafficSelSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelSrcPort.setStatus("current")


class _HmSec2VpnTrafficSelDstPort_Type(DisplayString):
    """Custom type hmSec2VpnTrafficSelDstPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2VpnTrafficSelDstPort_Type.__name__ = "DisplayString"
_HmSec2VpnTrafficSelDstPort_Object = MibTableColumn
hmSec2VpnTrafficSelDstPort = _HmSec2VpnTrafficSelDstPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 6),
    _HmSec2VpnTrafficSelDstPort_Type()
)
hmSec2VpnTrafficSelDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelDstPort.setStatus("current")


class _HmSec2VpnTrafficSelProto_Type(DisplayString):
    """Custom type hmSec2VpnTrafficSelProto based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmSec2VpnTrafficSelProto_Type.__name__ = "DisplayString"
_HmSec2VpnTrafficSelProto_Object = MibTableColumn
hmSec2VpnTrafficSelProto = _HmSec2VpnTrafficSelProto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 7),
    _HmSec2VpnTrafficSelProto_Type()
)
hmSec2VpnTrafficSelProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelProto.setStatus("current")


class _HmSec2VpnTrafficSelPolicy_Type(DisplayString):
    """Custom type hmSec2VpnTrafficSelPolicy based on DisplayString"""
    defaultValue = OctetString("require")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HmSec2VpnTrafficSelPolicy_Type.__name__ = "DisplayString"
_HmSec2VpnTrafficSelPolicy_Object = MibTableColumn
hmSec2VpnTrafficSelPolicy = _HmSec2VpnTrafficSelPolicy_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 8),
    _HmSec2VpnTrafficSelPolicy_Type()
)
hmSec2VpnTrafficSelPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelPolicy.setStatus("current")


class _HmSec2VpnTrafficSelDesc_Type(DisplayString):
    """Custom type hmSec2VpnTrafficSelDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2VpnTrafficSelDesc_Type.__name__ = "DisplayString"
_HmSec2VpnTrafficSelDesc_Object = MibTableColumn
hmSec2VpnTrafficSelDesc = _HmSec2VpnTrafficSelDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 9),
    _HmSec2VpnTrafficSelDesc_Type()
)
hmSec2VpnTrafficSelDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelDesc.setStatus("current")
_HmSec2VpnTrafficSelRowStatus_Type = RowStatus
_HmSec2VpnTrafficSelRowStatus_Object = MibTableColumn
hmSec2VpnTrafficSelRowStatus = _HmSec2VpnTrafficSelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 10),
    _HmSec2VpnTrafficSelRowStatus_Type()
)
hmSec2VpnTrafficSelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelRowStatus.setStatus("current")


class _HmSec2VpnTrafficSelSrcMapping_Type(DisplayString):
    """Custom type hmSec2VpnTrafficSelSrcMapping based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2VpnTrafficSelSrcMapping_Type.__name__ = "DisplayString"
_HmSec2VpnTrafficSelSrcMapping_Object = MibTableColumn
hmSec2VpnTrafficSelSrcMapping = _HmSec2VpnTrafficSelSrcMapping_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 11),
    _HmSec2VpnTrafficSelSrcMapping_Type()
)
hmSec2VpnTrafficSelSrcMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelSrcMapping.setStatus("current")


class _HmSec2VpnTrafficSelDstMapping_Type(DisplayString):
    """Custom type hmSec2VpnTrafficSelDstMapping based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2VpnTrafficSelDstMapping_Type.__name__ = "DisplayString"
_HmSec2VpnTrafficSelDstMapping_Object = MibTableColumn
hmSec2VpnTrafficSelDstMapping = _HmSec2VpnTrafficSelDstMapping_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 3, 1, 1, 12),
    _HmSec2VpnTrafficSelDstMapping_Type()
)
hmSec2VpnTrafficSelDstMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnTrafficSelDstMapping.setStatus("current")
_HmSec2VpnCertificateGroup_ObjectIdentity = ObjectIdentity
hmSec2VpnCertificateGroup = _HmSec2VpnCertificateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 4)
)


class _HmSec2VpnCertificateValidation_Type(Integer32):
    """Custom type hmSec2VpnCertificateValidation based on Integer32"""
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


_HmSec2VpnCertificateValidation_Type.__name__ = "Integer32"
_HmSec2VpnCertificateValidation_Object = MibScalar
hmSec2VpnCertificateValidation = _HmSec2VpnCertificateValidation_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 13, 1, 4, 4),
    _HmSec2VpnCertificateValidation_Type()
)
hmSec2VpnCertificateValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2VpnCertificateValidation.setStatus("current")
_HmSec2Redundancy_ObjectIdentity = ObjectIdentity
hmSec2Redundancy = _HmSec2Redundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14)
)
_HmSec2RedRouterGroup_ObjectIdentity = ObjectIdentity
hmSec2RedRouterGroup = _HmSec2RedRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1)
)


class _HmSec2RedAdminState_Type(Integer32):
    """Custom type hmSec2RedAdminState based on Integer32"""
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


_HmSec2RedAdminState_Type.__name__ = "Integer32"
_HmSec2RedAdminState_Object = MibScalar
hmSec2RedAdminState = _HmSec2RedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 1),
    _HmSec2RedAdminState_Type()
)
hmSec2RedAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RedAdminState.setStatus("current")


class _HmSec2RedStartupState_Type(Integer32):
    """Custom type hmSec2RedStartupState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("backup", 2))
    )


_HmSec2RedStartupState_Type.__name__ = "Integer32"
_HmSec2RedStartupState_Object = MibScalar
hmSec2RedStartupState = _HmSec2RedStartupState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 2),
    _HmSec2RedStartupState_Type()
)
hmSec2RedStartupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RedStartupState.setStatus("current")


class _HmSec2RedPriority_Type(Integer32):
    """Custom type hmSec2RedPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HmSec2RedPriority_Type.__name__ = "Integer32"
_HmSec2RedPriority_Object = MibScalar
hmSec2RedPriority = _HmSec2RedPriority_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 3),
    _HmSec2RedPriority_Type()
)
hmSec2RedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RedPriority.setStatus("current")


class _HmSec2RedOperState_Type(Integer32):
    """Custom type hmSec2RedOperState based on Integer32"""
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
        *(("master", 1),
          ("backup", 2),
          ("outofservice", 3))
    )


_HmSec2RedOperState_Type.__name__ = "Integer32"
_HmSec2RedOperState_Object = MibScalar
hmSec2RedOperState = _HmSec2RedOperState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 4),
    _HmSec2RedOperState_Type()
)
hmSec2RedOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2RedOperState.setStatus("current")


class _HmSec2RedOperInfo_Type(DisplayString):
    """Custom type hmSec2RedOperInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2RedOperInfo_Type.__name__ = "DisplayString"
_HmSec2RedOperInfo_Object = MibScalar
hmSec2RedOperInfo = _HmSec2RedOperInfo_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 5),
    _HmSec2RedOperInfo_Type()
)
hmSec2RedOperInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2RedOperInfo.setStatus("current")
_HmSec2RedIfaceTable_Object = MibTable
hmSec2RedIfaceTable = _HmSec2RedIfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 6)
)
if mibBuilder.loadTexts:
    hmSec2RedIfaceTable.setStatus("current")
_HmSec2RedIfaceEntry_Object = MibTableRow
hmSec2RedIfaceEntry = _HmSec2RedIfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 6, 1)
)
hmSec2RedIfaceEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2RedIfIndex"),
)
if mibBuilder.loadTexts:
    hmSec2RedIfaceEntry.setStatus("current")
_HmSec2RedIfIndex_Type = Integer32
_HmSec2RedIfIndex_Object = MibTableColumn
hmSec2RedIfIndex = _HmSec2RedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 6, 1, 1),
    _HmSec2RedIfIndex_Type()
)
hmSec2RedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2RedIfIndex.setStatus("current")
_HmSec2RedVirtualAddr_Type = IpAddress
_HmSec2RedVirtualAddr_Object = MibTableColumn
hmSec2RedVirtualAddr = _HmSec2RedVirtualAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 6, 1, 2),
    _HmSec2RedVirtualAddr_Type()
)
hmSec2RedVirtualAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RedVirtualAddr.setStatus("current")


class _HmSec2RedVRID_Type(Integer32):
    """Custom type hmSec2RedVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HmSec2RedVRID_Type.__name__ = "Integer32"
_HmSec2RedVRID_Object = MibTableColumn
hmSec2RedVRID = _HmSec2RedVRID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 6, 1, 3),
    _HmSec2RedVRID_Type()
)
hmSec2RedVRID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RedVRID.setStatus("current")
_HmSec2RedRemoteIPAddr_Type = IpAddress
_HmSec2RedRemoteIPAddr_Object = MibTableColumn
hmSec2RedRemoteIPAddr = _HmSec2RedRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 6, 1, 4),
    _HmSec2RedRemoteIPAddr_Type()
)
hmSec2RedRemoteIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RedRemoteIPAddr.setStatus("current")
_HmSec2RedSwitchCounter_Type = Integer32
_HmSec2RedSwitchCounter_Object = MibScalar
hmSec2RedSwitchCounter = _HmSec2RedSwitchCounter_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 1, 7),
    _HmSec2RedSwitchCounter_Type()
)
hmSec2RedSwitchCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2RedSwitchCounter.setStatus("current")
_HmSec2HostCheckGroup_ObjectIdentity = ObjectIdentity
hmSec2HostCheckGroup = _HmSec2HostCheckGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2)
)


class _HmSec2HostCheckAdminState_Type(Integer32):
    """Custom type hmSec2HostCheckAdminState based on Integer32"""
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


_HmSec2HostCheckAdminState_Type.__name__ = "Integer32"
_HmSec2HostCheckAdminState_Object = MibScalar
hmSec2HostCheckAdminState = _HmSec2HostCheckAdminState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2, 1),
    _HmSec2HostCheckAdminState_Type()
)
hmSec2HostCheckAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2HostCheckAdminState.setStatus("current")
_HmSec2HostCheckNumAddrs_Type = Integer32
_HmSec2HostCheckNumAddrs_Object = MibScalar
hmSec2HostCheckNumAddrs = _HmSec2HostCheckNumAddrs_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2, 2),
    _HmSec2HostCheckNumAddrs_Type()
)
hmSec2HostCheckNumAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2HostCheckNumAddrs.setStatus("current")


class _HmSec2HostCheckOperState_Type(Integer32):
    """Custom type hmSec2HostCheckOperState based on Integer32"""
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
        *(("running", 1),
          ("notchecking", 2),
          ("outofservice", 3))
    )


_HmSec2HostCheckOperState_Type.__name__ = "Integer32"
_HmSec2HostCheckOperState_Object = MibScalar
hmSec2HostCheckOperState = _HmSec2HostCheckOperState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2, 3),
    _HmSec2HostCheckOperState_Type()
)
hmSec2HostCheckOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2HostCheckOperState.setStatus("current")


class _HmSec2HostCheckOperInfo_Type(DisplayString):
    """Custom type hmSec2HostCheckOperInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2HostCheckOperInfo_Type.__name__ = "DisplayString"
_HmSec2HostCheckOperInfo_Object = MibScalar
hmSec2HostCheckOperInfo = _HmSec2HostCheckOperInfo_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2, 4),
    _HmSec2HostCheckOperInfo_Type()
)
hmSec2HostCheckOperInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2HostCheckOperInfo.setStatus("current")
_HmSec2HostCheckTable_Object = MibTable
hmSec2HostCheckTable = _HmSec2HostCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2, 5)
)
if mibBuilder.loadTexts:
    hmSec2HostCheckTable.setStatus("current")
_HmSec2HostCheckEntry_Object = MibTableRow
hmSec2HostCheckEntry = _HmSec2HostCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2, 5, 1)
)
hmSec2HostCheckEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2HostCheckIfIndex"),
    (0, "ABBSECURITY2-MIB", "hmSec2HostCheckTableIndex"),
)
if mibBuilder.loadTexts:
    hmSec2HostCheckEntry.setStatus("current")
_HmSec2HostCheckIfIndex_Type = Integer32
_HmSec2HostCheckIfIndex_Object = MibTableColumn
hmSec2HostCheckIfIndex = _HmSec2HostCheckIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2, 5, 1, 1),
    _HmSec2HostCheckIfIndex_Type()
)
hmSec2HostCheckIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2HostCheckIfIndex.setStatus("current")
_HmSec2HostCheckTableIndex_Type = Integer32
_HmSec2HostCheckTableIndex_Object = MibTableColumn
hmSec2HostCheckTableIndex = _HmSec2HostCheckTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2, 5, 1, 2),
    _HmSec2HostCheckTableIndex_Type()
)
hmSec2HostCheckTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2HostCheckTableIndex.setStatus("current")
_HmSec2HostCheckAddr_Type = IpAddress
_HmSec2HostCheckAddr_Object = MibTableColumn
hmSec2HostCheckAddr = _HmSec2HostCheckAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2, 5, 1, 3),
    _HmSec2HostCheckAddr_Type()
)
hmSec2HostCheckAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2HostCheckAddr.setStatus("current")
_HmSec2HostCheckRowStatus_Type = RowStatus
_HmSec2HostCheckRowStatus_Object = MibTableColumn
hmSec2HostCheckRowStatus = _HmSec2HostCheckRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 2, 5, 1, 4),
    _HmSec2HostCheckRowStatus_Type()
)
hmSec2HostCheckRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2HostCheckRowStatus.setStatus("current")
_HmSec2RedLayer2Group_ObjectIdentity = ObjectIdentity
hmSec2RedLayer2Group = _HmSec2RedLayer2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 3)
)


class _HmSec2RedLayer2AdminState_Type(Integer32):
    """Custom type hmSec2RedLayer2AdminState based on Integer32"""
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


_HmSec2RedLayer2AdminState_Type.__name__ = "Integer32"
_HmSec2RedLayer2AdminState_Object = MibScalar
hmSec2RedLayer2AdminState = _HmSec2RedLayer2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 3, 1),
    _HmSec2RedLayer2AdminState_Type()
)
hmSec2RedLayer2AdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RedLayer2AdminState.setStatus("current")
_HmSec2RedLayer2IfIndex_Type = Integer32
_HmSec2RedLayer2IfIndex_Object = MibScalar
hmSec2RedLayer2IfIndex = _HmSec2RedLayer2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 3, 2),
    _HmSec2RedLayer2IfIndex_Type()
)
hmSec2RedLayer2IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RedLayer2IfIndex.setStatus("current")
_HmSec2RedLayer2Packetcounter_Type = Integer32
_HmSec2RedLayer2Packetcounter_Object = MibScalar
hmSec2RedLayer2Packetcounter = _HmSec2RedLayer2Packetcounter_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 3, 3),
    _HmSec2RedLayer2Packetcounter_Type()
)
hmSec2RedLayer2Packetcounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2RedLayer2Packetcounter.setStatus("current")
_HmSec2RedTransparentGroup_ObjectIdentity = ObjectIdentity
hmSec2RedTransparentGroup = _HmSec2RedTransparentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 4)
)
_HmSec2RedTPRemoteIPAddr_Type = IpAddress
_HmSec2RedTPRemoteIPAddr_Object = MibScalar
hmSec2RedTPRemoteIPAddr = _HmSec2RedTPRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 4, 1),
    _HmSec2RedTPRemoteIPAddr_Type()
)
hmSec2RedTPRemoteIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2RedTPRemoteIPAddr.setStatus("current")


class _HmSec2RedTPOperState_Type(Integer32):
    """Custom type hmSec2RedTPOperState based on Integer32"""
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
        *(("master", 1),
          ("backup", 2),
          ("outofservice", 3))
    )


_HmSec2RedTPOperState_Type.__name__ = "Integer32"
_HmSec2RedTPOperState_Object = MibScalar
hmSec2RedTPOperState = _HmSec2RedTPOperState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 4, 2),
    _HmSec2RedTPOperState_Type()
)
hmSec2RedTPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2RedTPOperState.setStatus("current")


class _HmSec2RedTPOperInfo_Type(DisplayString):
    """Custom type hmSec2RedTPOperInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2RedTPOperInfo_Type.__name__ = "DisplayString"
_HmSec2RedTPOperInfo_Object = MibScalar
hmSec2RedTPOperInfo = _HmSec2RedTPOperInfo_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 4, 3),
    _HmSec2RedTPOperInfo_Type()
)
hmSec2RedTPOperInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2RedTPOperInfo.setStatus("current")


class _HmSec2RedTPCommunicationState_Type(Integer32):
    """Custom type hmSec2RedTPCommunicationState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HmSec2RedTPCommunicationState_Type.__name__ = "Integer32"
_HmSec2RedTPCommunicationState_Object = MibScalar
hmSec2RedTPCommunicationState = _HmSec2RedTPCommunicationState_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 14, 4, 4),
    _HmSec2RedTPCommunicationState_Type()
)
hmSec2RedTPCommunicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2RedTPCommunicationState.setStatus("current")
_HmSec2Nat_ObjectIdentity = ObjectIdentity
hmSec2Nat = _HmSec2Nat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15)
)
_HmSec2NatGeneralGroup_ObjectIdentity = ObjectIdentity
hmSec2NatGeneralGroup = _HmSec2NatGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 1)
)


class _HmSec2NatMappingMax_Type(Integer32):
    """Custom type hmSec2NatMappingMax based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HmSec2NatMappingMax_Type.__name__ = "Integer32"
_HmSec2NatMappingMax_Object = MibScalar
hmSec2NatMappingMax = _HmSec2NatMappingMax_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 1, 1),
    _HmSec2NatMappingMax_Type()
)
hmSec2NatMappingMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatMappingMax.setStatus("current")


class _HmSec2NatTimeoutEstablished_Type(Integer32):
    """Custom type hmSec2NatTimeoutEstablished based on Integer32"""
    defaultValue = 432000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HmSec2NatTimeoutEstablished_Type.__name__ = "Integer32"
_HmSec2NatTimeoutEstablished_Object = MibScalar
hmSec2NatTimeoutEstablished = _HmSec2NatTimeoutEstablished_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 1, 2),
    _HmSec2NatTimeoutEstablished_Type()
)
hmSec2NatTimeoutEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatTimeoutEstablished.setStatus("current")


class _HmSec2NatAllowOutputSameIface_Type(Integer32):
    """Custom type hmSec2NatAllowOutputSameIface based on Integer32"""
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


_HmSec2NatAllowOutputSameIface_Type.__name__ = "Integer32"
_HmSec2NatAllowOutputSameIface_Object = MibScalar
hmSec2NatAllowOutputSameIface = _HmSec2NatAllowOutputSameIface_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 1, 3),
    _HmSec2NatAllowOutputSameIface_Type()
)
hmSec2NatAllowOutputSameIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatAllowOutputSameIface.setStatus("current")
_HmSec2NatRulesGroup_ObjectIdentity = ObjectIdentity
hmSec2NatRulesGroup = _HmSec2NatRulesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2)
)
_HmSec2NatTable_Object = MibTable
hmSec2NatTable = _HmSec2NatTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    hmSec2NatTable.setStatus("current")
_HmSec2NatEntry_Object = MibTableRow
hmSec2NatEntry = _HmSec2NatEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 1, 1)
)
hmSec2NatEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2NatIndex"),
)
if mibBuilder.loadTexts:
    hmSec2NatEntry.setStatus("current")
_HmSec2NatIndex_Type = Integer32
_HmSec2NatIndex_Object = MibTableColumn
hmSec2NatIndex = _HmSec2NatIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 1, 1, 1),
    _HmSec2NatIndex_Type()
)
hmSec2NatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2NatIndex.setStatus("current")


class _HmSec2NatSrcNet_Type(DisplayString):
    """Custom type hmSec2NatSrcNet based on DisplayString"""
    defaultValue = OctetString("192.168.1.0/24")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2NatSrcNet_Type.__name__ = "DisplayString"
_HmSec2NatSrcNet_Object = MibTableColumn
hmSec2NatSrcNet = _HmSec2NatSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 1, 1, 2),
    _HmSec2NatSrcNet_Type()
)
hmSec2NatSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatSrcNet.setStatus("current")


class _HmSec2NatAlg_Type(Bits):
    """Custom type hmSec2NatAlg based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("ftp", 0)
    )

_HmSec2NatAlg_Type.__name__ = "Bits"
_HmSec2NatAlg_Object = MibTableColumn
hmSec2NatAlg = _HmSec2NatAlg_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 1, 1, 3),
    _HmSec2NatAlg_Type()
)
hmSec2NatAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatAlg.setStatus("current")


class _HmSec2NatDesc_Type(DisplayString):
    """Custom type hmSec2NatDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2NatDesc_Type.__name__ = "DisplayString"
_HmSec2NatDesc_Object = MibTableColumn
hmSec2NatDesc = _HmSec2NatDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 1, 1, 4),
    _HmSec2NatDesc_Type()
)
hmSec2NatDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatDesc.setStatus("current")


class _HmSec2NatErrorText_Type(DisplayString):
    """Custom type hmSec2NatErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2NatErrorText_Type.__name__ = "DisplayString"
_HmSec2NatErrorText_Object = MibTableColumn
hmSec2NatErrorText = _HmSec2NatErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 1, 1, 5),
    _HmSec2NatErrorText_Type()
)
hmSec2NatErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2NatErrorText.setStatus("current")
_HmSec2NatRowStatus_Type = RowStatus
_HmSec2NatRowStatus_Object = MibTableColumn
hmSec2NatRowStatus = _HmSec2NatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 1, 1, 6),
    _HmSec2NatRowStatus_Type()
)
hmSec2NatRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatRowStatus.setStatus("current")
_HmSec2Nat1To1Table_Object = MibTable
hmSec2Nat1To1Table = _HmSec2Nat1To1Table_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2)
)
if mibBuilder.loadTexts:
    hmSec2Nat1To1Table.setStatus("current")
_HmSec2Nat1To1Entry_Object = MibTableRow
hmSec2Nat1To1Entry = _HmSec2Nat1To1Entry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1)
)
hmSec2Nat1To1Entry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2Nat1To1Index"),
)
if mibBuilder.loadTexts:
    hmSec2Nat1To1Entry.setStatus("current")
_HmSec2Nat1To1Index_Type = Integer32
_HmSec2Nat1To1Index_Object = MibTableColumn
hmSec2Nat1To1Index = _HmSec2Nat1To1Index_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1, 1),
    _HmSec2Nat1To1Index_Type()
)
hmSec2Nat1To1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2Nat1To1Index.setStatus("current")


class _HmSec2Nat1To1SrcNet_Type(DisplayString):
    """Custom type hmSec2Nat1To1SrcNet based on DisplayString"""
    defaultValue = OctetString("192.168.1.1")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2Nat1To1SrcNet_Type.__name__ = "DisplayString"
_HmSec2Nat1To1SrcNet_Object = MibTableColumn
hmSec2Nat1To1SrcNet = _HmSec2Nat1To1SrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1, 2),
    _HmSec2Nat1To1SrcNet_Type()
)
hmSec2Nat1To1SrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2Nat1To1SrcNet.setStatus("current")


class _HmSec2Nat1To1DstNet_Type(DisplayString):
    """Custom type hmSec2Nat1To1DstNet based on DisplayString"""
    defaultValue = OctetString("10.0.1.1")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2Nat1To1DstNet_Type.__name__ = "DisplayString"
_HmSec2Nat1To1DstNet_Object = MibTableColumn
hmSec2Nat1To1DstNet = _HmSec2Nat1To1DstNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1, 3),
    _HmSec2Nat1To1DstNet_Type()
)
hmSec2Nat1To1DstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2Nat1To1DstNet.setStatus("current")


class _HmSec2Nat1To1NetMask_Type(Integer32):
    """Custom type hmSec2Nat1To1NetMask based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HmSec2Nat1To1NetMask_Type.__name__ = "Integer32"
_HmSec2Nat1To1NetMask_Object = MibTableColumn
hmSec2Nat1To1NetMask = _HmSec2Nat1To1NetMask_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1, 4),
    _HmSec2Nat1To1NetMask_Type()
)
hmSec2Nat1To1NetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2Nat1To1NetMask.setStatus("current")


class _HmSec2Nat1To1Desc_Type(DisplayString):
    """Custom type hmSec2Nat1To1Desc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2Nat1To1Desc_Type.__name__ = "DisplayString"
_HmSec2Nat1To1Desc_Object = MibTableColumn
hmSec2Nat1To1Desc = _HmSec2Nat1To1Desc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1, 5),
    _HmSec2Nat1To1Desc_Type()
)
hmSec2Nat1To1Desc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2Nat1To1Desc.setStatus("current")


class _HmSec2Nat1To1ErrorText_Type(DisplayString):
    """Custom type hmSec2Nat1To1ErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2Nat1To1ErrorText_Type.__name__ = "DisplayString"
_HmSec2Nat1To1ErrorText_Object = MibTableColumn
hmSec2Nat1To1ErrorText = _HmSec2Nat1To1ErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1, 6),
    _HmSec2Nat1To1ErrorText_Type()
)
hmSec2Nat1To1ErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2Nat1To1ErrorText.setStatus("current")
_HmSec2Nat1To1RowStatus_Type = RowStatus
_HmSec2Nat1To1RowStatus_Object = MibTableColumn
hmSec2Nat1To1RowStatus = _HmSec2Nat1To1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1, 7),
    _HmSec2Nat1To1RowStatus_Type()
)
hmSec2Nat1To1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2Nat1To1RowStatus.setStatus("current")


class _HmSec2Nat1To1Alg_Type(Bits):
    """Custom type hmSec2Nat1To1Alg based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("ftp", 0)
    )

_HmSec2Nat1To1Alg_Type.__name__ = "Bits"
_HmSec2Nat1To1Alg_Object = MibTableColumn
hmSec2Nat1To1Alg = _HmSec2Nat1To1Alg_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1, 8),
    _HmSec2Nat1To1Alg_Type()
)
hmSec2Nat1To1Alg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2Nat1To1Alg.setStatus("current")


class _HmSec2Nat1To1DoOutput_Type(Integer32):
    """Custom type hmSec2Nat1To1DoOutput based on Integer32"""
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


_HmSec2Nat1To1DoOutput_Type.__name__ = "Integer32"
_HmSec2Nat1To1DoOutput_Object = MibTableColumn
hmSec2Nat1To1DoOutput = _HmSec2Nat1To1DoOutput_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1, 9),
    _HmSec2Nat1To1DoOutput_Type()
)
hmSec2Nat1To1DoOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2Nat1To1DoOutput.setStatus("current")


class _HmSec2Nat1To1InvertDirection_Type(Integer32):
    """Custom type hmSec2Nat1To1InvertDirection based on Integer32"""
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


_HmSec2Nat1To1InvertDirection_Type.__name__ = "Integer32"
_HmSec2Nat1To1InvertDirection_Object = MibTableColumn
hmSec2Nat1To1InvertDirection = _HmSec2Nat1To1InvertDirection_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 2, 1, 10),
    _HmSec2Nat1To1InvertDirection_Type()
)
hmSec2Nat1To1InvertDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2Nat1To1InvertDirection.setStatus("current")
_HmSec2NatPortFwdTable_Object = MibTable
hmSec2NatPortFwdTable = _HmSec2NatPortFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3)
)
if mibBuilder.loadTexts:
    hmSec2NatPortFwdTable.setStatus("current")
_HmSec2NatPortFwdEntry_Object = MibTableRow
hmSec2NatPortFwdEntry = _HmSec2NatPortFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1)
)
hmSec2NatPortFwdEntry.setIndexNames(
    (0, "ABBSECURITY2-MIB", "hmSec2NatPortFwdIndex"),
)
if mibBuilder.loadTexts:
    hmSec2NatPortFwdEntry.setStatus("current")
_HmSec2NatPortFwdIndex_Type = Integer32
_HmSec2NatPortFwdIndex_Object = MibTableColumn
hmSec2NatPortFwdIndex = _HmSec2NatPortFwdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 1),
    _HmSec2NatPortFwdIndex_Type()
)
hmSec2NatPortFwdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdIndex.setStatus("current")


class _HmSec2NatPortFwdSrcNet_Type(DisplayString):
    """Custom type hmSec2NatPortFwdSrcNet based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2NatPortFwdSrcNet_Type.__name__ = "DisplayString"
_HmSec2NatPortFwdSrcNet_Object = MibTableColumn
hmSec2NatPortFwdSrcNet = _HmSec2NatPortFwdSrcNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 2),
    _HmSec2NatPortFwdSrcNet_Type()
)
hmSec2NatPortFwdSrcNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdSrcNet.setStatus("current")


class _HmSec2NatPortFwdSrcPort_Type(DisplayString):
    """Custom type hmSec2NatPortFwdSrcPort based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2NatPortFwdSrcPort_Type.__name__ = "DisplayString"
_HmSec2NatPortFwdSrcPort_Object = MibTableColumn
hmSec2NatPortFwdSrcPort = _HmSec2NatPortFwdSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 3),
    _HmSec2NatPortFwdSrcPort_Type()
)
hmSec2NatPortFwdSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdSrcPort.setStatus("current")


class _HmSec2NatPortFwdDstNet_Type(DisplayString):
    """Custom type hmSec2NatPortFwdDstNet based on DisplayString"""
    defaultValue = OctetString("%extern")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2NatPortFwdDstNet_Type.__name__ = "DisplayString"
_HmSec2NatPortFwdDstNet_Object = MibTableColumn
hmSec2NatPortFwdDstNet = _HmSec2NatPortFwdDstNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 4),
    _HmSec2NatPortFwdDstNet_Type()
)
hmSec2NatPortFwdDstNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdDstNet.setStatus("current")


class _HmSec2NatPortFwdDstPort_Type(DisplayString):
    """Custom type hmSec2NatPortFwdDstPort based on DisplayString"""
    defaultValue = OctetString("= 80")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2NatPortFwdDstPort_Type.__name__ = "DisplayString"
_HmSec2NatPortFwdDstPort_Object = MibTableColumn
hmSec2NatPortFwdDstPort = _HmSec2NatPortFwdDstPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 5),
    _HmSec2NatPortFwdDstPort_Type()
)
hmSec2NatPortFwdDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdDstPort.setStatus("current")


class _HmSec2NatPortFwdFwdNet_Type(DisplayString):
    """Custom type hmSec2NatPortFwdFwdNet based on DisplayString"""
    defaultValue = OctetString("127.0.0.1")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2NatPortFwdFwdNet_Type.__name__ = "DisplayString"
_HmSec2NatPortFwdFwdNet_Object = MibTableColumn
hmSec2NatPortFwdFwdNet = _HmSec2NatPortFwdFwdNet_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 6),
    _HmSec2NatPortFwdFwdNet_Type()
)
hmSec2NatPortFwdFwdNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdFwdNet.setStatus("current")


class _HmSec2NatPortFwdFwdPort_Type(DisplayString):
    """Custom type hmSec2NatPortFwdFwdPort based on DisplayString"""
    defaultValue = OctetString("= 80")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2NatPortFwdFwdPort_Type.__name__ = "DisplayString"
_HmSec2NatPortFwdFwdPort_Object = MibTableColumn
hmSec2NatPortFwdFwdPort = _HmSec2NatPortFwdFwdPort_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 7),
    _HmSec2NatPortFwdFwdPort_Type()
)
hmSec2NatPortFwdFwdPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdFwdPort.setStatus("current")


class _HmSec2NatPortFwdProto_Type(DisplayString):
    """Custom type hmSec2NatPortFwdProto based on DisplayString"""
    defaultValue = OctetString("tcp")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HmSec2NatPortFwdProto_Type.__name__ = "DisplayString"
_HmSec2NatPortFwdProto_Object = MibTableColumn
hmSec2NatPortFwdProto = _HmSec2NatPortFwdProto_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 8),
    _HmSec2NatPortFwdProto_Type()
)
hmSec2NatPortFwdProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdProto.setStatus("current")


class _HmSec2NatPortFwdLog_Type(Integer32):
    """Custom type hmSec2NatPortFwdLog based on Integer32"""
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


_HmSec2NatPortFwdLog_Type.__name__ = "Integer32"
_HmSec2NatPortFwdLog_Object = MibTableColumn
hmSec2NatPortFwdLog = _HmSec2NatPortFwdLog_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 9),
    _HmSec2NatPortFwdLog_Type()
)
hmSec2NatPortFwdLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdLog.setStatus("current")


class _HmSec2NatPortFwdDesc_Type(DisplayString):
    """Custom type hmSec2NatPortFwdDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2NatPortFwdDesc_Type.__name__ = "DisplayString"
_HmSec2NatPortFwdDesc_Object = MibTableColumn
hmSec2NatPortFwdDesc = _HmSec2NatPortFwdDesc_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 10),
    _HmSec2NatPortFwdDesc_Type()
)
hmSec2NatPortFwdDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdDesc.setStatus("current")


class _HmSec2NatPortFwdErrorText_Type(DisplayString):
    """Custom type hmSec2NatPortFwdErrorText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmSec2NatPortFwdErrorText_Type.__name__ = "DisplayString"
_HmSec2NatPortFwdErrorText_Object = MibTableColumn
hmSec2NatPortFwdErrorText = _HmSec2NatPortFwdErrorText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 11),
    _HmSec2NatPortFwdErrorText_Type()
)
hmSec2NatPortFwdErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdErrorText.setStatus("current")
_HmSec2NatPortFwdRowStatus_Type = RowStatus
_HmSec2NatPortFwdRowStatus_Object = MibTableColumn
hmSec2NatPortFwdRowStatus = _HmSec2NatPortFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 15, 2, 3, 1, 12),
    _HmSec2NatPortFwdRowStatus_Type()
)
hmSec2NatPortFwdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmSec2NatPortFwdRowStatus.setStatus("current")
_HmSec2Info_ObjectIdentity = ObjectIdentity
hmSec2Info = _HmSec2Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 20)
)
_HmSec2DHCPLastAccessMAC_Type = MacAddress
_HmSec2DHCPLastAccessMAC_Object = MibScalar
hmSec2DHCPLastAccessMAC = _HmSec2DHCPLastAccessMAC_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 20, 1),
    _HmSec2DHCPLastAccessMAC_Type()
)
hmSec2DHCPLastAccessMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2DHCPLastAccessMAC.setStatus("obsolete")
_HmSec2MiscTrapText_Type = DisplayString
_HmSec2MiscTrapText_Object = MibScalar
hmSec2MiscTrapText = _HmSec2MiscTrapText_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 1, 20, 2),
    _HmSec2MiscTrapText_Type()
)
hmSec2MiscTrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmSec2MiscTrapText.setStatus("current")

# Managed Objects groups


# Notification objects

hmSec2DHCPNewClientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0, 1)
)
hmSec2DHCPNewClientTrap.setObjects(
    ("ABBSECURITY2-MIB", "hmSec2DHCPLastAccessMAC")
)
if mibBuilder.loadTexts:
    hmSec2DHCPNewClientTrap.setStatus(
        "current"
    )

hmSec2RedundSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0, 2)
)
hmSec2RedundSwitchTrap.setObjects(
    ("ABBSECURITY2-MIB", "hmSec2RedOperState")
)
if mibBuilder.loadTexts:
    hmSec2RedundSwitchTrap.setStatus(
        "current"
    )

hmSec2VpnDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0, 3)
)
hmSec2VpnDownTrap.setObjects(
    ("ABBSECURITY2-MIB", "hmSec2VpnConnOperStatus")
)
if mibBuilder.loadTexts:
    hmSec2VpnDownTrap.setStatus(
        "current"
    )

hmSec2VpnUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0, 4)
)
hmSec2VpnUpTrap.setObjects(
    ("ABBSECURITY2-MIB", "hmSec2VpnConnOperStatus")
)
if mibBuilder.loadTexts:
    hmSec2VpnUpTrap.setStatus(
        "current"
    )

hmSec2LoginSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0, 5)
)
hmSec2LoginSuccessTrap.setObjects(
      *(("ABB-PRIVATE-MIB", "hmLastLoginUserName"),
        ("ABB-PRIVATE-MIB", "hmLastIpAddr"))
)
if mibBuilder.loadTexts:
    hmSec2LoginSuccessTrap.setStatus(
        "current"
    )

hmSec2LoginFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0, 6)
)
hmSec2LoginFailedTrap.setObjects(
      *(("ABB-PRIVATE-MIB", "hmLastLoginUserName"),
        ("ABB-PRIVATE-MIB", "hmLastIpAddr"))
)
if mibBuilder.loadTexts:
    hmSec2LoginFailedTrap.setStatus(
        "current"
    )

hmSec2UsrFwLogInTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0, 10)
)
hmSec2UsrFwLogInTrap.setObjects(
      *(("ABBSECURITY2-MIB", "hmSec2UsrFwUserName"),
        ("ABBSECURITY2-MIB", "hmSec2UsrFwUserLoginAddr"))
)
if mibBuilder.loadTexts:
    hmSec2UsrFwLogInTrap.setStatus(
        "current"
    )

hmSec2UsrFwLogOutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0, 11)
)
hmSec2UsrFwLogOutTrap.setObjects(
      *(("ABBSECURITY2-MIB", "hmSec2UsrFwUserName"),
        ("ABBSECURITY2-MIB", "hmSec2UsrFwUserLoginAddr"))
)
if mibBuilder.loadTexts:
    hmSec2UsrFwLogOutTrap.setStatus(
        "current"
    )

hmSec2UsrFwLogErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0, 12)
)
hmSec2UsrFwLogErrTrap.setObjects(
      *(("ABBSECURITY2-MIB", "hmSec2UsrFwUserName"),
        ("ABBSECURITY2-MIB", "hmSec2UsrFwUserLoginAddr"))
)
if mibBuilder.loadTexts:
    hmSec2UsrFwLogErrTrap.setStatus(
        "current"
    )

hmSec2FirewallLogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 52, 0, 15)
)
hmSec2FirewallLogTrap.setObjects(
    ("ABBSECURITY2-MIB", "hmSec2MiscTrapText")
)
if mibBuilder.loadTexts:
    hmSec2FirewallLogTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ABBSECURITY2-MIB",
    **{"abb": abb,
       "utilityCommProducts": utilityCommProducts,
       "arFamilyCommProducts": arFamilyCommProducts,
       "hmSecurity2": hmSecurity2,
       "hmSecurity2Event": hmSecurity2Event,
       "hmSec2DHCPNewClientTrap": hmSec2DHCPNewClientTrap,
       "hmSec2RedundSwitchTrap": hmSec2RedundSwitchTrap,
       "hmSec2VpnDownTrap": hmSec2VpnDownTrap,
       "hmSec2VpnUpTrap": hmSec2VpnUpTrap,
       "hmSec2LoginSuccessTrap": hmSec2LoginSuccessTrap,
       "hmSec2LoginFailedTrap": hmSec2LoginFailedTrap,
       "hmSec2UsrFwLogInTrap": hmSec2UsrFwLogInTrap,
       "hmSec2UsrFwLogOutTrap": hmSec2UsrFwLogOutTrap,
       "hmSec2UsrFwLogErrTrap": hmSec2UsrFwLogErrTrap,
       "hmSec2FirewallLogTrap": hmSec2FirewallLogTrap,
       "hmSecurity2Objects": hmSecurity2Objects,
       "hmSec2Device": hmSec2Device,
       "hmSec2Agent": hmSec2Agent,
       "hmSec2WebGroup": hmSec2WebGroup,
       "hmSec2WebLoginAccessWeb": hmSec2WebLoginAccessWeb,
       "hmSec2WebLoginTimeoutWeb": hmSec2WebLoginTimeoutWeb,
       "hmSec2WebHttpsPortNumber": hmSec2WebHttpsPortNumber,
       "hmSec2CliGroup": hmSec2CliGroup,
       "hmSec2CliLoginPrompt": hmSec2CliLoginPrompt,
       "hmSec2CliLoginTimeoutSerial": hmSec2CliLoginTimeoutSerial,
       "hmSec2CliLoginTimeoutSSH": hmSec2CliLoginTimeoutSSH,
       "hmSec2CliLoginTimeoutTelnet": hmSec2CliLoginTimeoutTelnet,
       "hmSec2CliLoginAccessSSH": hmSec2CliLoginAccessSSH,
       "hmSec2CliLoginAccessTelnet": hmSec2CliLoginAccessTelnet,
       "hmSec2CliLoginSshPortNumber": hmSec2CliLoginSshPortNumber,
       "hmSec2CliLoginFingerPrintDSA": hmSec2CliLoginFingerPrintDSA,
       "hmSec2CliLoginFingerPrintRSA": hmSec2CliLoginFingerPrintRSA,
       "hmSec2CliLoginDefaultPasswordActive": hmSec2CliLoginDefaultPasswordActive,
       "hmSec2FileManagementGroup": hmSec2FileManagementGroup,
       "hmSec2FileManagementActionGroup": hmSec2FileManagementActionGroup,
       "hmSec2FMActionType": hmSec2FMActionType,
       "hmSec2FMActionItemType": hmSec2FMActionItemType,
       "hmSec2FMActionSourceType": hmSec2FMActionSourceType,
       "hmSec2FMActionSourceData": hmSec2FMActionSourceData,
       "hmSec2FMActionDestinationType": hmSec2FMActionDestinationType,
       "hmSec2FMActionDestinationData": hmSec2FMActionDestinationData,
       "hmSec2FMActionActivate": hmSec2FMActionActivate,
       "hmSec2FMActionActivateResult": hmSec2FMActionActivateResult,
       "hmSec2FMActionActivateResultText": hmSec2FMActionActivateResultText,
       "hmSec2FMActionStatus": hmSec2FMActionStatus,
       "hmSec2FMActionPercentReady": hmSec2FMActionPercentReady,
       "hmSec2FMActionResult": hmSec2FMActionResult,
       "hmSec2FMActionResultText": hmSec2FMActionResultText,
       "hmSec2FileManagementProfileGroup": hmSec2FileManagementProfileGroup,
       "hmSec2FMNvProfileTable": hmSec2FMNvProfileTable,
       "hmSec2FMNvProfileEntry": hmSec2FMNvProfileEntry,
       "hmSec2FMNvProfileIndex": hmSec2FMNvProfileIndex,
       "hmSec2FMNvProfileName": hmSec2FMNvProfileName,
       "hmSec2FMNvProfileDateTime": hmSec2FMNvProfileDateTime,
       "hmSec2FMNvProfileActive": hmSec2FMNvProfileActive,
       "hmSec2FMNvProfileAction": hmSec2FMNvProfileAction,
       "hmSec2FMAcaProfileTable": hmSec2FMAcaProfileTable,
       "hmSec2FMAcaProfileEntry": hmSec2FMAcaProfileEntry,
       "hmSec2FMAcaProfileIndex": hmSec2FMAcaProfileIndex,
       "hmSec2FMAcaProfileName": hmSec2FMAcaProfileName,
       "hmSec2FMAcaProfileDateTime": hmSec2FMAcaProfileDateTime,
       "hmSec2FMAcaProfileActive": hmSec2FMAcaProfileActive,
       "hmSec2FMAcaProfileAction": hmSec2FMAcaProfileAction,
       "hmSec2FileManagementStatusGroup": hmSec2FileManagementStatusGroup,
       "hmSec2FMNvState": hmSec2FMNvState,
       "hmSec2FMAcaState": hmSec2FMAcaState,
       "hmSec2LoggingGroup": hmSec2LoggingGroup,
       "hmSec2LoggingGeneral": hmSec2LoggingGeneral,
       "hmSec2SyslogServerIPAddr": hmSec2SyslogServerIPAddr,
       "hmSec2SyslogServerUdpPort": hmSec2SyslogServerUdpPort,
       "hmSec2LogPermFileSize": hmSec2LogPermFileSize,
       "hmSec2LogPermFilesMax": hmSec2LogPermFilesMax,
       "hmSec2LogPermFilesLock": hmSec2LogPermFilesLock,
       "hmSec2LogLevelTable": hmSec2LogLevelTable,
       "hmSec2LogLevelEntry": hmSec2LogLevelEntry,
       "hmSec2LogLevelIndex": hmSec2LogLevelIndex,
       "hmSec2LogLevelUpto": hmSec2LogLevelUpto,
       "hmSec2LogLevelName": hmSec2LogLevelName,
       "hmSec2LogLevelDesc": hmSec2LogLevelDesc,
       "hmSec2LogLevelPerm": hmSec2LogLevelPerm,
       "hmSec2UserConfigGroup": hmSec2UserConfigGroup,
       "hmSec2UserConfigTable": hmSec2UserConfigTable,
       "hmSec2UserConfigEntry": hmSec2UserConfigEntry,
       "hmSec2UserName": hmSec2UserName,
       "hmSec2UserPassword": hmSec2UserPassword,
       "hmSec2UserAccessMode": hmSec2UserAccessMode,
       "hmSec2UserSnmpAuthenticationType": hmSec2UserSnmpAuthenticationType,
       "hmSec2UserSnmpEncryptionType": hmSec2UserSnmpEncryptionType,
       "hmSec2UserAuthenticationList": hmSec2UserAuthenticationList,
       "hmSec2UserStatus": hmSec2UserStatus,
       "hmSec2UserAuthListGroup": hmSec2UserAuthListGroup,
       "hmSec2UserAuthListTable": hmSec2UserAuthListTable,
       "hmSec2UserAuthListEntry": hmSec2UserAuthListEntry,
       "hmSec2UserAuthListName": hmSec2UserAuthListName,
       "hmSec2UserAuthListPolicy1": hmSec2UserAuthListPolicy1,
       "hmSec2UserAuthListPolicy2": hmSec2UserAuthListPolicy2,
       "hmSec2UserAuthListPolicy3": hmSec2UserAuthListPolicy3,
       "hmSec2UserAuthListStatus": hmSec2UserAuthListStatus,
       "hmSec2UserAuthListDefault": hmSec2UserAuthListDefault,
       "hmSec2UserFirewallAuthListDefault": hmSec2UserFirewallAuthListDefault,
       "hmSec2UsrFwUserGroup": hmSec2UsrFwUserGroup,
       "hmSec2UsrFwUserGroupAuth": hmSec2UsrFwUserGroupAuth,
       "hmSec2UsrFwUserTable": hmSec2UsrFwUserTable,
       "hmSec2UsrFwUserEntry": hmSec2UsrFwUserEntry,
       "hmSec2UsrFwUserName": hmSec2UsrFwUserName,
       "hmSec2UsrFwUserPassword": hmSec2UsrFwUserPassword,
       "hmSec2UsrFwUserAuthList": hmSec2UsrFwUserAuthList,
       "hmSec2UsrFwUserLoginStatus": hmSec2UsrFwUserLoginStatus,
       "hmSec2UsrFwUserLoginAddr": hmSec2UsrFwUserLoginAddr,
       "hmSec2UsrFwUserStatus": hmSec2UsrFwUserStatus,
       "hmSec2Security": hmSec2Security,
       "hmSec2Radius": hmSec2Radius,
       "hmSec2RadiusClient": hmSec2RadiusClient,
       "hmSec2RadiusMaxRetries": hmSec2RadiusMaxRetries,
       "hmSec2RadiusTimeout": hmSec2RadiusTimeout,
       "hmSec2RadiusAuthServerTable": hmSec2RadiusAuthServerTable,
       "hmSec2RadiusAuthServerEntry": hmSec2RadiusAuthServerEntry,
       "hmSec2RadiusAuthServerIndex": hmSec2RadiusAuthServerIndex,
       "hmSec2RadiusAuthServerAddress": hmSec2RadiusAuthServerAddress,
       "hmSec2RadiusAuthServerPort": hmSec2RadiusAuthServerPort,
       "hmSec2RadiusAuthServerSecret": hmSec2RadiusAuthServerSecret,
       "hmSec2RadiusAuthServerStatus": hmSec2RadiusAuthServerStatus,
       "hmSec2Firewall": hmSec2Firewall,
       "hmSec2FirewallDenialOfServiceGroup": hmSec2FirewallDenialOfServiceGroup,
       "hmSec2FirewallDenialOfServiceVars": hmSec2FirewallDenialOfServiceVars,
       "hmSec2FwDosInSynLimit": hmSec2FwDosInSynLimit,
       "hmSec2FwDosOutSynLimit": hmSec2FwDosOutSynLimit,
       "hmSec2FwDosInPingLimit": hmSec2FwDosInPingLimit,
       "hmSec2FwDosOutPingLimit": hmSec2FwDosOutPingLimit,
       "hmSec2FwDosInArpLimit": hmSec2FwDosInArpLimit,
       "hmSec2FwDosOutArpLimit": hmSec2FwDosOutArpLimit,
       "hmSec2FwDosInSynLimitLog": hmSec2FwDosInSynLimitLog,
       "hmSec2FwDosOutSynLimitLog": hmSec2FwDosOutSynLimitLog,
       "hmSec2FwDosInPingLimitLog": hmSec2FwDosInPingLimitLog,
       "hmSec2FwDosOutPingLimitLog": hmSec2FwDosOutPingLimitLog,
       "hmSec2FwDosInArpLimitLog": hmSec2FwDosInArpLimitLog,
       "hmSec2FwDosOutArpLimitLog": hmSec2FwDosOutArpLimitLog,
       "hmSec2FirewallL2PacketFilterGroup": hmSec2FirewallL2PacketFilterGroup,
       "hmSec2FirewallL2PfIncomingGroup": hmSec2FirewallL2PfIncomingGroup,
       "hmSec2FwL2PfInTable": hmSec2FwL2PfInTable,
       "hmSec2FwL2PfInEntry": hmSec2FwL2PfInEntry,
       "hmSec2FwL2PfInIndex": hmSec2FwL2PfInIndex,
       "hmSec2FwL2PfInSrcAddr": hmSec2FwL2PfInSrcAddr,
       "hmSec2FwL2PfInDstAddr": hmSec2FwL2PfInDstAddr,
       "hmSec2FwL2PfInProto": hmSec2FwL2PfInProto,
       "hmSec2FwL2PfInAction": hmSec2FwL2PfInAction,
       "hmSec2FwL2PfInLog": hmSec2FwL2PfInLog,
       "hmSec2FwL2PfInDesc": hmSec2FwL2PfInDesc,
       "hmSec2FwL2PfInErrorText": hmSec2FwL2PfInErrorText,
       "hmSec2FwL2PfInRowStatus": hmSec2FwL2PfInRowStatus,
       "hmSec2FirewallL2PfOutgoingGroup": hmSec2FirewallL2PfOutgoingGroup,
       "hmSec2FwL2PfOutTable": hmSec2FwL2PfOutTable,
       "hmSec2FwL2PfOutEntry": hmSec2FwL2PfOutEntry,
       "hmSec2FwL2PfOutIndex": hmSec2FwL2PfOutIndex,
       "hmSec2FwL2PfOutSrcAddr": hmSec2FwL2PfOutSrcAddr,
       "hmSec2FwL2PfOutDstAddr": hmSec2FwL2PfOutDstAddr,
       "hmSec2FwL2PfOutProto": hmSec2FwL2PfOutProto,
       "hmSec2FwL2PfOutAction": hmSec2FwL2PfOutAction,
       "hmSec2FwL2PfOutLog": hmSec2FwL2PfOutLog,
       "hmSec2FwL2PfOutDesc": hmSec2FwL2PfOutDesc,
       "hmSec2FwL2PfOutErrorText": hmSec2FwL2PfOutErrorText,
       "hmSec2FwL2PfOutRowStatus": hmSec2FwL2PfOutRowStatus,
       "hmSec2FirewallL3PacketFilterGroup": hmSec2FirewallL3PacketFilterGroup,
       "hmSec2FirewallL3PfIncomingGroup": hmSec2FirewallL3PfIncomingGroup,
       "hmSec2FwL3PfInTable": hmSec2FwL3PfInTable,
       "hmSec2FwL3PfInEntry": hmSec2FwL3PfInEntry,
       "hmSec2FwL3PfInIndex": hmSec2FwL3PfInIndex,
       "hmSec2FwL3PfInSrcNet": hmSec2FwL3PfInSrcNet,
       "hmSec2FwL3PfInSrcPort": hmSec2FwL3PfInSrcPort,
       "hmSec2FwL3PfInDstNet": hmSec2FwL3PfInDstNet,
       "hmSec2FwL3PfInDstPort": hmSec2FwL3PfInDstPort,
       "hmSec2FwL3PfInProto": hmSec2FwL3PfInProto,
       "hmSec2FwL3PfInAction": hmSec2FwL3PfInAction,
       "hmSec2FwL3PfInLog": hmSec2FwL3PfInLog,
       "hmSec2FwL3PfInDesc": hmSec2FwL3PfInDesc,
       "hmSec2FwL3PfInErrorText": hmSec2FwL3PfInErrorText,
       "hmSec2FwL3PfInRowStatus": hmSec2FwL3PfInRowStatus,
       "hmSec2FwL3PfInLogNonMatching": hmSec2FwL3PfInLogNonMatching,
       "hmSec2FirewallL3PfOutgoingGroup": hmSec2FirewallL3PfOutgoingGroup,
       "hmSec2FwL3PfOutTable": hmSec2FwL3PfOutTable,
       "hmSec2FwL3PfOutEntry": hmSec2FwL3PfOutEntry,
       "hmSec2FwL3PfOutIndex": hmSec2FwL3PfOutIndex,
       "hmSec2FwL3PfOutSrcNet": hmSec2FwL3PfOutSrcNet,
       "hmSec2FwL3PfOutSrcPort": hmSec2FwL3PfOutSrcPort,
       "hmSec2FwL3PfOutDstNet": hmSec2FwL3PfOutDstNet,
       "hmSec2FwL3PfOutDstPort": hmSec2FwL3PfOutDstPort,
       "hmSec2FwL3PfOutProto": hmSec2FwL3PfOutProto,
       "hmSec2FwL3PfOutAction": hmSec2FwL3PfOutAction,
       "hmSec2FwL3PfOutLog": hmSec2FwL3PfOutLog,
       "hmSec2FwL3PfOutDesc": hmSec2FwL3PfOutDesc,
       "hmSec2FwL3PfOutErrorText": hmSec2FwL3PfOutErrorText,
       "hmSec2FwL3PfOutRowStatus": hmSec2FwL3PfOutRowStatus,
       "hmSec2FwL3PfOutLogNonMatching": hmSec2FwL3PfOutLogNonMatching,
       "hmSec2FirewallL3TemplateGroup": hmSec2FirewallL3TemplateGroup,
       "hmSec2FwL3TplIdTable": hmSec2FwL3TplIdTable,
       "hmSec2FwL3TplIdEntry": hmSec2FwL3TplIdEntry,
       "hmSec2FwL3TplIdIndex": hmSec2FwL3TplIdIndex,
       "hmSec2FwL3TplIdName": hmSec2FwL3TplIdName,
       "hmSec2FwL3TplIdRowStatus": hmSec2FwL3TplIdRowStatus,
       "hmSec2FwL3TplNetTable": hmSec2FwL3TplNetTable,
       "hmSec2FwL3TplNetEntry": hmSec2FwL3TplNetEntry,
       "hmSec2FwL3TplNetIdIndex": hmSec2FwL3TplNetIdIndex,
       "hmSec2FwL3TplNetIndex": hmSec2FwL3TplNetIndex,
       "hmSec2FwL3TplNetAddr": hmSec2FwL3TplNetAddr,
       "hmSec2FwL3TplNetRowStatus": hmSec2FwL3TplNetRowStatus,
       "hmSec2FirewallPppFilterGroup": hmSec2FirewallPppFilterGroup,
       "hmSec2FirewallPppIncomingGroup": hmSec2FirewallPppIncomingGroup,
       "hmSec2FwPppInTable": hmSec2FwPppInTable,
       "hmSec2FwPppInEntry": hmSec2FwPppInEntry,
       "hmSec2FwPppInIndex": hmSec2FwPppInIndex,
       "hmSec2FwPppInSrcNet": hmSec2FwPppInSrcNet,
       "hmSec2FwPppInSrcPort": hmSec2FwPppInSrcPort,
       "hmSec2FwPppInDstNet": hmSec2FwPppInDstNet,
       "hmSec2FwPppInDstPort": hmSec2FwPppInDstPort,
       "hmSec2FwPppInProto": hmSec2FwPppInProto,
       "hmSec2FwPppInAction": hmSec2FwPppInAction,
       "hmSec2FwPppInLog": hmSec2FwPppInLog,
       "hmSec2FwPppInDesc": hmSec2FwPppInDesc,
       "hmSec2FwPppInErrorText": hmSec2FwPppInErrorText,
       "hmSec2FwPppInRowStatus": hmSec2FwPppInRowStatus,
       "hmSec2FwPppInLogNonMatching": hmSec2FwPppInLogNonMatching,
       "hmSec2FirewallSnmpFilterGroup": hmSec2FirewallSnmpFilterGroup,
       "hmSec2FwSnmpTable": hmSec2FwSnmpTable,
       "hmSec2FwSnmpEntry": hmSec2FwSnmpEntry,
       "hmSec2FwSnmpIndex": hmSec2FwSnmpIndex,
       "hmSec2FwSnmpInterface": hmSec2FwSnmpInterface,
       "hmSec2FwSnmpSrcNet": hmSec2FwSnmpSrcNet,
       "hmSec2FwSnmpAction": hmSec2FwSnmpAction,
       "hmSec2FwSnmpLog": hmSec2FwSnmpLog,
       "hmSec2FwSnmpDesc": hmSec2FwSnmpDesc,
       "hmSec2FwSnmpErrorText": hmSec2FwSnmpErrorText,
       "hmSec2FwSnmpRowStatus": hmSec2FwSnmpRowStatus,
       "hmSec2FirewallSshFilterGroup": hmSec2FirewallSshFilterGroup,
       "hmSec2FwSshTable": hmSec2FwSshTable,
       "hmSec2FwSshEntry": hmSec2FwSshEntry,
       "hmSec2FwSshIndex": hmSec2FwSshIndex,
       "hmSec2FwSshInterface": hmSec2FwSshInterface,
       "hmSec2FwSshSrcNet": hmSec2FwSshSrcNet,
       "hmSec2FwSshAction": hmSec2FwSshAction,
       "hmSec2FwSshLog": hmSec2FwSshLog,
       "hmSec2FwSshDesc": hmSec2FwSshDesc,
       "hmSec2FwSshErrorText": hmSec2FwSshErrorText,
       "hmSec2FwSshRowStatus": hmSec2FwSshRowStatus,
       "hmSec2FirewallHttpsFilterGroup": hmSec2FirewallHttpsFilterGroup,
       "hmSec2FwHttpsTable": hmSec2FwHttpsTable,
       "hmSec2FwHttpsEntry": hmSec2FwHttpsEntry,
       "hmSec2FwHttpsIndex": hmSec2FwHttpsIndex,
       "hmSec2FwHttpsInterface": hmSec2FwHttpsInterface,
       "hmSec2FwHttpsSrcNet": hmSec2FwHttpsSrcNet,
       "hmSec2FwHttpsAction": hmSec2FwHttpsAction,
       "hmSec2FwHttpsLog": hmSec2FwHttpsLog,
       "hmSec2FwHttpsDesc": hmSec2FwHttpsDesc,
       "hmSec2FwHttpsErrorText": hmSec2FwHttpsErrorText,
       "hmSec2FwHttpsRowStatus": hmSec2FwHttpsRowStatus,
       "hmSec2UsrFwConfigGroup": hmSec2UsrFwConfigGroup,
       "hmSec2UsrFwStatus": hmSec2UsrFwStatus,
       "hmSec2UsrFwTemplateTable": hmSec2UsrFwTemplateTable,
       "hmSec2UsrFwTemplateEntry": hmSec2UsrFwTemplateEntry,
       "hmSec2UsrFwTemplateIndex": hmSec2UsrFwTemplateIndex,
       "hmSec2UsrFwTemplateName": hmSec2UsrFwTemplateName,
       "hmSec2UsrFwTemplateTimeout": hmSec2UsrFwTemplateTimeout,
       "hmSec2UsrFwTemplateTimeoutType": hmSec2UsrFwTemplateTimeoutType,
       "hmSec2UsrFwTemplateComment": hmSec2UsrFwTemplateComment,
       "hmSec2UsrFwTemplateSrcAddr": hmSec2UsrFwTemplateSrcAddr,
       "hmSec2UsrFwTemplateStatus": hmSec2UsrFwTemplateStatus,
       "hmSec2UsrFwTemplateUserTable": hmSec2UsrFwTemplateUserTable,
       "hmSec2UsrFwTemplateUserEntry": hmSec2UsrFwTemplateUserEntry,
       "hmSec2UsrFwTemplateUserTemplateIndex": hmSec2UsrFwTemplateUserTemplateIndex,
       "hmSec2UsrFwTemplateUserName": hmSec2UsrFwTemplateUserName,
       "hmSec2UsrFwTemplateUserStatus": hmSec2UsrFwTemplateUserStatus,
       "hmSec2UsrFwTemplateRuleTable": hmSec2UsrFwTemplateRuleTable,
       "hmSec2UsrFwTemplateRuleEntry": hmSec2UsrFwTemplateRuleEntry,
       "hmSec2UsrFwTemplateRuleTemplateIndex": hmSec2UsrFwTemplateRuleTemplateIndex,
       "hmSec2UsrFwTemplateRuleIndex": hmSec2UsrFwTemplateRuleIndex,
       "hmSec2UsrFwTemplateRuleProto": hmSec2UsrFwTemplateRuleProto,
       "hmSec2UsrFwTemplateRuleSrcPort": hmSec2UsrFwTemplateRuleSrcPort,
       "hmSec2UsrFwTemplateRuleDstNet": hmSec2UsrFwTemplateRuleDstNet,
       "hmSec2UsrFwTemplateRuleDstPort": hmSec2UsrFwTemplateRuleDstPort,
       "hmSec2UsrFwTemplateRuleComment": hmSec2UsrFwTemplateRuleComment,
       "hmSec2UsrFwTemplateRuleLog": hmSec2UsrFwTemplateRuleLog,
       "hmSec2UsrFwTemplateRuleStatus": hmSec2UsrFwTemplateRuleStatus,
       "hmSec2FirewallDiagnosticsGroup": hmSec2FirewallDiagnosticsGroup,
       "hmSec2FwDiagL3Table": hmSec2FwDiagL3Table,
       "hmSec2FwDiagL3Entry": hmSec2FwDiagL3Entry,
       "hmSec2FwDiagL3Index": hmSec2FwDiagL3Index,
       "hmSec2FwDiagL3Group": hmSec2FwDiagL3Group,
       "hmSec2FwDiagL3Ref": hmSec2FwDiagL3Ref,
       "hmSec2FwDiagL3Interface": hmSec2FwDiagL3Interface,
       "hmSec2FwDiagL3SrcNet": hmSec2FwDiagL3SrcNet,
       "hmSec2FwDiagL3SrcPort": hmSec2FwDiagL3SrcPort,
       "hmSec2FwDiagL3DstNet": hmSec2FwDiagL3DstNet,
       "hmSec2FwDiagL3DstPort": hmSec2FwDiagL3DstPort,
       "hmSec2FwDiagL3Proto": hmSec2FwDiagL3Proto,
       "hmSec2FwDiagL3Action": hmSec2FwDiagL3Action,
       "hmSec2FwDiagL3Log": hmSec2FwDiagL3Log,
       "hmSec2FwDiagL3MatchCnt": hmSec2FwDiagL3MatchCnt,
       "hmSec2FwDiagL2Table": hmSec2FwDiagL2Table,
       "hmSec2FwDiagL2Entry": hmSec2FwDiagL2Entry,
       "hmSec2FwDiagL2Index": hmSec2FwDiagL2Index,
       "hmSec2FwDiagL2Group": hmSec2FwDiagL2Group,
       "hmSec2FwDiagL2Ref": hmSec2FwDiagL2Ref,
       "hmSec2FwDiagL2Interface": hmSec2FwDiagL2Interface,
       "hmSec2FwDiagL2SrcNet": hmSec2FwDiagL2SrcNet,
       "hmSec2FwDiagL2DstNet": hmSec2FwDiagL2DstNet,
       "hmSec2FwDiagL2Proto": hmSec2FwDiagL2Proto,
       "hmSec2FwDiagL2Action": hmSec2FwDiagL2Action,
       "hmSec2FwDiagL2Log": hmSec2FwDiagL2Log,
       "hmSec2FwDiagL2MatchCnt": hmSec2FwDiagL2MatchCnt,
       "hmSec2FirewallLearningModeGroup": hmSec2FirewallLearningModeGroup,
       "hmSec2FirewallLearningModeVars": hmSec2FirewallLearningModeVars,
       "hmSec2FLMAdminState": hmSec2FLMAdminState,
       "hmSec2FLMAction": hmSec2FLMAction,
       "hmSec2FLMInterfaces": hmSec2FLMInterfaces,
       "hmSec2FLMType": hmSec2FLMType,
       "hmSec2FLMAppState": hmSec2FLMAppState,
       "hmSec2FLMAppInfoEnum": hmSec2FLMAppInfoEnum,
       "hmSec2FLMAppInfoString": hmSec2FLMAppInfoString,
       "hmSec2FLML3Entries": hmSec2FLML3Entries,
       "hmSec2FLMFreeMem": hmSec2FLMFreeMem,
       "hmSec2FLMAnyRuleChange": hmSec2FLMAnyRuleChange,
       "hmSec2FwConfigGroup": hmSec2FwConfigGroup,
       "hmSec2FwStaticPacketCheck": hmSec2FwStaticPacketCheck,
       "hmSec2FwInternRemNumIPRules": hmSec2FwInternRemNumIPRules,
       "hmSec2Network": hmSec2Network,
       "hmSec2NetGeneralGroup": hmSec2NetGeneralGroup,
       "hmSec2NetworkMode": hmSec2NetworkMode,
       "hmSec2NetAction": hmSec2NetAction,
       "hmSec2NetDirectedBroadcasts": hmSec2NetDirectedBroadcasts,
       "hmSec2NetIPFragmentsAllowed": hmSec2NetIPFragmentsAllowed,
       "hmSec2NetICMPSendRedirects": hmSec2NetICMPSendRedirects,
       "hmSec2NetTransparentGroup": hmSec2NetTransparentGroup,
       "hmSec2LocalIPAddr": hmSec2LocalIPAddr,
       "hmSec2LocalPhysAddr": hmSec2LocalPhysAddr,
       "hmSec2GatewayIPAddr": hmSec2GatewayIPAddr,
       "hmSec2NetMask": hmSec2NetMask,
       "hmSec2UseVLAN": hmSec2UseVLAN,
       "hmSec2MgmtVLANID": hmSec2MgmtVLANID,
       "hmSec2NetProto": hmSec2NetProto,
       "hmSec2NetPassThroughSTP": hmSec2NetPassThroughSTP,
       "hmSec2NetPassThroughGMRP": hmSec2NetPassThroughGMRP,
       "hmSec2NetPassThroughDHCP": hmSec2NetPassThroughDHCP,
       "hmSec2NetRouterGroup": hmSec2NetRouterGroup,
       "hmSec2NetIPInterfaceTable": hmSec2NetIPInterfaceTable,
       "hmSec2NetIPInterfaceEntry": hmSec2NetIPInterfaceEntry,
       "hmSec2NetIPIfIndex": hmSec2NetIPIfIndex,
       "hmSec2NetIPIfAddr": hmSec2NetIPIfAddr,
       "hmSec2NetIPIfMask": hmSec2NetIPIfMask,
       "hmSec2NetIPIfUseVLAN": hmSec2NetIPIfUseVLAN,
       "hmSec2NetIPIfVLANID": hmSec2NetIPIfVLANID,
       "hmSec2NetIPIfNetProto": hmSec2NetIPIfNetProto,
       "hmSec2NetIPAliasesTable": hmSec2NetIPAliasesTable,
       "hmSec2NetIPAliasesEntry": hmSec2NetIPAliasesEntry,
       "hmSec2NetIPAliasIfIndex": hmSec2NetIPAliasIfIndex,
       "hmSec2NetIPAliasAddr": hmSec2NetIPAliasAddr,
       "hmSec2NetIPAliasMask": hmSec2NetIPAliasMask,
       "hmSec2NetIPAliasUseVLAN": hmSec2NetIPAliasUseVLAN,
       "hmSec2NetIPAliasVLANID": hmSec2NetIPAliasVLANID,
       "hmSec2NetIPAliasRowStatus": hmSec2NetIPAliasRowStatus,
       "hmSec2NetRouterExternalGroup": hmSec2NetRouterExternalGroup,
       "hmSec2NetRtrExternalGateway": hmSec2NetRtrExternalGateway,
       "hmSec2NetIPRouteTable": hmSec2NetIPRouteTable,
       "hmSec2NetIPRouteEntry": hmSec2NetIPRouteEntry,
       "hmSec2NetIPRouteIfIndex": hmSec2NetIPRouteIfIndex,
       "hmSec2NetIPRouteAddr": hmSec2NetIPRouteAddr,
       "hmSec2NetIPRouteMask": hmSec2NetIPRouteMask,
       "hmSec2NetIPRouteGateway": hmSec2NetIPRouteGateway,
       "hmSec2NetIPRouteRowStatus": hmSec2NetIPRouteRowStatus,
       "hmSec2NetPPPoEGroup": hmSec2NetPPPoEGroup,
       "hmSec2PPPoEUsername": hmSec2PPPoEUsername,
       "hmSec2PPPoEPassword": hmSec2PPPoEPassword,
       "hmSec2PPPoEMTU": hmSec2PPPoEMTU,
       "hmSec2PPPoEIfAddr": hmSec2PPPoEIfAddr,
       "hmSec2PPPoEIfMask": hmSec2PPPoEIfMask,
       "hmSec2PPPoEGateway": hmSec2PPPoEGateway,
       "hmSec2PPPoEStatus": hmSec2PPPoEStatus,
       "hmSec2PPPoEDisconAdminState": hmSec2PPPoEDisconAdminState,
       "hmSec2PPPoEDisconHour": hmSec2PPPoEDisconHour,
       "hmSec2NetPPPGroup": hmSec2NetPPPGroup,
       "hmSec2PPPUsername": hmSec2PPPUsername,
       "hmSec2PPPPassword": hmSec2PPPPassword,
       "hmSec2PPPLocalIPAddress": hmSec2PPPLocalIPAddress,
       "hmSec2PPPRemoteIPAddress": hmSec2PPPRemoteIPAddress,
       "hmSec2PPPModemAdminState": hmSec2PPPModemAdminState,
       "hmSec2PPPModemBaudRate": hmSec2PPPModemBaudRate,
       "hmSec2PPPMTU": hmSec2PPPMTU,
       "hmSec2PPPStatus": hmSec2PPPStatus,
       "hmSec2PPPModemFlowControl": hmSec2PPPModemFlowControl,
       "hmSec2NetDNSClientGroup": hmSec2NetDNSClientGroup,
       "hmSec2DNSClientServer1": hmSec2DNSClientServer1,
       "hmSec2DNSClientServer2": hmSec2DNSClientServer2,
       "hmSec2DNSClientServer3": hmSec2DNSClientServer3,
       "hmSec2DNSClientServer4": hmSec2DNSClientServer4,
       "hmSec2DNSClientConfigSource": hmSec2DNSClientConfigSource,
       "hmSec2NetDynDNSGroup": hmSec2NetDynDNSGroup,
       "hmSec2DynDNSProvider": hmSec2DynDNSProvider,
       "hmSec2DynDNSRegister": hmSec2DynDNSRegister,
       "hmSec2DynDNSServer": hmSec2DynDNSServer,
       "hmSec2DynDNSLogin": hmSec2DynDNSLogin,
       "hmSec2DynDNSPassword": hmSec2DynDNSPassword,
       "hmSec2DynDNSHostname": hmSec2DynDNSHostname,
       "hmSec2DynDNSRefresh": hmSec2DynDNSRefresh,
       "hmSec2DynDNSStatus": hmSec2DynDNSStatus,
       "hmSec2DynDNSCheckIPServer": hmSec2DynDNSCheckIPServer,
       "hmSec2NetPingGroup": hmSec2NetPingGroup,
       "hmSec2NetPingSourceAddr": hmSec2NetPingSourceAddr,
       "hmSec2NetPingDestAddr": hmSec2NetPingDestAddr,
       "hmSec2NetPingAction": hmSec2NetPingAction,
       "hmSec2NetPingActionStatus": hmSec2NetPingActionStatus,
       "hmSec2NetPingResult": hmSec2NetPingResult,
       "hmSec2NetPingResultText": hmSec2NetPingResultText,
       "hmSec2Vpn": hmSec2Vpn,
       "hmSec2VpnGroup": hmSec2VpnGroup,
       "hmSec2VpnGeneralGroup": hmSec2VpnGeneralGroup,
       "hmSec2VpnRemoteCtlPwd": hmSec2VpnRemoteCtlPwd,
       "hmSec2VpnLEDIndication": hmSec2VpnLEDIndication,
       "hmSec2VpnModeConfigPool": hmSec2VpnModeConfigPool,
       "hmSec2VpnConnGroup": hmSec2VpnConnGroup,
       "hmSec2VpnConnMax": hmSec2VpnConnMax,
       "hmSec2VpnConnNext": hmSec2VpnConnNext,
       "hmSec2VpnConnTable": hmSec2VpnConnTable,
       "hmSec2VpnConnEntry": hmSec2VpnConnEntry,
       "hmSec2VpnConnIndex": hmSec2VpnConnIndex,
       "hmSec2VpnConnIkeVersion": hmSec2VpnConnIkeVersion,
       "hmSec2VpnConnIkeStartup": hmSec2VpnConnIkeStartup,
       "hmSec2VpnConnIkeCompat": hmSec2VpnConnIkeCompat,
       "hmSec2VpnConnIkeLifetime": hmSec2VpnConnIkeLifetime,
       "hmSec2VpnConnIkeDpdTimeout": hmSec2VpnConnIkeDpdTimeout,
       "hmSec2VpnConnIkeLocalAddr": hmSec2VpnConnIkeLocalAddr,
       "hmSec2VpnConnIkeRemoteAddr": hmSec2VpnConnIkeRemoteAddr,
       "hmSec2VpnConnIkeAuthType": hmSec2VpnConnIkeAuthType,
       "hmSec2VpnConnIkeAuthMode": hmSec2VpnConnIkeAuthMode,
       "hmSec2VpnConnIkeAuthCertCA": hmSec2VpnConnIkeAuthCertCA,
       "hmSec2VpnConnIkeAuthCertRemote": hmSec2VpnConnIkeAuthCertRemote,
       "hmSec2VpnConnIkeAuthCertLocal": hmSec2VpnConnIkeAuthCertLocal,
       "hmSec2VpnConnIkeAuthPrivKey": hmSec2VpnConnIkeAuthPrivKey,
       "hmSec2VpnConnIkeAuthPasswd": hmSec2VpnConnIkeAuthPasswd,
       "hmSec2VpnConnIkeAuthPsk": hmSec2VpnConnIkeAuthPsk,
       "hmSec2VpnConnIkeAuthLocId": hmSec2VpnConnIkeAuthLocId,
       "hmSec2VpnConnIkeAuthLocType": hmSec2VpnConnIkeAuthLocType,
       "hmSec2VpnConnIkeAuthRemId": hmSec2VpnConnIkeAuthRemId,
       "hmSec2VpnConnIkeAuthRemType": hmSec2VpnConnIkeAuthRemType,
       "hmSec2VpnConnIkeAlgDh": hmSec2VpnConnIkeAlgDh,
       "hmSec2VpnConnIkeAlgHash": hmSec2VpnConnIkeAlgHash,
       "hmSec2VpnConnIkeAlgMac": hmSec2VpnConnIkeAlgMac,
       "hmSec2VpnConnIkeAlgEncr": hmSec2VpnConnIkeAlgEncr,
       "hmSec2VpnConnIpsecMode": hmSec2VpnConnIpsecMode,
       "hmSec2VpnConnIpsecNatTraversal": hmSec2VpnConnIpsecNatTraversal,
       "hmSec2VpnConnIpsecLifetime": hmSec2VpnConnIpsecLifetime,
       "hmSec2VpnConnIpsecAlgDh": hmSec2VpnConnIpsecAlgDh,
       "hmSec2VpnConnIpsecAlgMac": hmSec2VpnConnIpsecAlgMac,
       "hmSec2VpnConnIpsecAlgEncr": hmSec2VpnConnIpsecAlgEncr,
       "hmSec2VpnConnOperStatus": hmSec2VpnConnOperStatus,
       "hmSec2VpnConnDesc": hmSec2VpnConnDesc,
       "hmSec2VpnConnRowStatus": hmSec2VpnConnRowStatus,
       "hmSec2VpnConnServiceMode": hmSec2VpnConnServiceMode,
       "hmSec2VpnTrafficSelGroup": hmSec2VpnTrafficSelGroup,
       "hmSec2VpnTrafficSelTable": hmSec2VpnTrafficSelTable,
       "hmSec2VpnTrafficSelEntry": hmSec2VpnTrafficSelEntry,
       "hmSec2VpnTrafficSelIndex": hmSec2VpnTrafficSelIndex,
       "hmSec2VpnTrafficSelSrcAddr": hmSec2VpnTrafficSelSrcAddr,
       "hmSec2VpnTrafficSelDstAddr": hmSec2VpnTrafficSelDstAddr,
       "hmSec2VpnTrafficSelSrcPort": hmSec2VpnTrafficSelSrcPort,
       "hmSec2VpnTrafficSelDstPort": hmSec2VpnTrafficSelDstPort,
       "hmSec2VpnTrafficSelProto": hmSec2VpnTrafficSelProto,
       "hmSec2VpnTrafficSelPolicy": hmSec2VpnTrafficSelPolicy,
       "hmSec2VpnTrafficSelDesc": hmSec2VpnTrafficSelDesc,
       "hmSec2VpnTrafficSelRowStatus": hmSec2VpnTrafficSelRowStatus,
       "hmSec2VpnTrafficSelSrcMapping": hmSec2VpnTrafficSelSrcMapping,
       "hmSec2VpnTrafficSelDstMapping": hmSec2VpnTrafficSelDstMapping,
       "hmSec2VpnCertificateGroup": hmSec2VpnCertificateGroup,
       "hmSec2VpnCertificateValidation": hmSec2VpnCertificateValidation,
       "hmSec2Redundancy": hmSec2Redundancy,
       "hmSec2RedRouterGroup": hmSec2RedRouterGroup,
       "hmSec2RedAdminState": hmSec2RedAdminState,
       "hmSec2RedStartupState": hmSec2RedStartupState,
       "hmSec2RedPriority": hmSec2RedPriority,
       "hmSec2RedOperState": hmSec2RedOperState,
       "hmSec2RedOperInfo": hmSec2RedOperInfo,
       "hmSec2RedIfaceTable": hmSec2RedIfaceTable,
       "hmSec2RedIfaceEntry": hmSec2RedIfaceEntry,
       "hmSec2RedIfIndex": hmSec2RedIfIndex,
       "hmSec2RedVirtualAddr": hmSec2RedVirtualAddr,
       "hmSec2RedVRID": hmSec2RedVRID,
       "hmSec2RedRemoteIPAddr": hmSec2RedRemoteIPAddr,
       "hmSec2RedSwitchCounter": hmSec2RedSwitchCounter,
       "hmSec2HostCheckGroup": hmSec2HostCheckGroup,
       "hmSec2HostCheckAdminState": hmSec2HostCheckAdminState,
       "hmSec2HostCheckNumAddrs": hmSec2HostCheckNumAddrs,
       "hmSec2HostCheckOperState": hmSec2HostCheckOperState,
       "hmSec2HostCheckOperInfo": hmSec2HostCheckOperInfo,
       "hmSec2HostCheckTable": hmSec2HostCheckTable,
       "hmSec2HostCheckEntry": hmSec2HostCheckEntry,
       "hmSec2HostCheckIfIndex": hmSec2HostCheckIfIndex,
       "hmSec2HostCheckTableIndex": hmSec2HostCheckTableIndex,
       "hmSec2HostCheckAddr": hmSec2HostCheckAddr,
       "hmSec2HostCheckRowStatus": hmSec2HostCheckRowStatus,
       "hmSec2RedLayer2Group": hmSec2RedLayer2Group,
       "hmSec2RedLayer2AdminState": hmSec2RedLayer2AdminState,
       "hmSec2RedLayer2IfIndex": hmSec2RedLayer2IfIndex,
       "hmSec2RedLayer2Packetcounter": hmSec2RedLayer2Packetcounter,
       "hmSec2RedTransparentGroup": hmSec2RedTransparentGroup,
       "hmSec2RedTPRemoteIPAddr": hmSec2RedTPRemoteIPAddr,
       "hmSec2RedTPOperState": hmSec2RedTPOperState,
       "hmSec2RedTPOperInfo": hmSec2RedTPOperInfo,
       "hmSec2RedTPCommunicationState": hmSec2RedTPCommunicationState,
       "hmSec2Nat": hmSec2Nat,
       "hmSec2NatGeneralGroup": hmSec2NatGeneralGroup,
       "hmSec2NatMappingMax": hmSec2NatMappingMax,
       "hmSec2NatTimeoutEstablished": hmSec2NatTimeoutEstablished,
       "hmSec2NatAllowOutputSameIface": hmSec2NatAllowOutputSameIface,
       "hmSec2NatRulesGroup": hmSec2NatRulesGroup,
       "hmSec2NatTable": hmSec2NatTable,
       "hmSec2NatEntry": hmSec2NatEntry,
       "hmSec2NatIndex": hmSec2NatIndex,
       "hmSec2NatSrcNet": hmSec2NatSrcNet,
       "hmSec2NatAlg": hmSec2NatAlg,
       "hmSec2NatDesc": hmSec2NatDesc,
       "hmSec2NatErrorText": hmSec2NatErrorText,
       "hmSec2NatRowStatus": hmSec2NatRowStatus,
       "hmSec2Nat1To1Table": hmSec2Nat1To1Table,
       "hmSec2Nat1To1Entry": hmSec2Nat1To1Entry,
       "hmSec2Nat1To1Index": hmSec2Nat1To1Index,
       "hmSec2Nat1To1SrcNet": hmSec2Nat1To1SrcNet,
       "hmSec2Nat1To1DstNet": hmSec2Nat1To1DstNet,
       "hmSec2Nat1To1NetMask": hmSec2Nat1To1NetMask,
       "hmSec2Nat1To1Desc": hmSec2Nat1To1Desc,
       "hmSec2Nat1To1ErrorText": hmSec2Nat1To1ErrorText,
       "hmSec2Nat1To1RowStatus": hmSec2Nat1To1RowStatus,
       "hmSec2Nat1To1Alg": hmSec2Nat1To1Alg,
       "hmSec2Nat1To1DoOutput": hmSec2Nat1To1DoOutput,
       "hmSec2Nat1To1InvertDirection": hmSec2Nat1To1InvertDirection,
       "hmSec2NatPortFwdTable": hmSec2NatPortFwdTable,
       "hmSec2NatPortFwdEntry": hmSec2NatPortFwdEntry,
       "hmSec2NatPortFwdIndex": hmSec2NatPortFwdIndex,
       "hmSec2NatPortFwdSrcNet": hmSec2NatPortFwdSrcNet,
       "hmSec2NatPortFwdSrcPort": hmSec2NatPortFwdSrcPort,
       "hmSec2NatPortFwdDstNet": hmSec2NatPortFwdDstNet,
       "hmSec2NatPortFwdDstPort": hmSec2NatPortFwdDstPort,
       "hmSec2NatPortFwdFwdNet": hmSec2NatPortFwdFwdNet,
       "hmSec2NatPortFwdFwdPort": hmSec2NatPortFwdFwdPort,
       "hmSec2NatPortFwdProto": hmSec2NatPortFwdProto,
       "hmSec2NatPortFwdLog": hmSec2NatPortFwdLog,
       "hmSec2NatPortFwdDesc": hmSec2NatPortFwdDesc,
       "hmSec2NatPortFwdErrorText": hmSec2NatPortFwdErrorText,
       "hmSec2NatPortFwdRowStatus": hmSec2NatPortFwdRowStatus,
       "hmSec2Info": hmSec2Info,
       "hmSec2DHCPLastAccessMAC": hmSec2DHCPLastAccessMAC,
       "hmSec2MiscTrapText": hmSec2MiscTrapText}
)
