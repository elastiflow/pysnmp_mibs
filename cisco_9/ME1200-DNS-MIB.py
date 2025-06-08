# SNMP MIB module (ME1200-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-DNS-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200Unsigned16,) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200Unsigned16")

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

me1200DnsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53)
)
if mibBuilder.loadTexts:
    me1200DnsMib.setRevisions(
        ("2014-01-29 00:00",
         "2013-10-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200DnsServerType(TextualConvention, Integer32):
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
        *(("dhcp", 0),
          ("none", 1),
          ("static", 2),
          ("dhcpVlan", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200DnsMIBObjects_ObjectIdentity = ObjectIdentity
me1200DnsMIBObjects = _Me1200DnsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1)
)
_Me1200DnsConfig_ObjectIdentity = ObjectIdentity
me1200DnsConfig = _Me1200DnsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2)
)
_Me1200DnsGlobals_ObjectIdentity = ObjectIdentity
me1200DnsGlobals = _Me1200DnsGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2, 1)
)
_Me1200DnsGlobalsServerSetting_Type = ME1200DnsServerType
_Me1200DnsGlobalsServerSetting_Object = MibScalar
me1200DnsGlobalsServerSetting = _Me1200DnsGlobalsServerSetting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2, 1, 1),
    _Me1200DnsGlobalsServerSetting_Type()
)
me1200DnsGlobalsServerSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DnsGlobalsServerSetting.setStatus("current")
_Me1200DnsGlobalsServerStaticAddress_Type = IpAddress
_Me1200DnsGlobalsServerStaticAddress_Object = MibScalar
me1200DnsGlobalsServerStaticAddress = _Me1200DnsGlobalsServerStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2, 1, 2),
    _Me1200DnsGlobalsServerStaticAddress_Type()
)
me1200DnsGlobalsServerStaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DnsGlobalsServerStaticAddress.setStatus("current")
_Me1200DnsGlobalsServerStaticVlanId_Type = ME1200Unsigned16
_Me1200DnsGlobalsServerStaticVlanId_Object = MibScalar
me1200DnsGlobalsServerStaticVlanId = _Me1200DnsGlobalsServerStaticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2, 1, 3),
    _Me1200DnsGlobalsServerStaticVlanId_Type()
)
me1200DnsGlobalsServerStaticVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DnsGlobalsServerStaticVlanId.setStatus("current")
_Me1200DnsGlobalsProxyAdminState_Type = TruthValue
_Me1200DnsGlobalsProxyAdminState_Object = MibScalar
me1200DnsGlobalsProxyAdminState = _Me1200DnsGlobalsProxyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 2, 1, 4),
    _Me1200DnsGlobalsProxyAdminState_Type()
)
me1200DnsGlobalsProxyAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200DnsGlobalsProxyAdminState.setStatus("current")
_Me1200DnsStatus_ObjectIdentity = ObjectIdentity
me1200DnsStatus = _Me1200DnsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 3)
)
_Me1200DnsServerStatus_ObjectIdentity = ObjectIdentity
me1200DnsServerStatus = _Me1200DnsServerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 3, 1)
)
_Me1200DnsServerStatusIpAddress_Type = IpAddress
_Me1200DnsServerStatusIpAddress_Object = MibScalar
me1200DnsServerStatusIpAddress = _Me1200DnsServerStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 1, 3, 1, 1),
    _Me1200DnsServerStatusIpAddress_Type()
)
me1200DnsServerStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200DnsServerStatusIpAddress.setStatus("current")
_Me1200DnsMIBConformance_ObjectIdentity = ObjectIdentity
me1200DnsMIBConformance = _Me1200DnsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2)
)
_Me1200DnsMIBCompliances_ObjectIdentity = ObjectIdentity
me1200DnsMIBCompliances = _Me1200DnsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2, 1)
)
_Me1200DnsMIBGroups_ObjectIdentity = ObjectIdentity
me1200DnsMIBGroups = _Me1200DnsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2, 2)
)

# Managed Objects groups

me1200DnsGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2, 2, 1)
)
me1200DnsGlobalsInfoGroup.setObjects(
      *(("ME1200-DNS-MIB", "me1200DnsGlobalsServerSetting"),
        ("ME1200-DNS-MIB", "me1200DnsGlobalsServerStaticAddress"),
        ("ME1200-DNS-MIB", "me1200DnsGlobalsServerStaticVlanId"),
        ("ME1200-DNS-MIB", "me1200DnsGlobalsProxyAdminState"))
)
if mibBuilder.loadTexts:
    me1200DnsGlobalsInfoGroup.setStatus("current")

me1200DnsServerStatusInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2, 2, 2)
)
me1200DnsServerStatusInfoGroup.setObjects(
    ("ME1200-DNS-MIB", "me1200DnsServerStatusIpAddress")
)
if mibBuilder.loadTexts:
    me1200DnsServerStatusInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200DnsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 53, 2, 1, 1)
)
me1200DnsMibCompliance.setObjects(
      *(("ME1200-DNS-MIB", "me1200DnsGlobalsInfoGroup"),
        ("ME1200-DNS-MIB", "me1200DnsServerStatusInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200DnsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-DNS-MIB",
    **{"ME1200DnsServerType": ME1200DnsServerType,
       "me1200DnsMib": me1200DnsMib,
       "me1200DnsMIBObjects": me1200DnsMIBObjects,
       "me1200DnsConfig": me1200DnsConfig,
       "me1200DnsGlobals": me1200DnsGlobals,
       "me1200DnsGlobalsServerSetting": me1200DnsGlobalsServerSetting,
       "me1200DnsGlobalsServerStaticAddress": me1200DnsGlobalsServerStaticAddress,
       "me1200DnsGlobalsServerStaticVlanId": me1200DnsGlobalsServerStaticVlanId,
       "me1200DnsGlobalsProxyAdminState": me1200DnsGlobalsProxyAdminState,
       "me1200DnsStatus": me1200DnsStatus,
       "me1200DnsServerStatus": me1200DnsServerStatus,
       "me1200DnsServerStatusIpAddress": me1200DnsServerStatusIpAddress,
       "me1200DnsMIBConformance": me1200DnsMIBConformance,
       "me1200DnsMIBCompliances": me1200DnsMIBCompliances,
       "me1200DnsMibCompliance": me1200DnsMibCompliance,
       "me1200DnsMIBGroups": me1200DnsMIBGroups,
       "me1200DnsGlobalsInfoGroup": me1200DnsGlobalsInfoGroup,
       "me1200DnsServerStatusInfoGroup": me1200DnsServerStatusInfoGroup}
)
