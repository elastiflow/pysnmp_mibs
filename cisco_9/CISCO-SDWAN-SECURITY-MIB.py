# SNMP MIB module (CISCO-SDWAN-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SDWAN-SECURITY-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:58 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSdwanSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006)
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityMIB.setRevisions(
        ("2021-09-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class NotificationSeverity(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )



class PersonalityEnumOper(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )



class ControlProtocolEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 0),
          ("tls", 1))
    )



class ColorEnum(TextualConvention, Integer32):
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )



class OperState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1))
    )



class CertificateTypeEnum(TextualConvention, Integer32):
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
        *(("web-server", 1),
          ("enterprise", 2),
          ("vmanage", 3))
    )



class SessionState(TextualConvention, Integer32):
    status = "current"
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
        *(("down", 0),
          ("connect", 1),
          ("handshake", 2),
          ("trying", 3),
          ("challenge", 4),
          ("challenge-resp", 5),
          ("challenge-ack", 6),
          ("up", 7),
          ("tear-down", 8))
    )



class ConnFlagEnum(TextualConvention, Integer32):
    status = "current"
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
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82)
        )
    )
    namedValues = NamedValues(
        *(("noerr", 0),
          ("acsrrej", 1),
          ("stentry", 2),
          ("hsfail", 3),
          ("dcertfl", 4),
          ("nlcert", 5),
          ("lisfd", 6),
          ("snocheck", 7),
          ("ip-tos", 8),
          ("tmralc", 9),
          ("dconfail", 10),
          ("wrkrto", 11),
          ("vs-tmo", 12),
          ("vb-tmo", 13),
          ("vm-tmo", 14),
          ("vp-tmo", 15),
          ("distloc", 16),
          ("rmgspr", 17),
          ("prchal", 18),
          ("sysprch", 19),
          ("reclen0", 20),
          ("txchtobd", 21),
          ("rdsigfbd", 22),
          ("sslnfail", 23),
          ("dhstmo", 24),
          ("novs", 25),
          ("noactvb", 26),
          ("orptmo", 27),
          ("devalc", 28),
          ("tunalc", 29),
          ("crtrejser", 30),
          ("vbdest", 31),
          ("crtrev", 32),
          ("rxtrdwn", 33),
          ("xtvstrdn", 34),
          ("noslprcrt", 35),
          ("dupser", 36),
          ("serntpres", 37),
          ("crtverfl", 38),
          ("bidntpr", 39),
          ("bidntvrfd", 40),
          ("bdsgverfl", 41),
          ("memalcfl", 42),
          ("unmsgbdrg", 43),
          ("vscrtrev", 44),
          ("vecrtrev", 45),
          ("unauthel", 46),
          ("discvbd", 47),
          ("ctorgnmmis", 48),
          ("noztpen", 49),
          ("novmcfg", 50),
          ("chverfail", 51),
          ("dupclhelo", 52),
          ("certexprd", 53),
          ("sysipchng", 54),
          ("xtvmtrdn", 55),
          ("mgrtblckd", 56),
          ("noncgn", 57),
          ("xtmos", 58),
          ("iptmiss", 59),
          ("operdown", 60),
          ("ntprvmint", 61),
          ("stnmodetd", 62),
          ("lrntpeer", 63),
          ("cgnidchngd", 64),
          ("dupsysipdel", 65),
          ("bidsig", 66),
          ("idreqdecfail", 67),
          ("veyidbndfail", 68),
          ("credfail", 69),
          ("reccablobfail", 70),
          ("embargofail", 71),
          ("newvbnovmng", 72),
          ("hwcertren", 73),
          ("hwcertrev", 74),
          ("inztpentry", 75),
          ("tenantrm", 76),
          ("regidmis", 77),
          ("regidchg", 78),
          ("notenprst", 79),
          ("crtvercrlfl", 80),
          ("restrqfail", 81),
          ("psev6disc", 82))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSdwanSecurityMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSdwanSecurityMIBNotifs = _CiscoSdwanSecurityMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0)
)
_CiscoSdwanSecurityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanSecurityMIBObjects = _CiscoSdwanSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1)
)
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2)
)
_ControlConnectionsInfo_ObjectIdentity = ObjectIdentity
controlConnectionsInfo = _ControlConnectionsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 1)
)
_ControlConnectionsInfoRate_Type = String
_ControlConnectionsInfoRate_Object = MibScalar
controlConnectionsInfoRate = _ControlConnectionsInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 1, 1),
    _ControlConnectionsInfoRate_Type()
)
controlConnectionsInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsInfoRate.setStatus("current")
_ControlConnectionsTable_Object = MibTable
controlConnectionsTable = _ControlConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2)
)
if mibBuilder.loadTexts:
    controlConnectionsTable.setStatus("current")
_ControlConnectionsEntry_Object = MibTableRow
controlConnectionsEntry = _ControlConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1)
)
controlConnectionsEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlConnectionsInstance"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlConnectionsPeerType"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlConnectionsSiteId"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlConnectionsDomainId"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlConnectionsLocalPrivateIp"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlConnectionsLocalPrivatePort"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlConnectionsPublicIp"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlConnectionsPublicPort"),
)
if mibBuilder.loadTexts:
    controlConnectionsEntry.setStatus("current")
_ControlConnectionsInstance_Type = Unsigned32
_ControlConnectionsInstance_Object = MibTableColumn
controlConnectionsInstance = _ControlConnectionsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 1),
    _ControlConnectionsInstance_Type()
)
controlConnectionsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsInstance.setStatus("current")
_ControlConnectionsPeerType_Type = PersonalityEnumOper
_ControlConnectionsPeerType_Object = MibTableColumn
controlConnectionsPeerType = _ControlConnectionsPeerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 2),
    _ControlConnectionsPeerType_Type()
)
controlConnectionsPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsPeerType.setStatus("current")
_ControlConnectionsSiteId_Type = Unsigned32
_ControlConnectionsSiteId_Object = MibTableColumn
controlConnectionsSiteId = _ControlConnectionsSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 3),
    _ControlConnectionsSiteId_Type()
)
controlConnectionsSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsSiteId.setStatus("current")
_ControlConnectionsDomainId_Type = Unsigned32
_ControlConnectionsDomainId_Object = MibTableColumn
controlConnectionsDomainId = _ControlConnectionsDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 4),
    _ControlConnectionsDomainId_Type()
)
controlConnectionsDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsDomainId.setStatus("current")
_ControlConnectionsLocalPrivateIp_Type = InetAddressIP
_ControlConnectionsLocalPrivateIp_Object = MibTableColumn
controlConnectionsLocalPrivateIp = _ControlConnectionsLocalPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 5),
    _ControlConnectionsLocalPrivateIp_Type()
)
controlConnectionsLocalPrivateIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsLocalPrivateIp.setStatus("current")
_ControlConnectionsLocalPrivatePort_Type = Unsigned32
_ControlConnectionsLocalPrivatePort_Object = MibTableColumn
controlConnectionsLocalPrivatePort = _ControlConnectionsLocalPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 6),
    _ControlConnectionsLocalPrivatePort_Type()
)
controlConnectionsLocalPrivatePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsLocalPrivatePort.setStatus("current")
_ControlConnectionsPublicIp_Type = InetAddressIP
_ControlConnectionsPublicIp_Object = MibTableColumn
controlConnectionsPublicIp = _ControlConnectionsPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 7),
    _ControlConnectionsPublicIp_Type()
)
controlConnectionsPublicIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsPublicIp.setStatus("current")
_ControlConnectionsPublicPort_Type = Unsigned32
_ControlConnectionsPublicPort_Object = MibTableColumn
controlConnectionsPublicPort = _ControlConnectionsPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 8),
    _ControlConnectionsPublicPort_Type()
)
controlConnectionsPublicPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsPublicPort.setStatus("current")
_ControlConnectionsSystemIp_Type = InetAddressIP
_ControlConnectionsSystemIp_Object = MibTableColumn
controlConnectionsSystemIp = _ControlConnectionsSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 9),
    _ControlConnectionsSystemIp_Type()
)
controlConnectionsSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsSystemIp.setStatus("current")


class _ControlConnectionsProtocol_Type(ControlProtocolEnum):
    """Custom type controlConnectionsProtocol based on ControlProtocolEnum"""
    defaultValue = 0


_ControlConnectionsProtocol_Type.__name__ = "ControlProtocolEnum"
_ControlConnectionsProtocol_Object = MibTableColumn
controlConnectionsProtocol = _ControlConnectionsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 10),
    _ControlConnectionsProtocol_Type()
)
controlConnectionsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsProtocol.setStatus("current")
_ControlConnectionsLocalColor_Type = ColorEnum
_ControlConnectionsLocalColor_Object = MibTableColumn
controlConnectionsLocalColor = _ControlConnectionsLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 11),
    _ControlConnectionsLocalColor_Type()
)
controlConnectionsLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsLocalColor.setStatus("current")
_ControlConnectionsRemoteColor_Type = ColorEnum
_ControlConnectionsRemoteColor_Object = MibTableColumn
controlConnectionsRemoteColor = _ControlConnectionsRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 12),
    _ControlConnectionsRemoteColor_Type()
)
controlConnectionsRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRemoteColor.setStatus("current")
_ControlConnectionsPrivateIp_Type = InetAddressIP
_ControlConnectionsPrivateIp_Object = MibTableColumn
controlConnectionsPrivateIp = _ControlConnectionsPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 13),
    _ControlConnectionsPrivateIp_Type()
)
controlConnectionsPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsPrivateIp.setStatus("current")
_ControlConnectionsPrivatePort_Type = Unsigned32
_ControlConnectionsPrivatePort_Object = MibTableColumn
controlConnectionsPrivatePort = _ControlConnectionsPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 14),
    _ControlConnectionsPrivatePort_Type()
)
controlConnectionsPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsPrivatePort.setStatus("current")
_ControlConnectionsState_Type = SessionState
_ControlConnectionsState_Object = MibTableColumn
controlConnectionsState = _ControlConnectionsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 15),
    _ControlConnectionsState_Type()
)
controlConnectionsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsState.setStatus("current")
_ControlConnectionsLocalEnum_Type = ConnFlagEnum
_ControlConnectionsLocalEnum_Object = MibTableColumn
controlConnectionsLocalEnum = _ControlConnectionsLocalEnum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 16),
    _ControlConnectionsLocalEnum_Type()
)
controlConnectionsLocalEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsLocalEnum.setStatus("current")
_ControlConnectionsRemoteEnum_Type = ConnFlagEnum
_ControlConnectionsRemoteEnum_Object = MibTableColumn
controlConnectionsRemoteEnum = _ControlConnectionsRemoteEnum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 17),
    _ControlConnectionsRemoteEnum_Type()
)
controlConnectionsRemoteEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRemoteEnum.setStatus("current")
_ControlConnectionsLocalStateInfo_Type = String
_ControlConnectionsLocalStateInfo_Object = MibTableColumn
controlConnectionsLocalStateInfo = _ControlConnectionsLocalStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 18),
    _ControlConnectionsLocalStateInfo_Type()
)
controlConnectionsLocalStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsLocalStateInfo.setStatus("current")
_ControlConnectionsRemoteStateInfo_Type = String
_ControlConnectionsRemoteStateInfo_Object = MibTableColumn
controlConnectionsRemoteStateInfo = _ControlConnectionsRemoteStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 19),
    _ControlConnectionsRemoteStateInfo_Type()
)
controlConnectionsRemoteStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRemoteStateInfo.setStatus("current")
_ControlConnectionsUptime_Type = String
_ControlConnectionsUptime_Object = MibTableColumn
controlConnectionsUptime = _ControlConnectionsUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 20),
    _ControlConnectionsUptime_Type()
)
controlConnectionsUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsUptime.setStatus("current")
_ControlConnectionsTxHello_Type = Unsigned32
_ControlConnectionsTxHello_Object = MibTableColumn
controlConnectionsTxHello = _ControlConnectionsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 21),
    _ControlConnectionsTxHello_Type()
)
controlConnectionsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxHello.setStatus("current")
_ControlConnectionsTxConnects_Type = Unsigned32
_ControlConnectionsTxConnects_Object = MibTableColumn
controlConnectionsTxConnects = _ControlConnectionsTxConnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 22),
    _ControlConnectionsTxConnects_Type()
)
controlConnectionsTxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxConnects.setStatus("current")
_ControlConnectionsTxRegisters_Type = Unsigned32
_ControlConnectionsTxRegisters_Object = MibTableColumn
controlConnectionsTxRegisters = _ControlConnectionsTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 23),
    _ControlConnectionsTxRegisters_Type()
)
controlConnectionsTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxRegisters.setStatus("current")
_ControlConnectionsTxRegisterReplies_Type = Unsigned32
_ControlConnectionsTxRegisterReplies_Object = MibTableColumn
controlConnectionsTxRegisterReplies = _ControlConnectionsTxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 24),
    _ControlConnectionsTxRegisterReplies_Type()
)
controlConnectionsTxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxRegisterReplies.setStatus("current")
_ControlConnectionsTxChallenge_Type = Unsigned32
_ControlConnectionsTxChallenge_Object = MibTableColumn
controlConnectionsTxChallenge = _ControlConnectionsTxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 25),
    _ControlConnectionsTxChallenge_Type()
)
controlConnectionsTxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxChallenge.setStatus("current")
_ControlConnectionsTxChallengeResp_Type = Unsigned32
_ControlConnectionsTxChallengeResp_Object = MibTableColumn
controlConnectionsTxChallengeResp = _ControlConnectionsTxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 26),
    _ControlConnectionsTxChallengeResp_Type()
)
controlConnectionsTxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxChallengeResp.setStatus("current")
_ControlConnectionsTxChallengeAck_Type = Unsigned32
_ControlConnectionsTxChallengeAck_Object = MibTableColumn
controlConnectionsTxChallengeAck = _ControlConnectionsTxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 27),
    _ControlConnectionsTxChallengeAck_Type()
)
controlConnectionsTxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxChallengeAck.setStatus("current")
_ControlConnectionsTxTeardown_Type = Unsigned32
_ControlConnectionsTxTeardown_Object = MibTableColumn
controlConnectionsTxTeardown = _ControlConnectionsTxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 28),
    _ControlConnectionsTxTeardown_Type()
)
controlConnectionsTxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxTeardown.setStatus("current")
_ControlConnectionsTxTeardownAll_Type = Unsigned32
_ControlConnectionsTxTeardownAll_Object = MibTableColumn
controlConnectionsTxTeardownAll = _ControlConnectionsTxTeardownAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 29),
    _ControlConnectionsTxTeardownAll_Type()
)
controlConnectionsTxTeardownAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxTeardownAll.setStatus("current")
_ControlConnectionsTxVmToPeer_Type = Unsigned32
_ControlConnectionsTxVmToPeer_Object = MibTableColumn
controlConnectionsTxVmToPeer = _ControlConnectionsTxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 30),
    _ControlConnectionsTxVmToPeer_Type()
)
controlConnectionsTxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxVmToPeer.setStatus("current")
_ControlConnectionsTxRegisterToVm_Type = Unsigned32
_ControlConnectionsTxRegisterToVm_Object = MibTableColumn
controlConnectionsTxRegisterToVm = _ControlConnectionsTxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 31),
    _ControlConnectionsTxRegisterToVm_Type()
)
controlConnectionsTxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxRegisterToVm.setStatus("current")
_ControlConnectionsRxHello_Type = Unsigned32
_ControlConnectionsRxHello_Object = MibTableColumn
controlConnectionsRxHello = _ControlConnectionsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 32),
    _ControlConnectionsRxHello_Type()
)
controlConnectionsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxHello.setStatus("current")
_ControlConnectionsRxConnects_Type = Unsigned32
_ControlConnectionsRxConnects_Object = MibTableColumn
controlConnectionsRxConnects = _ControlConnectionsRxConnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 33),
    _ControlConnectionsRxConnects_Type()
)
controlConnectionsRxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxConnects.setStatus("current")
_ControlConnectionsRxRegisters_Type = Unsigned32
_ControlConnectionsRxRegisters_Object = MibTableColumn
controlConnectionsRxRegisters = _ControlConnectionsRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 34),
    _ControlConnectionsRxRegisters_Type()
)
controlConnectionsRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxRegisters.setStatus("current")
_ControlConnectionsRxRegisterReplies_Type = Unsigned32
_ControlConnectionsRxRegisterReplies_Object = MibTableColumn
controlConnectionsRxRegisterReplies = _ControlConnectionsRxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 35),
    _ControlConnectionsRxRegisterReplies_Type()
)
controlConnectionsRxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxRegisterReplies.setStatus("current")
_ControlConnectionsRxChallenge_Type = Unsigned32
_ControlConnectionsRxChallenge_Object = MibTableColumn
controlConnectionsRxChallenge = _ControlConnectionsRxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 36),
    _ControlConnectionsRxChallenge_Type()
)
controlConnectionsRxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxChallenge.setStatus("current")
_ControlConnectionsRxChallengeResp_Type = Unsigned32
_ControlConnectionsRxChallengeResp_Object = MibTableColumn
controlConnectionsRxChallengeResp = _ControlConnectionsRxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 37),
    _ControlConnectionsRxChallengeResp_Type()
)
controlConnectionsRxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxChallengeResp.setStatus("current")
_ControlConnectionsRxChallengeAck_Type = Unsigned32
_ControlConnectionsRxChallengeAck_Object = MibTableColumn
controlConnectionsRxChallengeAck = _ControlConnectionsRxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 38),
    _ControlConnectionsRxChallengeAck_Type()
)
controlConnectionsRxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxChallengeAck.setStatus("current")
_ControlConnectionsRxTeardown_Type = Unsigned32
_ControlConnectionsRxTeardown_Object = MibTableColumn
controlConnectionsRxTeardown = _ControlConnectionsRxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 39),
    _ControlConnectionsRxTeardown_Type()
)
controlConnectionsRxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxTeardown.setStatus("current")
_ControlConnectionsRxVmToPeer_Type = Unsigned32
_ControlConnectionsRxVmToPeer_Object = MibTableColumn
controlConnectionsRxVmToPeer = _ControlConnectionsRxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 40),
    _ControlConnectionsRxVmToPeer_Type()
)
controlConnectionsRxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxVmToPeer.setStatus("current")
_ControlConnectionsRxRegisterToVm_Type = Unsigned32
_ControlConnectionsRxRegisterToVm_Object = MibTableColumn
controlConnectionsRxRegisterToVm = _ControlConnectionsRxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 41),
    _ControlConnectionsRxRegisterToVm_Type()
)
controlConnectionsRxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxRegisterToVm.setStatus("current")
_ControlConnectionsNegotiatedHelloInterval_Type = Unsigned32
_ControlConnectionsNegotiatedHelloInterval_Object = MibTableColumn
controlConnectionsNegotiatedHelloInterval = _ControlConnectionsNegotiatedHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 42),
    _ControlConnectionsNegotiatedHelloInterval_Type()
)
controlConnectionsNegotiatedHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsNegotiatedHelloInterval.setStatus("current")
_ControlConnectionsNegotiatedHelloTolerance_Type = Unsigned32
_ControlConnectionsNegotiatedHelloTolerance_Object = MibTableColumn
controlConnectionsNegotiatedHelloTolerance = _ControlConnectionsNegotiatedHelloTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 43),
    _ControlConnectionsNegotiatedHelloTolerance_Type()
)
controlConnectionsNegotiatedHelloTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsNegotiatedHelloTolerance.setStatus("current")
_ControlConnectionsVOrgName_Type = String
_ControlConnectionsVOrgName_Object = MibTableColumn
controlConnectionsVOrgName = _ControlConnectionsVOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 45),
    _ControlConnectionsVOrgName_Type()
)
controlConnectionsVOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsVOrgName.setStatus("current")
_ControlConnectionsTxCreateCert_Type = Unsigned32
_ControlConnectionsTxCreateCert_Object = MibTableColumn
controlConnectionsTxCreateCert = _ControlConnectionsTxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 46),
    _ControlConnectionsTxCreateCert_Type()
)
controlConnectionsTxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxCreateCert.setStatus("current")
_ControlConnectionsRxCreateCert_Type = Unsigned32
_ControlConnectionsRxCreateCert_Object = MibTableColumn
controlConnectionsRxCreateCert = _ControlConnectionsRxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 47),
    _ControlConnectionsRxCreateCert_Type()
)
controlConnectionsRxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxCreateCert.setStatus("current")
_ControlConnectionsTxCreateCertReply_Type = Unsigned32
_ControlConnectionsTxCreateCertReply_Object = MibTableColumn
controlConnectionsTxCreateCertReply = _ControlConnectionsTxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 48),
    _ControlConnectionsTxCreateCertReply_Type()
)
controlConnectionsTxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsTxCreateCertReply.setStatus("current")
_ControlConnectionsRxCreateCertReply_Type = Unsigned32
_ControlConnectionsRxCreateCertReply_Object = MibTableColumn
controlConnectionsRxCreateCertReply = _ControlConnectionsRxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 49),
    _ControlConnectionsRxCreateCertReply_Type()
)
controlConnectionsRxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsRxCreateCertReply.setStatus("current")
_ControlConnectionsBehindProxy_Type = String
_ControlConnectionsBehindProxy_Object = MibTableColumn
controlConnectionsBehindProxy = _ControlConnectionsBehindProxy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 50),
    _ControlConnectionsBehindProxy_Type()
)
controlConnectionsBehindProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsBehindProxy.setStatus("current")
_ControlConnectionsPeerSessId_Type = Counter64
_ControlConnectionsPeerSessId_Object = MibTableColumn
controlConnectionsPeerSessId = _ControlConnectionsPeerSessId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 51),
    _ControlConnectionsPeerSessId_Type()
)
controlConnectionsPeerSessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsPeerSessId.setStatus("current")
_ControlConnectionsLocalInterface_Type = String
_ControlConnectionsLocalInterface_Object = MibTableColumn
controlConnectionsLocalInterface = _ControlConnectionsLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 2, 1, 52),
    _ControlConnectionsLocalInterface_Type()
)
controlConnectionsLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsLocalInterface.setStatus("current")
_ControlConnectionsHistoryTable_Object = MibTable
controlConnectionsHistoryTable = _ControlConnectionsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3)
)
if mibBuilder.loadTexts:
    controlConnectionsHistoryTable.setStatus("current")
_ControlConnectionsHistoryEntry_Object = MibTableRow
controlConnectionsHistoryEntry = _ControlConnectionsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1)
)
controlConnectionsHistoryEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryInstance"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryIndex"),
)
if mibBuilder.loadTexts:
    controlConnectionsHistoryEntry.setStatus("current")
_ControlConnectionsHistoryInstance_Type = Unsigned32
_ControlConnectionsHistoryInstance_Object = MibTableColumn
controlConnectionsHistoryInstance = _ControlConnectionsHistoryInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 1),
    _ControlConnectionsHistoryInstance_Type()
)
controlConnectionsHistoryInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsHistoryInstance.setStatus("current")
_ControlConnectionsHistoryIndex_Type = Unsigned32
_ControlConnectionsHistoryIndex_Object = MibTableColumn
controlConnectionsHistoryIndex = _ControlConnectionsHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 2),
    _ControlConnectionsHistoryIndex_Type()
)
controlConnectionsHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlConnectionsHistoryIndex.setStatus("current")
_ControlConnectionsHistoryPeerType_Type = PersonalityEnumOper
_ControlConnectionsHistoryPeerType_Object = MibTableColumn
controlConnectionsHistoryPeerType = _ControlConnectionsHistoryPeerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 3),
    _ControlConnectionsHistoryPeerType_Type()
)
controlConnectionsHistoryPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPeerType.setStatus("current")
_ControlConnectionsHistorySiteId_Type = Unsigned32
_ControlConnectionsHistorySiteId_Object = MibTableColumn
controlConnectionsHistorySiteId = _ControlConnectionsHistorySiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 4),
    _ControlConnectionsHistorySiteId_Type()
)
controlConnectionsHistorySiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistorySiteId.setStatus("current")
_ControlConnectionsHistoryDomainId_Type = Unsigned32
_ControlConnectionsHistoryDomainId_Object = MibTableColumn
controlConnectionsHistoryDomainId = _ControlConnectionsHistoryDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 5),
    _ControlConnectionsHistoryDomainId_Type()
)
controlConnectionsHistoryDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryDomainId.setStatus("current")
_ControlConnectionsHistoryPrivateIp_Type = InetAddressIP
_ControlConnectionsHistoryPrivateIp_Object = MibTableColumn
controlConnectionsHistoryPrivateIp = _ControlConnectionsHistoryPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 6),
    _ControlConnectionsHistoryPrivateIp_Type()
)
controlConnectionsHistoryPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPrivateIp.setStatus("current")
_ControlConnectionsHistoryPrivatePort_Type = Unsigned32
_ControlConnectionsHistoryPrivatePort_Object = MibTableColumn
controlConnectionsHistoryPrivatePort = _ControlConnectionsHistoryPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 7),
    _ControlConnectionsHistoryPrivatePort_Type()
)
controlConnectionsHistoryPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPrivatePort.setStatus("current")
_ControlConnectionsHistoryPublicIp_Type = InetAddressIP
_ControlConnectionsHistoryPublicIp_Object = MibTableColumn
controlConnectionsHistoryPublicIp = _ControlConnectionsHistoryPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 8),
    _ControlConnectionsHistoryPublicIp_Type()
)
controlConnectionsHistoryPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPublicIp.setStatus("current")
_ControlConnectionsHistoryPublicPort_Type = Unsigned32
_ControlConnectionsHistoryPublicPort_Object = MibTableColumn
controlConnectionsHistoryPublicPort = _ControlConnectionsHistoryPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 9),
    _ControlConnectionsHistoryPublicPort_Type()
)
controlConnectionsHistoryPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPublicPort.setStatus("current")
_ControlConnectionsHistorySystemIp_Type = InetAddressIP
_ControlConnectionsHistorySystemIp_Object = MibTableColumn
controlConnectionsHistorySystemIp = _ControlConnectionsHistorySystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 10),
    _ControlConnectionsHistorySystemIp_Type()
)
controlConnectionsHistorySystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistorySystemIp.setStatus("current")


class _ControlConnectionsHistoryProtocol_Type(ControlProtocolEnum):
    """Custom type controlConnectionsHistoryProtocol based on ControlProtocolEnum"""
    defaultValue = 0


_ControlConnectionsHistoryProtocol_Type.__name__ = "ControlProtocolEnum"
_ControlConnectionsHistoryProtocol_Object = MibTableColumn
controlConnectionsHistoryProtocol = _ControlConnectionsHistoryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 11),
    _ControlConnectionsHistoryProtocol_Type()
)
controlConnectionsHistoryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryProtocol.setStatus("current")
_ControlConnectionsHistoryLocalColor_Type = ColorEnum
_ControlConnectionsHistoryLocalColor_Object = MibTableColumn
controlConnectionsHistoryLocalColor = _ControlConnectionsHistoryLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 12),
    _ControlConnectionsHistoryLocalColor_Type()
)
controlConnectionsHistoryLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryLocalColor.setStatus("current")
_ControlConnectionsHistoryRemoteColor_Type = ColorEnum
_ControlConnectionsHistoryRemoteColor_Object = MibTableColumn
controlConnectionsHistoryRemoteColor = _ControlConnectionsHistoryRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 13),
    _ControlConnectionsHistoryRemoteColor_Type()
)
controlConnectionsHistoryRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRemoteColor.setStatus("current")
_ControlConnectionsHistoryState_Type = SessionState
_ControlConnectionsHistoryState_Object = MibTableColumn
controlConnectionsHistoryState = _ControlConnectionsHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 14),
    _ControlConnectionsHistoryState_Type()
)
controlConnectionsHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryState.setStatus("current")
_ControlConnectionsHistoryLocalEnum_Type = ConnFlagEnum
_ControlConnectionsHistoryLocalEnum_Object = MibTableColumn
controlConnectionsHistoryLocalEnum = _ControlConnectionsHistoryLocalEnum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 15),
    _ControlConnectionsHistoryLocalEnum_Type()
)
controlConnectionsHistoryLocalEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryLocalEnum.setStatus("current")
_ControlConnectionsHistoryRemoteEnum_Type = ConnFlagEnum
_ControlConnectionsHistoryRemoteEnum_Object = MibTableColumn
controlConnectionsHistoryRemoteEnum = _ControlConnectionsHistoryRemoteEnum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 16),
    _ControlConnectionsHistoryRemoteEnum_Type()
)
controlConnectionsHistoryRemoteEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRemoteEnum.setStatus("current")
_ControlConnectionsHistoryLocalStateInfo_Type = String
_ControlConnectionsHistoryLocalStateInfo_Object = MibTableColumn
controlConnectionsHistoryLocalStateInfo = _ControlConnectionsHistoryLocalStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 17),
    _ControlConnectionsHistoryLocalStateInfo_Type()
)
controlConnectionsHistoryLocalStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryLocalStateInfo.setStatus("current")
_ControlConnectionsHistoryRemoteStateInfo_Type = String
_ControlConnectionsHistoryRemoteStateInfo_Object = MibTableColumn
controlConnectionsHistoryRemoteStateInfo = _ControlConnectionsHistoryRemoteStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 18),
    _ControlConnectionsHistoryRemoteStateInfo_Type()
)
controlConnectionsHistoryRemoteStateInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRemoteStateInfo.setStatus("current")
_ControlConnectionsHistoryDowntime_Type = String
_ControlConnectionsHistoryDowntime_Object = MibTableColumn
controlConnectionsHistoryDowntime = _ControlConnectionsHistoryDowntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 19),
    _ControlConnectionsHistoryDowntime_Type()
)
controlConnectionsHistoryDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryDowntime.setStatus("current")
_ControlConnectionsHistoryTxHello_Type = Unsigned32
_ControlConnectionsHistoryTxHello_Object = MibTableColumn
controlConnectionsHistoryTxHello = _ControlConnectionsHistoryTxHello_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 20),
    _ControlConnectionsHistoryTxHello_Type()
)
controlConnectionsHistoryTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxHello.setStatus("current")
_ControlConnectionsHistoryTxConnects_Type = Unsigned32
_ControlConnectionsHistoryTxConnects_Object = MibTableColumn
controlConnectionsHistoryTxConnects = _ControlConnectionsHistoryTxConnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 21),
    _ControlConnectionsHistoryTxConnects_Type()
)
controlConnectionsHistoryTxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxConnects.setStatus("current")
_ControlConnectionsHistoryTxRegisters_Type = Unsigned32
_ControlConnectionsHistoryTxRegisters_Object = MibTableColumn
controlConnectionsHistoryTxRegisters = _ControlConnectionsHistoryTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 22),
    _ControlConnectionsHistoryTxRegisters_Type()
)
controlConnectionsHistoryTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxRegisters.setStatus("current")
_ControlConnectionsHistoryTxRegisterReplies_Type = Unsigned32
_ControlConnectionsHistoryTxRegisterReplies_Object = MibTableColumn
controlConnectionsHistoryTxRegisterReplies = _ControlConnectionsHistoryTxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 23),
    _ControlConnectionsHistoryTxRegisterReplies_Type()
)
controlConnectionsHistoryTxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxRegisterReplies.setStatus("current")
_ControlConnectionsHistoryTxChallenge_Type = Unsigned32
_ControlConnectionsHistoryTxChallenge_Object = MibTableColumn
controlConnectionsHistoryTxChallenge = _ControlConnectionsHistoryTxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 24),
    _ControlConnectionsHistoryTxChallenge_Type()
)
controlConnectionsHistoryTxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxChallenge.setStatus("current")
_ControlConnectionsHistoryTxChallengeResp_Type = Unsigned32
_ControlConnectionsHistoryTxChallengeResp_Object = MibTableColumn
controlConnectionsHistoryTxChallengeResp = _ControlConnectionsHistoryTxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 25),
    _ControlConnectionsHistoryTxChallengeResp_Type()
)
controlConnectionsHistoryTxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxChallengeResp.setStatus("current")
_ControlConnectionsHistoryTxChallengeAck_Type = Unsigned32
_ControlConnectionsHistoryTxChallengeAck_Object = MibTableColumn
controlConnectionsHistoryTxChallengeAck = _ControlConnectionsHistoryTxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 26),
    _ControlConnectionsHistoryTxChallengeAck_Type()
)
controlConnectionsHistoryTxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxChallengeAck.setStatus("current")
_ControlConnectionsHistoryTxTeardown_Type = Unsigned32
_ControlConnectionsHistoryTxTeardown_Object = MibTableColumn
controlConnectionsHistoryTxTeardown = _ControlConnectionsHistoryTxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 27),
    _ControlConnectionsHistoryTxTeardown_Type()
)
controlConnectionsHistoryTxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxTeardown.setStatus("current")
_ControlConnectionsHistoryTxTeardownAll_Type = Unsigned32
_ControlConnectionsHistoryTxTeardownAll_Object = MibTableColumn
controlConnectionsHistoryTxTeardownAll = _ControlConnectionsHistoryTxTeardownAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 28),
    _ControlConnectionsHistoryTxTeardownAll_Type()
)
controlConnectionsHistoryTxTeardownAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxTeardownAll.setStatus("current")
_ControlConnectionsHistoryTxVmToPeer_Type = Unsigned32
_ControlConnectionsHistoryTxVmToPeer_Object = MibTableColumn
controlConnectionsHistoryTxVmToPeer = _ControlConnectionsHistoryTxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 29),
    _ControlConnectionsHistoryTxVmToPeer_Type()
)
controlConnectionsHistoryTxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxVmToPeer.setStatus("current")
_ControlConnectionsHistoryTxRegisterToVm_Type = Unsigned32
_ControlConnectionsHistoryTxRegisterToVm_Object = MibTableColumn
controlConnectionsHistoryTxRegisterToVm = _ControlConnectionsHistoryTxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 30),
    _ControlConnectionsHistoryTxRegisterToVm_Type()
)
controlConnectionsHistoryTxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxRegisterToVm.setStatus("current")
_ControlConnectionsHistoryRxHello_Type = Unsigned32
_ControlConnectionsHistoryRxHello_Object = MibTableColumn
controlConnectionsHistoryRxHello = _ControlConnectionsHistoryRxHello_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 31),
    _ControlConnectionsHistoryRxHello_Type()
)
controlConnectionsHistoryRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxHello.setStatus("current")
_ControlConnectionsHistoryRxConnects_Type = Unsigned32
_ControlConnectionsHistoryRxConnects_Object = MibTableColumn
controlConnectionsHistoryRxConnects = _ControlConnectionsHistoryRxConnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 32),
    _ControlConnectionsHistoryRxConnects_Type()
)
controlConnectionsHistoryRxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxConnects.setStatus("current")
_ControlConnectionsHistoryRxRegisters_Type = Unsigned32
_ControlConnectionsHistoryRxRegisters_Object = MibTableColumn
controlConnectionsHistoryRxRegisters = _ControlConnectionsHistoryRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 33),
    _ControlConnectionsHistoryRxRegisters_Type()
)
controlConnectionsHistoryRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxRegisters.setStatus("current")
_ControlConnectionsHistoryRxRegisterReplies_Type = Unsigned32
_ControlConnectionsHistoryRxRegisterReplies_Object = MibTableColumn
controlConnectionsHistoryRxRegisterReplies = _ControlConnectionsHistoryRxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 34),
    _ControlConnectionsHistoryRxRegisterReplies_Type()
)
controlConnectionsHistoryRxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxRegisterReplies.setStatus("current")
_ControlConnectionsHistoryRxChallenge_Type = Unsigned32
_ControlConnectionsHistoryRxChallenge_Object = MibTableColumn
controlConnectionsHistoryRxChallenge = _ControlConnectionsHistoryRxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 35),
    _ControlConnectionsHistoryRxChallenge_Type()
)
controlConnectionsHistoryRxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxChallenge.setStatus("current")
_ControlConnectionsHistoryRxChallengeResp_Type = Unsigned32
_ControlConnectionsHistoryRxChallengeResp_Object = MibTableColumn
controlConnectionsHistoryRxChallengeResp = _ControlConnectionsHistoryRxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 36),
    _ControlConnectionsHistoryRxChallengeResp_Type()
)
controlConnectionsHistoryRxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxChallengeResp.setStatus("current")
_ControlConnectionsHistoryRxChallengeAck_Type = Unsigned32
_ControlConnectionsHistoryRxChallengeAck_Object = MibTableColumn
controlConnectionsHistoryRxChallengeAck = _ControlConnectionsHistoryRxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 37),
    _ControlConnectionsHistoryRxChallengeAck_Type()
)
controlConnectionsHistoryRxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxChallengeAck.setStatus("current")
_ControlConnectionsHistoryRxTeardown_Type = Unsigned32
_ControlConnectionsHistoryRxTeardown_Object = MibTableColumn
controlConnectionsHistoryRxTeardown = _ControlConnectionsHistoryRxTeardown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 38),
    _ControlConnectionsHistoryRxTeardown_Type()
)
controlConnectionsHistoryRxTeardown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxTeardown.setStatus("current")
_ControlConnectionsHistoryRxVmToPeer_Type = Unsigned32
_ControlConnectionsHistoryRxVmToPeer_Object = MibTableColumn
controlConnectionsHistoryRxVmToPeer = _ControlConnectionsHistoryRxVmToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 39),
    _ControlConnectionsHistoryRxVmToPeer_Type()
)
controlConnectionsHistoryRxVmToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxVmToPeer.setStatus("current")
_ControlConnectionsHistoryRxRegisterToVm_Type = Unsigned32
_ControlConnectionsHistoryRxRegisterToVm_Object = MibTableColumn
controlConnectionsHistoryRxRegisterToVm = _ControlConnectionsHistoryRxRegisterToVm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 40),
    _ControlConnectionsHistoryRxRegisterToVm_Type()
)
controlConnectionsHistoryRxRegisterToVm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxRegisterToVm.setStatus("current")
_ControlConnectionsHistoryRepCount_Type = Unsigned32
_ControlConnectionsHistoryRepCount_Object = MibTableColumn
controlConnectionsHistoryRepCount = _ControlConnectionsHistoryRepCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 41),
    _ControlConnectionsHistoryRepCount_Type()
)
controlConnectionsHistoryRepCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRepCount.setStatus("current")
_ControlConnectionsHistoryPrevDowntime_Type = String
_ControlConnectionsHistoryPrevDowntime_Object = MibTableColumn
controlConnectionsHistoryPrevDowntime = _ControlConnectionsHistoryPrevDowntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 42),
    _ControlConnectionsHistoryPrevDowntime_Type()
)
controlConnectionsHistoryPrevDowntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryPrevDowntime.setStatus("current")
_ControlConnectionsHistoryVHOrgName_Type = String
_ControlConnectionsHistoryVHOrgName_Object = MibTableColumn
controlConnectionsHistoryVHOrgName = _ControlConnectionsHistoryVHOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 44),
    _ControlConnectionsHistoryVHOrgName_Type()
)
controlConnectionsHistoryVHOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryVHOrgName.setStatus("current")
_ControlConnectionsHistoryUuid_Type = String
_ControlConnectionsHistoryUuid_Object = MibTableColumn
controlConnectionsHistoryUuid = _ControlConnectionsHistoryUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 45),
    _ControlConnectionsHistoryUuid_Type()
)
controlConnectionsHistoryUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryUuid.setStatus("current")
_ControlConnectionsHistoryTxCreateCert_Type = Unsigned32
_ControlConnectionsHistoryTxCreateCert_Object = MibTableColumn
controlConnectionsHistoryTxCreateCert = _ControlConnectionsHistoryTxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 46),
    _ControlConnectionsHistoryTxCreateCert_Type()
)
controlConnectionsHistoryTxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxCreateCert.setStatus("current")
_ControlConnectionsHistoryRxCreateCert_Type = Unsigned32
_ControlConnectionsHistoryRxCreateCert_Object = MibTableColumn
controlConnectionsHistoryRxCreateCert = _ControlConnectionsHistoryRxCreateCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 47),
    _ControlConnectionsHistoryRxCreateCert_Type()
)
controlConnectionsHistoryRxCreateCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxCreateCert.setStatus("current")
_ControlConnectionsHistoryTxCreateCertReply_Type = Unsigned32
_ControlConnectionsHistoryTxCreateCertReply_Object = MibTableColumn
controlConnectionsHistoryTxCreateCertReply = _ControlConnectionsHistoryTxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 48),
    _ControlConnectionsHistoryTxCreateCertReply_Type()
)
controlConnectionsHistoryTxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryTxCreateCertReply.setStatus("current")
_ControlConnectionsHistoryRxCreateCertReply_Type = Unsigned32
_ControlConnectionsHistoryRxCreateCertReply_Object = MibTableColumn
controlConnectionsHistoryRxCreateCertReply = _ControlConnectionsHistoryRxCreateCertReply_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 49),
    _ControlConnectionsHistoryRxCreateCertReply_Type()
)
controlConnectionsHistoryRxCreateCertReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryRxCreateCertReply.setStatus("current")
_ControlConnectionsHistoryLocalInterface_Type = String
_ControlConnectionsHistoryLocalInterface_Object = MibTableColumn
controlConnectionsHistoryLocalInterface = _ControlConnectionsHistoryLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 3, 1, 50),
    _ControlConnectionsHistoryLocalInterface_Type()
)
controlConnectionsHistoryLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlConnectionsHistoryLocalInterface.setStatus("current")
_ControlStatistics_ObjectIdentity = ObjectIdentity
controlStatistics = _ControlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4)
)
_ControlStatisticsTxPkts_Type = Counter64
_ControlStatisticsTxPkts_Object = MibScalar
controlStatisticsTxPkts = _ControlStatisticsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 1),
    _ControlStatisticsTxPkts_Type()
)
controlStatisticsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxPkts.setStatus("current")
_ControlStatisticsTxOctets_Type = Unsigned32
_ControlStatisticsTxOctets_Object = MibScalar
controlStatisticsTxOctets = _ControlStatisticsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 2),
    _ControlStatisticsTxOctets_Type()
)
controlStatisticsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxOctets.setStatus("current")
_ControlStatisticsTxError_Type = Unsigned32
_ControlStatisticsTxError_Object = MibScalar
controlStatisticsTxError = _ControlStatisticsTxError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 3),
    _ControlStatisticsTxError_Type()
)
controlStatisticsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxError.setStatus("current")
_ControlStatisticsTxBlocked_Type = Unsigned32
_ControlStatisticsTxBlocked_Object = MibScalar
controlStatisticsTxBlocked = _ControlStatisticsTxBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 4),
    _ControlStatisticsTxBlocked_Type()
)
controlStatisticsTxBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxBlocked.setStatus("current")
_ControlStatisticsTxHello_Type = Counter64
_ControlStatisticsTxHello_Object = MibScalar
controlStatisticsTxHello = _ControlStatisticsTxHello_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 5),
    _ControlStatisticsTxHello_Type()
)
controlStatisticsTxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxHello.setStatus("current")
_ControlStatisticsTxConnects_Type = Unsigned32
_ControlStatisticsTxConnects_Object = MibScalar
controlStatisticsTxConnects = _ControlStatisticsTxConnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 6),
    _ControlStatisticsTxConnects_Type()
)
controlStatisticsTxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxConnects.setStatus("current")
_ControlStatisticsTxRegisters_Type = Unsigned32
_ControlStatisticsTxRegisters_Object = MibScalar
controlStatisticsTxRegisters = _ControlStatisticsTxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 7),
    _ControlStatisticsTxRegisters_Type()
)
controlStatisticsTxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxRegisters.setStatus("current")
_ControlStatisticsTxRegisterReplies_Type = Unsigned32
_ControlStatisticsTxRegisterReplies_Object = MibScalar
controlStatisticsTxRegisterReplies = _ControlStatisticsTxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 8),
    _ControlStatisticsTxRegisterReplies_Type()
)
controlStatisticsTxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxRegisterReplies.setStatus("current")
_ControlStatisticsTxDtlsHandshake_Type = Unsigned32
_ControlStatisticsTxDtlsHandshake_Object = MibScalar
controlStatisticsTxDtlsHandshake = _ControlStatisticsTxDtlsHandshake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 9),
    _ControlStatisticsTxDtlsHandshake_Type()
)
controlStatisticsTxDtlsHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxDtlsHandshake.setStatus("current")
_ControlStatisticsTxDtlsHandshakeFailures_Type = Unsigned32
_ControlStatisticsTxDtlsHandshakeFailures_Object = MibScalar
controlStatisticsTxDtlsHandshakeFailures = _ControlStatisticsTxDtlsHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 10),
    _ControlStatisticsTxDtlsHandshakeFailures_Type()
)
controlStatisticsTxDtlsHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxDtlsHandshakeFailures.setStatus("current")
_ControlStatisticsTxDtlsHandshakeDone_Type = Unsigned32
_ControlStatisticsTxDtlsHandshakeDone_Object = MibScalar
controlStatisticsTxDtlsHandshakeDone = _ControlStatisticsTxDtlsHandshakeDone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 11),
    _ControlStatisticsTxDtlsHandshakeDone_Type()
)
controlStatisticsTxDtlsHandshakeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxDtlsHandshakeDone.setStatus("current")
_ControlStatisticsTxChallenge_Type = Unsigned32
_ControlStatisticsTxChallenge_Object = MibScalar
controlStatisticsTxChallenge = _ControlStatisticsTxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 12),
    _ControlStatisticsTxChallenge_Type()
)
controlStatisticsTxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallenge.setStatus("current")
_ControlStatisticsTxChallengeResp_Type = Unsigned32
_ControlStatisticsTxChallengeResp_Object = MibScalar
controlStatisticsTxChallengeResp = _ControlStatisticsTxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 13),
    _ControlStatisticsTxChallengeResp_Type()
)
controlStatisticsTxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeResp.setStatus("current")
_ControlStatisticsTxChallengeAck_Type = Unsigned32
_ControlStatisticsTxChallengeAck_Object = MibScalar
controlStatisticsTxChallengeAck = _ControlStatisticsTxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 14),
    _ControlStatisticsTxChallengeAck_Type()
)
controlStatisticsTxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeAck.setStatus("current")
_ControlStatisticsTxChallengeError_Type = Unsigned32
_ControlStatisticsTxChallengeError_Object = MibScalar
controlStatisticsTxChallengeError = _ControlStatisticsTxChallengeError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 15),
    _ControlStatisticsTxChallengeError_Type()
)
controlStatisticsTxChallengeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeError.setStatus("current")
_ControlStatisticsTxChallengeRespError_Type = Unsigned32
_ControlStatisticsTxChallengeRespError_Object = MibScalar
controlStatisticsTxChallengeRespError = _ControlStatisticsTxChallengeRespError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 16),
    _ControlStatisticsTxChallengeRespError_Type()
)
controlStatisticsTxChallengeRespError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeRespError.setStatus("current")
_ControlStatisticsTxChallengeAckError_Type = Unsigned32
_ControlStatisticsTxChallengeAckError_Object = MibScalar
controlStatisticsTxChallengeAckError = _ControlStatisticsTxChallengeAckError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 17),
    _ControlStatisticsTxChallengeAckError_Type()
)
controlStatisticsTxChallengeAckError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeAckError.setStatus("current")
_ControlStatisticsTxChallengeGenError_Type = Unsigned32
_ControlStatisticsTxChallengeGenError_Object = MibScalar
controlStatisticsTxChallengeGenError = _ControlStatisticsTxChallengeGenError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 18),
    _ControlStatisticsTxChallengeGenError_Type()
)
controlStatisticsTxChallengeGenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxChallengeGenError.setStatus("current")
_ControlStatisticsTxVmanageToPeer_Type = Unsigned32
_ControlStatisticsTxVmanageToPeer_Object = MibScalar
controlStatisticsTxVmanageToPeer = _ControlStatisticsTxVmanageToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 19),
    _ControlStatisticsTxVmanageToPeer_Type()
)
controlStatisticsTxVmanageToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxVmanageToPeer.setStatus("current")
_ControlStatisticsTxRegisterToVmanage_Type = Unsigned32
_ControlStatisticsTxRegisterToVmanage_Object = MibScalar
controlStatisticsTxRegisterToVmanage = _ControlStatisticsTxRegisterToVmanage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 20),
    _ControlStatisticsTxRegisterToVmanage_Type()
)
controlStatisticsTxRegisterToVmanage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsTxRegisterToVmanage.setStatus("current")
_ControlStatisticsRxPkts_Type = Counter64
_ControlStatisticsRxPkts_Object = MibScalar
controlStatisticsRxPkts = _ControlStatisticsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 21),
    _ControlStatisticsRxPkts_Type()
)
controlStatisticsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxPkts.setStatus("current")
_ControlStatisticsRxOctets_Type = Unsigned32
_ControlStatisticsRxOctets_Object = MibScalar
controlStatisticsRxOctets = _ControlStatisticsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 22),
    _ControlStatisticsRxOctets_Type()
)
controlStatisticsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxOctets.setStatus("current")
_ControlStatisticsRxError_Type = Unsigned32
_ControlStatisticsRxError_Object = MibScalar
controlStatisticsRxError = _ControlStatisticsRxError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 23),
    _ControlStatisticsRxError_Type()
)
controlStatisticsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxError.setStatus("current")
_ControlStatisticsRxHello_Type = Counter64
_ControlStatisticsRxHello_Object = MibScalar
controlStatisticsRxHello = _ControlStatisticsRxHello_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 24),
    _ControlStatisticsRxHello_Type()
)
controlStatisticsRxHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxHello.setStatus("current")
_ControlStatisticsRxConnects_Type = Unsigned32
_ControlStatisticsRxConnects_Object = MibScalar
controlStatisticsRxConnects = _ControlStatisticsRxConnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 25),
    _ControlStatisticsRxConnects_Type()
)
controlStatisticsRxConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxConnects.setStatus("current")
_ControlStatisticsRxRegisters_Type = Unsigned32
_ControlStatisticsRxRegisters_Object = MibScalar
controlStatisticsRxRegisters = _ControlStatisticsRxRegisters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 26),
    _ControlStatisticsRxRegisters_Type()
)
controlStatisticsRxRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxRegisters.setStatus("current")
_ControlStatisticsRxRegisterReplies_Type = Unsigned32
_ControlStatisticsRxRegisterReplies_Object = MibScalar
controlStatisticsRxRegisterReplies = _ControlStatisticsRxRegisterReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 27),
    _ControlStatisticsRxRegisterReplies_Type()
)
controlStatisticsRxRegisterReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxRegisterReplies.setStatus("current")
_ControlStatisticsRxDtlsHandshake_Type = Unsigned32
_ControlStatisticsRxDtlsHandshake_Object = MibScalar
controlStatisticsRxDtlsHandshake = _ControlStatisticsRxDtlsHandshake_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 28),
    _ControlStatisticsRxDtlsHandshake_Type()
)
controlStatisticsRxDtlsHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxDtlsHandshake.setStatus("current")
_ControlStatisticsRxDtlsHandshakeFailures_Type = Unsigned32
_ControlStatisticsRxDtlsHandshakeFailures_Object = MibScalar
controlStatisticsRxDtlsHandshakeFailures = _ControlStatisticsRxDtlsHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 29),
    _ControlStatisticsRxDtlsHandshakeFailures_Type()
)
controlStatisticsRxDtlsHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxDtlsHandshakeFailures.setStatus("current")
_ControlStatisticsRxDtlsHandshakeDone_Type = Unsigned32
_ControlStatisticsRxDtlsHandshakeDone_Object = MibScalar
controlStatisticsRxDtlsHandshakeDone = _ControlStatisticsRxDtlsHandshakeDone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 30),
    _ControlStatisticsRxDtlsHandshakeDone_Type()
)
controlStatisticsRxDtlsHandshakeDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxDtlsHandshakeDone.setStatus("current")
_ControlStatisticsRxChallenge_Type = Unsigned32
_ControlStatisticsRxChallenge_Object = MibScalar
controlStatisticsRxChallenge = _ControlStatisticsRxChallenge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 31),
    _ControlStatisticsRxChallenge_Type()
)
controlStatisticsRxChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxChallenge.setStatus("current")
_ControlStatisticsRxChallengeResp_Type = Unsigned32
_ControlStatisticsRxChallengeResp_Object = MibScalar
controlStatisticsRxChallengeResp = _ControlStatisticsRxChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 32),
    _ControlStatisticsRxChallengeResp_Type()
)
controlStatisticsRxChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxChallengeResp.setStatus("current")
_ControlStatisticsRxChallengeAck_Type = Unsigned32
_ControlStatisticsRxChallengeAck_Object = MibScalar
controlStatisticsRxChallengeAck = _ControlStatisticsRxChallengeAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 33),
    _ControlStatisticsRxChallengeAck_Type()
)
controlStatisticsRxChallengeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxChallengeAck.setStatus("current")
_ControlStatisticsChallengeFailures_Type = Unsigned32
_ControlStatisticsChallengeFailures_Object = MibScalar
controlStatisticsChallengeFailures = _ControlStatisticsChallengeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 34),
    _ControlStatisticsChallengeFailures_Type()
)
controlStatisticsChallengeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsChallengeFailures.setStatus("current")
_ControlStatisticsRxVmanageToPeer_Type = Unsigned32
_ControlStatisticsRxVmanageToPeer_Object = MibScalar
controlStatisticsRxVmanageToPeer = _ControlStatisticsRxVmanageToPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 35),
    _ControlStatisticsRxVmanageToPeer_Type()
)
controlStatisticsRxVmanageToPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxVmanageToPeer.setStatus("current")
_ControlStatisticsRxRegisterToVmanage_Type = Unsigned32
_ControlStatisticsRxRegisterToVmanage_Object = MibScalar
controlStatisticsRxRegisterToVmanage = _ControlStatisticsRxRegisterToVmanage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 36),
    _ControlStatisticsRxRegisterToVmanage_Type()
)
controlStatisticsRxRegisterToVmanage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsRxRegisterToVmanage.setStatus("current")
_ControlStatisticsBidFailuresNeedingReset_Type = Unsigned32
_ControlStatisticsBidFailuresNeedingReset_Object = MibScalar
controlStatisticsBidFailuresNeedingReset = _ControlStatisticsBidFailuresNeedingReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 4, 37),
    _ControlStatisticsBidFailuresNeedingReset_Type()
)
controlStatisticsBidFailuresNeedingReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlStatisticsBidFailuresNeedingReset.setStatus("current")
_ControlLocalProperties_ObjectIdentity = ObjectIdentity
controlLocalProperties = _ControlLocalProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5)
)


class _ControlLocalPropertiesDeviceType_Type(Integer32):
    """Custom type controlLocalPropertiesDeviceType based on Integer32"""
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
        *(("unknown", 0),
          ("vedge", 1),
          ("vhub", 2),
          ("vsmart", 3),
          ("vbond", 4),
          ("vmanage", 5),
          ("ztp", 6),
          ("vcontainer", 7))
    )


_ControlLocalPropertiesDeviceType_Type.__name__ = "Integer32"
_ControlLocalPropertiesDeviceType_Object = MibScalar
controlLocalPropertiesDeviceType = _ControlLocalPropertiesDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 1),
    _ControlLocalPropertiesDeviceType_Type()
)
controlLocalPropertiesDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesDeviceType.setStatus("current")


class _ControlLocalPropertiesOrganizationName_Type(String):
    """Custom type controlLocalPropertiesOrganizationName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ControlLocalPropertiesOrganizationName_Type.__name__ = "String"
_ControlLocalPropertiesOrganizationName_Object = MibScalar
controlLocalPropertiesOrganizationName = _ControlLocalPropertiesOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 2),
    _ControlLocalPropertiesOrganizationName_Type()
)
controlLocalPropertiesOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesOrganizationName.setStatus("current")
_ControlLocalPropertiesCertificateStatus_Type = String
_ControlLocalPropertiesCertificateStatus_Object = MibScalar
controlLocalPropertiesCertificateStatus = _ControlLocalPropertiesCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 3),
    _ControlLocalPropertiesCertificateStatus_Type()
)
controlLocalPropertiesCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesCertificateStatus.setStatus("current")
_ControlLocalPropertiesRootCaChainStatus_Type = String
_ControlLocalPropertiesRootCaChainStatus_Object = MibScalar
controlLocalPropertiesRootCaChainStatus = _ControlLocalPropertiesRootCaChainStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 4),
    _ControlLocalPropertiesRootCaChainStatus_Type()
)
controlLocalPropertiesRootCaChainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesRootCaChainStatus.setStatus("current")
_ControlLocalPropertiesCertificateValidity_Type = String
_ControlLocalPropertiesCertificateValidity_Object = MibScalar
controlLocalPropertiesCertificateValidity = _ControlLocalPropertiesCertificateValidity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 5),
    _ControlLocalPropertiesCertificateValidity_Type()
)
controlLocalPropertiesCertificateValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesCertificateValidity.setStatus("current")
_ControlLocalPropertiesCertificateNotValidBefore_Type = String
_ControlLocalPropertiesCertificateNotValidBefore_Object = MibScalar
controlLocalPropertiesCertificateNotValidBefore = _ControlLocalPropertiesCertificateNotValidBefore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 6),
    _ControlLocalPropertiesCertificateNotValidBefore_Type()
)
controlLocalPropertiesCertificateNotValidBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesCertificateNotValidBefore.setStatus("current")
_ControlLocalPropertiesCertificateNotValidAfter_Type = String
_ControlLocalPropertiesCertificateNotValidAfter_Object = MibScalar
controlLocalPropertiesCertificateNotValidAfter = _ControlLocalPropertiesCertificateNotValidAfter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 7),
    _ControlLocalPropertiesCertificateNotValidAfter_Type()
)
controlLocalPropertiesCertificateNotValidAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesCertificateNotValidAfter.setStatus("current")
_ControlLocalPropertiesDnsName_Type = String
_ControlLocalPropertiesDnsName_Object = MibScalar
controlLocalPropertiesDnsName = _ControlLocalPropertiesDnsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 8),
    _ControlLocalPropertiesDnsName_Type()
)
controlLocalPropertiesDnsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesDnsName.setStatus("current")
_ControlLocalPropertiesSiteId_Type = Unsigned32
_ControlLocalPropertiesSiteId_Object = MibScalar
controlLocalPropertiesSiteId = _ControlLocalPropertiesSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 9),
    _ControlLocalPropertiesSiteId_Type()
)
controlLocalPropertiesSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesSiteId.setStatus("current")
_ControlLocalPropertiesDomainId_Type = Unsigned32
_ControlLocalPropertiesDomainId_Object = MibScalar
controlLocalPropertiesDomainId = _ControlLocalPropertiesDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 10),
    _ControlLocalPropertiesDomainId_Type()
)
controlLocalPropertiesDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesDomainId.setStatus("current")
_ControlLocalPropertiesTlsPort_Type = Unsigned32
_ControlLocalPropertiesTlsPort_Object = MibScalar
controlLocalPropertiesTlsPort = _ControlLocalPropertiesTlsPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 12),
    _ControlLocalPropertiesTlsPort_Type()
)
controlLocalPropertiesTlsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesTlsPort.setStatus("current")
_ControlLocalPropertiesSystemIp_Type = InetAddressIP
_ControlLocalPropertiesSystemIp_Object = MibScalar
controlLocalPropertiesSystemIp = _ControlLocalPropertiesSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 13),
    _ControlLocalPropertiesSystemIp_Type()
)
controlLocalPropertiesSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesSystemIp.setStatus("current")
_ControlLocalPropertiesUuid_Type = String
_ControlLocalPropertiesUuid_Object = MibScalar
controlLocalPropertiesUuid = _ControlLocalPropertiesUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 14),
    _ControlLocalPropertiesUuid_Type()
)
controlLocalPropertiesUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesUuid.setStatus("current")


class _ControlLocalPropertiesBoardSerial_Type(String):
    """Custom type controlLocalPropertiesBoardSerial based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlLocalPropertiesBoardSerial_Type.__name__ = "String"
_ControlLocalPropertiesBoardSerial_Object = MibScalar
controlLocalPropertiesBoardSerial = _ControlLocalPropertiesBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 15),
    _ControlLocalPropertiesBoardSerial_Type()
)
controlLocalPropertiesBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesBoardSerial.setStatus("current")
_ControlLocalPropertiesRegisterInterval_Type = String
_ControlLocalPropertiesRegisterInterval_Object = MibScalar
controlLocalPropertiesRegisterInterval = _ControlLocalPropertiesRegisterInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 16),
    _ControlLocalPropertiesRegisterInterval_Type()
)
controlLocalPropertiesRegisterInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesRegisterInterval.setStatus("current")
_ControlLocalPropertiesRetryInterval_Type = String
_ControlLocalPropertiesRetryInterval_Object = MibScalar
controlLocalPropertiesRetryInterval = _ControlLocalPropertiesRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 17),
    _ControlLocalPropertiesRetryInterval_Type()
)
controlLocalPropertiesRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesRetryInterval.setStatus("current")
_ControlLocalPropertiesNoActivity_Type = String
_ControlLocalPropertiesNoActivity_Object = MibScalar
controlLocalPropertiesNoActivity = _ControlLocalPropertiesNoActivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 18),
    _ControlLocalPropertiesNoActivity_Type()
)
controlLocalPropertiesNoActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesNoActivity.setStatus("current")
_ControlLocalPropertiesDnsCacheFlushInterval_Type = String
_ControlLocalPropertiesDnsCacheFlushInterval_Object = MibScalar
controlLocalPropertiesDnsCacheFlushInterval = _ControlLocalPropertiesDnsCacheFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 19),
    _ControlLocalPropertiesDnsCacheFlushInterval_Type()
)
controlLocalPropertiesDnsCacheFlushInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesDnsCacheFlushInterval.setStatus("current")
_ControlLocalPropertiesPortHopped_Type = String
_ControlLocalPropertiesPortHopped_Object = MibScalar
controlLocalPropertiesPortHopped = _ControlLocalPropertiesPortHopped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 20),
    _ControlLocalPropertiesPortHopped_Type()
)
controlLocalPropertiesPortHopped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesPortHopped.setStatus("current")
_ControlLocalPropertiesTimeSincePortHop_Type = String
_ControlLocalPropertiesTimeSincePortHop_Object = MibScalar
controlLocalPropertiesTimeSincePortHop = _ControlLocalPropertiesTimeSincePortHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 21),
    _ControlLocalPropertiesTimeSincePortHop_Type()
)
controlLocalPropertiesTimeSincePortHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesTimeSincePortHop.setStatus("current")
_ControlLocalPropertiesMaxControllers_Type = UnsignedByte
_ControlLocalPropertiesMaxControllers_Object = MibScalar
controlLocalPropertiesMaxControllers = _ControlLocalPropertiesMaxControllers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 22),
    _ControlLocalPropertiesMaxControllers_Type()
)
controlLocalPropertiesMaxControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesMaxControllers.setStatus("current")
_ControlLocalPropertiesKeygenInterval_Type = String
_ControlLocalPropertiesKeygenInterval_Object = MibScalar
controlLocalPropertiesKeygenInterval = _ControlLocalPropertiesKeygenInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 23),
    _ControlLocalPropertiesKeygenInterval_Type()
)
controlLocalPropertiesKeygenInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesKeygenInterval.setStatus("current")
_ControlLocalPropertiesIpAddressListTable_Object = MibTable
controlLocalPropertiesIpAddressListTable = _ControlLocalPropertiesIpAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 24)
)
if mibBuilder.loadTexts:
    controlLocalPropertiesIpAddressListTable.setStatus("current")
_ControlLocalPropertiesIpAddressListEntry_Object = MibTableRow
controlLocalPropertiesIpAddressListEntry = _ControlLocalPropertiesIpAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 24, 1)
)
controlLocalPropertiesIpAddressListEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesIpAddressListIndex"),
)
if mibBuilder.loadTexts:
    controlLocalPropertiesIpAddressListEntry.setStatus("current")
_ControlLocalPropertiesIpAddressListIndex_Type = Unsigned32
_ControlLocalPropertiesIpAddressListIndex_Object = MibTableColumn
controlLocalPropertiesIpAddressListIndex = _ControlLocalPropertiesIpAddressListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 24, 1, 1),
    _ControlLocalPropertiesIpAddressListIndex_Type()
)
controlLocalPropertiesIpAddressListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlLocalPropertiesIpAddressListIndex.setStatus("current")
_ControlLocalPropertiesIpAddressListIp_Type = InetAddressIP
_ControlLocalPropertiesIpAddressListIp_Object = MibTableColumn
controlLocalPropertiesIpAddressListIp = _ControlLocalPropertiesIpAddressListIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 24, 1, 2),
    _ControlLocalPropertiesIpAddressListIp_Type()
)
controlLocalPropertiesIpAddressListIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesIpAddressListIp.setStatus("current")
_ControlLocalPropertiesIpAddressListPort_Type = Unsigned32
_ControlLocalPropertiesIpAddressListPort_Object = MibTableColumn
controlLocalPropertiesIpAddressListPort = _ControlLocalPropertiesIpAddressListPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 24, 1, 3),
    _ControlLocalPropertiesIpAddressListPort_Type()
)
controlLocalPropertiesIpAddressListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesIpAddressListPort.setStatus("current")
_ControlLocalPropertiesNumberVbondPeers_Type = Unsigned32
_ControlLocalPropertiesNumberVbondPeers_Object = MibScalar
controlLocalPropertiesNumberVbondPeers = _ControlLocalPropertiesNumberVbondPeers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 25),
    _ControlLocalPropertiesNumberVbondPeers_Type()
)
controlLocalPropertiesNumberVbondPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesNumberVbondPeers.setStatus("current")
_ControlLocalPropertiesVbondAddressListTable_Object = MibTable
controlLocalPropertiesVbondAddressListTable = _ControlLocalPropertiesVbondAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 26)
)
if mibBuilder.loadTexts:
    controlLocalPropertiesVbondAddressListTable.setStatus("current")
_ControlLocalPropertiesVbondAddressListEntry_Object = MibTableRow
controlLocalPropertiesVbondAddressListEntry = _ControlLocalPropertiesVbondAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 26, 1)
)
controlLocalPropertiesVbondAddressListEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesVbondAddressListIndex"),
)
if mibBuilder.loadTexts:
    controlLocalPropertiesVbondAddressListEntry.setStatus("current")
_ControlLocalPropertiesVbondAddressListIndex_Type = Unsigned32
_ControlLocalPropertiesVbondAddressListIndex_Object = MibTableColumn
controlLocalPropertiesVbondAddressListIndex = _ControlLocalPropertiesVbondAddressListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 26, 1, 1),
    _ControlLocalPropertiesVbondAddressListIndex_Type()
)
controlLocalPropertiesVbondAddressListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlLocalPropertiesVbondAddressListIndex.setStatus("current")
_ControlLocalPropertiesVbondAddressListIp_Type = InetAddressIP
_ControlLocalPropertiesVbondAddressListIp_Object = MibTableColumn
controlLocalPropertiesVbondAddressListIp = _ControlLocalPropertiesVbondAddressListIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 26, 1, 2),
    _ControlLocalPropertiesVbondAddressListIp_Type()
)
controlLocalPropertiesVbondAddressListIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesVbondAddressListIp.setStatus("current")
_ControlLocalPropertiesVbondAddressListPort_Type = Unsigned32
_ControlLocalPropertiesVbondAddressListPort_Object = MibTableColumn
controlLocalPropertiesVbondAddressListPort = _ControlLocalPropertiesVbondAddressListPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 26, 1, 3),
    _ControlLocalPropertiesVbondAddressListPort_Type()
)
controlLocalPropertiesVbondAddressListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesVbondAddressListPort.setStatus("current")
_ControlLocalPropertiesNumberActiveWanInterfaces_Type = Unsigned32
_ControlLocalPropertiesNumberActiveWanInterfaces_Object = MibScalar
controlLocalPropertiesNumberActiveWanInterfaces = _ControlLocalPropertiesNumberActiveWanInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 27),
    _ControlLocalPropertiesNumberActiveWanInterfaces_Type()
)
controlLocalPropertiesNumberActiveWanInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesNumberActiveWanInterfaces.setStatus("current")
_ControlLocalPropertiesWanInterfaceListTable_Object = MibTable
controlLocalPropertiesWanInterfaceListTable = _ControlLocalPropertiesWanInterfaceListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28)
)
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListTable.setStatus("current")
_ControlLocalPropertiesWanInterfaceListEntry_Object = MibTableRow
controlLocalPropertiesWanInterfaceListEntry = _ControlLocalPropertiesWanInterfaceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1)
)
controlLocalPropertiesWanInterfaceListEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListIndex"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListInstance"),
)
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListEntry.setStatus("current")
_ControlLocalPropertiesWanInterfaceListIndex_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListIndex_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListIndex = _ControlLocalPropertiesWanInterfaceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 1),
    _ControlLocalPropertiesWanInterfaceListIndex_Type()
)
controlLocalPropertiesWanInterfaceListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListIndex.setStatus("current")


class _ControlLocalPropertiesWanInterfaceListInterface_Type(String):
    """Custom type controlLocalPropertiesWanInterfaceListInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ControlLocalPropertiesWanInterfaceListInterface_Type.__name__ = "String"
_ControlLocalPropertiesWanInterfaceListInterface_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListInterface = _ControlLocalPropertiesWanInterfaceListInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 2),
    _ControlLocalPropertiesWanInterfaceListInterface_Type()
)
controlLocalPropertiesWanInterfaceListInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListInterface.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPublicIp_Type = InetAddressIP
_ControlLocalPropertiesWanInterfaceListPublicIp_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPublicIp = _ControlLocalPropertiesWanInterfaceListPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 3),
    _ControlLocalPropertiesWanInterfaceListPublicIp_Type()
)
controlLocalPropertiesWanInterfaceListPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPublicIp.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPublicPort_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListPublicPort_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPublicPort = _ControlLocalPropertiesWanInterfaceListPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 4),
    _ControlLocalPropertiesWanInterfaceListPublicPort_Type()
)
controlLocalPropertiesWanInterfaceListPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPublicPort.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPrivateIp_Type = InetAddressIP
_ControlLocalPropertiesWanInterfaceListPrivateIp_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPrivateIp = _ControlLocalPropertiesWanInterfaceListPrivateIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 5),
    _ControlLocalPropertiesWanInterfaceListPrivateIp_Type()
)
controlLocalPropertiesWanInterfaceListPrivateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPrivateIp.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPrivatePort_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListPrivatePort_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPrivatePort = _ControlLocalPropertiesWanInterfaceListPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 6),
    _ControlLocalPropertiesWanInterfaceListPrivatePort_Type()
)
controlLocalPropertiesWanInterfaceListPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPrivatePort.setStatus("current")
_ControlLocalPropertiesWanInterfaceListNumVsmarts_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListNumVsmarts_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListNumVsmarts = _ControlLocalPropertiesWanInterfaceListNumVsmarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 7),
    _ControlLocalPropertiesWanInterfaceListNumVsmarts_Type()
)
controlLocalPropertiesWanInterfaceListNumVsmarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListNumVsmarts.setStatus("current")
_ControlLocalPropertiesWanInterfaceListNumVmanages_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListNumVmanages_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListNumVmanages = _ControlLocalPropertiesWanInterfaceListNumVmanages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 8),
    _ControlLocalPropertiesWanInterfaceListNumVmanages_Type()
)
controlLocalPropertiesWanInterfaceListNumVmanages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListNumVmanages.setStatus("current")
_ControlLocalPropertiesWanInterfaceListWeight_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListWeight_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListWeight = _ControlLocalPropertiesWanInterfaceListWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 9),
    _ControlLocalPropertiesWanInterfaceListWeight_Type()
)
controlLocalPropertiesWanInterfaceListWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListWeight.setStatus("current")


class _ControlLocalPropertiesWanInterfaceListColor_Type(Integer32):
    """Custom type controlLocalPropertiesWanInterfaceListColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bonze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_ControlLocalPropertiesWanInterfaceListColor_Type.__name__ = "Integer32"
_ControlLocalPropertiesWanInterfaceListColor_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListColor = _ControlLocalPropertiesWanInterfaceListColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 10),
    _ControlLocalPropertiesWanInterfaceListColor_Type()
)
controlLocalPropertiesWanInterfaceListColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListColor.setStatus("current")


class _ControlLocalPropertiesWanInterfaceListCarrier_Type(Integer32):
    """Custom type controlLocalPropertiesWanInterfaceListCarrier based on Integer32"""
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
        *(("default", 1),
          ("carrier1", 2),
          ("carrier2", 3),
          ("carrier3", 4),
          ("carrier4", 5),
          ("carrier5", 6),
          ("carrier6", 7),
          ("carrier7", 8),
          ("carrier8", 9))
    )


_ControlLocalPropertiesWanInterfaceListCarrier_Type.__name__ = "Integer32"
_ControlLocalPropertiesWanInterfaceListCarrier_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListCarrier = _ControlLocalPropertiesWanInterfaceListCarrier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 11),
    _ControlLocalPropertiesWanInterfaceListCarrier_Type()
)
controlLocalPropertiesWanInterfaceListCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListCarrier.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPreference_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListPreference_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPreference = _ControlLocalPropertiesWanInterfaceListPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 12),
    _ControlLocalPropertiesWanInterfaceListPreference_Type()
)
controlLocalPropertiesWanInterfaceListPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPreference.setStatus("current")


class _ControlLocalPropertiesWanInterfaceListAdminState_Type(Integer32):
    """Custom type controlLocalPropertiesWanInterfaceListAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )


_ControlLocalPropertiesWanInterfaceListAdminState_Type.__name__ = "Integer32"
_ControlLocalPropertiesWanInterfaceListAdminState_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListAdminState = _ControlLocalPropertiesWanInterfaceListAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 13),
    _ControlLocalPropertiesWanInterfaceListAdminState_Type()
)
controlLocalPropertiesWanInterfaceListAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListAdminState.setStatus("current")


class _ControlLocalPropertiesWanInterfaceListOperationState_Type(Integer32):
    """Custom type controlLocalPropertiesWanInterfaceListOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )


_ControlLocalPropertiesWanInterfaceListOperationState_Type.__name__ = "Integer32"
_ControlLocalPropertiesWanInterfaceListOperationState_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListOperationState = _ControlLocalPropertiesWanInterfaceListOperationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 14),
    _ControlLocalPropertiesWanInterfaceListOperationState_Type()
)
controlLocalPropertiesWanInterfaceListOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListOperationState.setStatus("current")
_ControlLocalPropertiesWanInterfaceListLastConnTime_Type = String
_ControlLocalPropertiesWanInterfaceListLastConnTime_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListLastConnTime = _ControlLocalPropertiesWanInterfaceListLastConnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 15),
    _ControlLocalPropertiesWanInterfaceListLastConnTime_Type()
)
controlLocalPropertiesWanInterfaceListLastConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListLastConnTime.setStatus("current")
_ControlLocalPropertiesWanInterfaceListRestrictStr_Type = String
_ControlLocalPropertiesWanInterfaceListRestrictStr_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListRestrictStr = _ControlLocalPropertiesWanInterfaceListRestrictStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 16),
    _ControlLocalPropertiesWanInterfaceListRestrictStr_Type()
)
controlLocalPropertiesWanInterfaceListRestrictStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListRestrictStr.setStatus("current")
_ControlLocalPropertiesWanInterfaceListControlStr_Type = String
_ControlLocalPropertiesWanInterfaceListControlStr_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListControlStr = _ControlLocalPropertiesWanInterfaceListControlStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 17),
    _ControlLocalPropertiesWanInterfaceListControlStr_Type()
)
controlLocalPropertiesWanInterfaceListControlStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListControlStr.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPerWanMaxControllers_Type = UnsignedByte
_ControlLocalPropertiesWanInterfaceListPerWanMaxControllers_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPerWanMaxControllers = _ControlLocalPropertiesWanInterfaceListPerWanMaxControllers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 18),
    _ControlLocalPropertiesWanInterfaceListPerWanMaxControllers_Type()
)
controlLocalPropertiesWanInterfaceListPerWanMaxControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPerWanMaxControllers.setStatus("current")
_ControlLocalPropertiesWanInterfaceListInstance_Type = Unsigned32
_ControlLocalPropertiesWanInterfaceListInstance_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListInstance = _ControlLocalPropertiesWanInterfaceListInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 19),
    _ControlLocalPropertiesWanInterfaceListInstance_Type()
)
controlLocalPropertiesWanInterfaceListInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListInstance.setStatus("current")
_ControlLocalPropertiesWanInterfaceListPrivateIpv6_Type = InetAddressIP
_ControlLocalPropertiesWanInterfaceListPrivateIpv6_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListPrivateIpv6 = _ControlLocalPropertiesWanInterfaceListPrivateIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 20),
    _ControlLocalPropertiesWanInterfaceListPrivateIpv6_Type()
)
controlLocalPropertiesWanInterfaceListPrivateIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListPrivateIpv6.setStatus("current")
_ControlLocalPropertiesWanInterfaceListSpiChange_Type = String
_ControlLocalPropertiesWanInterfaceListSpiChange_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListSpiChange = _ControlLocalPropertiesWanInterfaceListSpiChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 21),
    _ControlLocalPropertiesWanInterfaceListSpiChange_Type()
)
controlLocalPropertiesWanInterfaceListSpiChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListSpiChange.setStatus("current")
_ControlLocalPropertiesWanInterfaceListLastResort_Type = String
_ControlLocalPropertiesWanInterfaceListLastResort_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListLastResort = _ControlLocalPropertiesWanInterfaceListLastResort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 22),
    _ControlLocalPropertiesWanInterfaceListLastResort_Type()
)
controlLocalPropertiesWanInterfaceListLastResort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListLastResort.setStatus("current")
_ControlLocalPropertiesWanInterfaceListWanPortHopped_Type = String
_ControlLocalPropertiesWanInterfaceListWanPortHopped_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListWanPortHopped = _ControlLocalPropertiesWanInterfaceListWanPortHopped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 23),
    _ControlLocalPropertiesWanInterfaceListWanPortHopped_Type()
)
controlLocalPropertiesWanInterfaceListWanPortHopped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListWanPortHopped.setStatus("current")
_ControlLocalPropertiesWanInterfaceListWanTimeSincePortHop_Type = String
_ControlLocalPropertiesWanInterfaceListWanTimeSincePortHop_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListWanTimeSincePortHop = _ControlLocalPropertiesWanInterfaceListWanTimeSincePortHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 24),
    _ControlLocalPropertiesWanInterfaceListWanTimeSincePortHop_Type()
)
controlLocalPropertiesWanInterfaceListWanTimeSincePortHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListWanTimeSincePortHop.setStatus("current")
_ControlLocalPropertiesWanInterfaceListVbondAsStunServer_Type = String
_ControlLocalPropertiesWanInterfaceListVbondAsStunServer_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListVbondAsStunServer = _ControlLocalPropertiesWanInterfaceListVbondAsStunServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 25),
    _ControlLocalPropertiesWanInterfaceListVbondAsStunServer_Type()
)
controlLocalPropertiesWanInterfaceListVbondAsStunServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListVbondAsStunServer.setStatus("current")
_ControlLocalPropertiesWanInterfaceListVmanageConnPreference_Type = UnsignedByte
_ControlLocalPropertiesWanInterfaceListVmanageConnPreference_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListVmanageConnPreference = _ControlLocalPropertiesWanInterfaceListVmanageConnPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 26),
    _ControlLocalPropertiesWanInterfaceListVmanageConnPreference_Type()
)
controlLocalPropertiesWanInterfaceListVmanageConnPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListVmanageConnPreference.setStatus("current")
_ControlLocalPropertiesWanInterfaceListLowBandwidthLink_Type = String
_ControlLocalPropertiesWanInterfaceListLowBandwidthLink_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListLowBandwidthLink = _ControlLocalPropertiesWanInterfaceListLowBandwidthLink_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 27),
    _ControlLocalPropertiesWanInterfaceListLowBandwidthLink_Type()
)
controlLocalPropertiesWanInterfaceListLowBandwidthLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListLowBandwidthLink.setStatus("current")
_ControlLocalPropertiesWanInterfaceListNatType_Type = String
_ControlLocalPropertiesWanInterfaceListNatType_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListNatType = _ControlLocalPropertiesWanInterfaceListNatType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 31),
    _ControlLocalPropertiesWanInterfaceListNatType_Type()
)
controlLocalPropertiesWanInterfaceListNatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListNatType.setStatus("current")


class _ControlLocalPropertiesWanInterfaceListInterfaceAdminState_Type(Integer32):
    """Custom type controlLocalPropertiesWanInterfaceListInterfaceAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )


_ControlLocalPropertiesWanInterfaceListInterfaceAdminState_Type.__name__ = "Integer32"
_ControlLocalPropertiesWanInterfaceListInterfaceAdminState_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListInterfaceAdminState = _ControlLocalPropertiesWanInterfaceListInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 32),
    _ControlLocalPropertiesWanInterfaceListInterfaceAdminState_Type()
)
controlLocalPropertiesWanInterfaceListInterfaceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListInterfaceAdminState.setStatus("current")


class _ControlLocalPropertiesWanInterfaceListInterfaceOperState_Type(Integer32):
    """Custom type controlLocalPropertiesWanInterfaceListInterfaceOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )


_ControlLocalPropertiesWanInterfaceListInterfaceOperState_Type.__name__ = "Integer32"
_ControlLocalPropertiesWanInterfaceListInterfaceOperState_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListInterfaceOperState = _ControlLocalPropertiesWanInterfaceListInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 33),
    _ControlLocalPropertiesWanInterfaceListInterfaceOperState_Type()
)
controlLocalPropertiesWanInterfaceListInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListInterfaceOperState.setStatus("current")
_ControlLocalPropertiesWanInterfaceListRegionId_Type = String
_ControlLocalPropertiesWanInterfaceListRegionId_Object = MibTableColumn
controlLocalPropertiesWanInterfaceListRegionId = _ControlLocalPropertiesWanInterfaceListRegionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 28, 1, 34),
    _ControlLocalPropertiesWanInterfaceListRegionId_Type()
)
controlLocalPropertiesWanInterfaceListRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesWanInterfaceListRegionId.setStatus("current")
_ControlLocalPropertiesVsmartListVersion_Type = Counter64
_ControlLocalPropertiesVsmartListVersion_Object = MibScalar
controlLocalPropertiesVsmartListVersion = _ControlLocalPropertiesVsmartListVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 30),
    _ControlLocalPropertiesVsmartListVersion_Type()
)
controlLocalPropertiesVsmartListVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesVsmartListVersion.setStatus("current")


class _ControlLocalPropertiesSPOrganizationName_Type(String):
    """Custom type controlLocalPropertiesSPOrganizationName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ControlLocalPropertiesSPOrganizationName_Type.__name__ = "String"
_ControlLocalPropertiesSPOrganizationName_Object = MibScalar
controlLocalPropertiesSPOrganizationName = _ControlLocalPropertiesSPOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 31),
    _ControlLocalPropertiesSPOrganizationName_Type()
)
controlLocalPropertiesSPOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesSPOrganizationName.setStatus("current")


class _ControlLocalPropertiesToken_Type(String):
    """Custom type controlLocalPropertiesToken based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlLocalPropertiesToken_Type.__name__ = "String"
_ControlLocalPropertiesToken_Object = MibScalar
controlLocalPropertiesToken = _ControlLocalPropertiesToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 32),
    _ControlLocalPropertiesToken_Type()
)
controlLocalPropertiesToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesToken.setStatus("current")
_ControlLocalPropertiesEmbargoCheck_Type = String
_ControlLocalPropertiesEmbargoCheck_Object = MibScalar
controlLocalPropertiesEmbargoCheck = _ControlLocalPropertiesEmbargoCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 34),
    _ControlLocalPropertiesEmbargoCheck_Type()
)
controlLocalPropertiesEmbargoCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEmbargoCheck.setStatus("current")
_ControlLocalPropertiesEnterpriseSerial_Type = String
_ControlLocalPropertiesEnterpriseSerial_Object = MibScalar
controlLocalPropertiesEnterpriseSerial = _ControlLocalPropertiesEnterpriseSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 35),
    _ControlLocalPropertiesEnterpriseSerial_Type()
)
controlLocalPropertiesEnterpriseSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEnterpriseSerial.setStatus("current")
_ControlLocalPropertiesEnterpriseCertificateStatus_Type = String
_ControlLocalPropertiesEnterpriseCertificateStatus_Object = MibScalar
controlLocalPropertiesEnterpriseCertificateStatus = _ControlLocalPropertiesEnterpriseCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 36),
    _ControlLocalPropertiesEnterpriseCertificateStatus_Type()
)
controlLocalPropertiesEnterpriseCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEnterpriseCertificateStatus.setStatus("current")
_ControlLocalPropertiesEnterpriseCertificateValidity_Type = String
_ControlLocalPropertiesEnterpriseCertificateValidity_Object = MibScalar
controlLocalPropertiesEnterpriseCertificateValidity = _ControlLocalPropertiesEnterpriseCertificateValidity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 37),
    _ControlLocalPropertiesEnterpriseCertificateValidity_Type()
)
controlLocalPropertiesEnterpriseCertificateValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEnterpriseCertificateValidity.setStatus("current")
_ControlLocalPropertiesEnterpriseCertificateNotValidBefore_Type = String
_ControlLocalPropertiesEnterpriseCertificateNotValidBefore_Object = MibScalar
controlLocalPropertiesEnterpriseCertificateNotValidBefore = _ControlLocalPropertiesEnterpriseCertificateNotValidBefore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 38),
    _ControlLocalPropertiesEnterpriseCertificateNotValidBefore_Type()
)
controlLocalPropertiesEnterpriseCertificateNotValidBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEnterpriseCertificateNotValidBefore.setStatus("current")
_ControlLocalPropertiesEnterpriseCertificateNotValidAfter_Type = String
_ControlLocalPropertiesEnterpriseCertificateNotValidAfter_Object = MibScalar
controlLocalPropertiesEnterpriseCertificateNotValidAfter = _ControlLocalPropertiesEnterpriseCertificateNotValidAfter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 39),
    _ControlLocalPropertiesEnterpriseCertificateNotValidAfter_Type()
)
controlLocalPropertiesEnterpriseCertificateNotValidAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesEnterpriseCertificateNotValidAfter.setStatus("current")
_ControlLocalPropertiesRootCaCrlStatus_Type = String
_ControlLocalPropertiesRootCaCrlStatus_Object = MibScalar
controlLocalPropertiesRootCaCrlStatus = _ControlLocalPropertiesRootCaCrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 40),
    _ControlLocalPropertiesRootCaCrlStatus_Type()
)
controlLocalPropertiesRootCaCrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesRootCaCrlStatus.setStatus("current")
_ControlLocalPropertiesPairwiseKeying_Type = String
_ControlLocalPropertiesPairwiseKeying_Object = MibScalar
controlLocalPropertiesPairwiseKeying = _ControlLocalPropertiesPairwiseKeying_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 41),
    _ControlLocalPropertiesPairwiseKeying_Type()
)
controlLocalPropertiesPairwiseKeying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesPairwiseKeying.setStatus("current")


class _ControlLocalPropertiesSubjectSerialNumber_Type(String):
    """Custom type controlLocalPropertiesSubjectSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_ControlLocalPropertiesSubjectSerialNumber_Type.__name__ = "String"
_ControlLocalPropertiesSubjectSerialNumber_Object = MibScalar
controlLocalPropertiesSubjectSerialNumber = _ControlLocalPropertiesSubjectSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 42),
    _ControlLocalPropertiesSubjectSerialNumber_Type()
)
controlLocalPropertiesSubjectSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesSubjectSerialNumber.setStatus("current")
_ControlLocalPropertiesProtocol_Type = ControlProtocolEnum
_ControlLocalPropertiesProtocol_Object = MibScalar
controlLocalPropertiesProtocol = _ControlLocalPropertiesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 5, 43),
    _ControlLocalPropertiesProtocol_Type()
)
controlLocalPropertiesProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlLocalPropertiesProtocol.setStatus("current")
_ControlValidVsmartsTable_Object = MibTable
controlValidVsmartsTable = _ControlValidVsmartsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 6)
)
if mibBuilder.loadTexts:
    controlValidVsmartsTable.setStatus("current")
_ControlValidVsmartsEntry_Object = MibTableRow
controlValidVsmartsEntry = _ControlValidVsmartsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 6, 1)
)
controlValidVsmartsEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlValidVsmartsSerialNumber"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlValidVsmartsOrg"),
)
if mibBuilder.loadTexts:
    controlValidVsmartsEntry.setStatus("current")


class _ControlValidVsmartsSerialNumber_Type(String):
    """Custom type controlValidVsmartsSerialNumber based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlValidVsmartsSerialNumber_Type.__name__ = "String"
_ControlValidVsmartsSerialNumber_Object = MibTableColumn
controlValidVsmartsSerialNumber = _ControlValidVsmartsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 6, 1, 1),
    _ControlValidVsmartsSerialNumber_Type()
)
controlValidVsmartsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlValidVsmartsSerialNumber.setStatus("current")


class _ControlValidVsmartsOrg_Type(String):
    """Custom type controlValidVsmartsOrg based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ControlValidVsmartsOrg_Type.__name__ = "String"
_ControlValidVsmartsOrg_Object = MibTableColumn
controlValidVsmartsOrg = _ControlValidVsmartsOrg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 6, 1, 2),
    _ControlValidVsmartsOrg_Type()
)
controlValidVsmartsOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlValidVsmartsOrg.setStatus("current")
_ControlSummaryTable_Object = MibTable
controlSummaryTable = _ControlSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8)
)
if mibBuilder.loadTexts:
    controlSummaryTable.setStatus("current")
_ControlSummaryEntry_Object = MibTableRow
controlSummaryEntry = _ControlSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1)
)
controlSummaryEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlSummaryInstance"),
)
if mibBuilder.loadTexts:
    controlSummaryEntry.setStatus("current")
_ControlSummaryInstance_Type = Unsigned32
_ControlSummaryInstance_Object = MibTableColumn
controlSummaryInstance = _ControlSummaryInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1, 1),
    _ControlSummaryInstance_Type()
)
controlSummaryInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSummaryInstance.setStatus("current")
_ControlSummaryVbondCounts_Type = UnsignedShort
_ControlSummaryVbondCounts_Object = MibTableColumn
controlSummaryVbondCounts = _ControlSummaryVbondCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1, 2),
    _ControlSummaryVbondCounts_Type()
)
controlSummaryVbondCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryVbondCounts.setStatus("current")
_ControlSummaryVmanageCounts_Type = UnsignedShort
_ControlSummaryVmanageCounts_Object = MibTableColumn
controlSummaryVmanageCounts = _ControlSummaryVmanageCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1, 3),
    _ControlSummaryVmanageCounts_Type()
)
controlSummaryVmanageCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryVmanageCounts.setStatus("current")
_ControlSummaryVsmartCounts_Type = UnsignedShort
_ControlSummaryVsmartCounts_Object = MibTableColumn
controlSummaryVsmartCounts = _ControlSummaryVsmartCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1, 4),
    _ControlSummaryVsmartCounts_Type()
)
controlSummaryVsmartCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryVsmartCounts.setStatus("current")
_ControlSummaryVedgeCounts_Type = UnsignedShort
_ControlSummaryVedgeCounts_Object = MibTableColumn
controlSummaryVedgeCounts = _ControlSummaryVedgeCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1, 5),
    _ControlSummaryVedgeCounts_Type()
)
controlSummaryVedgeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryVedgeCounts.setStatus("current")


class _ControlSummaryProtocol_Type(Integer32):
    """Custom type controlSummaryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dtls", 0),
          ("tls", 1))
    )


_ControlSummaryProtocol_Type.__name__ = "Integer32"
_ControlSummaryProtocol_Object = MibTableColumn
controlSummaryProtocol = _ControlSummaryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1, 6),
    _ControlSummaryProtocol_Type()
)
controlSummaryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryProtocol.setStatus("current")
_ControlSummaryListeningIp_Type = InetAddressIP
_ControlSummaryListeningIp_Object = MibTableColumn
controlSummaryListeningIp = _ControlSummaryListeningIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1, 7),
    _ControlSummaryListeningIp_Type()
)
controlSummaryListeningIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryListeningIp.setStatus("current")
_ControlSummaryListeningPort_Type = Unsigned32
_ControlSummaryListeningPort_Object = MibTableColumn
controlSummaryListeningPort = _ControlSummaryListeningPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1, 8),
    _ControlSummaryListeningPort_Type()
)
controlSummaryListeningPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryListeningPort.setStatus("current")
_ControlSummaryListeningIpv6_Type = InetAddressIP
_ControlSummaryListeningIpv6_Object = MibTableColumn
controlSummaryListeningIpv6 = _ControlSummaryListeningIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1, 9),
    _ControlSummaryListeningIpv6_Type()
)
controlSummaryListeningIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryListeningIpv6.setStatus("current")
_ControlSummaryValidControllerCounts_Type = UnsignedShort
_ControlSummaryValidControllerCounts_Object = MibTableColumn
controlSummaryValidControllerCounts = _ControlSummaryValidControllerCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 8, 1, 10),
    _ControlSummaryValidControllerCounts_Type()
)
controlSummaryValidControllerCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSummaryValidControllerCounts.setStatus("current")
_ControlAffinity_ObjectIdentity = ObjectIdentity
controlAffinity = _ControlAffinity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9)
)
_ControlAffinityConfigTable_Object = MibTable
controlAffinityConfigTable = _ControlAffinityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    controlAffinityConfigTable.setStatus("current")
_ControlAffinityConfigEntry_Object = MibTableRow
controlAffinityConfigEntry = _ControlAffinityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 1, 1)
)
controlAffinityConfigEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlAffinityConfigAffcIndex"),
)
if mibBuilder.loadTexts:
    controlAffinityConfigEntry.setStatus("current")
_ControlAffinityConfigAffcIndex_Type = Unsigned32
_ControlAffinityConfigAffcIndex_Object = MibTableColumn
controlAffinityConfigAffcIndex = _ControlAffinityConfigAffcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 1, 1, 1),
    _ControlAffinityConfigAffcIndex_Type()
)
controlAffinityConfigAffcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcIndex.setStatus("current")
_ControlAffinityConfigAffcInterface_Type = String
_ControlAffinityConfigAffcInterface_Object = MibTableColumn
controlAffinityConfigAffcInterface = _ControlAffinityConfigAffcInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 1, 1, 2),
    _ControlAffinityConfigAffcInterface_Type()
)
controlAffinityConfigAffcInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcInterface.setStatus("current")
_ControlAffinityConfigAffcErvc_Type = Unsigned32
_ControlAffinityConfigAffcErvc_Object = MibTableColumn
controlAffinityConfigAffcErvc = _ControlAffinityConfigAffcErvc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 1, 1, 3),
    _ControlAffinityConfigAffcErvc_Type()
)
controlAffinityConfigAffcErvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcErvc.setStatus("current")
_ControlAffinityConfigAffcEcl_Type = String
_ControlAffinityConfigAffcEcl_Object = MibTableColumn
controlAffinityConfigAffcEcl = _ControlAffinityConfigAffcEcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 1, 1, 4),
    _ControlAffinityConfigAffcEcl_Type()
)
controlAffinityConfigAffcEcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcEcl.setStatus("current")
_ControlAffinityConfigAffcCcl_Type = String
_ControlAffinityConfigAffcCcl_Object = MibTableColumn
controlAffinityConfigAffcCcl = _ControlAffinityConfigAffcCcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 1, 1, 5),
    _ControlAffinityConfigAffcCcl_Type()
)
controlAffinityConfigAffcCcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcCcl.setStatus("current")
_ControlAffinityConfigAffcEquil_Type = String
_ControlAffinityConfigAffcEquil_Object = MibTableColumn
controlAffinityConfigAffcEquil = _ControlAffinityConfigAffcEquil_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 1, 1, 6),
    _ControlAffinityConfigAffcEquil_Type()
)
controlAffinityConfigAffcEquil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcEquil.setStatus("current")
_ControlAffinityConfigAffcLastResort_Type = String
_ControlAffinityConfigAffcLastResort_Object = MibTableColumn
controlAffinityConfigAffcLastResort = _ControlAffinityConfigAffcLastResort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 1, 1, 7),
    _ControlAffinityConfigAffcLastResort_Type()
)
controlAffinityConfigAffcLastResort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcLastResort.setStatus("current")
_ControlAffinityConfigAffcTenantCount_Type = UnsignedByte
_ControlAffinityConfigAffcTenantCount_Object = MibTableColumn
controlAffinityConfigAffcTenantCount = _ControlAffinityConfigAffcTenantCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 1, 1, 8),
    _ControlAffinityConfigAffcTenantCount_Type()
)
controlAffinityConfigAffcTenantCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityConfigAffcTenantCount.setStatus("current")
_ControlAffinityStatusTable_Object = MibTable
controlAffinityStatusTable = _ControlAffinityStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    controlAffinityStatusTable.setStatus("current")
_ControlAffinityStatusEntry_Object = MibTableRow
controlAffinityStatusEntry = _ControlAffinityStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 2, 1)
)
controlAffinityStatusEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "controlAffinityStatusAffsIndex"),
)
if mibBuilder.loadTexts:
    controlAffinityStatusEntry.setStatus("current")
_ControlAffinityStatusAffsIndex_Type = Unsigned32
_ControlAffinityStatusAffsIndex_Object = MibTableColumn
controlAffinityStatusAffsIndex = _ControlAffinityStatusAffsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 2, 1, 1),
    _ControlAffinityStatusAffsIndex_Type()
)
controlAffinityStatusAffsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlAffinityStatusAffsIndex.setStatus("current")
_ControlAffinityStatusAffsAcc_Type = String
_ControlAffinityStatusAffsAcc_Object = MibTableColumn
controlAffinityStatusAffsAcc = _ControlAffinityStatusAffsAcc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 2, 1, 2),
    _ControlAffinityStatusAffsAcc_Type()
)
controlAffinityStatusAffsAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityStatusAffsAcc.setStatus("current")
_ControlAffinityStatusAffsInterface_Type = String
_ControlAffinityStatusAffsInterface_Object = MibTableColumn
controlAffinityStatusAffsInterface = _ControlAffinityStatusAffsInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 2, 1, 3),
    _ControlAffinityStatusAffsInterface_Type()
)
controlAffinityStatusAffsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityStatusAffsInterface.setStatus("current")
_ControlAffinityStatusAffsUcc_Type = String
_ControlAffinityStatusAffsUcc_Object = MibTableColumn
controlAffinityStatusAffsUcc = _ControlAffinityStatusAffsUcc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 2, 1, 4),
    _ControlAffinityStatusAffsUcc_Type()
)
controlAffinityStatusAffsUcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityStatusAffsUcc.setStatus("current")
_ControlAffinityStatusAffsAc_Type = String
_ControlAffinityStatusAffsAc_Object = MibTableColumn
controlAffinityStatusAffsAc = _ControlAffinityStatusAffsAc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 2, 9, 2, 1, 5),
    _ControlAffinityStatusAffsAc_Type()
)
controlAffinityStatusAffsAc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlAffinityStatusAffsAc.setStatus("current")
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4)
)
_IpsecLocalSaTable_Object = MibTable
ipsecLocalSaTable = _IpsecLocalSaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipsecLocalSaTable.setStatus("current")
_IpsecLocalSaEntry_Object = MibTableRow
ipsecLocalSaEntry = _IpsecLocalSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1, 1)
)
ipsecLocalSaEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecLocalSaTlocAddress"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecLocalSaTlocColor"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecLocalSaSpi"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecLocalSaTlocIndex"),
)
if mibBuilder.loadTexts:
    ipsecLocalSaEntry.setStatus("current")
_IpsecLocalSaTlocAddress_Type = InetAddressIP
_IpsecLocalSaTlocAddress_Object = MibTableColumn
ipsecLocalSaTlocAddress = _IpsecLocalSaTlocAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1, 1, 1),
    _IpsecLocalSaTlocAddress_Type()
)
ipsecLocalSaTlocAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecLocalSaTlocAddress.setStatus("current")
_IpsecLocalSaTlocColor_Type = ColorEnum
_IpsecLocalSaTlocColor_Object = MibTableColumn
ipsecLocalSaTlocColor = _IpsecLocalSaTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1, 1, 2),
    _IpsecLocalSaTlocColor_Type()
)
ipsecLocalSaTlocColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecLocalSaTlocColor.setStatus("current")
_IpsecLocalSaSpi_Type = Unsigned32
_IpsecLocalSaSpi_Object = MibTableColumn
ipsecLocalSaSpi = _IpsecLocalSaSpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1, 1, 3),
    _IpsecLocalSaSpi_Type()
)
ipsecLocalSaSpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecLocalSaSpi.setStatus("current")
_IpsecLocalSaTlocIndex_Type = Unsigned32
_IpsecLocalSaTlocIndex_Object = MibTableColumn
ipsecLocalSaTlocIndex = _IpsecLocalSaTlocIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1, 1, 4),
    _IpsecLocalSaTlocIndex_Type()
)
ipsecLocalSaTlocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecLocalSaTlocIndex.setStatus("current")
_IpsecLocalSaIp_Type = InetAddressIP
_IpsecLocalSaIp_Object = MibTableColumn
ipsecLocalSaIp = _IpsecLocalSaIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1, 1, 5),
    _IpsecLocalSaIp_Type()
)
ipsecLocalSaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLocalSaIp.setStatus("current")
_IpsecLocalSaPort_Type = Unsigned32
_IpsecLocalSaPort_Object = MibTableColumn
ipsecLocalSaPort = _IpsecLocalSaPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1, 1, 6),
    _IpsecLocalSaPort_Type()
)
ipsecLocalSaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLocalSaPort.setStatus("current")
_IpsecLocalSaEncryptKeyHash_Type = String
_IpsecLocalSaEncryptKeyHash_Object = MibTableColumn
ipsecLocalSaEncryptKeyHash = _IpsecLocalSaEncryptKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1, 1, 7),
    _IpsecLocalSaEncryptKeyHash_Type()
)
ipsecLocalSaEncryptKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLocalSaEncryptKeyHash.setStatus("current")
_IpsecLocalSaAuthKeyHash_Type = String
_IpsecLocalSaAuthKeyHash_Object = MibTableColumn
ipsecLocalSaAuthKeyHash = _IpsecLocalSaAuthKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1, 1, 8),
    _IpsecLocalSaAuthKeyHash_Type()
)
ipsecLocalSaAuthKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLocalSaAuthKeyHash.setStatus("current")
_IpsecLocalSaIpv6_Type = InetAddressIP
_IpsecLocalSaIpv6_Object = MibTableColumn
ipsecLocalSaIpv6 = _IpsecLocalSaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 1, 1, 9),
    _IpsecLocalSaIpv6_Type()
)
ipsecLocalSaIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecLocalSaIpv6.setStatus("current")
_IpsecInboundConnectionsTable_Object = MibTable
ipsecInboundConnectionsTable = _IpsecInboundConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ipsecInboundConnectionsTable.setStatus("current")
_IpsecInboundConnectionsEntry_Object = MibTableRow
ipsecInboundConnectionsEntry = _IpsecInboundConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1)
)
ipsecInboundConnectionsEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsLocalTlocAddress"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsLocalTlocColor"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsRemoteTlocAddress"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsRemoteTlocColor"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsLocalTlocIndex"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsRemoteTlocIndex"),
)
if mibBuilder.loadTexts:
    ipsecInboundConnectionsEntry.setStatus("current")
_IpsecInboundConnectionsLocalTlocAddress_Type = InetAddressIP
_IpsecInboundConnectionsLocalTlocAddress_Object = MibTableColumn
ipsecInboundConnectionsLocalTlocAddress = _IpsecInboundConnectionsLocalTlocAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 1),
    _IpsecInboundConnectionsLocalTlocAddress_Type()
)
ipsecInboundConnectionsLocalTlocAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsLocalTlocAddress.setStatus("current")
_IpsecInboundConnectionsLocalTlocColor_Type = ColorEnum
_IpsecInboundConnectionsLocalTlocColor_Object = MibTableColumn
ipsecInboundConnectionsLocalTlocColor = _IpsecInboundConnectionsLocalTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 2),
    _IpsecInboundConnectionsLocalTlocColor_Type()
)
ipsecInboundConnectionsLocalTlocColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsLocalTlocColor.setStatus("current")
_IpsecInboundConnectionsRemoteTlocAddress_Type = InetAddressIP
_IpsecInboundConnectionsRemoteTlocAddress_Object = MibTableColumn
ipsecInboundConnectionsRemoteTlocAddress = _IpsecInboundConnectionsRemoteTlocAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 3),
    _IpsecInboundConnectionsRemoteTlocAddress_Type()
)
ipsecInboundConnectionsRemoteTlocAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsRemoteTlocAddress.setStatus("current")
_IpsecInboundConnectionsRemoteTlocColor_Type = ColorEnum
_IpsecInboundConnectionsRemoteTlocColor_Object = MibTableColumn
ipsecInboundConnectionsRemoteTlocColor = _IpsecInboundConnectionsRemoteTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 4),
    _IpsecInboundConnectionsRemoteTlocColor_Type()
)
ipsecInboundConnectionsRemoteTlocColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsRemoteTlocColor.setStatus("current")
_IpsecInboundConnectionsLocalTlocIndex_Type = Unsigned32
_IpsecInboundConnectionsLocalTlocIndex_Object = MibTableColumn
ipsecInboundConnectionsLocalTlocIndex = _IpsecInboundConnectionsLocalTlocIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 5),
    _IpsecInboundConnectionsLocalTlocIndex_Type()
)
ipsecInboundConnectionsLocalTlocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsLocalTlocIndex.setStatus("current")
_IpsecInboundConnectionsRemoteTlocIndex_Type = Unsigned32
_IpsecInboundConnectionsRemoteTlocIndex_Object = MibTableColumn
ipsecInboundConnectionsRemoteTlocIndex = _IpsecInboundConnectionsRemoteTlocIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 6),
    _IpsecInboundConnectionsRemoteTlocIndex_Type()
)
ipsecInboundConnectionsRemoteTlocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsRemoteTlocIndex.setStatus("current")
_IpsecInboundConnectionsSourceIp_Type = InetAddressIP
_IpsecInboundConnectionsSourceIp_Object = MibTableColumn
ipsecInboundConnectionsSourceIp = _IpsecInboundConnectionsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 7),
    _IpsecInboundConnectionsSourceIp_Type()
)
ipsecInboundConnectionsSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsSourceIp.setStatus("current")
_IpsecInboundConnectionsSourcePort_Type = Unsigned32
_IpsecInboundConnectionsSourcePort_Object = MibTableColumn
ipsecInboundConnectionsSourcePort = _IpsecInboundConnectionsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 8),
    _IpsecInboundConnectionsSourcePort_Type()
)
ipsecInboundConnectionsSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsSourcePort.setStatus("current")
_IpsecInboundConnectionsDestIp_Type = InetAddressIP
_IpsecInboundConnectionsDestIp_Object = MibTableColumn
ipsecInboundConnectionsDestIp = _IpsecInboundConnectionsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 9),
    _IpsecInboundConnectionsDestIp_Type()
)
ipsecInboundConnectionsDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsDestIp.setStatus("current")
_IpsecInboundConnectionsDestPort_Type = Unsigned32
_IpsecInboundConnectionsDestPort_Object = MibTableColumn
ipsecInboundConnectionsDestPort = _IpsecInboundConnectionsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 10),
    _IpsecInboundConnectionsDestPort_Type()
)
ipsecInboundConnectionsDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsDestPort.setStatus("current")
_IpsecInboundConnectionsNegEncrAlgo_Type = String
_IpsecInboundConnectionsNegEncrAlgo_Object = MibTableColumn
ipsecInboundConnectionsNegEncrAlgo = _IpsecInboundConnectionsNegEncrAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 11),
    _IpsecInboundConnectionsNegEncrAlgo_Type()
)
ipsecInboundConnectionsNegEncrAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsNegEncrAlgo.setStatus("current")
_IpsecInboundConnectionsTcSpiPerTun_Type = Unsigned32
_IpsecInboundConnectionsTcSpiPerTun_Object = MibTableColumn
ipsecInboundConnectionsTcSpiPerTun = _IpsecInboundConnectionsTcSpiPerTun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 2, 1, 12),
    _IpsecInboundConnectionsTcSpiPerTun_Type()
)
ipsecInboundConnectionsTcSpiPerTun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecInboundConnectionsTcSpiPerTun.setStatus("current")
_IpsecOutboundConnectionsTable_Object = MibTable
ipsecOutboundConnectionsTable = _IpsecOutboundConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsTable.setStatus("current")
_IpsecOutboundConnectionsEntry_Object = MibTableRow
ipsecOutboundConnectionsEntry = _IpsecOutboundConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1)
)
ipsecOutboundConnectionsEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsSourceIp"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsSourcePort"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsDestIp"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsDestPort"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsSpi"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsTlocIndex"),
)
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsEntry.setStatus("current")
_IpsecOutboundConnectionsSourceIp_Type = InetAddressIP
_IpsecOutboundConnectionsSourceIp_Object = MibTableColumn
ipsecOutboundConnectionsSourceIp = _IpsecOutboundConnectionsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 1),
    _IpsecOutboundConnectionsSourceIp_Type()
)
ipsecOutboundConnectionsSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsSourceIp.setStatus("current")
_IpsecOutboundConnectionsSourcePort_Type = Unsigned32
_IpsecOutboundConnectionsSourcePort_Object = MibTableColumn
ipsecOutboundConnectionsSourcePort = _IpsecOutboundConnectionsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 2),
    _IpsecOutboundConnectionsSourcePort_Type()
)
ipsecOutboundConnectionsSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsSourcePort.setStatus("current")
_IpsecOutboundConnectionsDestIp_Type = InetAddressIP
_IpsecOutboundConnectionsDestIp_Object = MibTableColumn
ipsecOutboundConnectionsDestIp = _IpsecOutboundConnectionsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 3),
    _IpsecOutboundConnectionsDestIp_Type()
)
ipsecOutboundConnectionsDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsDestIp.setStatus("current")
_IpsecOutboundConnectionsDestPort_Type = Unsigned32
_IpsecOutboundConnectionsDestPort_Object = MibTableColumn
ipsecOutboundConnectionsDestPort = _IpsecOutboundConnectionsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 4),
    _IpsecOutboundConnectionsDestPort_Type()
)
ipsecOutboundConnectionsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsDestPort.setStatus("current")
_IpsecOutboundConnectionsSpi_Type = Unsigned32
_IpsecOutboundConnectionsSpi_Object = MibTableColumn
ipsecOutboundConnectionsSpi = _IpsecOutboundConnectionsSpi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 5),
    _IpsecOutboundConnectionsSpi_Type()
)
ipsecOutboundConnectionsSpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsSpi.setStatus("current")
_IpsecOutboundConnectionsTlocIndex_Type = Unsigned32
_IpsecOutboundConnectionsTlocIndex_Object = MibTableColumn
ipsecOutboundConnectionsTlocIndex = _IpsecOutboundConnectionsTlocIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 6),
    _IpsecOutboundConnectionsTlocIndex_Type()
)
ipsecOutboundConnectionsTlocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsTlocIndex.setStatus("current")
_IpsecOutboundConnectionsTunnelMtu_Type = Unsigned32
_IpsecOutboundConnectionsTunnelMtu_Object = MibTableColumn
ipsecOutboundConnectionsTunnelMtu = _IpsecOutboundConnectionsTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 7),
    _IpsecOutboundConnectionsTunnelMtu_Type()
)
ipsecOutboundConnectionsTunnelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsTunnelMtu.setStatus("current")
_IpsecOutboundConnectionsRemoteTlocAddress_Type = InetAddressIP
_IpsecOutboundConnectionsRemoteTlocAddress_Object = MibTableColumn
ipsecOutboundConnectionsRemoteTlocAddress = _IpsecOutboundConnectionsRemoteTlocAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 8),
    _IpsecOutboundConnectionsRemoteTlocAddress_Type()
)
ipsecOutboundConnectionsRemoteTlocAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsRemoteTlocAddress.setStatus("current")
_IpsecOutboundConnectionsRemoteTlocColor_Type = ColorEnum
_IpsecOutboundConnectionsRemoteTlocColor_Object = MibTableColumn
ipsecOutboundConnectionsRemoteTlocColor = _IpsecOutboundConnectionsRemoteTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 9),
    _IpsecOutboundConnectionsRemoteTlocColor_Type()
)
ipsecOutboundConnectionsRemoteTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsRemoteTlocColor.setStatus("current")
_IpsecOutboundConnectionsAuthenticationUsed_Type = String
_IpsecOutboundConnectionsAuthenticationUsed_Object = MibTableColumn
ipsecOutboundConnectionsAuthenticationUsed = _IpsecOutboundConnectionsAuthenticationUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 10),
    _IpsecOutboundConnectionsAuthenticationUsed_Type()
)
ipsecOutboundConnectionsAuthenticationUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsAuthenticationUsed.setStatus("current")
_IpsecOutboundConnectionsEncryptKeyHash_Type = String
_IpsecOutboundConnectionsEncryptKeyHash_Object = MibTableColumn
ipsecOutboundConnectionsEncryptKeyHash = _IpsecOutboundConnectionsEncryptKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 11),
    _IpsecOutboundConnectionsEncryptKeyHash_Type()
)
ipsecOutboundConnectionsEncryptKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsEncryptKeyHash.setStatus("current")
_IpsecOutboundConnectionsAuthKeyHash_Type = String
_IpsecOutboundConnectionsAuthKeyHash_Object = MibTableColumn
ipsecOutboundConnectionsAuthKeyHash = _IpsecOutboundConnectionsAuthKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 12),
    _IpsecOutboundConnectionsAuthKeyHash_Type()
)
ipsecOutboundConnectionsAuthKeyHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsAuthKeyHash.setStatus("current")
_IpsecOutboundConnectionsNegotiatedAlgo_Type = String
_IpsecOutboundConnectionsNegotiatedAlgo_Object = MibTableColumn
ipsecOutboundConnectionsNegotiatedAlgo = _IpsecOutboundConnectionsNegotiatedAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 13),
    _IpsecOutboundConnectionsNegotiatedAlgo_Type()
)
ipsecOutboundConnectionsNegotiatedAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsNegotiatedAlgo.setStatus("current")
_IpsecOutboundConnectionsTcSpiPerTun_Type = Unsigned32
_IpsecOutboundConnectionsTcSpiPerTun_Object = MibTableColumn
ipsecOutboundConnectionsTcSpiPerTun = _IpsecOutboundConnectionsTcSpiPerTun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 4, 3, 1, 14),
    _IpsecOutboundConnectionsTcSpiPerTun_Type()
)
ipsecOutboundConnectionsTcSpiPerTun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecOutboundConnectionsTcSpiPerTun.setStatus("current")
_Tunnel_ObjectIdentity = ObjectIdentity
tunnel = _Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5)
)
_TunnelStatisticsTable_Object = MibTable
tunnelStatisticsTable = _TunnelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tunnelStatisticsTable.setStatus("current")
_TunnelStatisticsEntry_Object = MibTableRow
tunnelStatisticsEntry = _TunnelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1)
)
tunnelStatisticsEntry.setIndexNames(
    (0, "CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsTunnelProtocol"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsSourceIp"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsDestIp"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsSourcePort"),
    (0, "CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsDestPort"),
)
if mibBuilder.loadTexts:
    tunnelStatisticsEntry.setStatus("current")


class _TunnelStatisticsTunnelProtocol_Type(Integer32):
    """Custom type tunnelStatisticsTunnelProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_TunnelStatisticsTunnelProtocol_Type.__name__ = "Integer32"
_TunnelStatisticsTunnelProtocol_Object = MibTableColumn
tunnelStatisticsTunnelProtocol = _TunnelStatisticsTunnelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 1),
    _TunnelStatisticsTunnelProtocol_Type()
)
tunnelStatisticsTunnelProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsTunnelProtocol.setStatus("current")
_TunnelStatisticsSourceIp_Type = InetAddressIP
_TunnelStatisticsSourceIp_Object = MibTableColumn
tunnelStatisticsSourceIp = _TunnelStatisticsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 2),
    _TunnelStatisticsSourceIp_Type()
)
tunnelStatisticsSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsSourceIp.setStatus("current")
_TunnelStatisticsDestIp_Type = InetAddressIP
_TunnelStatisticsDestIp_Object = MibTableColumn
tunnelStatisticsDestIp = _TunnelStatisticsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 3),
    _TunnelStatisticsDestIp_Type()
)
tunnelStatisticsDestIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsDestIp.setStatus("current")
_TunnelStatisticsSourcePort_Type = Unsigned32
_TunnelStatisticsSourcePort_Object = MibTableColumn
tunnelStatisticsSourcePort = _TunnelStatisticsSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 4),
    _TunnelStatisticsSourcePort_Type()
)
tunnelStatisticsSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsSourcePort.setStatus("current")
_TunnelStatisticsDestPort_Type = Unsigned32
_TunnelStatisticsDestPort_Object = MibTableColumn
tunnelStatisticsDestPort = _TunnelStatisticsDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 5),
    _TunnelStatisticsDestPort_Type()
)
tunnelStatisticsDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tunnelStatisticsDestPort.setStatus("current")
_TunnelStatisticsSystemIp_Type = InetAddressIP
_TunnelStatisticsSystemIp_Object = MibTableColumn
tunnelStatisticsSystemIp = _TunnelStatisticsSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 6),
    _TunnelStatisticsSystemIp_Type()
)
tunnelStatisticsSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsSystemIp.setStatus("current")
_TunnelStatisticsLocalColor_Type = ColorEnum
_TunnelStatisticsLocalColor_Object = MibTableColumn
tunnelStatisticsLocalColor = _TunnelStatisticsLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 7),
    _TunnelStatisticsLocalColor_Type()
)
tunnelStatisticsLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsLocalColor.setStatus("current")
_TunnelStatisticsRemoteColor_Type = ColorEnum
_TunnelStatisticsRemoteColor_Object = MibTableColumn
tunnelStatisticsRemoteColor = _TunnelStatisticsRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 8),
    _TunnelStatisticsRemoteColor_Type()
)
tunnelStatisticsRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsRemoteColor.setStatus("current")
_TunnelStatisticsTunnelMtu_Type = Unsigned32
_TunnelStatisticsTunnelMtu_Object = MibTableColumn
tunnelStatisticsTunnelMtu = _TunnelStatisticsTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 9),
    _TunnelStatisticsTunnelMtu_Type()
)
tunnelStatisticsTunnelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsTunnelMtu.setStatus("current")
_TunnelStatisticsTxPkts_Type = Counter64
_TunnelStatisticsTxPkts_Object = MibTableColumn
tunnelStatisticsTxPkts = _TunnelStatisticsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 10),
    _TunnelStatisticsTxPkts_Type()
)
tunnelStatisticsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsTxPkts.setStatus("current")
_TunnelStatisticsTxOctets_Type = Counter64
_TunnelStatisticsTxOctets_Object = MibTableColumn
tunnelStatisticsTxOctets = _TunnelStatisticsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 11),
    _TunnelStatisticsTxOctets_Type()
)
tunnelStatisticsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsTxOctets.setStatus("current")
_TunnelStatisticsRxPkts_Type = Counter64
_TunnelStatisticsRxPkts_Object = MibTableColumn
tunnelStatisticsRxPkts = _TunnelStatisticsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 12),
    _TunnelStatisticsRxPkts_Type()
)
tunnelStatisticsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsRxPkts.setStatus("current")
_TunnelStatisticsRxOctets_Type = Counter64
_TunnelStatisticsRxOctets_Object = MibTableColumn
tunnelStatisticsRxOctets = _TunnelStatisticsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 13),
    _TunnelStatisticsRxOctets_Type()
)
tunnelStatisticsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsRxOctets.setStatus("current")
_TunnelStatisticsIpsecDecryptInbound_Type = Counter64
_TunnelStatisticsIpsecDecryptInbound_Object = MibTableColumn
tunnelStatisticsIpsecDecryptInbound = _TunnelStatisticsIpsecDecryptInbound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 14),
    _TunnelStatisticsIpsecDecryptInbound_Type()
)
tunnelStatisticsIpsecDecryptInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecDecryptInbound.setStatus("current")
_TunnelStatisticsIpsecRxAuthFailures_Type = Counter64
_TunnelStatisticsIpsecRxAuthFailures_Object = MibTableColumn
tunnelStatisticsIpsecRxAuthFailures = _TunnelStatisticsIpsecRxAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 15),
    _TunnelStatisticsIpsecRxAuthFailures_Type()
)
tunnelStatisticsIpsecRxAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecRxAuthFailures.setStatus("current")
_TunnelStatisticsIpsecRxFailures_Type = Counter64
_TunnelStatisticsIpsecRxFailures_Object = MibTableColumn
tunnelStatisticsIpsecRxFailures = _TunnelStatisticsIpsecRxFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 16),
    _TunnelStatisticsIpsecRxFailures_Type()
)
tunnelStatisticsIpsecRxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecRxFailures.setStatus("current")
_TunnelStatisticsIpsecEncryptOutbound_Type = Counter64
_TunnelStatisticsIpsecEncryptOutbound_Object = MibTableColumn
tunnelStatisticsIpsecEncryptOutbound = _TunnelStatisticsIpsecEncryptOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 17),
    _TunnelStatisticsIpsecEncryptOutbound_Type()
)
tunnelStatisticsIpsecEncryptOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecEncryptOutbound.setStatus("current")
_TunnelStatisticsIpsecTxAuthFailures_Type = Counter64
_TunnelStatisticsIpsecTxAuthFailures_Object = MibTableColumn
tunnelStatisticsIpsecTxAuthFailures = _TunnelStatisticsIpsecTxAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 18),
    _TunnelStatisticsIpsecTxAuthFailures_Type()
)
tunnelStatisticsIpsecTxAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecTxAuthFailures.setStatus("current")
_TunnelStatisticsIpsecTxFailures_Type = Counter64
_TunnelStatisticsIpsecTxFailures_Object = MibTableColumn
tunnelStatisticsIpsecTxFailures = _TunnelStatisticsIpsecTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 19),
    _TunnelStatisticsIpsecTxFailures_Type()
)
tunnelStatisticsIpsecTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIpsecTxFailures.setStatus("current")
_TunnelStatisticsTcpMssAdjust_Type = Unsigned32
_TunnelStatisticsTcpMssAdjust_Object = MibTableColumn
tunnelStatisticsTcpMssAdjust = _TunnelStatisticsTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 20),
    _TunnelStatisticsTcpMssAdjust_Type()
)
tunnelStatisticsTcpMssAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsTcpMssAdjust.setStatus("current")
_TunnelStatisticsBfdTxPkts_Type = Counter64
_TunnelStatisticsBfdTxPkts_Object = MibTableColumn
tunnelStatisticsBfdTxPkts = _TunnelStatisticsBfdTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 21),
    _TunnelStatisticsBfdTxPkts_Type()
)
tunnelStatisticsBfdTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBfdTxPkts.setStatus("current")
_TunnelStatisticsBfdRxPkts_Type = Counter64
_TunnelStatisticsBfdRxPkts_Object = MibTableColumn
tunnelStatisticsBfdRxPkts = _TunnelStatisticsBfdRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 22),
    _TunnelStatisticsBfdRxPkts_Type()
)
tunnelStatisticsBfdRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBfdRxPkts.setStatus("current")
_TunnelStatisticsBfdTxOctets_Type = Counter64
_TunnelStatisticsBfdTxOctets_Object = MibTableColumn
tunnelStatisticsBfdTxOctets = _TunnelStatisticsBfdTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 23),
    _TunnelStatisticsBfdTxOctets_Type()
)
tunnelStatisticsBfdTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBfdTxOctets.setStatus("current")
_TunnelStatisticsBfdRxOctets_Type = Counter64
_TunnelStatisticsBfdRxOctets_Object = MibTableColumn
tunnelStatisticsBfdRxOctets = _TunnelStatisticsBfdRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 24),
    _TunnelStatisticsBfdRxOctets_Type()
)
tunnelStatisticsBfdRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsBfdRxOctets.setStatus("current")
_TunnelStatisticsPmtuTxPkts_Type = Counter64
_TunnelStatisticsPmtuTxPkts_Object = MibTableColumn
tunnelStatisticsPmtuTxPkts = _TunnelStatisticsPmtuTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 25),
    _TunnelStatisticsPmtuTxPkts_Type()
)
tunnelStatisticsPmtuTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPmtuTxPkts.setStatus("current")
_TunnelStatisticsPmtuRxPkts_Type = Counter64
_TunnelStatisticsPmtuRxPkts_Object = MibTableColumn
tunnelStatisticsPmtuRxPkts = _TunnelStatisticsPmtuRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 26),
    _TunnelStatisticsPmtuRxPkts_Type()
)
tunnelStatisticsPmtuRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPmtuRxPkts.setStatus("current")
_TunnelStatisticsPmtuTxOctets_Type = Counter64
_TunnelStatisticsPmtuTxOctets_Object = MibTableColumn
tunnelStatisticsPmtuTxOctets = _TunnelStatisticsPmtuTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 27),
    _TunnelStatisticsPmtuTxOctets_Type()
)
tunnelStatisticsPmtuTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPmtuTxOctets.setStatus("current")
_TunnelStatisticsPmtuRxOctets_Type = Counter64
_TunnelStatisticsPmtuRxOctets_Object = MibTableColumn
tunnelStatisticsPmtuRxOctets = _TunnelStatisticsPmtuRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 28),
    _TunnelStatisticsPmtuRxOctets_Type()
)
tunnelStatisticsPmtuRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPmtuRxOctets.setStatus("current")
_TunnelStatisticsIPv6TxPkts_Type = Counter64
_TunnelStatisticsIPv6TxPkts_Object = MibTableColumn
tunnelStatisticsIPv6TxPkts = _TunnelStatisticsIPv6TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 29),
    _TunnelStatisticsIPv6TxPkts_Type()
)
tunnelStatisticsIPv6TxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIPv6TxPkts.setStatus("current")
_TunnelStatisticsIPv6TxOctets_Type = Counter64
_TunnelStatisticsIPv6TxOctets_Object = MibTableColumn
tunnelStatisticsIPv6TxOctets = _TunnelStatisticsIPv6TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 30),
    _TunnelStatisticsIPv6TxOctets_Type()
)
tunnelStatisticsIPv6TxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIPv6TxOctets.setStatus("current")
_TunnelStatisticsIPv6RxPkts_Type = Counter64
_TunnelStatisticsIPv6RxPkts_Object = MibTableColumn
tunnelStatisticsIPv6RxPkts = _TunnelStatisticsIPv6RxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 31),
    _TunnelStatisticsIPv6RxPkts_Type()
)
tunnelStatisticsIPv6RxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIPv6RxPkts.setStatus("current")
_TunnelStatisticsIPv6RxOctets_Type = Counter64
_TunnelStatisticsIPv6RxOctets_Object = MibTableColumn
tunnelStatisticsIPv6RxOctets = _TunnelStatisticsIPv6RxOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 32),
    _TunnelStatisticsIPv6RxOctets_Type()
)
tunnelStatisticsIPv6RxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIPv6RxOctets.setStatus("current")
_TunnelStatisticsFecRxDataPkts_Type = Unsigned32
_TunnelStatisticsFecRxDataPkts_Object = MibTableColumn
tunnelStatisticsFecRxDataPkts = _TunnelStatisticsFecRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 33),
    _TunnelStatisticsFecRxDataPkts_Type()
)
tunnelStatisticsFecRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecRxDataPkts.setStatus("current")
_TunnelStatisticsFecRxParityPkts_Type = Unsigned32
_TunnelStatisticsFecRxParityPkts_Object = MibTableColumn
tunnelStatisticsFecRxParityPkts = _TunnelStatisticsFecRxParityPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 34),
    _TunnelStatisticsFecRxParityPkts_Type()
)
tunnelStatisticsFecRxParityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecRxParityPkts.setStatus("current")
_TunnelStatisticsFecTxDataPkts_Type = Unsigned32
_TunnelStatisticsFecTxDataPkts_Object = MibTableColumn
tunnelStatisticsFecTxDataPkts = _TunnelStatisticsFecTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 35),
    _TunnelStatisticsFecTxDataPkts_Type()
)
tunnelStatisticsFecTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecTxDataPkts.setStatus("current")
_TunnelStatisticsFecTxParityPkts_Type = Unsigned32
_TunnelStatisticsFecTxParityPkts_Object = MibTableColumn
tunnelStatisticsFecTxParityPkts = _TunnelStatisticsFecTxParityPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 36),
    _TunnelStatisticsFecTxParityPkts_Type()
)
tunnelStatisticsFecTxParityPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecTxParityPkts.setStatus("current")
_TunnelStatisticsFecReconstructPkts_Type = Unsigned32
_TunnelStatisticsFecReconstructPkts_Object = MibTableColumn
tunnelStatisticsFecReconstructPkts = _TunnelStatisticsFecReconstructPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 37),
    _TunnelStatisticsFecReconstructPkts_Type()
)
tunnelStatisticsFecReconstructPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecReconstructPkts.setStatus("current")
_TunnelStatisticsFecCapable_Type = TruthValue
_TunnelStatisticsFecCapable_Object = MibTableColumn
tunnelStatisticsFecCapable = _TunnelStatisticsFecCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 38),
    _TunnelStatisticsFecCapable_Type()
)
tunnelStatisticsFecCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecCapable.setStatus("current")
_TunnelStatisticsFecDynamic_Type = TruthValue
_TunnelStatisticsFecDynamic_Object = MibTableColumn
tunnelStatisticsFecDynamic = _TunnelStatisticsFecDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 39),
    _TunnelStatisticsFecDynamic_Type()
)
tunnelStatisticsFecDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsFecDynamic.setStatus("current")
_TunnelStatisticsPktDupRxPkts_Type = Unsigned32
_TunnelStatisticsPktDupRxPkts_Object = MibTableColumn
tunnelStatisticsPktDupRxPkts = _TunnelStatisticsPktDupRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 40),
    _TunnelStatisticsPktDupRxPkts_Type()
)
tunnelStatisticsPktDupRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupRxPkts.setStatus("current")
_TunnelStatisticsPktDupRxOtherPkts_Type = Unsigned32
_TunnelStatisticsPktDupRxOtherPkts_Object = MibTableColumn
tunnelStatisticsPktDupRxOtherPkts = _TunnelStatisticsPktDupRxOtherPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 41),
    _TunnelStatisticsPktDupRxOtherPkts_Type()
)
tunnelStatisticsPktDupRxOtherPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupRxOtherPkts.setStatus("current")
_TunnelStatisticsPktDupRxThisPkts_Type = Unsigned32
_TunnelStatisticsPktDupRxThisPkts_Object = MibTableColumn
tunnelStatisticsPktDupRxThisPkts = _TunnelStatisticsPktDupRxThisPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 42),
    _TunnelStatisticsPktDupRxThisPkts_Type()
)
tunnelStatisticsPktDupRxThisPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupRxThisPkts.setStatus("current")
_TunnelStatisticsPktDupTxPkts_Type = Unsigned32
_TunnelStatisticsPktDupTxPkts_Object = MibTableColumn
tunnelStatisticsPktDupTxPkts = _TunnelStatisticsPktDupTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 43),
    _TunnelStatisticsPktDupTxPkts_Type()
)
tunnelStatisticsPktDupTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupTxPkts.setStatus("current")
_TunnelStatisticsPktDupTxOtherPkts_Type = Unsigned32
_TunnelStatisticsPktDupTxOtherPkts_Object = MibTableColumn
tunnelStatisticsPktDupTxOtherPkts = _TunnelStatisticsPktDupTxOtherPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 44),
    _TunnelStatisticsPktDupTxOtherPkts_Type()
)
tunnelStatisticsPktDupTxOtherPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupTxOtherPkts.setStatus("current")
_TunnelStatisticsPktDupCapable_Type = TruthValue
_TunnelStatisticsPktDupCapable_Object = MibTableColumn
tunnelStatisticsPktDupCapable = _TunnelStatisticsPktDupCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 45),
    _TunnelStatisticsPktDupCapable_Type()
)
tunnelStatisticsPktDupCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsPktDupCapable.setStatus("current")
_TunnelStatisticsIPv4TxMcPkts_Type = Counter64
_TunnelStatisticsIPv4TxMcPkts_Object = MibTableColumn
tunnelStatisticsIPv4TxMcPkts = _TunnelStatisticsIPv4TxMcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 46),
    _TunnelStatisticsIPv4TxMcPkts_Type()
)
tunnelStatisticsIPv4TxMcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIPv4TxMcPkts.setStatus("current")
_TunnelStatisticsIPv4TxMcOctets_Type = Counter64
_TunnelStatisticsIPv4TxMcOctets_Object = MibTableColumn
tunnelStatisticsIPv4TxMcOctets = _TunnelStatisticsIPv4TxMcOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 47),
    _TunnelStatisticsIPv4TxMcOctets_Type()
)
tunnelStatisticsIPv4TxMcOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIPv4TxMcOctets.setStatus("current")
_TunnelStatisticsIPv4RxMcPkts_Type = Counter64
_TunnelStatisticsIPv4RxMcPkts_Object = MibTableColumn
tunnelStatisticsIPv4RxMcPkts = _TunnelStatisticsIPv4RxMcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 48),
    _TunnelStatisticsIPv4RxMcPkts_Type()
)
tunnelStatisticsIPv4RxMcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIPv4RxMcPkts.setStatus("current")
_TunnelStatisticsIPv4RxMcOctets_Type = Counter64
_TunnelStatisticsIPv4RxMcOctets_Object = MibTableColumn
tunnelStatisticsIPv4RxMcOctets = _TunnelStatisticsIPv4RxMcOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 5, 1, 1, 49),
    _TunnelStatisticsIPv4RxMcOctets_Type()
)
tunnelStatisticsIPv4RxMcOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatisticsIPv4RxMcOctets.setStatus("current")
_SecurityInfo_ObjectIdentity = ObjectIdentity
securityInfo = _SecurityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 6)
)
_SecurityInfoRekey_Type = Unsigned32
_SecurityInfoRekey_Object = MibScalar
securityInfoRekey = _SecurityInfoRekey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 6, 1),
    _SecurityInfoRekey_Type()
)
securityInfoRekey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoRekey.setStatus("current")
_SecurityInfoReplayWindow_Type = Unsigned32
_SecurityInfoReplayWindow_Object = MibScalar
securityInfoReplayWindow = _SecurityInfoReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 6, 2),
    _SecurityInfoReplayWindow_Type()
)
securityInfoReplayWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoReplayWindow.setStatus("current")
_SecurityInfoEncryptionSupported_Type = String
_SecurityInfoEncryptionSupported_Object = MibScalar
securityInfoEncryptionSupported = _SecurityInfoEncryptionSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 6, 3),
    _SecurityInfoEncryptionSupported_Type()
)
securityInfoEncryptionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoEncryptionSupported.setStatus("current")
_SecurityInfoFipsMode_Type = String
_SecurityInfoFipsMode_Object = MibScalar
securityInfoFipsMode = _SecurityInfoFipsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 6, 4),
    _SecurityInfoFipsMode_Type()
)
securityInfoFipsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoFipsMode.setStatus("current")
_SecurityInfoPairwiseKeying_Type = String
_SecurityInfoPairwiseKeying_Object = MibScalar
securityInfoPairwiseKeying = _SecurityInfoPairwiseKeying_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 6, 5),
    _SecurityInfoPairwiseKeying_Type()
)
securityInfoPairwiseKeying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoPairwiseKeying.setStatus("current")
_SecurityInfoPwkSymRekey_Type = String
_SecurityInfoPwkSymRekey_Object = MibScalar
securityInfoPwkSymRekey = _SecurityInfoPwkSymRekey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 6, 6),
    _SecurityInfoPwkSymRekey_Type()
)
securityInfoPwkSymRekey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoPwkSymRekey.setStatus("current")
_SecurityInfoExtendedAntiReplayWindow_Type = String
_SecurityInfoExtendedAntiReplayWindow_Object = MibScalar
securityInfoExtendedAntiReplayWindow = _SecurityInfoExtendedAntiReplayWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 6, 7),
    _SecurityInfoExtendedAntiReplayWindow_Type()
)
securityInfoExtendedAntiReplayWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoExtendedAntiReplayWindow.setStatus("current")
_SecurityInfoIntegrityType_Type = String
_SecurityInfoIntegrityType_Object = MibScalar
securityInfoIntegrityType = _SecurityInfoIntegrityType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 1, 6, 8),
    _SecurityInfoIntegrityType_Type()
)
securityInfoIntegrityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityInfoIntegrityType.setStatus("current")
_CiscoSdwanSecurityMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanSecurityMIBNotifObjects = _CiscoSdwanSecurityMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2)
)
_NetconfNotificationSeverity_Type = NotificationSeverity
_NetconfNotificationSeverity_Object = MibScalar
netconfNotificationSeverity = _NetconfNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 2),
    _NetconfNotificationSeverity_Type()
)
netconfNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netconfNotificationSeverity.setStatus("current")
_CiscoSdwanSecurityPersonality_Type = PersonalityEnumOper
_CiscoSdwanSecurityPersonality_Object = MibScalar
ciscoSdwanSecurityPersonality = _CiscoSdwanSecurityPersonality_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 3),
    _CiscoSdwanSecurityPersonality_Type()
)
ciscoSdwanSecurityPersonality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityPersonality.setStatus("current")
_CiscoSdwanSecurityPeerType_Type = PersonalityEnumOper
_CiscoSdwanSecurityPeerType_Object = MibScalar
ciscoSdwanSecurityPeerType = _CiscoSdwanSecurityPeerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 4),
    _CiscoSdwanSecurityPeerType_Type()
)
ciscoSdwanSecurityPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityPeerType.setStatus("current")
_CiscoSdwanSecurityPeerSystemIp_Type = InetAddressIP
_CiscoSdwanSecurityPeerSystemIp_Object = MibScalar
ciscoSdwanSecurityPeerSystemIp = _CiscoSdwanSecurityPeerSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 5),
    _CiscoSdwanSecurityPeerSystemIp_Type()
)
ciscoSdwanSecurityPeerSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityPeerSystemIp.setStatus("current")
_CiscoSdwanSecurityPeerVmanageSystemIp_Type = InetAddressIP
_CiscoSdwanSecurityPeerVmanageSystemIp_Object = MibScalar
ciscoSdwanSecurityPeerVmanageSystemIp = _CiscoSdwanSecurityPeerVmanageSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 6),
    _CiscoSdwanSecurityPeerVmanageSystemIp_Type()
)
ciscoSdwanSecurityPeerVmanageSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityPeerVmanageSystemIp.setStatus("current")
_CiscoSdwanSecurityPublicIp_Type = InetAddressIP
_CiscoSdwanSecurityPublicIp_Object = MibScalar
ciscoSdwanSecurityPublicIp = _CiscoSdwanSecurityPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 7),
    _CiscoSdwanSecurityPublicIp_Type()
)
ciscoSdwanSecurityPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityPublicIp.setStatus("current")
_CiscoSdwanSecurityPublicPort_Type = Unsigned32
_CiscoSdwanSecurityPublicPort_Object = MibScalar
ciscoSdwanSecurityPublicPort = _CiscoSdwanSecurityPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 8),
    _CiscoSdwanSecurityPublicPort_Type()
)
ciscoSdwanSecurityPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityPublicPort.setStatus("current")
_CiscoSdwanSecuritySrcColor_Type = ColorEnum
_CiscoSdwanSecuritySrcColor_Object = MibScalar
ciscoSdwanSecuritySrcColor = _CiscoSdwanSecuritySrcColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 9),
    _CiscoSdwanSecuritySrcColor_Type()
)
ciscoSdwanSecuritySrcColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySrcColor.setStatus("current")
_CiscoSdwanSecurityRemoteColor_Type = ColorEnum
_CiscoSdwanSecurityRemoteColor_Object = MibScalar
ciscoSdwanSecurityRemoteColor = _CiscoSdwanSecurityRemoteColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 10),
    _CiscoSdwanSecurityRemoteColor_Type()
)
ciscoSdwanSecurityRemoteColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityRemoteColor.setStatus("current")
_CiscoSdwanSecurityUptime_Type = OctetString
_CiscoSdwanSecurityUptime_Object = MibScalar
ciscoSdwanSecurityUptime = _CiscoSdwanSecurityUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 11),
    _CiscoSdwanSecurityUptime_Type()
)
ciscoSdwanSecurityUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityUptime.setStatus("current")
_CiscoSdwanSecurityNewState_Type = OperState
_CiscoSdwanSecurityNewState_Object = MibScalar
ciscoSdwanSecurityNewState = _CiscoSdwanSecurityNewState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 12),
    _CiscoSdwanSecurityNewState_Type()
)
ciscoSdwanSecurityNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityNewState.setStatus("current")
_CiscoSdwanSecurityLocalSystemIp_Type = InetAddressIP
_CiscoSdwanSecurityLocalSystemIp_Object = MibScalar
ciscoSdwanSecurityLocalSystemIp = _CiscoSdwanSecurityLocalSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 13),
    _CiscoSdwanSecurityLocalSystemIp_Type()
)
ciscoSdwanSecurityLocalSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityLocalSystemIp.setStatus("current")
_CiscoSdwanSecurityLocalColor_Type = ColorEnum
_CiscoSdwanSecurityLocalColor_Object = MibScalar
ciscoSdwanSecurityLocalColor = _CiscoSdwanSecurityLocalColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 14),
    _CiscoSdwanSecurityLocalColor_Type()
)
ciscoSdwanSecurityLocalColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityLocalColor.setStatus("current")
_CiscoSdwanSecurityReason_Type = OctetString
_CiscoSdwanSecurityReason_Object = MibScalar
ciscoSdwanSecurityReason = _CiscoSdwanSecurityReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 15),
    _CiscoSdwanSecurityReason_Type()
)
ciscoSdwanSecurityReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityReason.setStatus("current")
_CiscoSdwanSecurityOldPublicIp_Type = InetAddressIP
_CiscoSdwanSecurityOldPublicIp_Object = MibScalar
ciscoSdwanSecurityOldPublicIp = _CiscoSdwanSecurityOldPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 16),
    _CiscoSdwanSecurityOldPublicIp_Type()
)
ciscoSdwanSecurityOldPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityOldPublicIp.setStatus("current")
_CiscoSdwanSecurityOldPublicPort_Type = Unsigned32
_CiscoSdwanSecurityOldPublicPort_Object = MibScalar
ciscoSdwanSecurityOldPublicPort = _CiscoSdwanSecurityOldPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 17),
    _CiscoSdwanSecurityOldPublicPort_Type()
)
ciscoSdwanSecurityOldPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityOldPublicPort.setStatus("current")
_CiscoSdwanSecurityNewPublicIp_Type = InetAddressIP
_CiscoSdwanSecurityNewPublicIp_Object = MibScalar
ciscoSdwanSecurityNewPublicIp = _CiscoSdwanSecurityNewPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 18),
    _CiscoSdwanSecurityNewPublicIp_Type()
)
ciscoSdwanSecurityNewPublicIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityNewPublicIp.setStatus("current")
_CiscoSdwanSecurityNewPublicPort_Type = Unsigned32
_CiscoSdwanSecurityNewPublicPort_Object = MibScalar
ciscoSdwanSecurityNewPublicPort = _CiscoSdwanSecurityNewPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 19),
    _CiscoSdwanSecurityNewPublicPort_Type()
)
ciscoSdwanSecurityNewPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityNewPublicPort.setStatus("current")
_CiscoSdwanSecurityColor_Type = ColorEnum
_CiscoSdwanSecurityColor_Object = MibScalar
ciscoSdwanSecurityColor = _CiscoSdwanSecurityColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 20),
    _CiscoSdwanSecurityColor_Type()
)
ciscoSdwanSecurityColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityColor.setStatus("current")
_CiscoSdwanSecurityUuid_Type = OctetString
_CiscoSdwanSecurityUuid_Object = MibScalar
ciscoSdwanSecurityUuid = _CiscoSdwanSecurityUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 21),
    _CiscoSdwanSecurityUuid_Type()
)
ciscoSdwanSecurityUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityUuid.setStatus("current")
_CiscoSdwanSecuritySerial_Type = OctetString
_CiscoSdwanSecuritySerial_Object = MibScalar
ciscoSdwanSecuritySerial = _CiscoSdwanSecuritySerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 22),
    _CiscoSdwanSecuritySerial_Type()
)
ciscoSdwanSecuritySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySerial.setStatus("current")
_CiscoSdwanSecurityVmanageConnectionPreference_Type = UnsignedByte
_CiscoSdwanSecurityVmanageConnectionPreference_Object = MibScalar
ciscoSdwanSecurityVmanageConnectionPreference = _CiscoSdwanSecurityVmanageConnectionPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 23),
    _CiscoSdwanSecurityVmanageConnectionPreference_Type()
)
ciscoSdwanSecurityVmanageConnectionPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityVmanageConnectionPreference.setStatus("current")
_CiscoSdwanSecurityOrganizationName_Type = OctetString
_CiscoSdwanSecurityOrganizationName_Object = MibScalar
ciscoSdwanSecurityOrganizationName = _CiscoSdwanSecurityOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 24),
    _CiscoSdwanSecurityOrganizationName_Type()
)
ciscoSdwanSecurityOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityOrganizationName.setStatus("current")
_CiscoSdwanSecuritySpOrganizationName_Type = OctetString
_CiscoSdwanSecuritySpOrganizationName_Object = MibScalar
ciscoSdwanSecuritySpOrganizationName = _CiscoSdwanSecuritySpOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 25),
    _CiscoSdwanSecuritySpOrganizationName_Type()
)
ciscoSdwanSecuritySpOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySpOrganizationName.setStatus("current")
_CiscoSdwanSecurityCertificateType_Type = CertificateTypeEnum
_CiscoSdwanSecurityCertificateType_Object = MibScalar
ciscoSdwanSecurityCertificateType = _CiscoSdwanSecurityCertificateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 26),
    _CiscoSdwanSecurityCertificateType_Type()
)
ciscoSdwanSecurityCertificateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityCertificateType.setStatus("current")
_CiscoSdwanSecurityCertificateSerialNumber_Type = OctetString
_CiscoSdwanSecurityCertificateSerialNumber_Object = MibScalar
ciscoSdwanSecurityCertificateSerialNumber = _CiscoSdwanSecurityCertificateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 27),
    _CiscoSdwanSecurityCertificateSerialNumber_Type()
)
ciscoSdwanSecurityCertificateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityCertificateSerialNumber.setStatus("current")
_CiscoSdwanSecurityIssuer_Type = OctetString
_CiscoSdwanSecurityIssuer_Object = MibScalar
ciscoSdwanSecurityIssuer = _CiscoSdwanSecurityIssuer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 28),
    _CiscoSdwanSecurityIssuer_Type()
)
ciscoSdwanSecurityIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityIssuer.setStatus("current")
_CiscoSdwanSecurityDaysToExpiry_Type = Integer32
_CiscoSdwanSecurityDaysToExpiry_Object = MibScalar
ciscoSdwanSecurityDaysToExpiry = _CiscoSdwanSecurityDaysToExpiry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 2, 29),
    _CiscoSdwanSecurityDaysToExpiry_Type()
)
ciscoSdwanSecurityDaysToExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSecurityDaysToExpiry.setStatus("current")
_CiscoSdwanSecurityMIBConform_ObjectIdentity = ObjectIdentity
ciscoSdwanSecurityMIBConform = _CiscoSdwanSecurityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3)
)
_CiscoSdwanSecurityMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSdwanSecurityMIBCompliances = _CiscoSdwanSecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 1)
)
_CiscoSdwanSecurityMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSdwanSecurityMIBGroups = _CiscoSdwanSecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2)
)

# Managed Objects groups

cSdwanSecurityControlLocalPropertiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 1)
)
cSdwanSecurityControlLocalPropertiesGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesDeviceType"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesOrganizationName"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesCertificateStatus"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesRootCaChainStatus"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesCertificateValidity"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesCertificateNotValidBefore"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesCertificateNotValidAfter"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesDnsName"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesSiteId"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesDomainId"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesTlsPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesSystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesUuid"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesBoardSerial"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesRegisterInterval"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesRetryInterval"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesNoActivity"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesDnsCacheFlushInterval"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesPortHopped"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesTimeSincePortHop"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesMaxControllers"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesKeygenInterval"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesNumberVbondPeers"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesNumberActiveWanInterfaces"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesVsmartListVersion"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesSPOrganizationName"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesToken"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesEmbargoCheck"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesEnterpriseSerial"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesEnterpriseCertificateStatus"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesEnterpriseCertificateValidity"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesEnterpriseCertificateNotValidBefore"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesEnterpriseCertificateNotValidAfter"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesRootCaCrlStatus"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesPairwiseKeying"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesSubjectSerialNumber"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityControlLocalPropertiesGroup.setStatus("current")

cSdwanSecurityNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 2)
)
cSdwanSecurityNotifObjsGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPersonality"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPeerType"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPeerSystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPeerVmanageSystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPublicIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPublicPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySrcColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityRemoteColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityUptime"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityNewState"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityLocalSystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityLocalColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityReason"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityOldPublicIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityOldPublicPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityNewPublicIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityNewPublicPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityUuid"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySerial"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityVmanageConnectionPreference"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityOrganizationName"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySpOrganizationName"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityCertificateType"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityCertificateSerialNumber"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityIssuer"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityDaysToExpiry"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityNotifObjsGroup.setStatus("current")

cSdwanSecurityControlSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 4)
)
cSdwanSecurityControlSummaryGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlSummaryVbondCounts"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlSummaryVmanageCounts"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlSummaryVsmartCounts"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlSummaryVedgeCounts"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlSummaryProtocol"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlSummaryListeningIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlSummaryListeningPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlSummaryListeningIpv6"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlSummaryValidControllerCounts"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityControlSummaryGroup.setStatus("current")

cSdwanSecurityAffinityConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 5)
)
cSdwanSecurityAffinityConfigGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlAffinityConfigAffcInterface"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlAffinityConfigAffcErvc"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlAffinityConfigAffcEcl"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlAffinityConfigAffcCcl"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlAffinityConfigAffcEquil"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlAffinityConfigAffcLastResort"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlAffinityConfigAffcTenantCount"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityAffinityConfigGroup.setStatus("current")

cSdwanSecurityIpAddressListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 6)
)
cSdwanSecurityIpAddressListGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesIpAddressListIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesIpAddressListPort"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityIpAddressListGroup.setStatus("current")

cSdwanSecurityVbondAddressListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 7)
)
cSdwanSecurityVbondAddressListGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesVbondAddressListIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesVbondAddressListPort"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityVbondAddressListGroup.setStatus("current")

cSdwanSecurityAffinityStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 8)
)
cSdwanSecurityAffinityStatusGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlAffinityStatusAffsInterface"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlAffinityStatusAffsAcc"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlAffinityStatusAffsUcc"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlAffinityStatusAffsAc"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityAffinityStatusGroup.setStatus("current")

cSdwanSecurityControlConnectionsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 9)
)
cSdwanSecurityControlConnectionsInfoGroup.setObjects(
    ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsInfoRate")
)
if mibBuilder.loadTexts:
    cSdwanSecurityControlConnectionsInfoGroup.setStatus("current")

cSdwanSecuritySecurityInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 10)
)
cSdwanSecuritySecurityInfoGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "securityInfoRekey"),
        ("CISCO-SDWAN-SECURITY-MIB", "securityInfoReplayWindow"),
        ("CISCO-SDWAN-SECURITY-MIB", "securityInfoEncryptionSupported"),
        ("CISCO-SDWAN-SECURITY-MIB", "securityInfoFipsMode"),
        ("CISCO-SDWAN-SECURITY-MIB", "securityInfoPairwiseKeying"),
        ("CISCO-SDWAN-SECURITY-MIB", "securityInfoPwkSymRekey"),
        ("CISCO-SDWAN-SECURITY-MIB", "securityInfoExtendedAntiReplayWindow"),
        ("CISCO-SDWAN-SECURITY-MIB", "securityInfoIntegrityType"))
)
if mibBuilder.loadTexts:
    cSdwanSecuritySecurityInfoGroup.setStatus("current")

cSdwanSecurityWanInterfaceListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 11)
)
cSdwanSecurityWanInterfaceListGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListInterface"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListPublicIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListPublicPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListPrivateIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListPrivatePort"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListNumVsmarts"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListNumVmanages"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListWeight"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListCarrier"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListPreference"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListAdminState"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListOperationState"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListLastConnTime"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListRestrictStr"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListControlStr"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListPerWanMaxControllers"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListPrivateIpv6"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListSpiChange"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListLastResort"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListWanPortHopped"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListWanTimeSincePortHop"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListVbondAsStunServer"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListVmanageConnPreference"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListLowBandwidthLink"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListNatType"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListInterfaceAdminState"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListInterfaceOperState"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlLocalPropertiesWanInterfaceListRegionId"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityWanInterfaceListGroup.setStatus("current")

cSdwanSecurityControlStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 12)
)
cSdwanSecurityControlStatisticsGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxError"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxBlocked"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxHello"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxConnects"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxRegisters"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxRegisterReplies"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxDtlsHandshake"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxDtlsHandshakeFailures"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxDtlsHandshakeDone"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxChallenge"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxChallengeResp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxChallengeAck"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxChallengeError"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxChallengeRespError"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxChallengeAckError"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxChallengeGenError"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxVmanageToPeer"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsTxRegisterToVmanage"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxError"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxHello"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxConnects"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxRegisters"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxRegisterReplies"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxDtlsHandshake"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxDtlsHandshakeFailures"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxDtlsHandshakeDone"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxChallenge"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxChallengeResp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxChallengeAck"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsChallengeFailures"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxVmanageToPeer"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsRxRegisterToVmanage"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlStatisticsBidFailuresNeedingReset"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityControlStatisticsGroup.setStatus("current")

cSdwanSecurityControlValidVsmartsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 13)
)
cSdwanSecurityControlValidVsmartsGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlValidVsmartsSerialNumber"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlValidVsmartsOrg"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityControlValidVsmartsGroup.setStatus("current")

cSdwanSecurityControlConnectionsHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 14)
)
cSdwanSecurityControlConnectionsHistoryGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryPeerType"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistorySiteId"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryDomainId"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryPrivateIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryPrivatePort"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryPublicIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryPublicPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistorySystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryProtocol"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryLocalColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRemoteColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryState"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryLocalEnum"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRemoteEnum"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryLocalStateInfo"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRemoteStateInfo"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryDowntime"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxHello"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxConnects"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxRegisters"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxRegisterReplies"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxChallenge"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxChallengeResp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxChallengeAck"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxTeardown"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxTeardownAll"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxVmToPeer"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxRegisterToVm"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxHello"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxConnects"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxRegisters"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxRegisterReplies"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxChallenge"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxChallengeResp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxChallengeAck"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxTeardown"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxVmToPeer"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxRegisterToVm"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRepCount"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryPrevDowntime"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryVHOrgName"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryUuid"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxCreateCert"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxCreateCert"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryTxCreateCertReply"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryRxCreateCertReply"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsHistoryLocalInterface"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityControlConnectionsHistoryGroup.setStatus("current")

cSdwanSecurityIpsecLocalSaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 15)
)
cSdwanSecurityIpsecLocalSaGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "ipsecLocalSaIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecLocalSaPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecLocalSaEncryptKeyHash"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecLocalSaAuthKeyHash"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecLocalSaIpv6"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityIpsecLocalSaGroup.setStatus("current")

cSdwanSecurityControlConnectionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 16)
)
cSdwanSecurityControlConnectionsGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsVOrgName"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsSystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsProtocol"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsLocalColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRemoteColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsPrivateIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsPrivatePort"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsState"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsLocalEnum"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRemoteEnum"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsLocalStateInfo"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRemoteStateInfo"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsUptime"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxHello"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxConnects"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxRegisters"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxRegisterReplies"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxChallenge"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxChallengeResp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxChallengeAck"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxTeardown"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxTeardownAll"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxVmToPeer"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxRegisterToVm"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxHello"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxConnects"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxRegisters"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxRegisterReplies"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxChallenge"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxChallengeResp"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxChallengeAck"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxTeardown"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxVmToPeer"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxRegisterToVm"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsNegotiatedHelloInterval"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsNegotiatedHelloTolerance"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxCreateCert"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxCreateCert"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsTxCreateCertReply"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsRxCreateCertReply"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsBehindProxy"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsPeerSessId"),
        ("CISCO-SDWAN-SECURITY-MIB", "controlConnectionsLocalInterface"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityControlConnectionsGroup.setStatus("current")

cSdwanSecurityIpsecOutboundConnectionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 17)
)
cSdwanSecurityIpsecOutboundConnectionsGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsTunnelMtu"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsRemoteTlocAddress"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsRemoteTlocColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsAuthenticationUsed"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsEncryptKeyHash"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsAuthKeyHash"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsNegotiatedAlgo"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecOutboundConnectionsTcSpiPerTun"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityIpsecOutboundConnectionsGroup.setStatus("current")

cSdwanSecurityTunnelStatistics = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 18)
)
cSdwanSecurityTunnelStatistics.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsSystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsLocalColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsRemoteColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsTunnelMtu"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsTxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsTxOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsRxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsRxOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIpsecDecryptInbound"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIpsecRxAuthFailures"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIpsecRxFailures"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIpsecEncryptOutbound"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIpsecTxAuthFailures"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIpsecTxFailures"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsTcpMssAdjust"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsBfdTxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsBfdRxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsBfdTxOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsBfdRxOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsPmtuTxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsPmtuRxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsPmtuTxOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsPmtuRxOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIPv6TxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIPv6TxOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIPv6RxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIPv6RxOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsFecRxDataPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsFecRxParityPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsFecTxDataPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsFecTxParityPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsFecReconstructPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsFecCapable"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsFecDynamic"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsPktDupRxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsPktDupRxOtherPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsPktDupRxThisPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsPktDupTxPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsPktDupTxOtherPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsPktDupCapable"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIPv4TxMcPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIPv4TxMcOctets"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIPv4RxMcPkts"),
        ("CISCO-SDWAN-SECURITY-MIB", "tunnelStatisticsIPv4RxMcOctets"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityTunnelStatistics.setStatus("current")

cSdwanSecurityIpsecInboundConnectionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 19)
)
cSdwanSecurityIpsecInboundConnectionsGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsSourceIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsSourcePort"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsDestIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsDestPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsNegEncrAlgo"),
        ("CISCO-SDWAN-SECURITY-MIB", "ipsecInboundConnectionsTcSpiPerTun"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityIpsecInboundConnectionsGroup.setStatus("current")


# Notification objects

ciscoSdwanSecurityControlConnectionStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 1)
)
ciscoSdwanSecurityControlConnectionStateChange.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPersonality"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPeerType"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPeerSystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPeerVmanageSystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPublicIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPublicPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySrcColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityRemoteColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityUptime"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityNewState"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityControlConnectionStateChange.setStatus(
        "current"
    )

ciscoSdwanSecurityControlConnectionAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 2)
)
ciscoSdwanSecurityControlConnectionAuthFail.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPersonality"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPeerType"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPeerSystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityLocalSystemIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityLocalColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityReason"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityControlConnectionAuthFail.setStatus(
        "current"
    )

ciscoSdwanSecurityControlConnectionTlocIpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 3)
)
ciscoSdwanSecurityControlConnectionTlocIpChange.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPersonality"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityOldPublicIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityOldPublicPort"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityNewPublicIp"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityNewPublicPort"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityControlConnectionTlocIpChange.setStatus(
        "current"
    )

ciscoSdwanSecurityControlVbondStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 4)
)
ciscoSdwanSecurityControlVbondStateChange.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPersonality"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityNewState"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityControlVbondStateChange.setStatus(
        "current"
    )

ciscoSdwanSecurityControlNoActiveVsmart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 5)
)
ciscoSdwanSecurityControlNoActiveVsmart.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPersonality"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityControlNoActiveVsmart.setStatus(
        "current"
    )

ciscoSdwanSecurityControlNoActiveVbond = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 6)
)
ciscoSdwanSecurityControlNoActiveVbond.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPersonality"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityControlNoActiveVbond.setStatus(
        "current"
    )

ciscoSdwanSecurityTunnelIpsecRekey = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 7)
)
ciscoSdwanSecurityTunnelIpsecRekey.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPersonality"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityColor"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityTunnelIpsecRekey.setStatus(
        "current"
    )

ciscoSdwanSecurityTunnelIpsecManualRekey = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 8)
)
ciscoSdwanSecurityTunnelIpsecManualRekey.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPersonality"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityColor"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityTunnelIpsecManualRekey.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityRootCertChainInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 9)
)
ciscoSdwanSecuritySecurityRootCertChainInstalled.setObjects(
    ("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity")
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityRootCertChainInstalled.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityCertificateExpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 10)
)
ciscoSdwanSecuritySecurityCertificateExpiring.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityCertificateType"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityCertificateSerialNumber"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityIssuer"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityDaysToExpiry"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityCertificateExpiring.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityCertificateExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 11)
)
ciscoSdwanSecuritySecurityCertificateExpired.setObjects(
    ("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity")
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityCertificateExpired.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityCertificateInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 12)
)
ciscoSdwanSecuritySecurityCertificateInstalled.setObjects(
    ("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity")
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityCertificateInstalled.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityNewCsrGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 13)
)
ciscoSdwanSecuritySecurityNewCsrGenerated.setObjects(
    ("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity")
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityNewCsrGenerated.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityRootCertChainUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 14)
)
ciscoSdwanSecuritySecurityRootCertChainUninstalled.setObjects(
    ("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity")
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityRootCertChainUninstalled.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityClearInstalledCertificate = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 15)
)
ciscoSdwanSecuritySecurityClearInstalledCertificate.setObjects(
    ("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity")
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityClearInstalledCertificate.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityVedgeSerialFileUploaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 16)
)
ciscoSdwanSecuritySecurityVedgeSerialFileUploaded.setObjects(
    ("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity")
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityVedgeSerialFileUploaded.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityVsmartSerialFileUploaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 17)
)
ciscoSdwanSecuritySecurityVsmartSerialFileUploaded.setObjects(
    ("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity")
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityVsmartSerialFileUploaded.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityVedgeEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 18)
)
ciscoSdwanSecuritySecurityVedgeEntryAdded.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityUuid"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySerial"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityVedgeEntryAdded.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityVedgeEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 19)
)
ciscoSdwanSecuritySecurityVedgeEntryRemoved.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityUuid"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityVedgeEntryRemoved.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityVsmartEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 20)
)
ciscoSdwanSecuritySecurityVsmartEntryAdded.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySerial"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityVsmartEntryAdded.setStatus(
        "current"
    )

ciscoSdwanSecuritySecurityVsmartEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 21)
)
ciscoSdwanSecuritySecurityVsmartEntryRemoved.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySerial"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecuritySecurityVsmartEntryRemoved.setStatus(
        "current"
    )

ciscoSdwanSecurityVmanageConnectionPreferenceChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 23)
)
ciscoSdwanSecurityVmanageConnectionPreferenceChanged.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityColor"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityVmanageConnectionPreference"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityVmanageConnectionPreferenceChanged.setStatus(
        "current"
    )

ciscoSdwanSecurityVbondRejectVedgeConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 24)
)
ciscoSdwanSecurityVbondRejectVedgeConnection.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityUuid"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityOrganizationName"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySpOrganizationName"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityReason"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityVbondRejectVedgeConnection.setStatus(
        "current"
    )

ciscoSdwanSecurityDeviceTemplateMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 25)
)
ciscoSdwanSecurityDeviceTemplateMissing.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityUuid"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPeerType"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityDeviceTemplateMissing.setStatus(
        "current"
    )

ciscoSdwanSecurityDeviceTemplateAttachedDuringZtp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 0, 26)
)
ciscoSdwanSecurityDeviceTemplateAttachedDuringZtp.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityUuid"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityPeerType"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityDeviceTemplateAttachedDuringZtp.setStatus(
        "current"
    )


# Notifications groups

cSdwanSecurityNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 2, 3)
)
cSdwanSecurityNotifsGroup.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityControlConnectionStateChange"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityControlConnectionAuthFail"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityControlConnectionTlocIpChange"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityControlVbondStateChange"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityControlNoActiveVsmart"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityControlNoActiveVbond"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityTunnelIpsecRekey"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityTunnelIpsecManualRekey"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityRootCertChainInstalled"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityCertificateExpiring"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityCertificateExpired"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityCertificateInstalled"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityNewCsrGenerated"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityRootCertChainUninstalled"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityClearInstalledCertificate"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityVedgeSerialFileUploaded"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityVsmartSerialFileUploaded"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityVedgeEntryAdded"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityVedgeEntryRemoved"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityVsmartEntryAdded"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecuritySecurityVsmartEntryRemoved"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityVmanageConnectionPreferenceChanged"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityVbondRejectVedgeConnection"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityDeviceTemplateMissing"),
        ("CISCO-SDWAN-SECURITY-MIB", "ciscoSdwanSecurityDeviceTemplateAttachedDuringZtp"))
)
if mibBuilder.loadTexts:
    cSdwanSecurityNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSdwanSecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1006, 3, 1, 1)
)
ciscoSdwanSecurityMIBCompliance.setObjects(
      *(("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityControlConnectionsInfoGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityControlConnectionsGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityControlStatisticsGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityControlLocalPropertiesGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityControlValidVsmartsGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityIpAddressListGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityVbondAddressListGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityWanInterfaceListGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityNotifObjsGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityNotifsGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityControlSummaryGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityAffinityStatusGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityAffinityConfigGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecuritySecurityInfoGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityControlConnectionsHistoryGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityIpsecLocalSaGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityIpsecInboundConnectionsGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityIpsecOutboundConnectionsGroup"),
        ("CISCO-SDWAN-SECURITY-MIB", "cSdwanSecurityTunnelStatistics"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSecurityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDWAN-SECURITY-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "InetAddressIP": InetAddressIP,
       "String": String,
       "NotificationSeverity": NotificationSeverity,
       "PersonalityEnumOper": PersonalityEnumOper,
       "ControlProtocolEnum": ControlProtocolEnum,
       "ColorEnum": ColorEnum,
       "OperState": OperState,
       "CertificateTypeEnum": CertificateTypeEnum,
       "SessionState": SessionState,
       "ConnFlagEnum": ConnFlagEnum,
       "ciscoSdwanSecurityMIB": ciscoSdwanSecurityMIB,
       "ciscoSdwanSecurityMIBNotifs": ciscoSdwanSecurityMIBNotifs,
       "ciscoSdwanSecurityControlConnectionStateChange": ciscoSdwanSecurityControlConnectionStateChange,
       "ciscoSdwanSecurityControlConnectionAuthFail": ciscoSdwanSecurityControlConnectionAuthFail,
       "ciscoSdwanSecurityControlConnectionTlocIpChange": ciscoSdwanSecurityControlConnectionTlocIpChange,
       "ciscoSdwanSecurityControlVbondStateChange": ciscoSdwanSecurityControlVbondStateChange,
       "ciscoSdwanSecurityControlNoActiveVsmart": ciscoSdwanSecurityControlNoActiveVsmart,
       "ciscoSdwanSecurityControlNoActiveVbond": ciscoSdwanSecurityControlNoActiveVbond,
       "ciscoSdwanSecurityTunnelIpsecRekey": ciscoSdwanSecurityTunnelIpsecRekey,
       "ciscoSdwanSecurityTunnelIpsecManualRekey": ciscoSdwanSecurityTunnelIpsecManualRekey,
       "ciscoSdwanSecuritySecurityRootCertChainInstalled": ciscoSdwanSecuritySecurityRootCertChainInstalled,
       "ciscoSdwanSecuritySecurityCertificateExpiring": ciscoSdwanSecuritySecurityCertificateExpiring,
       "ciscoSdwanSecuritySecurityCertificateExpired": ciscoSdwanSecuritySecurityCertificateExpired,
       "ciscoSdwanSecuritySecurityCertificateInstalled": ciscoSdwanSecuritySecurityCertificateInstalled,
       "ciscoSdwanSecuritySecurityNewCsrGenerated": ciscoSdwanSecuritySecurityNewCsrGenerated,
       "ciscoSdwanSecuritySecurityRootCertChainUninstalled": ciscoSdwanSecuritySecurityRootCertChainUninstalled,
       "ciscoSdwanSecuritySecurityClearInstalledCertificate": ciscoSdwanSecuritySecurityClearInstalledCertificate,
       "ciscoSdwanSecuritySecurityVedgeSerialFileUploaded": ciscoSdwanSecuritySecurityVedgeSerialFileUploaded,
       "ciscoSdwanSecuritySecurityVsmartSerialFileUploaded": ciscoSdwanSecuritySecurityVsmartSerialFileUploaded,
       "ciscoSdwanSecuritySecurityVedgeEntryAdded": ciscoSdwanSecuritySecurityVedgeEntryAdded,
       "ciscoSdwanSecuritySecurityVedgeEntryRemoved": ciscoSdwanSecuritySecurityVedgeEntryRemoved,
       "ciscoSdwanSecuritySecurityVsmartEntryAdded": ciscoSdwanSecuritySecurityVsmartEntryAdded,
       "ciscoSdwanSecuritySecurityVsmartEntryRemoved": ciscoSdwanSecuritySecurityVsmartEntryRemoved,
       "ciscoSdwanSecurityVmanageConnectionPreferenceChanged": ciscoSdwanSecurityVmanageConnectionPreferenceChanged,
       "ciscoSdwanSecurityVbondRejectVedgeConnection": ciscoSdwanSecurityVbondRejectVedgeConnection,
       "ciscoSdwanSecurityDeviceTemplateMissing": ciscoSdwanSecurityDeviceTemplateMissing,
       "ciscoSdwanSecurityDeviceTemplateAttachedDuringZtp": ciscoSdwanSecurityDeviceTemplateAttachedDuringZtp,
       "ciscoSdwanSecurityMIBObjects": ciscoSdwanSecurityMIBObjects,
       "control": control,
       "controlConnectionsInfo": controlConnectionsInfo,
       "controlConnectionsInfoRate": controlConnectionsInfoRate,
       "controlConnectionsTable": controlConnectionsTable,
       "controlConnectionsEntry": controlConnectionsEntry,
       "controlConnectionsInstance": controlConnectionsInstance,
       "controlConnectionsPeerType": controlConnectionsPeerType,
       "controlConnectionsSiteId": controlConnectionsSiteId,
       "controlConnectionsDomainId": controlConnectionsDomainId,
       "controlConnectionsLocalPrivateIp": controlConnectionsLocalPrivateIp,
       "controlConnectionsLocalPrivatePort": controlConnectionsLocalPrivatePort,
       "controlConnectionsPublicIp": controlConnectionsPublicIp,
       "controlConnectionsPublicPort": controlConnectionsPublicPort,
       "controlConnectionsSystemIp": controlConnectionsSystemIp,
       "controlConnectionsProtocol": controlConnectionsProtocol,
       "controlConnectionsLocalColor": controlConnectionsLocalColor,
       "controlConnectionsRemoteColor": controlConnectionsRemoteColor,
       "controlConnectionsPrivateIp": controlConnectionsPrivateIp,
       "controlConnectionsPrivatePort": controlConnectionsPrivatePort,
       "controlConnectionsState": controlConnectionsState,
       "controlConnectionsLocalEnum": controlConnectionsLocalEnum,
       "controlConnectionsRemoteEnum": controlConnectionsRemoteEnum,
       "controlConnectionsLocalStateInfo": controlConnectionsLocalStateInfo,
       "controlConnectionsRemoteStateInfo": controlConnectionsRemoteStateInfo,
       "controlConnectionsUptime": controlConnectionsUptime,
       "controlConnectionsTxHello": controlConnectionsTxHello,
       "controlConnectionsTxConnects": controlConnectionsTxConnects,
       "controlConnectionsTxRegisters": controlConnectionsTxRegisters,
       "controlConnectionsTxRegisterReplies": controlConnectionsTxRegisterReplies,
       "controlConnectionsTxChallenge": controlConnectionsTxChallenge,
       "controlConnectionsTxChallengeResp": controlConnectionsTxChallengeResp,
       "controlConnectionsTxChallengeAck": controlConnectionsTxChallengeAck,
       "controlConnectionsTxTeardown": controlConnectionsTxTeardown,
       "controlConnectionsTxTeardownAll": controlConnectionsTxTeardownAll,
       "controlConnectionsTxVmToPeer": controlConnectionsTxVmToPeer,
       "controlConnectionsTxRegisterToVm": controlConnectionsTxRegisterToVm,
       "controlConnectionsRxHello": controlConnectionsRxHello,
       "controlConnectionsRxConnects": controlConnectionsRxConnects,
       "controlConnectionsRxRegisters": controlConnectionsRxRegisters,
       "controlConnectionsRxRegisterReplies": controlConnectionsRxRegisterReplies,
       "controlConnectionsRxChallenge": controlConnectionsRxChallenge,
       "controlConnectionsRxChallengeResp": controlConnectionsRxChallengeResp,
       "controlConnectionsRxChallengeAck": controlConnectionsRxChallengeAck,
       "controlConnectionsRxTeardown": controlConnectionsRxTeardown,
       "controlConnectionsRxVmToPeer": controlConnectionsRxVmToPeer,
       "controlConnectionsRxRegisterToVm": controlConnectionsRxRegisterToVm,
       "controlConnectionsNegotiatedHelloInterval": controlConnectionsNegotiatedHelloInterval,
       "controlConnectionsNegotiatedHelloTolerance": controlConnectionsNegotiatedHelloTolerance,
       "controlConnectionsVOrgName": controlConnectionsVOrgName,
       "controlConnectionsTxCreateCert": controlConnectionsTxCreateCert,
       "controlConnectionsRxCreateCert": controlConnectionsRxCreateCert,
       "controlConnectionsTxCreateCertReply": controlConnectionsTxCreateCertReply,
       "controlConnectionsRxCreateCertReply": controlConnectionsRxCreateCertReply,
       "controlConnectionsBehindProxy": controlConnectionsBehindProxy,
       "controlConnectionsPeerSessId": controlConnectionsPeerSessId,
       "controlConnectionsLocalInterface": controlConnectionsLocalInterface,
       "controlConnectionsHistoryTable": controlConnectionsHistoryTable,
       "controlConnectionsHistoryEntry": controlConnectionsHistoryEntry,
       "controlConnectionsHistoryInstance": controlConnectionsHistoryInstance,
       "controlConnectionsHistoryIndex": controlConnectionsHistoryIndex,
       "controlConnectionsHistoryPeerType": controlConnectionsHistoryPeerType,
       "controlConnectionsHistorySiteId": controlConnectionsHistorySiteId,
       "controlConnectionsHistoryDomainId": controlConnectionsHistoryDomainId,
       "controlConnectionsHistoryPrivateIp": controlConnectionsHistoryPrivateIp,
       "controlConnectionsHistoryPrivatePort": controlConnectionsHistoryPrivatePort,
       "controlConnectionsHistoryPublicIp": controlConnectionsHistoryPublicIp,
       "controlConnectionsHistoryPublicPort": controlConnectionsHistoryPublicPort,
       "controlConnectionsHistorySystemIp": controlConnectionsHistorySystemIp,
       "controlConnectionsHistoryProtocol": controlConnectionsHistoryProtocol,
       "controlConnectionsHistoryLocalColor": controlConnectionsHistoryLocalColor,
       "controlConnectionsHistoryRemoteColor": controlConnectionsHistoryRemoteColor,
       "controlConnectionsHistoryState": controlConnectionsHistoryState,
       "controlConnectionsHistoryLocalEnum": controlConnectionsHistoryLocalEnum,
       "controlConnectionsHistoryRemoteEnum": controlConnectionsHistoryRemoteEnum,
       "controlConnectionsHistoryLocalStateInfo": controlConnectionsHistoryLocalStateInfo,
       "controlConnectionsHistoryRemoteStateInfo": controlConnectionsHistoryRemoteStateInfo,
       "controlConnectionsHistoryDowntime": controlConnectionsHistoryDowntime,
       "controlConnectionsHistoryTxHello": controlConnectionsHistoryTxHello,
       "controlConnectionsHistoryTxConnects": controlConnectionsHistoryTxConnects,
       "controlConnectionsHistoryTxRegisters": controlConnectionsHistoryTxRegisters,
       "controlConnectionsHistoryTxRegisterReplies": controlConnectionsHistoryTxRegisterReplies,
       "controlConnectionsHistoryTxChallenge": controlConnectionsHistoryTxChallenge,
       "controlConnectionsHistoryTxChallengeResp": controlConnectionsHistoryTxChallengeResp,
       "controlConnectionsHistoryTxChallengeAck": controlConnectionsHistoryTxChallengeAck,
       "controlConnectionsHistoryTxTeardown": controlConnectionsHistoryTxTeardown,
       "controlConnectionsHistoryTxTeardownAll": controlConnectionsHistoryTxTeardownAll,
       "controlConnectionsHistoryTxVmToPeer": controlConnectionsHistoryTxVmToPeer,
       "controlConnectionsHistoryTxRegisterToVm": controlConnectionsHistoryTxRegisterToVm,
       "controlConnectionsHistoryRxHello": controlConnectionsHistoryRxHello,
       "controlConnectionsHistoryRxConnects": controlConnectionsHistoryRxConnects,
       "controlConnectionsHistoryRxRegisters": controlConnectionsHistoryRxRegisters,
       "controlConnectionsHistoryRxRegisterReplies": controlConnectionsHistoryRxRegisterReplies,
       "controlConnectionsHistoryRxChallenge": controlConnectionsHistoryRxChallenge,
       "controlConnectionsHistoryRxChallengeResp": controlConnectionsHistoryRxChallengeResp,
       "controlConnectionsHistoryRxChallengeAck": controlConnectionsHistoryRxChallengeAck,
       "controlConnectionsHistoryRxTeardown": controlConnectionsHistoryRxTeardown,
       "controlConnectionsHistoryRxVmToPeer": controlConnectionsHistoryRxVmToPeer,
       "controlConnectionsHistoryRxRegisterToVm": controlConnectionsHistoryRxRegisterToVm,
       "controlConnectionsHistoryRepCount": controlConnectionsHistoryRepCount,
       "controlConnectionsHistoryPrevDowntime": controlConnectionsHistoryPrevDowntime,
       "controlConnectionsHistoryVHOrgName": controlConnectionsHistoryVHOrgName,
       "controlConnectionsHistoryUuid": controlConnectionsHistoryUuid,
       "controlConnectionsHistoryTxCreateCert": controlConnectionsHistoryTxCreateCert,
       "controlConnectionsHistoryRxCreateCert": controlConnectionsHistoryRxCreateCert,
       "controlConnectionsHistoryTxCreateCertReply": controlConnectionsHistoryTxCreateCertReply,
       "controlConnectionsHistoryRxCreateCertReply": controlConnectionsHistoryRxCreateCertReply,
       "controlConnectionsHistoryLocalInterface": controlConnectionsHistoryLocalInterface,
       "controlStatistics": controlStatistics,
       "controlStatisticsTxPkts": controlStatisticsTxPkts,
       "controlStatisticsTxOctets": controlStatisticsTxOctets,
       "controlStatisticsTxError": controlStatisticsTxError,
       "controlStatisticsTxBlocked": controlStatisticsTxBlocked,
       "controlStatisticsTxHello": controlStatisticsTxHello,
       "controlStatisticsTxConnects": controlStatisticsTxConnects,
       "controlStatisticsTxRegisters": controlStatisticsTxRegisters,
       "controlStatisticsTxRegisterReplies": controlStatisticsTxRegisterReplies,
       "controlStatisticsTxDtlsHandshake": controlStatisticsTxDtlsHandshake,
       "controlStatisticsTxDtlsHandshakeFailures": controlStatisticsTxDtlsHandshakeFailures,
       "controlStatisticsTxDtlsHandshakeDone": controlStatisticsTxDtlsHandshakeDone,
       "controlStatisticsTxChallenge": controlStatisticsTxChallenge,
       "controlStatisticsTxChallengeResp": controlStatisticsTxChallengeResp,
       "controlStatisticsTxChallengeAck": controlStatisticsTxChallengeAck,
       "controlStatisticsTxChallengeError": controlStatisticsTxChallengeError,
       "controlStatisticsTxChallengeRespError": controlStatisticsTxChallengeRespError,
       "controlStatisticsTxChallengeAckError": controlStatisticsTxChallengeAckError,
       "controlStatisticsTxChallengeGenError": controlStatisticsTxChallengeGenError,
       "controlStatisticsTxVmanageToPeer": controlStatisticsTxVmanageToPeer,
       "controlStatisticsTxRegisterToVmanage": controlStatisticsTxRegisterToVmanage,
       "controlStatisticsRxPkts": controlStatisticsRxPkts,
       "controlStatisticsRxOctets": controlStatisticsRxOctets,
       "controlStatisticsRxError": controlStatisticsRxError,
       "controlStatisticsRxHello": controlStatisticsRxHello,
       "controlStatisticsRxConnects": controlStatisticsRxConnects,
       "controlStatisticsRxRegisters": controlStatisticsRxRegisters,
       "controlStatisticsRxRegisterReplies": controlStatisticsRxRegisterReplies,
       "controlStatisticsRxDtlsHandshake": controlStatisticsRxDtlsHandshake,
       "controlStatisticsRxDtlsHandshakeFailures": controlStatisticsRxDtlsHandshakeFailures,
       "controlStatisticsRxDtlsHandshakeDone": controlStatisticsRxDtlsHandshakeDone,
       "controlStatisticsRxChallenge": controlStatisticsRxChallenge,
       "controlStatisticsRxChallengeResp": controlStatisticsRxChallengeResp,
       "controlStatisticsRxChallengeAck": controlStatisticsRxChallengeAck,
       "controlStatisticsChallengeFailures": controlStatisticsChallengeFailures,
       "controlStatisticsRxVmanageToPeer": controlStatisticsRxVmanageToPeer,
       "controlStatisticsRxRegisterToVmanage": controlStatisticsRxRegisterToVmanage,
       "controlStatisticsBidFailuresNeedingReset": controlStatisticsBidFailuresNeedingReset,
       "controlLocalProperties": controlLocalProperties,
       "controlLocalPropertiesDeviceType": controlLocalPropertiesDeviceType,
       "controlLocalPropertiesOrganizationName": controlLocalPropertiesOrganizationName,
       "controlLocalPropertiesCertificateStatus": controlLocalPropertiesCertificateStatus,
       "controlLocalPropertiesRootCaChainStatus": controlLocalPropertiesRootCaChainStatus,
       "controlLocalPropertiesCertificateValidity": controlLocalPropertiesCertificateValidity,
       "controlLocalPropertiesCertificateNotValidBefore": controlLocalPropertiesCertificateNotValidBefore,
       "controlLocalPropertiesCertificateNotValidAfter": controlLocalPropertiesCertificateNotValidAfter,
       "controlLocalPropertiesDnsName": controlLocalPropertiesDnsName,
       "controlLocalPropertiesSiteId": controlLocalPropertiesSiteId,
       "controlLocalPropertiesDomainId": controlLocalPropertiesDomainId,
       "controlLocalPropertiesTlsPort": controlLocalPropertiesTlsPort,
       "controlLocalPropertiesSystemIp": controlLocalPropertiesSystemIp,
       "controlLocalPropertiesUuid": controlLocalPropertiesUuid,
       "controlLocalPropertiesBoardSerial": controlLocalPropertiesBoardSerial,
       "controlLocalPropertiesRegisterInterval": controlLocalPropertiesRegisterInterval,
       "controlLocalPropertiesRetryInterval": controlLocalPropertiesRetryInterval,
       "controlLocalPropertiesNoActivity": controlLocalPropertiesNoActivity,
       "controlLocalPropertiesDnsCacheFlushInterval": controlLocalPropertiesDnsCacheFlushInterval,
       "controlLocalPropertiesPortHopped": controlLocalPropertiesPortHopped,
       "controlLocalPropertiesTimeSincePortHop": controlLocalPropertiesTimeSincePortHop,
       "controlLocalPropertiesMaxControllers": controlLocalPropertiesMaxControllers,
       "controlLocalPropertiesKeygenInterval": controlLocalPropertiesKeygenInterval,
       "controlLocalPropertiesIpAddressListTable": controlLocalPropertiesIpAddressListTable,
       "controlLocalPropertiesIpAddressListEntry": controlLocalPropertiesIpAddressListEntry,
       "controlLocalPropertiesIpAddressListIndex": controlLocalPropertiesIpAddressListIndex,
       "controlLocalPropertiesIpAddressListIp": controlLocalPropertiesIpAddressListIp,
       "controlLocalPropertiesIpAddressListPort": controlLocalPropertiesIpAddressListPort,
       "controlLocalPropertiesNumberVbondPeers": controlLocalPropertiesNumberVbondPeers,
       "controlLocalPropertiesVbondAddressListTable": controlLocalPropertiesVbondAddressListTable,
       "controlLocalPropertiesVbondAddressListEntry": controlLocalPropertiesVbondAddressListEntry,
       "controlLocalPropertiesVbondAddressListIndex": controlLocalPropertiesVbondAddressListIndex,
       "controlLocalPropertiesVbondAddressListIp": controlLocalPropertiesVbondAddressListIp,
       "controlLocalPropertiesVbondAddressListPort": controlLocalPropertiesVbondAddressListPort,
       "controlLocalPropertiesNumberActiveWanInterfaces": controlLocalPropertiesNumberActiveWanInterfaces,
       "controlLocalPropertiesWanInterfaceListTable": controlLocalPropertiesWanInterfaceListTable,
       "controlLocalPropertiesWanInterfaceListEntry": controlLocalPropertiesWanInterfaceListEntry,
       "controlLocalPropertiesWanInterfaceListIndex": controlLocalPropertiesWanInterfaceListIndex,
       "controlLocalPropertiesWanInterfaceListInterface": controlLocalPropertiesWanInterfaceListInterface,
       "controlLocalPropertiesWanInterfaceListPublicIp": controlLocalPropertiesWanInterfaceListPublicIp,
       "controlLocalPropertiesWanInterfaceListPublicPort": controlLocalPropertiesWanInterfaceListPublicPort,
       "controlLocalPropertiesWanInterfaceListPrivateIp": controlLocalPropertiesWanInterfaceListPrivateIp,
       "controlLocalPropertiesWanInterfaceListPrivatePort": controlLocalPropertiesWanInterfaceListPrivatePort,
       "controlLocalPropertiesWanInterfaceListNumVsmarts": controlLocalPropertiesWanInterfaceListNumVsmarts,
       "controlLocalPropertiesWanInterfaceListNumVmanages": controlLocalPropertiesWanInterfaceListNumVmanages,
       "controlLocalPropertiesWanInterfaceListWeight": controlLocalPropertiesWanInterfaceListWeight,
       "controlLocalPropertiesWanInterfaceListColor": controlLocalPropertiesWanInterfaceListColor,
       "controlLocalPropertiesWanInterfaceListCarrier": controlLocalPropertiesWanInterfaceListCarrier,
       "controlLocalPropertiesWanInterfaceListPreference": controlLocalPropertiesWanInterfaceListPreference,
       "controlLocalPropertiesWanInterfaceListAdminState": controlLocalPropertiesWanInterfaceListAdminState,
       "controlLocalPropertiesWanInterfaceListOperationState": controlLocalPropertiesWanInterfaceListOperationState,
       "controlLocalPropertiesWanInterfaceListLastConnTime": controlLocalPropertiesWanInterfaceListLastConnTime,
       "controlLocalPropertiesWanInterfaceListRestrictStr": controlLocalPropertiesWanInterfaceListRestrictStr,
       "controlLocalPropertiesWanInterfaceListControlStr": controlLocalPropertiesWanInterfaceListControlStr,
       "controlLocalPropertiesWanInterfaceListPerWanMaxControllers": controlLocalPropertiesWanInterfaceListPerWanMaxControllers,
       "controlLocalPropertiesWanInterfaceListInstance": controlLocalPropertiesWanInterfaceListInstance,
       "controlLocalPropertiesWanInterfaceListPrivateIpv6": controlLocalPropertiesWanInterfaceListPrivateIpv6,
       "controlLocalPropertiesWanInterfaceListSpiChange": controlLocalPropertiesWanInterfaceListSpiChange,
       "controlLocalPropertiesWanInterfaceListLastResort": controlLocalPropertiesWanInterfaceListLastResort,
       "controlLocalPropertiesWanInterfaceListWanPortHopped": controlLocalPropertiesWanInterfaceListWanPortHopped,
       "controlLocalPropertiesWanInterfaceListWanTimeSincePortHop": controlLocalPropertiesWanInterfaceListWanTimeSincePortHop,
       "controlLocalPropertiesWanInterfaceListVbondAsStunServer": controlLocalPropertiesWanInterfaceListVbondAsStunServer,
       "controlLocalPropertiesWanInterfaceListVmanageConnPreference": controlLocalPropertiesWanInterfaceListVmanageConnPreference,
       "controlLocalPropertiesWanInterfaceListLowBandwidthLink": controlLocalPropertiesWanInterfaceListLowBandwidthLink,
       "controlLocalPropertiesWanInterfaceListNatType": controlLocalPropertiesWanInterfaceListNatType,
       "controlLocalPropertiesWanInterfaceListInterfaceAdminState": controlLocalPropertiesWanInterfaceListInterfaceAdminState,
       "controlLocalPropertiesWanInterfaceListInterfaceOperState": controlLocalPropertiesWanInterfaceListInterfaceOperState,
       "controlLocalPropertiesWanInterfaceListRegionId": controlLocalPropertiesWanInterfaceListRegionId,
       "controlLocalPropertiesVsmartListVersion": controlLocalPropertiesVsmartListVersion,
       "controlLocalPropertiesSPOrganizationName": controlLocalPropertiesSPOrganizationName,
       "controlLocalPropertiesToken": controlLocalPropertiesToken,
       "controlLocalPropertiesEmbargoCheck": controlLocalPropertiesEmbargoCheck,
       "controlLocalPropertiesEnterpriseSerial": controlLocalPropertiesEnterpriseSerial,
       "controlLocalPropertiesEnterpriseCertificateStatus": controlLocalPropertiesEnterpriseCertificateStatus,
       "controlLocalPropertiesEnterpriseCertificateValidity": controlLocalPropertiesEnterpriseCertificateValidity,
       "controlLocalPropertiesEnterpriseCertificateNotValidBefore": controlLocalPropertiesEnterpriseCertificateNotValidBefore,
       "controlLocalPropertiesEnterpriseCertificateNotValidAfter": controlLocalPropertiesEnterpriseCertificateNotValidAfter,
       "controlLocalPropertiesRootCaCrlStatus": controlLocalPropertiesRootCaCrlStatus,
       "controlLocalPropertiesPairwiseKeying": controlLocalPropertiesPairwiseKeying,
       "controlLocalPropertiesSubjectSerialNumber": controlLocalPropertiesSubjectSerialNumber,
       "controlLocalPropertiesProtocol": controlLocalPropertiesProtocol,
       "controlValidVsmartsTable": controlValidVsmartsTable,
       "controlValidVsmartsEntry": controlValidVsmartsEntry,
       "controlValidVsmartsSerialNumber": controlValidVsmartsSerialNumber,
       "controlValidVsmartsOrg": controlValidVsmartsOrg,
       "controlSummaryTable": controlSummaryTable,
       "controlSummaryEntry": controlSummaryEntry,
       "controlSummaryInstance": controlSummaryInstance,
       "controlSummaryVbondCounts": controlSummaryVbondCounts,
       "controlSummaryVmanageCounts": controlSummaryVmanageCounts,
       "controlSummaryVsmartCounts": controlSummaryVsmartCounts,
       "controlSummaryVedgeCounts": controlSummaryVedgeCounts,
       "controlSummaryProtocol": controlSummaryProtocol,
       "controlSummaryListeningIp": controlSummaryListeningIp,
       "controlSummaryListeningPort": controlSummaryListeningPort,
       "controlSummaryListeningIpv6": controlSummaryListeningIpv6,
       "controlSummaryValidControllerCounts": controlSummaryValidControllerCounts,
       "controlAffinity": controlAffinity,
       "controlAffinityConfigTable": controlAffinityConfigTable,
       "controlAffinityConfigEntry": controlAffinityConfigEntry,
       "controlAffinityConfigAffcIndex": controlAffinityConfigAffcIndex,
       "controlAffinityConfigAffcInterface": controlAffinityConfigAffcInterface,
       "controlAffinityConfigAffcErvc": controlAffinityConfigAffcErvc,
       "controlAffinityConfigAffcEcl": controlAffinityConfigAffcEcl,
       "controlAffinityConfigAffcCcl": controlAffinityConfigAffcCcl,
       "controlAffinityConfigAffcEquil": controlAffinityConfigAffcEquil,
       "controlAffinityConfigAffcLastResort": controlAffinityConfigAffcLastResort,
       "controlAffinityConfigAffcTenantCount": controlAffinityConfigAffcTenantCount,
       "controlAffinityStatusTable": controlAffinityStatusTable,
       "controlAffinityStatusEntry": controlAffinityStatusEntry,
       "controlAffinityStatusAffsIndex": controlAffinityStatusAffsIndex,
       "controlAffinityStatusAffsAcc": controlAffinityStatusAffsAcc,
       "controlAffinityStatusAffsInterface": controlAffinityStatusAffsInterface,
       "controlAffinityStatusAffsUcc": controlAffinityStatusAffsUcc,
       "controlAffinityStatusAffsAc": controlAffinityStatusAffsAc,
       "ipsec": ipsec,
       "ipsecLocalSaTable": ipsecLocalSaTable,
       "ipsecLocalSaEntry": ipsecLocalSaEntry,
       "ipsecLocalSaTlocAddress": ipsecLocalSaTlocAddress,
       "ipsecLocalSaTlocColor": ipsecLocalSaTlocColor,
       "ipsecLocalSaSpi": ipsecLocalSaSpi,
       "ipsecLocalSaTlocIndex": ipsecLocalSaTlocIndex,
       "ipsecLocalSaIp": ipsecLocalSaIp,
       "ipsecLocalSaPort": ipsecLocalSaPort,
       "ipsecLocalSaEncryptKeyHash": ipsecLocalSaEncryptKeyHash,
       "ipsecLocalSaAuthKeyHash": ipsecLocalSaAuthKeyHash,
       "ipsecLocalSaIpv6": ipsecLocalSaIpv6,
       "ipsecInboundConnectionsTable": ipsecInboundConnectionsTable,
       "ipsecInboundConnectionsEntry": ipsecInboundConnectionsEntry,
       "ipsecInboundConnectionsLocalTlocAddress": ipsecInboundConnectionsLocalTlocAddress,
       "ipsecInboundConnectionsLocalTlocColor": ipsecInboundConnectionsLocalTlocColor,
       "ipsecInboundConnectionsRemoteTlocAddress": ipsecInboundConnectionsRemoteTlocAddress,
       "ipsecInboundConnectionsRemoteTlocColor": ipsecInboundConnectionsRemoteTlocColor,
       "ipsecInboundConnectionsLocalTlocIndex": ipsecInboundConnectionsLocalTlocIndex,
       "ipsecInboundConnectionsRemoteTlocIndex": ipsecInboundConnectionsRemoteTlocIndex,
       "ipsecInboundConnectionsSourceIp": ipsecInboundConnectionsSourceIp,
       "ipsecInboundConnectionsSourcePort": ipsecInboundConnectionsSourcePort,
       "ipsecInboundConnectionsDestIp": ipsecInboundConnectionsDestIp,
       "ipsecInboundConnectionsDestPort": ipsecInboundConnectionsDestPort,
       "ipsecInboundConnectionsNegEncrAlgo": ipsecInboundConnectionsNegEncrAlgo,
       "ipsecInboundConnectionsTcSpiPerTun": ipsecInboundConnectionsTcSpiPerTun,
       "ipsecOutboundConnectionsTable": ipsecOutboundConnectionsTable,
       "ipsecOutboundConnectionsEntry": ipsecOutboundConnectionsEntry,
       "ipsecOutboundConnectionsSourceIp": ipsecOutboundConnectionsSourceIp,
       "ipsecOutboundConnectionsSourcePort": ipsecOutboundConnectionsSourcePort,
       "ipsecOutboundConnectionsDestIp": ipsecOutboundConnectionsDestIp,
       "ipsecOutboundConnectionsDestPort": ipsecOutboundConnectionsDestPort,
       "ipsecOutboundConnectionsSpi": ipsecOutboundConnectionsSpi,
       "ipsecOutboundConnectionsTlocIndex": ipsecOutboundConnectionsTlocIndex,
       "ipsecOutboundConnectionsTunnelMtu": ipsecOutboundConnectionsTunnelMtu,
       "ipsecOutboundConnectionsRemoteTlocAddress": ipsecOutboundConnectionsRemoteTlocAddress,
       "ipsecOutboundConnectionsRemoteTlocColor": ipsecOutboundConnectionsRemoteTlocColor,
       "ipsecOutboundConnectionsAuthenticationUsed": ipsecOutboundConnectionsAuthenticationUsed,
       "ipsecOutboundConnectionsEncryptKeyHash": ipsecOutboundConnectionsEncryptKeyHash,
       "ipsecOutboundConnectionsAuthKeyHash": ipsecOutboundConnectionsAuthKeyHash,
       "ipsecOutboundConnectionsNegotiatedAlgo": ipsecOutboundConnectionsNegotiatedAlgo,
       "ipsecOutboundConnectionsTcSpiPerTun": ipsecOutboundConnectionsTcSpiPerTun,
       "tunnel": tunnel,
       "tunnelStatisticsTable": tunnelStatisticsTable,
       "tunnelStatisticsEntry": tunnelStatisticsEntry,
       "tunnelStatisticsTunnelProtocol": tunnelStatisticsTunnelProtocol,
       "tunnelStatisticsSourceIp": tunnelStatisticsSourceIp,
       "tunnelStatisticsDestIp": tunnelStatisticsDestIp,
       "tunnelStatisticsSourcePort": tunnelStatisticsSourcePort,
       "tunnelStatisticsDestPort": tunnelStatisticsDestPort,
       "tunnelStatisticsSystemIp": tunnelStatisticsSystemIp,
       "tunnelStatisticsLocalColor": tunnelStatisticsLocalColor,
       "tunnelStatisticsRemoteColor": tunnelStatisticsRemoteColor,
       "tunnelStatisticsTunnelMtu": tunnelStatisticsTunnelMtu,
       "tunnelStatisticsTxPkts": tunnelStatisticsTxPkts,
       "tunnelStatisticsTxOctets": tunnelStatisticsTxOctets,
       "tunnelStatisticsRxPkts": tunnelStatisticsRxPkts,
       "tunnelStatisticsRxOctets": tunnelStatisticsRxOctets,
       "tunnelStatisticsIpsecDecryptInbound": tunnelStatisticsIpsecDecryptInbound,
       "tunnelStatisticsIpsecRxAuthFailures": tunnelStatisticsIpsecRxAuthFailures,
       "tunnelStatisticsIpsecRxFailures": tunnelStatisticsIpsecRxFailures,
       "tunnelStatisticsIpsecEncryptOutbound": tunnelStatisticsIpsecEncryptOutbound,
       "tunnelStatisticsIpsecTxAuthFailures": tunnelStatisticsIpsecTxAuthFailures,
       "tunnelStatisticsIpsecTxFailures": tunnelStatisticsIpsecTxFailures,
       "tunnelStatisticsTcpMssAdjust": tunnelStatisticsTcpMssAdjust,
       "tunnelStatisticsBfdTxPkts": tunnelStatisticsBfdTxPkts,
       "tunnelStatisticsBfdRxPkts": tunnelStatisticsBfdRxPkts,
       "tunnelStatisticsBfdTxOctets": tunnelStatisticsBfdTxOctets,
       "tunnelStatisticsBfdRxOctets": tunnelStatisticsBfdRxOctets,
       "tunnelStatisticsPmtuTxPkts": tunnelStatisticsPmtuTxPkts,
       "tunnelStatisticsPmtuRxPkts": tunnelStatisticsPmtuRxPkts,
       "tunnelStatisticsPmtuTxOctets": tunnelStatisticsPmtuTxOctets,
       "tunnelStatisticsPmtuRxOctets": tunnelStatisticsPmtuRxOctets,
       "tunnelStatisticsIPv6TxPkts": tunnelStatisticsIPv6TxPkts,
       "tunnelStatisticsIPv6TxOctets": tunnelStatisticsIPv6TxOctets,
       "tunnelStatisticsIPv6RxPkts": tunnelStatisticsIPv6RxPkts,
       "tunnelStatisticsIPv6RxOctets": tunnelStatisticsIPv6RxOctets,
       "tunnelStatisticsFecRxDataPkts": tunnelStatisticsFecRxDataPkts,
       "tunnelStatisticsFecRxParityPkts": tunnelStatisticsFecRxParityPkts,
       "tunnelStatisticsFecTxDataPkts": tunnelStatisticsFecTxDataPkts,
       "tunnelStatisticsFecTxParityPkts": tunnelStatisticsFecTxParityPkts,
       "tunnelStatisticsFecReconstructPkts": tunnelStatisticsFecReconstructPkts,
       "tunnelStatisticsFecCapable": tunnelStatisticsFecCapable,
       "tunnelStatisticsFecDynamic": tunnelStatisticsFecDynamic,
       "tunnelStatisticsPktDupRxPkts": tunnelStatisticsPktDupRxPkts,
       "tunnelStatisticsPktDupRxOtherPkts": tunnelStatisticsPktDupRxOtherPkts,
       "tunnelStatisticsPktDupRxThisPkts": tunnelStatisticsPktDupRxThisPkts,
       "tunnelStatisticsPktDupTxPkts": tunnelStatisticsPktDupTxPkts,
       "tunnelStatisticsPktDupTxOtherPkts": tunnelStatisticsPktDupTxOtherPkts,
       "tunnelStatisticsPktDupCapable": tunnelStatisticsPktDupCapable,
       "tunnelStatisticsIPv4TxMcPkts": tunnelStatisticsIPv4TxMcPkts,
       "tunnelStatisticsIPv4TxMcOctets": tunnelStatisticsIPv4TxMcOctets,
       "tunnelStatisticsIPv4RxMcPkts": tunnelStatisticsIPv4RxMcPkts,
       "tunnelStatisticsIPv4RxMcOctets": tunnelStatisticsIPv4RxMcOctets,
       "securityInfo": securityInfo,
       "securityInfoRekey": securityInfoRekey,
       "securityInfoReplayWindow": securityInfoReplayWindow,
       "securityInfoEncryptionSupported": securityInfoEncryptionSupported,
       "securityInfoFipsMode": securityInfoFipsMode,
       "securityInfoPairwiseKeying": securityInfoPairwiseKeying,
       "securityInfoPwkSymRekey": securityInfoPwkSymRekey,
       "securityInfoExtendedAntiReplayWindow": securityInfoExtendedAntiReplayWindow,
       "securityInfoIntegrityType": securityInfoIntegrityType,
       "ciscoSdwanSecurityMIBNotifObjects": ciscoSdwanSecurityMIBNotifObjects,
       "netconfNotificationSeverity": netconfNotificationSeverity,
       "ciscoSdwanSecurityPersonality": ciscoSdwanSecurityPersonality,
       "ciscoSdwanSecurityPeerType": ciscoSdwanSecurityPeerType,
       "ciscoSdwanSecurityPeerSystemIp": ciscoSdwanSecurityPeerSystemIp,
       "ciscoSdwanSecurityPeerVmanageSystemIp": ciscoSdwanSecurityPeerVmanageSystemIp,
       "ciscoSdwanSecurityPublicIp": ciscoSdwanSecurityPublicIp,
       "ciscoSdwanSecurityPublicPort": ciscoSdwanSecurityPublicPort,
       "ciscoSdwanSecuritySrcColor": ciscoSdwanSecuritySrcColor,
       "ciscoSdwanSecurityRemoteColor": ciscoSdwanSecurityRemoteColor,
       "ciscoSdwanSecurityUptime": ciscoSdwanSecurityUptime,
       "ciscoSdwanSecurityNewState": ciscoSdwanSecurityNewState,
       "ciscoSdwanSecurityLocalSystemIp": ciscoSdwanSecurityLocalSystemIp,
       "ciscoSdwanSecurityLocalColor": ciscoSdwanSecurityLocalColor,
       "ciscoSdwanSecurityReason": ciscoSdwanSecurityReason,
       "ciscoSdwanSecurityOldPublicIp": ciscoSdwanSecurityOldPublicIp,
       "ciscoSdwanSecurityOldPublicPort": ciscoSdwanSecurityOldPublicPort,
       "ciscoSdwanSecurityNewPublicIp": ciscoSdwanSecurityNewPublicIp,
       "ciscoSdwanSecurityNewPublicPort": ciscoSdwanSecurityNewPublicPort,
       "ciscoSdwanSecurityColor": ciscoSdwanSecurityColor,
       "ciscoSdwanSecurityUuid": ciscoSdwanSecurityUuid,
       "ciscoSdwanSecuritySerial": ciscoSdwanSecuritySerial,
       "ciscoSdwanSecurityVmanageConnectionPreference": ciscoSdwanSecurityVmanageConnectionPreference,
       "ciscoSdwanSecurityOrganizationName": ciscoSdwanSecurityOrganizationName,
       "ciscoSdwanSecuritySpOrganizationName": ciscoSdwanSecuritySpOrganizationName,
       "ciscoSdwanSecurityCertificateType": ciscoSdwanSecurityCertificateType,
       "ciscoSdwanSecurityCertificateSerialNumber": ciscoSdwanSecurityCertificateSerialNumber,
       "ciscoSdwanSecurityIssuer": ciscoSdwanSecurityIssuer,
       "ciscoSdwanSecurityDaysToExpiry": ciscoSdwanSecurityDaysToExpiry,
       "ciscoSdwanSecurityMIBConform": ciscoSdwanSecurityMIBConform,
       "ciscoSdwanSecurityMIBCompliances": ciscoSdwanSecurityMIBCompliances,
       "ciscoSdwanSecurityMIBCompliance": ciscoSdwanSecurityMIBCompliance,
       "ciscoSdwanSecurityMIBGroups": ciscoSdwanSecurityMIBGroups,
       "cSdwanSecurityControlLocalPropertiesGroup": cSdwanSecurityControlLocalPropertiesGroup,
       "cSdwanSecurityNotifObjsGroup": cSdwanSecurityNotifObjsGroup,
       "cSdwanSecurityNotifsGroup": cSdwanSecurityNotifsGroup,
       "cSdwanSecurityControlSummaryGroup": cSdwanSecurityControlSummaryGroup,
       "cSdwanSecurityAffinityConfigGroup": cSdwanSecurityAffinityConfigGroup,
       "cSdwanSecurityIpAddressListGroup": cSdwanSecurityIpAddressListGroup,
       "cSdwanSecurityVbondAddressListGroup": cSdwanSecurityVbondAddressListGroup,
       "cSdwanSecurityAffinityStatusGroup": cSdwanSecurityAffinityStatusGroup,
       "cSdwanSecurityControlConnectionsInfoGroup": cSdwanSecurityControlConnectionsInfoGroup,
       "cSdwanSecuritySecurityInfoGroup": cSdwanSecuritySecurityInfoGroup,
       "cSdwanSecurityWanInterfaceListGroup": cSdwanSecurityWanInterfaceListGroup,
       "cSdwanSecurityControlStatisticsGroup": cSdwanSecurityControlStatisticsGroup,
       "cSdwanSecurityControlValidVsmartsGroup": cSdwanSecurityControlValidVsmartsGroup,
       "cSdwanSecurityControlConnectionsHistoryGroup": cSdwanSecurityControlConnectionsHistoryGroup,
       "cSdwanSecurityIpsecLocalSaGroup": cSdwanSecurityIpsecLocalSaGroup,
       "cSdwanSecurityControlConnectionsGroup": cSdwanSecurityControlConnectionsGroup,
       "cSdwanSecurityIpsecOutboundConnectionsGroup": cSdwanSecurityIpsecOutboundConnectionsGroup,
       "cSdwanSecurityTunnelStatistics": cSdwanSecurityTunnelStatistics,
       "cSdwanSecurityIpsecInboundConnectionsGroup": cSdwanSecurityIpsecInboundConnectionsGroup}
)
