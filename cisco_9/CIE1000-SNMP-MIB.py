# SNMP MIB module (CIE1000-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-SNMP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000DisplayString,
 CIE1000InetAddress,
 CIE1000RowEditorState,
 CIE1000Unsigned16) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000InetAddress",
    "CIE1000RowEditorState",
    "CIE1000Unsigned16")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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

cie1000SnmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36)
)
if mibBuilder.loadTexts:
    cie1000SnmpMib.setRevisions(
        ("2016-04-06 00:00",
         "2016-03-07 00:00",
         "2016-02-23 00:00",
         "2016-02-11 00:00",
         "2015-12-11 00:00",
         "2015-07-24 00:00",
         "2014-07-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000SnmpAuthProtocl(TextualConvention, Integer32):
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
        *(("snmpNoAuthProtocol", 0),
          ("snmpMD5AuthProtocol", 1),
          ("snmpSHAAuthProtocol", 2))
    )



class CIE1000SnmpPrivProtocl(TextualConvention, Integer32):
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
        *(("snmpNoPrivProtocol", 0),
          ("snmpDESPrivProtocol", 1),
          ("snmpAESPrivProtocol", 2))
    )



class CIE1000SnmpSecurityLevel(TextualConvention, Integer32):
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
        *(("snmpNoAuthNoPriv", 1),
          ("snmpAuthNoPriv", 2),
          ("snmpAuthPriv", 3))
    )



class CIE1000SnmpSecurityModel(TextualConvention, Integer32):
    status = "current"
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
        *(("any", 0),
          ("v1", 1),
          ("v2c", 2),
          ("usm", 3))
    )



class CIE1000SnmpTrapNotifyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trap", 0),
          ("inform", 1))
    )



class CIE1000SnmpVersion(TextualConvention, Integer32):
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
        *(("snmpV1", 0),
          ("snmpV2c", 1),
          ("snmpV3", 2))
    )



class CIE1000SnmpViewType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("included", 0),
          ("excluded", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000SnmpMibObjects_ObjectIdentity = ObjectIdentity
cie1000SnmpMibObjects = _Cie1000SnmpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1)
)
_Cie1000SnmpConfig_ObjectIdentity = ObjectIdentity
cie1000SnmpConfig = _Cie1000SnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2)
)
_Cie1000SnmpConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000SnmpConfigGlobals = _Cie1000SnmpConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 1)
)
_Cie1000SnmpConfigGlobalsMode_Type = TruthValue
_Cie1000SnmpConfigGlobalsMode_Object = MibScalar
cie1000SnmpConfigGlobalsMode = _Cie1000SnmpConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 1, 1),
    _Cie1000SnmpConfigGlobalsMode_Type()
)
cie1000SnmpConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigGlobalsMode.setStatus("current")


class _Cie1000SnmpConfigGlobalsEngineId_Type(OctetString):
    """Custom type cie1000SnmpConfigGlobalsEngineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Cie1000SnmpConfigGlobalsEngineId_Type.__name__ = "OctetString"
_Cie1000SnmpConfigGlobalsEngineId_Object = MibScalar
cie1000SnmpConfigGlobalsEngineId = _Cie1000SnmpConfigGlobalsEngineId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 1, 5),
    _Cie1000SnmpConfigGlobalsEngineId_Type()
)
cie1000SnmpConfigGlobalsEngineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigGlobalsEngineId.setStatus("current")
_Cie1000SnmpConfigCommunityTable_Object = MibTable
cie1000SnmpConfigCommunityTable = _Cie1000SnmpConfigCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityTable.setStatus("current")
_Cie1000SnmpConfigCommunityEntry_Object = MibTableRow
cie1000SnmpConfigCommunityEntry = _Cie1000SnmpConfigCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 2, 1)
)
cie1000SnmpConfigCommunityEntry.setIndexNames(
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunityName"),
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunitySourceIP"),
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunitySourceIPPrefixSize"),
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityEntry.setStatus("current")


class _Cie1000SnmpConfigCommunityName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigCommunityName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigCommunityName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigCommunityName_Object = MibTableColumn
cie1000SnmpConfigCommunityName = _Cie1000SnmpConfigCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 2, 1, 1),
    _Cie1000SnmpConfigCommunityName_Type()
)
cie1000SnmpConfigCommunityName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityName.setStatus("current")
_Cie1000SnmpConfigCommunitySourceIP_Type = IpAddress
_Cie1000SnmpConfigCommunitySourceIP_Object = MibTableColumn
cie1000SnmpConfigCommunitySourceIP = _Cie1000SnmpConfigCommunitySourceIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 2, 1, 2),
    _Cie1000SnmpConfigCommunitySourceIP_Type()
)
cie1000SnmpConfigCommunitySourceIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunitySourceIP.setStatus("current")


class _Cie1000SnmpConfigCommunitySourceIPPrefixSize_Type(Integer32):
    """Custom type cie1000SnmpConfigCommunitySourceIPPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Cie1000SnmpConfigCommunitySourceIPPrefixSize_Type.__name__ = "Integer32"
_Cie1000SnmpConfigCommunitySourceIPPrefixSize_Object = MibTableColumn
cie1000SnmpConfigCommunitySourceIPPrefixSize = _Cie1000SnmpConfigCommunitySourceIPPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 2, 1, 3),
    _Cie1000SnmpConfigCommunitySourceIPPrefixSize_Type()
)
cie1000SnmpConfigCommunitySourceIPPrefixSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunitySourceIPPrefixSize.setStatus("current")
_Cie1000SnmpConfigCommunitySecret_Type = CIE1000DisplayString
_Cie1000SnmpConfigCommunitySecret_Object = MibTableColumn
cie1000SnmpConfigCommunitySecret = _Cie1000SnmpConfigCommunitySecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 2, 1, 4),
    _Cie1000SnmpConfigCommunitySecret_Type()
)
cie1000SnmpConfigCommunitySecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunitySecret.setStatus("current")
_Cie1000SnmpConfigCommunityAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigCommunityAction_Object = MibTableColumn
cie1000SnmpConfigCommunityAction = _Cie1000SnmpConfigCommunityAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 2, 1, 100),
    _Cie1000SnmpConfigCommunityAction_Type()
)
cie1000SnmpConfigCommunityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityAction.setStatus("current")
_Cie1000SnmpConfigCommunityTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000SnmpConfigCommunityTableRowEditor = _Cie1000SnmpConfigCommunityTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 3)
)


class _Cie1000SnmpConfigCommunityTableRowEditorName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigCommunityTableRowEditorName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigCommunityTableRowEditorName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigCommunityTableRowEditorName_Object = MibScalar
cie1000SnmpConfigCommunityTableRowEditorName = _Cie1000SnmpConfigCommunityTableRowEditorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 3, 1),
    _Cie1000SnmpConfigCommunityTableRowEditorName_Type()
)
cie1000SnmpConfigCommunityTableRowEditorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityTableRowEditorName.setStatus("current")
_Cie1000SnmpConfigCommunityTableRowEditorSourceIP_Type = IpAddress
_Cie1000SnmpConfigCommunityTableRowEditorSourceIP_Object = MibScalar
cie1000SnmpConfigCommunityTableRowEditorSourceIP = _Cie1000SnmpConfigCommunityTableRowEditorSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 3, 2),
    _Cie1000SnmpConfigCommunityTableRowEditorSourceIP_Type()
)
cie1000SnmpConfigCommunityTableRowEditorSourceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityTableRowEditorSourceIP.setStatus("current")


class _Cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize_Type(Integer32):
    """Custom type cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize_Type.__name__ = "Integer32"
_Cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize_Object = MibScalar
cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize = _Cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 3, 3),
    _Cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize_Type()
)
cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize.setStatus("current")
_Cie1000SnmpConfigCommunityTableRowEditorSecret_Type = CIE1000DisplayString
_Cie1000SnmpConfigCommunityTableRowEditorSecret_Object = MibScalar
cie1000SnmpConfigCommunityTableRowEditorSecret = _Cie1000SnmpConfigCommunityTableRowEditorSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 3, 4),
    _Cie1000SnmpConfigCommunityTableRowEditorSecret_Type()
)
cie1000SnmpConfigCommunityTableRowEditorSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityTableRowEditorSecret.setStatus("current")
_Cie1000SnmpConfigCommunityTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigCommunityTableRowEditorAction_Object = MibScalar
cie1000SnmpConfigCommunityTableRowEditorAction = _Cie1000SnmpConfigCommunityTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 3, 100),
    _Cie1000SnmpConfigCommunityTableRowEditorAction_Type()
)
cie1000SnmpConfigCommunityTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityTableRowEditorAction.setStatus("current")
_Cie1000SnmpConfigUserTable_Object = MibTable
cie1000SnmpConfigUserTable = _Cie1000SnmpConfigUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTable.setStatus("current")
_Cie1000SnmpConfigUserEntry_Object = MibTableRow
cie1000SnmpConfigUserEntry = _Cie1000SnmpConfigUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 4, 1)
)
cie1000SnmpConfigUserEntry.setIndexNames(
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigUserEngineId"),
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigUserUserName"),
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserEntry.setStatus("current")


class _Cie1000SnmpConfigUserEngineId_Type(OctetString):
    """Custom type cie1000SnmpConfigUserEngineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Cie1000SnmpConfigUserEngineId_Type.__name__ = "OctetString"
_Cie1000SnmpConfigUserEngineId_Object = MibTableColumn
cie1000SnmpConfigUserEngineId = _Cie1000SnmpConfigUserEngineId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 4, 1, 1),
    _Cie1000SnmpConfigUserEngineId_Type()
)
cie1000SnmpConfigUserEngineId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserEngineId.setStatus("current")


class _Cie1000SnmpConfigUserUserName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigUserUserName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigUserUserName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigUserUserName_Object = MibTableColumn
cie1000SnmpConfigUserUserName = _Cie1000SnmpConfigUserUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 4, 1, 2),
    _Cie1000SnmpConfigUserUserName_Type()
)
cie1000SnmpConfigUserUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserUserName.setStatus("current")
_Cie1000SnmpConfigUserSecurityLevel_Type = CIE1000SnmpSecurityLevel
_Cie1000SnmpConfigUserSecurityLevel_Object = MibTableColumn
cie1000SnmpConfigUserSecurityLevel = _Cie1000SnmpConfigUserSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 4, 1, 3),
    _Cie1000SnmpConfigUserSecurityLevel_Type()
)
cie1000SnmpConfigUserSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserSecurityLevel.setStatus("current")
_Cie1000SnmpConfigUserAuthProtocol_Type = CIE1000SnmpAuthProtocl
_Cie1000SnmpConfigUserAuthProtocol_Object = MibTableColumn
cie1000SnmpConfigUserAuthProtocol = _Cie1000SnmpConfigUserAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 4, 1, 4),
    _Cie1000SnmpConfigUserAuthProtocol_Type()
)
cie1000SnmpConfigUserAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserAuthProtocol.setStatus("current")
_Cie1000SnmpConfigUserAuthPassword_Type = CIE1000DisplayString
_Cie1000SnmpConfigUserAuthPassword_Object = MibTableColumn
cie1000SnmpConfigUserAuthPassword = _Cie1000SnmpConfigUserAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 4, 1, 5),
    _Cie1000SnmpConfigUserAuthPassword_Type()
)
cie1000SnmpConfigUserAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserAuthPassword.setStatus("current")
_Cie1000SnmpConfigUserPrivProtocol_Type = CIE1000SnmpPrivProtocl
_Cie1000SnmpConfigUserPrivProtocol_Object = MibTableColumn
cie1000SnmpConfigUserPrivProtocol = _Cie1000SnmpConfigUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 4, 1, 6),
    _Cie1000SnmpConfigUserPrivProtocol_Type()
)
cie1000SnmpConfigUserPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserPrivProtocol.setStatus("current")
_Cie1000SnmpConfigUserPrivPassword_Type = CIE1000DisplayString
_Cie1000SnmpConfigUserPrivPassword_Object = MibTableColumn
cie1000SnmpConfigUserPrivPassword = _Cie1000SnmpConfigUserPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 4, 1, 7),
    _Cie1000SnmpConfigUserPrivPassword_Type()
)
cie1000SnmpConfigUserPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserPrivPassword.setStatus("current")
_Cie1000SnmpConfigUserAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigUserAction_Object = MibTableColumn
cie1000SnmpConfigUserAction = _Cie1000SnmpConfigUserAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 4, 1, 100),
    _Cie1000SnmpConfigUserAction_Type()
)
cie1000SnmpConfigUserAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserAction.setStatus("current")
_Cie1000SnmpConfigUserTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000SnmpConfigUserTableRowEditor = _Cie1000SnmpConfigUserTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 5)
)


class _Cie1000SnmpConfigUserTableRowEditorEngineId_Type(OctetString):
    """Custom type cie1000SnmpConfigUserTableRowEditorEngineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Cie1000SnmpConfigUserTableRowEditorEngineId_Type.__name__ = "OctetString"
_Cie1000SnmpConfigUserTableRowEditorEngineId_Object = MibScalar
cie1000SnmpConfigUserTableRowEditorEngineId = _Cie1000SnmpConfigUserTableRowEditorEngineId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 5, 1),
    _Cie1000SnmpConfigUserTableRowEditorEngineId_Type()
)
cie1000SnmpConfigUserTableRowEditorEngineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTableRowEditorEngineId.setStatus("current")


class _Cie1000SnmpConfigUserTableRowEditorUserName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigUserTableRowEditorUserName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigUserTableRowEditorUserName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigUserTableRowEditorUserName_Object = MibScalar
cie1000SnmpConfigUserTableRowEditorUserName = _Cie1000SnmpConfigUserTableRowEditorUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 5, 2),
    _Cie1000SnmpConfigUserTableRowEditorUserName_Type()
)
cie1000SnmpConfigUserTableRowEditorUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTableRowEditorUserName.setStatus("current")
_Cie1000SnmpConfigUserTableRowEditorSecurityLevel_Type = CIE1000SnmpSecurityLevel
_Cie1000SnmpConfigUserTableRowEditorSecurityLevel_Object = MibScalar
cie1000SnmpConfigUserTableRowEditorSecurityLevel = _Cie1000SnmpConfigUserTableRowEditorSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 5, 3),
    _Cie1000SnmpConfigUserTableRowEditorSecurityLevel_Type()
)
cie1000SnmpConfigUserTableRowEditorSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTableRowEditorSecurityLevel.setStatus("current")
_Cie1000SnmpConfigUserTableRowEditorAuthProtocol_Type = CIE1000SnmpAuthProtocl
_Cie1000SnmpConfigUserTableRowEditorAuthProtocol_Object = MibScalar
cie1000SnmpConfigUserTableRowEditorAuthProtocol = _Cie1000SnmpConfigUserTableRowEditorAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 5, 4),
    _Cie1000SnmpConfigUserTableRowEditorAuthProtocol_Type()
)
cie1000SnmpConfigUserTableRowEditorAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTableRowEditorAuthProtocol.setStatus("current")
_Cie1000SnmpConfigUserTableRowEditorAuthPassword_Type = CIE1000DisplayString
_Cie1000SnmpConfigUserTableRowEditorAuthPassword_Object = MibScalar
cie1000SnmpConfigUserTableRowEditorAuthPassword = _Cie1000SnmpConfigUserTableRowEditorAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 5, 5),
    _Cie1000SnmpConfigUserTableRowEditorAuthPassword_Type()
)
cie1000SnmpConfigUserTableRowEditorAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTableRowEditorAuthPassword.setStatus("current")
_Cie1000SnmpConfigUserTableRowEditorPrivProtocol_Type = CIE1000SnmpPrivProtocl
_Cie1000SnmpConfigUserTableRowEditorPrivProtocol_Object = MibScalar
cie1000SnmpConfigUserTableRowEditorPrivProtocol = _Cie1000SnmpConfigUserTableRowEditorPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 5, 6),
    _Cie1000SnmpConfigUserTableRowEditorPrivProtocol_Type()
)
cie1000SnmpConfigUserTableRowEditorPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTableRowEditorPrivProtocol.setStatus("current")
_Cie1000SnmpConfigUserTableRowEditorPrivPassword_Type = CIE1000DisplayString
_Cie1000SnmpConfigUserTableRowEditorPrivPassword_Object = MibScalar
cie1000SnmpConfigUserTableRowEditorPrivPassword = _Cie1000SnmpConfigUserTableRowEditorPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 5, 7),
    _Cie1000SnmpConfigUserTableRowEditorPrivPassword_Type()
)
cie1000SnmpConfigUserTableRowEditorPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTableRowEditorPrivPassword.setStatus("current")
_Cie1000SnmpConfigUserTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigUserTableRowEditorAction_Object = MibScalar
cie1000SnmpConfigUserTableRowEditorAction = _Cie1000SnmpConfigUserTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 5, 100),
    _Cie1000SnmpConfigUserTableRowEditorAction_Type()
)
cie1000SnmpConfigUserTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTableRowEditorAction.setStatus("current")
_Cie1000SnmpConfigUserToAccessGroupTable_Object = MibTable
cie1000SnmpConfigUserToAccessGroupTable = _Cie1000SnmpConfigUserToAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupTable.setStatus("current")
_Cie1000SnmpConfigUserToAccessGroupEntry_Object = MibTableRow
cie1000SnmpConfigUserToAccessGroupEntry = _Cie1000SnmpConfigUserToAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 6, 1)
)
cie1000SnmpConfigUserToAccessGroupEntry.setIndexNames(
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupSecurityModel"),
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupUserOrCommunity"),
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupEntry.setStatus("current")
_Cie1000SnmpConfigUserToAccessGroupSecurityModel_Type = CIE1000SnmpSecurityModel
_Cie1000SnmpConfigUserToAccessGroupSecurityModel_Object = MibTableColumn
cie1000SnmpConfigUserToAccessGroupSecurityModel = _Cie1000SnmpConfigUserToAccessGroupSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 6, 1, 1),
    _Cie1000SnmpConfigUserToAccessGroupSecurityModel_Type()
)
cie1000SnmpConfigUserToAccessGroupSecurityModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupSecurityModel.setStatus("current")


class _Cie1000SnmpConfigUserToAccessGroupUserOrCommunity_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigUserToAccessGroupUserOrCommunity based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigUserToAccessGroupUserOrCommunity_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigUserToAccessGroupUserOrCommunity_Object = MibTableColumn
cie1000SnmpConfigUserToAccessGroupUserOrCommunity = _Cie1000SnmpConfigUserToAccessGroupUserOrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 6, 1, 2),
    _Cie1000SnmpConfigUserToAccessGroupUserOrCommunity_Type()
)
cie1000SnmpConfigUserToAccessGroupUserOrCommunity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupUserOrCommunity.setStatus("current")


class _Cie1000SnmpConfigUserToAccessGroupAccessGroupName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigUserToAccessGroupAccessGroupName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigUserToAccessGroupAccessGroupName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigUserToAccessGroupAccessGroupName_Object = MibTableColumn
cie1000SnmpConfigUserToAccessGroupAccessGroupName = _Cie1000SnmpConfigUserToAccessGroupAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 6, 1, 3),
    _Cie1000SnmpConfigUserToAccessGroupAccessGroupName_Type()
)
cie1000SnmpConfigUserToAccessGroupAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupAccessGroupName.setStatus("current")
_Cie1000SnmpConfigUserToAccessGroupAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigUserToAccessGroupAction_Object = MibTableColumn
cie1000SnmpConfigUserToAccessGroupAction = _Cie1000SnmpConfigUserToAccessGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 6, 1, 100),
    _Cie1000SnmpConfigUserToAccessGroupAction_Type()
)
cie1000SnmpConfigUserToAccessGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupAction.setStatus("current")
_Cie1000SnmpConfigUserToAccessGroupTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000SnmpConfigUserToAccessGroupTableRowEditor = _Cie1000SnmpConfigUserToAccessGroupTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 7)
)
_Cie1000SnmpConfigUserToAccessGroupTableRowEditorSecurityModel_Type = CIE1000SnmpSecurityModel
_Cie1000SnmpConfigUserToAccessGroupTableRowEditorSecurityModel_Object = MibScalar
cie1000SnmpConfigUserToAccessGroupTableRowEditorSecurityModel = _Cie1000SnmpConfigUserToAccessGroupTableRowEditorSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 7, 1),
    _Cie1000SnmpConfigUserToAccessGroupTableRowEditorSecurityModel_Type()
)
cie1000SnmpConfigUserToAccessGroupTableRowEditorSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupTableRowEditorSecurityModel.setStatus("current")


class _Cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity_Object = MibScalar
cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity = _Cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 7, 2),
    _Cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity_Type()
)
cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity.setStatus("current")


class _Cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName_Object = MibScalar
cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName = _Cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 7, 3),
    _Cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName_Type()
)
cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName.setStatus("current")
_Cie1000SnmpConfigUserToAccessGroupTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigUserToAccessGroupTableRowEditorAction_Object = MibScalar
cie1000SnmpConfigUserToAccessGroupTableRowEditorAction = _Cie1000SnmpConfigUserToAccessGroupTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 7, 100),
    _Cie1000SnmpConfigUserToAccessGroupTableRowEditorAction_Type()
)
cie1000SnmpConfigUserToAccessGroupTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupTableRowEditorAction.setStatus("current")
_Cie1000SnmpConfigAccessGroupTable_Object = MibTable
cie1000SnmpConfigAccessGroupTable = _Cie1000SnmpConfigAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupTable.setStatus("current")
_Cie1000SnmpConfigAccessGroupEntry_Object = MibTableRow
cie1000SnmpConfigAccessGroupEntry = _Cie1000SnmpConfigAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 8, 1)
)
cie1000SnmpConfigAccessGroupEntry.setIndexNames(
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupAccessGroupName"),
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupSecurityModel"),
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupSecurityLevel"),
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupEntry.setStatus("current")


class _Cie1000SnmpConfigAccessGroupAccessGroupName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigAccessGroupAccessGroupName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigAccessGroupAccessGroupName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigAccessGroupAccessGroupName_Object = MibTableColumn
cie1000SnmpConfigAccessGroupAccessGroupName = _Cie1000SnmpConfigAccessGroupAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 8, 1, 1),
    _Cie1000SnmpConfigAccessGroupAccessGroupName_Type()
)
cie1000SnmpConfigAccessGroupAccessGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupAccessGroupName.setStatus("current")
_Cie1000SnmpConfigAccessGroupSecurityModel_Type = CIE1000SnmpSecurityModel
_Cie1000SnmpConfigAccessGroupSecurityModel_Object = MibTableColumn
cie1000SnmpConfigAccessGroupSecurityModel = _Cie1000SnmpConfigAccessGroupSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 8, 1, 2),
    _Cie1000SnmpConfigAccessGroupSecurityModel_Type()
)
cie1000SnmpConfigAccessGroupSecurityModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupSecurityModel.setStatus("current")
_Cie1000SnmpConfigAccessGroupSecurityLevel_Type = CIE1000SnmpSecurityLevel
_Cie1000SnmpConfigAccessGroupSecurityLevel_Object = MibTableColumn
cie1000SnmpConfigAccessGroupSecurityLevel = _Cie1000SnmpConfigAccessGroupSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 8, 1, 3),
    _Cie1000SnmpConfigAccessGroupSecurityLevel_Type()
)
cie1000SnmpConfigAccessGroupSecurityLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupSecurityLevel.setStatus("current")


class _Cie1000SnmpConfigAccessGroupReadViewName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigAccessGroupReadViewName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigAccessGroupReadViewName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigAccessGroupReadViewName_Object = MibTableColumn
cie1000SnmpConfigAccessGroupReadViewName = _Cie1000SnmpConfigAccessGroupReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 8, 1, 4),
    _Cie1000SnmpConfigAccessGroupReadViewName_Type()
)
cie1000SnmpConfigAccessGroupReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupReadViewName.setStatus("current")


class _Cie1000SnmpConfigAccessGroupWriteViewName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigAccessGroupWriteViewName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigAccessGroupWriteViewName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigAccessGroupWriteViewName_Object = MibTableColumn
cie1000SnmpConfigAccessGroupWriteViewName = _Cie1000SnmpConfigAccessGroupWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 8, 1, 5),
    _Cie1000SnmpConfigAccessGroupWriteViewName_Type()
)
cie1000SnmpConfigAccessGroupWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupWriteViewName.setStatus("current")
_Cie1000SnmpConfigAccessGroupAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigAccessGroupAction_Object = MibTableColumn
cie1000SnmpConfigAccessGroupAction = _Cie1000SnmpConfigAccessGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 8, 1, 100),
    _Cie1000SnmpConfigAccessGroupAction_Type()
)
cie1000SnmpConfigAccessGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupAction.setStatus("current")
_Cie1000SnmpConfigAccessGroupTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000SnmpConfigAccessGroupTableRowEditor = _Cie1000SnmpConfigAccessGroupTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 9)
)


class _Cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName_Object = MibScalar
cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName = _Cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 9, 1),
    _Cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName_Type()
)
cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName.setStatus("current")
_Cie1000SnmpConfigAccessGroupTableRowEditorSecurityModel_Type = CIE1000SnmpSecurityModel
_Cie1000SnmpConfigAccessGroupTableRowEditorSecurityModel_Object = MibScalar
cie1000SnmpConfigAccessGroupTableRowEditorSecurityModel = _Cie1000SnmpConfigAccessGroupTableRowEditorSecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 9, 2),
    _Cie1000SnmpConfigAccessGroupTableRowEditorSecurityModel_Type()
)
cie1000SnmpConfigAccessGroupTableRowEditorSecurityModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupTableRowEditorSecurityModel.setStatus("current")
_Cie1000SnmpConfigAccessGroupTableRowEditorSecurityLevel_Type = CIE1000SnmpSecurityLevel
_Cie1000SnmpConfigAccessGroupTableRowEditorSecurityLevel_Object = MibScalar
cie1000SnmpConfigAccessGroupTableRowEditorSecurityLevel = _Cie1000SnmpConfigAccessGroupTableRowEditorSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 9, 3),
    _Cie1000SnmpConfigAccessGroupTableRowEditorSecurityLevel_Type()
)
cie1000SnmpConfigAccessGroupTableRowEditorSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupTableRowEditorSecurityLevel.setStatus("current")


class _Cie1000SnmpConfigAccessGroupTableRowEditorReadViewName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigAccessGroupTableRowEditorReadViewName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigAccessGroupTableRowEditorReadViewName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigAccessGroupTableRowEditorReadViewName_Object = MibScalar
cie1000SnmpConfigAccessGroupTableRowEditorReadViewName = _Cie1000SnmpConfigAccessGroupTableRowEditorReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 9, 4),
    _Cie1000SnmpConfigAccessGroupTableRowEditorReadViewName_Type()
)
cie1000SnmpConfigAccessGroupTableRowEditorReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupTableRowEditorReadViewName.setStatus("current")


class _Cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName_Object = MibScalar
cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName = _Cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 9, 5),
    _Cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName_Type()
)
cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName.setStatus("current")
_Cie1000SnmpConfigAccessGroupTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigAccessGroupTableRowEditorAction_Object = MibScalar
cie1000SnmpConfigAccessGroupTableRowEditorAction = _Cie1000SnmpConfigAccessGroupTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 9, 100),
    _Cie1000SnmpConfigAccessGroupTableRowEditorAction_Type()
)
cie1000SnmpConfigAccessGroupTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupTableRowEditorAction.setStatus("current")
_Cie1000SnmpConfigViewTable_Object = MibTable
cie1000SnmpConfigViewTable = _Cie1000SnmpConfigViewTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewTable.setStatus("current")
_Cie1000SnmpConfigViewEntry_Object = MibTableRow
cie1000SnmpConfigViewEntry = _Cie1000SnmpConfigViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 10, 1)
)
cie1000SnmpConfigViewEntry.setIndexNames(
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigViewName"),
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigViewSubtree"),
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewEntry.setStatus("current")


class _Cie1000SnmpConfigViewName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigViewName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigViewName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigViewName_Object = MibTableColumn
cie1000SnmpConfigViewName = _Cie1000SnmpConfigViewName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 10, 1, 1),
    _Cie1000SnmpConfigViewName_Type()
)
cie1000SnmpConfigViewName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewName.setStatus("current")


class _Cie1000SnmpConfigViewSubtree_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigViewSubtree based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000SnmpConfigViewSubtree_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigViewSubtree_Object = MibTableColumn
cie1000SnmpConfigViewSubtree = _Cie1000SnmpConfigViewSubtree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 10, 1, 2),
    _Cie1000SnmpConfigViewSubtree_Type()
)
cie1000SnmpConfigViewSubtree.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewSubtree.setStatus("current")
_Cie1000SnmpConfigViewViewType_Type = CIE1000SnmpViewType
_Cie1000SnmpConfigViewViewType_Object = MibTableColumn
cie1000SnmpConfigViewViewType = _Cie1000SnmpConfigViewViewType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 10, 1, 3),
    _Cie1000SnmpConfigViewViewType_Type()
)
cie1000SnmpConfigViewViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewViewType.setStatus("current")
_Cie1000SnmpConfigViewAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigViewAction_Object = MibTableColumn
cie1000SnmpConfigViewAction = _Cie1000SnmpConfigViewAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 10, 1, 100),
    _Cie1000SnmpConfigViewAction_Type()
)
cie1000SnmpConfigViewAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewAction.setStatus("current")
_Cie1000SnmpConfigViewTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000SnmpConfigViewTableRowEditor = _Cie1000SnmpConfigViewTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 11)
)


class _Cie1000SnmpConfigViewTableRowEditorName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigViewTableRowEditorName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigViewTableRowEditorName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigViewTableRowEditorName_Object = MibScalar
cie1000SnmpConfigViewTableRowEditorName = _Cie1000SnmpConfigViewTableRowEditorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 11, 1),
    _Cie1000SnmpConfigViewTableRowEditorName_Type()
)
cie1000SnmpConfigViewTableRowEditorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewTableRowEditorName.setStatus("current")


class _Cie1000SnmpConfigViewTableRowEditorSubtree_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigViewTableRowEditorSubtree based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000SnmpConfigViewTableRowEditorSubtree_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigViewTableRowEditorSubtree_Object = MibScalar
cie1000SnmpConfigViewTableRowEditorSubtree = _Cie1000SnmpConfigViewTableRowEditorSubtree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 11, 2),
    _Cie1000SnmpConfigViewTableRowEditorSubtree_Type()
)
cie1000SnmpConfigViewTableRowEditorSubtree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewTableRowEditorSubtree.setStatus("current")
_Cie1000SnmpConfigViewTableRowEditorViewType_Type = CIE1000SnmpViewType
_Cie1000SnmpConfigViewTableRowEditorViewType_Object = MibScalar
cie1000SnmpConfigViewTableRowEditorViewType = _Cie1000SnmpConfigViewTableRowEditorViewType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 11, 3),
    _Cie1000SnmpConfigViewTableRowEditorViewType_Type()
)
cie1000SnmpConfigViewTableRowEditorViewType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewTableRowEditorViewType.setStatus("current")
_Cie1000SnmpConfigViewTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigViewTableRowEditorAction_Object = MibScalar
cie1000SnmpConfigViewTableRowEditorAction = _Cie1000SnmpConfigViewTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 11, 100),
    _Cie1000SnmpConfigViewTableRowEditorAction_Type()
)
cie1000SnmpConfigViewTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewTableRowEditorAction.setStatus("current")
_Cie1000SnmpConfigCommunity6Table_Object = MibTable
cie1000SnmpConfigCommunity6Table = _Cie1000SnmpConfigCommunity6Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6Table.setStatus("current")
_Cie1000SnmpConfigCommunity6Entry_Object = MibTableRow
cie1000SnmpConfigCommunity6Entry = _Cie1000SnmpConfigCommunity6Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 12, 1)
)
cie1000SnmpConfigCommunity6Entry.setIndexNames(
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6Name"),
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6SourceIPv6"),
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6SourceIPv6PrefixSize"),
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6Entry.setStatus("current")


class _Cie1000SnmpConfigCommunity6Name_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigCommunity6Name based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigCommunity6Name_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigCommunity6Name_Object = MibTableColumn
cie1000SnmpConfigCommunity6Name = _Cie1000SnmpConfigCommunity6Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 12, 1, 1),
    _Cie1000SnmpConfigCommunity6Name_Type()
)
cie1000SnmpConfigCommunity6Name.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6Name.setStatus("current")
_Cie1000SnmpConfigCommunity6SourceIPv6_Type = InetAddressIPv6
_Cie1000SnmpConfigCommunity6SourceIPv6_Object = MibTableColumn
cie1000SnmpConfigCommunity6SourceIPv6 = _Cie1000SnmpConfigCommunity6SourceIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 12, 1, 2),
    _Cie1000SnmpConfigCommunity6SourceIPv6_Type()
)
cie1000SnmpConfigCommunity6SourceIPv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6SourceIPv6.setStatus("current")


class _Cie1000SnmpConfigCommunity6SourceIPv6PrefixSize_Type(Integer32):
    """Custom type cie1000SnmpConfigCommunity6SourceIPv6PrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cie1000SnmpConfigCommunity6SourceIPv6PrefixSize_Type.__name__ = "Integer32"
_Cie1000SnmpConfigCommunity6SourceIPv6PrefixSize_Object = MibTableColumn
cie1000SnmpConfigCommunity6SourceIPv6PrefixSize = _Cie1000SnmpConfigCommunity6SourceIPv6PrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 12, 1, 3),
    _Cie1000SnmpConfigCommunity6SourceIPv6PrefixSize_Type()
)
cie1000SnmpConfigCommunity6SourceIPv6PrefixSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6SourceIPv6PrefixSize.setStatus("current")
_Cie1000SnmpConfigCommunity6Secret_Type = CIE1000DisplayString
_Cie1000SnmpConfigCommunity6Secret_Object = MibTableColumn
cie1000SnmpConfigCommunity6Secret = _Cie1000SnmpConfigCommunity6Secret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 12, 1, 4),
    _Cie1000SnmpConfigCommunity6Secret_Type()
)
cie1000SnmpConfigCommunity6Secret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6Secret.setStatus("current")
_Cie1000SnmpConfigCommunity6Action_Type = CIE1000RowEditorState
_Cie1000SnmpConfigCommunity6Action_Object = MibTableColumn
cie1000SnmpConfigCommunity6Action = _Cie1000SnmpConfigCommunity6Action_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 12, 1, 100),
    _Cie1000SnmpConfigCommunity6Action_Type()
)
cie1000SnmpConfigCommunity6Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6Action.setStatus("current")
_Cie1000SnmpConfigCommunity6TableRowEditor_ObjectIdentity = ObjectIdentity
cie1000SnmpConfigCommunity6TableRowEditor = _Cie1000SnmpConfigCommunity6TableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 13)
)


class _Cie1000SnmpConfigCommunity6TableRowEditorName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigCommunity6TableRowEditorName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigCommunity6TableRowEditorName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigCommunity6TableRowEditorName_Object = MibScalar
cie1000SnmpConfigCommunity6TableRowEditorName = _Cie1000SnmpConfigCommunity6TableRowEditorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 13, 1),
    _Cie1000SnmpConfigCommunity6TableRowEditorName_Type()
)
cie1000SnmpConfigCommunity6TableRowEditorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6TableRowEditorName.setStatus("current")
_Cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6_Type = InetAddressIPv6
_Cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6_Object = MibScalar
cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6 = _Cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 13, 2),
    _Cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6_Type()
)
cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6.setStatus("current")


class _Cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize_Type(Integer32):
    """Custom type cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize_Type.__name__ = "Integer32"
_Cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize_Object = MibScalar
cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize = _Cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 13, 3),
    _Cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize_Type()
)
cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize.setStatus("current")
_Cie1000SnmpConfigCommunity6TableRowEditorSecret_Type = CIE1000DisplayString
_Cie1000SnmpConfigCommunity6TableRowEditorSecret_Object = MibScalar
cie1000SnmpConfigCommunity6TableRowEditorSecret = _Cie1000SnmpConfigCommunity6TableRowEditorSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 13, 4),
    _Cie1000SnmpConfigCommunity6TableRowEditorSecret_Type()
)
cie1000SnmpConfigCommunity6TableRowEditorSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6TableRowEditorSecret.setStatus("current")
_Cie1000SnmpConfigCommunity6TableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigCommunity6TableRowEditorAction_Object = MibScalar
cie1000SnmpConfigCommunity6TableRowEditorAction = _Cie1000SnmpConfigCommunity6TableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 13, 100),
    _Cie1000SnmpConfigCommunity6TableRowEditorAction_Type()
)
cie1000SnmpConfigCommunity6TableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6TableRowEditorAction.setStatus("current")
_Cie1000SnmpConfigTrapReceiverTable_Object = MibTable
cie1000SnmpConfigTrapReceiverTable = _Cie1000SnmpConfigTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20)
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTable.setStatus("current")
_Cie1000SnmpConfigTrapReceiverEntry_Object = MibTableRow
cie1000SnmpConfigTrapReceiverEntry = _Cie1000SnmpConfigTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1)
)
cie1000SnmpConfigTrapReceiverEntry.setIndexNames(
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverName"),
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverEntry.setStatus("current")


class _Cie1000SnmpConfigTrapReceiverName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigTrapReceiverName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigTrapReceiverName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigTrapReceiverName_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverName = _Cie1000SnmpConfigTrapReceiverName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 1),
    _Cie1000SnmpConfigTrapReceiverName_Type()
)
cie1000SnmpConfigTrapReceiverName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverName.setStatus("current")
_Cie1000SnmpConfigTrapReceiverEnable_Type = TruthValue
_Cie1000SnmpConfigTrapReceiverEnable_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverEnable = _Cie1000SnmpConfigTrapReceiverEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 2),
    _Cie1000SnmpConfigTrapReceiverEnable_Type()
)
cie1000SnmpConfigTrapReceiverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverEnable.setStatus("current")
_Cie1000SnmpConfigTrapReceiverAddress_Type = CIE1000InetAddress
_Cie1000SnmpConfigTrapReceiverAddress_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverAddress = _Cie1000SnmpConfigTrapReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 3),
    _Cie1000SnmpConfigTrapReceiverAddress_Type()
)
cie1000SnmpConfigTrapReceiverAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverAddress.setStatus("current")
_Cie1000SnmpConfigTrapReceiverPort_Type = CIE1000Unsigned16
_Cie1000SnmpConfigTrapReceiverPort_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverPort = _Cie1000SnmpConfigTrapReceiverPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 4),
    _Cie1000SnmpConfigTrapReceiverPort_Type()
)
cie1000SnmpConfigTrapReceiverPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverPort.setStatus("current")
_Cie1000SnmpConfigTrapReceiverVersion_Type = CIE1000SnmpVersion
_Cie1000SnmpConfigTrapReceiverVersion_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverVersion = _Cie1000SnmpConfigTrapReceiverVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 5),
    _Cie1000SnmpConfigTrapReceiverVersion_Type()
)
cie1000SnmpConfigTrapReceiverVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverVersion.setStatus("current")
_Cie1000SnmpConfigTrapReceiverCommunity_Type = CIE1000DisplayString
_Cie1000SnmpConfigTrapReceiverCommunity_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverCommunity = _Cie1000SnmpConfigTrapReceiverCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 6),
    _Cie1000SnmpConfigTrapReceiverCommunity_Type()
)
cie1000SnmpConfigTrapReceiverCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverCommunity.setStatus("current")
_Cie1000SnmpConfigTrapReceiverNotifyType_Type = CIE1000SnmpTrapNotifyType
_Cie1000SnmpConfigTrapReceiverNotifyType_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverNotifyType = _Cie1000SnmpConfigTrapReceiverNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 7),
    _Cie1000SnmpConfigTrapReceiverNotifyType_Type()
)
cie1000SnmpConfigTrapReceiverNotifyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverNotifyType.setStatus("current")


class _Cie1000SnmpConfigTrapReceiverTimeout_Type(Integer32):
    """Custom type cie1000SnmpConfigTrapReceiverTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147),
    )


_Cie1000SnmpConfigTrapReceiverTimeout_Type.__name__ = "Integer32"
_Cie1000SnmpConfigTrapReceiverTimeout_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverTimeout = _Cie1000SnmpConfigTrapReceiverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 8),
    _Cie1000SnmpConfigTrapReceiverTimeout_Type()
)
cie1000SnmpConfigTrapReceiverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTimeout.setStatus("current")


class _Cie1000SnmpConfigTrapReceiverRetries_Type(Integer32):
    """Custom type cie1000SnmpConfigTrapReceiverRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cie1000SnmpConfigTrapReceiverRetries_Type.__name__ = "Integer32"
_Cie1000SnmpConfigTrapReceiverRetries_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverRetries = _Cie1000SnmpConfigTrapReceiverRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 9),
    _Cie1000SnmpConfigTrapReceiverRetries_Type()
)
cie1000SnmpConfigTrapReceiverRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverRetries.setStatus("current")


class _Cie1000SnmpConfigTrapReceiverEngineId_Type(OctetString):
    """Custom type cie1000SnmpConfigTrapReceiverEngineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Cie1000SnmpConfigTrapReceiverEngineId_Type.__name__ = "OctetString"
_Cie1000SnmpConfigTrapReceiverEngineId_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverEngineId = _Cie1000SnmpConfigTrapReceiverEngineId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 10),
    _Cie1000SnmpConfigTrapReceiverEngineId_Type()
)
cie1000SnmpConfigTrapReceiverEngineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverEngineId.setStatus("current")


class _Cie1000SnmpConfigTrapReceiverUserName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigTrapReceiverUserName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigTrapReceiverUserName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigTrapReceiverUserName_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverUserName = _Cie1000SnmpConfigTrapReceiverUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 11),
    _Cie1000SnmpConfigTrapReceiverUserName_Type()
)
cie1000SnmpConfigTrapReceiverUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverUserName.setStatus("current")
_Cie1000SnmpConfigTrapReceiverAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigTrapReceiverAction_Object = MibTableColumn
cie1000SnmpConfigTrapReceiverAction = _Cie1000SnmpConfigTrapReceiverAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 20, 1, 100),
    _Cie1000SnmpConfigTrapReceiverAction_Type()
)
cie1000SnmpConfigTrapReceiverAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverAction.setStatus("current")
_Cie1000SnmpConfigTrapReceiverTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000SnmpConfigTrapReceiverTableRowEditor = _Cie1000SnmpConfigTrapReceiverTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21)
)


class _Cie1000SnmpConfigTrapReceiverTableRowEditorName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigTrapReceiverTableRowEditorName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigTrapReceiverTableRowEditorName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigTrapReceiverTableRowEditorName_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorName = _Cie1000SnmpConfigTrapReceiverTableRowEditorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 1),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorName_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorName.setStatus("current")
_Cie1000SnmpConfigTrapReceiverTableRowEditorEnable_Type = TruthValue
_Cie1000SnmpConfigTrapReceiverTableRowEditorEnable_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorEnable = _Cie1000SnmpConfigTrapReceiverTableRowEditorEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 2),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorEnable_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorEnable.setStatus("current")
_Cie1000SnmpConfigTrapReceiverTableRowEditorAddress_Type = CIE1000InetAddress
_Cie1000SnmpConfigTrapReceiverTableRowEditorAddress_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorAddress = _Cie1000SnmpConfigTrapReceiverTableRowEditorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 3),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorAddress_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorAddress.setStatus("current")
_Cie1000SnmpConfigTrapReceiverTableRowEditorPort_Type = CIE1000Unsigned16
_Cie1000SnmpConfigTrapReceiverTableRowEditorPort_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorPort = _Cie1000SnmpConfigTrapReceiverTableRowEditorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 4),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorPort_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorPort.setStatus("current")
_Cie1000SnmpConfigTrapReceiverTableRowEditorVersion_Type = CIE1000SnmpVersion
_Cie1000SnmpConfigTrapReceiverTableRowEditorVersion_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorVersion = _Cie1000SnmpConfigTrapReceiverTableRowEditorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 5),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorVersion_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorVersion.setStatus("current")
_Cie1000SnmpConfigTrapReceiverTableRowEditorCommunity_Type = CIE1000DisplayString
_Cie1000SnmpConfigTrapReceiverTableRowEditorCommunity_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorCommunity = _Cie1000SnmpConfigTrapReceiverTableRowEditorCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 6),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorCommunity_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorCommunity.setStatus("current")
_Cie1000SnmpConfigTrapReceiverTableRowEditorNotifyType_Type = CIE1000SnmpTrapNotifyType
_Cie1000SnmpConfigTrapReceiverTableRowEditorNotifyType_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorNotifyType = _Cie1000SnmpConfigTrapReceiverTableRowEditorNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 7),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorNotifyType_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorNotifyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorNotifyType.setStatus("current")


class _Cie1000SnmpConfigTrapReceiverTableRowEditorTimeout_Type(Integer32):
    """Custom type cie1000SnmpConfigTrapReceiverTableRowEditorTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147),
    )


_Cie1000SnmpConfigTrapReceiverTableRowEditorTimeout_Type.__name__ = "Integer32"
_Cie1000SnmpConfigTrapReceiverTableRowEditorTimeout_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorTimeout = _Cie1000SnmpConfigTrapReceiverTableRowEditorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 8),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorTimeout_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorTimeout.setStatus("current")


class _Cie1000SnmpConfigTrapReceiverTableRowEditorRetries_Type(Integer32):
    """Custom type cie1000SnmpConfigTrapReceiverTableRowEditorRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cie1000SnmpConfigTrapReceiverTableRowEditorRetries_Type.__name__ = "Integer32"
_Cie1000SnmpConfigTrapReceiverTableRowEditorRetries_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorRetries = _Cie1000SnmpConfigTrapReceiverTableRowEditorRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 9),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorRetries_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorRetries.setStatus("current")


class _Cie1000SnmpConfigTrapReceiverTableRowEditorEngineId_Type(OctetString):
    """Custom type cie1000SnmpConfigTrapReceiverTableRowEditorEngineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )


_Cie1000SnmpConfigTrapReceiverTableRowEditorEngineId_Type.__name__ = "OctetString"
_Cie1000SnmpConfigTrapReceiverTableRowEditorEngineId_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorEngineId = _Cie1000SnmpConfigTrapReceiverTableRowEditorEngineId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 10),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorEngineId_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorEngineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorEngineId.setStatus("current")


class _Cie1000SnmpConfigTrapReceiverTableRowEditorUserName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigTrapReceiverTableRowEditorUserName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cie1000SnmpConfigTrapReceiverTableRowEditorUserName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigTrapReceiverTableRowEditorUserName_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorUserName = _Cie1000SnmpConfigTrapReceiverTableRowEditorUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 11),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorUserName_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorUserName.setStatus("current")
_Cie1000SnmpConfigTrapReceiverTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigTrapReceiverTableRowEditorAction_Object = MibScalar
cie1000SnmpConfigTrapReceiverTableRowEditorAction = _Cie1000SnmpConfigTrapReceiverTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 21, 100),
    _Cie1000SnmpConfigTrapReceiverTableRowEditorAction_Type()
)
cie1000SnmpConfigTrapReceiverTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorAction.setStatus("current")
_Cie1000SnmpConfigTrapSourceTable_Object = MibTable
cie1000SnmpConfigTrapSourceTable = _Cie1000SnmpConfigTrapSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 22)
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceTable.setStatus("current")
_Cie1000SnmpConfigTrapSourceEntry_Object = MibTableRow
cie1000SnmpConfigTrapSourceEntry = _Cie1000SnmpConfigTrapSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 22, 1)
)
cie1000SnmpConfigTrapSourceEntry.setIndexNames(
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceName"),
    (0, "CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceIndexFilterID"),
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceEntry.setStatus("current")


class _Cie1000SnmpConfigTrapSourceName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigTrapSourceName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000SnmpConfigTrapSourceName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigTrapSourceName_Object = MibTableColumn
cie1000SnmpConfigTrapSourceName = _Cie1000SnmpConfigTrapSourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 22, 1, 1),
    _Cie1000SnmpConfigTrapSourceName_Type()
)
cie1000SnmpConfigTrapSourceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceName.setStatus("current")


class _Cie1000SnmpConfigTrapSourceIndexFilterID_Type(Integer32):
    """Custom type cie1000SnmpConfigTrapSourceIndexFilterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cie1000SnmpConfigTrapSourceIndexFilterID_Type.__name__ = "Integer32"
_Cie1000SnmpConfigTrapSourceIndexFilterID_Object = MibTableColumn
cie1000SnmpConfigTrapSourceIndexFilterID = _Cie1000SnmpConfigTrapSourceIndexFilterID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 22, 1, 2),
    _Cie1000SnmpConfigTrapSourceIndexFilterID_Type()
)
cie1000SnmpConfigTrapSourceIndexFilterID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceIndexFilterID.setStatus("current")


class _Cie1000SnmpConfigTrapSourceIndexFilter_Type(OctetString):
    """Custom type cie1000SnmpConfigTrapSourceIndexFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 508),
    )


_Cie1000SnmpConfigTrapSourceIndexFilter_Type.__name__ = "OctetString"
_Cie1000SnmpConfigTrapSourceIndexFilter_Object = MibTableColumn
cie1000SnmpConfigTrapSourceIndexFilter = _Cie1000SnmpConfigTrapSourceIndexFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 22, 1, 3),
    _Cie1000SnmpConfigTrapSourceIndexFilter_Type()
)
cie1000SnmpConfigTrapSourceIndexFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceIndexFilter.setStatus("current")


class _Cie1000SnmpConfigTrapSourceIndexMask_Type(OctetString):
    """Custom type cie1000SnmpConfigTrapSourceIndexMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000SnmpConfigTrapSourceIndexMask_Type.__name__ = "OctetString"
_Cie1000SnmpConfigTrapSourceIndexMask_Object = MibTableColumn
cie1000SnmpConfigTrapSourceIndexMask = _Cie1000SnmpConfigTrapSourceIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 22, 1, 4),
    _Cie1000SnmpConfigTrapSourceIndexMask_Type()
)
cie1000SnmpConfigTrapSourceIndexMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceIndexMask.setStatus("current")
_Cie1000SnmpConfigTrapSourceFilterType_Type = CIE1000SnmpViewType
_Cie1000SnmpConfigTrapSourceFilterType_Object = MibTableColumn
cie1000SnmpConfigTrapSourceFilterType = _Cie1000SnmpConfigTrapSourceFilterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 22, 1, 5),
    _Cie1000SnmpConfigTrapSourceFilterType_Type()
)
cie1000SnmpConfigTrapSourceFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceFilterType.setStatus("current")
_Cie1000SnmpConfigTrapSourceAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigTrapSourceAction_Object = MibTableColumn
cie1000SnmpConfigTrapSourceAction = _Cie1000SnmpConfigTrapSourceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 22, 1, 100),
    _Cie1000SnmpConfigTrapSourceAction_Type()
)
cie1000SnmpConfigTrapSourceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceAction.setStatus("current")
_Cie1000SnmpConfigTrapSourceTableRowEditor_ObjectIdentity = ObjectIdentity
cie1000SnmpConfigTrapSourceTableRowEditor = _Cie1000SnmpConfigTrapSourceTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 23)
)


class _Cie1000SnmpConfigTrapSourceTableRowEditorName_Type(CIE1000DisplayString):
    """Custom type cie1000SnmpConfigTrapSourceTableRowEditorName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cie1000SnmpConfigTrapSourceTableRowEditorName_Type.__name__ = "CIE1000DisplayString"
_Cie1000SnmpConfigTrapSourceTableRowEditorName_Object = MibScalar
cie1000SnmpConfigTrapSourceTableRowEditorName = _Cie1000SnmpConfigTrapSourceTableRowEditorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 23, 1),
    _Cie1000SnmpConfigTrapSourceTableRowEditorName_Type()
)
cie1000SnmpConfigTrapSourceTableRowEditorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceTableRowEditorName.setStatus("current")


class _Cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID_Type(Integer32):
    """Custom type cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID_Type.__name__ = "Integer32"
_Cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID_Object = MibScalar
cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID = _Cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 23, 2),
    _Cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID_Type()
)
cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID.setStatus("current")


class _Cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter_Type(OctetString):
    """Custom type cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 508),
    )


_Cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter_Type.__name__ = "OctetString"
_Cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter_Object = MibScalar
cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter = _Cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 23, 3),
    _Cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter_Type()
)
cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter.setStatus("current")


class _Cie1000SnmpConfigTrapSourceTableRowEditorIndexMask_Type(OctetString):
    """Custom type cie1000SnmpConfigTrapSourceTableRowEditorIndexMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cie1000SnmpConfigTrapSourceTableRowEditorIndexMask_Type.__name__ = "OctetString"
_Cie1000SnmpConfigTrapSourceTableRowEditorIndexMask_Object = MibScalar
cie1000SnmpConfigTrapSourceTableRowEditorIndexMask = _Cie1000SnmpConfigTrapSourceTableRowEditorIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 23, 4),
    _Cie1000SnmpConfigTrapSourceTableRowEditorIndexMask_Type()
)
cie1000SnmpConfigTrapSourceTableRowEditorIndexMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceTableRowEditorIndexMask.setStatus("current")
_Cie1000SnmpConfigTrapSourceTableRowEditorFilterType_Type = CIE1000SnmpViewType
_Cie1000SnmpConfigTrapSourceTableRowEditorFilterType_Object = MibScalar
cie1000SnmpConfigTrapSourceTableRowEditorFilterType = _Cie1000SnmpConfigTrapSourceTableRowEditorFilterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 23, 5),
    _Cie1000SnmpConfigTrapSourceTableRowEditorFilterType_Type()
)
cie1000SnmpConfigTrapSourceTableRowEditorFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceTableRowEditorFilterType.setStatus("current")
_Cie1000SnmpConfigTrapSourceTableRowEditorAction_Type = CIE1000RowEditorState
_Cie1000SnmpConfigTrapSourceTableRowEditorAction_Object = MibScalar
cie1000SnmpConfigTrapSourceTableRowEditorAction = _Cie1000SnmpConfigTrapSourceTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 1, 2, 23, 100),
    _Cie1000SnmpConfigTrapSourceTableRowEditorAction_Type()
)
cie1000SnmpConfigTrapSourceTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceTableRowEditorAction.setStatus("current")
_Cie1000SnmpMibConformance_ObjectIdentity = ObjectIdentity
cie1000SnmpMibConformance = _Cie1000SnmpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2)
)
_Cie1000SnmpMibCompliances_ObjectIdentity = ObjectIdentity
cie1000SnmpMibCompliances = _Cie1000SnmpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 1)
)
_Cie1000SnmpMibGroups_ObjectIdentity = ObjectIdentity
cie1000SnmpMibGroups = _Cie1000SnmpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2)
)

# Managed Objects groups

cie1000SnmpConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 1)
)
cie1000SnmpConfigGlobalsInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigGlobalsMode"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigGlobalsEngineId"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigGlobalsInfoGroup.setStatus("current")

cie1000SnmpConfigCommunityTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 2)
)
cie1000SnmpConfigCommunityTableInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunityName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunitySourceIP"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunitySourceIPPrefixSize"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunitySecret"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunityAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityTableInfoGroup.setStatus("current")

cie1000SnmpConfigCommunityTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 3)
)
cie1000SnmpConfigCommunityTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunityTableRowEditorName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunityTableRowEditorSourceIP"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunityTableRowEditorSecret"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunityTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunityTableRowEditorInfoGroup.setStatus("current")

cie1000SnmpConfigUserTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 4)
)
cie1000SnmpConfigUserTableInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserEngineId"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserUserName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserSecurityLevel"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserAuthProtocol"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserAuthPassword"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserPrivProtocol"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserPrivPassword"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTableInfoGroup.setStatus("current")

cie1000SnmpConfigUserTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 5)
)
cie1000SnmpConfigUserTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserTableRowEditorEngineId"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserTableRowEditorUserName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserTableRowEditorSecurityLevel"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserTableRowEditorAuthProtocol"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserTableRowEditorAuthPassword"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserTableRowEditorPrivProtocol"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserTableRowEditorPrivPassword"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserTableRowEditorInfoGroup.setStatus("current")

cie1000SnmpConfigUserToAccessGroupTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 6)
)
cie1000SnmpConfigUserToAccessGroupTableInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupSecurityModel"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupUserOrCommunity"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupAccessGroupName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupTableInfoGroup.setStatus("current")

cie1000SnmpConfigUserToAccessGroupTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 7)
)
cie1000SnmpConfigUserToAccessGroupTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupTableRowEditorSecurityModel"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigUserToAccessGroupTableRowEditorInfoGroup.setStatus("current")

cie1000SnmpConfigAccessGroupTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 8)
)
cie1000SnmpConfigAccessGroupTableInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupAccessGroupName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupSecurityModel"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupSecurityLevel"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupReadViewName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupWriteViewName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupTableInfoGroup.setStatus("current")

cie1000SnmpConfigAccessGroupTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 9)
)
cie1000SnmpConfigAccessGroupTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupTableRowEditorSecurityModel"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupTableRowEditorSecurityLevel"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupTableRowEditorReadViewName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigAccessGroupTableRowEditorInfoGroup.setStatus("current")

cie1000SnmpConfigViewTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 10)
)
cie1000SnmpConfigViewTableInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigViewName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigViewSubtree"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigViewViewType"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigViewAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewTableInfoGroup.setStatus("current")

cie1000SnmpConfigViewTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 11)
)
cie1000SnmpConfigViewTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigViewTableRowEditorName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigViewTableRowEditorSubtree"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigViewTableRowEditorViewType"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigViewTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigViewTableRowEditorInfoGroup.setStatus("current")

cie1000SnmpConfigCommunity6TableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 12)
)
cie1000SnmpConfigCommunity6TableInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6Name"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6SourceIPv6"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6SourceIPv6PrefixSize"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6Secret"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6Action"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6TableInfoGroup.setStatus("current")

cie1000SnmpConfigCommunity6TableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 13)
)
cie1000SnmpConfigCommunity6TableRowEditorInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6TableRowEditorName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6TableRowEditorSecret"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6TableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigCommunity6TableRowEditorInfoGroup.setStatus("current")

cie1000SnmpConfigTrapReceiverTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 14)
)
cie1000SnmpConfigTrapReceiverTableInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverEnable"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverAddress"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverPort"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverVersion"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverCommunity"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverNotifyType"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTimeout"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverRetries"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverEngineId"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverUserName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableInfoGroup.setStatus("current")

cie1000SnmpConfigTrapReceiverTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 15)
)
cie1000SnmpConfigTrapReceiverTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorEnable"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorAddress"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorPort"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorVersion"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorCommunity"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorNotifyType"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorTimeout"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorRetries"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorEngineId"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorUserName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapReceiverTableRowEditorInfoGroup.setStatus("current")

cie1000SnmpConfigTrapSourceTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 16)
)
cie1000SnmpConfigTrapSourceTableInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceIndexFilterID"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceIndexFilter"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceIndexMask"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceFilterType"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceTableInfoGroup.setStatus("current")

cie1000SnmpConfigTrapSourceTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 2, 17)
)
cie1000SnmpConfigTrapSourceTableRowEditorInfoGroup.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceTableRowEditorName"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceTableRowEditorIndexMask"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceTableRowEditorFilterType"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    cie1000SnmpConfigTrapSourceTableRowEditorInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000SnmpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 36, 2, 1, 1)
)
cie1000SnmpMibCompliance.setObjects(
      *(("CIE1000-SNMP-MIB", "cie1000SnmpConfigGlobalsInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunityTableInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunityTableRowEditorInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserTableInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserTableRowEditorInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupTableInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigUserToAccessGroupTableRowEditorInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupTableInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigAccessGroupTableRowEditorInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigViewTableInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigViewTableRowEditorInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6TableInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigCommunity6TableRowEditorInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapReceiverTableRowEditorInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceTableInfoGroup"),
        ("CIE1000-SNMP-MIB", "cie1000SnmpConfigTrapSourceTableRowEditorInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000SnmpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-SNMP-MIB",
    **{"CIE1000SnmpAuthProtocl": CIE1000SnmpAuthProtocl,
       "CIE1000SnmpPrivProtocl": CIE1000SnmpPrivProtocl,
       "CIE1000SnmpSecurityLevel": CIE1000SnmpSecurityLevel,
       "CIE1000SnmpSecurityModel": CIE1000SnmpSecurityModel,
       "CIE1000SnmpTrapNotifyType": CIE1000SnmpTrapNotifyType,
       "CIE1000SnmpVersion": CIE1000SnmpVersion,
       "CIE1000SnmpViewType": CIE1000SnmpViewType,
       "cie1000SnmpMib": cie1000SnmpMib,
       "cie1000SnmpMibObjects": cie1000SnmpMibObjects,
       "cie1000SnmpConfig": cie1000SnmpConfig,
       "cie1000SnmpConfigGlobals": cie1000SnmpConfigGlobals,
       "cie1000SnmpConfigGlobalsMode": cie1000SnmpConfigGlobalsMode,
       "cie1000SnmpConfigGlobalsEngineId": cie1000SnmpConfigGlobalsEngineId,
       "cie1000SnmpConfigCommunityTable": cie1000SnmpConfigCommunityTable,
       "cie1000SnmpConfigCommunityEntry": cie1000SnmpConfigCommunityEntry,
       "cie1000SnmpConfigCommunityName": cie1000SnmpConfigCommunityName,
       "cie1000SnmpConfigCommunitySourceIP": cie1000SnmpConfigCommunitySourceIP,
       "cie1000SnmpConfigCommunitySourceIPPrefixSize": cie1000SnmpConfigCommunitySourceIPPrefixSize,
       "cie1000SnmpConfigCommunitySecret": cie1000SnmpConfigCommunitySecret,
       "cie1000SnmpConfigCommunityAction": cie1000SnmpConfigCommunityAction,
       "cie1000SnmpConfigCommunityTableRowEditor": cie1000SnmpConfigCommunityTableRowEditor,
       "cie1000SnmpConfigCommunityTableRowEditorName": cie1000SnmpConfigCommunityTableRowEditorName,
       "cie1000SnmpConfigCommunityTableRowEditorSourceIP": cie1000SnmpConfigCommunityTableRowEditorSourceIP,
       "cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize": cie1000SnmpConfigCommunityTableRowEditorSourceIPPrefixSize,
       "cie1000SnmpConfigCommunityTableRowEditorSecret": cie1000SnmpConfigCommunityTableRowEditorSecret,
       "cie1000SnmpConfigCommunityTableRowEditorAction": cie1000SnmpConfigCommunityTableRowEditorAction,
       "cie1000SnmpConfigUserTable": cie1000SnmpConfigUserTable,
       "cie1000SnmpConfigUserEntry": cie1000SnmpConfigUserEntry,
       "cie1000SnmpConfigUserEngineId": cie1000SnmpConfigUserEngineId,
       "cie1000SnmpConfigUserUserName": cie1000SnmpConfigUserUserName,
       "cie1000SnmpConfigUserSecurityLevel": cie1000SnmpConfigUserSecurityLevel,
       "cie1000SnmpConfigUserAuthProtocol": cie1000SnmpConfigUserAuthProtocol,
       "cie1000SnmpConfigUserAuthPassword": cie1000SnmpConfigUserAuthPassword,
       "cie1000SnmpConfigUserPrivProtocol": cie1000SnmpConfigUserPrivProtocol,
       "cie1000SnmpConfigUserPrivPassword": cie1000SnmpConfigUserPrivPassword,
       "cie1000SnmpConfigUserAction": cie1000SnmpConfigUserAction,
       "cie1000SnmpConfigUserTableRowEditor": cie1000SnmpConfigUserTableRowEditor,
       "cie1000SnmpConfigUserTableRowEditorEngineId": cie1000SnmpConfigUserTableRowEditorEngineId,
       "cie1000SnmpConfigUserTableRowEditorUserName": cie1000SnmpConfigUserTableRowEditorUserName,
       "cie1000SnmpConfigUserTableRowEditorSecurityLevel": cie1000SnmpConfigUserTableRowEditorSecurityLevel,
       "cie1000SnmpConfigUserTableRowEditorAuthProtocol": cie1000SnmpConfigUserTableRowEditorAuthProtocol,
       "cie1000SnmpConfigUserTableRowEditorAuthPassword": cie1000SnmpConfigUserTableRowEditorAuthPassword,
       "cie1000SnmpConfigUserTableRowEditorPrivProtocol": cie1000SnmpConfigUserTableRowEditorPrivProtocol,
       "cie1000SnmpConfigUserTableRowEditorPrivPassword": cie1000SnmpConfigUserTableRowEditorPrivPassword,
       "cie1000SnmpConfigUserTableRowEditorAction": cie1000SnmpConfigUserTableRowEditorAction,
       "cie1000SnmpConfigUserToAccessGroupTable": cie1000SnmpConfigUserToAccessGroupTable,
       "cie1000SnmpConfigUserToAccessGroupEntry": cie1000SnmpConfigUserToAccessGroupEntry,
       "cie1000SnmpConfigUserToAccessGroupSecurityModel": cie1000SnmpConfigUserToAccessGroupSecurityModel,
       "cie1000SnmpConfigUserToAccessGroupUserOrCommunity": cie1000SnmpConfigUserToAccessGroupUserOrCommunity,
       "cie1000SnmpConfigUserToAccessGroupAccessGroupName": cie1000SnmpConfigUserToAccessGroupAccessGroupName,
       "cie1000SnmpConfigUserToAccessGroupAction": cie1000SnmpConfigUserToAccessGroupAction,
       "cie1000SnmpConfigUserToAccessGroupTableRowEditor": cie1000SnmpConfigUserToAccessGroupTableRowEditor,
       "cie1000SnmpConfigUserToAccessGroupTableRowEditorSecurityModel": cie1000SnmpConfigUserToAccessGroupTableRowEditorSecurityModel,
       "cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity": cie1000SnmpConfigUserToAccessGroupTableRowEditorUserOrCommunity,
       "cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName": cie1000SnmpConfigUserToAccessGroupTableRowEditorAccessGroupName,
       "cie1000SnmpConfigUserToAccessGroupTableRowEditorAction": cie1000SnmpConfigUserToAccessGroupTableRowEditorAction,
       "cie1000SnmpConfigAccessGroupTable": cie1000SnmpConfigAccessGroupTable,
       "cie1000SnmpConfigAccessGroupEntry": cie1000SnmpConfigAccessGroupEntry,
       "cie1000SnmpConfigAccessGroupAccessGroupName": cie1000SnmpConfigAccessGroupAccessGroupName,
       "cie1000SnmpConfigAccessGroupSecurityModel": cie1000SnmpConfigAccessGroupSecurityModel,
       "cie1000SnmpConfigAccessGroupSecurityLevel": cie1000SnmpConfigAccessGroupSecurityLevel,
       "cie1000SnmpConfigAccessGroupReadViewName": cie1000SnmpConfigAccessGroupReadViewName,
       "cie1000SnmpConfigAccessGroupWriteViewName": cie1000SnmpConfigAccessGroupWriteViewName,
       "cie1000SnmpConfigAccessGroupAction": cie1000SnmpConfigAccessGroupAction,
       "cie1000SnmpConfigAccessGroupTableRowEditor": cie1000SnmpConfigAccessGroupTableRowEditor,
       "cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName": cie1000SnmpConfigAccessGroupTableRowEditorAccessGroupName,
       "cie1000SnmpConfigAccessGroupTableRowEditorSecurityModel": cie1000SnmpConfigAccessGroupTableRowEditorSecurityModel,
       "cie1000SnmpConfigAccessGroupTableRowEditorSecurityLevel": cie1000SnmpConfigAccessGroupTableRowEditorSecurityLevel,
       "cie1000SnmpConfigAccessGroupTableRowEditorReadViewName": cie1000SnmpConfigAccessGroupTableRowEditorReadViewName,
       "cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName": cie1000SnmpConfigAccessGroupTableRowEditorWriteViewName,
       "cie1000SnmpConfigAccessGroupTableRowEditorAction": cie1000SnmpConfigAccessGroupTableRowEditorAction,
       "cie1000SnmpConfigViewTable": cie1000SnmpConfigViewTable,
       "cie1000SnmpConfigViewEntry": cie1000SnmpConfigViewEntry,
       "cie1000SnmpConfigViewName": cie1000SnmpConfigViewName,
       "cie1000SnmpConfigViewSubtree": cie1000SnmpConfigViewSubtree,
       "cie1000SnmpConfigViewViewType": cie1000SnmpConfigViewViewType,
       "cie1000SnmpConfigViewAction": cie1000SnmpConfigViewAction,
       "cie1000SnmpConfigViewTableRowEditor": cie1000SnmpConfigViewTableRowEditor,
       "cie1000SnmpConfigViewTableRowEditorName": cie1000SnmpConfigViewTableRowEditorName,
       "cie1000SnmpConfigViewTableRowEditorSubtree": cie1000SnmpConfigViewTableRowEditorSubtree,
       "cie1000SnmpConfigViewTableRowEditorViewType": cie1000SnmpConfigViewTableRowEditorViewType,
       "cie1000SnmpConfigViewTableRowEditorAction": cie1000SnmpConfigViewTableRowEditorAction,
       "cie1000SnmpConfigCommunity6Table": cie1000SnmpConfigCommunity6Table,
       "cie1000SnmpConfigCommunity6Entry": cie1000SnmpConfigCommunity6Entry,
       "cie1000SnmpConfigCommunity6Name": cie1000SnmpConfigCommunity6Name,
       "cie1000SnmpConfigCommunity6SourceIPv6": cie1000SnmpConfigCommunity6SourceIPv6,
       "cie1000SnmpConfigCommunity6SourceIPv6PrefixSize": cie1000SnmpConfigCommunity6SourceIPv6PrefixSize,
       "cie1000SnmpConfigCommunity6Secret": cie1000SnmpConfigCommunity6Secret,
       "cie1000SnmpConfigCommunity6Action": cie1000SnmpConfigCommunity6Action,
       "cie1000SnmpConfigCommunity6TableRowEditor": cie1000SnmpConfigCommunity6TableRowEditor,
       "cie1000SnmpConfigCommunity6TableRowEditorName": cie1000SnmpConfigCommunity6TableRowEditorName,
       "cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6": cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6,
       "cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize": cie1000SnmpConfigCommunity6TableRowEditorSourceIPv6PrefixSize,
       "cie1000SnmpConfigCommunity6TableRowEditorSecret": cie1000SnmpConfigCommunity6TableRowEditorSecret,
       "cie1000SnmpConfigCommunity6TableRowEditorAction": cie1000SnmpConfigCommunity6TableRowEditorAction,
       "cie1000SnmpConfigTrapReceiverTable": cie1000SnmpConfigTrapReceiverTable,
       "cie1000SnmpConfigTrapReceiverEntry": cie1000SnmpConfigTrapReceiverEntry,
       "cie1000SnmpConfigTrapReceiverName": cie1000SnmpConfigTrapReceiverName,
       "cie1000SnmpConfigTrapReceiverEnable": cie1000SnmpConfigTrapReceiverEnable,
       "cie1000SnmpConfigTrapReceiverAddress": cie1000SnmpConfigTrapReceiverAddress,
       "cie1000SnmpConfigTrapReceiverPort": cie1000SnmpConfigTrapReceiverPort,
       "cie1000SnmpConfigTrapReceiverVersion": cie1000SnmpConfigTrapReceiverVersion,
       "cie1000SnmpConfigTrapReceiverCommunity": cie1000SnmpConfigTrapReceiverCommunity,
       "cie1000SnmpConfigTrapReceiverNotifyType": cie1000SnmpConfigTrapReceiverNotifyType,
       "cie1000SnmpConfigTrapReceiverTimeout": cie1000SnmpConfigTrapReceiverTimeout,
       "cie1000SnmpConfigTrapReceiverRetries": cie1000SnmpConfigTrapReceiverRetries,
       "cie1000SnmpConfigTrapReceiverEngineId": cie1000SnmpConfigTrapReceiverEngineId,
       "cie1000SnmpConfigTrapReceiverUserName": cie1000SnmpConfigTrapReceiverUserName,
       "cie1000SnmpConfigTrapReceiverAction": cie1000SnmpConfigTrapReceiverAction,
       "cie1000SnmpConfigTrapReceiverTableRowEditor": cie1000SnmpConfigTrapReceiverTableRowEditor,
       "cie1000SnmpConfigTrapReceiverTableRowEditorName": cie1000SnmpConfigTrapReceiverTableRowEditorName,
       "cie1000SnmpConfigTrapReceiverTableRowEditorEnable": cie1000SnmpConfigTrapReceiverTableRowEditorEnable,
       "cie1000SnmpConfigTrapReceiverTableRowEditorAddress": cie1000SnmpConfigTrapReceiverTableRowEditorAddress,
       "cie1000SnmpConfigTrapReceiverTableRowEditorPort": cie1000SnmpConfigTrapReceiverTableRowEditorPort,
       "cie1000SnmpConfigTrapReceiverTableRowEditorVersion": cie1000SnmpConfigTrapReceiverTableRowEditorVersion,
       "cie1000SnmpConfigTrapReceiverTableRowEditorCommunity": cie1000SnmpConfigTrapReceiverTableRowEditorCommunity,
       "cie1000SnmpConfigTrapReceiverTableRowEditorNotifyType": cie1000SnmpConfigTrapReceiverTableRowEditorNotifyType,
       "cie1000SnmpConfigTrapReceiverTableRowEditorTimeout": cie1000SnmpConfigTrapReceiverTableRowEditorTimeout,
       "cie1000SnmpConfigTrapReceiverTableRowEditorRetries": cie1000SnmpConfigTrapReceiverTableRowEditorRetries,
       "cie1000SnmpConfigTrapReceiverTableRowEditorEngineId": cie1000SnmpConfigTrapReceiverTableRowEditorEngineId,
       "cie1000SnmpConfigTrapReceiverTableRowEditorUserName": cie1000SnmpConfigTrapReceiverTableRowEditorUserName,
       "cie1000SnmpConfigTrapReceiverTableRowEditorAction": cie1000SnmpConfigTrapReceiverTableRowEditorAction,
       "cie1000SnmpConfigTrapSourceTable": cie1000SnmpConfigTrapSourceTable,
       "cie1000SnmpConfigTrapSourceEntry": cie1000SnmpConfigTrapSourceEntry,
       "cie1000SnmpConfigTrapSourceName": cie1000SnmpConfigTrapSourceName,
       "cie1000SnmpConfigTrapSourceIndexFilterID": cie1000SnmpConfigTrapSourceIndexFilterID,
       "cie1000SnmpConfigTrapSourceIndexFilter": cie1000SnmpConfigTrapSourceIndexFilter,
       "cie1000SnmpConfigTrapSourceIndexMask": cie1000SnmpConfigTrapSourceIndexMask,
       "cie1000SnmpConfigTrapSourceFilterType": cie1000SnmpConfigTrapSourceFilterType,
       "cie1000SnmpConfigTrapSourceAction": cie1000SnmpConfigTrapSourceAction,
       "cie1000SnmpConfigTrapSourceTableRowEditor": cie1000SnmpConfigTrapSourceTableRowEditor,
       "cie1000SnmpConfigTrapSourceTableRowEditorName": cie1000SnmpConfigTrapSourceTableRowEditorName,
       "cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID": cie1000SnmpConfigTrapSourceTableRowEditorIndexFilterID,
       "cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter": cie1000SnmpConfigTrapSourceTableRowEditorIndexFilter,
       "cie1000SnmpConfigTrapSourceTableRowEditorIndexMask": cie1000SnmpConfigTrapSourceTableRowEditorIndexMask,
       "cie1000SnmpConfigTrapSourceTableRowEditorFilterType": cie1000SnmpConfigTrapSourceTableRowEditorFilterType,
       "cie1000SnmpConfigTrapSourceTableRowEditorAction": cie1000SnmpConfigTrapSourceTableRowEditorAction,
       "cie1000SnmpMibConformance": cie1000SnmpMibConformance,
       "cie1000SnmpMibCompliances": cie1000SnmpMibCompliances,
       "cie1000SnmpMibCompliance": cie1000SnmpMibCompliance,
       "cie1000SnmpMibGroups": cie1000SnmpMibGroups,
       "cie1000SnmpConfigGlobalsInfoGroup": cie1000SnmpConfigGlobalsInfoGroup,
       "cie1000SnmpConfigCommunityTableInfoGroup": cie1000SnmpConfigCommunityTableInfoGroup,
       "cie1000SnmpConfigCommunityTableRowEditorInfoGroup": cie1000SnmpConfigCommunityTableRowEditorInfoGroup,
       "cie1000SnmpConfigUserTableInfoGroup": cie1000SnmpConfigUserTableInfoGroup,
       "cie1000SnmpConfigUserTableRowEditorInfoGroup": cie1000SnmpConfigUserTableRowEditorInfoGroup,
       "cie1000SnmpConfigUserToAccessGroupTableInfoGroup": cie1000SnmpConfigUserToAccessGroupTableInfoGroup,
       "cie1000SnmpConfigUserToAccessGroupTableRowEditorInfoGroup": cie1000SnmpConfigUserToAccessGroupTableRowEditorInfoGroup,
       "cie1000SnmpConfigAccessGroupTableInfoGroup": cie1000SnmpConfigAccessGroupTableInfoGroup,
       "cie1000SnmpConfigAccessGroupTableRowEditorInfoGroup": cie1000SnmpConfigAccessGroupTableRowEditorInfoGroup,
       "cie1000SnmpConfigViewTableInfoGroup": cie1000SnmpConfigViewTableInfoGroup,
       "cie1000SnmpConfigViewTableRowEditorInfoGroup": cie1000SnmpConfigViewTableRowEditorInfoGroup,
       "cie1000SnmpConfigCommunity6TableInfoGroup": cie1000SnmpConfigCommunity6TableInfoGroup,
       "cie1000SnmpConfigCommunity6TableRowEditorInfoGroup": cie1000SnmpConfigCommunity6TableRowEditorInfoGroup,
       "cie1000SnmpConfigTrapReceiverTableInfoGroup": cie1000SnmpConfigTrapReceiverTableInfoGroup,
       "cie1000SnmpConfigTrapReceiverTableRowEditorInfoGroup": cie1000SnmpConfigTrapReceiverTableRowEditorInfoGroup,
       "cie1000SnmpConfigTrapSourceTableInfoGroup": cie1000SnmpConfigTrapSourceTableInfoGroup,
       "cie1000SnmpConfigTrapSourceTableRowEditorInfoGroup": cie1000SnmpConfigTrapSourceTableRowEditorInfoGroup}
)
